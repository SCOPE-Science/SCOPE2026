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

The standalone standard-library script `verify.py` implements the explicit finite Taylor-jet polynomial for \(\mathcal F_f(q)=\lVert1-qf\rVert_{H^{2m}}^{2m}\) and independently approximates the normalized circle integral with 8192 equally spaced nodes. Its Schur-parameter implementation reconstructs a finite Blaschke product from the truncated input jet and compares Taylor coefficients and boundary moduli. It tests triples \((m,n,L)=(2,1,1),(3,2,4),(4,1,3)\), using two distinct genuine inner rational factors of matching jets. It then checks the sharp cutoff identity \(\mathcal F_{z^L}(1+z^n)-\mathcal F_{-z^L}(1+z^n)=-4m\) at \((2,1),(3,2),(4,1),(5,3)\).

Execution: `python verify.py`. The exact reproducible output is embedded as `verification_output.txt`, ending in `ALL TESTS PASSED`. A reviewer can inspect the implementation and run it from these two local files. No external packages or network are required.

**Limits.** Quadrature is approximate, and the parameter tests are finite. Universal correctness is supported by the exact boundary binomial identity, Fourier coefficient truncation, strict convexity, and the finite Schur construction proved in `RESULT.md`. The test code does not independently certify originality or the infinite family of assertions; independent audit was not performed.
