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

# Reproduction and analytical scope

Execute `python3 verify.py` from a directory containing the supplied standalone file. The standard-library script deterministically prints `VERIFY_OK 42521` when all its assertions hold. No packages or downloaded data are required.

The tests include 5,913 rational-polynomial identities for the strict-worsening factorization, 2,100 randomly selected condition numbers and angular bounds with numerical checks of both endpoint optimality and all sampled interior angles, 1,700 randomly chosen unshifted-worsening thresholds, 800 independent trace/determinant eigenvalue calculations, and eight asymptotic spot checks. These are finite samples, not infinite proofs or exhaustive numerical searches.

The mathematical proof covers **all** real `kappa>1`, `0<=Phi<=pi/4`, fixed `theta>0` and unknown angle in `[0,Phi]`. It establishes an exact scalar invariant and proves the global unique minimax and exact cutoff using algebraic monotonicity and factorization, without relying on sampled values. No independent mathematical audit has been performed; no claim of numerical implementation certification is made.
