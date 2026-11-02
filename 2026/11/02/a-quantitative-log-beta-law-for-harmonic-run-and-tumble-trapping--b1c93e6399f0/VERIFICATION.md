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

# Reproduction and verification

The self-contained `verify.py` declares its only external mathematical package in `requirements.txt` (`mpmath`). To replay, install the requirements and run `python verify.py` from the same directory. The fixed pseudorandom seed and exact integrated-telegraph switch-event clock make the finite diagnostics reproducible; they are not a proof for infinitely many parameters or unbounded times.

The verifier checks beta-density balance at five switching/confinement ratios, normalizations, positivity of the exact limit mean and variance, the lower and upper bounds on an independent closed-form hypergeometric first-passage mean at several launch distances, and 22,500 exact-switch-clock first-passage samples at \(C=1000\). The recorded total was `PASS: 22808 analytic and exact-clock diagnostic assertions`. Simulated sample means at switching ratios 0.5, 1, and 2 were approximately 1.37573, 1.00713, and 0.82939, compared with log-beta values 1.38629, 1, and 0.83333.

The infinite-domain statement is established instead by the pathwise identity \(B_t=U_t+e^{-\mu t}B_0\), the beta stationary law, and the deterministic bound \(0\le B_0\le1\). This yields exact stochastic and quantile bounds for all \(C\ge1\) and all positive rates. Independent priority and third-party mathematical audit have not been performed.
