#!/usr/bin/env python3
"""Exact finite checks for a Fourier-minor rank census (standard library only)."""
from itertools import combinations, product
from math import comb


def h2_zero(N, p, C):
    # For primitive N=p^a, Phi_N(X)=sum(X**(j*N/p), j=0..p-1).
    # Residue-vector reduction is EXACT, using no floating point arithmetic.
    q=N//p
    v=[0]*N
    for i in range(4):
        for j in range(i,4):
            v[(C[i]+C[j])%N]+=1
    return all(len({v[r+j*q] for j in range(p)})==1 for r in range(q))


def predicted(N,p,C):
    S=frozenset(C)
    if p==2 and N>=8:
        h=N//4
        if any(S=={a,(a+h)%N,(a+2*h)%N,(a+3*h)%N} for a in range(N)):
            return True
        e=N//8
        return any(S=={a,(a+e)%N,(a+3*e)%N,(a+4*e)%N} for a in range(N))
    if p==5 and N>=25:
        e=N//5
        return any(len(S.intersection({a,(a+e)%N,(a+2*e)%N,(a+3*e)%N,(a+4*e)%N}))==4 for a in range(N))
    return False


def verify_5_residue_lemma():
    # For any four residues modulo 5, every nonzero pair-sum class
    # occurring a multiple of 5 times forces the residues all equal.
    checked=0
    for t in product(range(5),repeat=4):
        v=[0]*5
        for i in range(4):
            for j in range(i,4):
                v[(t[i]+t[j])%5]+=1
        if all(x%5==0 for x in v):
            assert len(set(t))==1, (t,v)
        checked+=1
    return checked


def verify_5_base():
    checked=0
    for t in product(range(5),repeat=4):
        v=[0]*5
        for i in range(4):
            for j in range(i,4):
                v[(t[i]+t[j])%5]+=1
        zero=len(set(v))==1
        assert zero==(len(set(t))==4), (t,v)
        checked+=1
    return checked


def verify_census(N,p):
    expected = 5*N//4 if p==2 else N if p==5 else 0
    actual=0
    for C in combinations(range(N),4):
        z=h2_zero(N,p,C)
        assert z==predicted(N,p,C), (N,C,z)
        actual+=z
    assert actual==expected, (N,p,actual,expected)
    print('N=%d, exact-minors=%d, singular=%d, classified=yes'%(N,comb(N,4),actual))


def main():
    print('Five-residue lemma exhaustive cases:',verify_5_residue_lemma())
    print('Fifth-root base lemma exhaustive cases:',verify_5_base())
    for N,p in [(7,7),(8,2),(9,3),(11,11),(16,2),(25,5),(27,3),(32,2),(49,7),(64,2)]:
        verify_census(N,p)
    print('ALL EXACT CHECKS PASSED')

if __name__=='__main__':main()
