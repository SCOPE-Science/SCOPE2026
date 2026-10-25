---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For K=s conv(v0,…,vk)+B₂ⁿ, with regular centered simplex {vi}⊂U, n>k≥2, the proposed t>0 solves nt²+(n−k)st=k; t≤sqrt(k/n). Let p=||P_U u|| for a unit direction. The actual support satisfies h_K(u)=1+s max_i〈vi,P_Uu〉≤1+sp, with equality precisely for projected normals pvi. The proposed ellipsoid with squared radii A=(1+st)(1+s/t), B=1+st has support gap A p²+B(1−p²)−(1+sp)²=(s/t)(p−t)²≥0; it contains K in all directions. Equality normals p=t and projected vi yield exactly (s+t)vi+sqrt(1−t²)w as contacts. The normalized contact squared U and U⊥ portions are k/n and (n−k)/n. Taking each vi with signed unit basis in U⊥ yields finite equal-weight isotropic normalized mean 0, covariance I_n/n. Any encompassing ellipsoid then obeys a trace inverse-square constraint and AM-GM forcing determinant ≥1 with equality only at identity, certifying global Löwner optimality without symmetry assumptions. Differentiating log κ_n A^{k/2}B^{(n−k)/2} along parameter t(s), stationary derivative eliminates t′ and gives k/(s+t) and negative second derivative, with s=0 and s→∞ correct limits. Independently checked support identity and contact norms over 330 triples, including six support directions each; these calculations are finite corroboration only.

## originality

PASS

General minimum-volume ellipsoid theory and algorithms for convex hulls of ellipsoids include K as input, but standard existence/approximation does not supply this exact family-specific formula and contact classification. Güler–Gürtuna Section 8 treats convex hulls of TWO parallel ellipsoidal sections, a different object from k+1≥3 ball centers of full simplex dimension. A possibly relevant full Yıldırım paper was inaccessible after open-access attempts; this is explicit priority risk, not proof of coverage or ground for automatic O rejection.

## value

PASS

Regular simplices thickened by Euclidean balls are a natural prototypical polytope parallel body, distinct from a line-segment capsule. The exact outer ellipse, complete continuous contact locus in each normal sphere, scale-independent k/n energy split and strictly concave log-volume growth are reusable extremal geometry facts inaccessible from a generic algorithmic approximation guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
