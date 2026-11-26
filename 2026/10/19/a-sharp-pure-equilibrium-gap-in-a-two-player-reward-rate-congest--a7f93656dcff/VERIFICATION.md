---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

At (X,U) both use the congested pair and each gets (4+1)/(2+2)=5/4; at (X,V) player 1 gets (5+6)/(1+1)=11/2 and A alone yields eta. At (Y,U), player 1 gets 1/2 from congested C and player 2 gets (5+1)/(1+2)=2. At (Y,V) C and A each have occupancy one, yielding (6,eta). All stipulated resource rewards strictly decrease and times strictly increase for eta>0, including the unused second-occupancy A data. Player 1's X-minus-Y gaps are 3/4 at U and -1/2 at V; player 2's U-minus-V gaps are 5/4-eta and 2-eta. Thus only (X,U) at eta<=5/4 and (Y,V) at eta>=2 can be pure equilibria, including both ties. In the gap the four strict unilateral improvements have gains eta-5/4, 1/2, 2-eta, 3/4, so no scalar can increase on every strict deviation. Under the ordinary mixed extension (expectation of the realized profile ratios, not ratio of expectations), indifference gives (5/4)q-1/2=0 and 2-eta-(3/4)p=0. If either player is pure, the other's reply is unique and pure in this interval, contradicting no pure equilibrium. Thus these interior solutions are the unique mixed equilibrium. All four gains and resource inequalities are strictly positive at each fixed interior parameter and depend continuously on the reward/time vector on positive denominators, proving joint open robustness without a uniform radius claim. Inspected the frozen rational verifier but did not execute it. The scope is this asymmetric family, not a minimal resource classification or any claim about dynamic selection of mixes.

## originality

PASS

The new content supported by the comparison is the explicit common reward/time resource representation with strict congestion monotonicity and its exact gap and equilibrium law. Neither the general existence of improvement cycles in nonlinear congestion games nor mixing in a two-by-two game is new. The direct quotient and the fixed-parameter transformed game in the closest paper are genuinely different; the latter's potential does not imply or rule out this gap. Access to two older congestion-averse texts was incomplete and is a residual risk, not negative evidence.

## value

PASS

The example resolves a motivated logical gap: good monotonicity of physical resource data and the additive potential at each fixed multiplier do not even guarantee existence of a pure equilibrium for the original rate objective. The exact parameter interval, strict margins and explicit unique mixed alternative show the failure is structural in a simple realizable family, not just a knife-edge violation of the potential identity. The ordinary best-reply algebra is not independently credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
