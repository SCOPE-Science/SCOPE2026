#!/usr/bin/env python3
"""Exact finite checks for the Pascal-row p-kernel rank theorem.

Uses only Python's standard library. Finite tests corroborate, but do not
replace, the unrestricted reachability/observability argument.
"""
from fractions import Fraction
from math import comb


def step(s, d, p, alpha):
    u, v = s[:alpha], s[alpha:]
    un = [(d+1)*u[k]+d*v[k] for k in range(alpha)]
    vn = [0]*alpha
    for k in range(1, alpha):
        vn[k] = (p-1-d)*u[k-1]+(p-d)*v[k-1]
    return tuple(un+vn)


def from_digits(ds, p, alpha):
    state = (1,)+(0,)*(2*alpha-1)
    for d in ds:
        state = step(state, d, p, alpha)
    return state


def automaton(n,p,alpha):
    ds=[]
    while n:
        ds.append(n%p); n//=p
    return sum(from_digits(ds,p,alpha)[:alpha])


def digit_sequence(n,p):
    out=[]
    while n:
        out.append(n%p); n//=p
    return out


def rank_integer(mat):
    if not mat: return 0
    A = [[Fraction(x) for x in row] for row in mat]
    n,m=len(A),len(A[0]); row=0
    for col in range(m):
        piv=next((i for i in range(row,n) if A[i][col]), None)
        if piv is None: continue
        A[row],A[piv]=A[piv],A[row]
        a=A[row][col]
        A[row]=[x/a for x in A[row]]
        for i in range(n):
            if i!=row and A[i][col]:
                v=A[i][col]; A[i]=[x-v*y for x,y in zip(A[i],A[row])]
        row+=1
        if row==n:return row
    return row


def test(p,alpha):
    D=2*alpha-1
    assert D>0
    # Direct coefficient arithmetic from actual Pascal rows.
    mod=p**alpha
    for n in range(0,min(2*p**alpha+18,160)):
        direct=sum(comb(n,k)%mod != 0 for k in range(n+1))
        assert automaton(n,p,alpha)==direct, (p,alpha,n,direct,automaton(n,p,alpha))
    # Reachability based on explicit digits, not the claimed abstract proof.
    prefixes=[[]]
    for r in range(1,alpha):prefixes.append([0]*r)
    for r in range(1,alpha):prefixes.append([0]*r+[p-1])
    assert len(prefixes)==D
    states=[from_digits(ds,p,alpha) for ds in prefixes]
    assert rank_integer(states)==D,(p,alpha,'reach',rank_integer(states))
    # Suffix observations: all-p-1 blocks and zero followed by all-p-1.
    suffixes=[[]]
    suffixes += [[p-1]*h for h in range(1,alpha)]
    suffixes += [[0]+[p-1]*h for h in range(1,alpha)]
    assert len(suffixes)==D
    mat=[]
    for s in states:
        mat.append([sum(_apply(s, suf,p,alpha)[:alpha]) for suf in suffixes])
    assert rank_integer(mat)==D,(p,alpha,'hankel',rank_integer(mat),mat)
    # Direct p-kernel table n -> a(p^e*n+r) for the prefix residues.
    ext=[]
    for ds in prefixes:
        e=len(ds); residue=sum(x*p**i for i,x in enumerate(ds))
        ext.append([automaton(p**e*n+residue,p,alpha) for n in [sum(d*p**i for i,d in enumerate(suf)) for suf in suffixes]])
    # Existence of independent sampled suffixes is not guaranteed for all alpha.
    sample_rank=rank_integer(ext)
    assert sample_rank==D,(p,alpha,'sampled',sample_rank)
    print('CASE_OK',p,alpha,'dimension',D,'direct_n',min(2*p**alpha+18,160),'hankel',D,'sample',sample_rank,flush=True)


def _apply(state,ds,p,alpha):
    for d in ds: state=step(state,d,p,alpha)
    return state

if __name__=='__main__':
    for p in (2,3,5):
        for a in range(1,7): test(p,a)
    print('VERIFY_OK exact_rational_full_rank_cases=18 all_cases_passed=True')
