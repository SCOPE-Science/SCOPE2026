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

Execute `python verify.py` using Python 3.10 or later. The checker requires no nonstandard packages and completed successfully with 331210 deterministic assertions and 5649 qualifying finite paths.

The checker uses exact rational arithmetic to verify the first-passage mean/variance recursion and gambler's-ruin harmonic identities at four rational biases. It enumerates all sign paths of length twelve, separately for cycle sizes three through eight, verifying that coverage and integer-range width agree and testing the hitting-time/last-vertex identity whenever the finite-path sufficient conditions hold.

These experiments cannot establish an infinite-horizon geometric minimum, an exponential probability estimate, or a central limit theorem. The proof independently establishes those steps by gambler's ruin, conditional strong-Markov estimates, passage-time renewal theory, and finite-prefix conditional Gaussian convergence. The finite-path test checks only a deterministic structural implication, not a probabilistic certificate of novelty or an independent mathematical audit.

The available analysis does not address a vanishing drift, the symmetric random walk, higher-dimensional cycles, or a Berry–Esseen rate. No independent audit has been performed.
