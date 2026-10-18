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

PASS. From Ardila Proposition 2.8 every bisubset has origin slack sigma=n^2-(u-v)^2 and squared intrinsic normal [u(n-u)+v(n-v)]/n. Hence D^2=n sigma^2/[u(n-u)+v(n-v)]. For |u-v|<=n-2 the denominator bound places D strictly beyond n(2n-1)^2/(n-1); the remaining (n-1,0) and (0,n-1) give the optimum, 2n facets. Averaging under the full symmetry makes the origin optimal; inequalities of these tangent facets force x_j,y_j>=0 and sum zero, yielding unique center. n=2 six facets give the exceptional incenter interval. Independent enumeration all 3^n-3 valid bisubsets for n=2..7 gave radii squared 16,75/2,196/3,405/4,726/5,1183/6 and counts 2,6,8,10,12,14. Finite checks corroborate the full algebraic argument.

## originality

PASS

PASS, best-of-knowledge. Ardila arXiv:2008.02295 Proposition 2.8 (primary full PDF opened and exact facet page visually inspected) proves the H-facet description and maximal symmetry, not the normalized facet-clearance minimum or exactly 2n tangent facets. Searches checked inradius/insphere/Chebyshev-center and radial/circumscribed variants; the closest same-object public metric record treats vertex radial shells and does not imply inradius. Generic deformed-permutahedron facet work lacks this specialized offset/radius comparison. A missing old metric table remains an acknowledged risk.

## value

PASS

PASS. This is a natural exact intrinsic Euclidean inball of the maximally symmetric bipermutahedron, with complete global facet-distance comparison, all-n uniqueness and exceptional n=2 center freedom. It adds a metric constraint to known combinatorial facet theory not extractable from face counts or vertex shells. It is not the routine normalization of one selected facet: all 3^n-3 facet orbits and optimizer uniqueness matter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
