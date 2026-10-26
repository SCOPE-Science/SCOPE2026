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

# Verification

The script `check.py` uses only the Python standard library. Running `python check.py` reported `CHECK_OK 2171` followed by the two numerical trace-envelope boundaries. Its exact-fraction tests check the Haar projector second moments against the beta/idempotence identities in dimensions 2 through 13, the coefficient invariants, and isotropic thresholds. Numerical matrix tests reconstruct the explicitly defined nonnegative variance operator on randomized positive spectra, compare its Perron radius below and above the critical scalar root, and check the trace-constrained extremizers with fixed dimension and endpoints. The sharp example in dimension four has critical steps approximately 0.3131948736438942 and 0.3375977868030830.

The printed count is a finite software check, not an exhaustive proof. The document `RESULT.md` contains the separate analytic derivation of the second-moment operator, the positive rank-one secular condition, and convex-majorization extremal characterization. Floating-point Perron and bisection checks have ordinary rounding error. No independent audit has been performed.
