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

The analytic proof reduces the full supremum to minimization of \(F(A,\lambda)\) on \(A\in[0,1]\), \(\lambda\ge0\). The boundary and \(\lambda\to\infty\) values are at least \(1\), while the unique feasible interior stationary point satisfies \(18A^4-15A^2+1=0\), \(A^2=(5-\sqrt{17})/12\), and \(\lambda^4=(15+3\sqrt{17})/2\). Substitution gives \(F=(5-\sqrt{17})/2\), so \(\mu_4^4=(5+\sqrt{17})/4\).

The standalone script `verify_mu4.py` uses only Python's standard `decimal` module. It checks the polynomial equation, both stationary equations, the normalized minimum, and the reciprocal fourth-power identity to high precision and prints `VERIFY_OK`. This computation checks algebraic consistency only; the infinite optimization is certified by the symbolic reduction and boundary/uniqueness argument in `RESULT.md`.

Limits: no claim is made for complex scalars, higher dimensions, other exponents, or the classical rectangular constant. The original 1970 definition source was not available as full text in the inspected public sources, so an older notation-level duplicate remains a bibliographic risk rather than a correctness risk.
