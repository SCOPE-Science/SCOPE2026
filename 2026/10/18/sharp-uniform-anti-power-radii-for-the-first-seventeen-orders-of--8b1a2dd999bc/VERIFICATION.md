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

Execute `python3 verify.py` with Python 3 standard library. The program checks the exact finite values at orders \(2,3,4,5,8,9,16,17\), tests every distinct prefix factor of each required length, independently reconstructs the paperfolding word by both a recurrence and an odd-part formula, and compares two factor enumerators. The complete-factor cardinalities are \(12,60,96,140,224,324,576,1020\), matching the published theorem at the corresponding lengths. Every factor supports at least one permitted anti-power; a concrete factor for each row excludes all smaller block lengths. The mathematical monotonicity argument supplies the other orders through \(17\).

The program enumerates a finite prefix only. The step from those factors to **all** positions of the infinite word relies on the independently published exact factor-complexity theorem. This is not independent verification by another scientist; it is a reproducible exact program checked during self-review. No result at any order greater than \(17\), except the monotonic lower bound, is verified or asserted.
