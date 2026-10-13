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

# Mathematical verification

The standalone file `verify.py` uses only the Python 3 standard library. Run `python3 verify.py` from this directory; the final expected line is `VERIFY_OK`.

It performs exact rational checks of the three negative-definite tangent quadratic-form Sylvester certificates, the normalized four-support and three-support equilibrium polynomial identities, both excluded-type invasion-fitness formulae, all required strict interval inequalities through Bernstein-basis coefficients, monotonic cubic derivatives, and rational isolating intervals for both unique support transitions. These are finite exact polynomial calculations for all real interpolation parameters in the unit interval, not sampled numerical integrations.

The global dynamic argument additionally uses an analytic strict-relative-entropy Lyapunov inequality for each fixed matrix and compactness of positive-support sublevels. Extinction exponents follow by taking time-averages of the log-fitness identity after proved convergence. The polynomial checker does not independently certify those general analytic arguments, literature novelty, physiological plausibility, or treatment efficacy.

Scientific limitations: only positive initial four-type fractions and the two specified fixed affine payoff paths are treated. Independent review has not been performed.
