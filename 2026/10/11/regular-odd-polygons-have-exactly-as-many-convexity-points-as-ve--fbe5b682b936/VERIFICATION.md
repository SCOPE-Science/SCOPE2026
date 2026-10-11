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

The general theorem is proved analytically in `RESULT.md` from the published middle-line characterization and exposed-point lemma.

The following source-dependent steps were materially checked in the primary texts:
- `arXiv:1504.00541`, Lemma 2: for bodies with no pair of parallel edges, a point is a convexity point exactly when every middle line through it has a middle set containing it.
- `arXiv:1504.00541`, Lemma 6: exposed points of the convex hull of all middle sets are convexity points.
- `arXiv:1607.03014`, Section 2 and the polygonal discussion in Section 3: for a polygon without parallel edges, the middle hedgehog is the polygonal union of the edge middle sets.
- `arXiv:1607.03014`, introduction: triangles and Reuleaux triangles are given as examples with precisely three convexity points, while a typical planar convex body is proved to have infinitely many.

`verify.py` checks the regular-polygon indexing, middle-set endpoint identity, and radius formula for many odd values. It is a sanity check only; the infinite statement does not depend on enumeration.

Scientific limit: the theorem does not classify even regular polygons or arbitrary odd polygons, and it does not claim that only odd finite convexity-point counts are possible in general.
