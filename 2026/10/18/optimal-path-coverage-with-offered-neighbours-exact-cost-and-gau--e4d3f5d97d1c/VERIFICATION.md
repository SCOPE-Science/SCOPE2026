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

# Reproducibility and verification

The included `verify.py` is Python 3 standard-library-only and executable as `python3 verify.py`. It recomputes the exact expected hitting times for all 150 parameter pairs with path lengths 1 through 30 and candidate-offer counts 1 through 5, enumerating ordered offered-neighbour tuples rather than assuming a closed-form optimal choice. The script checks 3600 exact rational Bellman, monotonicity and worst-start statements, and derives central-cover-time second moments from the corresponding first-step equations, comparing variance per vertex against the limiting constants for three offer counts and increasing path lengths. Its successful execution supports finite algebra but is not a proof for infinite sizes.

The analytic verification reconstructs the full Bellman boundary conditions, monotone value functions, finite-horizon boundary cases, exact two-offer formulas and a random-time martingale central limit argument. Reflection visits are tight because a fixed positive drift gives geometric return probabilities. As a separate scientific limitation, historical priority is based on inspected primary texts and searches; no independent audit is asserted.
