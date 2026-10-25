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

# Reproducibility and limits

Run `python3 verify_multiorder.py` with a standard Python 3 interpreter. The script explicitly constructs each admissible finite signed-coordinate permutation fixing a labeled base ranking configuration, acts on every possible one-point insertion-slot vector, computes orbit sets by canonical representatives, and compares their counts with the binomial product formula. It independently checks the group size and global extrema over the listed small configurations, including reversed ranking representatives.

A completed run produced the adjacent `verification_output.txt` file and ended in `ALL_CHECKS_PASS; type_action_instances= 987 extremal_instances= 14`. The unrestricted statement for all dimensions, numbers of parameters and coordinates follows from the mathematical proof in `RESULT.md`; finite tests alone would not establish it. The code requires no third-party packages. No independent mathematical audit has been performed.
