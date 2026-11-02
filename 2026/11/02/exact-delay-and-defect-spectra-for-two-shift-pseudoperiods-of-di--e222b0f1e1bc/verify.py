#!/usr/bin/env python3
"""Independent finite-case checks for two-shift pseudoperiod spectra.

Run: python3 verify.py
Uses only Python's standard library. The infinite theorem is proved in RESULT.md;
these tests compare its predictions against literal periodic words.
"""
from itertools import combinations, product
from math import comb


def predicted_bad(run_lengths, s, t):
    p = sum(run_lengths)
    u = p - t
    return sum(max(0, r - max(0, r - s) - max(0, r - u))
               for r in run_lengths)


def literal_bad(word, s, t):
    p = len(word)
    return sum(word[i] != word[(i+s) % p] and
               word[i] != word[(i+t) % p] for i in range(p))


def main():
    cases = set()
    for q in range(2, 6):
        cases.update(product(range(1, 5), repeat=q))
    cases.update(product(range(1, 9), repeat=3))
    cases.update(product(range(1, 4), repeat=6))
    tested_pairs = tested_budgets = tested_finite = 0
    failed_phases = 0
    for lengths in sorted(cases):
        word = tuple(ch for ch, r in enumerate(lengths) for _ in range(r))
        p = len(word)
        m = min(lengths)
        literal = set()
        two_copies = word + word
        for s, t in combinations(range(1, p), 2):
            observed = literal_bad(word, s, t)
            proposed = predicted_bad(lengths, s, t)
            assert observed == proposed, (lengths, s, t, observed, proposed)
            failed_phases += observed
            holds = observed == 0
            finite_holds = all(two_copies[i] in
                               (two_copies[i+s], two_copies[i+t])
                               for i in range(2*p-t))
            assert holds == finite_holds, (lengths, s, t, 'two copies')
            if holds:
                literal.add((s, t))
            tested_pairs += 1
            tested_finite += 1
        formula = {(s, p-u)
                   for s in range(1, m)
                   for u in range(1, m-s+1)}
        assert literal == formula, (lengths, literal, formula)
        assert len(literal) == comb(m, 2)
        for B in range(1, p):
            count = sum(t <= B for s, t in literal)
            h = max(0, B-p+m)
            assert count == h*(h+1)//2, (lengths, B, count)
            tested_budgets += 1
        if m >= 2:
            first_t = min(t for _, t in literal)
            assert first_t == p-m+1
            assert [(s,t) for s,t in literal if t == first_t] == [(1, p-m+1)]
        else:
            assert not literal
    # Distinct-letter-per-run is essential, even for a primitive period.
    repeated = (0,0,1,0,1)
    assert all(repeated[i] in (repeated[(i+2)%5], repeated[(i+3)%5])
               for i in range(5))
    assert all(tuple(repeated[i:]+repeated[:i]) != repeated
               for i in range(1, 5))
    print('VERIFY_OK cases={} shift_pairs={} delay_budgets={} '
          'two_period_checks={} mismatch_phase_evaluations={} '
          'distinct_run_assumption_counterexample=00101'.format(
          len(cases), tested_pairs, tested_budgets, tested_finite,
          failed_phases))

if __name__ == '__main__':
    main()
