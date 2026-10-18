#!/usr/bin/env python3
"""Standalone checks for cyclic mixed domination/locating-domination partitions.
Python standard library only. Graph predicate is independent of forbidden-word counting.
"""
from itertools import product
from fractions import Fraction


def direct_partition(n, bits):
    # bits[i] = 1 for L, 0 for D. Cycles are simple of order n >= 3.
    D = {i for i, b in enumerate(bits) if b == 0}
    L = set(range(n)) - D
    if any(not ({(i-1) % n, (i+1) % n} & D) for i in L):
        return False
    seen = set()
    for i in D:
        sig = frozenset({(i-1) % n, (i+1) % n} & L)
        if not sig or sig in seen:
            return False
        seen.add(sig)
    return True


def local_pattern(n, bits):
    # Deliberately separate from direct graph predicate.
    for i in range(n):
        if all(bits[(i+j) % n] == 0 for j in range(3)):
            return False
        if all(bits[(i+j) % n] == 1 for j in range(3)):
            return False
        if tuple(bits[(i+j) % n] for j in range(5)) == (0, 0, 1, 0, 0):
            return False
    return True


def poly_add(a, b):
    out = [0] * max(len(a), len(b))
    for i, v in enumerate(a): out[i] += v
    for i, v in enumerate(b): out[i] += v
    return out


def poly_mul(a, b, cap):
    out = [0] * (cap + 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if i+j <= cap: out[i+j] += ai*bj
    return out


def mat_mul(A, B, cap):
    return [[poly_add(poly_mul(A[i][0],B[0][j],cap),
                      poly_mul(A[i][1],B[1][j],cap))[:cap+1]
             for j in range(2)] for i in range(2)]


def trace_transfer(cap):
    # M = [[z²+z³,z²+z³],[z³+z⁴,z⁴]].
    a = [0,0,1,1]
    b = [0,0,0,1,1]
    c = [0,0,0,0,1]
    M = [[a,a],[b,c]]
    P = M
    ans = [0]*(cap+1)
    for k in range(1,cap//2+1):
        trace = poly_add(P[0][0],P[1][1])
        # Marking a vertex multiplies degree n; divide by k marked zero-runs.
        for n in range(1, min(cap+1,len(trace))):
            ans[n] += Fraction(n*trace[n], k)
        P = mat_mul(P,M,cap)
    assert all(int(v)==v for v in ans)
    return [int(v) for v in ans]


def recurrence_trace(cap):
    # -z d/dz log(1-z²-z³-z⁴-z⁵-z⁶).
    # From A(z)=z Delta'(z) negative, solve Delta(z)T(z)=-z Delta'(z).
    weights=[2,3,4,5,6]
    vals=[0]*(cap+1)
    for n in range(1,cap+1):
        vals[n]=sum(vals[n-k] for k in weights if n>=k)
        if n in weights: vals[n]+=n
    return vals


def main():
    cap=30
    trace=trace_transfer(cap)
    recurrence=recurrence_trace(cap)
    assert trace==recurrence
    assert trace[2]==2 and trace[4]==6
    predicted=recurrence[:]
    predicted[2]-=2
    predicted[4]-=2
    assert predicted[3]==3 and predicted[4]==4
    total=0
    local_exceptions=[]
    for n in range(3,17):
        cnt=0
        forbidden=0
        for bits in product((0,1),repeat=n):
            direct=direct_partition(n,bits)
            local=local_pattern(n,bits)
            if direct: cnt+=1
            if local: forbidden+=1
            if direct!=local:
                local_exceptions.append((n, ''.join(map(str,bits)),direct,local))
            if n>=5: assert direct==local, (n,bits)
        assert cnt == predicted[n], (n,cnt,predicted[n])
        total+=2**n
        print('n=%2d direct=%5d forbidden_word=%5d transfer=%5d tested=%6d'%
              (n,cnt,forbidden,predicted[n],2**n))
    assert local_exceptions==[(4,'0101',False,True),(4,'1010',False,True)],local_exceptions
    print('C4 exceptions:',local_exceptions)
    print('EXACT TRANSFER COEFFICIENTS 3..30:',predicted[3:])
    print('Total independent bitstrings tested:',total)
    print('VERIFICATION_OK')

if __name__ == '__main__': main()
