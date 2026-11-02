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

The included `verify.py` was executed with Python 3, NumPy and SciPy. It returned `PASS: 93 finite-difference, strict-bound, special-case, asymptotic checks`.

It independently discretizes the nonlocal Dirichlet problem \(-D T''+r(T-\mathbb E[T(AX)])=1\) with centered second differences and linear interpolation of reset destinations, and compares numerical solutions against the factorial series for several factor laws and starting positions. It also checks sharp inequalities over six quadratic-retention values and five reset rates, the exact all-or-nothing hyperbolic-cosine expression, sign invariance, the first distribution-sensitive weak-rate coefficient and the high-rate product coefficient.

The analytic proof and moment inequalities in RESULT.md establish the infinite parameter-domain assertions; these checks do not constitute an exhaustive computation or an independent scientific audit. The strict inequalities require \(r>0\), \(0<\mathbb E[A^2]<1\), and interior starting positions.

Run `python verify.py`; dependencies are listed in `requirements.txt`.
