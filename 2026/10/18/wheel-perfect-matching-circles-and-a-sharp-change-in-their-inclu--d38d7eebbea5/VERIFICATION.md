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

Every perfect matching contains exactly one hub spoke s_i; deleting its incident rim vertex leaves an even path with a unique perfect matching, yielding N=2r+1 facets M_i. The rim-edge incidence sets S_j={j+2,j+4,...,j+2r} in facet index, and inverse-of-two relabeling identifies their nerve with the cyclic length-r interval complex B(N,r). All nonempty facet-simplex intersections are contractible. For each 3<=t<=r, cyclic length-t facet has free endpoint edge because 2(t-1)<N, and its upper Boolean interval removes in 2^(t-3) elementary pairs; different intervals are disjoint. Hence B(N,r) simplicially collapses to B(N,2)=C_N in N(2^(r-2)-1) pairs, giving P_r≃S1. Equivariant nerve (simplex intersections have fixed barycenters) and circular-arc model yield rotations degree +1, reflections -1 on integral H1, without asserting the collapse itself equivariant. At r=2, enumeration shows M2 is P2 plus exactly five edges and no new triangles, so M2≃wedge^6 S1 and inclusion primitive split; at r>=3 Vega Theorem 5.2 makes ordinary wheel matching complex a wedge of spheres in dimension ceil((2r-2)/3)>=2, thus simply connected and the map from S1 null. Purity of P_r dimension r and nonzero H1 precludes pure shellable/CM. Independently checked finite r=2..7 facet incidences, nerve equality and Euler 0; finite test alone cannot prove the uniform statement.

## originality

PASS

Best-of-knowledge statement-level originality is limited to the differentiated new result, with credited general tools, broader prior coverage, and recorded access risks. Known cyclic nerve circle and ordinary wheel matching targets do not themselves state the perfect-matching wheel correspondence and sharp inclusion map.

## value

PASS

The distinction between an extendible-perfect-matching subcomplex and the ordinary matching complex is a natural topological graph invariant. The all-wheel identification, explicit collapses, dihedral character and sharp change in the inclusion map are structurally meaningful, not a relabeling of the published cyclic-arc nerve: the wheel-specific graph-to-nerve bridge and exceptional six-vertex cell attachment must be established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
