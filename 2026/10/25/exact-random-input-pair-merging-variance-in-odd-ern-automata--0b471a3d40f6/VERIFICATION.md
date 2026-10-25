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

# Reproducing the mathematical checks

Run `python3 checker.py` using Python 3 and its standard library. The program builds the pair chain from the original two transition maps, solves the first- and second-moment recurrences with exact fractions for \(n=3,5,7,9,11\), and compares the result to both displayed closed forms. It also calculates the scalar boundary/difference formulas at seven separate positive integer parameters. The final expression is a polynomial of degree at most six, so seven distinct exact points establish the last algebraic identity provided the recurrence reduction and degree bound in RESULT.md hold. This finite checker does not establish the initial pair-state reduction, all possible input distributions, or novelty, which are assessed separately in the written proof and literature comparison. No independent audit has been performed.
