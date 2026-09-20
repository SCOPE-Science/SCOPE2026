#!/usr/bin/env python3
"""Exact finite checks for the off-diagonal greedy strict 2-sumfree theorem."""

def greedy_2sumfree(f, g, limit):
    seq = [f, g]
    forbidden = {f + g}
    for n in range(g + 1, limit + 1):
        if n not in forbidden:
            for a in seq:
                forbidden.add(a + n)
            seq.append(n)
    return seq


def interval(a, b):
    return set(range(a, b + 1)) if a <= b else set()


def formula_data(f, delta):
    M = 5 * f + 2 * delta - 1
    E = {f} | set(range(2 * f + delta, 3 * f + delta))
    R = (
        {f - 1, f}
        | set(range(2 * f + delta + 1, 3 * f + delta - 1))
        | set(range(4 * f + delta, 4 * f + 2 * delta + 1))
    )
    return M, E, R


def formula_sequence(f, delta, limit):
    M, E, R = formula_data(f, delta)
    out = set(E)
    for n in range(4 * f + delta, limit + 1):
        if n % M in R:
            out.add(n)
    return sorted(out)


def modular_sumset(A, B, M, distinct=False):
    return {
        (a + b) % M
        for a in A
        for b in B
        if not distinct or a != b
    }


def predicted_sumsets(f, delta):
    if delta == 1:
        EE = interval(0, f - 2) | interval(3 * f + 1, 4 * f) | interval(4 * f + 3, 5 * f)
        ER = (
            interval(0, f - 2)
            | interval(f + 1, 2 * f + 1)
            | interval(3 * f, 4 * f)
            | interval(4 * f + 3, 5 * f)
        )
        RR = interval(0, f - 3) | interval(f + 2, 2 * f) | interval(3 * f + 1, 4 * f - 1) | interval(4 * f + 4, 5 * f)
    else:
        EE = interval(0, f - 2) | interval(3 * f + 2, 4 * f + 1) | interval(4 * f + 5, 5 * f + 2)
        ER = (
            interval(0, f - 2)
            | interval(f + 1, 2 * f + 2)
            | interval(3 * f + 1, 4 * f + 1)
            | interval(4 * f + 5, 5 * f + 2)
        )
        RR = interval(0, f - 3) | interval(f + 2, 2 * f + 1) | interval(3 * f + 1, 4 * f) | interval(4 * f + 6, 5 * f + 2)
    return EE, ER, RR


def check():
    cases = 0
    for delta in (1, 2):
        for f in range(5, 301):
            M, E, R = formula_data(f, delta)
            limit = 4 * f + delta + 8 * M

            actual = greedy_2sumfree(f, 2 * f + delta, limit)
            predicted = formula_sequence(f, delta, limit)
            assert actual == predicted

            EE, ER, RR = predicted_sumsets(f, delta)
            assert modular_sumset(E, E, M, distinct=True) == EE
            assert modular_sumset(E, R, M) == ER
            assert modular_sumset(R, R, M) == RR
            assert not (EE & R)
            assert not (ER & R)
            assert not (RR & R)

            assert len(R) == f + delta + 1
            cases += 1

    print(f"verified exact formula in {cases} parameter cases")
    print("range: 5 <= f <= 300, delta in {1,2}")
    print("comparison depth: eight full residue periods beyond the periodic tail")
    print("verified all three modular sumset identities, including diagonal R+R pairs")


if __name__ == "__main__":
    check()
