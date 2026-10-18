#!/usr/bin/env python3
"""Exact finite-window and transfer certificates for Ising exchange minima.
Run: python verification.py (requires SymPy 1.12 or later).
"""
from itertools import product
from fractions import Fraction
from collections import deque
import sympy as S

WORDS = list(product((-1, 1), repeat=5))
IX = {word:i for i, word in enumerate(WORDS)}
X = S.Symbol('x')
REPRESENTATIVES = [
    ('low', S.Rational(1,4), X**6-X**5-X**4-X**2+1),
    ('half', S.Rational(1,2), X**6-X**5-X**4-X**2+1),
    ('intermediate', S.Rational(3,4), X**5-X**4-X**2-X-1),
    ('equal', S.Integer(1), X**9-2*X**8+X**7-X**6-X**4+X**3-X+1),
    ('high', S.Integer(2), X**9-2*X**8+X**7-X**6+X+1),
]

def delta(w, r):
    a,b,c,d,e,f = w
    return (c-d)*((1-r)*(b-e)+r*(a-f))

def matrix(r):
    T = S.zeros(32)
    for word in WORDS:
        for z in (-1,1):
            w = word + (z,)
            if delta(w,r) >= 0:
                T[IX[word],IX[w[1:]]] = 1
    return T

def block(T, sign):
    # Global inversion pairs the 32 words; first spin -1 chooses a representative.
    reps = [w for w in WORDS if w[0] == -1]
    B = S.zeros(16)
    for i,u in enumerate(reps):
        for j,v in enumerate(reps):
            B[i,j] = T[IX[u],IX[v]] + sign*T[IX[u],IX[tuple(-s for s in v)]]
    return B

def energy(spins, r):
    n=len(spins)
    return -sum(spins[i]*spins[(i+1)%n] for i in range(n)) - r*sum(spins[i]*spins[(i+2)%n] for i in range(n))

def no_decrease(spins,r):
    original = energy(spins,r)
    for i in range(len(spins)):
        j=(i+1)%len(spins)
        if spins[i] == spins[j]:
            continue
        new=list(spins)
        new[i],new[j]=new[j],new[i]
        if energy(new,r)<original:
            return False
    return True

def graph_scc(T):
    N=T.rows
    graph=[[j for j in range(N) if T[i,j]] for i in range(N)]
    reverse=[[i for i in range(N) if T[i,j]] for j in range(N)]
    visited=set(); order=[]
    def dfs(v):
        visited.add(v)
        for z in graph[v]:
            if z not in visited: dfs(z)
        order.append(v)
    for v in range(N):
        if v not in visited:dfs(v)
    visited=set(); comps=[]
    def dfs_rev(v,C):
        visited.add(v);C.append(v)
        for z in reverse[v]:
            if z not in visited:dfs_rev(z,C)
    for v in reversed(order):
        if v not in visited:
            C=[];dfs_rev(v,C);comps.append(C)
    return sorted(comps,key=len,reverse=True)

def prove_spectrum():
    expected_characteristics = {
      'low': (X**10*(X**6-X**5-X**4-X**2+1), X**10*(X**6-X**5+X**4-X**2-1)),
      'half': (X**9*(X-1)*(X**6-X**5-X**4-X**2+1), X**9*(X+1)*(X**6-X**5+X**4-X**2-1)),
      'intermediate':(X**10*(X-1)*(X**5-X**4-X**2-X-1),X**10*(X+1)*(X**5-X**4+X**2-X-1)),
      'equal': (X**7*(X**9-2*X**8+X**7-X**6-X**4+X**3-X+1), X**7*(X**9-X**7+X**6-3*X**4-X**3+X+1)),
      'high': (X**7*(X**9-2*X**8+X**7-X**6+X+1),X**7*(X**9-X**7+X**6-2*X**4-X+1)),
    }
    roots={}
    mats={}
    for label,r,p in REPRESENTATIVES:
        T=matrix(r);mats[label]=T
        cp_even=block(T,1).charpoly(X).as_expr()
        cp_odd=block(T,-1).charpoly(X).as_expr()
        A,B=expected_characteristics[label]
        assert S.expand(cp_even-A)==0, ('even charpoly',label)
        assert S.expand(cp_odd-B)==0, ('odd charpoly',label)
        Cs=graph_scc(T)
        main=Cs[0]
        assert len(Cs[0])>15
        # All main components are irreducible and have a positive diagonal entry;
        # this gives a primitive Perron component.
        assert any(T[i,i]==1 for i in main)
        assert all(len(c)<=2 for c in Cs[1:])
        for C in Cs[1:]:
            if len(C)==1:assert T[C[0],C[0]]==0
            else:assert len(C)==2
        # Use exact real-root isolation to verify the chosen factor is Perron:
        # it has the largest positive root of the inversion-even quotient.
        # intervals(p) results ((a,b),multiplicity); positivity interval checked below
        intervals=S.polys.polytools.intervals(p,eps=S.Rational(1,10**8))
        positive=[(a,b) for (a,b),mult in intervals if b>1]
        assert positive, (label,positive)
        a,b=max(positive,key=lambda interval: interval[1])
        roots[label]=(float(a+b)/2)
        print('spectrum',label,'rho bracket',str(a),str(b),'SCC sizes',[len(c) for c in Cs])
        # Confirm that no other factor of the even quotient has root >1.
        residual=S.cancel(cp_even/p)
        assert S.degree(residual,X)<S.degree(cp_even,X)
        if label=='half':assert S.expand(residual-X**9*(X-1))==0
        elif label=='intermediate': assert S.expand(residual-X**10*(X-1))==0
        else: assert S.expand(residual-X**(16-S.degree(p,X)))==0
    assert all(mats[s][i,j]<=mats['equal'][i,j] for s in ('intermediate','high') for i in range(32) for j in range(32))
    assert sum(mats['equal'])>sum(mats['intermediate']) and sum(mats['equal'])>sum(mats['high'])
    assert roots['equal']>max(roots['low'],roots['intermediate'],roots['high'])
    return mats

def test_local_energy():
    for w in product((-1,1),repeat=6):
      for r in (S.Rational(1,4),S.Rational(1,2),S.Rational(3,4),S.Integer(1),S.Integer(2)):
        sigma=tuple(w)+ (1,-1,1,-1)
        # Edge (2,3) is at least distance 2 from wraparound on n=10.
        old=energy(sigma,r)
        new=list(sigma);new[2],new[3]=new[3],new[2]
        assert energy(new,r)-old==delta(w,r)

def test_counts(mats):
    for label,r,p in REPRESENTATIVES:
        T=mats[label]
        for n in range(6,13):
            direct=sum(no_decrease(spins,r) for spins in product((-1,1),repeat=n))
            tr=int(S.trace(T**n))
            assert direct==tr,(label,n,direct,tr)
        print('full-energy matches',label,'n=6..12')
    T0=mats['low'];T1=mats['half']
    for n in range(6,26):
        assert S.trace(T1**n)-S.trace(T0**n) == (2 if n%2==0 else 0)
    print('half-coupling exact parity correction checked for n=6..25')

if __name__=='__main__':
    test_local_energy()
    matrices=prove_spectrum()
    test_counts(matrices)
    print('ALL CHECKS PASS')
