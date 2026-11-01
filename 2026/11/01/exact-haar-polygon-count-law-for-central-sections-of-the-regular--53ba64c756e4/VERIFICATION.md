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

# Checks performed

The analytic proof in `RESULT.md` partitions all generic directions through the exact signed-permutation chamber and counts crossed facets. Its critical steps are the square-face intersection criterion, the four opposite hex-face-pair criteria, the resulting three indicator functions, and the exact three spherical-cone areas. The independent finite program `check_section_law.py` was run from its actual local file and reported:

```
24 vertices, 14 facets, 36 edges
Exact integer-normal checks: 10690
Normal-chamber probabilities: {6: 0.4984506899177035, 8: 0.31610885558019075, 10: 0.18544045450210575}
Independent Gaussian-normal frequencies: {6: 0.497, 8: 0.316575, 10: 0.186425}
All checks passed
```

The exact integer tests are finite and the orientation sampling is statistical. Neither establishes the universal statement without the analytic proof. The code uses only Python's standard library and can be run as `python3 check_section_law.py`. Its vertex/facet and edge constructions are independent of the analytic chamber formula, while its solid-angle routine evaluates the displayed cone identity. Directions making a vertex lie in the plane have zero Haar measure and are excluded by the theorem. Historical originality has not been independently certified, and there has been no independent audit.
