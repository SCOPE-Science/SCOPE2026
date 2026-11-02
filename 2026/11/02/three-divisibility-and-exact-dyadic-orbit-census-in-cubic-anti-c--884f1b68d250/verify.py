#!/usr/bin/env python3
"""Independent finite-volume checks for parity neighbor updates on prism graphs.

No external dependencies. Algebraic identities in the accompanying proof, not this
finite verifier, establish the theorem for arbitrarily large networks.
"""

def adjacency_rows(n):
    assert n >= 3
    out = []
    for a in range(2):
        for i in range(n):
            out.append((1 << (a*n + (i-1)%n)) |
                       (1 << (a*n + (i+1)%n)) |
                       (1 << ((1-a)*n+i)))
    return out


def apply(rows, x):
    y = 0
    for i, r in enumerate(rows):
        if (r & x).bit_count() % 2:
            y |= 1 << i
    return y


def compose(left, right):
    # Row matrix of the product left*right (function composition).
    out = []
    for row in left:
        r, mask = 0, row
        while mask:
            low = mask & -mask
            r ^= right[low.bit_length()-1]
            mask ^= low
        out.append(r)
    return out


def mat_power(rows, power):
    d = len(rows)
    ans = [1 << i for i in range(d)]
    while power:
        if power & 1:
            ans = compose(ans, rows)
        rows = compose(rows, rows)
        power >>= 1
    return ans


def rank(rows):
    basis = {}
    for r in rows:
        while r:
            pivot = r.bit_length()-1
            if pivot not in basis:
                basis[pivot] = r
                break
            r ^= basis[pivot]
    return len(basis)


def fixed_dimension(M):
    return len(M) - rank([r ^ (1 << i) for i, r in enumerate(M)])


def highest_power_two_dividing(n):
    return n & -n


def check():
    assert [((k%2)) for k in range(4)] == [0,1,0,1] # anti-conformist code 0101
    general = 0
    for n in range(3, 37):
        A = adjacency_rows(n)
        t = highest_power_two_dividing(n)
        if n % 3:
            assert rank(A) == 2*n
        else:
            assert rank(A) == 2*n-2*min(t, 2)
            tau = max(2, t)
            stable = mat_power(A, tau)
            assert rank(stable) == 2*n-4*t, (n, rank(stable))
            assert rank(mat_power(A, tau-1)) > rank(stable)
        assert fixed_dimension(A) == __import__('math').gcd(n, 4)
        general += 1

    dyadic = []
    for k in range(2, 7):
        n = 1 << k
        A = adjacency_rows(n)
        F = []
        for j in range(k):
            F.append(1 << fixed_dimension(mat_power(A, 1 << j)))
        expected = [16] + [1 << (2 * min(n, 1 << (j+1))) for j in range(1,k)]
        assert F == expected, (n,F,expected)
        assert mat_power(A,n//2) == [1 << i for i in range(2*n)]
        assert F[-1] == 1 << (2*n)
        assert F[-2] < F[-1]
        dyadic.append((n, [f.bit_length()-1 for f in F]))

    census = {}
    for n in (4,8):
        A = adjacency_rows(n)
        counts = {1 << j:0 for j in range(n.bit_length()-1)}
        for state in range(1 << (2*n)):
            x=state
            for t in range(1,n//2+1):
                x=apply(A,x)
                if x==state:
                    counts[t] += 1
                    break
            else: raise AssertionError((n,state))
        assert sum(counts.values()) == (1 << (2*n))
        F=[16]+[(1 << (2*min(n, 1 << (j+1)))) for j in range(1,n.bit_length()-1)]
        prior=0
        for j,p in enumerate(counts):
            assert counts[p] == F[j]-prior, (n,p,counts[p],F[j]-prior)
            prior=F[j]
        census[n]=counts
    print('PASS: invertibility and eventual-periodic ranks, n=3..36 (34 graphs)')
    print('PASS: dyadic fixed-space dimensions and exact global orders, n=4,8,16,32,64')
    print('PASS: exhaustive orbit census, n=4 and 8', census)
    print('DYADIC_DIMS', dyadic)


if __name__ == '__main__':
    check()
