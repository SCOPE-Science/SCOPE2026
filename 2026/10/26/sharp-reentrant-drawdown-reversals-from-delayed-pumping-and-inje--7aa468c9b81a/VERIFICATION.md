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

Run `python verify.py` in an environment with Python 3 and SciPy (`scipy.optimize` and `scipy.special`). The script is standalone; no external data or private logs are required.

The executable checks 4,500 deterministic pseudorandom positive \((a,b,\tau)\) triples for the quadratic-derived kernel-minimum classification, 100 direct finite-difference comparisons against the exponential-integral drawdown derivative, and both strict turning points in each of two reentrant delays. It also brackets the transition delays for a deliberately selected example and uses elementary exact exponential inequalities to prove the \(2,0,2\) comparison without relying on rounded values.

Finite random tests cannot prove the universal quantified result. Mathematical verification depends on the exact derivative factorization, the quadratic one-minimum lemma, the envelope derivative, and limiting arguments in `RESULT.md`. Floating-point underflow for extremely small minima is handled by testing their logarithms for finiteness and negativity. The code checks this model only; no independent audit, stochastic observation study, field extrapolation, or certificate of historical uniqueness has been performed.
