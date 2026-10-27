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
# Verification of the matching perfect-coalition census

The standalone `verify.py` uses only the Python standard library. It constructs the \(2n\)-vertex matching directly, enumerates each unlabeled vertex partition exactly once by restricted-growth strings, and tests every possible coalition pair using the original open-neighborhood restrictions and perfect-domination condition. It never calls the proof's edge-type support classification to decide whether a partition is valid.

Run `python3 verify.py`. Checked outcomes for \(n=2,3,4,5\): respectively \(1,30,364,3480\) optimal four-class partitions. The partner-type profile in \((C_4,P_4,2K_2)\) order is respectively \((1,0,0)\), \((6,24,0)\), \((28,288,48)\), \((120,2400,960)\). The actual script run produced all assertions passing. The program also verifies that no partition with more than four classes exists in this finite range.

These tests do not constitute exhaustive verification for every \(n\); the independent unlimited-\(n\) argument is the graph-cover proof in `RESULT.md`. No independent external audit has been performed.
