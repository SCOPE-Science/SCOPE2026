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

# Reproduction and limits
Run `python3 check_a4.py` from the folder containing this file. The script uses only Python standard-library `fractions.Fraction` and `itertools.combinations`; it constructs all ten oriented \(A_4\) roots and independently forms the Gram matrices and incidence projectors. It executes exact rational assertions over degrees \(0\) through \(300\), including rank-sector formulas, sharp condition-number equality cases, and candidate frame bounds. The derived analytic formulas and inequalities in RESULT.md, rather than a finite enumeration, establish the conclusions for all degrees. Independent external audit has not been performed.
