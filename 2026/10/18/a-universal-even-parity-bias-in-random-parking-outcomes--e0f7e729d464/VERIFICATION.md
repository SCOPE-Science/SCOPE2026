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

# Reproducibility and bounds

Run `python3 verify.py` using Python 3 and its standard library. A successful run prints `PASS 131 assertions`, followed by values of the signed imbalance. Four calculation routes are deliberately separated: signed binary shuffles; the last-vacancy recurrence; the positive formal differential equation with exact rational coefficients; occupied-subset dynamic programming; and independent simulation of every preference vector through six cars.

The checked range is finite: shuffles through nine positions, the two formal recurrences through 24 cars, occupied-subset states through thirteen cars, and all preference vectors through six cars. The all-size strict inequality follows from the induction in `RESULT.md`; finite checks cannot establish it alone. No analytic convergence of the formal series, asymptotic parity rate, or independent audit is claimed.
