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

# Reproducible verification

The included standalone `verify_spider.py` needs Python 3, NumPy, and SciPy. Run `python verify_spider.py` in a directory containing that file. The expected terminal line from the executable mathematical tests is:

```
PASS 1256 independent structural, numerical, and matrix tests
```

The program evaluates the closed-form optimal resistance diameter and edge conductances for heterogeneous random spider trees, then verifies total power-law expenditure, exact path-sum diameter, and the Laplacian pseudoinverse distance formula. It compares against 960 directly generated feasible nonsymmetric allocations, solves 18 instances through an independent constrained numerical optimization on arm radii, and checks special rational and power-exponent-transition cases.

The deterministic tests use pseudorandom seed `194002`. Matrix verification is subject to numerical tolerances of order \(10^{-8}\). Numerical minimization is checked to relative error \(2\times10^{-6}\); this is not a global symbolic certificate. The all-size, all-parameter claim relies instead on the strict convexity and one-variable reduction proof in `RESULT.md`. No external or independent scientific audit is claimed.
