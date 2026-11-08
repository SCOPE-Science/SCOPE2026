#!/usr/bin/env python3
"""Exact checks for a hexagonal-strip independence-complex fixed Euler series.

Only Python's standard library is required. The all-parameter proof uses an
8-state transfer and a verified integer-matrix annihilator; sample enumeration
is a separate check, not a substitute for the proof.
"""
from functools import lru_cache
from itertools import combinations


def original_graph(n):
    assert n >= 1
    V = {(r, j) for r, length in enumerate((2*n+1, 2*n+2, 2*n+1))
         for j in range(1, length+1)}
    E = {frozenset(((r, j), (r, j+1)))
         for r, length in enumerate((2*n+1, 2*n+2, 2*n+1))
         for j in range(1, length)}
    E.update(frozenset(((0, j), (1, j+1))) for j in range(1, 2*n+2, 2))
    E.update(frozenset(((1, j), (2, j))) for j in range(1, 2*n+2, 2))
    return V, E


def halfturn(n, v):
    r, j = v
    return (1, 2*n+3-j) if r == 1 else (2-r, 2*n+2-j)


def quotient(n):
    V, E = original_graph(n)
    assert {frozenset(halfturn(n,v) for v in e) for e in E} == E
    assert all(halfturn(n,halfturn(n,v)) == v for v in V)
    rem = set(V)
    O = []
    while rem:
        v = min(rem)
        orb = frozenset((v, halfturn(n,v)))
        rem -= orb
        if not (orb in E):
            O.append(orb)
    edge = lambda x,y: frozenset((x,y)) in E
    QE = {frozenset((i,j)) for i,j in combinations(range(len(O)),2)
          if any(edge(x,y) for x in O[i] for y in O[j])}
    return O, QE


def canonical(n):
    # A_j (j=1,...,2n+1), M_i (i=1,...,n).
    A = [('A',j) for j in range(1,2*n+2)]
    M = [('M',j) for j in range(1,n+1)]
    E = {frozenset((A[i],A[i+1])) for i in range(2*n)}
    E.update(frozenset((M[i],M[i+1])) for i in range(n-1))
    for i in range(1,n+1):
        j = 2*n+2-i if i%2 else i-1
        E.add(frozenset((('M',i),('A',j))))
    return A+M,E


def direct_canonical_equals_orbits(n):
    O, QE = quotient(n)
    bijection = {}
    for i,orb in enumerate(O):
        top = [j for r,j in orb if r == 0]
        mid = [j for r,j in orb if r == 1]
        bijection[i] = ('A', top[0]) if top else ('M', min(mid))
    CV, CE = canonical(n)
    assert set(bijection.values()) == set(CV)
    assert {frozenset((bijection[i],bijection[j])) for i,j in (tuple(e) for e in QE)} == CE
    return O, QE


def mask_polyeval(vertices,edges):
    ix = {v:i for i,v in enumerate(vertices)}
    ngh = [0]*len(ix)
    for e in edges:
        u,v = tuple(e)
        i,j = ix[u],ix[v]
        ngh[i] |= 1<<j; ngh[j] |= 1<<i
    @lru_cache(None)
    def rec(mask):
        if mask == 0: return 1
        v=(mask & -mask).bit_length()-1
        return rec(mask ^ (1<<v)) - rec(mask & ~(ngh[v] | (1<<v)))
    return rec((1<<len(vertices))-1)


def entry(s,b): return (s >> b) & 1
STATES=list(range(8))

def transfer(parity):
    # Each state is (U,V,W); layer i has V_i-W_i edge if odd.
    # For even i, W_i-U_(i-1) is the diagonal edge.
    out=[]
    for p in STATES:
        row=[]
        for q in STATES:
            allowed = (p&q)==0
            if parity: allowed &= not(entry(q,1) and entry(q,2))
            else: allowed &= not(entry(p,0) and entry(q,2))
            row.append((-1)**q.bit_count() if allowed else 0)
        out.append(row)
    return out
