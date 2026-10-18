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

The standalone `verify.py` executed under Python with SciPy available. Its output was:

`PASS: 112 exact rational moments / spectral quadrature / background-driving / boundary assertions`

The program uses five rational parameter quadruples and compares moments of orders zero through eight from exact stationary-generator recurrences to independent exact Taylor-series calculations of the Fourier transform. It checks direct numerical integration of the Lévy–Khintchine exponent, and the integrated OU background-driving exponent, at four sets of physical rates and four Fourier frequencies. It separately checks the sign boundary, critical equality, and recovery of the equal-switching formula published in the original physical paper.

The mathematical proof does not rely on finite numerical checks. The quadrature assertions have finite floating-point tolerance and are not rigorous interval certificates. The generic class-\(L\) implication uses the classical canonical Lévy-density theorem; this is cited, not reproved from scratch. No independent audit has yet been performed.
