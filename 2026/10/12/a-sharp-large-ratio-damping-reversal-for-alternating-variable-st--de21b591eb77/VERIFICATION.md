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

# Verification scope

Run `python3 verify.py` with Python 3's standard library. The code performs 9 exact-rational zero-equation trace/determinant identities, 45 exact-rational damped matrix constructions, and an exact sign certificate at \(r=100\), \(q=1/10\). Observed result: `VERIFY_OK: nine exact zero-ODE monodromies, 45 damped two-period maps, exact negative-real-axis instability certificate`.

The theorem for all \(r\) and \(q\) comes from explicit coefficient formulas, an entrywise matrix limit, and continuity of polynomial roots. The finite script cannot certify the universal limit, historical originality, other differential equations, or independent validation.
