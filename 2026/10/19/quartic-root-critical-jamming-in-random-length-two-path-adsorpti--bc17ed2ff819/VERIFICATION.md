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

Run `python trimer_checks.py` with Python 3.10 or later; no packages are required. This checks exact recursion versus independent physical enumeration on nine small bipartite graphs, confirms the first nontrivial terminal probabilities, independently verifies one-step drift and conditional variance over positive-count states, and checks the gamma integrating-factor relation at many integer arguments. Seeded simulations compare finite mean terminal counts with the two asymptotic regimes. All tests passed in the packaged version.

The asymptotic proof is independent of the experiments. Its nonstandard claims are the exact gamma-ratio martingale, the order-\(N^{1/3}\) quadratic variation, the CLT after deterministic cutoff, the negligible late-stage noise, and the terminal inversion producing the exponent \(1/4\). These are established analytically in the RESULT proof. Finite simulation cannot establish asymptotic uniqueness or exclude unknown published equivalents.
