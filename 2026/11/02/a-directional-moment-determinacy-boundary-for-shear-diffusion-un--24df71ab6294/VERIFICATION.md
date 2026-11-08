---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For full resetting, the stationary age has Exp(r) law and the exact unit-projection conditional variance is V(t)=2D[t+gamma*u*v*t^2+gamma^2*u^2*t^3/3]. Direct integration when gamma*u=0 gives the Laplace density and finite MGF. When gamma*u!=0, saddle t=ell*sqrt(abs(z)), with F(s)=s+1/(3s^3), unique s=1, F(1)=4/3, F''=4, yields K*abs(z)^(-1/2)*exp(-B*sqrt(abs(z))); the c2 correction gives exp(r*v/(gamma*u)). Small/large t tails are suppressed relative to the saddle. All polynomial moments exist by exponential age mixing; the finite two-sided Hamburger Krein logarithmic integral establishes indeterminacy; absence of MGF alone would not. Independent symbolic variance and constant checks passed. No joint-law determinacy or uniform gamma*u->0 statement is proved.

## originality

PASS

The shear-model stationary renewal mixture, Gaussian propagator and moment identities are explicitly prior art; half-power stretched-exponential tails also occur in other stochastic-reset models. The compared original studies do not state this full-reset stationary all-direction sharp prefactor or axis-specific Hamburger moment-(in)determinacy. Applying Krein is classical, not a new theorem. Best-of-knowledge novelty rests on this precise combination, with broader mixture asymptotic coverage a residual risk.

## value

PASS

Observable stationary displacement cannot in general be reconstructed from all moments under shear, while one geometrically distinguished transverse observation remains determinate. Exact directional tail rates/prefactors quantify rare excursions beyond low-order moments and expose nonuniform small-shear tail behavior, a natural distributional boundary rather than a generic saddle exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
