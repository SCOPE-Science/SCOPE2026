---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

The final claim is correct for every n>=2 in Ardila's exact integral realization in M_n×M_n with the inherited Euclidean norm. Expanding a bipermutation into its n first/unbarred and n second/barred occurrences gives a bijection to the ordered odd integers and u_pi with ||u_pi||²=2n(4n²−1)/3. Because the unique singleton is expanded to adjacent k,bar(k), the two altered coordinates have values p,q with q−p=2. Replacing these two entries by p−s and −q−s gives ||v_B||²=||u_pi||²+2s²+4s. The bar/unbar pattern is a Dyck word; if u_j are the first-occurrence positions, then s=2A−n², A=Σ(u_j−j). The Dyck/Ferrers-staircase correspondence realizes each integer A from 0 to n(n−1)/2; any Dyck word yields a bipermutation by selecting a peak singleton and labeling the matching pairs. Thus s∈{−n²,−n²+2,...,−n} and 2s²+4s strictly decreases over the entire range for n>=2, proving exactly n(n−1)/2+1 radial shells and outer level A=0. The maximum squared norm simplifies to 2n(n−1)(3n²+7n+1)/3. The Euclidean minimum enclosing ball is unique, and Ardila's simultaneous S_n action fixes only 0 in M_n×M_n, so the circumcenter is 0. At A=0, the only adjacent unbarred/barred transition carries the singleton; n choices times two independent (n−1)! orders give exactly n((n−1)!)² farthest vertices. Independent exhaustive enumeration of 116,016 labeled bipermutations for n=2,3,4,5 confirms every coordinate norm, shell count and outer multiplicity; it is corroborative, not an infinite proof.

## originality

PASS

A best-of-knowledge original exact Euclidean radial classification for the canonical bipermutahedron. The defining work gives coordinates/symmetry and a Minkowski quotient, the same-polytope published inball theorem is dual metric data, the harmonic-polytope shell theorem has a different vertex family, and the graph reversal result concerns edge-move distance. Full-text primary sections and closest published findings were compared at implication level; no inspected theorem entails the focal full-shell and circumball formula.

## value

PASS

Ardila's bipermutahedron is a canonical, non-vertex-transitive 2(n−1)-dimensional polytope arising in matroid conormal geometry. Its exact Euclidean vertex-shell spectrum is a natural intrinsic metric invariant of the specified integral realization. The theorem converts an exponentially large set of labeled vertices into the single classical Dyck-area statistic; it gives every distinct shell, a sharp minimum enclosing sphere and exact outer-shell contact count for all n. These are reusable geometric and combinatorial data not determined by the inspected facet, fan, graph-distance or harmonic-polytope results. The calculation is self-contained rather than a general theorem for all deformations; it is not an arbitrary finite slice or an unmotivated numerical recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
