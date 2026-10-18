---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For C_{2m} stable-set P, primitive outward facet rays r_i=-e_i and s_i=e_i+e_{i+1} become signed apex/rim graph-incidence columns under bipartition sign twist, hence totally unimodular. A normal cone is nonsmooth exactly at dependent active facet rays. Feasible graph circuits are whole rim (alternating 1-dimensional face F_alt) or apex-rim path circuits; each active latter forces the four-ray cone for F_i:x_i=1. Thus singular reduced components are L=F_alt orbit closure P1 and n pairwise incomparable Y_i, each toric path stable-set of dim n-3. Their saturated primitive circuit relations yield transverse 2x2 and m x m rank-one determinantal cones, with node and binom(2m-2,m-1) multiplicities. Intersections of Y_i for nonempty S are nonempty iff S is stable; remaining induced complement-N[S] graph is disjoint paths; unimodular fence-poset equivalence and Stanley linear-extension theorem imply degree multinomial(d;d_j) prod E_{d_j}. L intersections iff S single parity, one endpoint. Independent full face incidence test on C6: 18 stable vertices, 403 nonempty faces, 7 maximal non-simplicial faces, top degrees n=6,8,10 -> 12,128,2720; not a proof for all n.

## originality

PASS

Scientific best-of-knowledge assessment after independently reading the frozen RESULT.md and recreating relevant proof/calculation, checking Resultary and named primary source statements. Wagner 1996 and the Lakshmibai--Mukherjee 2007 Theorem6.9 give general Hibi singular-locus criteria, so an abstract method for locating nonsmooth orbits is PRIOR. Stanley 1986 already gives path-fence volumes Euler zigzag numbers. The claimed new synthesis is a complete even-cycle specialization with an extra singular line of different codimension, generic rank-one determinantal transverse models and complete intersection-degree formulas for all selected Y_S. General statements alone need explicit circuit/face analysis; no exact same-specialization earlier table was located in targeted searches.

## value

PASS

Even-cycle stable-set polytope varieties are canonical graph toric varieties. The theorem determines their non-equidimensional singular support, generic local multiplicities and degrees not only of irreducible components but all component intersections for every even n>=6, a motivated complete structural classification useful in singular and intersection geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
