#!/usr/bin/env python3
"""Independent rational and matrix checks for optimal grounded-coherence leader sets on K_n corona K_1."""
from fractions import Fraction as Q
from math import comb
from itertools import combinations
import numpy as np
import sympy as sp


def rational_cost(n, u, x, c, y):
    assert u+x+c+y==n
    if u+c==0: return Q(x)
    d=1-Q(u,n)-Q(c,n+1)
    assert d>0
    return Q(u+x)+Q(2*u,n)+Q(c,n+1)+(Q(2*u,n*n)+Q(c,(n+1)**2))/d


def pair_counts(n, S):
    u=x=c=y=0
    for i in range(n):
        a=i in S; b=(n+i) in S
        if not a and not b: u+=1
        elif a and not b: x+=1
        elif not a and b: c+=1
        else: y+=1
    return u,x,c,y


def best_orbits(n, budget):
    best=None; optimal=[]
    for y in range(n+1):
        for x in range(n-y+1):
            c=budget-x-2*y; u=n-x-c-y
            if min(c,u)<0: continue
            val=rational_cost(n,u,x,c,y)
            if best is None or val<best: best=val; optimal=[(u,x,c,y)]
            elif val==best: optimal.append((u,x,c,y))
    return best,optimal


def theorem_orbits(n,budget):
    if budget>n:
        return [(0,0,2*n-budget,budget-n)]
    P=n*budget**2+(2*n*n+3*n+2)*budget-2*n*(n+1)**2
    options=[]
    if P>=0: options.append((n-budget,0,budget,0))
    if P<=0: options.append((n-budget,1,budget-1,0))
    return options


def dense_laplacian(n):
    L=np.zeros((2*n,2*n),dtype=float)
    for i in range(n):
        for j in range(i+1,n):
            L[i,i]+=1; L[j,j]+=1; L[i,j]-=1;L[j,i]-=1
        L[i,i]+=1;L[i+n,i+n]+=1;L[i,i+n]-=1;L[i+n,i]-=1
    return L


def check_symbolic():
    n,b,x=sp.symbols('n b x',positive=True)
    u=n-b;c=b-x
    d=1-u/n-c/(n+1)
    f=sp.factor(u+x+2*u/n+c/(n+1)+(2*u/n**2+c/(n+1)**2)/d)
    P=n*b**2+(2*n**2+3*n+2)*b-2*n*(n+1)**2
    assert sp.simplify(f.subs(x,1)-f.subs(x,0)-P/(b*(b+n)*(n+1)))==0
    second=2*n*(2*n**2+2*n-b*n-2*b)/(b+n*x)**3
    assert sp.simplify(sp.diff(f,x,2)-second)==0
    z=(b**2*n+4*b*n**2+3*b*n+2*b-4*n**2-2*n)/((b+n)*(b+2*n)*(n+1))
    assert sp.simplify(f.subs(x,2)-f.subs(x,1)-z)==0
    f0=n-b+2*(n-b)/n+(b+n)/(n+1)+2*(n-b)*(n+1)/(n*b)
    f1=n-b+1+2*(n-b)/n+(b-1)/(n+1)+2*(n-b)*(n+1)/(n*(n+b))+n*(b-1)/((n+1)*(n+b))
    assert sp.simplify(f.subs(x,0)-f0)==0
    assert sp.simplify(f.subs(x,1)-f1)==0
    q=sp.symbols('q',positive=True)
    c=2*n-q
    high=c/(n+1)+c/((n+1)**2*(1-c/(n+1)))
    plus=c/(n+1)+c/((n+1)*(q-n+1))
    assert sp.simplify(high-plus)==0
    print('symbolic_identities=6')


def check_orbits():
    cases=0; ties=0
    for n in range(3,45):
        for b in range(1,2*n):
            _, got=best_orbits(n,b)
            expected=theorem_orbits(n,b)
            if b<=n:
                assert n*b*b+(2*n*n+3*n+2)*b-2*n*(n+1)**2 != 0
            assert sorted(got)==sorted(expected),(n,b,got,expected)
            cases+=1
            if len(got)>1: ties+=1
    print('exact_rational_all_budget_cases=',cases,'tie_cases=',ties)


def check_dense():
    exhaust=0;independent=0;orbitmat=0
    for n in range(3,7):
        L=dense_laplacian(n)
        for b in range(1,2*n):
            expected_val,optimal_orbits=best_orbits(n,b)
            best=float('inf'); optimal=[]
            for tup in combinations(range(2*n),b):
                S=set(tup); followers=[i for i in range(2*n) if i not in S]
                val=float(np.trace(np.linalg.inv(L[np.ix_(followers,followers)])))
                formula=float(rational_cost(n,*pair_counts(n,S)))
                assert abs(val-formula)<1.e-7,(n,b,S,val,formula)
                if val<best-1e-8: best=val;optimal=[S]
                elif abs(val-best)<=1e-8:optimal.append(S)
                exhaust+=1
            assert abs(best-float(expected_val))<1e-7
            assert all(pair_counts(n,S) in optimal_orbits for S in optimal)
            count=sum((sp.factorial(n)/(sp.factorial(u)*sp.factorial(x)*sp.factorial(c)*sp.factorial(y))) for u,x,c,y in optimal_orbits)
            assert len(optimal)==int(count),(n,b,len(optimal),count)
            independent+=1
    # Independently rational invert representative matrices from each orbit through n=8.
    for n in range(3,9):
        A=sp.Matrix(dense_laplacian(n)).applyfunc(lambda a: sp.Integer(round(float(a))))
        for y in range(n+1):
            for x in range(n-y+1):
                for c in range(n-x-y+1):
                    u=n-x-y-c
                    if x+c+2*y==0 or x+c+2*y==2*n:continue
                    mask=set()
                    for j in range(u,u+x): mask.add(j)
                    for j in range(u+x,u+x+c):mask.add(n+j)
                    for j in range(u+x+c,n):mask.add(j);mask.add(n+j)
                    assert pair_counts(n,mask)==(u,x,c,y)
                    followers=[j for j in range(2*n) if j not in mask]
                    mat=A.extract(followers,followers)
                    actual=sum(mat.inv()[i,i] for i in range(len(followers)))
                    expected=rational_cost(n,u,x,c,y)
                    assert actual==expected,(n,u,x,c,y,actual,expected)
                    orbitmat+=1
    print('dense_exhaustive_sets=',exhaust,'budgets=',independent,'sympy_exact_orbit_inverse=',orbitmat)


if __name__=='__main__':
    check_symbolic()
    check_orbits()
    check_dense()
    print('VERIFY_OK')
