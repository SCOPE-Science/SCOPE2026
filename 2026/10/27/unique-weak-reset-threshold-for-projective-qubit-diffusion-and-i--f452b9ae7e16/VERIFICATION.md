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
# Reproduction and proof limits

Run `python CHECK.py` in an environment with Python 3 and `mpmath` installed. The code defines its own parameters and checks the following identities with high-precision arithmetic: the first and second backward moment equations for five target thresholds and four interior starting fractions at two diffusion scales; the hypergeometric first-passage Laplace transform and its first two derivatives; the Poisson renewal derivative; the unique-root sign pattern at eight target thresholds; and the two asymptotic laws.

The executed program returned `PASS 178 analytical/numerical identities and threshold diagnostics`. It prints representative switching fidelities. Tests of finite instances neither prove the sign for every fidelity nor certify originality. Infinite-range claims in RESULT.md depend on analytic differentiations, the single-crossing argument, and the two limiting implicit expansions. No independent audit has been performed.
