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

# Verification and scope

The mathematical proof is in `RESULT.md`. The executable companion `CHECK.py` requires Python 3 with NumPy, SciPy and SymPy. Running `python CHECK.py` on the supplied source produced:

```
PASS: 25 symbolic, endpoint, and deterministic quadrature assertions.
Quadrature checks finite-parameter agreement with asymptotic limits; it does not prove them.
```

The symbolic checks evaluate both branches of the curvature-scale integral, the corner-scale four-dimensional integral, and endpoint consistency. The numerical checks evaluate the exact Euclidean separation inequality for pairs close to opposite square corners by Gaussian quadrature after a change to inward sum/difference coordinates. The numerical test values approach three distinct asymptotic regimes; they cannot replace the proof's localization and dominated-convergence steps.

The parameter restrictions, normalizations, quantifiers and no-uniformity disclaimer are given in `RESULT.md`. The work has not undergone an independent audit.
