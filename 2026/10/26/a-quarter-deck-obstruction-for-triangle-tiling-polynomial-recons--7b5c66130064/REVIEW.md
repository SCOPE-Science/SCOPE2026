# Review: A quarter-deck obstruction for triangle-tiling polynomial reconstruction

**Correctness (C): PASS.** The equal-deck path pair satisfies the hypotheses of Spinoza–West Theorem 1.7. The edge-vertex expansion lemma follows by splitting selected vertices into original vertices and edge-vertices; the count of each induced type is a degree-polynomial of degree at most the number of selected edge-vertices, hence determined by induced subgraphs on at most the deck size. In the expanded forest, triangles correspond bijectively to original edges, and disjoint triangle packings correspond to matchings. The perfect-matching coefficient differs by parity of \(\ell\).

**Originality (O): PASS, residual risk.** Kim–Lee's Theorem 1.4 and Corollary 1.6 give the upper bound and explicitly leave the asymptotic optimal fraction open in Problem 6.1; they do not state this lower bound. Spinoza–West provide the path-forest deck pair but do not transfer it to triangle-tiling polynomials. Targeted bibliographic searches for the exact constant and triangle-tiling deck lower bounds returned no matching claim. Unindexed work or a published equivalent transfer lemma may remain undiscovered.

**Value (V): PASS.** The claim gives a concrete positive lower bound for the exact asymptotic invariant identified as open in the 2025 reconstruction paper. It converts a known deck-equivalence phenomenon into an obstruction for a different, natural spanning-structure polynomial and narrows the possible interval from the known upper bound alone.

Closest literature: Kim–Lee (2025), which proves the general upper bound and poses Problem 6.1; Spinoza–West (2016), which proves equal decks for the path-forest pair. Neither source states the expansion transfer plus \(c_{K_3}\ge1/4\).

Self-review: passed. Independent audit: not yet performed.
