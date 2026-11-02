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

# Verification and reproducibility

Run `python verify.py` with Python 3, NumPy and SciPy. The bundled script performs direct density-matrix propagation with a 16-by-16 GKLS Liouvillian, rather than assuming the reduced transfer formula. It tests 825 different \((J,\gamma,p,t)\) parameter combinations (three coupling choices, eleven decay choices, five charger populations and five time choices), including weak/strong dissipation, the critical point, and the overdamped regime. For each, it checks trace, positivity, independently calculated ergotropy, battery excited population and squared energy coherence. It additionally checks threshold roots and ordering for fifteen lobe indices, strict peak/passivity comparisons on either side of the roots, the exact window count for thirteen damping values, universal peak curvature, the square-root width ratio near four critical lobes, the large-index root asymptotic, and numerical quadrature of all positive-work windows for five small damping values against the Catalan-constant limit.

Replayed output:

```
PASS: 4348 exact-identity/numerical checks, independent GKLS comparison and threshold tests
critical k,x,gamma/J: 0 0.255275637649 1.021102550595
critical k,x,gamma/J: 1 0.074520240857 0.298080963427
critical k,x,gamma/J: 2 0.044334071096 0.177336284386
critical k,x,gamma/J: 3 0.031594433915 0.126377735658
```

Tests have bounded parameters and numerical tolerances; they cannot prove uniqueness of every critical root, the infinite threshold ordering, the all-parameter exact interval count the global-time limit or the limiting exponents. These follow instead from the analytic monotonicity of \(F_k\), exact single-lobe maxima and a Taylor expansion at the nondegenerate peak. No independent audit has been conducted.
