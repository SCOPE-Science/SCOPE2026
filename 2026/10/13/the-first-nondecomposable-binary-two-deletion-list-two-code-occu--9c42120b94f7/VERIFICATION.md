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
The standalone `verify.py` enumerates all two-deletion shadows, checks ten explicit codebooks for \(3\le n\le7\), and verifies all dual column inequalities in exact integer arithmetic. The \(n=2\) case is immediate from its unique empty descendant. It checks the strict comparison at length seven and the absence of one at shorter lengths. Execute `python3 verify.py` from the directory containing this file. Actual run output ends in `VERIFY_OK`.

The dual certificate is a finite complete proof, not statistical testing or incomplete enumeration; both the primal constructions and dual inequalities range over every relevant finite word. No computation proves analogous behavior for longer blocklengths. No external validation was performed.
