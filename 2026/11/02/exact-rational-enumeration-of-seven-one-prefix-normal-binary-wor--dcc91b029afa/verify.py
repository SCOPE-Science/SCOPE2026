#!/usr/bin/env python3
"""Exact integer verification for the seven-one prefix-normal generating function.

No third-party packages are required. Run: python3 verify.py
"""
from itertools import combinations
from math import gcd
from functools import reduce

# Inequalities A*v >= 0 for v=(x,y,z,t,v), five nonnegative gap offsets.
A = [
    (1, 0, 0, 0, 0), (0, 1, 0, 0, 0), (0, 0, 1, 0, 0),
    (0, 0, 0, 1, 0), (0, 0, 0, 0, 1),
    (-1, 1, 1, 0, 0), (-1, 0, 1, 1, 0),
    (-1, 0, 0, 1, 1), (-1, -1, 1, 1, 1),
]
RAYS = {
    (0, 0, 0, 0, 1), (0, 0, 0, 1, 0), (0, 0, 1, 0, 0),
    (0, 1, 0, 0, 1), (0, 1, 0, 1, 0), (0, 1, 1, 0, 0),
    (1, 0, 1, 0, 1), (1, 0, 1, 1, 0),
    (1, 1, 0, 1, 1), (1, 1, 0, 2, 0), (1, 1, 1, 0, 1),
    (2, 1, 1, 1, 1), (2, 1, 1, 2, 0),
}
H = [1, 3, 9, 17, 35, 48, 76, 85, 108, 103,
     108, 85, 76, 48, 35, 17, 9, 3, 1]


def determinant(matrix):
    # Division-free recursive expansion; here matrices have at most four rows.
    n = len(matrix)
    if n == 0:
        return 1
    if n == 1:
        return matrix[0][0]
    return sum(((-1) ** j) * matrix[0][j] *
               determinant([row[:j] + row[j + 1:] for row in matrix[1:]])
               for j in range(n))


def rays_from_facets():
    result = set()
    for inds in combinations(range(len(A)), 4):
        sub = [list(A[i]) for i in inds]
        v = [((-1) ** j) * determinant([r[:j] + r[j + 1:] for r in sub])
             for j in range(5)]
        if not any(v):
            continue
        d = reduce(gcd, (abs(i) for i in v))
        v = tuple(i // d for i in v)
        for cand in (v, tuple(-i for i in v)):
            if all(sum(a*b for a,b in zip(row,cand)) >= 0 for row in A):
                result.add(cand)
    return result


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i + j] += ai * bj
    return c


def polynomial_remainder(p, divisor):
    p = p.copy()
    while len(p) >= len(divisor):
        lead = p[-1] // divisor[-1]
        start = len(p)-len(divisor)
        for j,c in enumerate(divisor):
            p[start+j] -= lead*c
        while p and p[-1] == 0:
            p.pop()
    return p


def one_minus_power(n):
    a = [0] * (n + 1)
    a[0] = 1
    a[n] = -1
    return a


def numerator_from_cone(N):
    g = [0] * (N + 1)
    for x in range(N+1):
        for y in range(N-x+1):
            for z in range(N-x-y+1):
                if y+z < x:
                    continue
                for t in range(N-x-y-z+1):
                    if z+t < x:
                        continue
                    min_v = max(0, x-t, x+y-z-t)
                    for v in range(min_v, N-x-y-z-t+1):
                        g[x+y+z+t+v] += 1
    return g


def series_denominator(denom, N):
    # Given denominator polynomial with constant term one, return its reciprocal.
    a = [0] * (N+1)
    a[0] = 1
    for i in range(1, N+1):
        a[i] = -sum(denom[j] * a[i-j] for j in range(1, min(i, len(denom)-1)+1))
    return a


def predicted_word_counts(N):
    q = [1]
    for k in [1,3,4,4,6,6,6]:
        q = mul(q, one_minus_power(k))
    # generating function z^7 H(z)/Q(z), Q as above.
    inv = series_denominator(q, N)
    return [0 if n<7 else sum(H[j]*inv[n-7-j]
             for j in range(min(len(H)-1, n-7)+1)) for n in range(N+1)]


def prefix_normal(word):
    n = len(word)
    pref = [0]
    for x in word:
        pref.append(pref[-1]+x)
    for width in range(1,n+1):
        for st in range(n-width+1):
            if pref[st+width]-pref[st] > pref[width]:
                return False
    return True


def brute_word_counts(N=18):
    counts=[]
    for n in range(7,N+1):
        c=0
        for inds in combinations(range(1,n),6):
            w=[0]*n
            w[0]=1
            for i in inds:
                w[i]=1
            c+=prefix_normal(w)
        counts.append(c)
    return counts


def run():
    rays=rays_from_facets()
    assert rays == RAYS, (rays-RAYS,RAYS-rays)
    assert len(rays)==13
    degrees=sorted(sum(r) for r in rays)
    assert degrees == [1,1,1,2,2,2,3,3,4,4,4,6,6]
    assert sum(degrees)==39
    D=[1]
    for degree in degrees:
        D=mul(D,one_minus_power(degree))
    K=[1]
    for degree in [1,1,1,2,2,2,3,4]:
        K=mul(K,one_minus_power(degree))
    Q=[1]
    for degree in [3,4,4,6,6]:
        Q=mul(Q,one_minus_power(degree))
    assert mul(K,Q)==D
    g=numerator_from_cone(70)
    actual=[sum(D[i]*g[n-i] for i in range(min(n,len(D)-1)+1))
            for n in range(40)]
    expected=mul(K,H)
    assert len(expected)==35
    assert actual==expected+[0]*(40-len(expected)), (actual,expected)
    # Independently test extra coefficients without relying on finite-determination bound.
    for n in range(40,71):
        assert sum(D[i]*g[n-i] for i in range(min(n,len(D)-1)+1))==0
    pred=predicted_word_counts(18)
    brute=brute_word_counts(18)
    assert pred[7:19] == brute, (pred[7:19],brute)
    assert H==H[::-1] and sum(H)==867
    assert polynomial_remainder(H,[1,0,1])==[0,1]  # Phi_4
    assert polynomial_remainder(H,[1,-1,1])==[1]   # Phi_6
    assert pred[7:19]==[1,4,13,31,71,134,249,417,688,1062,1628,2367]
    print('VERIFY_OK rays=13 degrees_sum=39 coeffs=71 word_lengths=7..18')
    print('density7_counts_n7_to18',','.join(map(str,brute)))
    print('numerator_H',','.join(map(str,H)))

if __name__=='__main__':
    run()
