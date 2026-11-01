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

Run `python3 verify.py` from the directory containing that file. It requires only Python 3 and no network or external datasets. The output should match the complete contents of `verification_output.txt` byte-for-byte and finish with `PUNCTURED_HYPERCUBE_GF2_RANK_AND_STATE_CHECKS_PASSED: 7 dimensions, 51352 states`.

The program constructs GF(2) adjacency rows and independently checks power ranks and recurrence identities in dimensions 2 through 8. It enumerates each binary state in dimensions 2 through 4, each quaternary-field state in dimensions 2 and 3 (addition is bitwise XOR), and samples additional larger-dimensional states. Its exact output was reproduced in a fresh replay, matching `verification_output.txt`.

The mathematical proof in `RESULT.md` separately establishes the N/2 compression rank for all dimensions over every characteristic-two field, then reconstructs Jordan sizes and state populations analytically. These finite tests do not constitute independent audit, infinite computation or a replacement for the all-dimensional proof.
