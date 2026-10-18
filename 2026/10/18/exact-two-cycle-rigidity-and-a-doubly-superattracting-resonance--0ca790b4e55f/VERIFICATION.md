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

The enclosed `verify.py` runs with Python 3 and SymPy (version 1.14.0 used in this check; see `requirements.txt`). It symbolically checks \(M^2=\mu I_2\), \(\mu=-7-16/a\) after \(a=-2(1+u^2)\), the derivative of the rational multiplier and the exact degeneracy parameters. It directly replays the full nonlinear two-cycle and both Jacobians for 28 rational parameter pairs and tests 200 rational stability-window comparisons.

Actual execution result:

```
PASS: 544 exact symbolic and rational checks
```

The global uniqueness of the prime two-cycle is proved by the eliminations in `RESULT.md`, not by finite test counts. Local hyperbolic attraction and repulsion use the two-step Jacobian and standard local hyperbolic theory. At the double \(-1\) point no nonlinear boundary conclusion is claimed. The verifier does not establish historical priority or independent validation.
