# A Desargues component inside the Desargues edge-Kempe graph

## Finding

Let \(D=\operatorname{GP}(10,3)\) denote the twenty-vertex Desargues graph. Form the reconfiguration graph \(\mathcal K(D)\) whose vertices are proper three-edge-colorings of \(D\) **modulo global permutations of the three colors**, with an edge when one coloring can be obtained from the other by exchanging two colors on a single connected bichromatic cycle. Then

\[
\boxed{\mathcal K(D)\cong D\;\sqcup\;6K_2.}
\]

Thus there are exactly \(32\) unordered one-factorizations, \(36\) reconfiguration edges, and seven connected components, with sizes \(20,2,2,2,2,2,2\). The nontrivial twenty-vertex component is itself a copy of the original Desargues graph, not just a cubic graph with the same distance distribution. Its distance profile from every vertex is \((1,3,6,6,3,1)\) and its diameter is five. The six other components are isolated edges.

There is an intrinsic coloring distinction: all three bichromatic two-factors split into two ten-cycles at the twenty vertices of the Desargues component; at each of the other twelve vertices precisely one bichromatic two-factor splits into two ten-cycles and the other two are Hamiltonian twenty-cycles.

## Assumptions and scope

The base graph has vertices \(u_i,v_i\) for \(0\leq i<10\), with indices reduced modulo ten, and edges
\[
u_iu_{i+1},\qquad u_iv_i,\qquad v_iv_{i+3}\quad(0\leq i<10).
\]
A proper three-edge-coloring assigns one color to each edge so that the three incident edges at every vertex have distinct colors. The reconfiguration states are *unlabeled color classes*: two colorings are the same state if one is obtained by permuting the color names globally. This is the color-permutation quotient, not the full named-color reconfiguration graph. A Kempe move exchanges two colors on exactly one connected cycle of their union, and yields an edge only when the resulting quotient state differs from the initial one. No graph-automorphism quotient is taken: the twenty original vertices remain labeled.

## Proof

**1. Exhaustive matching decomposition.** Every color class is a perfect matching because the base graph is cubic. The program `verify_factorizations.py` recursively lists *all* perfect matchings: for the least unmatched vertex, it branches over each of its neighbors not yet matched and removes those two vertices. Each perfect matching is generated on precisely one branch by induction on the unmatched-vertex set; duplicates are removed only after exhaustive generation. The program obtains exactly \(60\) matchings. Deleting any one matching leaves a spanning two-regular graph. Its cycle-length type is \((10,10)\) for exactly \(36\) matchings and \((20)\) for exactly \(24\) matchings.

Each even cycle has exactly two ways to split its edges alternately into the other two perfect matchings. If the complementary two-factor has \(c\) cycles, it has \(2^{c-1}\) unordered two-color splits. Each unordered three-matching factorization is counted from each of its three constituent matchings. Therefore the exact number of quotient colorings is
\[
\frac{36\cdot2+24\cdot1}{3}=32.
\]
This argument gives an independent combinatorial count rather than relying only on the enumerator's final length.

**2. Exact switch adjacency.** For each of the \(32\) resulting color partitions, the same program examines every pair of color classes, traverses all connected components in their union, and toggles the two color masks on the edges of each component. Because the graph is three-regular and properly colored, each such component is necessarily an even cycle and the process enumerates every possible elementary Kempe move. The outputs are canonically sorted as unordered color-class triples; self-moves and duplicate undirected edges are discarded. There are exactly \(36\) distinct edges. Twenty states have three neighbors and bichromatic cycle profile \(((10,10),(10,10),(10,10))\); twelve states have one neighbor and profile \(((10,10),(20),(20))\). Exhaustive connected-component traversal gives one twenty-state component and six two-state components.

