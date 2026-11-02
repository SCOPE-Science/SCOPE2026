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
# Verification notes

The argument is analytic-algebraic for every integer \(q\ge3\); it relies on the following identities, all explicitly proved in RESULT.md: the logarithmic critical equation \(\epsilon(r+q)t^q+(r+1)t+r=0\), the derivative \(R_\epsilon'=-N_\epsilon/f_\epsilon^2\), the equality \(N_\epsilon(-q/(q-1))=1-\epsilon/\epsilon_q\), the collision polynomial \(D_q\), and the logarithmic derivative of the Belyi coefficient map \(E_q\). Riemann–Hurwitz and transposition conjugacy supply the infinite statements.

A separate Python 3 script `verify.py` uses SymPy to check the identities and discriminant factorization exactly for \(3\le q\le8\). It is run with `python verify.py`; its success marker is `VERIFY_OK`. Successful finite checks do not establish the all-degree theorem and are not represented as independent verification. No numerical approximations or stochastic arguments are used.

The parameter values \(\epsilon=0\) and \(\epsilon=\epsilon_q\), resonant exponent ratios, and the projective point at infinity are not ordinary smooth very-affine fibers. They are excluded or explicitly analyzed as limits.
