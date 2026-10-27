#!/usr/bin/env python3
"""Independent finite boundary checks for the rank-two cyclic semigroup theorem.

The infinite statement relies on the interval/residue proof in RESULT.md.
This script tests bounded instances, not every period/index.
"""

def mult(i, j, m, p):
    s = i + j
    return s if s < m else m + (s - m) % p


def atomic_diagram(a, b, m, p):
    w = (a, b)
    # All 8 instances of a ternary relation on two selected elements,
    # plus both equality directions. No identity or generator constant.
    return (a == b, b == a) + tuple(
        mult(w[i], w[j], m, p) == w[k]
        for i in range(2) for j in range(2) for k in range(2)
    )


def rank_two_type(m, p):
    elements = range(1, m + p)
    return frozenset(
        frozenset(atomic_diagram(x, y, m, p) for y in elements)
        for x in elements
    )


def formula_holds(m, p):
    es = range(1, m + p)
    idem = {x for x in es if mult(x, x, m, p) == x}
    for x in es:
        if x in idem:
            continue
        square = mult(x, x, m, p)
        if square in idem:
            continue
        if not any(mult(y, y, m, p) == x for y in es):
            continue
        if not any(mult(x, z, m, p) == z for z in idem):
            continue
        return True
    return False


def signature(x, m, p):
    return ('tail', x % p) if x >= m else ('transient', x % p, x % 2, 2*x < m)


def pointed_types(m, p):
    es = range(1, m + p)
    return {x: frozenset(atomic_diagram(x, y, m, p) for y in es) for x in es}


def test():
    checked = 0
    for p in range(1, 31):
        L = p if p % 2 == 0 else 2*p
        threshold = 2*L + 1
        # Exact separating sentence, including strict boundary.
        for m in range(1, threshold + 4):
            assert formula_holds(m, p) == (m >= threshold), (m, p)
            checked += 1
        # Compare the complete rank-two theory on several distinct sizes.
        ref = rank_two_type(threshold, p)
        for m in (threshold + 1, threshold + 2, threshold + 7, threshold + 15):
            assert rank_two_type(m, p) == ref, (m, p)
        assert rank_two_type(threshold - 1, p) != ref, p
        # The pointed-signature lemma checks the step that supports the proof.
        by_signature = {}
        for m in (threshold, threshold + 1, threshold + 4, threshold + 13):
            for x, typ in pointed_types(m, p).items():
                sig = signature(x, m, p)
                if sig in by_signature:
                    assert by_signature[sig] == typ, (p, m, x, sig)
                else:
                    by_signature[sig] = typ
        assert len(by_signature) == 2*L + p, (p, len(by_signature), 2*L+p)
    print('DIRECT_ATOMIC_RANK2_OK periods=1..30; threshold+15 sampled')
    print(f'EXPLICIT_FORMULA_BOUNDARY_OK pairs={checked}; threshold=2*lcm(p,2)+1')
    print('POINTED_SIGNATURE_SATURATION_OK periods=1..30; four index samples')
    # A separate small direct two-move game check: every chosen first
    # element is answered by one with the identical set of atomic
    # two-point extensions, in both directions.
    for p in range(1, 9):
        T = 2 * (p if p % 2 == 0 else 2*p) + 1
        assert set(pointed_types(T,p).values()) == set(pointed_types(T+11,p).values())
    print('TWO_MOVE_BACK_AND_FORTH_OK periods=1..8; 11-index gap')
    print('VERIFY_OK')

if __name__ == '__main__':
    test()
