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

# Verification record

Run `python3 verification/verify.py` from the extraction root with Python 3.10 or newer. The program requires only the standard library. The embedded output records:

```
run-pattern threshold cases: 190840
maximum sphere word-tests: 282205 parameter rows: 201
sharp alphabet threshold examples: 7
ALL CHECKS PASSED
```

The run-pattern check generates all words of lengths up to eight on alphabets of size two and three and up to seven on an alphabet of size four, and evaluates every admissible number of deletions. The extremal check enumerates eligible cases through length eight for the tested alphabets. The sharpness check examines seven abstract uniform-threshold instances.

Proof obligations beyond the finite tests are discharged in `RESULT.md`: a collision forces deletion of an intervening complete-run segment, and the converse collision construction works for all larger deletion counts. Coefficientwise smoothing and periodic-symbol attainment extend the bound to all permitted integers. No formal proof assistant or independent review is claimed.
