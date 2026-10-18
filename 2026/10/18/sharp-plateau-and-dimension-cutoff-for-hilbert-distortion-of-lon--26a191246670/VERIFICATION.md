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

# Computational and analytic verification

Run `python3 verify_long_even_cycles.py` with Python 3; it uses the standard library only. Expected exact output lines:

```
PASS: 90 exact rational vertex-shell/ellipsoid comparisons
PASS: 45 independent golden-section minimizations
PASS: dimension cutoff m<=15 and known four-cycle boundary
```

The script independently generates feasible cube-vertex and cube-edge/strip vertices, then checks the proposed outer shell formula by exact fractions. A separate golden-section minimizer evaluates the complete two-parameter objective at forty-five dimension/length choices, including dimensions beyond the plateau cutoff. The symbolic proof in `RESULT.md`, rather than any finite run of the program, verifies the infinite family and continuous domain. No independent scientific audit has been performed.
