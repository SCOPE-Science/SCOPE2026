---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The theorem concerns feasible positive solutions of the exact Xu–Zou state-dependent impulsive equations with zero predator restocking, 0≤psi≤1 and strict deficit δ=µ-ea(h_l/η)/(1+aq(h_l/η))>0. On H=ηx+(1-η)y≤h_l, x≤h_l/η; monotonicity of ax/(1+aqx) yields y-dot/y≤-δ. Every pulse multiplies y by 1-p2 E_l in (0,1). Therefore y(t)≤y(0)e^{-δt}(1-p2E_l)^N(t); positive periodic solutions of ANY impulse order are excluded. Post-jump H≤κh_l, κ<1, and bounded dot H on the compact triangle yield a positive minimum inter-pulse time, so no Zeno problem. Independent exact fraction checks confirmed ψ(y)=y/(1+y), two positive unharvested equilibria (5,1),(20/3,7/9), source case-(1) h_l=1/2≤min(h*=3,ηK=5), pbar=1/19>p2=1/100 and δ=5/12. The coexistence points lie outside the accessible triangle. The literal source theorem may include a predator-free order-1 orbit, which is not disproved.

## originality

PASS

Earlier same-model local Floquet stability work reduces the semitrivial multiplier to (1-p2E_l)e^{-µT}<1, refuting a local instability claim, but explicitly does not exclude disjoint strictly positive periodic trajectories. The current full feasible-triangle decay bound excludes ALL strictly positive cycles under δ>0 and gives a new exact simultaneous-theorem-hypotheses witness. Xu–Zou 2026 original printed Theorem 2.2(1) is an existence claim with a positive-cycle argument, not a proof of the global exclusion. No searched published same-model theorem or cited neighboring weighted-harvest model implies the specific strict-positive impossibility at these exact parameters. O PASS with risk of a generic unpublished barrier and literal semitrivial ambiguity.

## value

PASS

A strict feasibility barrier for predator persistence exposes a substantive missing hypothesis in a recent impulsive-fishery positive-periodic-orbit argument, even with two unharvested coexistence equilibria and every printed numerical case-(1) inequality satisfied. It is a global invariant obstruction, stronger than a local stability calculation, with exact biological-variable parameter witness; not merely a sign or formatting check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
