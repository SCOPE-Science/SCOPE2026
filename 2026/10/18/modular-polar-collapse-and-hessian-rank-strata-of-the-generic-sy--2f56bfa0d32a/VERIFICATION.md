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

Install the declared dependency with `python3 -m pip install -r verification/requirements.txt` and run `python3 verification/check_hessian.py` from the package root. The script computes actual symbolic determinants, ordinary second partials and gradient polynomials for symmetric matrices with independent upper triangular coordinates, with exact arithmetic. It verifies the Hessian polynomial identity symbolically at \(n=3\), checks an independent full-rank specialization at \(n=4\), and tests Hessian ranks and characteristic-two polar degeneration modulo small primes at canonical matrix representatives. Its expected final line is `VERIFY_OK`. Run `cd verification && python3 random_checks.py` to exhaust all 64 symmetric 3-by-3 matrices over the binary field and check 150 reproducibly sampled symmetric 4-by-4 matrices. This second script verifies both the reduced base-support criterion and the pointwise Hessian-rank formulas; it ends with `FINITE_SPOTS_OK`.

Proof of the infinite-family identity is the integral congruence-covariance argument and identity evaluation in RESULT.md, not interpolation of finite examples. Proof of the characteristic-two base support is the adjugate rank stratification and the alternating-inverse condition. Proof of all Hessian ranks is the explicit 2-jet in each matrix-corank stratum, plus the classification of nonsingular symmetric bilinear forms. No full primary decomposition or nilpotent/embedded structure of the base ideal is claimed. The self-review has passed; no independent audit has been performed.
