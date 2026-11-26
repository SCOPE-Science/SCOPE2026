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

Enumerating repeated-label and all-distinct outcomes yields z_i(1+z_i−S). At a fixed point the received coordinates satisfy one quadratic. For its two roots a>b, ab=p/[k(1−p)] and a+b=S+kab give the asserted converse as well: p/k=(1−p)ab<b, so the recovered x belongs to the simplex. The ratio equation gives a finite fixed-point set at each p. The weighted Cauchy–Schwarz bound makes the tangent Jacobian positive definite; its high/low splitting and group-contrast eigenvalues give instability for r≥2 and attraction exactly on the upper one-high branch, aside from the unit-eigenvalue cases. The one-high scalar increment at the uniform threshold is positive for small positive perturbations and at the fold is −Cu(u−u*)², repelling points immediately below u*. The monotone increments on these one-sided intervals and absence of intervening fixed points justify the nonlinear endpoint conclusions. Differentiating p(t) gives its sole maximum at k−1 for r=1. The map is the gradient of the stated convex potential on the simplex; the supporting-plane inequality gives a bounded Lyapunov function with increments at least half the step squared. Steps therefore vanish, every accumulation point is fixed, and an orbit with vanishing steps and a finite fixed-point accumulation set converges. Exact substitution of t=3 and t=4/3 gives the rational witness and stated spectra; the r=2 branch stays below p_lin in this example. The frozen verifier was read, not run; its finite tests do not establish convergence or endpoint stability.

## originality

PASS

The same communication-noise mechanism is known for binary 3-majority and the sampling rule is known without noise. The actual compared statements do not give the two positive-noise deterministic multistate thresholds, the exhaustive stability classification or convergence of every simplex orbit for this particular map.

## value

PASS

The exact split between the loss of linear attraction at the disordered state and the disappearance of ordered attractors gives a genuine deterministic coexistence regime, with endpoint and rational checks. Global convergence adds information not implied by the equilibrium list: no orbit has a nonfixed accumulation point. The result is useful without claiming finite-population escape times or stationary laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
