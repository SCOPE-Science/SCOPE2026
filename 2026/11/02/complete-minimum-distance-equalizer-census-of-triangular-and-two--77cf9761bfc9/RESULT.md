# Complete minimum distance-equalizer census of triangular and two-subset Kneser graphs

## Finding

Let \(J(n,2)=L(K_n)\) be the triangular graph with vertices the two-element subsets of \([n]\), adjacent when they intersect. For \(n\ge5\) also let \(KG(n,2)\) be the Kneser graph on these same vertices, adjacent when they are disjoint. A *distance-equalizer* is a vertex set \(S\) such that any two distinct vertices outside \(S\) have equal distances from some member of \(S\). A *basis* means a distance-equalizer of minimum cardinality, not an inclusion-minimal set.

The entire basis classification is as follows. Identify a selected graph-vertex set with a three-edge (or, for \(n=4\), two-edge) subgraph of the root complete graph.

| Root order | Basis cardinality | Exactly the permitted root-edge configurations | Labeled basis count |
| --- | --- | --- | --- |
| \(n=4\) | \(2\) | One perfect matching of \(K_4\) | \(3\) |
| \(n=5\) | \(3\) | One triangle, or \(P_3\sqcup K_2\) | \(\binom53+30=40\) |
| \(n=6\) | \(3\) | One triangle, or a perfect matching of \(K_6\) | \(\binom63+15=35\) |
| \(n\ge7\) | \(3\) | One triangle only | \(\binom n3\) |

For \(n\ge5\) this table applies, with exactly the same selected vertex subsets, to **both** \(J(n,2)\) and \(KG(n,2)\). In fact their full families of distance-equalizer sets, not just their bases, coincide. In particular, triangular configurations become the unique basis type starting at \(n=7\), while orders five and six have distinct exceptional types.

## Assumptions and scope

All graphs are finite simple graphs with standard unweighted shortest-path distance. The triangular graph is considered for each integer \(n\ge4\). The Kneser graph is considered for each integer \(n\ge5\), when it is connected of diameter two. The two-element subsets are **labeled**; counts refer to distinct unordered chosen sets of graph vertices, not to ordered landmark sequences or root-graph isomorphism classes. A displayed pair \((i,j)\) denotes the graph vertex corresponding to the unordered root edge with endpoints \(i,j\); indices start at zero in canonical representatives.

## Proof

**Signature reduction.** Fix a selected set \(S\) of root edges. For every unselected root edge \(e\), define its incidence word \(\sigma_S(e)\in\{0,1\}^{|S|}\), with the bit indexed by \(s\in S\) equal to one exactly when \(e\cap s\ne\varnothing\). Since any two distinct vertices of the triangular graph have distance one if their root edges meet and two otherwise, \(d_{J(n,2)}(e,s)=2-\sigma_S(e)_s\) for \(e\notin S\). Therefore \(S\) is a distance-equalizer if and only if **no two unselected edges have bitwise complementary incidence words**: two distinct words differ in every position precisely when they are complementary. This equivalence includes repeated words, which are harmless.

For \(n\ge5\), the Kneser graph has diameter two. Distinct root edges that are disjoint are adjacent, and if they intersect a common disjoint root edge exists because at least two root vertices lie outside their union of at most three vertices. Consequently \(d_{KG(n,2)}(e,s)=1+\sigma_S(e)_s=3-d_{J(n,2)}(e,s)\) for each unselected \(e\) and each selected \(s\). Equality of the two distances to a fixed landmark is thus equivalent in both graphs. This proves the full-family coincidence asserted above.

**Minimum cardinality.** At \(n=4\), a selected pair of disjoint root edges, say \(S=\{(0,1),(2,3)\}\), gives every unselected edge the incidence word \((1,1)\), hence is an equalizer. A pair of adjacent edges, say \(\{(0,1),(0,2)\}\), fails: \((1,3)\) and \((2,3)\) have opposite incidence words. A singleton cannot be an equalizer either, because the property is upward closed under enlarging \(S\) and no adjacent-edge pair works. Thus the bases for \(n=4\) are precisely the three perfect matchings.

At \(n\ge5\), any two selected edges are either adjacent or disjoint. An adjacent pair \(S=\{(0,1),(0,2)\}\) is invalid for the same unselected pair \((1,3),(2,3)\) as above. A disjoint pair \(S=\{(0,1),(2,3)\}\) is invalid for the unselected pair \((0,4),(2,4)\), which has complementary incidence words. By upward closure a singleton also fails. On the other hand, any three edges forming a triangle, say \(\{(0,1),(0,2),(1,2)\}\), give every unselected edge an incidence word of Hamming weight zero or two. Such words have no complements among themselves. Thus the minimum cardinality equals three for every \(n\ge5\).

