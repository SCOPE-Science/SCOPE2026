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

# Reproducible checks

Run `python3 check_sections.py` from this directory using Python 3 and its standard library. The successful output is:

```
EXACT_SECTION_CHAMBERS_OK 21151 positive cones and symbolic edge sets OK
HAAR_EXPECTATION_MC_OK [('lo', 0.25, 6.74956, 6.76182), ('lo', 0.5, 7.37456, 7.37398), ('lo', 0.75, 7.78722, 7.77844), ('hi', 0.25, 7.126, 7.11557), ('hi', 0.5, 6.22633, 6.23164), ('hi', 0.75, 5.41589, 5.41583)]
```

The script independently generates vertex-edge graphs for the lower, joining, and upper regimes, verifies vertex and edge counts, and compares exact edge-sign crossings to the chamber indicator formulas over 21,151 eligible integer-normal and rational-parameter configurations. It checks explicit support witnesses for the 3+1+4 possible counts across five rational scales. Finally, rotationally invariant Gaussian normals test the exact angular-mean identities at six values. The Gaussian comparison has a declared numerical tolerance and is not a rigorous probability certificate. The all-parameter assertions, excluded boundaries, and strict derivatives are established symbolically in `RESULT.md`; the finite replay is supplementary. No external validation was performed.
