---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Petersen KG(5,2) has exactly ten indexed vertices, permitting complete enumeration of all 2^10 subsets. Independent bitset connectivity reconstruction finds 120/65/10 disconnected-complement facets at k=5/6/7 and exactly 496/211/51 faces including empty. Independently reconstructed greedy face-toggle Morse matchings have 241/100/20 pairs, topological-sort acyclicity on the entire oriented Hasse diagram, and critical cells (5 dim3+9 dim4)/(11 dim3)/(11 dim1), plus one vertex. The signed integral 5×9 Morse boundary in the k=5 case has exact rank four with a unit 4×4 minor and explicit row relation, giving four unimodular cancellation pairs and S³∨5S⁴, not merely mod-two homology. k6 and k7 are wedges of eleven spheres of dimensions 3 and 1. Exhaustion confirms k≥8 void. No claim about other graphs.

## originality

PASS

Best-of-knowledge originality after actual source and implication comparisons. Smaller cut levels do not determine homotopy types of strict subcomplexes at higher k. Total-cut k=3 and matching-complex results are categorically different simplicial complexes. Bayer et al. 2024 establishes Petersen k=2; other published SCOPE results treat k=3 and total k=3. High-girth graph formulas require hypotheses Petersen girth five fails for k≥5.

## value

PASS

The Petersen graph is a canonical finite nonchordal symmetric graph discussed in the foundational cut-complex paper. Completing its three terminal nonvoid ordinary-cut homotopy types gives naturally motivated exact topological invariants, including a mixed-dimensional integral wedge and a sharp nonshellability witness. Being finite does not make this a rote table computation; exhaustive Morse theory is material.

The dated certificate retains the supplied scientific assessment, sources and limitations.
