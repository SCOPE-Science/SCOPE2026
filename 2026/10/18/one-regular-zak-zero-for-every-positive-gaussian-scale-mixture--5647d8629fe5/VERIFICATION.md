---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For each Gaussian, Q_s(t,theta)=sum_k K_s(t-k)e^{ik theta} solves a heat equation with twisted boundary condition Q_s(1,theta)=e^{i theta}Q_s(0,theta) and Q_s(0,theta)=sum_l exp[-s(theta+2pi l)²]>0. The imaginary part on 0<t<1 for 0<theta<pi has zero left boundary, positive right boundary, and nonnegative zero initial trace; the strict Dirichlet heat maximum principle proves a uniform positive sign. On theta=pi the real half-interval Dirichlet problem changes sign only at t=1/2; Hopf boundary derivative there is strictly negative. The Gaussian derivative identity ∂t H_b=-2ib ∂theta H_b at the center makes both real-Jacobian diagonal entries negative, with off-diagonals zero. Positive mu integration preserves these common strict signs, and inverse-square-root integrability at a→0 plus center Gaussian decay at a→∞ legitimizes Fubini and differentiation. The q shifted Zak fibers have no simultaneous zero and thus have positive compact-torus lower bound. Independently evaluated multiple finite positive Gaussian mixtures over a grid of h,t,xi and checked sector signs and both central derivatives. These finite checks do not cover arbitrary measures.

## originality

PASS

Best-of-knowledge source/statement comparison, not mere keyword or parameter match: Aliases Gaussian precision mixing, completely monotone squared-radius profiles, theta heat-kernel mixtures and variation-diminishing windows were compared; a general uncatalogued heat-kernel result remains possible. The explicit nonlogconcave and locally nonconvex member blocks the main accessible stronger-window hypotheses. The 2017 apparently close averaged-TP title warrants an explicit access residual risk and cannot be declared NOT_COVERING from abstract only. Inspected theorem hypotheses do not directly imply the stated all-positive-mixture closure. The inaccessible same-topic 2017 full text remains a material, but not on its own disqualifying, originality limitation.

## value

PASS

The zero-set geometry, *regularity* and orientation are structurally stable across the entire positive Gaussian precision-mixture cone, far beyond an individual width. That cone includes smooth non-log-concave, nonconvex two-scale windows and inverse-multiquadrics; known convex/total-positivity criteria cannot simply be invoked. This gives a useful exact zero theorem and a concrete integer-oversampling Gabor frame guarantee for broad windows, not merely an existing frame criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
