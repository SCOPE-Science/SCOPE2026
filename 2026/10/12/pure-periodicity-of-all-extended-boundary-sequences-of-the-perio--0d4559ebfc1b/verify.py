#!/usr/bin/env python3
"""Reproducible finite checks for a symbolic all-width boundary theorem.
No external libraries, network, or previously generated files are needed.
"""

def valuation2(v):
    assert v > 0
    return (v & -v).bit_length() - 1


def pd(j):
    return valuation2(j + 1) & 1


def possible_valuation_pairs(delta):
    assert delta > 0
    if delta & 1:
        return {(0, 0), (0, 1), (1, 0)}
    return {(0, 0), (0, 1), (1, 0), (1, 1)}


def exact_boundary(ell, distance):
    """Formula using residues and *proved* 2-adic valuation-pair lemma."""
    assert ell >= 1 and distance >= ell
    k = (ell - 1).bit_length()
    P = 1 << k
    boundary = set()
    for r in range(P):
        rows = []
        holes = []
        for step in (0, distance):
            row = []
            for offset in range(ell):
                j = r + step + offset
                if (j + 1) % P == 0:
                    holes.append((step, offset, (j + 1) // P))
                    row.append(-1)
                else:
                    row.append(pd(j))
            rows.append(row)
        assert len(holes) <= 2
        if len(holes) == 0:
            assignments = [()]
        elif len(holes) == 1:
            assignments = [(0,), (1,)]
        else:
            delta = holes[1][2] - holes[0][2]
            assert delta > 0
            assignments = possible_valuation_pairs(delta)
        for assignment in assignments:
            it = iter(assignment)
            codes = []
            for row in rows:
                code = 0
                for digit in row:
                    bit = ((next(it) ^ (k & 1)) if digit == -1 else digit)
                    code = (code << 1) | bit
                codes.append(code)
            boundary.add(tuple(codes))
    return boundary


def factor_codes(word, ell):
    mask = (1 << ell) - 1
    v = 0
    out = []
    for j, bit in enumerate(word):
        v = ((v << 1) | bit) & mask
        if j + 1 >= ell:
            out.append(v)
    return out


def independent_prefix_boundary(codes, distance, n):
    return {(codes[i], codes[i + distance]) for i in range(n)}


def check():
    # Independent construction from the substitution 0->01, 1->00.
    sub = [0]
    while len(sub) < 8192:
        sub = [b for v in sub for b in ((0, 1) if v == 0 else (0, 0))]
    assert sub[:8192] == [pd(j) for j in range(8192)]

    # Exhaust finite examples of the 2-adic parity-pair lemma.
    for delta in range(1, 129):
        observed = {(valuation2(t) & 1, valuation2(t + delta) & 1)
                    for t in range(1, 8193)}
        assert observed == possible_valuation_pairs(delta), (delta, observed)

    symbolic=0
    for ell in range(1, 17):
        k = (ell - 1).bit_length()
        P = 1 << k
        T = 2 * P
        for d in range(ell, ell + 2 * T):
            A = exact_boundary(ell, d)
            B = exact_boundary(ell, d + T)
            assert A == B, (ell, d)
            assert len(A) <= 4 * P
            symbolic += 1

    N=65536
    maxd=80
    word = [pd(j) for j in range(N + maxd + 20)]
    brute=0
    for ell in range(1,13):
        P = 1 << ((ell-1).bit_length())
        T=2*P
        codes = factor_codes(word, ell)
        for d in range(ell, ell+T):
            brute_set = independent_prefix_boundary(codes, d, N)
            symbolic_set = exact_boundary(ell, d)
            assert brute_set == symbolic_set, (ell,d,brute_set^symbolic_set)
            brute += 1
    print('VERIFY_OK '+
          'morphism_prefix=8192 '+
          'valuation_pair_deltas=1..128 '+
          'symbolic_period_widths=1..16 '+
          f'symbolic_cases={symbolic} '+
          'direct_prefix=65536 '+
          f'direct_cases={brute} '+
          'symbolic_max_pairs_le_4P')

if __name__ == '__main__':
    check()
