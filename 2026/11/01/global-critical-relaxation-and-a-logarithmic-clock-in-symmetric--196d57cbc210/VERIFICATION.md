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
# Verification record

The delivered standalone `VERIFY.py` was executed with SymPy and mpmath. It checked exact symbolic rational coefficients in the Taylor jet of the second diagonal iterate and inverse-square increment, and tested the exact algebraic mean/imbalance identities against the original two-species map at four coupling values with both signs of the initial slow variable. It additionally checked quadratic graph invariance and finite-iterate leading and logarithmically centered critical asymptotics.

These computations are reproducibility and arithmetic checks. The infinite proof of global convergence comes from the cited Ricker convergence theorem plus exclusion of noncoexistence limits. The invariant graph, null preimage exceptional class, and infinite-time logarithmic asymptotic are established analytically, not inferred from numeric samples. The complete texts of some older comparison papers remained inaccessible, leaving a priority risk. No independent mathematical audit has been performed.
