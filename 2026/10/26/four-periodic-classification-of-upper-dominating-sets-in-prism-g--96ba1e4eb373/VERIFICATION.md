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

Run `python3 verify.py` with Python 3 and no third-party dependencies. The program constructs the labelled graph independently of the proof, tests ordinary dominating and inclusion-minimal conditions for every subset of size \(n\) on \(C_n\square K_2\) for \(3\le n\le10\), and compares all sets—not just their number—with the stated three families. It also enumerates all subsets larger than \(n\) for \(3\le n\le8\). Its actual stdout is embedded as `verify_output.txt` and ends in `VERIFY_OK`. The unrestricted proof uses the private-neighbor counting argument and complete cyclic cut analysis from `RESULT.md`; finite verification is corroborative only. No external/independent audit has been performed.
