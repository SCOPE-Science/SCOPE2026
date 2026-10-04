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

The verification target is the exact coordinate-second-moment law for the published quadratic-only flow.

Checks performed:

1. Re-derived the three finite-time balance equations by direct integration of the published ODE.
2. Checked that the moment-system determinant is \(-b_1(a_1c_2+a_2c_1)\), hence nonzero for strictly positive parameters.
3. Substituted the claimed general moment formulas into all three limiting balance equations.
4. Checked the nominal specialization \(a_1=a_2=b_2=c_2=1\), \(b_1=2\), \(c_1=3\), obtaining \(1/8,1/4,1/4\).
5. Checked the multistable specialization \(c_1=13/5\), obtaining \(5/36,5/18,5/18\).
6. Checked that these values equal the squares of the source's equilibrium-coordinate magnitudes.

The bundled `verify.py` performs the algebraic specializations using exact rational arithmetic and prints `VERIFY_OK` on success.

Limits: no numerical trajectory integration is used as proof; no claim is made that all trajectories are bounded or that the reported attractors exist independently of the source's numerical evidence.
