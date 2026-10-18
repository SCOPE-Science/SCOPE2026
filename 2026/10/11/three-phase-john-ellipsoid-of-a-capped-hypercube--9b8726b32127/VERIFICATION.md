---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Permutation uniqueness reduces shape to aP+bH, a,b>0 and center t*1. Exact halfspace support yields s^2=((n-1)a+b)/n, s<=t, s<=1-t, nt+sqrt(nb)<=tau. At fixed t the determinant maximizer is b=min(t^2,n(tau/n-t)^2); the logarithmic derivative on the rank-active branch has sign tau-(n+1)t and its global maximizer is t=min(tau/(n+1),1/2). These exact inequalities produce all three displayed parameter regions and matching boundaries. Independent substitution checked n=2 and representative n,tau including transitions; the argument, not samples, proves arbitrary n and real tau.

## originality

PASS

Best-of-knowledge the complete three-phase off-center John ellipsoid and two transition locations are not entailed by the inspected uniform-matroid Ehrhart treatment, known halfcube special case or ellipsoids of symmetrized polymatroids. Previous work covers geometric objects/special cases but does not provide all tau, center, anisotropic and contact regimes.

## value

PASS

Exact John ellipsoid and facet-contact regimes are natural affine-invariant-of-Euclidean-realization metric data for uniform-matroid independence polytopes and real capped hypercubes; the intermediate anisotropic phase has independent geometric significance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
