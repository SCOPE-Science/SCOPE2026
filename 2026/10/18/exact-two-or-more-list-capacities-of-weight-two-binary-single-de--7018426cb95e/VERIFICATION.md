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
The file `verify.py` constructs the promised codes and directly enumerates distinct deletion descendants, checking every possible output's list multiplicity. The recorded `verification_output.txt` contains successful runs of 150 (blocklength, list-size) combinations for blocklengths 2 through 24 with selected list sizes, as well as complete subset enumeration for all blocklengths 2 through 6 and list sizes 2 through n+1.

To reproduce, run `python3 verify.py`. The enumeration uses Python's standard library and has no external data dependencies.

These finite tests validate the explicit code, test small boundaries, and support the proof. Only the written combinatorial argument establishes the all-parameter theorem. Historical priority and independent external validation have not been certified.
