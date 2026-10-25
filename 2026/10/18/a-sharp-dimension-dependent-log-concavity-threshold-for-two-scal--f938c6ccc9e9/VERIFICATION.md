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

From f=e^{-alpha||x||²/2}(1+t) times constant, t=r e^{-delta||x||²/2}, the Hessian equals -u(t)I+delta² t xx^T/(1+t)², with tangential eigenvalue -u<0 and radial sign log r-F_q(t). Verified derivative F'_q=((q+1)t²+2t-q)/(2t²) has unique positive minimum at t_*=q/(1+sqrt(1+q(q+1))), giving exact criterion. Endpoints t=r at origin and t→0 at infinity are negative; when r<R minimum radial curvature stays negative uniformly. At equality a single spherical radial zero; above an open annular positive radial shell. Surjective projection can be whitened, preserving w and scale ratio but replacing d by k. Independent q=1/3 check R=1.1586706546951728, w3≈0.12651 and w4≈0.06753, so w=0.1 is 3D-yes/4D-no. Universal conclusion follows analytic Hessian, not numeric examples.

## originality

PASS

Available original full texts on Gaussian mixtures treat entropy/geometry, Rosenthal bounds, Fisher information, not a pointwise scalar radial-Hessian necessary/sufficient condition coupled to dimension-projection separation. The 2026 mixture separation manuscript and any unindexed sharp Gaussian mixture logconcavity theorem remain plausible risks; accessible abstract does not justify exclusion.

## value

PASS

An exact geometric classification of logconcavity for a canonical parametric Gaussian scale-mixture family, including curvature phase and a striking high-dimensional versus all lower-dimensional marginal separation. The dimension factor Q^d is a substantive threshold, not a cosmetic restatement of entropy bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
