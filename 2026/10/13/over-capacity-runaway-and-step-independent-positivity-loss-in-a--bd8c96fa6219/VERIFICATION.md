---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For u′=u(A−r k1 u−a v), v′=c v (K−v)(eu−f)/(K+dv) with A=r−b, K=k2, the wedge 0<u<f/e, v>max(K,A/a) is forward invariant for the ODE: u decreases and v increases. With g(v)=(v−K)/(K+dv), 0<g<1/d and g′>0; exponential lower/upper bounds give global existence, u→0, v→∞. Exact deficit cf/d−(log v)′=ce u g(v)+cfK(1+d)/(d(K+dv)) is time-integrable, proving v e^{−cft/d}→C>0; derivative ratio or l’Hôpital yields −log u/v→ad/(cf). Under any Euler h>0, positivity until exit forces v_n≥v0 q^n with q>1 and u_n decreasing; as soon as v_n≥max(v0,(A+1/h)/a), the prey multiplier is ≤0, proving explicit bound. Independent exact-rational witness u1=21/64, v1=57/14, q=57/56; forward simulation first crosses at 16 vs rigorous upper bound 53.

## originality

PASS

The exact Gao 2026 source treats equilibrium stability, local bifurcations and numerical trajectories for the same continuous and Euler equations. Its accessible full text does not derive the overcapacity invariant wedge, exact two asymptotic constants or step-size-independent positivity loss. Other Smith-type predator–prey sources use different multiplicative/additive predation laws or Smith prey-growth mechanisms, so they do not directly imply these paired conclusions. Abstract-only limitations retained.

## value

PASS

Above capacity, low prey reverses feedback; showing global predator runaway together with quantified superexponential prey decline reveals a model-state boundary. Every positive Euler step loses nonnegativity for the same open set, even under published small-step constraints, a substantive warning about interpreting long-term numerical trajectories.

The dated certificate retains the supplied scientific assessment, sources and limitations.
