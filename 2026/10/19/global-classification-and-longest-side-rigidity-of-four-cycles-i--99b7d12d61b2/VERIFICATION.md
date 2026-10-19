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

Run `python3 verify.py` with Python 3; no third-party packages are needed. The script evaluates exact rational orthogonal projections, independently enumerates all cyclic length-four line itineraries with no equal adjacent labels, solves each prescribed affine return, enforces the actual farthest-choice branch and tie rule, and compares the resulting least-period-four orbits against the analytic four-inequality predicate on all three candidate repeated sides. It also checks the exact quartic isosceles criterion.

Observed output:

```
CHECK_OK exact rational triangles: 236; grid cycles zero/one: [161, 43]
```

There are 204 triangles in the two-parameter rational grid, with 161 zero-cycle and 43 one-cycle cases, plus 32 additional isosceles checks. This finite exact-arithmetic diagnostic verifies formulas on its specified grid only; **it does not prove the full real-parameter classification**. The analytical proof in `RESULT.md` supplies completeness of the itineraries, uniqueness of the candidate, sufficiency/necessity of all switching tests, longest-side rigidity, the strict equality boundary, and the isosceles cutoff. Prior work already covered the acute isosceles threshold, which is not treated here as a new result. No external/independent audit has been performed.
