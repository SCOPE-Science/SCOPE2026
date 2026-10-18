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

The attached standalone `verify.py` runs using the Python standard library. Execute `python verify.py`. Its observed output is saved in `verification_output.txt`. The script generates all integer partitions of each size one through fifteen, models prime-primary face deletion, verifies \(\partial_1\partial_2=0\), repeatedly removes orbit triangles exposed on a unique orbit edge, computes full column ranks modulo 101 and 103, and verifies the four-triangle primitive integer cycle in degree two.

Free-edge elimination forces the coefficients of exposed triangles to vanish in any integral two-cycle; its residual four faces at fifteen form exactly a tetrahedral boundary. The rank calculations are exact finite computations, not probabilistic tests. Full modular column rank implies integral injectivity in ranks below fifteen. At fifteen, rank 23 modulo 101 combined with the explicit primitive kernel vector gives the exact integral kernel rank one. The separate absence-of-three-cells argument in `RESULT.md` identifies this kernel with degree-two homology.

Verification does not assess any mathematical assertion beyond ranks one through fifteen, nor does it constitute an independent external audit.
