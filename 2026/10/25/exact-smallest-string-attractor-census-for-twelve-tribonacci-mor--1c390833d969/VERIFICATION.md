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
# Verification of the finite census

The complete list of minimum attractors in each of twelve cases is embedded at `certificates/attractors.json` as zero-based increasing position arrays. Run `python3 verify.py` to reconstruct every word and recompute the list of all feasible optimal-size subsets, not merely to replay a claimed count. A second implementation `python3 verify_independent.py` constructs factor sets reached by each position and independently tests every size-three candidate through substitution order nine.

Exact results checked: the word lengths are 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, and 927; the respective minimum-attractor cardinalities are 1, 2, and 3 for every remaining order; the exact numbers of optimum sets are 1, 1, 2, 8, 12, 16, 32, 56, 112, 224, 416, and 832. Exact-coverage-mask antichain sizes, at orders two to eleven, are 3, 3, 5, 6, 6, 7, 10, 11, 12, 15. Every certificate word SHA-256 is checked against the newly generated word.

Limits: full factor-incidence enumeration is a finite correctness certificate; it does not establish any pattern for unexamined orders. The second implementation checks the first ten orders (through index nine), not the last two; their first implementation is still fully exhaustive. No independent external audit has been performed.
