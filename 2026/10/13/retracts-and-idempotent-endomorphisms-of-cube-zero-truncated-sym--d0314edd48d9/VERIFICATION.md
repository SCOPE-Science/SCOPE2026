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

# Reproducible verification

Run `python3 verify.py` using Python 3.8 or later; no third-party packages are required. The code reconstructs the truncated algebra \(K\oplus V\oplus\operatorname{Sym}^2V\), builds the full induced degree-two maps from independent linear projections, and checks the linear constraints over prime fields.

**Matrix-kernel check:** for \((r,q)=(1,2),(2,2),(2,3),(2,5),(3,2),(3,3)\), exhaustive enumeration of all \(r\times r\) matrices tests the idempotent linear parts, computes kernel dimensions of quadratic conditions, and matches each rank-stratum formula. Results include \(I_{2,1}(2)=48\), \(I_{2,1}(3)=324\), \(I_{3,1}(2)=3584\), \(I_{3,2}(2)=14336\).

**Direct full-map check:** for \((r,q)=(2,2),(2,3)\), enumerate all quadratic and linear coefficients, square the actual degree-two matrix of each algebra endomorphism, count idempotents, and compute canonical row-span representations of their images. The resulting rank-one image counts are respectively \(12\) and \(36\), with rank-zero and rank-full counts of one each.

The test program prints `VERIFY_OK` and `DIRECT_VERIFY_OK` upon successful completion. Only prime fields appear in this executable; the proof handles all finite prime powers and arbitrary fields. Finite enumeration cannot replace the symbolic proof or establish publication originality. Independent audit has not been performed.
