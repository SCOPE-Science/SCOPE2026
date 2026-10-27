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

# Reproduction and verification

Run `python3 verify.py` in the directory containing this document and the accompanying result. The script uses Python standard library only. It enumerates all ordered representation pairs independently for every integer below \(4^k\) at \(0\le k\le7\), checks each multiplicity against the separate base-four scalar recursion, and compares exact covered/unique/maximal values with the closed formulas. It directly checks the digit-carry transition matrix by enumeration of all four pairs of digits, and conducts additional state-vector checks for \(1\le k\le14\).

Expected terminal line:

`PASS: direct pair enumerations \(k=0\)..7 and state-vector checks k=1..14`

These are finite reproducibility tests. The global claims and boundary cases are established by the complete symbolic carry-state and induction arguments in `RESULT.md`, which must be checked mathematically rather than inferred from finite tests. External independent audit has not been performed.
