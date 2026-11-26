---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In the rank-six affine lattice, Edmonds' inequalities cover every facet. Singleton, complement-of-singleton and Fano-line inequalities suffice: rank-two pair constraints follow from the coordinate upper bounds and all rank-three upper constraints follow from the coordinate lower bounds and total sum. The candidate supporting vertex sets of affine rank 5 give 21 actual facets. Taking all intersections (including the full and empty faces) gives 772 faces, with proper nonempty face vector (28,126,245,238,112,21). At a d-face the normal cone is spanned by the distinct primitive active facet rays (1_{i∈S}−1_{7∈S})_{i=1}^6 and has dimension k=6−d. Regularity is exactly k rays with determinant divisor 1 in the ambient lattice, equivalently a basis of the saturated span. The exhaustive replay gives 308 nonregular cones and no simplicial nonregular ones. The orbit closure order is the face inclusion order, so the 70 maximal singular faces yield exactly the irreducible components of the reduced locus: (dimension, vertices, rays)=(3,4,4)×21, (2,4,5)×21, (2,3,5)×28. All invertible binary point transformations were checked; each of the three types is one orbit. For each such cone the transverse toric chart uses the saturated span; the determinant divisor 1 for the full ray set makes the dual divisor-sequence cokernel torsion free, and k+1 rays give free rank one. This establishes Cl≅Z, and cone simpliciality is the local Q-factoriality criterion. A finite quotient of a smooth germ is Q-factorial, so it cannot describe these generic singularities. Fresh standard-library replay: python3 /workspace/branches/284f24b9-91f2-4abb-a478-b24e8f372f80/reproduce_fano_normal_fan.py; results in fano_reproduction.log alongside it. The frozen checker was inspected, not executed. The proof concerns the reduced singular locus of this toric variety, not any scheme multiplicities or a classification of general matroids.

## originality

PASS

The distinct result is the exhaustive positive-dimensional component and singular-orbit classification, including unimodularity of all simplicial cones and the generic transverse class groups. Resultary ab9ef237f801 is materially overlapping: it implies the Fano facet count and the singular, non-Q-factorial fixed points. It does not classify positive-dimensional strata, and its fixed-point theorem does not imply the claimed component types, total strata count, or transverse class groups. Neither the common catalogue date nor the titles decide priority. The previously inaccessible Fano-specific source was inspected at its relevant theorem and triangulation section; these are not the asserted normal-fan classification.

## value

PASS

This is a complete geometric classification for a canonical matroid, not a sample of cone singularities. The 70 components in two dimensions and three symmetry types, 308 strata and equality of singular and non-Q-factorial loci distinguish the variety substantially beyond fixed-point information. The generic class-group statement describes the local failure of Q-factoriality on every component type.

The dated certificate retains the supplied scientific assessment, sources and limitations.
