# Three four-round theories of diameter-two Moore graphs

## Finding

Let \(\mathcal M\) be the class of finite, simple, undirected Moore graphs of diameter two and degree \(d\ge2\): these are \(d\)-regular graphs attaining the order \(d^2+1\). Interpret them in ordinary first-order logic with equality and the undirected adjacency relation, without counting or named vertices. Write \(G\equiv_4 H\) for agreement on every sentence of quantifier rank at most four.

**Theorem.** For any \(G,H\in\mathcal M\), of degrees \(d,e\), respectively,
\[
G\equiv_4 H\quad\Longleftrightarrow\quad \min(d,4)=\min(e,4).
\]
There are exactly three nonempty rank-four classes: the five-cycle \(C_5\), the Petersen graph, and a class represented by the fifty-vertex Hoffman–Singleton graph. The last class contains **every possible** degree-fifty-seven Moore graph, should any exist. Every member is rank-four equivalent to a member of \(\mathcal M\) on at most fifty vertices; this is the sharp uniform bound among representatives within \(\mathcal M\).

More generally, the equivalence of all degrees \(d\ge4\) follows solely from the local parameters \((d^2+1,d,0,1)\), and does not use the classification of possible degrees. The Hoffman–Singleton theorem is used only to identify the three realized classes and the optimal representative size.

## Assumptions and scope

All graphs are nonempty, finite, simple, undirected, loopless, of diameter exactly two, and attain the Moore bound for their degree. Their parameters satisfy \(v=d^2+1\), regular valency \(d\), no triangles, and a **unique** common neighbor for each pair of distinct nonadjacent vertices. These implications are elementary: equality in the degree-diameter bound forces no triangles, no four-cycles, and every nonadjacent pair to have distance exactly two. Conversely, such a strongly regular graph attains the bound.

The language contains only equality and adjacency. Quantifier rank counts nested quantifiers (not total quantifiers, nor counting quantifiers). The possibility of a degree-fifty-seven Moore graph is not asserted.

## Proof

### One-point extension cells over triples

For three *distinct* selected vertices \(x,y,z\), partition all unselected vertices by the subset of \(\{x,y,z\}\) to which they are adjacent. Any selected triple is either an induced path of length two, a single edge plus an isolated vertex, or independent; an independent triple is **concurrent** when its three vertices have a common neighbor, and **separate** otherwise. The absence of triangles and four-cycles shows that three pairwise nonadjacent selected vertices have either one common center for all three pairs or three distinct centers. There are no other triple types.

The exact extension-cell counts are as follows. For a single-edge triple, order \(x,y,z\) so that \(xy\) is the edge; for a path, let \(y\) be the middle vertex. A “single” cell is adjacent to precisely the indicated selected vertex; a “pair” cell is adjacent to precisely the indicated pair.

| Triple type | Adjacent to none | Singles \((x,y,z)\) | Pairs \((xy,xz,yz)\) | All three |
| --- | --- | --- | --- | --- |
| Path \(x-y-z\) | \((d-1)(d-2)\) | \((d-1,d-2,d-1)\) | \((0,0,0)\) | \(0\) |
| Edge \(xy\), isolated \(z\) | \((d-1)(d-2)\) | \((d-2,d-2,d-2)\) | \((0,1,1)\) | \(0\) |
| Independent, concurrent | \(d(d-3)\) | \((d-1,d-1,d-1)\) | \((0,0,0)\) | \(1\) |
| Independent, separate | \(d^2-3d+1\) | \((d-2,d-2,d-2)\) | \((1,1,1)\) | \(0\) |

For example, in the concurrent independent case the three degree-\(d\) neighborhoods have exactly one common vertex and no other pairwise intersections. Their union therefore has size \(3d-2\); the three selected vertices are outside that union. Subtracting this union and the selected vertices from \(d^2+1\) gives \(d(d-3)\) vertices adjacent to none. Each single cell has \(d-1\) vertices. For a separate independent triple there are three distinct pair centers; inclusion–exclusion gives \(d^2-3d+1\) vertices adjacent to none. The analogous neighborhood accounting, removing the two or three selected neighbors where applicable, gives the two remaining rows. These are integer identities, not probabilistic estimates.

For every \(d\ge4\), all listed nonzero cell counts are **strictly positive**, and all zero counts are identically zero. Consequently the complete fourth-vertex extension *support* depends only on the labelled triple type, never on \(d\). In contrast, at \(d=3\) the “adjacent to none” cell for a concurrent independent triple has size zero.

### Matching triples from any selected pair

The previous table is useful only if the corresponding triple types can be matched in the earlier rounds. Fix two distinct selected vertices. If they are adjacent, an unselected vertex adjacent only to the first (respectively second) exists in \(d-1\) ways, while a vertex adjacent to neither exists in \((d-1)^2\) ways; there is no vertex adjacent to both. If they are nonadjacent, the unique common neighbor exists, each single-adjacency cell contains \(d-1\) vertices, and their neither-adjacency cell has \(d(d-2)\) vertices.

In the latter cell, let \(c\) be the unique common neighbor of the selected pair. Exactly \(d-2\) possibilities are additional neighbors of \(c\), producing concurrent independent triples. The other \((d-1)(d-2)\) possibilities produce separate independent triples. All these required possibilities are present for every \(d\ge3\). Repeated selections are matched by equality. From one selected vertex, both a neighbor and a distinct nonneighbor exist for every \(d\ge2\).

