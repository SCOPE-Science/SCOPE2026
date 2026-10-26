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

Run `python3 verify.py` and then `python3 check_witness.py` in the folder containing the artifacts; no nonstandard packages are needed. The first script re-derives the exact four-endpoint dynamic program, cross-checks its output against an independently implemented explicit-hypothesis bitset recurrence for all \(0\le n\le16\), and then checks both sides of each of the ten claimed minimal-length transitions. It also generates `depth10_n52_witness.json` and validates all \(1024\) root-to-leaf paths directly against concrete ordered pairs \((a,b)\), not merely by trusting dynamic-programming ranks.

The second script reads the supplied witness from disk and independently verifies all its paths. In the recorded execution, there were \(708345\) distinct cached normalized states, the threshold sequence was \(1,2,3,5,8,12,17,25,36,52\), and `ALL_CHECKS_OK` was printed. The exact integer calculations are finite checks. The all-length correctness guarantee derives separately from the proved four-interval closure and recurrence. The verification does not establish historical priority or constitute independent mathematical review.
