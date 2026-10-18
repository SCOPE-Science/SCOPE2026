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
# Verification of the finite-cycle interacting exclusion identity

The standalone `verify_cycle_shielding.py` uses only the Python standard library. Running `python3 verify_cycle_shielding.py` prints successful exact rational tests. The single-walker auxiliary Poisson system was solved in 219 finite settings with 10,098 individual rational edge-weight checks. More importantly, the code independently enumerated the full interacting finite-particle state space and inverted its Poisson operator in 94 choices of ring length, particle number, block size, and hopping rate, totaling 1,374 enumerated configuration appearances. The resulting rate, individual spatial-bond quadratic variations, and boundary fraction matched the formulas. Several large-cycle gradients were checked arithmetically, up to 1,024 sites.

The arbitrary-size conclusion relies on the written periodic difference-equation solution, exact exclusion-generator calculation, stationary hypergeometric bond activity, and finite-state martingale argument. These finite tests are reproducibility checks, not an assertion that finite enumeration certifies all integers or an independently performed audit.
