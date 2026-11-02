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

# Direct checks and limits

Execute \(\texttt{python3 verify\_rule110.py}\) with a standard Python 3 interpreter. The checked standalone script prints \(\texttt{VERIFY\_OK}\).

The script enumerates every input on each binary ring of length 1 through 13 by the literal Rule-110 truth table; it tests the all-one preimage count against the Perrin sequence, the all-zero preimage count against two, the exact weight envelope for every output, and uniqueness of the maximum from ring length five onward. A distinct four-state de Bruijn matrix is built independently from the same truth table and its cyclic trace is checked for every output through ring length seven.

The proof's nonstandard steps are the exact three-state trace bijection and the entrywise domination by identity on zero-labeled steps, given explicitly in RESULT.md. The all-length conclusion relies on those steps and the elementary Perrin recurrence, not on the finite computation. Publication-priority verification of inaccessible related full text and any independent expert review remain unperformed.
