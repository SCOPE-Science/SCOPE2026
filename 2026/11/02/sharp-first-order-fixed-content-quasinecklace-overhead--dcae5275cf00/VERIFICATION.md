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

The provided `check_quasinecklace.py` is self-contained Python 3 and uses no third-party libraries. Run `python3 check_quasinecklace.py` to replay the finite tests; the recorded terminal output is in `check_output.txt`.

The direct tests enumerate binary words up to length 17 (at most eight ones), and separately enumerate all weak gap compositions for one through seven ones and at most 16 zeros. They compare direct definitions to exact counting formulas and check the three-one excess identity up to 999 zeros, then sample the leading asymptotic constant with exact rational arithmetic. The program does not certify the infinite theorem; the proof is in `RESULT.md`.

Independent external audit has not been performed. No assertion of independent validation is made.
