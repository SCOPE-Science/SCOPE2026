# Franklin perfect-matching topology: six two-spheres and no invariant second-homology classes

## Finding
Let \(F\) be the Franklin graph on \(V=\mathbb Z/12\mathbb Z\), with cycle edges \(\{i,i+1\}\) for each \(i\) and six chords \(\{i,i+5\}\) for even \(i\), all indices modulo twelve. Define the perfect-matching complex \(\mathcal M_p(F)\) to have graph edges as vertices and faces exactly the edge sets contained in some perfect matching.

There are precisely 17 perfect matchings, and the complete **integral homotopy type** is
\[\mathcal M_p(F)\simeq\bigvee^{6} S^2.\]
In particular its only nonzero reduced integral homology is \(\widetilde H_2(\mathcal M_p(F);\mathbb Z)\cong\mathbb Z^6\).

The natural full 48-element graph automorphism group acts on this homology. The traces of its rational degree-two representation are \(6\) once, \(2\) twelve times, \(0\) twenty times and \(-2\) fifteen times. Their average vanishes, hence
\[\dim_{\mathbb Q}\widetilde H_2(\mathcal M_p(F);\mathbb Q)^{\operatorname{Aut}(F)}=0.\]
The multiset does not assert an equivariant sphere-wedge decomposition.

## Assumptions and scope
The graph is finite, undirected and simple. Edges are ordered lexicographically and represented by bit positions 0 through 17. Perfect matchings cover all twelve vertices once; partial edge subsets are faces precisely when they extend to a perfect matching. All stated topology is ordinary (nonequivariant) integral homotopy; the symmetry statement concerns only rational homology. The Franklin graph is also called the six-crossed prism and the twelve-vertex Knödel graph \(W_{3,12}\). This theorem concerns that graph alone.

## Proof
First enumerate perfect matchings recursively: choose the least uncovered graph vertex, pair it with each available neighbor, and recurse. There are 17 distinct matchings of six edges. Their downward closure contains the empty simplex and 761 nonempty simplices, with numbers of faces of cardinality zero through six
\[(1,18,117,264,243,102,17).\]
An independent algorithm examines all \(2^{18}=262144\) edge subsets, identifies precisely the same 17 perfect matchings, and reconstructs the same downward closure.

Next construct a discrete-Morse matching on the 761 nonempty faces. In the first stage, repeatedly choose a face contained in exactly one surviving immediate coface, with priority given to the largest face and then the lexicographically smallest bitmask. Verify that the unique coface is maximal and remove the pair. This gives 321 genuine elementary simplicial collapses, leaving a two-dimensional subcomplex with 17 vertices, 56 edges and 46 triangles.

In the second stage, maintain the set of unprocessed nonempty faces of that residual complex. Whenever a face has exactly one remaining codimension-one boundary face, pair the two, prioritizing the smallest possible upper dimension and choosing from sorted candidates with a fixed pseudorandom seed zero. When no such pair exists, declare a cell critical, prioritizing the smallest available dimension. This produces 56 further pairs and leaves exactly one critical zero-cell and six critical two-cells. The choice rule is implemented literally in the accompanying standard-library checker.

For completeness, combine the two collections of pairs on the full original face set. Orient a matched codimension-one incidence from its lower face to its upper face, and every other incidence downward. An exhaustive topological sort visits all 761 faces and verifies that the directed graph, containing 2610 incidences, is acyclic. Thus the pairs constitute a valid discrete-Morse matching. The discrete-Morse CW theorem yields a complex with one zero-cell, six two-cells and no other cells. Every two-cell attaches to the single-point one-skeleton, so the CW complex is exactly a wedge of six two-spheres.

