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

The polynomial-frequency Fourier representation was checked against the source's exact Hardy–Sobolev normalization. The main proof contains the operator iteration identity, convergence of its supremum through uniform tails, explicit infinite-multiplicity eigenfamilies of the operator or its adjoint, and the small-displacement polynomial rescaling. These are the mathematical evidence for the infinite-dimensional conclusion.

The standalone `check.py` provides independent finite numerical diagnostics of the power limit and a pointwise complex-parameter eigenvector equation, not a certificate of a full spectrum. It was executed successfully for several polynomial orders and dilation/translation parameters. Independent mathematical audit has not been performed. The result makes no claim for negative displacement, complex dilation, or nonaffine symbols.
