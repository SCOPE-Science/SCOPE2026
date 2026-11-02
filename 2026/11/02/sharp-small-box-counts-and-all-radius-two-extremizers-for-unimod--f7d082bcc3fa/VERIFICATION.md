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

Run `python3 verify.py` from the directory containing this file and `verify.py`. Python 3 standard library only; no network or external data are required.

The program exhaustively evaluates 256, 2,401, 10,000 and 28,561 reduced starting quadruples for block widths 2, 3, 4 and 5. It uses exact determinant equality. For each maximizing tuple it independently checks the count via the linear equation for a second column, and it crosschecks 1,200 further tuples using both formulas. At width five it checks all eight maximizing starting blocks, all five values in each of the four coordinate blocks occur among counted matrices, and the origin/shifted counts are 52/60. The final line must read `VERIFY_OK width=2..5, all reduced starts, exact integer determinant, finite certificate`.

The reduction to finitely many cases rests on the proved Bézout completion argument in `RESULT.md`. The verifier alone does not establish that localization lemma or any assertions beyond radius two. Independent auditing has not been performed.
