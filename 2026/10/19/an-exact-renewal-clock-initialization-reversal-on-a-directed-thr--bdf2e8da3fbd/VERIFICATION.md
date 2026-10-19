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

# Verification and scope

The mathematical proof is given in `RESULT.md`. Run `python3 verify.py` from a directory containing that script. It uses only the Python standard library. It builds a separate stage-augmented generator-harmonic system for Erlang shapes 1 through 12, solves those systems exactly with rational arithmetic, checks every generator equation, and compares the resulting opinion-fixation vectors against the independent renewal-formula predictions. It verifies the explicit shape-two probabilities and the strict Poisson-benchmark reversal. It also simulates 25,000 complete trajectories for each initial-clock protocol, with a fixed random seed and an explicit tolerance. The stochastic check is not a proof.

The all-distribution conclusion is established by the renewal-epoch martingale and equilibrium-residual Laplace identity, not finite phase tests. The clocks must be independent, the renewal intervals strictly positive with finite mean one, and the initial opinions distinct. The referenced literature's detailed treatment of distinct graphs and initialization conventions is not itself a proof of priority for this theorem. Independent scientific audit has not been performed.
