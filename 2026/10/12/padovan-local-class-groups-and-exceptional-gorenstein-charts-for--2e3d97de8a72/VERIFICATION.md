---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For the projective wheel edge polytope P_n=conv(e_i,e_i+e_{i+1})⊂Z^n, Ohsugi–Hibi normality applies: odd wheel cycles either triangles sharing hub or (when n odd) the rim, satisfying odd cycle condition. Fundamental independent rim sets are precisely dominating independent sets of C_n, whose consecutive cyclic gaps are 2 or 3; compositions count a_n with a0=1,a1=0,a2=a3=1,a_n=a_(n−2)+a_(n−3). The exact facets are coordinate xj≥0, lower total Σx≥1, upper Σx≤2 iff odd n, plus Σ_{i in S}xi≤1 for maximal independent rim S. At spoke e0 active primitive normals comprise n standard-unimodular basis rays plus a_n rim-independent facets, so local Cl=Z^a_n. At rim e0+e1 active rays are n−2 coordinate rays, 2a_n independent facets and odd upper facet; a unimodular basis again gives torsionfree rank 2a_n−2+[n odd]. Rational canonical support requires m0=n−2=|S| at spoke, forcing n=4, and every maximal C_n independent set same size at rim, precisely n=4,5,7 via 2/3 gap partitions, with odd upper-sum m-vector condition satisfied. Solutions integral in all cases; rim n=4 is only smooth fixed chart. Independently enumerated C_n maximal independent sets and formed exact integer ray matrices; for each n=4..10 found correct class ranks, full rank, and Q-Gorenstein linear solvability for spoke/rim, using SymPy exact rational ranks. Finite tests corroborate, Ohsugi–Hibi facet theorem plus combinatorial argument prove all n.

## originality

PASS

Ohsugi–Hibi 1998 explicitly owns normality and facet theorem of graph edge polytopes; 2008 classifies globally SIMPLE graph polytopes, not local class groups and canonical Q-Cartier support at individual wheel torus-fixed points. Well-covered cycle exception list C4,C5,C7 is known, but knowing it alone does not imply the toric chart canonical class condition or torsionfree Padovan ranks. Resultary's 'symmetric edge polytope of wheel' records use conv(±(e_i−e_j)), an entirely different polytope from the projective edge-monomial polytope conv(e_i+e_j). No exact literature source with the combined local class group + wheel Gorenstein chart classification was located. Best-of-knowledge originality and aliasing risk explicitly recorded.

## value

PASS

Complete exact local divisor class-group ranks and Gorenstein/smoothness classification at all wheel torus-fixed points is a natural toric invariant family, not just a recomputation of the Padovan sequence. The exceptional singular but Gorenstein n=7 rim charts and non-Q-Gorenstein behavior elsewhere give a sharp structural boundary suitable for comparisons of graph edge-toric singularities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
