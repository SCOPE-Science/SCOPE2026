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

The proof of the statement for all \(n>1\) with \(\omega(n)\le6\) is symbolic, except for a finite prime check bounded by \(383\), exhaustively covered by the standalone `verify.py` and the exact `support_catalog.csv` table.

Run `python3 verify.py` in the directory containing both supplied files. The script uses only the standard library. It reconstructs every prime candidate, checks all rational thresholds and every catalog row, and evaluates Dedekind psi and Euler's totient directly for all \(2\le n\le400000\). It checks exact agreement with the structural predicate rather than using a term table to identify the result.

The finite integer sweep is corroborative. It is not presented as proof of the unrestricted classification, which follows from the inequalities in `RESULT.md` and the finite upper bound \(v<384\).