For the symmetry statement, enumerate every adjacency-preserving permutation of the twelve graph vertices using a complete injective backtracking search. Exactly 48 are found. Each induces a permutation \(p\) of the 18 lexicographically ordered graph edges. For any nonempty simplex \(\sigma\), the trace of the induced oriented chain map on its dimension is zero unless \(p\sigma=\sigma\); in the latter case it is the sign of the permutation of its ordered vertices. By the simplicial Lefschetz trace identity, since \(H_0\cong\mathbb Q\), \(\widetilde H_2\cong\mathbb Q^6\) and all other positive rational homology vanishes,
\[\operatorname{tr}(p\mid\widetilde H_2)=\sum_{\substack{\emptyset\ne\sigma\in\mathcal M_p(F)\\p\sigma=\sigma}}(-1)^{|\sigma|-1}\operatorname{sgn}(p\mid\sigma)-1.\]
Evaluating this exact finite expression for all 48 permutations yields the stated trace multiset. Their sum is \(6+12\cdot2+20\cdot0+15\cdot(-2)=0\); averaging characters gives zero invariant dimension.

## Verification
Run `python3 verify_franklin_pmc.py` and `python3 verify_franklin_chain.py` from the directory containing these supplied standalone files. The first program reconstructs the graph, its two-stage matching and complete directed incidence graph, all automorphisms and all signed chain traces. It verifies 377 matched pairs, the seven critical cells, 2610 incidences, 48 automorphisms and the invariant dimension. Its terminal marker is `FRANKLIN_PMC_COMPLETE_ACYCLIC_MORSE_AND_CHARACTER_VERIFIED`.

The independently written second program enumerates every possible graph-edge subset and computes reduced mod-two simplicial homology. It finds 1092 ordinary graph matchings including empty, of which 762 are extendible, and reduced mod-two Betti ranks \((0,0,6,0,0,0)\) in dimensions zero through five. Its terminal marker is `INDEPENDENT_FRANKLIN_PMC_CHAIN_CHECK_PASS`. Both actual outputs are supplied in `verification_output.txt`. The homotopy assertion rests on the complete acyclic matching, not just on finite-field ranks.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega introduce perfect-matching complexes and determine homotopy types for specified **planar** honeycomb patches, not for the nonplanar Franklin graph. Chandrakar and Singh study polygonal **line** tilings and two-row grids, also not this graph. Agarwal and Basak's Möbius-ladder theorem concerns a different graph family; in particular, their twelve-vertex Möbius ladder contains odd cycles, whereas the Franklin graph is bipartite.

The closest located calculation specifically for the Franklin graph, *Edge-orbit matching-complex splitting for the Franklin graph*, treats the **ordinary** matching complex, which permits all matchings. It proves \(\mathcal M(F)\simeq\bigvee^{12}S^3\). The proper extendible-matching subcomplex studied here has 762 faces including empty, compared with 1092 for the ordinary complex, and neither its homotopy type nor its symmetry action is implied by that ordinary-complex classification. Targeted searches under the graph's crossed-prism, Knödel and toroidal-honeycomb aliases found no prior exact statement of the present conjunction.

## Limitations
This is an exact result for one canonical finite graph; it does not classify all crossed prisms, Knödel graphs, toroidal honeycombs or cubic bipartite graphs. The symmetry result specifies rational traces and invariant dimension, not the full integral representation or an equivariant homotopy splitting. An unindexed earlier computation might exist. All finite certificates are reproducible ordinary Python programs, rather than a formal proof-assistant verification.

## References
1. M. Bayer, M. Jelić Milutinović, J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803 (first public 2022-09-06), https://arxiv.org/abs/2209.02803.
2. H. Chandrakar, A. Singh, *Perfect Matching Complexes of Polygonal Line Tiling*, arXiv:2407.05809 (first public 2024-07-08), https://arxiv.org/abs/2407.05809.
3. A. Agarwal, B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph*, arXiv:2608.30601 (first public 2026-08-31), https://arxiv.org/abs/2608.30601.
4. *Edge-orbit matching-complex splitting for the Franklin graph*, published research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-edge-orbit-matching-complex-splitting-for-the-franklin-graph--be4888fadcca.
5. E. W. Weisstein, *Franklin Graph*, MathWorld, https://mathworld.wolfram.com/FranklinGraph.html (graph aliases and LCF description).
