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

# Reproduction and limits

Run `python3 verify.py` with Python 3 standard library only. The checked execution printed:

```
VERIFY_OK exact_rational_assertions=3952 cases=3
```

This program independently clips rational convex polygons with rational halfplanes, checks the middle-slice cap algebra for three polygon families over rational directions and thresholds, identifies a strictly positive cap imbalance for two incomparable centered rectangles, checks the nested limiting halfspace witnesses, and verifies the rational sharp one-third witness profile for seven thin crossed-rectangle pairs. The calculations are exact rational arithmetic, with no floating-point decisions.

The all-dimension theorem is proved analytically in `RESULT.md`; tests over finitely many directions do **not** establish an infimum or supremum over all directions, nor prove geometric inclusion. Separate analytic arguments establish quasiconcavity, nesting equivalence, sharpness, and strictness for the equal-volume bound. The literature comparison remains a documented best-knowledge originality assessment; an independent scientific audit has not been performed.
