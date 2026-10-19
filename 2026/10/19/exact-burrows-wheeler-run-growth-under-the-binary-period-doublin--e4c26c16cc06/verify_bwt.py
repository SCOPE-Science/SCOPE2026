#!/usr/bin/env python3
"""Two-method exact checks for the binary period-doubling BWT identity.

Only standard-library Python is used. All computations are finite checks;
the accompanying mathematical argument proves the unbounded statement.
"""
from itertools import product

def theta(x):
    return ''.join('01' if a == '0' else '00' for a in x)

def bwt_naive(x):
    n = len(x)
    rotations = sorted(range(n), key=lambda i: x[i:] + x[:i])
    return ''.join(x[(i - 1) % n] for i in rotations)

def bwt_doubling(x):
    n = len(x)
    if n == 1:
        return x
    rank = [int(a) for a in x]
    span = 1
    while span < n:
        inds = sorted(range(n), key=lambda i: (rank[i], rank[(i + span) % n]))
        newrank = [0] * n
        for j in range(1, n):
            a, b = inds[j - 1], inds[j]
            newrank[b] = newrank[a] + (
                (rank[a], rank[(a + span) % n]) !=
                (rank[b], rank[(b + span) % n])
            )
        rank = newrank
        span *= 2
    inds = sorted(range(n), key=lambda i: rank[i])
    return ''.join(x[(i-1) % n] for i in inds)

def is_primitive(x):
    return all(x != x[:d] * (len(x)//d) for d in range(1, len(x)) if len(x) % d == 0)

def transfer(x):
    bx = bwt_naive(x)
    zeros = x.count('0')
    ones = x.count('1')
    b0, b1 = bx[:zeros], bx[zeros:]
    flip = lambda s: ''.join('1' if ch == '0' else '0' for ch in s)
    return flip(b1[::-1]) + '0' * ones + flip(b0[::-1]) + '0' * zeros

def runs(x):
    return 1 + sum(x[i] != x[i-1] for i in range(1, len(x)))

def main():
    general_checks = 0
    for n in range(1, 11):
        for bits in product('01', repeat=n):
            x=''.join(bits)
            if not is_primitive(x) or '11' in x + x[0]:
                continue
            tx=theta(x)
            assert is_primitive(tx), (x,tx)
            assert transfer(x) == bwt_naive(tx), (x, transfer(x), bwt_naive(tx))
            general_checks += 1
    x = '0'
    prev = ''
    prev_bwt = ''
    for k in range(1,15):
        x = theta(x)
        assert '11' not in x+x[0]
        assert is_primitive(x)
        d = bwt_doubling(x)
        if k <= 9:
            assert d == bwt_naive(x)
        if k > 1:
            pz = prev.count('0')
            po = prev.count('1')
            b0, b1 = prev_bwt[:pz], prev_bwt[pz:]
            flip = lambda s: ''.join('1' if ch == '0' else '0' for ch in s)
            via_transfer = flip(b1[::-1]) + '0'*po + flip(b0[::-1]) + '0'*pz
            assert d == via_transfer, (k, d[:50], via_transfer[:50])
            assert runs(d) == 2*k - 2, (k, runs(d))
            assert d[-x.count('1'):] == '0' * x.count('1')
        else:
            assert d == '10'
        prev, prev_bwt = x, d
    print('VERIFY_OK general_primitive_no11_n_le10_cases='+str(general_checks)+
          ' two_independent_BWT_algorithms_k_le9'+
          ' cyclic_suffix_doubling_k_le14'+
          ' exact_BWT_transfer_and_runs_k_le14'+
          ' run_formula_k_2_to14')

if __name__ == '__main__':
    main()