### Four-round strategy

For two graphs of degrees at least four, Duplicator responds to the first two selections by preserving equality and adjacency. At the third selection, the previous paragraph guarantees a reply that preserves the labelled triple type, including the concurrent/separate distinction when all three vertices are independent. At the fourth selection, the support table guarantees a vertex realizing the same equality and adjacency pattern relative to the selected triple. These arguments work regardless of which graph Spoiler chooses on each turn. Hence all degree-at-least-four Moore graphs are \(\equiv_4\).

### Exact lower-degree separation

The graph \(C_5\) has no independent set of size three, whereas the Petersen graph and every degree-at-least-four Moore graph do: three distinct neighbors of any vertex are independent because triangles are absent. The existential sentence asserting three distinct pairwise nonadjacent vertices (rank three) therefore separates the degree-two class.

For the next boundary, consider the rank-four sentence asserting the existence of three distinct pairwise nonadjacent vertices \(x,y,z\) satisfying **both** of the following clauses: (i) some fourth vertex is adjacent to all three; and (ii) every vertex is either one of \(x,y,z\) or adjacent to at least one of them. This sentence has rank four because the existential quantifier in (i) and the universal quantifier in (ii) occur in separate conjuncts, after the three outer existential quantifiers.

In the Petersen graph, the three neighbors of any vertex are a concurrent independent triple. Their common-neighbor cell has size one and their no-neighbor cell has size \(3(3-3)=0\); they dominate the remaining vertices, so the sentence is true. In every degree-at-least-four Moore graph, any concurrent independent triple has \(d(d-3)>0\) unselected vertices adjacent to none. Thus clause (ii) fails whenever clause (i) holds, and the sentence is false. Hence degree three is a distinct four-round class.

Hoffman and Singleton established that the possible degrees are \(2,3,7,57\), with unique graphs at degrees two, three, seven and the last case unresolved. The three known graphs therefore witness three nonempty classes. The degree-seven member has fifty vertices, and there is no Moore graph of degree four, five or six that could provide a smaller representative of its rank-four class. This proves the sharp fifty-vertex bound **within this family**.

## Verification

Run `python3 moore_verify.py` for exact adjacency constructions of \(C_5\), the Petersen graph and the Hoffman–Singleton graph. The program checks the full strongly regular conditions \((d^2+1,d,0,1)\), enumerates all unordered triples and their actual fourth-vertex extension supports, and computes their complete rank-four first-order types using exhaustive recursive ordered-tuple extensions, including repeated vertices. Its final line is `FINITE_EXACT_TYPES_AND_TRIPLE_SUPPORTS_OK`.

Run `python3 support_formula.py` to independently check the symbolic extension-cell arithmetic for degrees \(3,4,7,57\), including the crucial zero at degree three and strict positivity beginning at degree four. Its final line is `SYMBOLIC_EXTENSION_ARITHMETIC_OK`. The two recorded runs are included as text artifacts. The hypothetical degree-fifty-seven graph is **not** enumerated or assumed to exist; only the parameter-conditional algebra is checked for that value. The proof above, rather than finite extrapolation, covers every such graph if one exists.

## Relationship to prior work

Hoffman and Singleton (1960) prove the Moore degree restriction and uniqueness of the three known diameter-two examples using spectral and block-matrix arguments. Their article does not state a bounded-rank first-order classification. Reichard (2014) develops the graph-theoretic \(t\)-vertex condition and its equivalence to strong regularity at \(t=3\), but its inspected definitions and main results concern uniform induced-subgraph counts, not cross-graph four-round equivalence. Pikhurko and Verbitsky (2011) explain graph first-order quantifier depth and Ehrenfeucht games in general; the inspected game sections do not give this Moore-graph threshold. The present argument converts exact three-point *extension support*, rather than multiplicities or the spectrum, into an infinite four-round equivalence and proves a sharp two-step lower-degree separation.

## Limitations

This theorem applies only to the pure adjacency-and-equality language and to quantifier rank at most four. It neither resolves the existence of a degree-fifty-seven Moore graph nor claims anything about its higher-rank theory, isomorphism, or automorphisms. The optimal representative bound is within the Moore family, not among all finite graphs. The available source comparison is not a proof of absolute historical priority; an equivalent observation in less searchable literature remains possible. Independent mathematical audit has not been performed.

## References

1. A. J. Hoffman and R. R. Singleton, “On Moore Graphs with Diameters 2 and 3,” *IBM Journal of Research and Development* 4 (1960), 497–504. DOI `10.1147/rd.45.0497`. Public full text: `https://people.orie.cornell.edu/dpw/orie6334/HoffmanS60.pdf`.
2. Sven Reichard, “Strongly Regular Graphs With The 7-Vertex Condition,” arXiv:`1401.6816` (first public version January 27, 2014). `https://arxiv.org/pdf/1401.6816`.
3. Oleg Pikhurko and Oleg Verbitsky, “Logical complexity of graphs: a survey,” *Contemporary Mathematics* 558 (2011), 129–180. `https://opikhurko.warwick.ac.uk/E/PikhurkoVerbitsky11cm.pdf`.
