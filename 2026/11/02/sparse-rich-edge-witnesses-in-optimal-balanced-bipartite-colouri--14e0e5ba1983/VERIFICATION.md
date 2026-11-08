---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The endpoints of any rich-edge set form a vertex cover of K_n,n, so at least one whole part is covered and |R|≥n. For n≥4, divide one part into d and n−d (each ≥2), choose disjoint palettes X,Y of n−1 and z, fill cyclic Latin rectangles on the two complementary blocks, and complete two center rows with unused colors and z. Checking incident color intersections shows exactly the n edges of two stars are rich and all edges have an adjacent distinct rich edge. Every rich edge forces at least 2n−1 colors. n=2 requires four all-distinct colors; for n=3 the exhibited five-color matrix gives exactly four rich edges, while any putative 3-rich set must be a star (rich-edge P4 impossible at 2n−1 colors) and then would force a K_3,2 proper coloring from only two unused colors, impossible. Independent direct edge-neighbor tests checked all splits for n=4..14; full normalized order-three five-color enumeration found minimum four, independently confirming but not replacing the all-n proof.

## originality

PASS

Best-knowledge PASS for sharp minimum rich-edge support conditional on an optimal color palette. Kong 2026 proves the chromatic-index minimum, but the color-count theorem does not determine or imply this support optimization. General total edge domination is weaker because it omits simultaneous 2n−1 proper palette realizability.

## value

PASS

Exact joint optimization of local witness sparsity and minimal palette on the canonical balanced complete bipartite family; resolves the natural n=3 exceptional obstruction and every n≥4 without arbitrary slicing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
