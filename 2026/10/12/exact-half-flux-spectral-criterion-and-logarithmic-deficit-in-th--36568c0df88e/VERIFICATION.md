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

The proof uses the exact half-flux band inequality from arXiv:2302.04601v1. The two endpoint inequalities are algebraically reduced to factored expressions in \(s=\sin^2 k\), from which the exact spectral union follows for \(k>1\).

The bundled `verify.py` performs four reproducibility checks: it evaluates the published rational function and the factorized membership criterion at deterministic sample points; it solves the exact narrow-band boundary equations by bisection; it solves the exact central-gap equations by bisection; and it estimates the coefficient of the cumulative logarithmic term from the slope between two large cutoffs. A successful replay ends in `VERIFY_OK`.

The checker is finite and does not certify the infinite asymptotic theorem. The infinite statement rests on the displayed exact factorization, the elementary local scalings near \(n\pi\) and \((n+1/2)\pi\), and convergence of the summed \(O(n^{-2})\) remainders. No claim is made for fluxes other than \(\Phi=\pi\).
