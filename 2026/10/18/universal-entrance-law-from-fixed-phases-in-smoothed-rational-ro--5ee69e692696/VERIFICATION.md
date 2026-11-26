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

On K=[d,1/n-d] the discontinuous itinerary advances the site index by k modulo n in the interval of indices k-n through k-1. Coprimality visits each site once, and the nearest positive and negative sites are t and t−1/n. A finite induction bounds the smooth itinerary error by O(e^(-ad)), preserving signs. Every other site's correction is O(e^(-a(1/n+d))). The shift of the nearest negative site's argument is p_a(t) plus those smaller terms; its derivative is O(a e^(-a(1/n-t))) along that shift. This gives the uniform O(a q_a²) remainder in the one-return displacement. For large a, all branch derivatives are in (0,1), giving an increasing return with decreasing displacement and an interior fixed point. Testing h±c/a for each c>0 yields a(t_a*−h)→0 and the orbit from x_0 is trapped monotonically between x_0 and t_a*. In y=e^(-σa(t-h)), with σ the initial side, let u=e^(-at), v=e^(-a(1/n-t)). Then y(u+v)=q_a(1+y²), with y≤2 eventually and u+v=O(e^(-ad)). This controls the exponential and logistic Taylor remainders uniformly even at y→0, and the step a q_a has drift 1−y²+o(1). Discrete Gronwall gives y→tanh τ uniformly on bounded time intervals from y_0→0. The logarithm is uniform only away from τ=0. After a possible crossing of h the scaled displacement is o(1), so the absolute-displacement threshold observable differs uniformly from y by o(1). The uniform limit brackets the first sampled crossing, proves finiteness and gives the artanh clock. The verification notes and script were inspected, not executed; the 88 recorded checks evaluate the smooth map numerically and are not certificates for the limits.

## originality

PASS

The supported distinct claim is the full positive-time profile and sharp first-return clock from a fixed noncentral interior phase. The same-family half-grid orbit, local return formula and exponential contraction scale are already known and not counted as new. The strongest checked quantitative formula is restricted to a neighborhood shrinking exponentially in a, and the qualitative global results do not bridge the fixed-phase portion of the orbit on the rescaled clock.

## value

PASS

The natural dynamical question is how long actual trajectories take to enter the inverse-steepness layer, not how slowly a trajectory already extremely near its attractor contracts. The theorem gives an entire scaled transient and a sharp threshold-dependent clock independent of the fixed initial distance and rotation numerator. Uniform control across the intermediate phases makes this more than a restatement of the local multiplier.

The dated certificate retains the supplied scientific assessment, sources and limitations.
