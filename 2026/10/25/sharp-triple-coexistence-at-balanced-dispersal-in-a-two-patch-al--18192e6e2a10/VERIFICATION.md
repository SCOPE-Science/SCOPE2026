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
# Reproducibility and limits

Run `python3 verify.py` with standard Python 3 in the extracted package directory. It prints `PASS: 543 exact rational checks; Q signs and exact saddle verified`. The script makes all comparisons in rational arithmetic using the standard library; no network access is needed.

It checks the quintic derived from the balance \(\delta=s\), the exact rational signs \(Q(1/3),Q(1/2),Q(1),Q(3/2),Q(8/5)\), and the middle equilibrium's determinant and trace. Across a grid of positive rational parameters and evaluation points it independently reconstructs the nonlinear first equation, the scalar root polynomial and the Jacobian determinant chain rule.

The certificate is finite and does **not** claim to enumerate all parameter choices or to prove the all-parameter three-root upper bound. That bound, the sign-classification of all simple roots, and continuation of the three hyperbolic equilibria are proved analytically in `RESULT.md`. Stability of a degenerate equilibrium and the global separatrix geometry are outside the claim.
