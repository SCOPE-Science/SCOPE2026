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

# Verification record

The proof relies on four independently inspectable identities: (i) the equilibrium renewal-age survival law \(\Pr(A>a)=(1+a/b)^{-\alpha}\); (ii) the bivariate integrated Brownian covariance \(\left(\begin{smallmatrix}1/3&1/2\\1/2&1\end{smallmatrix}\right)\) with determinant \(1/12\); (iii) dominated passage from an exact Lomax survival formula to Gaussian-weighted tails; and (iv) positive-normal power tilting, Gaussian conditional regression, and strict likelihood-ratio ordering. The exact \(\alpha=3/2\) integral is also evaluated analytically in `RESULT.md`.

Reproduction: run `python checks.py` in the same directory, using NumPy and SciPy. The checks compare separate analytic formulas and deterministic numerical integrations, and check large-but-finite conditional events against the exact limit. These are corroborative finite checks, not a computer proof of the infinite tail or of universal monotonicity. There is no independent audit evidence.
