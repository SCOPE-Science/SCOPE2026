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

# Reproducibility and verification

The included `verify.py` uses `mpmath`, `numpy`, and `scipy`. Run `python verify.py`. It evaluates the exact Bessel integral representation, independently solves the radial coupled boundary-value problem at twelve sets of geometric and rotational parameters, checks the absorbing endpoints, verifies all boundary signs, and compares high-rotational-diffusion scaling and the sharp outer-wall quadratic layer. All 171 finite diagnostic assertions passed in the supplied execution.

The proof, not this finite test suite, establishes the asymptotic assertion for every fixed annulus ratio, the strict sign inequality, analytic weak-swimming expansion, and local simple-root law. The asymptotic is sequential: take the speed derivative first and only then let rotational diffusion grow. No finite nonzero-speed assertion or independent audit is represented by these checks.
