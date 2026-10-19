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
Run `python3 verify.py` using Python 3 and no additional packages. The checker makes 135 direct Floquet comparisons with the closed-form matrix exponentials, determinant and Perron-vector tests, plus five checks of the nonlinear period map, attraction and critical scaling, for **140 checks**. The reported example has \(r=1\), \(d=9/8\), \(h=\log 2\), \(\kappa=0.7\), with \(T_*=3.376610599770\ldots\), \(\Lambda(2)=0.052444418600\ldots\), and \(\Lambda(5)=-0.036709836247\ldots\).

The finite checks are consistency tests, not proof of global dynamics or of the infinite-time limit. Critical analytic steps are: the exact shared-density transformation; trace and determinant of the positive monodromy matrix; strict negative curvature of the inverse-hyperbolic-sine expression; and positive Perron decomposition with the complete-period denominator asymptotics. The main result states each hypothesis and quantifier and records unresolved literature-access limitations. Independent validation has not been performed.
