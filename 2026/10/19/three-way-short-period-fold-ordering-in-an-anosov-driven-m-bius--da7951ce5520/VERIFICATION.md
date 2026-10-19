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

# Verification and reproducibility

Run `python3 verify.py` with `mpmath` and `sympy` available. The standalone checker uses determinant-congruence enumeration of the Anosov base points, exact symbolic identities involving fifth roots of unity, independent multiplication of the actual complex Möbius-return matrices, and arbitrary-precision root finding. The checker completed **519 consistency checks**, printed `CHECK_OK`, and gave \(\alpha_-(1/10)=-0.03370194797518050324915709496196778\) and \(\alpha_+(1/10)=0.088141535115618067207741444102382362\).

The infinite claims, including uniqueness, follow instead from the explicit analytic trace and derivative inequalities in RESULT.md. Sampling cannot certify a theorem quantified over every phase and amplitude. All calculations apply only to \(\varepsilon=2/5\), \(0<\mu\le1/10\), and \(-\pi/2\le\alpha\le\pi/2\). The code has no external file dependencies and does not access network resources.
