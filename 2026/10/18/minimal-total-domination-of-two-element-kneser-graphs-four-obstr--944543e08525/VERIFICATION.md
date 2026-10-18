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

# Executable verification

Run `python verify_minimal_total_kneser.py` with Python 3.9 or later from a directory containing the script. It uses only the standard library, independently builds \(K(n,2)\) from the rule that two vertices are adjacent when their base pairs are disjoint, exhaustively tests every nonempty selected subset for open-neighborhood total domination, and checks inclusion-minimality by removing each selected vertex individually. This implementation does not use the cover-number classification to decide whether a set is total dominating.

Direct checks for \(n=4\), \(5\), \(6\), and \(7\) enumerate respectively \(63\), \(1{,}023\), \(32{,}767\), and \(2{,}097{,}151\) nonempty subsets, totaling \(2{,}131{,}004\), and match every coefficient of the stated minimal-set polynomial. A separate arithmetic check tests log-concavity and unimodality for each \(4\le n\le80\), including both boundary orders and subsequent failures.

`verification_output.txt` contains actual program output reproduced in execution, finishing in `VERIFICATION_OK`. Exhaustive graph testing proves only those finite cases; the theorem for all \(n\ge4\) relies on the cover-number and criticality arguments in `RESULT.md`.
