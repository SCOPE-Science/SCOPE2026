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

# Direct scientific and computational checks

The pointwise theorem is certified here by its analytical folding-and-unfolding argument, not by a finite test. The script `check_crosspolytope.py` (standard-library Python 3) was executed on the actual included source; it passed 4,002 exact-rational equatorial-path and stretch configurations over dimensions 2 through 24, plus 23 exact-rational mean-square checks. The checker separately tested 180,000 area-uniform samples for the squared-excess tail, with maximum observed absolute tail error 0.00195556 at the specified 16 comparison thresholds and maximum floating squared-distance discrepancy 8.88e-16.

Checks of dimensions 2 through 24 do not imply the universal claim for all larger dimensions. The proof handles the quantifiers, both signs, vanishing coordinates, and antipodal target directly. The finite random sample does not establish the probability law, which follows from simplex barycentric integration.

Scientific scope: the source is a vertex, the metric is Euclidean arclength along the entire boundary, and the claimed distribution concerns the squared geodesic excess rather than the full random intrinsic distance.
