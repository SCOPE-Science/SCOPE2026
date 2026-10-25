---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For even n>=2, eta>0 the proper energy E=v²/2+x^(2n+2)/(2n+2) has E_dot=-eta*x^n*v²<=0, excluding finite positive-time blow-up and forcing convergence to the origin. Projective z=v/x^(n+1) obeys z_dot=-x^n[(n+1)z²+eta*z+1]; its quadratic has no real root precisely 0<eta<2sqrt(n+1), giving no fixed angular direction, while real invariant rays stop infinite full rotations above threshold. On the oscillatory side, d log |x|/dz=-z/P(z) yields the exact contraction of crossing speeds q=exp(-pi*eta/sqrt(4(n+1)-eta²)). Physical time dt/dtheta is a positive integrable (cos theta)^(-n/(n+1)) quadrature and gives C_{n,eta} V^-alpha. Geometric backward flight durations sum to C V^-alpha q^alpha/(1-q^alpha); quasi-homogeneous flow self-similarity forces exact logarithmic antiperiodicity and minimal period 2pi*n*eta/[(n+1)*sqrt(4(n+1)-eta²)]. Independently integrated full ODE via high-accuracy adaptive solver for (n,eta)=(2,1),(4,0.8): crossing-speed errors <4e-12 against predicted q. Numerical runs cannot establish global all-n winding/boundary claims, which follow from the projective monotonicity and energy/global time argument.

## originality

PASS

Matsue 2026 establishes the general periodic blow-up balance-law correspondence and computes n=2, eta=1 period and multipliers NUMERICALLY; Matsue 2018 examines an even-n, eta=1 near-infinity Liénard system with angular Poincare return integral and qualitative oscillation, credited. The candidate supplies the all-continuous-damping exact crossing ratio, physical-time flight and lifetime, parameter-dependent minimal log period and sharp inverse-square-root divergence. The earlier 1999 Dumortier–Herssens primary paper plausibly treats global near-infinity returns and may contain implicit quantitative coverage but complete text remained inaccessible; Oxford authorized attempt returned vpn_disconnected. This residual risk does not alone disprove best-knowledge O. The qualitative threshold alone is not claimed as wholly novel.

## value

PASS

Exact time-resolved blow-up clock of a natural quasi-homogeneous Liénard family is a structural dynamical quantity: it replaces previously numerical profile periods with closed all-degree/all-damping laws, identifies a sharp oscillation-to-nonoscillation boundary and a nontrivial essential singularity in flight-time ratios near it. Scaling alone does not determine the damping-dependent half-turn factor; the Riccati quadrature is substantive. No robustness or critical equality rate beyond winding absence is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
