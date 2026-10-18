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

# Reproduction and scope

Run `python verify.py` with Python 3, NumPy 1.24+ and SciPy 1.10+. The standalone program uses deterministic pseudorandom seeds and Gaussian-Hermite quadrature, as well as adaptive real-line quadrature. It checks algebraic identities for Anderson and ridge steps on 1,200 independent Gaussian sample pairs, conditional-normal tail integrals evaluated numerically at two thresholds for four parameter choices, and four pairs of regularized second-moment integrals. Its reported 3,636 finite numerical/algebraic checks passed in the stated environment. The program uses direct second-moment integration, not Monte Carlo estimates of nonexistent moments.

The proof's sharp Pareto tail, moment-existence threshold, and vanishing-regularization limit are established analytically in `RESULT.md`; finite tests cannot establish them for all parameters and limiting regimes. No multistep method or floating-point robustness guarantee was verified. Independent scientific audit has not been performed.
