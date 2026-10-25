# A sharp palette threshold and a two-component recoloring obstruction for the thirteen-vertex Paley graph

## Finding

Let \(P\) be the Paley graph on \(\mathbb Z/13\mathbb Z\), with \(i\sim j\) exactly when \(j-i\) is a nonzero quadratic residue modulo \(13\). In particular its connection set is \(\{1,3,4,9,10,12\}\). For every integer \(k\ge 5\), let \(R_k(P)\) have as vertices all proper maps \(c:V(P)\to\{0,\ldots,k-1\}\), with two maps adjacent precisely when they differ at one vertex. Color names and graph vertices are **not** identified under permutations.

The chromatic number is \(\chi(P)=5\). The graph \(R_5(P)\) has exactly \(45{,}240\) vertices, \(98{,}280\) edges and **two** connected components of \(22{,}620\) vertices and \(49{,}140\) edges each. Its entire degree distribution consists of \(37{,}440\) vertices of degree four and \(7{,}800\) vertices of degree six. No five-coloring is frozen. The action of every even global color permutation preserves both components, while every odd global color permutation exchanges them.

The graph \(R_6(P)\) is connected; it has exactly \(4{,}502{,}160\) vertices and \(27{,}626{,}040\) edges. Moreover, \(R_k(P)\) is connected for **every** integer \(k\ge6\). Thus six is the exact mixing threshold of \(P\), in the standard single-vertex recoloring sense.

## Assumptions and scope

The vertices and all color labels are fixed. A recoloring changes exactly one coordinate while retaining properness at every intermediate step. The assertion is not about simultaneous Kempe switches, colorings up to global permutation, or Markov-chain rapid mixing. Connectivity is a property of the finite state graphs; no bound on the diameter of \(R_6(P)\) is asserted. The state enumeration and absence of a Grundy seven-coloring are fully finite assertions, not probabilistic tests.

## Proof

**1. Chromatic number and independent partitions.** The standalone `check_partitions.py` enumerates every nonempty independent subset of \(\mathbb Z/13\mathbb Z\) by testing all \(2^{13}-1\) subset masks. The maximum cardinality is three. Consequently four independent color classes cannot cover thirteen vertices, so \(\chi(P)\ge5\). One valid five-coloring, in vertex order \(0,1,\ldots,12\), is
\[
(0,1,0,1,2,3,2,0,1,4,3,2,3).
\]
Thus \(\chi(P)=5\).

Every proper five-coloring uses all five colors. To enumerate it without assuming its answer, choose the smallest uncovered vertex, choose *every* independent block containing that vertex and contained in the currently uncovered vertices, remove the block and recurse until exactly five nonempty blocks have been selected. Each unordered partition into five independent color classes appears exactly once: its first block is forced by the smallest remaining vertex and induction applies. The independent-block search finds precisely \(377\) partitions. Labeling the five blocks by all \(5!=120\) bijections gives \(377\cdot120=45{,}240\) distinct proper colorings. Their class-size multisets are \(\{2,2,3,3,3\}\) in \(37{,}440\) cases and \(\{1,3,3,3,3\}\) in \(7{,}800\) cases.

**2. Complete five-color reconfiguration graph.** For every enumerated coloring \(c\), every vertex \(v\) and every other palette value \(a\), the independent code tests whether any neighbor of \(v\) receives \(a\). Exactly when none does, it forms \(c'\) by setting \(c'(v)=a\), and links the two enumerated colorings. This procedure captures *all and only* allowed recolorings by definition. It obtains \(98{,}280\) undirected edges, verifies all targets belong to the independently enumerated set, and visits exactly two components by complete breadth-first traversal, each of size \(22{,}620\). Every coloring of class pattern \(\{2,2,3,3,3\}\) has four neighbors; every coloring of pattern \(\{1,3,3,3,3\}\) has six. The two components are isomorphic by any odd global color permutation and therefore have \(49{,}140\) edges each.

In detail, the global transposition \((0\ 1)\) maps *every* five-coloring to the other component, as checked directly from the component index for all \(45{,}240\) colorings. Every global permutation induces an automorphism of the recoloring graph, giving a homomorphism from \(S_5\) to the permutation group on its two components. Since a transposition exchanges the components and the unique nontrivial homomorphism \(S_5\to S_2\) is permutation sign, the stated parity rule follows.

**3. Six colors.** The separate C++ checker `check_recolor.cpp` uses depth-first recursive assignment of every proper palette-six coloring. At each step a new color is permitted exactly when absent from already colored neighbors. This is an exhaustive partition of all \(6^{13}\) assignments, with invalid prefixes pruned only after they have an equal-colored edge. Every resulting state receives a unique base-six integer encoding. For each state and each possible single-vertex recoloring, the checker looks up the resulting encoding, increments the corresponding degree, and unions the pair in a disjoint-set data structure. The exact results are \(4{,}502{,}160\) states and \(27{,}626{,}040\) undirected edges, with a single final union-find root. Thus \(R_6(P)\) is connected. The same C++ checker independently reproduces the complete five-color counts and component split.

