"""Independent exact checker for dyadic parabolic exponential spectra.

Uses cyclotomic coefficient equality, not floating-point sums or a
quadratic-Gauss evaluation, for its Fourier-zero decisions. Python 3 stdlib.
"""
from itertools import combinations


def exact_fourier_zero(k, u, v):
    q = 1 << k
    counts = [0] * q
    for x in range(q):
        counts[(u*x + v*x*x) % q] += 1
    # Phi_{2^k}(X) = X^{q/2}+1; all degree < q integer
    # polynomials vanishing at a primitive root are multiples of Phi.
    return all(counts[r] == counts[r+q//2] for r in range(q//2))


def recurrence_fourier_zero(k, u, v):
    while k >= 2:
        if u % 2:
            return True
        if v % 2:
            return False
        u //= 2
        v //= 2
        k -= 1
    return bool((u+v) % 2)


def maximal_cliques(neighbors):
    # Bron-Kerbosch with pivot and integer bitsets.
    n = len(neighbors)
    def itbits(bits):
        while bits:
            b = bits & -bits
            yield b.bit_length()-1
            bits -= b
    def visit(R, P, X):
        if not P and not X:
            yield R
            return
        U = P | X
        pivot = max(itbits(U), key=lambda j:(P & neighbors[j]).bit_count()) if U else None
        cand = P & ~(neighbors[pivot] if pivot is not None else 0)
        while cand:
            vbit = cand & -cand
            v = vbit.bit_length()-1
            yield from visit(R | vbit, P & neighbors[v], X & neighbors[v])
            P &= ~vbit
            X |= vbit
            cand &= ~vbit
    yield from visit(0, (1 << n)-1, 0)


def run():
    comparisons = 0
    for k in range(1,8):
        q = 1 << k
        for u in range(q):
            for v in range(q):
                got = exact_fourier_zero(k,u,v)
                predicted = recurrence_fourier_zero(k,u,v)
                assert got == predicted, (k,u,v,got,predicted)
                comparisons += 1
    print('EXACT_CYCLOTOMIC_ZERO_MATCH',comparisons,'for levels 1..7')
    total_maximal = 0
    for k in (1,2,3):
        q=1<<k
        freq=[(u,v) for u in range(q) for v in range(q)]
        neighbors = [0]*(q*q)
        for a,b in combinations(range(q*q),2):
            u,v=freq[a]
            w,z=freq[b]
            if exact_fourier_zero(k,(u-w)%q,(v-z)%q):
                neighbors[a] |= 1<<b
                neighbors[b] |= 1<<a
        sizes={}
        for c in maximal_cliques(neighbors):
            size=c.bit_count()
            sizes[size]=sizes.get(size,0)+1
        expected=2**(2**(k+1)-2)
        assert sizes=={q:expected},(k,sizes,expected)
        total_maximal+=expected
        print('INDEPENDENT_MAXIMAL_CLIQUES',k,'q',q,'basis_sets',expected,'other_maximal_sizes',0)
    print('ALL_TESTS_PASS',comparisons,'zero_tests',total_maximal,'maximal_cliques')

if __name__=='__main__':run()
