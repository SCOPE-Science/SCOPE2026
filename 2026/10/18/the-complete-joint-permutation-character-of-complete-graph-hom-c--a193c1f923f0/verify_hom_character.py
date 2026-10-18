"""Check signed cellular traces in complete-graph Hom complexes.

The proof for all sizes is mathematical; this script checks finite instances.
Only the Python standard library is required.
"""
from itertools import permutations, product, combinations
from math import comb, factorial, prod


def cycles(p):
    seen = set()
    lengths = []
    for i in range(len(p)):
        if i not in seen:
            x = i
            length = 0
            while x not in seen:
                seen.add(x)
                x = p[x]
                length += 1
            lengths.append(length)
    return lengths


def closed_character_euler(alpha, beta):
    """Cycle-divisibility inclusion-exclusion expression, computed exactly."""
    aa, bb = cycles(alpha), cycles(beta)
    return sum(
        (-1) ** len(T)
        * prod(1 - sum(aa[j] for j in T if L % aa[j] == 0) for L in bb)
        for size in range(len(aa) + 1)
        for T in combinations(range(len(aa)), size)
    )


def cells(m, n):
    """Enumerate product-of-simplices cells independently of cycle lengths."""
    for assignment in product(range(m + 1), repeat=n):
        if any(i not in assignment for i in range(m)):
            continue
        yield tuple(tuple(j for j, a in enumerate(assignment) if a == i) for i in range(m))


def parity(seq):
    return (-1) ** sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i + 1, len(seq)))


def signed_cell_trace(m, n, alpha, beta, allcells):
    """Compute a cellular Lefschetz trace with orientation signs.

    Factor transpositions contribute a Koszul sign based on factor dimensions.
    Relabeling target simplex vertices contributes the sign of their order.
    """
    total = 0
    for C in allcells:
        if any(tuple(sorted(beta[j] for j in C[i])) != C[alpha[i]] for i in range(m)):
            continue
        dims = [len(A) - 1 for A in C]
        sign = (-1) ** sum(dims)
        sign *= (-1) ** sum(
            dims[i] * dims[j]
            for i in range(m)
            for j in range(i + 1, m)
            if alpha[i] > alpha[j]
        )
        for A in C:
            sign *= parity([beta[j] for j in A])
        total += sign
    return total


def old_sphere_number(m, n):
    """Independent non-equivariant sphere-number formula of Babson–Kozlov."""
    return sum((-1) ** (m + k + 1) * comb(m, k + 1) * k ** n for k in range(1, m))


def verify():
    cases = ((2, 3), (2, 4), (3, 4), (3, 5), (3, 6), (4, 5))
    for m, n in cases:
        allcells = list(cells(m, n))
        alphas = list(permutations(range(m)))
        if n <= 5:
            betas = list(permutations(range(n)))
        else:
            betas = [tuple(range(n)), (1, 0, 2, 3, 4, 5),
                     (1, 2, 0, 3, 4, 5), (1, 2, 3, 4, 5, 0),
                     (1, 0, 3, 2, 5, 4)]
        for alpha in alphas:
            for beta in betas:
                direct = signed_cell_trace(m, n, alpha, beta, allcells)
                claimed = closed_character_euler(alpha, beta)
                assert direct == claimed, (m, n, alpha, beta, direct, claimed)
        identity = closed_character_euler(tuple(range(m)), tuple(range(n)))
        assert identity == 1 + (-1) ** (n - m) * old_sphere_number(m, n)
        print('CELL_TRACE_OK', m, n, len(allcells), len(alphas) * len(betas))

    # Independently compute diagonal-quotient invariant dimensions from
    # explicitly enumerated cellular actions, not the closed character.
    for n in range(4, 8):
        m = 3
        allcells = list(cells(m, n))
        signed_sum = 0
        for alpha in permutations(range(m)):
            beta = tuple(alpha) + tuple(range(m, n))
            signed_sum += (-1) ** (n - m) * (signed_cell_trace(m, n, alpha, beta, allcells) - 1)
        assert signed_sum % factorial(m) == 0
        dimension = signed_sum // factorial(m)
        expected = (2 ** n - 3 + 7 * (-1) ** (n - 3)) // 6
        assert (2 ** n - 3 + 7 * (-1) ** (n - 3)) % 6 == 0
        assert dimension == expected
        print('DIAGONAL_QUOTIENT_OK', n, dimension)
    print('VERIFY_OK_COMPLETE_GRAPH_HOM_CHARACTER')


if __name__ == '__main__':
    verify()
