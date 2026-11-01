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

## Reproducibility

Run `python3 check_geometry.py` from the directory containing this document and the accompanying script. The script needs only the Python standard library. Its deterministic random seed is set internally. The expected terminal summary is `PASS 12100 independent numerical comparisons`.

The script independently constructs all polygon vertices by intersecting consecutive tangents to the unit circle, computes convex-polygon areas by the shoelace formula, and compares them with the closed forms. It also checks selected majorization transfers, derivative signs, sharp endpoint products and the local second variation. For positive gaps, the vertices of the original polygon have polar angles midway between consecutive unit support normals and radii equal to the reciprocal cosine of half their angular separation.

These are numerical consistency checks for finitely many cases. The universal conclusion is justified by the elementary derivative and majorization proof in `RESULT.md`; the checker does not establish universal originality, independent audit, or any infinite claim.

## Boundaries

The proof covers all integers \(n\ge3\), \(k\ge2\), every nonnegative angular-gap vector summing to \(2\pi/n\), and boundary configurations with repeated rotations. Local stability has a fixed-parameter remainder. The paper comparison documents remaining historical-priority risk; no independent audit has been conducted.
