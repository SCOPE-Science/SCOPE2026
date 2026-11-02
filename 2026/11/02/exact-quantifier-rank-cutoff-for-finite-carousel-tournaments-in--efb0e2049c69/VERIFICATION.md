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

# Verification record

Execute `python3 verify.py` in the directory containing this file and the program. The program requires only the Python standard library. Its output must equal `verification_output.txt` exactly.

The program checks direct recursive semantics of the two interval-threshold formula families for 18,600 cases and independently computes full three-variable formula-type refinement for odd tournament orders three through 39 and quantifier ranks zero through five. All assertions passed in the recorded run. The sample does not provide a proof of the arbitrary-rank theorem; that theorem is established by the mathematical induction and game strategy in `RESULT.md`.

The source-paper comparisons are not historical-priority certification, and this verification is not an independent mathematical audit.
