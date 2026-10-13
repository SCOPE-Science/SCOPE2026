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

# Reproduction and boundaries

Run `python3 checker.py` with standard Python 3. Exact rational tests cover 4,935 finite parameter cells; the sampled concavity tests cover 3,045 midpoint inequalities; five independent cyclic-exponential simulations and five sparse-limit checks were also run. The analytic claims rely on the simplex-slice geometry, Brunn–Minkowski, invertibility of a Vandermonde matrix and uniform convergence with compactness; no finite grid is presented as an exhaustive proof of a continuum or all integers.

Rational tests of the alternating-sum formula do not independently certify its probabilistic derivation; that is given in RESULT.md. Monte Carlo outcomes are stochastic and use a fixed reproducible seed; they are corroborative only. No theorem about increasing component size, external datasets or historical priority was established by the checker.
