# Decagon mobility and two-cycle antipodes among Coxeter perfect matchings

## Finding
Let \(X\) be the 28-vertex Coxeter graph. Write \(\mathcal M\) for its perfect matchings. For an even integer \(\ell\), let \(F_\ell(X)\) be the graph on \(\mathcal M\) in which distinct matchings are adjacent precisely when their symmetric difference is the edge set of **one simple cycle of length \(\ell\)** in \(X\). Then:

1. \(|\mathcal M|=84\) and \(F_8(X)\cong42K_2\). In particular, eight-cycle switches fail to connect the perfect matchings.
2. \(F_{10}(X)\) is connected and four-regular, with \(84\) vertices, \(168\) edges, radius \(6\), and diameter \(6\). Every vertex has distance-layer sizes \((1,4,12,25,28,13,1)\).
3. Every matching \(M\) has a **unique** matching \(M^*\) at ten-switch distance \(6\). An unordered pair \(\{M,N\}\) has ten-switch distance \(6\) **if and only if** \(M\triangle N\) consists of exactly two disjoint alternating cycles, one of length \(8\) and one of length \(16\). There are precisely \(42\) such unordered pairs. These are *not* single 24-cycle switches.
4. The unique eight-cycle-switch neighbor of any \(M\) is at ten-switch distance \(5\) from \(M\).

Since \(X\) has girth \(7\), no alternating-cycle switch of length below \(8\) is possible. Thus \(10\) is the **smallest allowed cycle-length bound that makes the perfect-matching space connected**: allowing all alternating cycles of length at most \(8\) is insufficient, whereas allowing cycles of length at most \(10\) is sufficient. Ten-cycle switches alone already suffice.

## Assumptions and scope
All graphs and matchings are finite, simple and labeled. Set \([7]=\{0,1,\ldots,6\}\) and define the seven Fano lines \(\mathcal L=\{\{t,t+1,t+3\}\pmod 7:t\in[7]\}\). One explicit model of \(X\) has vertex set \(\binom{[7]}3\setminus\mathcal L\); two vertices (three-element subsets) are adjacent if and only if they are disjoint. There are \(28\) vertices, and every vertex has degree three. The graph has girth seven.

An alternative model has seven hub vertices \(h_t\) and three seven-element satellite rings \(c_t,d_t,e_t\), with indices in \(\mathbb Z/7\mathbb Z\). The edges are \(h_tc_t,h_td_t,h_te_t\), along with \(c_tc_{t+1}\), \(d_td_{t+2}\), and \(e_te_{t+4}\) for each \(t\). The supplied explicit permutation verifies that these two models are isomorphic. Thus all conclusions are graph-invariant and independent of the labels.

An alternating cycle must alternate between edges in \(M\) and edges outside \(M\). For perfect matchings \(M,N\), the symmetric difference is a disjoint union of alternating even cycles; for an edge of \(F_\ell(X)\), it must be a **single** cycle. The radius, diameter and distances in the finding refer to \(F_{10}(X)\), not to the original Coxeter graph or to a graph allowing arbitrary-length switches.

## Proof
The assertion is a finite exhaustive theorem, with a self-contained complete enumeration and two independent computation paths, rather than extrapolation from sampled instances.

**Step 1: Exhaustive perfect-matching generation.** Form the explicit \(42\)-edge Coxeter graph from its \(28\) nonline triples. To enumerate perfect matchings, take the set of vertices not yet covered, choose one uncovered vertex \(v\) (the first verifier uses a minimum-remaining-partner pivot; the second uses the smallest index), and branch on each edge \(vw\) to another uncovered vertex. Remove \(v,w\) and recurse; the empty uncovered set produces one matching. Every perfect matching has exactly one incident matching edge at \(v\), so these branches are disjoint and exhaustive. The first verifier returns \(84\) distinct matchings, all of size \(14\). This count agrees with the previously reported \(84\) one-factors; it is not itself the new assertion.

**Step 2: Exact switch construction.** For every unordered pair among the \(84\) matchings, the first verifier computes the symmetric difference. Since it is a disjoint union of even cycles and the Coxeter graph has girth seven, at total lengths \(8\) and \(10\) the condition that every incident vertex has difference-degree two is equivalent to having exactly one cycle (two such cycles would require at least \(16\) edges). This exhaustive pair test gives \(42\) undirected eight-switch edges and \(168\) undirected ten-switch edges. Every eight-switch vertex has degree one, and every ten-switch vertex has degree four.

For an independent construction, the second verifier uses the seven-star, three-ring graph model, enumerates all perfect matchings recursively, then directly performs depth-first enumeration of simple \(8\)- and \(10\)-cycles alternating against each matching. Flipping their matched/unmatched edges produces exactly one eight-switch neighbor and four ten-switch neighbors for every matching. An explicit \(28\)-point isomorphism certificate in `verify_models.py` identifies the two host graphs.

**Step 3: Distances, connectivity, and antipodes.** From every one of the \(84\) matchings, run breadth-first search in the ten-switch graph. Both verification methods reach all \(84\) matchings and independently return the same layer sizes \((1,4,12,25,28,13,1)\). This proves connectedness, regularity, radius and diameter. Exactly one vertex lies at distance six from each starting vertex, giving \(42\) unordered diametral pairs.

