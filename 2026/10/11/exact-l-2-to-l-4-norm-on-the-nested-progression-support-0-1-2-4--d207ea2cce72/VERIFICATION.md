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
The exact checker is `artifacts/verify.py`. Run it with Python and SymPy 1.14.0.

It verifies four proof-critical facts: (1) the boundary reduction has maximum \(15/7\); (2) the equal-modulus point gives \(9/4\), so the global maximum is interior; (3) the exact lexicographic Gröbner basis of the scaled stationary system yields the stated degree-nine elimination polynomial for the normalized excess \(\delta\); and (4) that polynomial has one sign change and an exact rational root bracket \(1497/5000<\delta<599/2000\).

The numerical root and constant printed by the script are only decimal evaluations of the exact algebraic certificate. No finite sampling is used to infer the universal inequality.
