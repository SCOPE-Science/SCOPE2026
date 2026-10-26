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

# Reproducibility and analytical boundaries

The proof gives a convergent Laurent expansion, an exact periodized logistic kernel, and the Poisson Fourier series. The critical asymptotic comes from the second harmonic at the quarter-period and the first harmonic in the derivative. Their exponentially different scales produce a displacement of size \(e^{-2\pi^2/L}\), rather than an algebraic term in \(L\).

`verify_annulus.py` requires `mpmath==1.3.0`. Execute it using Python to reproduce `CHECK_OUTPUT.txt`. It compares independent direct-Laurent and Poisson sums at seven values of \(L\), brackets the distinguished zero by bisection, and evaluates the width-to-leading-term ratio. The maximum observed absolute duality discrepancy was below \(6\times10^{-102}\) with 100-digit working precision, and all seven ratios differed from \(1\) by less than \(3\times10^{-6}\). These tests do not prove the exact Fourier identity, uniform convergence, exhaustive scalar-root classification, or asymptotic limit; those rely on the written analysis and the cited qualitative classification.

The complete 2009 annulus source was inspected. A relevant earlier Eisenstein-series article was not available for full-text comparison. Independent audit was not performed.
