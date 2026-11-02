---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducibility

Run `python3 verify_primary.py` using Python 3.8 or later; it requires only the Python standard library. Run `g++ -std=c++17 -O2 verify_alt.cpp -o verify_alt && ./verify_alt` with a C++17 compiler. Both tests generate their inputs from exact permutation definitions rather than stored output tables.

The Python checker enumerates every derangement for orders three through eight and builds the switch graph from explicit legal swaps; it compares the degree multiset with an independent exponential-formula recurrence for cycles of length at least three. The C++ checker enumerates all labelled derangements independently, checks legal four-cycle switches from forbidden diagonal entries, recomputes two-cycle counts, and verifies connectivity and the small-order metric witnesses.

The tests confirm that the three-letter graph has two isolated vertices; that orders four through eight are connected; that every pair in order four retains ambient transposition distance; and that the displayed order-five and order-six witnesses have constrained distance four instead of two. They also confirm the degree counts and total edge counts. The general connectivity, degree and threshold theorems are mathematical arguments in RESULT.md, not claims inferred from computational extrapolation.

Exact observed degrees and edge totals:

| n | states | edges | vertex degrees and multiplicities |
|---:|---:|---:|---|
| 3 | 2 | 0 | 0:2 |
| 4 | 9 | 12 | 2:6, 4:3 |
| 5 | 44 | 120 | 5:24, 6:20 |
| 6 | 265 | 1260 | 9:160, 10:90, 12:15 |
| 7 | 1854 | 13440 | 14:1140, 15:504, 16:210 |
| 8 | 14833 | 152040 | 20:8988, 21:4480, 22:1260, 24:105 |

Independent scholarly validation has not been performed. The output programs verify finite cases only; they do not decide the entire metric distortion or all-pairs distribution in unbounded order.
