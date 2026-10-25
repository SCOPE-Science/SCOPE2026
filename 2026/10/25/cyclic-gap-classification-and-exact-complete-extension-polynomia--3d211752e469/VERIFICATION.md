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

Run `python3 checker.py` using the Python 3 standard library. The command exhaustively examines every binary choice of selected arguments for the labelled bidirected cycle on each \(n=3,4,\ldots,16\), a total of \(131064\) subset evaluations, and separately computes (a) Dung complete semantics from the universal defender condition; (b) the cyclic-gap criterion; (c) the coefficient of the allowed-gap generating series by integer convolution. The complete-extension size histograms match at every order. The checker also verifies stable extensions against the two-gap composition rule and bounds the positive singularity numerically, terminating in `ALL_CHECKS_OK` upon success.

Finite enumeration cannot establish an all-order statement, an asymptotic limit, or priority in the literature. Those assertions depend respectively on the symbolic gap characterization, exact cyclic-composition argument, pole-transfer proof, and comparisons with identified published primary texts. No independent audit has been performed.
