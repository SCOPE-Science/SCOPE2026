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

The analytic proof is in `RESULT.md` and the exact-rational checker is `check.py`. Run `python check.py` using Python 3 with no external dependencies. Tests include finite-horizon Bellman equations, their monotonicity cone and optimal fixed action, an independent full-cycle finite-horizon policy comparison, first and second moments of the finite absorbing distance chains, and the displayed closed moment formulas. Finite tests do not verify the infinite-horizon theorem by themselves; that conclusion uses the cone-invariance proof, the stagewise stochastic coupling, and Lyapunov's theorem. Independent mathematical audit has not been performed.
