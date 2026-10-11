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
# Verification

Run `python verify.py` using Python 3.9+ standard library only. Successful execution prints `CHECK_OK`. The script uses independent deterministic numerical Simpson quadratures for the two original-time periods, a divergence-theorem radial integral for the geometric Floquet quantity, exact rational saddle-weight arithmetic, numerical comparison to the elementary exact critical geometric integral, and a direct fourth-order Runge–Kutta return check from \((x,y)=(3,2)\) at \(\mu=39\), \(\varepsilon=1\). The asymptotic endpoint analysis, global uniqueness of limit cycles, equality of the exact Floquet integrals, and the analytic integral evaluation rest on the displayed proof, not the numerical program. Unchecked limits: no machine formal proof, no independent audit, no exhaustive literature priority guarantee. All numerically reported values are illustrative, not a substitute for an infinite-domain theorem.
