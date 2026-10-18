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

The exact formula is proved for every finite radius-two tree with at least one edge and integer branch sizes \(a_i\ge0\); finite checking does not replace the proof. The standalone standard-library checker `artifacts/verify.py` independently computes the law by the first-available-edge recurrence over residual edge sets, and compares the complete probability dictionary against polynomial integration. On 452 branch profiles with at most ten edges it matched all 5,163 output points. Independently, it directly checked 189,821 uniformly weighted edge permutations on smaller profiles. It tested the strict all-positive nonuniformity witness on 21,840 parameter profiles and the double-star formula on 289 positive parameter pairs. All exact-rational assertions passed.

Run `python3 artifacts/verify.py` at the package root; the expected stdout is the complete single line in `artifacts/verify_output.txt`. The recurrence, enumeration and inequalities check the same stated theorem by different finite calculations. No exhaustive infinite enumeration, formal proof assistant verification, independent scientific audit, or priority certificate is claimed.
