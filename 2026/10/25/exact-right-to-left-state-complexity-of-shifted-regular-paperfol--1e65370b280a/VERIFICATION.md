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

A standalone Python 3 program is provided at `verify.py` and its actual terminal output at `verification_output.txt`. Running `python3 verify.py` requires only the standard library.

The checker computes the regular paperfolding bit directly from the number immediately after its index. It independently enumerates all residual outputs over a finite continuation domain for every shift \(0\le c\le95\) and selected power-of-two boundary values, compares the number of distinct finite signatures against the stated formula, tests additional structural boundaries, and checks every residue-case identity on an explicit finite grid of shifts, prefixes and future inputs. All assertions passed in the recorded run.

This check is finite and cannot establish nonperiodicity, reachability for arbitrary shifts, or minimality in an infinite parameter domain. Those facts are proved mathematically in `RESULT.md`. No independent audit has been performed.
