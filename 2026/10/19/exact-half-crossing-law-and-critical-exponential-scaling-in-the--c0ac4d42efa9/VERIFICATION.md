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

Run `python3 check.py` with Python 3 and no third-party packages. It prints a PASS result only after 96 exact rational finite-time distribution comparisons: six map-selection probabilities, two starting halves, and eight time horizons. The real-interval method propagates piecewise-affine images with exact Jacobian densities, whereas the comparison method propagates dyadic depth states and their geometric resets. The shell method aggregates all depth levels too far away to cross within the given finite horizon, which is an *exact* finite-horizon reduction, not a cutoff approximation. The script additionally checks 15 levels of the harmonic hitting equations and algebraic mean identities for the chosen rational parameters.

The exact infinite-time theorem is proved by the nearest-neighbor gambler's-ruin formula and the strong Markov restart law. Its critical scaling uses a geometric-tail asymptotic, while its almost-sure endpoint decay uses the strong law of large numbers. No finite experiment establishes these infinite statements in isolation. Boundary initial conditions, arbitrary nonuniform initial measures, the distribution of last-passage time, and full invariant-measure questions are outside the claim.
