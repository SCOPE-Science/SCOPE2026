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

Run `python check_sparse_mutualism.py` in the directory containing the scientific files. The exact-rational script checks 964 parameter/group configurations, balancing both constructed equilibrium branches and using Sylvester's criterion for the symmetric full-state Jacobian factor. It also checks the fold identity. The executable file included in this package is the one used for the numerical checks.

The proof additionally requires verifying (1) the factorization of the Jacobian, (2) the eigenvalue of the unregulated principal block, (3) the scalar quadratic equilibrium reduction, and (4) the signs of the remaining full-state modes. These steps are supplied in `RESULT.md`. The bounded exact arithmetic samples are not an infinite proof. No external independent scientific audit has been conducted.
