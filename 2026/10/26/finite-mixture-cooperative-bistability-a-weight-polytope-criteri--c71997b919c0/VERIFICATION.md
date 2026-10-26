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

The full analytical argument, including quantifiers and endpoint hypotheses, is in `RESULT.md`. The accompanying self-contained `verify.py` uses only the Python standard library. Run `python3 verify.py` to obtain:

```
PASS: 1555 exact-rational assertions; general proof is separate
K = 20614528/2170899 ~ 9.495848494103134
```

The script checks the explicit polynomial identity for three rational perturbation parameters, its endpoint slopes, its positive curvature, and the exact coefficient of the quadratic opening law. It independently reconstructs an additional parameter point with exactly two interior roots, identified by a positive/negative/positive sign pattern and strict convexity. It also checks derivative and convexity formulas on a finite exact-rational grid. These checks are consistent with the formulas but are not exhaustive over mixture sizes, parameters or real-valued populations. The root bound, strict interval characterization, simplex halfspace feasibility and asymptotic law follow from the written mathematical proof, not the enumeration.

The model is deterministic and well mixed; finite-population and network dynamics are not checked. The possibility that prior literature contains an equivalent result is a priority uncertainty rather than a mathematical proof obligation. No independent audit evidence is asserted.
