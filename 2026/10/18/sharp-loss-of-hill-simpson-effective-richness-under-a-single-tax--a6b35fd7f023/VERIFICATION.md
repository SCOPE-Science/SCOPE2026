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

# Reproducible verification

Run `python3 check_hill_merge.py` with Python 3 and its standard library. A verified execution produced `PASS`, checked eight exact derivative identities, and evaluated 59,776 positive-rational abundance profiles using exact `Fraction` arithmetic and 70-digit `Decimal` bounds. The code checks the unique positive quartic root by bisection, constructs the maximizing proportions, and compares the claimed maximum against direct merger losses. It additionally checks the sharp asymptotic coefficient numerically. Sample expected values of the maximum loss are approximately \(1.314056108733\) for \(n=3\), \(1.602550323404\) for \(n=4\), and \(3.124244628662\) for \(n=10\).

The finite tests do not prove the infinite statement. The proof's nonstandard steps are independently verifiable from its displayed symmetrization inequalities, exact derivative factorization, monotonic quartic and limit argument. The included code has no external datasets and no network dependencies. Independent expert or formal verification has not been performed.
