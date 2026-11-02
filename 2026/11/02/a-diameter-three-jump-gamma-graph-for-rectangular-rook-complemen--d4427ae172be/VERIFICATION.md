---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification of the bounded-support exchange theorem

The exact predicate is the categorical-product adjacency \((i,j)\sim(i',j')\) if \(i\ne i'\) and \(j\ne j'\). A successful three-cell domination configuration is one of two disjoint families: three distinct rows and columns, or a row-column corner occupying two rows and two columns. This classification is proved mathematically in `RESULT.md`.

Run the included standalone `proof_checker.py` using Python 3. The source has no external dependencies. It has two logically distinct tests. First, for the six boards \(4\times4\), \(4\times5\), \(4\times6\), \(5\times5\), \(5\times6\), \(6\times6\), it compares every three-cell shape to the original direct closed-neighborhood domination predicate and independently compares exact degrees and counts. It checks \(17{,}224\) triples in this stage.

Second, it exhaustively constructs the pattern exchange graphs for all \(25\) ordered pairs \((p,q)\) with \(2\le p,q\le6\). Adjacency is computed exactly by common two-cell subsets. Bitset operations calculate all vertices at distance at most two and at most three from **every** source vertex, with an assertion that the three-step neighborhood is the whole graph. This proves a finite combinatorial lemma used in `RESULT.md`. The largest of these graphs has \(3300\) vertices; all assertions passed. The saved output is `checker_output.txt`.

The infinite conclusion is not deduced from naive extrapolation: any two minimum dominating triples in an arbitrary rectangle occupy at most six row labels and at most six column labels. Relabeling this bounded support embeds them in one of the verified finite exchange graphs. Every intermediate corner/matching triple lifts to a minimum dominating set in the original rectangle. The disjoint-corner witness independently proves that two jumps never suffice for all pairs.

**Limits:** This confirms the bounded finite computation and its use in the written proof, not external or independent mathematical certification; the full literature-priority question remains open to further review.
