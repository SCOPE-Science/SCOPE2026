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

# Reproducibility and limits

Run `python verify.py` in the same directory. The program uses only the Python 3 standard library, rational fractions, and combinatorial enumeration. It verifies the exact configuration, every integral coalition and proposed candidate set for one through seven seats, all possible committee-sized Pareto alternatives for those sizes, and rational fractional feasible witnesses for one through one hundred seats. The observed run completed with `PASS: 86367 integral (coalition, proposal) cases; exact rational witness for 100 seat counts`.

The all-positive-integer claims do not rely on exhaustive verification: they follow from the explicit subset argument and the inequality \(2Y\leq kZ\). The exact supremum is attained by a rational witness, so no numerical optimizer or limit extrapolation is needed. Historical-priority verification is limited to inspected and retrieved literature; independent mathematical and literature audits have not been performed.
