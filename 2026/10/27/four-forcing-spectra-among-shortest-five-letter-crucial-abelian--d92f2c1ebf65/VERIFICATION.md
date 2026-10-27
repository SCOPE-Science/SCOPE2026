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

# Reproducibility and proof boundaries

The theorem concerns all length-13 strings on exactly five distinguishable symbols, modulo relabeling for the class count. A canonical word starts with `0` and each first new symbol is the next unused integer. Every candidate is examined by the recursion and exact integer Parikh-prefix comparisons in `check_census.py`.

Run `python3 check_census.py` from the directory containing the source. It completes a finite exhaustive search, asserting 297588 visited square-free canonical prefixes, 205424 full-alphabet square-free words of length 13, the complete list of fourteen right-crucial canonical words, unique extension witnesses for each appended letter, and the four signature frequencies. It also checks the smaller alphabet sizes three and four, with respectively one and five canonical classes.

For a computational cross-check using different code and a direct signed-count test instead of prefix-vector subtraction, compile `g++ -O2 -std=c++17 independent_census.cpp -o independent_census`, then run `./independent_census`. Its printed list of canonical words must equal the first column of `canonical_representatives.csv`. The five append-witness columns in that table can be reproduced directly from the Python routine `exhaustive(5)`.

The proof of exhaustive coverage is essential: appending a letter can create a forbidden Abelian square only as a new suffix; all possible first-appearance canonical branches are traversed without repetition; and any right-crucial word must use all alphabet symbols. These facts, rather than an unbounded experimental extrapolation, allow finite enumeration to establish the exact classification. Shortestness at length 13 relies on the published all-alphabet minimum theorem of Evdokimov and Kitaev, Theorem 5, arXiv:math/0205217v1. No infinite-size census, independent audit, or historical-uniqueness certificate is asserted.
