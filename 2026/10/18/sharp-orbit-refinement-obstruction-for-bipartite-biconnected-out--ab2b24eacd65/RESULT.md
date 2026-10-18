# Sharp orbit-refinement obstruction for bipartite biconnected outerplanar graphs

## Finding

For finite simple biconnected bipartite outerplanar graphs, started from the uniform vertex colour, ordinary one-dimensional counting colour refinement (1-WL) is orbit-exact on every graph of fewer than twelve vertices. At twelve vertices there is, up to graph isomorphism, exactly one exception: the cycle \(C_{12}\), with vertices \(0,1,\ldots,11\) in cyclic order, and the additional edges \(\{0,3\}\) and \(\{6,9\}\). Among the \(48\) isomorphism types of twelve-vertex bipartite biconnected outerplanar graphs, it is the sole failure. Its two stable cells have cardinalities \(4\) and \(8\), whereas its automorphism orbits have sizes \(4,4,4\).

Moreover the obstruction extends to an infinite family. For every odd integer \(\ell=2h+1\ge3\), let \(B_\ell\) be the cycle \(C_{4\ell}\) with additional edges \(\{0,\ell\}\) and \(\{2\ell,3\ell\}\), with indices interpreted modulo \(4\ell\). This graph is bipartite, biconnected and outerplanar. Uniform-start counting refinement stabilizes in exactly \(h\) strict rounds with \(h+1\) colour classes, while its automorphism group has \(2h+1\) vertex orbits. The difference in numbers of orbit and colour classes is \(h\), and is unbounded.

## Assumptions and scope

Graphs are finite, undirected and simple. Biconnected means 2-vertex-connected with at least three vertices. Bipartiteness is ordinary proper 2-colourability. Outerplanarity means an embedding exists with every vertex incident to the outer face. In one-dimensional counting colour refinement, every vertex initially has the same colour and at each step its new colour consists of its previous colour together with the *multiset* of previous colours of its neighbours, canonically re-encoded. A stable colour partition is **orbit-exact** if its classes are precisely the orbits of the full graph automorphism group.

The first-public-date of the background dissection-enumeration source is \(2005\)-\(11\)-\(16\); this is not a publication or priority date of the present finding. No claim is made that the already known enumerative sequence of bipartite outerplanar isomorphism classes is new.

## Proof

**1. Canonical outer cycle and exhaustive representation.** Every simple biconnected outerplanar graph on at least three vertices has a unique Hamiltonian cycle, namely the outer facial boundary in an outerplanar embedding. This standard fact is used in Bodirsky–Fusy–Kang–Vigerske, §3.1 [1]. Thus each graph of order \(n\) can be represented by a labeled \(n\)-cycle together with a family of pairwise noncrossing diagonals, with no duplication of perimeter edges. Every such family conversely yields a biconnected outerplanar graph. If the graph is bipartite then \(n\) is even and all diagonals must connect odd-separated polygon indices; conversely those restrictions give a bipartite graph. Every graph isomorphism preserves the unique Hamiltonian cycle, hence acts on polygon indices by a rotation or reflection. Therefore *exactly* the dihedral orbits of noncrossing, odd-separated diagonal sets enumerate graph isomorphism classes.

An additional finite bound follows from planar face lengths. With \(c\) diagonals there are \(c+1\) bounded faces. Each bounded face has at least four sides because the graph is bipartite. Consequently \(2(n+c)\ge n+4(c+1)\), which implies \(c\le n/2-2\). This upper bound is also used by the independent combination-based verification.

**2. Complete finite classification.** The standalone program `verify_2conn_bipartite_outerplanar.py` recursively includes or excludes every legal diagonal while excluding exactly pairs with alternating endpoints, canonicalizes each noncrossing set under all \(2n\) dihedral maps, computes stable counting colours, and computes automorphism orbits by the subset of dihedral maps preserving the diagonal set. Its output is reproduced in `primary_output.txt`.

The independently implemented `verify_independent.py` instead enumerates all diagonal combinations to the proved face bound, rejects crossings, deduplicates via full `networkx` graph isomorphism, and computes automorphism orbits by complete self-isomorphism enumeration; its output is `independent_output.txt`. Both methods agree as follows, with order \(n\), number of labeled noncrossing diagonal sets, number of isomorphism types, and count of orbit-refinement failures:

\[
\begin{array}{c|rrrrr}
n&4&6&8&10&12\\ \hline
\text{labeled}&1&4&21&126&818\\
\text{isomorphism types}&1&2&4&13&48\\
\text{failures}&0&0&0&0&1
\end{array}
\]

The canonical exceptional diagonal set is exactly \(\{\{0,3\},\{6,9\}\}\). Its four chord endpoints form a size-four colour class (degree \(3\)); its other eight vertices form a size-eight colour class (degree \(2\)). Each degree-three vertex has exactly one degree-three and two degree-two neighbours. Each degree-two vertex has one neighbour of each degree, so this partition is equitable and stable after one strict round. Its full automorphism group has order four, and its orbits are
\[
\{0,3,6,9\},\quad \{1,2,7,8\},\quad \{4,5,10,11\}.
\]
This gives the unique twelve-vertex failure. Bipartite 2-connected graphs have at least four vertices and even order, so the five even orders checked suffice for the sharp lower bound.

