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

# Verification of cyclic Rule 178 entry times

Reproduction requires the standard Python 3 library and the companion `verify_rule178.py` in the same directory. Run `python3 verify_rule178.py` to compare the direct local-rule dynamics with the wall-gap formula and the cyclic-composition counting formula.

The executable enumerates all \(262136\) labelled configurations for ring sizes \(3\le n\le17\). It records the first occurrence of a repeated global state to determine the actual first-periodic-entry time and least period. It separately checks the exact coefficient formula, the number of primitive two-cycles through the Lucas identity, and the terminal-shell counts. The recorded output file `verification_output.txt` ends with `RULE178_ALL_CHECKS_PASSED; enumerated_states= 262136`.

The proof for arbitrary ring length is in `RESULT.md`. A finite enumeration is not a replacement for that infinite-family argument. The logarithmic random-time law is established by mathematical probability inequalities in the proof, not by simulation. Independent validation has not been performed.
