"""Finite independent checks for Ising antiferromagnet on a triangular strip.
Usage: python verify.py   (Python 3 with SymPy installed)
"""
from collections import Counter
from itertools import product
from math import isclose
import sympy as sp

R = list(product((0, 1), repeat=2))
S = [(a,b) for a in range(4) for b in range(4)]
I = {s:i for i,s in enumerate(S)}

def local_ok(a,b,c,strict=False):
    t = [a[0],c[0],b[1],c[1]]
    d = [a[1],c[1],b[0],a[0]]
    k = 3 if strict else 2
    return sum(x != b[0] for x in t) >= k and sum(x != b[1] for x in d) >= k

def frustr(b,c):
    return sum(x == y for x,y in ((b[0],b[1]),(b[0],c[0]),(b[1],c[1]),(b[0],c[1])))

def transfer_energy(n, strict=False):
    # Graphical loop-count on the 16-state de Bruijn graph, separate
    # from direct enumeration of physical vertices below.
    ans = Counter()
    trans = {i: [] for i in range(16)}
    for i,(a,b) in enumerate(S):
        for c in range(4):
            if local_ok(R[a],R[b],R[c],strict):
                trans[i].append((I[(b,c)], frustr(R[b],R[c])))
    for start in range(16):
        layer={(start,0):1}
        for _ in range(n):
            nxt=Counter()
            for (v,e),val in layer.items():
                for w,f in trans[v]:nxt[(w,e+f)]+=val
            layer=nxt
        for (v,e),val in layer.items():
            if v==start:ans[e]+=val
    return ans

def graph_energy(n):
    # Independent graph-edge/adjacency construction, no transfer states.
    edges=set()
    def edge(a,b): edges.add(tuple(sorted((a,b))))
    for i in range(n):
        j=(i+1)%n
        edge(i,j);edge(n+i,n+j);edge(i,n+i);edge(i,n+j)
    neighbors=[set() for _ in range(2*n)]
    for a,b in edges:neighbors[a].add(b);neighbors[b].add(a)
    assert len(edges)==4*n and all(len(x)==4 for x in neighbors)
    weak=Counter();strict=Counter();allstates=Counter()
    for mask in range(1<<(2*n)):
        bad=sum(((mask>>a)&1)==((mask>>b)&1) for a,b in edges)
        allstates[bad]+=1
        oppos=[sum(((mask>>a)&1)!=((mask>>b)&1) for b in neighbors[a]) for a in range(2*n)]
        if min(oppos)>=2:weak[bad]+=1
        if min(oppos)>=3:strict[bad]+=1
    return weak,strict,allstates

def symbolic_check():
    u,x=sp.symbols('u x')
    M=sp.zeros(16)
    for i,(a,b) in enumerate(S):
        for c in range(4):
            if local_ok(R[a],R[b],R[c]):M[i,I[(b,c)]]=u**frustr(R[b],R[c])
    P=x**5-2*u*x**4-(2*u**3-u**2)*x**3-(u**6+2*u**5-u**4)*x**2-(2*u**7+u**6)*x-u**8
    Q=x**5+2*u*x**4+(2*u**3+u**2)*x**3-(u**6-2*u**5-u**4)*x**2+(2*u**7-u**6)*x-u**8
    observed=M.charpoly(x).as_expr()
    expected=x**4*(x-u**2)**2*P*Q
    assert sp.expand(observed-expected)==0
    B=M.subs(u,1)[1:15,1:15]
    C=B**5
    assert all(C[i,j]>0 for i in range(14) for j in range(14))
    W=sp.Matrix([[u**frustr(a,b) for b in R] for a in R])
    A=W.diff(u).subs(u,0)
    D=(W.diff(u,2)/2).subs(u,0)
    assert A**2-sp.eye(4) != sp.zeros(4)
    assert (A**2-sp.eye(4))**2==sp.zeros(4)
    assert sp.trace(A)==0 and sp.trace(A**2)==4
    assert sp.trace(D)==2 and sp.trace((A**2-sp.eye(4))*D)==4
    root=max(float(sp.re(z)) for z in sp.nroots(P.subs(u,1),maxsteps=200))
    mup=-sp.diff(P,u)/sp.diff(P,x)/x
    mu=float(mup.subs({u:1,x:root}))
    assert isclose(root,2.77656214629284,rel_tol=1e-11)
    assert isclose(mu,1.46407373267748,rel_tol=1e-11)
    print('symbolic transfer factorization and primitive core: PASS')
    print('dominant root',root,'mean frustrated bonds/column',mu)

if __name__=='__main__':
    for n in range(4,9):
        g_weak,g_strict,g_all=graph_energy(n)
        t_weak=transfer_energy(n)
        t_strict=transfer_energy(n,strict=True)
        assert g_weak==t_weak,(n,g_weak,t_weak)
        assert g_strict==t_strict,(n,g_strict,t_strict)
        assert sum(g_strict.values())==(4 if n%2==0 else 0)
        lo=min(g_all)
        assert lo==(n if n%2==0 else n+1)
        assert g_all[lo]==(4 if n%2==0 else 2*n*n)
        print('n=',n,'weak=',sum(g_weak.values()),'strict=',sum(g_strict.values()),'ground=',g_all[lo],'Fmin=',lo,'PASS')
    assert [sum(transfer_energy(n).values()) for n in range(4,12)]==[62,172,450,1276,3550,9782,27256,75616]
    symbolic_check()
    print('ALL CHECKS PASS')