**All three-edge types.** Up to relabeling and isolated root vertices, a simple graph with three edges has exactly five forms: a triangle, a three-edge star, a four-vertex path, \(P_3\sqcup K_2\), or \(3K_2\). The triangle works for all orders where it exists. The following explicit choices rule out the other shapes whenever enough root vertices exist. Each row lists a canonical chosen set \(S\) and two unselected root edges \(x,y\) whose incidence words are complementary; in particular, no selected edge is equidistant from \(x,y\).

| Shape | Chosen edges \(S\) | Forbidden unselected pair \(x,y\) | Valid obstruction range |
| --- | --- | --- | --- |
| Three-edge star | \(\{(0,1),(0,2),(0,3)\}\) | \((1,2),(3,4)\) | \(n\ge5\) |
| Four-vertex path | \(\{(0,1),(1,2),(2,3)\}\) | \((0,4),(2,4)\) | \(n\ge5\) |
| \(P_3\sqcup K_2\) | \(\{(0,1),(0,2),(3,4)\}\) | \((0,5),(3,5)\) | \(n\ge6\) |
| \(3K_2\) | \(\{(0,1),(2,3),(4,5)\}\) | \((0,2),(4,6)\) | \(n\ge7\) |

The exceptional smaller orders really admit the listed additional shapes. For \(n=5\), the unselected incidence words for \(S=\{(0,1),(0,2),(3,4)\}\) are, as a set, \(\{110,111,101,011\}\). None is the bitwise complement of another. For \(n=6\), if \(S\) is a perfect matching of the six root vertices, each unselected root edge joins two distinct matching edges. It therefore meets exactly two members of \(S\), so every unselected incidence word has weight two and no complementary pair occurs. This exhausts all five three-edge graph types and proves the asserted basis classification and all thresholds.

**Enumeration.** The root graph contains exactly \(\binom n3\) triangles. At \(n=5\), a \(P_3\sqcup K_2\) is uniquely chosen by its center (five choices) and its two leaves (\(\binom42\) choices), contributing thirty extra bases. At \(n=6\), there are \(6!/(2^3 3!)=15\) perfect matchings. The three perfect matchings of \(K_4\) give the remaining count. All constructions are distinct because the root-edge shapes are distinct or their labeled edge sets differ. \(\square\)

## Verification

The included `verify_equalizer.py` rebuilds the Johnson and Kneser graphs directly from their adjacency definitions, uses breadth-first search to compute shortest-path distances, and tests the original distance-equalizer condition for **every** two- and three-vertex candidate in the ranges specified below. For the triangular graph it checks every order \(4\le n\le10\); for the Kneser graph it checks every order \(5\le n\le10\). All \(57{,}753\) tested candidate subsets across these thirteen graph instances agree with the complete structural predictions. Run `python3 verify_equalizer.py` with Python 3; only the standard library is needed. The infinite ranges follow from the preceding signature proof, not from the finite census.

## Relationship to prior work

González, Hernando, and Mora introduced distance-equalizer sets, and studied Johnson graphs, in the public 2021 preprint subsequently appearing in 2022. Kratica, Čangalović, and Kovačević-Vujčić proved the **scalar** values \(\operatorname{eqdim}(J(n,2))=3\) (for \(n\ge5\), with the \(n=4\) exception) and \(\operatorname{eqdim}(KG(n,2))=3\) in their 2024 preprint, displaying a triangle construction. Their results establish the required minimum sizes but do not enumerate all labeled minimizers or classify the nontriangle exceptional families. The contribution here is the complete basis classification, exact multiplicities at every order, and the eventual triangle-only rigidity simultaneously for both complementary diameter-two graphs; the scalar dimension identities are not presented as new.

## Limitations

The theorem classifies **minimum-cardinality** equalizer sets, not all inclusion-minimal or all larger sets. It applies only to two-subset Johnson and Kneser graphs; it makes no claim about higher-subset Johnson graphs. No exhaustive guarantee of publication priority is possible: results using another name for minimum equalizer configurations might exist. The finite checker only establishes the stated finite comparisons; it is not an independent certificate of the universal theorem.

## References

1. A. González, C. Hernando, M. Mora, *The Equidistant Dimension of Graphs*, arXiv:2107.10805 (first publicly posted 2021-07-22); *Bull. Malays. Math. Sci. Soc.* 45 (2022), 1757–1775, DOI:10.1007/s40840-022-01295-z.
2. J. Kratica, M. Čangalović, V. Kovačević-Vujčić, *Equidistant dimension of Johnson and Kneser graphs*, arXiv:2406.17870 (first publicly posted 2024-06-25); in particular the full accessible preprint's §§2.2, 2.5, and 2.6.
