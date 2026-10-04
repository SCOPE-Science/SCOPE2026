#!/usr/bin/env python3
from itertools import combinations


def E(s):
    return ''.join('1' if c == '0' else '0' for c in reversed(s))


def anti_closure(s):
    # Shortest E-palindrome having s as a prefix.  For a candidate total
    # length L, consistency on the already fixed prefix is necessary and
    # sufficient; the remaining symbols are then forced by E-symmetry.
    m = len(s)
    for L in range(m, 2*m + 3):
        if L % 2:
            continue
        ok = True
        for i in range(m):
            j = L - 1 - i
            if j < m and s[i] == s[j]:
                ok = False
                break
        if not ok:
            continue
        a = list(s) + ['?'] * (L-m)
        for i in range(L):
            j = L - 1 - i
            if a[i] != '?' and a[j] == '?':
                a[j] = '1' if a[i] == '0' else '0'
            elif a[i] == '?' and a[j] != '?':
                a[i] = '1' if a[j] == '0' else '0'
        p = ''.join(a)
        if '?' not in p and p == E(p) and p.startswith(s):
            return p
    raise AssertionError('closure search failed')


def pseudostandard(delta):
    w = ''
    for d in delta:
        w = anti_closure(w + d)
    return w


def factor_masks(w):
    n = len(w)
    masks = {}
    for L in range(1, n+1):
        for i in range(n-L+1):
            f = w[i:i+L]
            masks.setdefault(f, 0)
            masks[f] |= ((1 << L) - 1) << i
    return tuple(masks.values())


def smallest_pairs(w):
    masks = factor_masks(w)
    n = len(w)
    # No singleton can attract both single-letter factors when both occur.
    assert set(w) == {'0','1'}
    for i in range(n):
        one = 1 << i
        assert not all(one & M for M in masks)
    ans = set()
    for i, j in combinations(range(n), 2):
        pm = (1 << i) | (1 << j)
        if all(pm & M for M in masks):
            ans.add((i,j))
    assert ans
    return ans


def pred_A(n):
    N = 2*n
    return {(i,j) for i,j in combinations(range(N),2)
            if ((i-j) & 1) and (i,j) != (0,N-1)}


def pred_B(n):
    N = 4*n-2
    bad = {(1,N-3),(2,N-2)}
    return {(i,j) for i,j in combinations(range(1,N-1),2)
            if (j-i) % 4 == 2 and (i,j) not in bad}


def anti(s):
    return s == E(s)

# Verify the finite-directive identities and the complete pair classifications.
for n in range(2, 15):
    A = pseudostandard('0'*n)
    assert A == '01'*n
    assert anti(A)
    gotA = smallest_pairs(A)
    assert gotA == pred_A(n)
    assert len(gotA) == n*n - 1

    B = pseudostandard('0' + '1'*(n-1))
    assert B == '0' + '1100'*(n-1) + '1'
    assert anti(B)
    gotB = smallest_pairs(B)
    if n == 2:
        assert gotB == {(1,3),(2,4)}
    else:
        assert gotB == pred_B(n)
        assert len(gotB) == 2*n*(n-2)

# Independently stress the pair criteria directly on the closed forms beyond
# the closure-reconstruction loop above.
for n in range(15, 41):
    A = '01'*n
    B = '0' + '1100'*(n-1) + '1'
    assert smallest_pairs(A) == pred_A(n)
    assert smallest_pairs(B) == pred_B(n)

print('VERIFY_OK A_n=2..40 B_n=2..40 exact_pair_classification')
