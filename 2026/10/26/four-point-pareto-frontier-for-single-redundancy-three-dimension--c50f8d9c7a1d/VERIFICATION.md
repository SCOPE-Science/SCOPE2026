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
# Verification of the four-point Pareto theorem

Run `python3 verify_retrieval_frontier.py` with standard Python 3. It uses only the standard library and evaluates all expectations with `fractions.Fraction`.

Two independent exact methods are implemented: a subset-count calculation using the four-column recovery identity and a coupon-drawing Markov recursion on all \(16\) subsets of observed column indices. The test enumerates all nonzero projective four-column multisets of rank three over the binary and ternary prime fields and compares every pair of resulting expectations. The resulting counts are \(119\) and \(1404\) matrices and \(22\) and \(30\) distinct expectation pairs, respectively. The four predicted Pareto pairs appear in each case. All explicit witness matrices are also checked over prime fields of sizes \(2,3,5,7\).

The recorded run in `verification_output.txt` ends with `VERIFY_OK`. Neither finite enumeration nor a successful execution proves the all-field result; that comes from the projective-dependence case proof in `RESULT.md`. Exhaustive searches over larger fields were not needed for the proof. No independent audit has been performed.
