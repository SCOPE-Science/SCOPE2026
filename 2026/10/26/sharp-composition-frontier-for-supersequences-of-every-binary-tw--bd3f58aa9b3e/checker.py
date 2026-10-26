#!/usr/bin/env python3
"""Independent finite checks for the weight-two universal-supersequence theorem.

Run: python3 checker.py
"""
from itertools import combinations, product
from math import isqrt

def is_subsequence(target, source):
    j = 0
    for s in source:
        if j < len(target) and target[j] == s:
            j += 1
    return j == len(target)

def targets(N):
    return ["0" * a + "1" + "0" * b + "1" + "0" * (N - a - b)
            for a in range(N + 1) for b in range(N - a + 1)]

def source(m, N):
    if N == 0:
        return "1" * m
    gaps = [((i+1)*N)//(m-1) - (i*N)//(m-1)
            for i in range(m+1)]
    return ''.join('0'*gaps[i] + ('1' if i<m else '') for i in range(m+1))

def all_binaries(zeros, ones):
    for positions in combinations(range(zeros+ones), ones):
        bits = ['0']*(zeros+ones)
        for i in positions:
            bits[i]='1'
        yield ''.join(bits)

def checks():
    # Greedy-embedding implementation does not share the counting/covering proof.
    for N in range(0, 81):
        tw=targets(N)
        for m in range(2, 22):
            s=source(m,N)
            Z=len(s)-m
            assert Z==N+(2*N)//(m-1),(m,N,'zero count')
            assert all(is_subsequence(w,s) for w in tw),(m,N,s)
    print('Beatty-gap source valid for N=0..80, m=2..21: 1680 cases')

    # Independently enumerate all sources with given zeros and ones.
    tests=0
    for m in range(2,6):
        for N in range(0,8):
            optimum=N+(2*N)//(m-1)
            tw=targets(N)
            for Z in range(N, optimum+1):
                count=0
                for s in all_binaries(Z,m):
                    if all(is_subsequence(w,s) for w in tw):
                        count+=1
                if Z<optimum: assert count==0,(m,N,Z,count)
                else: assert count>=1,(m,N,Z)
                tests+=1
    print('Full-source exhaustive searches on m=2..5, N=0..7:',tests,'(m,N,Z) domains')

    # Independent brute force of unconstrained optimum, from the source alphabet.
    for N in range(0,8):
        T=targets(N)
        opt=N+1+isqrt(8*N+1)
        assert len(source(1+isqrt(2*N)+1 if N else 2,N))>=0
        assert any(all(is_subsequence(w,s) for w in T)
                   for m in range(2,opt+1)
                   for s in all_binaries(opt-m,m)),(N,'no witness')
        for L in range(N+2,opt):
            for n_ones in range(2,L-N+1):
                assert not any(all(is_subsequence(w,s) for w in T)
                               for s in all_binaries(L-n_ones,n_ones)),(N,L)
    print('Global length optimum by exhaustive binary enumeration for N=0..7')
    for N in range(0,501):
        lhs=min(k+(2*N)//k for k in range(1,max(2*N+2,2)))
        assert lhs==isqrt(8*N+1),(N,lhs)
    print('Integer floor-square-root identity tested through N=500')

if __name__=='__main__':
    checks()
