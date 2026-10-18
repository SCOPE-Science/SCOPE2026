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
# Verification and limits

The accompanying `RESULT.md` proves the theorem using the stationary Poisson reset age, an exact beta mixing variable, the conditional binomial central limit theorem and a Hoeffding-dominated integral. The proof covers every \(\beta>0\) for fixed positive parameters and every fixed \(s\in\mathbb R\). The normal moment integral yields the threshold constant without fitting data.

Run `python verify.py` in this directory with SciPy available. Numerical integration checks the finite-binomial mixture at three positive rates and three increasing population sizes, tests two nonzero count offsets, and independently re-integrates the physical reset age at one parameter set. It concludes `NUMERICAL CHECKS PASSED` when the two independent finite-parameter integrals agree.

The finite numerical tests do not certify the infinite limit, and the proof does not treat joint particle-number/reset-rate limits, non-Poisson reset clocks, interactions or asymmetric counting windows. No independent audit has been performed.
