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

# Verification and scope

Run `python verify.py` with Python 3 and SymPy 1.14 (or compatible version). The packaged program performs exact polynomial checks of the three sign-comparison identities, exact resultant elimination and rational Sturm endpoint signs. It then verifies the rational example, directly enumerates every sampling word for 1,000 seeded floating-point parameter choices, and compares the sharp sign formula over a grid of 19,701 pairs. Its recorded output is in `verification-output.txt`: `PASS 28701 direct/parametric assertions; sextic_kstar=1.645487146309 tstar=0.342323879476`.

The continuum statement is analytically certified by elementary factor identities and monotonicity inequalities in `RESULT.md`. The numerical parameter grid does **not** certify the infinite continuum, and the floating approximations do **not** certify algebraic uniqueness. The exact rational Sturm sign counts and direct inequality proof supply those steps. No external or independent audit was performed. The proof covers the stated planar rank-one family only, not general stochastic extragradient or multiple epochs.
