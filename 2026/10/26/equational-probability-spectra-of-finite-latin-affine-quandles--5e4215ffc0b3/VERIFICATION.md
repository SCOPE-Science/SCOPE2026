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

Run `python3 verify.py` in the directory containing the standalone verifier. The program constructs actual two-variable term coefficients by finite closure under the Alexander operation, constructs the independent polynomial-evaluation ring, compares the two sets, computes possible equation ranks, and directly tests solution counts in eight small examples. The reproducible success marker is `VERIFY_OK cases=8`. The tested cases cover characteristic two with irreducible degree-two and degree-three actions, characteristic three with a nontrivial Jordan block and decomposable scalar actions, and characteristic five with split eigenvalues.

The general proof does not rely on finite computation. Its critical arguments are coefficient reachability via translations, principal-ideal image reduction for arbitrary equations, and elementary-divisor kernel counts. No independent scientific audit has been performed. The exact result is limited to finite-dimensional prime-field vector spaces with both affine multipliers invertible, in the binary quandle language with no constants or division operations.
