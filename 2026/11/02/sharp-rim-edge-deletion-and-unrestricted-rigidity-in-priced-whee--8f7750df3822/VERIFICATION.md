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

# Reproducible checks

Run `python3 verify.py` with Python 3.10 or later. No additional packages or network access are needed. The verifier prints `VERIFY_OK 827 assertions` after all checks pass.

The code independently builds the standard weighted wheel Laplacian, solves finite real symmetric eigenproblems by Jacobi rotations, compares the exact candidate formulas against their spectral branches and budget, checks exact rational cases with \(n=3,4,6\), and challenges the global bound with reproducibly seeded nonsymmetric feasible random allocations. It also checks the threshold continuum and the inverse-square price limit numerically at two finite sizes.

The mathematical proof of uniqueness and all-integer validity is in `RESULT.md`, not delegated to numerical experiments. Finite random trials are not exhaustive, and numerical eigensolvers have floating-point tolerance. Search-based historical comparisons do not prove that no prior equivalent statement exists.
