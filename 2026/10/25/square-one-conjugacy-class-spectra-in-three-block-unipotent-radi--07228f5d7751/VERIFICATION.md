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
The general proof derives the group law, the square-one condition \(XY=0\), the compatible-rank count \(N_{r,s}\), and the conjugacy-orbit dimension \(as+cr-rs\) without computational assumptions. The maximum exponent follows from two sharp inequalities with explicit attainment cases.

Run `python3 verify.py`. The script constructs actual group elements over \(\mathbb F_2\) or \(\mathbb F_4\), computes inverses and all conjugates using literal matrix-block products, partitions square-one elements into complete conjugacy orbits, and compares the resulting class-size multiplicities against the closed Gaussian-binomial formula. Its tested parameter quadruples are (1,1,1,2), (1,2,1,2), (2,1,1,2), (1,1,2,2), (2,1,2,2), (2,2,1,2), (1,1,1,4), and (1,1,2,4). Success is marked `VERIFY_OK_THREE_BLOCK_SQUARE_ONE_CONJUGACY`.

Independent audit has not been performed. The finite tests do not establish the formula at arbitrary block size or arbitrary even field; that is the function of the proof. Existing literature covers the base three-block orbit mechanism, and completeness of historical-priority research is not established.
