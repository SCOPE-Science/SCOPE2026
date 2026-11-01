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

# Verification procedures and limitations

Execute `python checks/verify.py` with NumPy installed. The script uses the independent trihedral determinant/atan2 formula on three distinct planar polygonal bases and a geometric sequence of 75 positive heights, and checks each base-vertex and apex angle. The analytic proof, not finite sampling, establishes monotonicity in every dimension. The Gaussian integral identities follow by conditioning on vertical normal coordinates, while nested translated cone geometry proves the required strictness. No external independent audit has been performed.
