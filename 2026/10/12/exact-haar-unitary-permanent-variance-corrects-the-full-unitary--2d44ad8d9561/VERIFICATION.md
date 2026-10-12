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

The all-parameter proof is analytic: `RESULT.md` identifies the permanent with a matrix coefficient of \(\operatorname{Sym}^n(\mathbb C^n)\), applies Schur orthogonality, and then uses Stirling and Markov.

The bundled `artifacts/verify.py` checks the factorial/binomial identities exactly for \(1\le n\le100\), verifies the first nontrivial value \(1/3\) at \(n=2\), and confirms the stated asymptotic ratio numerically at increasing \(n\). Those checks corroborate arithmetic only and are not used as an infinite proof.

The result does not test or certify a Gaussian limit after correct variance normalization, and it makes no claim for the small-submatrix, large-ambient Haar regime.
