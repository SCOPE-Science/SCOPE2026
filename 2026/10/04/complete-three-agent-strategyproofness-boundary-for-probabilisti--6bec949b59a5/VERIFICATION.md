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
The embedded `verify_ps3_strategyproof_boundary.py` is an exact finite replay.

For two agents it enumerates all four strict profiles and all unilateral false reports, finding no full-strategyproofness failure.

For three agents it enumerates all \(6^3=216\) strict profiles and all \(3\cdot5\) false-report opportunities at each profile. PS allocations are computed with exact rational arithmetic. A failure is recorded exactly when the truthful lottery does not weakly stochastically dominate the lottery induced by the false report under the agent's true ranking.

Two independent PS implementations are compared on every three-agent profile: a continuous event-driven rational algorithm and a twelve-microtick exact integer replay. Their allocations must agree profile by profile.

The verifier then checks:
- exactly \(54\) bad profiles and exact profile incidence \(1/4\);
- exactly \(72\) vulnerable agent-profile pairs and exact distinguished-agent incidence \(1/9\);
- one violating report per vulnerable agent;
- \(36\) bad profiles with one vulnerable agent and \(18\) with two;
- exactly two bad-profile orbits under independent agent/object relabeling, of sizes \(18\) and \(36\);
- exactly two normalized event orbits, each of size \(36\);
- every false report swaps the top two objects;
- every event has objectwise lottery difference \((-1/4,1/3,-1/12)\) in true preference order;
- the expected-utility gain formula \((-3T+4M-B)/12\), hence profitability iff \(4M>3T+B\);
- zero strict stochastic-dominance improvements from false reports, confirming weak strategyproofness on the enumerated boundary;
- exactly ten agent/object isomorphism classes in the complete three-agent profile universe.

Run:

`python3 verify_ps3_strategyproof_boundary.py`

The first output line must be:

`VERIFY_OK`

All conclusions are finite statements about the two-by-two and three-by-three assignment problems. No claim about larger markets is inferred from this enumeration.
