#!/usr/bin/env python3
"""Exact finite-state checks for uniform sliding-window coupon coverage episodes.
Scientific artifacts only; Python 3 standard library.
"""
from fractions import Fraction
from itertools import product
from math import factorial


def stirling(k, n):
    if k < n: return 0
    a = [0] * (n+1); a[0] = 1
    for _ in range(k):
        a = [0]+[j*a[j]+a[j-1] for j in range(1,n+1)]
    return a[n]


def onto(w, alphabet):
    return len(set(w)) == alphabet


def entry_windows(n,M):
    # At a stationary new entry, the appended color is n-1 and the preceding M-1 word
    # is uniformly chosen among onto words over the other n-1 colors.
    for w in product(range(n-1),repeat=M-1):
        if onto(w,n-1): yield w+(n-1,)


def matrix_mean(n,M):
    states=[w for w in product(range(n),repeat=M) if onto(w,n)]
    index={w:i for i,w in enumerate(states)}
    N=len(states)
    A=[[Fraction(int(i==j)) for j in range(N)]+[Fraction(1)] for i in range(N)]
    for w,i in index.items():
        for a in range(n):
            nxt=w[1:]+(a,)
            if nxt in index:
                A[i][index[nxt]]-=Fraction(1,n)
    # Gaussian elimination (linear systems only for small finite n,M).
    for c in range(N):
        i=next((j for j in range(c,N) if A[j][c]),None)
        assert i is not None
        A[c], A[i]=A[i], A[c]
        div=A[c][c]
        A[c]=[v/div for v in A[c]]
        for r in range(N):
            if r==c: continue
            fac=A[r][c]
            if fac:
                A[r]=[a-fac*b for a,b in zip(A[r],A[c])]
    values=[A[i][-1] for i in range(N)]
    starts=list(entry_windows(n,M))
    assert starts
    return sum(values[index[w]] for w in starts)/len(starts)


def main():
    checks=0
    for n in [2,3,4]:
        for M in range(n,min(n+3,7)):
            starts=list(entry_windows(n,M)); m=M-1; N=n-1
            assert len(starts)==factorial(N)*stirling(m,N)
            checks+=1
            for u in range(0,min(m,2)+1):
                count=0
                for w in starts:
                    for future in product(range(n),repeat=u):
                        curr=w
                        survived=True
                        for a in future:
                            curr=curr[1:]+(a,)
                            if not onto(curr,n):
                                survived=False;break
                        count+=survived
                survival=Fraction(count,len(starts)*n**u)
                lower=Fraction(N**u*stirling(m-u,N),stirling(m,N))
                er=Fraction(sum(len(set(w[:u])-set(w[u:m])) for w in starts),len(starts))
                upper=lower+Fraction(u,n)*er
                assert lower<=survival<=upper, (n,M,u,lower,survival,upper)
                if u==0:assert survival==1
                checks+=3
    for n,M in [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4)]:
        exact=matrix_mean(n,M)
        # E[L]=stationary onto-window mass divided by new-entry flux.
        target=Fraction(n*stirling(M,n),(n-1)*stirling(M-1,n-1))
        assert exact==target,(n,M,exact,target)
        checks+=1
    # First bin chosen uniformly on the nonmissing colors, plus independent appended color.
    # When M=n, entry word is a permutation and each surviving future shift requires
    # the new symbol to copy the symbol being removed: geometric exit hazard 1-1/n.
    for n in range(2,7):
        assert Fraction(n,n-1)==Fraction(n*stirling(n,n),(n-1)*stirling(n-1,n-1))
        checks+=1
    print(f'VERIFY_OK {checks} exact finite-state / combinatorial assertions')

if __name__=='__main__':main()
