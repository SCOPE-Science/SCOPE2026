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
# Verification and reproducibility

The exact theorem is proved in `RESULT.md`. Run `python3 verify_invariants.py` from the same directory to reproduce the checks. The program has no nonstandard Python dependencies and uses `fractions.Fraction` for exact arithmetic.

Observed checks: 100 exact rational transformations for degrees \(L=1,\ldots,5\), with unchanged \(K_i,J_i\), covariance of \(\Delta_S\), and sign preservation; centered finite-difference checks for a representative polynomial vector field at degrees \(L=1,2,3\); 240 exact rational checks of the barycentric differential identity for degrees \(L=1,\ldots,6\). All checks passed on the packaged script.

The proof, not these experiments, establishes infinite-parameter identities, independence, and orbit separation. No tests are asserted for collision strata, zero base divided difference, or passage through projective infinity. Independent audit is not performed.
