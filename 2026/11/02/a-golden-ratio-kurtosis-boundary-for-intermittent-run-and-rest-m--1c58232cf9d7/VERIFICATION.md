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

The analytical derivation in `RESULT.md` is the proof; computation alone is not a proof of the all-rate sign theorem. For reproduction, run `python check_three_state.py` with Python 3, NumPy, and SciPy. The checker constructs the block moment generator independently from the convolution-kernel realization, then compares their fourth cumulants across a rate/speed/time grid, sign regions, root locations and asymptotic checks. On the provided implementation it yielded **PASS 567 independent full-Feynman-Kac and positive-kernel checks**. An example gives a crossover at \(t_*\approx0.854478453989\) when \(\alpha=1.8\), \(\beta=v=1\).

The algebraic generator is a three-state finite matrix. The independent convolution representation is a six-stage linear cascade with separate matrix coefficients. Numerical tolerances protect against floating-point cancellation; there is no interval-arithmetic or machine-checked infinite certification. The all-time theorem is instead proved by the conditional moment identities, the exact Laplace inversion, log-concavity of convolution, and an analytic strict-monotonicity argument. A directly relevant 2013 full paper was not accessible for comprehensive novelty inspection, and independent validation has not been performed.
