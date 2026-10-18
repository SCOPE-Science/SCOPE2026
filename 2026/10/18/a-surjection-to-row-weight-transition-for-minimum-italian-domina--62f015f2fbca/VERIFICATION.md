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

# Reproduction of the finite checks

Run `python3 verify_italian_rook.py` with a standard Python 3 installation. No third-party modules or input files are required. Its output is included in `verification_output.txt`. The script counts all labelings with total weight no larger than \(\min\{n,2m\}\), constructs adjacency from shared rows or columns, and directly tests the required defending-neighborhood weight at every zero vertex. The nineteen graph profiles and expected counts are printed explicitly. A successful run ends with `VERIFICATION_OK 19`.

This is finite exhaustive validation only for the listed dimensions; it is not an exhaustive check for all integers and does not replace the mathematical proof. The general argument is the zero-column versus nonempty-column dichotomy in `RESULT.md`.
