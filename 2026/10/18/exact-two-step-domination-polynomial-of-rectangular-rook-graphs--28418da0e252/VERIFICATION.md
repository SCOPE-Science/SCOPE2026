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

# Computational reproduction and limits

Run `python3 verify.py` using Python 3.8 or newer. The program requires no external libraries and uses exact integers throughout. Its formula evaluator and independent exhaustive neighborhood checker are separate functions.

The exhaustive checker directly tests, for each vertex, the existence of a selected vertex whose two coordinates both differ. All 714,576 labelled subsets on 13 small dimension pairs are evaluated, and every polynomial coefficient agrees. Symmetry, nonnegative coefficients and minimum counts are checked for 841 ordered dimension pairs from 2 through 30. The latter are finite consistency checks, not an infinite proof.

The infinite family is proved by the three-way column-type classification and algebraic summation documented in `RESULT.md`. Previously known minimum-size values were not treated as novel. Full theorem-level comparison to Dod (2016) and independent validation remain outstanding.
