#!/usr/bin/env python3
"""Independent finite-state and exact characteristic-polynomial checks for the KA ladder."""
import itertools
from collections import Counter
import sympy as sp

R = tuple(itertools.product((0,1), repeat=2))
V = tuple(itertools.product(range(4),repeat=3))
index = {v:i for i,v in enumerate(V)}

def local_ok(a,b,c,d):
    rungs = (R[a], R[b], R[c], R[d])
    def adjacent(p):
        i,j=p
        return ((i-1,j),(i+1,j),(i,1-j))
    for u,v in [((1,0),(1,1)),((1,0),(2,0)),((1,1),(2,1))]:
        if rungs[u[0]][u[1]] == rungs[v[0]][v[1]]:
            continue
        if rungs[u[0]][u[1]] == 0: u,v=v,u
        excess_u=sum(rungs[k][l]==0 for k,l in adjacent(u) if (k,l)!=v)
        excess_v=sum(rungs[k][l]==0 for k,l in adjacent(v) if (k,l)!=u)
        if excess_u>=1 and excess_v>=1: return False
    return True

def transfer_edges():
    return [(index[(a,b,c)],index[(b,c,d)],sum(R[d]))
            for a,b,c,d in itertools.product(range(4),repeat=4)
            if local_ok(a,b,c,d)]

def independent_ok(word):
    n=len(word)
    occ={(i,j):R[word[i]][j] for i in range(n) for j in range(2)}
    def nbr(p):
        i,j=p
        return (((i-1)%n,j),((i+1)%n,j),(i,1-j))
    undirected=[]
    for i in range(n):
        for j in range(2):
            undirected.append(((i,j),((i+1)%n,j)))
        undirected.append(((i,0),(i,1)))
    for a,b in undirected:
        if occ[a]==occ[b]: continue
        if occ[a]==0:a,b=b,a
        src_vac=sum(occ[p]==0 for p in nbr(a) if p!=b)
        dst_vac=sum(occ[p]==0 for p in nbr(b) if p!=a)
        if src_vac and dst_vac:return False
    return True

def core_states(edges):
    out=[set() for _ in V]
    for a,b,k in edges:out[a].add(b)
    def reach(start):
        stack=[start];visited={start}
        while stack:
            for b in out[stack.pop()]:
                if b not in visited:visited.add(b);stack.append(b)
        return visited
    allr=[reach(i) for i in range(64)]
    cyc={i for i in range(64) if any((j==i or i in allr[j]) for j in out[i])}
    # The recurrent directed subgraph is a single strongly connected component.
    assert len(cyc)==29 and all(j in allr[i] for i in cyc for j in cyc)
    assert any(i in out[i] for i in cyc), "aperiodic core needs a loop"
    return sorted(cyc)

def solve():
    E=transfer_edges()
    core=core_states(E)
    assert len(E)==108 and len(core)==29,(len(E),len(core))
    z,x=sp.symbols('z x')
    ids={v:i for i,v in enumerate(core)}
    T=sp.zeros(len(core))
    for a,b,k in E:
        if a in ids and b in ids:T[ids[a],ids[b]] += z**k
    p=T.charpoly(x).as_expr()
    G=x**5-z**2*x**3+z**4*x**2+z**5*x-z**7
    F=x**8-(1+z)**2*x**7+(2*z+2*z**2)*x**6-(z**4+z**2)*x**5+(3*z**5-z**6)*x**4+(4*z**7-z**5)*x**3+(z**9-z**8-2*z**7)*x**2-2*z**9*x-z**11
    assert sp.expand(p-x**16*F*G)==0
    assert sp.factor(F.subs(z,1))==x**8-4*x**7+4*x**6-2*x**5+2*x**4+3*x**3-2*x**2-2*x-1
    # A second completely independent check enumerates all configurations and all physical edges.
    expected={4:54,5:129,6:319,7:837,8:2150}
    for n in range(4,9):
        brute=Counter()
        for w in itertools.product(range(4),repeat=n):
            if independent_ok(w):brute[sum(sum(R[v]) for v in w)]+=1
        assert sum(brute.values())==expected[n]
        # charpoly gives the full trace: only the 13 nonzero eigenvalues contribute
        q=sp.Poly(sp.expand(F*G),x)
        # Newton recurrence: trace of a matrix from coefficients of monic characteristic polynomial
        cs=q.all_coeffs(); power=[sp.Integer(13)]
        for k in range(1,n+1):
            power.append(sp.expand(-sum(cs[j]*power[k-j] for j in range(1,k)) - k*cs[k]))
        coeff=sp.Poly(power[n],z)
        actual={int(d[0]):int(v) for d,v in coeff.terms() if v!=0}
        assert actual==dict(brute),(n,actual,dict(brute))
        print('n=%d exhaustive=%d coefficient_checks=%d'%(n,sum(brute.values()),len(actual)))
    lam=2.605506658540588
    F1=F.subs(z,1)
    assert abs(float(F1.subs(x,lam)))<1e-7
    rho=float((-sp.diff(F,z)/sp.diff(F,x)*z/x).subs({x:lam,z:1}))
    assert abs(rho-1.47244402662209)<1e-8
    print('weighted_charpoly=PASS, Perron_root=%.12f, particles_per_rung=%.12f'%(lam,rho))
if __name__=='__main__':solve()
