---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For an admissible rank array, every composite minor condition is stable under the vertex diagonal torus acting by change of bases. A generic one-parameter subgroup gives pairwise distinct weights on the arrow matrix-unit basis of H, so fixed points in projective PH are precisely coordinate points. At a point with exactly one nonzero rank-one arrow all products of length >=2 vanish, so membership in PΩ_r is equivalent to r_{i,i+1}>0 on that arrow. Fixed locus therefore has exactly sum_{i:r_i,i+1>0} d_i*d_i+1 points. Compactly supported Euler characteristic of complex algebraic C*-varieties localizes to the fixed locus even if singular; projectivity identifies χ_c with χ_top. If all direct bounds zero the projectivization is empty. Independent toy example V0=V1=V2=C with both direct bounds1 but composite bound0 gives XY=0 in P1: two points, χ=2. Formal localization, not the toy case, proves all dimensions.

## originality

PASS

Best-of-knowledge PASS: Buch computes classes of the same composite-rank quiver varieties in K theory, and Kinser-Rajchgot identify type-A quiver loci with Schubert geometry; neither inspected primary paper states this ordinary Euler characteristic of the projectivized closed cone nor the direct-arrow-support collapse. The result follows from standard C* Euler localization with a simple but application-specific fixed-point identification. Residual risk: equivariant torus localization may make the result routine to specialists or hidden as a specialization of broader equivariant characteristic-class formulae; no decisive prior implication was found.

## value

PASS

PASS: The natural topological invariant χ(PΩ_r) unexpectedly ignores every longer-composite rank inequality despite singular and proper loci, giving a usable universal closed formula for a standard quiver-degeneracy family. It distinguishes geometric complexity from Euler behavior and may streamline characteristic-class or degeneration checks; its concise localization proof is not merely a relabeling of a known numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
