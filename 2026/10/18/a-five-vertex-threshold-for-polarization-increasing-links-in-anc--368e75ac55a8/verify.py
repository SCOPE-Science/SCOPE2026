#!/usr/bin/env python3
"""Exact certificate for a five-vertex opinion-polarization edge paradox.
Requires sympy >=1.10. No graph tables, external data, or numerical root searches.
"""
from itertools import combinations, permutations
from fractions import Fraction
import sympy as S

a = S.symbols('a')

def laplacian(n, edges):
    M = S.zeros(n)
    for u, v in edges:
        M[u,u] += 1; M[v,v] += 1
        M[u,v] -= 1; M[v,u] -= 1
    return M

def connected(n, edges):
    seen={0}; todo=[0]
    while todo:
        u=todo.pop()
        for i,j in edges:
            if i==u and j not in seen: seen.add(j); todo.append(j)
            if j==u and i not in seen: seen.add(i); todo.append(i)
    return len(seen)==n

def canonical_mask(n, mask, pairs):
    pindex={edge:i for i,edge in enumerate(pairs)}
    ans=mask
    for perm in permutations(range(n)):
        y=0
        for t,(i,j) in enumerate(pairs):
            if mask & (1<<t):
                v,w=sorted((perm[i],perm[j]))
                y |= 1<<pindex[(v,w)]
        ans=min(ans,y)
    return ans

def connected_unlabeled(n):
    pairs=list(combinations(range(n),2))
    found=set()
    for mask in range(1<<len(pairs)):
        edges=[e for k,e in enumerate(pairs) if mask&(1<<k)]
        if not connected(n,edges): continue
        canon=canonical_mask(n,mask,pairs)
        if canon not in found:
            found.add(canon)
            yield [e for k,e in enumerate(pairs) if canon&(1<<k)]

def poly_certificate(n,edges,e,s):
    L=laplacian(n,edges)
    H=L+laplacian(n,[e])
    M=L+a*S.eye(n)
    N=H+a*S.eye(n)
    k=S.factor(M.det()); h=S.factor(N.det())
    adjM=M.adjugate(); adjN=N.adjugate()
    # x(a)=a adj(M)s/det(M), and every equilibrium mean equals mean(s).
    C=S.eye(n)-S.ones(n)/n
    vm=adjM*s; vn=adjN*s
    # Difference = a^2 * P(a) / (k^2 h^2).
    numerator=S.Poly(S.expand((vn.T*C*vn)[0]*k*k-(vm.T*C*vm)[0]*h*h),a)
    # Every coefficient is nonpositive, hence the edge never raises polarization.
    return numerator

def all_lower_bounds():
    counts={}; nonzero=0; zero=0
    for n in range(2,5):
        cnt=0; graphcnt=0
        for edges in connected_unlabeled(n):
            graphcnt+=1
            for e in combinations(range(n),2):
                if e in edges: continue
                # Binary complement symmetry allows s[0] = 0, and all-zero is trivial.
                for bits in range(1,1<<(n-1)):
                    s=S.Matrix([0]+[(bits>>(i-1))&1 for i in range(1,n)])
                    P=poly_certificate(n,edges,e,s)
                    cnt+=1
                    assert all(c<=0 for c in P.all_coeffs()), (n,edges,e,s,P)
                    if P.is_zero: zero+=1
                    else:nonzero+=1
        counts[n]=(graphcnt,cnt)
    assert counts == {2:(1,0),3:(2,3),4:(6,77)},counts
    assert (nonzero,zero)==(58,22),(nonzero,zero)
    print('SMALL_NETWORK_CERTIFICATE',counts,'strict',nonzero,'identity',zero)

def witness():
    # A path of five vertices: 4--0--1--2--3, with shortcut 0--2.
    n=5
    edges=[(0,1),(0,4),(1,2),(2,3)]
    e=(0,2)
    s=S.Matrix([0,0,1,0,1]); I=S.eye(n)
    C=I-S.ones(n)/n
    L=laplacian(n,edges)
    z=a*(L+a*I).inv()*s
    zz=a*(L+laplacian(n,[e])+a*I).inv()*s
    delta=S.factor((zz.T*C*zz)[0]-(z.T*C*z)[0])
    F=a**4+4*a**3-7*a-3
    expected=-2*a**3*F/((a**2+3*a+1)**2*(a**2+5*a+3)**2)
    assert S.cancel(delta-expected)==0
    assert delta.subs(a,1)==S.Rational(2,405)
    assert delta.subs(a,2)==-S.Rational(496,34969)
    # F's descending coefficient signs are +,+,0,-,-; exactly one positive
    # root by Descartes' rule, with F(1)<0<F(2).
    assert S.Poly(F,a).count_roots(0,S.oo)==1
    assert F.subs(a,1)<0 and F.subs(a,2)>0
    # Independent source-by-source exact arithmetic with integer matrices.
    for aval in [S.Rational(1,2),S.Integer(1),S.Integer(2),S.Integer(3)]:
        A=L+aval*I; B=L+laplacian(n,[e])+aval*I
        x=A.inv()*s*aval; y=B.inv()*s*aval
        val=S.factor((y.T*C*y)[0]-(x.T*C*x)[0])
        assert val==delta.subs(a,aval)
    print('WITNESS',str(S.factor(delta)))
    print('TEST_POINTS',delta.subs(a,1),delta.subs(a,2))

if __name__=='__main__':
    all_lower_bounds()
    witness()
    print('PASS')
