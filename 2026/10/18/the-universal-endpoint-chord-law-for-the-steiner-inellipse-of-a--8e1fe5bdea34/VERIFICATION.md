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

Run `python3 checker.py` with Python 3, NumPy, SciPy and SymPy. The checker verifies the conic/line criterion and the exact primitive symbolically, then compares the closed expression at nine scales against adaptive quadrature independently of the primitive. It also samples direct Euclidean segments and evaluates their geometric ellipse-hit condition for four nonsimilar triangles at five scales. The reported output was:

```
symbolic conic/incidence/primitive/endpoint checks: PASS
independent quadrature and small-scale checks: PASS 9 scales
direct physical ellipse/chord sampling: PASS 20 cases
```

All probabilistic geometry in the theorem is established by the analytic proof, not by finite simulation. The strict shape extremizers are consequences of the exact factorization and strict convexity of the sum of normalized squared side lengths. Extremely near scale one, use the integral expression or arbitrary precision because the closed form subtracts divergent intermediate terms. No independent audit has been performed.
