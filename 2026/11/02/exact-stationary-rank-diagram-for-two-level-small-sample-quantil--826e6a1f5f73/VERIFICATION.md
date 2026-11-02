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

# Reproducible checks

Run `python3 verify.py` under Python 3.9 or later; no third-party packages are required. The checker uses exact rational probabilities and enumerates all \(s\)-row subsets for total row counts from three through ten, every strictly minority corruption count, every admissible sample size, and every residual rank. It reconstructs selected rows directly for both states and checks the formulas independently of the transition-tail derivation.

It checks stationary error ordering, the sharp absorption cutoff, exact eigenvalue signs and medians, seven-step time evolution, with-replacement binomial formulas, and worked rational examples. The observed output is: `PASS: 2174 exact rational identities and enumerated row-selection checks`.

The rigorous universal proof is in `RESULT.md`. Exact finite enumeration is not an infinite proof. This verification does not test general higher-dimensional quantile Kaczmarz, arbitrary corrupt values, approximate arithmetic, or non-independent sample schedules. Independent audit has not been performed.
