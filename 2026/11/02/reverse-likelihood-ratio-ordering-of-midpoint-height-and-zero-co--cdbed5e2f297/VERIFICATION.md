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

The complete reproducible check is in `verify.py`, requiring only Python 3 and no third-party packages. Run `python3 verify.py` in the extracted artifact directory. The output is `PASS 1430938 exact integer assertions; n<=150 half-profile; n<=80 full LR minors; n<=11 complete Dyck enumeration`.

The verifier independently generates every Dyck excursion of semilength at most eleven and records its midpoint height and strictly interior zero contacts. It also independently constructs the distributions of zero contacts for nonnegative half-walks by dynamic programming; it checks exact coefficient formulas, normalized sums, log-concavity and reverse two-by-two minors using integer arithmetic. The all-size statement rests on the proof in `RESULT.md`, not on finite verification. No independent audit has been performed.
