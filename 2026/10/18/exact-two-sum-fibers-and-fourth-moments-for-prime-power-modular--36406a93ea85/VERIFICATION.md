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

# Reproduction notes

Run `python3 verify.py` with Python 3 and no dependencies. The checker reconstructs \(r(s,z)\) by **direct enumeration** over \((\mathbb Z/p^k\mathbb Z)^\times\), compares the entire histogram including zero fibers for each sum \(s\), checks the closed energy expression and, separately, directly evaluates two complex two-parameter Kloosterman fourth moments. Cases: \((p,k)=(3,2),(3,3),(3,4),(5,2),(5,3),(7,2),(11,2)\). The exact ledger-embedded file was run successfully, reporting `VERIFY_OK fields=7 rows=437 ordered_pairs=27540 direct_moments=2`.

This finite enumeration cannot establish the theorem for every odd prime and exponent. The unrestricted statement is proved using root counts of quadratic congruences, Hensel lifting and exact character orthogonality in `RESULT.md`. No independent external mathematical audit or priority certification has occurred.
