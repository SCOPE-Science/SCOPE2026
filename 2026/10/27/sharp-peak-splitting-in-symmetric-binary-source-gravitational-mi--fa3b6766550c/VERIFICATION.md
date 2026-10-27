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

# Reproducibility and scientific limits

Run `python verify.py` from this directory using Python 3. All checks use the standard library; no external data files are required. The exact-rational checks confirm the derivative identities used to establish the strict monotonicity of the transformed stationary-point equation. Randomized checks compare analytic peak classification with independent evaluations of the original Paczyński sum. The exact benchmark uses \(b=1\) and \(s=0.8\); the near-critical tests check the square-root coefficient.

Observed completed run: 199 rational derivative confirmations, 180,000 sampled light-curve derivative/brightness comparisons, 647 configurations with split maxima, and the exact benchmark and onset-coefficient checks, all passed.

The proof of universal uniqueness is contained in RESULT.md. The tests cannot establish the infinite theorem by enumeration. They also do not quantify observing cadence, noise, orbital motion, source radii, parameter uncertainty or historical priority. The earliest selected publicly dated source is the 1998-04-26 arXiv preprint cited in RESULT.md. Independent audit has not been performed.
