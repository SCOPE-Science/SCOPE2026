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

# Reproducibility

Run `python3 verify.py` with a standard Python 3 interpreter. A successful run prints `VERIFY_OK cyclic_words=828 sorted_iterates=12 max_round=20`.

The program exhaustively examines 828 mixed cyclic \(11\)-avoiding words up to length 12, testing the entire transform formula by a direct cyclic-rotation sort and a separately implemented cyclic rank-doubling sort. It also tests the complete transform formula and the run counts on period-doubling iterates, directly sorting through exponent 13 and reconstructing the entire BWT by the recurrence through exponent 20.

These finite calculations verify concrete instances and implementation consistency only. The general formula and exact run count for arbitrarily large exponents require the four-block lexicographic proof in RESULT.md. No independent scientific audit has been performed.
