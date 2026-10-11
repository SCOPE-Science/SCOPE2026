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
# Verification of the stated mathematical theorem

The deterministic Python 3 standard-library script `verify.py` uses `fractions.Fraction` exact rational arithmetic. Invoke it as `python3 verify.py` after placing the script in the current directory; no network or external package is needed.

A successful run prints `VERIFY_OK` and the following totals: 1,184 graph profiles, 2,368 nonnegative center instances, 7,300 nonintegral vertex/farthest-point comparisons, 4,836 exact odd-cycle gain identity checks, and 1,184 weighted diameter equality tests. Graphs include all 1,024 labeled graphs on five vertices and 160 additional six-vertex instances. A triangle with a negative center is separately confirmed as a sharp hypothesis boundary.

The graph instances and finite center cases are not exhaustive over graphs, metric weights, or centers of arbitrary order. The proof of the general result is the extremal-vertex classification, the exact odd-cycle mean-gain identity, center clamping, and the strict quadratic identity in RESULT.md; no numerical inference is used to extend finite tests to infinite quantifiers. No independent scientific audit has yet been performed.
