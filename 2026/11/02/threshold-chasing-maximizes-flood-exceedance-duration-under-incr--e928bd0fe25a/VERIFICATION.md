---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For strictly increasing locally Lipschitz f with f(0)=0 and f>0 on (0,∞), each nonnegative recession segment exists forward and any positive post-event discharge decreases toward zero. If it starts above h, the time to h is the given finite integral. The clock Φ_h along a flow segment decreases at unit speed above h and is otherwise flat, apart from immaterial threshold instants. The initial and limiting clock values are zero, so the total occupation time telescopes to the sum of clock jumps, including for coincident pulses (successive jumps with no intervening flow). For P>h, the jump Φ_h(y+P)−Φ_h(y) increases strictly on 0≤y≤h and decreases strictly on y≥h, by strict increase of Φ_h above h in the former case and comparison of the translated integrals of 1/f in the latter. The first pre-pulse state is zero, and the pointwise optimum y=h is attainable at all later pulses simultaneously by the threshold-return recursion. The strict inequalities exclude every other subsequent pre-state and ensure strictly positive gaps, so simultaneous pulses cannot be optimal. The only lost increment is the positive penalty ∫_P^(P+h)1/f(u) du for the first pulse, strictly decreasing in P. Thus precisely a maximal occurrence may go first, with all later orders permitted and unique gaps for any fixed order. The logarithmic formula and the example with h=k=1 follow by integration, including log 60 versus log 10 for coincident pulses. As an additional exact check, with f(q)=q², h=1 and pulses (2,3,5), the optimal times conditional on first pulse 2, 3, or 5 are 25/12, 13/6, and 133/60, respectively, from Φ_1(z)=1−1/z above 1. The argument is an analytical sharp bound and proof of equality, not a grid search over calendars.

## originality

PASS

The supported distinct statement is the sharp full-calendar characterization for arbitrary finitely many prescribed individually superthreshold additive impulses under a strictly increasing scalar autonomous recession law, not the notion of a recession clock, hydrograph duration or a particular test value. The strongest inspected indexed comparison shares the occupation objective but uses a two-reservoir impulse response and two equal pulses. The closest inspected primary optimization uses peak, not occupation time. A bounded comparison found no statement or transport of the full scalar calendar law; two plausible but inaccessible papers remain named access risks, not evidence of absence.

## value

PASS

This is a structural optimum for a naturally posed occupation problem with continuous time decisions, discrete order and arbitrary nonlinear monotone recession. The equality classification shows concretely why packing input for a high peak is not optimal for time above threshold, why no below-threshold delay is needed, and why only the largest first pulse matters for ordering after the others are fired on threshold returns. The clock bound makes this distinction without fitting any particular recession exponent or instance. Its role is a benchmark for an idealized model, not a rule for managing actual floods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
