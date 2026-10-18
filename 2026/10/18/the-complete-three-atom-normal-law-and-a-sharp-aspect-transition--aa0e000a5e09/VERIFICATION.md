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

# Computational verification and limits

Run `python3 check_normals.py` with a standard Python 3 interpreter; it has no third-party dependencies.

The checker uses `fractions.Fraction` to clip each of the sixteen possible strict-sign chambers from the unit square against all four side-foot inequalities. It computes chamber areas with a rational shoelace formula and normal multiplicities using geometric vertex-cone tests. Across 87 rational angle/aspect pairs (including orthogonal, skew and exact transition cases), every probability equals the theorem's exact rational expression. Four further cases verify phase-boundary and extremal identities.

A separate numerical routine constructs the actual Euclidean side vectors and tests normal feet by orthogonal projection plus normal cones by dot products. It agrees with the chamber model at 1,250 deterministic interior samples over five geometries. Expected output:

```
PARALLELOGRAM_NORMAL_EXACT_OK rational_chambers=87 phase_extrema=4
EUCLIDEAN_NORMAL_POINTWISE_OK cases=1250
```

These are finite checks and do not establish validity for all real side ratios or angles. The analytical proof in `RESULT.md` handles the infinite parameter domain, the boundary and equality cases. Historical originality has only a self-review and has not been independently audited.
