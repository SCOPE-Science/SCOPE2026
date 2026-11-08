---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

At s,t∈{±1}² coordinatewise Bernoulli rounding gives P_h(s,t)=((1+t1(as1+bs2))(1+t2(-bs1+as2)))/4 with a=1-h,b=hc. Summation over the four source spins cancels the cross term, yielding double stochasticity and π=1/4. The four clockwise neighbor probabilities equal p+=h(1+c)(2-h(1-c))/4 and reverse p-=h(1-c)(2-h(1+c))/4; p+-p-=hc. Opposite-corner transition pairs are symmetric. Entropy is (p+-p-) log(p+/p-), derivative of rate is +4c²/((2-h(1-c))(2-h(1+c)))>0. |a±ib|<1 gives convergent mean; all corners lie at squared distance 1/2. Direct 841 rational (h,c) pairs reproduce full P, stochasticity, neighbor flux, positivity. Valid for stated four initial corners and fresh coordinate rounding, not generic floating-point computation.

## originality

PASS

The finite-step simultaneous-coordinate-flip kernel, with exactly step-invariant flux rate and step-increasing entropy production, is not identified in the inspected published stochastic-rounding or asymmetric-spin treatments. Nonzero circulation and its h→0 generator are explicitly prior results, not independently original.

## value

PASS

Numerical discretization can preserve correct first moments yet exhibit persistent irreversibility and a nonvanishing error floor. The exact h dependence separates stochastic-rounding geometry, stationary physical-time current, and entropy production in a canonical analytically solvable numerical-integration benchmark; it is more than a trivial parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
