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

# Verification scope
The standard-library script `verify.py` reproduces a rational exact-volume moment integration for the three-cycle polytope, with diagonal variance \(23/576\), off-diagonal covariance \(-29/2880\), and condition number \(48/19\). Its independent truncated transfer traces and Fourier diagonalizations cover ten finite cycle sizes and compare the resulting covariance eigenvalues with the limiting symbol. It checks the endpoint identities and derivative numerically using absolutely convergent sums.

Execute with `python3 verify.py` in the directory containing this file and RESULT.md. The expected output is `VERIFY_OK exact_small_simplex=1 sampled_spectral_lengths=10 symbol_checks=10`. Numerical truncations and finite tests are not infinite proofs; RESULT.md provides the operator norm remainder estimate, strict derivative sign and asymptotic Taylor argument. Only self-review has been performed; no independent audit or independent verification is claimed.
