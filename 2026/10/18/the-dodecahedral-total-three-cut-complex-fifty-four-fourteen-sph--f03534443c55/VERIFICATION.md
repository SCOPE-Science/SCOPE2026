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

For the 20-vertex cubic triangle-free dodecahedral graph GP(10,2), X=total-three-cut has facets complements of independent triples. Its Alexander dual K consists exactly of subsets with independence number≤2; R(3,3)=6 gives |face|≤5. Complete counts in sizes 0..5 are (1,20,190,480,375,12). Exact signed integer boundary reductions ∂1..∂4 have ranks (19,171,309,12), unit Smith factors and zero remainder, hence reduced integral H3(K)=Z54 only. On 20 vertices combinatorial Alexander duality and UCT yield reduced H14(X)=Z54, others zero. The complete 13-skeleton ensures sufficient connectivity; Hurewicz and homology Whitehead give X≃54 S14 (not mere homology). A separate independently implemented Python check reconstructed all 660 independent triples, K face vector, primitive boundary ranks and all 120 automorphisms and signed Lefschetz character. Traces grouped by order are 1:54×1, 2:6×31, 3:0×20, 5:-1×24, 6:0×20, 10:1×24. Average gives 2 invariant dimensions; central antipode ± eigendim 30/24. Pure dimension16 and H14 nonzero excludes shellability.

## originality

PASS

PASS (best knowledge): No inspected family formula covers total 3-cut on the dodecahedron or its complete rational 120-element character. Indexed near neighbors differ either by graph or by complex.

## value

PASS

PASS: Total cut is an established natural graph-topology construction. The dodecahedron is a highly symmetric Platonic graph outside previously solved chordal/cycle families. A pure 16-dimensional but homotopy 54 S14 example is a genuine non-shellability phenomenon, and full rational icosahedral symmetry character distinguishes the homology module from its rank. The exact integral homotopy and character are motivated, not arbitrary recomputations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
