---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For n>=2, C^2 support functions with positive curvature-radius operator, use Besau–Hoehner line-symmetric-difference definition with Haar probability and c_n=omega_n/(2*kappa_{n−1}) to derive delta1(K,K+tv)=2c_n ∫min(t|u·v|,h_{K−K}(u))dσ. Thus F(t)=2t−delta1=2c_n ∫(t|u·v|−h_D(u))_+dσ. The support inequality for ±tv in D proves F(t)=0 exactly for 0<=t<=T, and strict positivity after contact. Uniform strict curvature yields precisely two antipodal equality normals ±u0 at Tv. In each cap h_D(u)−Tv·u=0.5 ξ^TQ ξ+o(|ξ|^2), Q=∇²_Sh_D+h_D I>0, γ=u0·v>0. Replacing ξ with sqrt(eps γ) Q^-1/2 z, integrating (1−|z|²/2)_+ over R^{n−1}, and accounting for two caps and sphere normalization gives F(T+eps)~2^((n+3)/2)/(n+1) *γ^((n+1)/2)*sqrt(κ_G(D,Tv))*eps^((n+1)/2). Independent planar-ball cap integral ratios ~0.99955 for radii 0.7,1,3; 3D exact 2eps²/(2r+eps) agrees coefficient 1/r. The curvature-positive hypothesis is essential for the nondegenerate exponent, and equality-before-contact is prior work.

## originality

PASS

Best-of-knowledge PASS for curvature-dependent post-contact one-sided exponent and coefficient, while Besau–Hoehner 2022 Proposition 2.6(v) already implies equality throughout intersection; their Definition 1.1 supplies the exact integral. The audited post-contact local curvature asymptotic is not a mere restatement of the covered overlap theorem. Standard local cap asymptotics could yield an equivalent unindexed derivation; residual risk expressly retained.

## value

PASS

The first intrinsic-volume metric is a natural convex-body metric, and the first departure from translation distance is a geometric phase transition. Its exact exponent and curvature/incidence constant give a local inverse measurement of the Gauss curvature of K−K, while exposing the smooth-curvature boundary of the earlier overlap result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
