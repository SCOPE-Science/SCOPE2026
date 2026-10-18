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

The exact symbolic derivation in RESULT.md holds for every integer \(n\geq3\). The separate reproducibility program `check_metric_face.py` independently constructs the normalized consecutive-cut vertices as rational matrices and checks the claimed centers, radii, determinant, and volume by exact rational arithmetic for all \(3\leq n\leq10\). Run with `python3 check_metric_face.py`; it requires no external Python packages. The finite checks do not certify statements outside the tested range; universal validity rests on the discrete Green-kernel and barycentric-distance proof. The initial source is the arXiv text of Erickson and Kretschmann (arXiv:2311.07522, 2023-11-13). Independent mathematical audit has not been performed.
