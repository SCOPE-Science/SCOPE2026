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

The exact target is the ordinary (not total) four-cut complex of P=KG(5,2), not the complement graph. Enumerating 210 four-vertex subsets gives 70 connected and 140 disconnected sets; their complement facets generate 766 faces including empty, f-vector (10,45,120,210,240,140). Independently rebuilt deterministic successive-toggle matching from the actual RESULT.md and verify.py: 369 pairs, a directed Hasse graph with 765 nonempty nodes fully topologically sorted, and precisely one critical vertex plus 26 critical 5-cells. This is an integral discrete-Morse wedge proof, not merely a mod-2 rank check. Independently evaluated signed simplicial Lefschetz traces for all 120 label permutations: the seven S5 conjugacy types give 26,6,-2,2,0,0,1; the source Murnaghan–Nakayama exact inner products yield multiplicities 1,2,1,2. Rational invariants under S5 and A5 both dimension one. The calculation assumes the finite graph exactly and does not establish an equivariant Morse matching or integral S5-lattice.

## originality

PASS

Best-of-knowledge PASS for the specific k=4 Petersen integral homotopy and full S5 rational character. The first ordinary cut-complex paper already covers k=2 for the Petersen graph; the second gives group characters for other graph families. Related Resultary three-cut Petersen and four-cut triangular-complement records do not imply k=4 Petersen results; the high-girth family theorem requires girth >=6 whereas P has girth 5. Character requires signed fixed-face data beyond Euler rank.

## value

PASS

Petersen is a canonical cubic girth-five graph; the four-cut case is immediately outside a natural girth-six k=4 family theorem. Exact integral topology of its 140-facet complex and its complete S5 symmetry character distinguish it from known two/three-cut cases and from the complementary triangular graph. This is a motivated complete classification, including a nonzero invariant class in its symmetry quotient, not merely face-count recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
