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

# Reproducibility and evidence

Execute `python3 verify.py` using Python's standard library. The checked output in `verify_output.txt` is:

```
ALL CHECKS PASSED: 365
q=0.1 uniqueness probabilities at phases 0,1/2: 0.4228450039085308 0.35864555478618615
first Fourier coefficient magnitude: 0.022262606886656395
```

The executable enumerates all uniform nontrivial package sizes for coupon counts \(3\le n\le7\) and collection rounds \(1\le t\le6\), comparing exact rational dynamic transitions with an independent exact inclusion–exclusion formula for every achievable terminal multiplicity. It also checks the normalization of the proposed Poisson terminal-event probabilities, numerical phase integration against the asserted logarithmic-series masses for three package fractions and seven terminal multiplicities, and the predicted magnitude of a nonzero Fourier coefficient.

The finite calculations do not prove convergence or nonconvergence for arbitrary coupon counts. The infinite assertions are established analytically using finite-label hypergeometric comparison, multivariate factorial moments, last-time tightness, exact Fourier/Mellin integration and logarithmic equidistribution, all written in `RESULT.md`. The generated checker output is not evidence of independent mathematical certification.
