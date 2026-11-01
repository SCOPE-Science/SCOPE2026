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

# Reproducibility checks

Run `python verification_partition.py` (requires SymPy) to reproduce the exact six-cell conic partition, the symbolic vertices and area normalization, and the associated numerical solid angles. Run `python verification_faces.py` (requires NumPy) to reconstruct all 24 vertices, all 14 faces, and check the facet-crossing count against the proved indicator formula for 40,000 deterministic random normals. Their captured outputs are `check_partition_output.txt` and `check_faces_output.txt`. The latter reports zero disagreement. The probabilistic verifier is nonexhaustive; the analytic line-partition proof covers all generic normals. Source arXiv:0909.0940 anchors the known solid's geometry; arXiv:2412.12419 is related general background rather than a proof of the reported distribution.
