---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS. For the printed 2022 delayed SEQIJR model, incidence β exp(-m I(t-τ)) S(t) I(t) has current derivatives u s(t)+v i(t) and delayed derivative -m v I_* i(t-τ), where u=βexp(-m I_*)I_* and v=βexp(-m I_*)S_*. The source incorrectly combines both i contributions in delay matrix. Directly expanding 4×4 det(ξI-A-e^{-ξτ}B) and using cpγv=CGL yields F=(ξ+C)(ξ+G)(ξ+L)(ξ+μ+u)+CGL(ξ+μ)(mI_*exp(-ξτ)-1); removed compartment contributes stable ξ+d2+μ. Independent symbolic determinant was verified. With printed parameters equilibrium I*=13.646976755..., S*=3271.592615..., zero-delay quartic satisfies strict Routh-Hurwitz. Frequency modulus polynomial has coefficient signs +,+,+,-,-, hence one strictly positive root; its phase first τ*=18.59248621759530, frequency θ*=0.06652293610984329, crossing derivative Re(dξ/dτ)=0.001262757946...>0. Continuity of retarded characteristic roots and no zero root then prove first local linear stability loss, not nonlinear Hopf orbit behavior.

## originality

PASS

PASS on material full-text primary comparison. Maji et al AIMS Mathematics 2022 directly displays current/delay matrices merging the current I(t) term into delayed term; this is not valid for τ>0 and their printed characteristic factor differs. Source numeric transition around 18–19 agrees qualitatively but does not contain the corrected factor/threshold derivation. Related Basir–Ray–Venturino 2018 SIS-type awareness/media-delay system is mathematically different, not a stronger SEQIJR coverage. Specific prior erratum could exist but was not found in identified material; failed Resultary is not evidence of absence.

## value

PASS

PASS. The source publishes a characteristic equation and local stability threshold for a concrete delayed epidemic model based on a wrong current/delayed Jacobian allocation. A corrected exact characteristic factor and reproducible first crossing are a scientifically motivated correction that directly changes the analytic conclusions for a studied model, even though a nonlinear Hopf theorem is not claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
