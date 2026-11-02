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

Run `python3 check.py` (Python 3.9+, standard library only). The checker uses exact quadratic-field rational arithmetic for all 25 Fourier eigenvalues in each degree \(0\le\ell\le47\), tests exact nonnegative signs, confirms the rank list and checks the unique constant-character null direction at degree six. Explicit degree-five and degree-six rational spectral multisets are also verified. It was executed successfully on the delivered source file.

This computation does not assert an infinite enumeration. For \(\ell\ge48\), use \(U_\ell(1)=\ell+1\ge49\), at most 24 off-diagonal entries, and the strictly smaller-than-two bound for each off-diagonal entry derived from the inner-product bound \(|t|\le(1+\sqrt5)/4<\sqrt3/2\). Strict diagonal dominance then proves full rank. The public proof specifies this deduction and the positive normalization of the spherical harmonic Gram matrix.

Originality was assessed by primary-literature comparison and bounded semantic searches. An equivalent result hidden in unindexed literature cannot be excluded. Independent verification has not been performed.
