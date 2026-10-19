#!/usr/bin/env python3
"""Independent checks of the shortest-absent-subsequence profile of Thue-Morse blocks.

No external dependencies.  Execute with Python 3.10+.
"""
from itertools import product
from collections import defaultdict
from math import exp, log, log1p


def tm_substitution(m):
    z = '0'
    for _ in range(m):
        z = ''.join('01' if a == '0' else '10' for a in z)
    return z


def tm_digits(m):
    return ''.join(str(i.bit_count() % 2) for i in range(1 << m))


def is_subsequence(v, w):
    p = 0
    for a in w:
        if p < len(v) and v[p] == a:
            p += 1
    return p == len(v)


def direct_missing(w, r):
    return sum(not is_subsequence(''.join(v), w)
               for v in product('01', repeat=r))


def missing_via_greedy_states(w, r):
    n = len(w)
    nxt = [[n, n] for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        nxt[i] = nxt[i + 1].copy()
        nxt[i][int(w[i])] = i
    states = {0: 1}
    for _ in range(r):
        following = defaultdict(int)
        for st, count in states.items():
            for a in range(2):
                pos = nxt[st][a]
                if pos != n:
                    following[pos + 1] += count
        states = following
    return (1 << r) - sum(states.values())


def matmul(a, b):
    return ((a[0][0]*b[0][0] + a[0][1]*b[1][0],
             a[0][0]*b[0][1] + a[0][1]*b[1][1]),
            (a[1][0]*b[0][0] + a[1][1]*b[1][0],
             a[1][0]*b[0][1] + a[1][1]*b[1][1]))


def tm_matrix(m):
    a0 = ((1, 0), (1, 1))
    a1 = ((1, 1), (0, 1))
    p = ((1, 0), (0, 1))
    for bit in tm_digits(m):
        p = matmul(p, a0 if bit == '0' else a1)
    return p


def count_with_recurrence(m):
    d, s = 2, 1
    for _ in range(m - 1):
        d, s = s*s + 2, s*d
    return d + s


def verify():
    # Full equivalence test: any pair of complementary arches, up to seven arches.
    for k in range(1, 8):
        for x in product('01', repeat=k):
            w = ''.join(c + ('1' if c == '0' else '0') for c in x)
            for vv in product('01', repeat=k+1):
                v = ''.join(vv)
                aligned = any(v[j:j+2] == x[j] + ('1' if x[j]=='0' else '0')
                              for j in range(k))
                assert is_subsequence(v, w) == aligned, (x,v)
    target_counts = (3,5,12,74,2666,3647090,6476006417762)
    for m in range(1, 10):
        w = tm_digits(m)
        assert w == tm_substitution(m)
        k = len(w)//2
        assert all(w[2*i] != w[2*i+1] for i in range(k))
        matrix_count = sum(map(sum, tm_matrix(m-1)))
        recurrence_count = count_with_recurrence(m)
        greedy_count = missing_via_greedy_states(w, k+1)
        assert matrix_count == recurrence_count == greedy_count, (m,matrix_count,recurrence_count,greedy_count)
        if m <= len(target_counts):
            assert greedy_count == target_counts[m-1], m
        if m <= 5:
            assert direct_missing(w,k+1)==greedy_count
            assert missing_via_greedy_states(w,k)==0
    # Rigorous tail: s_j is increasing; log(1+2/s_j**2)<=2/s_N**2 for j>=N.
    s=[1,2]
    for i in range(2,10):
        s.append(s[-1]*(s[-2]*s[-2]+2))
    N=8
    L_partial=log(2)+sum(2**(-i-1)*log1p(2/(s[i]*s[i])) for i in range(N))
    tail_bound=2**(1-N)/(s[N]*s[N])
    rho_min=exp(L_partial/3)
    rho_max=exp((L_partial+tail_bound)/3)
    assert 1.56866478 < rho_min <= rho_max < 1.56866480
    print('VERIFY_OK ThueMorse-SAS: arbitrary_complementary_arches_k<=7; '
          'two_generators_m<=9; three_count_engines_m<=9; '
          'direct_absent_subsequences_m<=5; exact_nonlinear_recurrence; '
          'rho_in_[%.12f, %.12f]'%(rho_min,rho_max))

if __name__ == '__main__':
    verify()
