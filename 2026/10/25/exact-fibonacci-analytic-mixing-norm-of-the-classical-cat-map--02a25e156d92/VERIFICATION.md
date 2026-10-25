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

# Direct verification and limits

The embedded `verify.py` is self-contained standard-library Python using exact integers. It checks the matrix-power Fibonacci identities implicitly by integer multiplication and independently enumerates the \(\ell_1\)-bounded search domain. Every minimizer must lie in the tested domain at finite horizon, since \(|k|_1+|A^n k|_1\ge |k|_1\), and the exhibited candidate already has value \(F_{n+3}\). Thus the check is finite-horizon exhaustive rather than heuristic.

Actual execution: `VERIFY_OK exhaustive_n=0..12 exact_integer_pairs= 1207324 minimizers_per_n=4 candidate_iterations=0..120`. The verifier confirms the four candidate frequencies and the exact minimum at all thirteen integer times, then checks candidate identities through time 120. Only the analytical sign-case argument establishes the universal result for arbitrary nonnegative time. An uninspected historical equivalence remains possible. Independent audit was not performed.
