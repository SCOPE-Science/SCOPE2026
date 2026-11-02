"""Finite-chain checks from two constructions for the pair-shadow cover theorem.
Run: python verify.py. Standard library only.
Finite checks corroborate the exact lumping; they do not prove the limit law.
"""
import itertools
import math
from fractions import Fraction

ASSERTIONS = 0


def check(condition, description):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(description)


def reduced_chain(n, r, edges, exact=False):
    """Substochastic avoidance kernel, states = currently held marked labels."""
    marks = sorted({v for edge in edges for v in edge})
    edge_sets = tuple(map(frozenset, edges))
    states = tuple(frozenset(t) for j in range(min(r, len(marks)) + 1)
                   for t in itertools.combinations(marks, j)
                   if not any(e <= frozenset(t) for e in edge_sets))
    indices = {s: i for i, s in enumerate(states)}
    z = Fraction(0) if exact else 0.0
    P = [[z for _ in states] for _ in states]
    one = Fraction(1) if exact else 1.0
    eps = one / (n-r)
    for i, s in enumerate(states):
        j = len(s)
        for v in s:
            after = s - {v}
            P[i][indices[after]] += (one / r)*(1-(len(marks)-j)*eps)
            for y in marks:
                if y not in s:
                    after2 = after | {y}
                    if after2 in indices:
                        P[i][indices[after2]] += eps/r
        if j < r:
            P[i][i] += ((r-j)*one/r)*(1-(len(marks)-j)*eps)
            for y in marks:
                if y not in s:
                    after = s | {y}
                    if after in indices:
                        P[i][indices[after]] += ((r-j)*one/r)*eps
    return states, P


def full_chain(n,r,edges):
    edge_sets = tuple(map(frozenset,edges))
    states=tuple(frozenset(s) for s in itertools.combinations(range(n),r)
                 if not any(e <= frozenset(s) for e in edge_sets))
    idx={s:i for i,s in enumerate(states)}
    P=[[Fraction(0) for _ in states] for _ in states]
    for i,s in enumerate(states):
        for old in s:
            for new in range(n):
                if new not in s:
                    state=(s-{old})|{new}
                    if state in idx:
                        P[i][idx[state]] += Fraction(1,r*(n-r))
    return states,P


def multiply(vec, mat):
    out=[type(vec[0])(0) for _ in vec]
    for i,x in enumerate(vec):
        if not x: continue
        for j,y in enumerate(mat[i]):
            if y: out[j]+=x*y
    return out


def spectral_rate(n,r,edges):
    states,P = reduced_chain(n,r,edges)
    d=len(states)
    v=[0.0]*d
    v[states.index(frozenset())]=1.0
    for _ in range(130):
        nextv=multiply(v,P)
        size=sum(nextv)
        v=[x/size for x in nextv]
    lam=sum(multiply(v,P))
    return n*n*(1-lam),lam


def exact_checks():
    cases=[(7,3,[(0,1)]),(7,3,[(0,1),(1,2)]),
           (8,4,[(0,1),(2,3)]),(9,3,[(0,1),(2,3)]),
           (8,3,[(0,1),(0,2),(1,2)])]
    for n,r,edges in cases:
        states,P=reduced_chain(n,r,edges,exact=True)
        fstates,Q=full_chain(n,r,edges)
        marks={v for e in edges for v in e}
        a=[Fraction(sum(1 for x in fstates if x & marks==s),math.comb(n,r))
           for s in states]
        b=[Fraction(1,math.comb(n,r)) for _ in fstates]
        check(sum(a)==sum(b),f'initial normalization: {n,r,edges}')
        for t in range(9):
            check(sum(a)==sum(b),f'finite survival: {n,r,edges,t}')
            a=multiply(a,P)
            b=multiply(b,Q)
        for i,row in enumerate(P):
            check(0<=sum(row)<=1,f'row substochastic: {n,r,edges,i}')


def perturbation_checks():
    patterns=[[(0,1)],[(0,1),(1,2)],[(0,1),(2,3)],
              [(0,1),(1,2),(0,2)]]
    for r in (3,4,5):
        for edges in patterns:
            prev=None
            for n in (60,120,240,480):
                rate,lam=spectral_rate(n,r,edges)
                goal=2*(r-1)*len(edges)
                check(0<rate<goal+1.0,f'positive decay: {r,edges,n,rate}')
                check(abs(rate-goal)<(5000.0/n),f'1/n rate: {r,edges,n,rate}')
                if prev is not None:
                    check(abs(rate-goal)<abs(prev-goal),f'rate convergence: {r,edges,n}')
                prev=rate


if __name__=='__main__':
    exact_checks()
    perturbation_checks()
    print(f'PASS: {ASSERTIONS} finite-chain and asymptotic-rate assertions')