**3. An explicit isomorphism witness.** The complete list of the \(32\) canonical colorings and the \(36\) adjacency pairs is in `certificate.json`, together with an explicit bijection from the twenty states in its large component to the integers \(0,\ldots,19\). The programs check, for *every* unordered pair in that component, that it is adjacent if and only if its images are joined by an edge \(u_iu_{i+1}\), \(u_iv_i\), or \(v_iv_{i+3}\) in the graph defined above. Thus the map is a genuine graph isomorphism, not an inference from degree sequence or local distances. The remaining twelve vertices pair into six edges, proving the displayed decomposition.

**4. Independent enumeration.** The separate program `verify_direct_colors.py` never constructs perfect matchings. Instead it assigns colors edge by edge, forbidding any repetition at either endpoint. The three edges at one fixed vertex receive colors in fixed order, which selects exactly one representative of each global color-permutation orbit. Most-constrained-edge backtracking exhausts every possible proper coloring consistent with those fixed colors. Its \(32\) states coincide with all certified states. It computes the bichromatic components directly by breadth-first search in the two-color edge-induced graph, obtains the same \(36\) switch edges, verifies the supplied isomorphism, and independently calculates the distance profile \((1,3,6,6,3,1)\).

## Verification

Run in a directory containing the packaged files, using Python 3 and only its standard library:

```sh
python3 verify_factorizations.py
python3 verify_direct_colors.py
```

Their complete expected output lines are recorded in `factorization_output.txt` and `direct_output.txt`. Both check the entire `certificate.json` and print its SHA-256, `d34d0c2b0fe953fa127ef17e6bfe64d7350aae19b36bad29f0d48f937ed44f6c`. The certificate contains all vertices, all links, and the explicit isomorphism mapping; it is not merely a sample. See `VERIFICATION.md` for the finite-exhaustiveness argument and limits.

## Relationship to prior work

Belcastro and Haas (2012/2014) established the edge-Kempe-equivalence framework and supplied general component-count theorems, with explicit prism and Möbius-ladder families. Their article does not identify the full color-quotient reconfiguration graph of the Desargues graph. Their 2017 article studies the graph structures themselves, distinguishing named colors from colors fixed at a vertex, and gives a complete description for crossed prisms. It does not give the present Desargues graph decomposition; notably, the twenty-vertex crossed prism is not isomorphic to \(\operatorname{GP}(10,3)\). Goedgebeur and Östergård (2021/2022) enumerate Kempe-equivalence component counts across cubic graphs, including bipartite graphs of this order, but their presented tables and algorithm do not state the decomposition \(D\sqcup6K_2\) or the explicit self-isomorphism. Existing component-count calculations are credited, not represented as the new mathematical content. The assessed contribution is the **complete, structurally identified reconfiguration graph** of this canonical example.

## Limitations

The assertion concerns one specified finite graph and the color-permutation quotient under one-cycle switches. It does not imply the same decomposition for other generalized Petersen graphs or for named-color edge-Kempe graphs. Its exactness rests on two exhaustively replayable finite computations and an explicit finite witness, not a uniform symbolic theorem for an infinite family. Neither an absence of indexed search results nor these computations establishes historical publication priority. Unindexed equivalent results or implicit information in previously distributed datasets remain possible. No independent external audit has been conducted.

## References

- S.-M. Belcastro and R. Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs*, arXiv:1209.1730, first submitted 2012-09-08; *Discrete Mathematics* 325 (2014), 77–84. https://arxiv.org/abs/1209.1730
- S.-M. Belcastro and R. Haas, *Edge-Kempe-equivalence graphs of class-1 regular graphs*, *Australasian Journal of Combinatorics* 69(2) (2017), 197–214. https://ajc.maths.uq.edu.au/pdf/69/ajc_v69_p197.pdf
- J. Goedgebeur and P. R. J. Östergård, *Switching 3-edge-colorings of cubic graphs*, arXiv:2105.01363 (2021); *Discrete Mathematics* 345 (2022), article 112963. https://arxiv.org/abs/2105.01363
- The Desargues graph is the generalized Petersen graph \(\operatorname{GP}(10,3)\); this classical identification is also documented in E. W. Weisstein, *Desargues Graph*, MathWorld. https://mathworld.wolfram.com/DesarguesGraph.html
