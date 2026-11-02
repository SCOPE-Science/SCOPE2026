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

# Verification record

The theorem's claim is the analytic phase diagram and limiting fitness-gap distributions in `RESULT.md`. The standalone `verification.py` is a finite supporting test, not a proof of limits or novelty.

**Actual execution:** `python verification.py` completed with `PASS: 46 deterministic analytical-formula and quadrature checks`. The program uses Python 3 and SciPy (`scipy.integrate.quad`), reconstructs the exact stationary integrals after the substitution \(s=\log(1/(1-l))\), and compares against exactly integrable linear-reset formulas, normalized mixture masses, four divergent asymptotic branches, three first-logarithmic distributional regimes, the nested-log regime and finite-density examples.

**Critical analytic steps:** use the true stationary mean profile (Grange 2023, equations 41–44); prove \(J_\zeta\to J_0\) by dominated convergence using \(q(l)=O((1-l)^\alpha)\); derive \(I_\zeta\) from the exact logarithmic integral and compare on subcritical logarithmic windows; derive weak endpoint concentration when \(I_\zeta\to\infty\); derive beta/uniform limits as restricted-kernel ratios; use the second logarithm when \(\theta=1\).

**Limits:** Numerical quadrature samples only finitely many explicit parameters and cannot validate an asymptotic result for every admissible profile. No finite-system stochastic simulation, external expert review, or exhaustive publication-priority certification is claimed.
