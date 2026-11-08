---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

For unit S^2 and W={x>=0,y>=0}, normalized area sampling has z uniform[-1,1] and longitude phi uniform[0,pi/2]. Crofton's formula gives per(K)=2pi Pr(unoriented random great circle hits K); the great-circle misses the finite spherical hull exactly when all independent sample points lie on one side. Symmetry yields deficit 2pi-E[L_n]=integral_{z=-1}^1 integral_{theta=0}^{2pi} p(z,theta)^n dtheta dz. A Gaussian sign orthant calculation with correlations u_1,u_2 yields p=1/2+[arcsin(u_1)+arcsin(u_2)]/pi, with u=(sqrt(1-z^2)cos theta,sqrt(1-z^2)sin theta,z). At fixed z, the inverse-sine sum maximizes at equal positive transverse components, so p<=1-arcsin(z^2)/pi<=exp(-z^2/pi). At z=t/sqrt(n), for 0<theta<pi/2, n log p tends to -t^2/(pi sin 2theta); for other longitude p(0,theta)<1. Gaussian domination permits dominated convergence, giving sqrt(n)(2pi-E[L_n]) -> pi integral_0^(pi/2) sqrt(sin 2theta)dtheta =pi/2 B(3/4,1/2). Independently evaluated the exact integral by numerical quadrature for n=100 and 1000, obtaining scaled deficits about 3.8772 and 3.77557 approaching 3.764068559; quadrature alone is corroborative, not proof.

## originality

PASS

Besau et al arXiv:2203.07916 study the same orthogonal spherical-wedge random-hull model, but their stated two-dimensional main theorem is E[number of edges]~(4/3)log n, not the expected intrinsic perimeter. Bárány-Hug-Reitzner-Schneider arXiv:1505.04672 establish spherical Crofton/mean-width methods for the hemisphere model, which is not the intersecting two-hemisphere wedge and has different supporting-normal degeneracy. The exact n-sample wedge integral and n^-1/2 beta-function perimeter coefficient are not direct restatements of either known theorem. The use of Crofton/Gaussian orthant identities is credited rather than claimed as new; older unpublished random-hull calculations remain residual risk.

## value

PASS

An already-studied natural random spherical-wedge polygon has a sharp geometric deficit law distinct from its known edge-count asymptotic. The exact finite-sample Crofton integral and evaluated beta constant are usable precise invariants and reveal the supporting-normal boundary layer, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