**3. Infinite family: stable colours.** Fix odd \(\ell=2h+1\ge3\). The four chord endpoints \(H=\{0,\ell,2\ell,3\ell\}\) have degree three. Their four intervening cycle arcs all have length \(\ell\); exactly two opposite arcs have chords joining their endpoints. For \(1\le t\le h\), let \(L_t\) be the eight non-hub vertices at cycle-arc distance \(t\) from the nearer endpoint of their arc. The partition \(\{H,L_1,\ldots,L_h\}\) is equitable: every hub has one hub neighbour and two \(L_1\) neighbours; the shell \(L_1\) has one hub and one \(L_2\) neighbour when \(h>1\), or one hub and one \(L_1\) neighbour when \(h=1\); intermediate shells \(L_t\) each have one neighbour in each adjacent shell; and vertices of \(L_h\) have one neighbour in \(L_{h-1}\) and one in \(L_h\) for \(h>1\). Therefore colour refinement cannot split a shell, while it does separate the degree-three hubs in round one. Because the graph distance from a vertex in \(L_t\) to the degree-three set \(H\) is exactly \(t\), counting refinement separates successive shells one round at a time. More explicitly, at round \(r\) the stable initial hub class and each of \(L_1,\ldots,L_{r-1}\) are separated, and all remaining shells are unresolved (when \(r\le h\)); in round \(h\) all \(h+1\) cells are distinguished. For \(h=1\) these statements give the directly checked first-round partition. Thus the strict refinement depth is exactly \(h\).

**4. Infinite family: full automorphism orbits.** Every automorphism preserves the uniquely embedded boundary cycle and the two chords. On the cyclically ordered four hubs, the chord matching is \(\{\{0,\ell\},\{2\ell,3\ell\}\}\). Its dihedral stabilizer consists of four symmetries, generated by rotation through \(2\ell\) and reflection \(i\mapsto\ell-i\) modulo \(4\ell\). These maps act transitively on \(H\), and for each \(t\) act with exactly two size-four orbits on \(L_t\): vertices belonging to the two **chord-shortened** boundary arcs and vertices belonging to the two **unshortened** boundary arcs. No automorphism exchanges these types, because the additional chord joining an arc's endpoints is an isomorphism invariant. Thus there are exactly \(1+2h\) orbits, versus \(1+h\) stable colours. The cardinality of their difference is \(h\). This proves the infinite family assertion.

## Verification

To reproduce the complete finite census, run `python verify_2conn_bipartite_outerplanar.py` and `python verify_independent.py` (the latter requires NetworkX). Both independently yield five lines with isomorphism counts \(1,2,4,13,48\), failure counts \(0,0,0,0,1\), and the same exceptional chords. For the infinite family, run `python verify_family.py` alongside the first program. The family checker tests every odd length from \(3\) to \(81\), i.e. forty representatives, comparing refinement depth, colour and orbit counts, full dihedral automorphisms, and class sizes; outputs in `family_output.txt`. Finite experiments are checks of the all-order proof, not substitutes for that proof. The enumerations are exhaustive **only up to order twelve**, as established by the canonical polygon representation and complete search.

## Relationship to prior work

Bodirsky, Fusy, Kang and Vigerske [1] establish the outerplanar dissection representation and count bipartite two-connected outerplanar graph types. The sequence \(1,2,4,13,48\) is recorded as OEIS A111757 [3]; it is used here as an existing consistency check, not asserted as new. Their inspected full paper, including §3.1 on unique outer cycles and §3.4 on bipartite outerplanar enumeration, does not classify counting-colour-refinement versus automorphism orbits in these graphs.

Arvind, Köbler, Rattan and Verbitsky [2] develop general relations among color refinement, automorphism orbits, amenability and refinability; the inspected full text gives a conceptual framework rather than this exact bipartite outerplanar cutoff and chord-pair obstruction family. An earlier structural or computational classification could exist despite the searches undertaken; this has not received independent priority evaluation. General algorithms that can compute colours or automorphisms on input graphs are not automatically an enumerative theorem at the claimed sharp cutoff.

## Limitations

The sharp uniqueness claim is exhaustive only for orders at most twelve, and assumes biconnectivity, bipartiteness and uniform initial colouring. For larger orders, the infinite family produces obstructions but no complete classification is asserted. The family theorem concerns counting colour refinement's *orbit partition* and its stabilization rounds, not graph identification among all graphs nor a classification of arbitrary individualizations. The verification runs are reproducible computational evidence, with the universal infinite-family conclusion resting on the mathematical proof. The novelty comparison cannot exclude an inaccessible specialized earlier result, and independent scientific validation has not been performed.

## References

[1] M. Bodirsky, É. Fusy, M. Kang and S. Vigerske, *Enumeration of Unlabeled Outerplanar Graphs*, arXiv:math/0511422 (first submitted 2005-11-16), §3.1 and §3.4, https://arxiv.org/abs/math/0511422.

[2] V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (first submitted 2015-02-04), https://arxiv.org/abs/1502.01255; full report at https://eccc.weizmann.ac.il/report/2015/032/.

[3] OEIS A111757, *Number of bipartite 2-connected outerplanar graphs on \(2n\) unlabeled nodes*, https://oeis.org/A111757.
