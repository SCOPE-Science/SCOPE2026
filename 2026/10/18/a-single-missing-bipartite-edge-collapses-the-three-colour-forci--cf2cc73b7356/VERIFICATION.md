---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For the intact graph the first force requires two colors on one shore, say A, so every proper colored neighbor on B has the third color, and no initially blank vertex on A can ever be forced. Thus one whole shore and exactly two colors there are necessary and sufficient at the minimum n; this gives 2·3·(2^n−2). With matching deletions, a first force still needs two distinct-colored seeds on one shore. With only two seeds any resulting colored vertices across the bipartition are monochromatic, and blanks on the seeded shore cannot move. With three seeds on one shore the same obstruction holds for at most two colors, while three distinct colors forbid any proper extension at the opposite vertex of an index outside the seed indices (n≥4). In the remaining 2+1 case with two distinctly colored seeds on A, a third seed of the unused color on B would leave B monochromatic and A stuck. Reusing one of the A colors requires a missing edge by properness; the only possibilities are the deleted matching pairs. Conversely, from a_i,b_i colored c and a_j colored d≠c, the n−2 vertices b_k outside {i,j} see c and d and force to e. Every blank a_l sees b_i and at least one of these e vertices because it misses at most one; it forces to d. Then b_j sees c and a d from an index other than j and forces to e. This is a proper extension, and any legal force must agree with that extension, so the construction does not rely on a conflicting update order. The unique shared seeded pair makes the product t·3·2·2·(n−1) exact. At each vertex the states are categorical (three color probabilities p, blank 1−3p), independently across vertices; the minimal-size term in the resulting sum of p^k(1−3p)^(2n−k) gives each announced probability expansion.

## originality

PASS

Credit Farr's probability-polynomial relation and the prior exact complete-bipartite polynomial for the intact baseline. The distinct supported result is the full seed classification and count across all nonempty matching deletions under the three-color propagation rule. Earlier crown-graph coloring classifications share an exact count at the perfect-matching endpoint and even similar matched-pair structure, but count different objects; their classification does not prove the seed forcing criterion or its extension to partial matchings. The closest same-family propagation comparison uses a different forcing rule.

## value

PASS

The setup asks a natural perturbation question for a graph forcing invariant: can the sparsest possible missing-edge perturbation change the order of vanishing, and what are the extremizing seeds? One deleted edge lowers the minimum from n to 3 for every n≥4, and the complete classification exposes the causal combinatorial feature (one shared color can now be seeded across the shores). Extending this to every matching size and counting all such triples gives the exact dependence of the first coefficient, not just upper and lower examples on a crown graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
