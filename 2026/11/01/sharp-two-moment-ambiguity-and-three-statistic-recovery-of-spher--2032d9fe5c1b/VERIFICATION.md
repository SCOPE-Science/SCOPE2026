---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Spherical area coordinates have t=x3 uniform on [m-h,m+h] and azimuth uniform. The first and second moment tensor T=diag((1-u-z/3)/2,(1-u-z/3)/2,u+z/3) yields M=2(1-u) and V=4(tr(T²)-u²). Conditional independence given X1 yields C=4uz/3. Completing square V=4/3-4u²+(2/3)(z-(1-3u))². The fold z*=1-3u is strictly interior to (0,(1-sqrt(u))²] exactly for 1/4<u<1/3, giving two widths but at most two; u=3/10 and z=3/50,7/50 yield M=7/5,V=609/625 and C=3/125,7/125. When u>0, z=3C/(4u); u=0 uses V=4/3+2(1-z)²/3 to recover z. Correct across caps, whole sphere, and centered zones, with h>0 and reflection ambiguity. Inspected pinned proof and exact rational checker, independently verified tensor identities and witness; no extrapolation from Monte Carlo.

## originality

PASS

The claimed inverse low-moment fold of a generally nonconvex two-boundary latitude zone and three-sample covariance repair differs from known full-sphere or spherical-convex-cap distance distributions; not merely a special value of the general spherical-convex theorem. Best-of-knowledge PASS while possible zonal inverse-statistics aliases remain.

## value

PASS

Complete sharp inverse-identifiability classification for a natural two-parameter spherical sampling family, including a constructive two-zone ambiguity and minimal shared-endpoint covariance disambiguation. Population-moment identifiability is a concrete stochastic-geometry problem beyond routine chord second moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
