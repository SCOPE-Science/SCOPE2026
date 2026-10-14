---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Reconstructed Calussi et al. Example 4.1 exactly: Khatri–Rao M has rank 5 and kernel generator [0,-2,0,3,2,2], giving a point projection of the smooth Segre P¹×Y into P⁴. The conic Q=9z0²−18z0z1+18z0z2+11z1²+z1z2−28z2² has symmetric determinant −5913/4≠0. The center row line z=(3,2−2t,2) meets Y at two distinct points, Q|line=44t²+16t+17 with discriminant −2736. Rank-two secant decomposition uniqueness gives one double fiber, and non-tangency rules out ramification elsewhere. Independent exact arithmetic over Q(ω), ω²=−19, verifies both preimages map to q=[0:17:−51:−66:−77:−44] and five tangent image vectors have nonzero minor 2357771608607690880 ω; the branches are transverse. Their completed local intersection is C[[u,v,s,t]]/(us,ut,vs,vt). Independent Gröbner reduction of the Fitting/Jacobian 2-minors gives exactly m²; basis 1,u,v,s,t gives scheme length 5. This proves support and analytic germ rather than inferring them from degree alone.

## originality

PASS

The primary Example 4.1 reports singular dimension zero and degree five, not the support or transverse two-branch analytic type. The local classification and Fitting explanation are new relative to the inspected preprint. A later 2024 monograph is a high-relevance unresolved-access risk, not an automatic novelty veto.

## value

PASS

It resolves the geometric meaning of a published degree-five singular-scheme computation: instead of five nodes or unspecified fat points there is one transverse double surface point with precisely determined completed local ring and embedded Jacobian length five. Such an exact local classification of a natural counterexample to generic Hadamard smoothness is independently useful in singularity, projection and scheme calculations; not an arbitrary slice or a recomputed degree.

The dated certificate retains the supplied scientific assessment, sources and limitations.