For every pair of matchings the first verifier also decomposes its symmetric difference into connected even-cycle components. Exactly \(42\) unordered pairs have cycle-length partition \((8,16)\). Every one of these has ten-switch distance six; conversely, every one of the \(42\) diameter pairs has this partition. The second verifier independently checks both implications in the seven-star model. Finally, each of the \(42\) eight-switch edges joins two vertices at ten-switch distance five, as both verifiers confirm.

**Step 4: Sharp smallest allowed length.** Every alternating cycle has even length. A simple graph of girth seven has no cycle of lengths \(2,4,6\); the eight-switch graph has \(42\) components, while the ten-switch graph is connected. Hence the smallest permitted upper bound is \(10\), as asserted. \(\square\)

## Verification
Run the three programs in the same directory using Python 3 and the standard library only:

```
python3 verify_fano.py
python3 verify_claws.py
python3 verify_models.py
```

The first program additionally writes `fano_certificate.json`, giving the \(42\) labeled Coxeter edges, every one of the \(84\) perfect matchings, the full eight- and ten-switch adjacency lists, and the antipodal matching indices. The original execution's `fano_output.json`, `claws_output.json`, and `model_output.json` record the exact outcomes. The two main programs agree in every common invariant. The model verifier checks an explicit vertex permutation carrying the ring construction to the Fano-triple construction. All three were replayed successfully from actual standalone package paths before acceptance.

The scripts verify the girth-seven premise directly, enumerate *all* matchings, check *all* relevant candidate pairs or alternating cycles, and explore *every* ten-switch starting vertex. Each assertion therefore follows from finite exhaustive computation with complete code, not an unbounded computational search or a probabilistic experiment. The appended certificate can be checked against the program output without reliance on a previously computed external data table.

## Relationship to prior work
Klymenko's 2011 Coxeter-graph exposition gives the \(84\) perfect matchings and shows that the graph automorphism group acts transitively on them. It does not give the fixed-length alternating-cycle exchange adjacencies, their distances or the two-cycle antipodal relation. The later published matching-polynomial table likewise reports the count \(84\) but does not establish this transformation metric in its accessible material.

Figueroa, Fresán-Figueroa and Rivera-Campo's 2015 work studies perfect-matching graphs defined by prescribed families of cycles, including necessary and sufficient criteria for connectedness in general graphs and special bipartite classes. Its accessible manuscript does not give Coxeter-specific ten-cycle adjacency or distance distribution. No general connectivity criterion supplies the present exact finite graph without additional graph-specific hypotheses and verification. Ito et al. (2019) analyze the unconstrained alternating-cycle model; arbitrary-length switches always connect, which does not imply connectivity under a fixed length bound, much less its sharp threshold and exact distances.

The present classification is specifically about the small highly symmetric, girth-seven, non-Hamiltonian Coxeter graph. It is not a theorem about arbitrary cubic graphs, nor is it a new perfect-matching count. The principal new objects are the sharp length-restricted mobility, the uniform distance profile and the exact geometry of the unique farthest pairs.

## Limitations
This is an exact finite classification for the 28-vertex Coxeter graph; it does not generalize the distance profile to all girth-seven cubic graphs. The current literature comparison cannot exclude unpublished or differently indexed equivalences. A relevant 2025 matching-polynomial article was accessible only through search excerpts during this study; no whole-document noncoverage conclusion is inferred from it. The available 2011 exposition and the 2015 cycle-family manuscript were inspected substantively; the 2019 preprint was compared at its definitions, theorems and relevant introduction sections. Independent external mathematical validation has not been performed.

## References
1. A. Klymenko, *The Coxeter graph*, University of Primorska lecture slides, explicitly dated 23 May 2011, https://www.famnit.upr.si/files/files/seminarji/coxeterpresentation-Anna%20Klymenko.pdf. Slides 11–18 discuss all \(84\) one-factors and transitivity.
2. A. P. Figueroa, J. Fresán-Figueroa and E. Rivera-Campo, *On the perfect matching graph defined by a set of cycles*, Boletín de la Sociedad Matemática Mexicana, 2015 online, DOI 10.1007/s40590-015-0079-1; accessible full manuscript at https://www.researchgate.net/publication/284929468_On_the_perfect_matching_graph_defined_by_a_set_of_cycles.
3. T. Ito, N. Kakimura, N. Kamiyama, Y. Kobayashi and Y. Okamoto, *Shortest Reconfiguration of Perfect Matchings via Alternating Cycles*, arXiv:1907.01700, 3 July 2019, https://arxiv.org/pdf/1907.01700.
4. *Matching Polynomials of Symmetric, Semisymmetric, Double Group Graphs, Polyacenes, Wheels, Fans, and Symmetric Solids in Third and Higher Dimensions*, *Symmetry* 17 (2025), article 133, https://www.mdpi.com/2073-8994/17/1/133 (accessible abstract/excerpts only).