A=transfer(1);B=transfer(0)
s=[(-1)**q.bit_count() if not(entry(q,1) and entry(q,2)) else 0 for q in STATES]
t=[int(entry(q,0) or entry(q,1)) for q in STATES]

def matmul(X,Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(len(Y)))
             for j in range(len(Y[0]))] for i in range(len(X))]

def matpow(X,k):
    N=len(X); res=[[int(i==j) for j in range(N)] for i in range(N)]
    while k:
        if k & 1: res=matmul(res,X)
        X=matmul(X,X);k//=2
    return res

def matlin(*terms):
    N=len(terms[0][1]);return [[sum(a*X[i][j] for a,X in terms)
                  for j in range(N)] for i in range(N)]

def mat_apply(row,M):
    return [sum(row[i]*M[i][j] for i in STATES) for j in STATES]

def scalar(row,col):return sum(x*y for x,y in zip(row,col))

def from_transfer(n):
    row=s[:]
    for layer in range(2,n+1): row=mat_apply(row,B if layer%2==0 else A)
    return scalar(row,t)


def graph_invariant_face_sum(n):
    # Uses original graph only; does NOT build the quotient conflict graph.
    V,E=original_graph(n);unvisited=set(V);orbits=[]
    while unvisited:
        v=min(unvisited);o=frozenset((v,halfturn(n,v)));unvisited-=o
        if o not in E:orbits.append(o)
    N=len(orbits);total=0
    for mask in range(1<<N):
        selected=set().union(*(orbits[i] for i in range(N) if (mask>>i)&1))
        if all(not e.issubset(selected) for e in E):
            total+=(-1)**mask.bit_count()
    return total


def main():
    T=matmul(B,A)
    P=matlin((1,matpow(T,8)),(-1,matpow(T,7)),(2,matpow(T,6)),(1,matpow(T,4)))
    assert P == [[0]*8 for _ in range(8)]  # exact annihilating polynomial
    odd=[scalar(mat_apply(s,matpow(T,k)),t) for k in range(8)]
    Bt=[sum(B[i][j]*t[j] for j in STATES) for i in STATES]
    even=[scalar(mat_apply(s,matpow(T,k)),Bt) for k in range(8)]
    D=[1,-1,2,0,1]
    def prod8(seq):
        return [sum(D[j]*seq[k-j] for j in range(min(4,k)+1)) for k in range(8)]
    assert prod8(odd)==[0,-2,0,-1,0,0,0,0]
    assert prod8(even)==[1,1,1,0,0,0,0,0]
    # By the matrix annihilator, later coefficients of D times each series vanish.
    # These checks therefore prove the two generating-function numerators exactly.
    coeff=[0]*240
    for n in range(1,240):
        coeff[n]=from_transfer(n)
        if n>=5:assert coeff[n]+coeff[n-1]+coeff[n-4]==0
    assert coeff[1:13]==[0,1,-2,2,-2,1,1,-3,5,-6,5,-2]
    for n in range(1,16):
        O,QE=direct_canonical_equals_orbits(n)
        assert from_transfer(n)==mask_polyeval(range(len(O)),QE)
    for n in range(1,6):
        assert graph_invariant_face_sum(n)==from_transfer(n)
    print('HALFTURN_FIXED_EULER_OK')
    print('integer-matrix annihilator: T^8 - T^7 + 2*T^6 + T^4 = 0')
    print('odd numerator: -2z-z^3; even numerator: 1+z+z^2')
    print('I_n generating function: z^2*(1-z)/(1+z+z^4)')
    print('reduced fixed Euler generating function: z^2*(z-1)/(1+z+z^4)')
    print('cross-checks: 15 orbit-conflict graphs; 5 original invariant-face enumerations; 239 transfer terms')
    print('initial reduced Euler: ',[-coeff[n] for n in range(1,16)])
if __name__ == '__main__':main()
