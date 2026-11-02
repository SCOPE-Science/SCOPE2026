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

## Reproducible checks

Run `python verify.py` (Python 3 standard library only). Its exact-fraction tests check the two sharp extremal families at eleven thresholds; every ordered positive five-part integer composition with sum 8, 12, 18, or 24 at the same eleven thresholds (127,600 inequality comparisons); the expectation identity on 100 nonuniform five-column profiles; and the equality/right-limit distinction at the first tail threshold. The checker printed `PASS` for all groups on execution.

## Proof responsibilities and limits

The universal real-parameter inequality is proved combinatorially in RESULT.md by the five-cycle obstruction, the unique possible seven-light-edge class, its cross-edge sum bound, and attaining positive mass patterns. The checker is a finite independent algebra sanity test and cannot establish infinite-parameter completeness or mathematical novelty. Source novelty inspection was not a systematic search of all historical weighted-graph and volume-sampling papers. Independent external audit remains unperformed.
