---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For m≥4, n≥5, neighborhood facets in K_m □ C_n are exactly F_(a,i)=(R_i\{a})∪{(a,i−1),(a,i+1)}. Uniqueness of the opposite-wing pair's common center for n≥5 gives valid descending-dimension elementary collapse pairs, then one-wing high-cardinality faces similarly collapse, leaving each row boundary B_i=∂Δ^(m−1)≃S^(m−2), m(m−1) cross edges per interface and 2m(m−2) fan triangles. I inspected verify_neighborhood_cycle_products.py at its frozen source Git blob; it checks individual free-coface conditions and equality with the explicit core. The cross-edge relation graph is the line graph of connected K_(m,m) minus the diagonal; choosing a tree of E−1 relations cancels all but one bridging 1-cell per interface. Because B_i is simply connected for m≥4, remaining interface 2-cells null-attach and split λ=2m(m−2)−[m(m−1)−1]=m²−3m+1 independent S² per interface. n bridges form a circle, so N≃S¹∨(∨^n S^(m−2))∨(∨^(nλ) S²). Independent direct adjacency-to-faces and F₂ boundary rank tests give (m,n)=(4,5): β1=1,β2=30; (4,6):1,36; (5,5):β1=1,β2=55,β3=5; (5,6):1,66,6. The proof, not these finite examples, covers all m,n. At m=4 the two species of 2-spheres combine to 6n; no extension below m=4,n=5 was assumed.

## originality

PASS

Best-of-knowledge PASS for the full open-neighborhood homotopy of the entire K_m □ C_n family, not for local clique-prism topology or the different total-two-cut functor. Direct full-text primary Shukla and Chauhan–Shukla–Vinayak comparisons do not imply this statement: the first assumes degree≤3 or particular 4-regular circulants, whereas these products have degree m+1≥5; the second computes total 2-cut complexes for some same graphs but different simplices and sphere dimensions. Resultary's K_m □ K2/prism local answer is considered, but does not supply the n-cycle gluing, fundamental S1, or nλ multiplicities automatically. Risks from other product graph-complex formulae recorded.

## value

PASS

A uniform two-parameter infinite-family integral homotopy classification for a canonical cartesian graph product, with mixed sphere dimensions and precise multiplicity, is substantive. The local free-face collapse and crown graph relative cancellation explain a persistent S1 factor and cannot be replaced by a finite numerical table; it is a useful topological structural theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