**4. Every larger palette.** The maximum degree of \(P\) is six, so its Grundy number \(\Gamma(P)\), the maximum number of colors ever produced by first-fit greedy coloring in some vertex order, is at most seven. In any proper Grundy coloring using seven colors, select a vertex of color seven. Translation symmetry of the Paley graph sends it to vertex zero, whose six neighbors must receive **each** of the colors one through six, exactly once. The program `check_grundy.cpp` exhausts all \(6!\) permutations of those six colors on the neighbors, then recursively exhausts every proper choice from the seven colors on the remaining six vertices. Its final full-neighborhood test requires that every vertex of color \(j\) have a neighbor in *each* color \(1,\ldots,j-1\). None of the \(681{,}120\) complete proper candidate assignments satisfies these conditions. Hence \(\Gamma(P)\le6\).

Bonamy and Bousquet's mixing theorem (Theorem 1 in the referenced preprint) states that every finite graph is \(k\)-mixing for \(k\ge\Gamma(G)+1\). Therefore \(R_k(P)\) is connected for every \(k\ge7\). Together with Step 3 and the two-component obstruction of Step 2, this proves the exact threshold six. The appeal to the theorem is necessary: connectivity at one palette size alone does **not** imply monotonicity in the palette size for arbitrary graphs.

## Verification

Three complete standalone programs are included with their exact outputs. `check_partitions.py` independently enumerates five-colorings from independent-set partitions, builds the complete five-color recoloring graph, verifies component sizes, degrees and global permutation behavior. `check_recolor.cpp` uses a different vertex-by-vertex coloring enumerator and base-\(k\) integer states, with disjoint-set connectivity for both \(k=5\) and \(k=6\). `check_grundy.cpp` independently enumerates every possible Grundy seven-coloring after fixing the unique maximum-color vertex by translation. Outputs in `output_python.txt` and `output_cpp.txt` are from compilations/executions of these packaged source paths, not from unrelated runs. There are no randomized steps, unexpanded tables or unverified external certificates.

Reproduce from the containing directory using `python3 check_partitions.py`, then `c++ -O3 -std=c++17 check_recolor.cpp -o checker && ./checker 5 && ./checker 6`, and `c++ -O3 -std=c++17 check_grundy.cpp -o grundy_checker && ./grundy_checker`.

## Relationship to prior work

The Paley graph and its quadratic-residue description are classical. Standard tables already give its chromatic number five, which is not claimed as new. Cereceda, van den Heuvel and Johnson's work introduced and studied the single-vertex color graph, including nonmonotonic examples; it does not compute these two Paley state graphs. Bonamy and Bousquet's theorem supplies the final general-palette implication once the graph-specific Grundy upper bound is established, but neither that bound nor the exact palette-five and -six enumerations follows from their theorem alone. Brewster and Noel study general color-graph/homomorphism mixing, without these graph-specific statements. Existing published mathematical records on the Paley neighborhood complex concern a distinct homotopy invariant; they do not imply this coloring-state census or component split.

## Limitations

This is a finite computer-assisted theorem. The proof of the two component counts, the six-color connectivity and the Grundy upper bound depends on complete exhaustive checkers whose logic and full source are supplied, not on a short noncomputational structural classification. The theorem gives no exact diameter or mixing time for the connected palette-six graph, nor any threshold formula for Paley graphs of other orders. The published-literature comparison is limited to identified relevant sources; equivalent unindexed results remain possible. Independent external scientific audit has not been performed.

## References

1. M. Bonamy and N. Bousquet, *Recoloring graphs via tree decompositions*, arXiv:1403.6386v1, first posted 2014-03-25. Theorem 1, Grundy-number mixing bound. https://arxiv.org/abs/1403.6386
2. L. Cereceda, J. van den Heuvel, and M. Johnson, *Connectedness of the Graph of Vertex-Colourings*, CDAM Research Report LSE-CDAM-2005-11 (July 2005); later Discrete Mathematics 308 (2008), 913–919. https://matthewjohnsondurham.github.io/papers/cdam-2005-11.pdf
3. R. C. Brewster and J. A. Noel, *Mixing Homomorphisms, Recolourings, and Extending Circular Precolourings*, arXiv:1412.3493v1, first posted 2014-12-10. https://arxiv.org/abs/1412.3493
4. G. Exoo, *Chromatic Numbers of Small Paley Graphs*, published table of small Paley graph independence and chromatic numbers. https://cs.indstate.edu/ge/Paley/chromatic.html
