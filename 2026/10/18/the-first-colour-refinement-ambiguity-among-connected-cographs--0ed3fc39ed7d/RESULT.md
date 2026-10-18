# The first colour-refinement ambiguity among connected cographs

## Finding

For each integer \(1\le n\le11\), ordinary colour refinement distinguishes every pair of nonisomorphic connected cographs on \(n\) vertices. On \(12\) vertices, the \(21{,}965\) connected cograph isomorphism classes have exactly **three** indistinguishable unordered pairs; every other colour-refinement equivalence class is a singleton. The three pairs are regular, with degrees \(7\), \(8\), and \(9\), respectively, and have \(42\), \(48\), and \(54\) edges.

The graph pairs are explicitly given using the following notation: \(\overline G\) is the simple complement of \(G\); \(G\sqcup H\) is disjoint union; \(G\vee H\) is the graph join; \(E_k\) is the edgeless graph on \(k\) vertices; \(mG\) denotes \(m\) disjoint copies; and \(K_{a_1,\ldots,a_t}\) is complete multipartite with the specified part sizes.

* Degree \(7\): \(\overline{K_5\sqcup(E_3\vee(2K_2))}\) and \(\overline{2K_{2,2,2}}\).
* Degree \(8\): \(\overline{3K_4}\) and \(\overline{2K_{3,3}}\).
* Degree \(9\): \(\overline{4K_3}\) and \(\overline{3K_{2,2}}\).

In these three cases, the component-size multisets of the complementary graphs differ, proving nonisomorphism. Each original graph is connected and \(P_4\)-free. Both members of each pair are regular with the stated common degree, and hence colour refinement cannot distinguish them.

## Assumptions and scope

All graphs here are finite, simple, undirected, uncoloured and **connected**. A cograph is a graph with no induced four-vertex path \(P_4\); equivalently, it is constructible from single vertices by disjoint union and join. The comparison procedure begins with a single uniform colour and iterates the signature consisting of a vertex's previous colour and the multiset of its neighbours' previous colours. When two graphs are compared, colours are assigned by a single shared feature dictionary (equivalently, refine their disjoint union). The conclusion concerns exactly the vertex orders \(1\) through \(12\), not disconnected cographs or larger orders.

A key prior mathematical source is Arvind, Köbler, Rattan and Verbitsky (first arXiv submission 4 February 2015), which gives general structural background for colour refinement.

## Proof

**Enumeration lemma.** Every connected cograph of order greater than one has a unique reduced cotree: the leaves are the graph vertices, each internal node has at least two unordered children, internal nodes alternate between join and union operations along edges, and the root is labelled join. Conversely, every such tree constructs a connected cograph and different reduced cotrees construct nonisomorphic cographs. The uniqueness follows by recursive identification of the connected components of the graph or its complement: at a union node they are the graph's components; at a join node they are the complement's components. At each step these canonical components determine the multiset of immediate subtrees. Induction on leaf count establishes uniqueness.

The attached `verify_cograph_cr.py` implements this recurrence without invoking graph-isomorphism heuristics. It enumerates nondecreasing multisets of alternating-operation child trees whose positive leaf counts sum to \(n\), with at least two children, and then builds the graph adjacency bitmasks from disjoint union and join. The count by order \(1,\ldots,12\) is
\[
1,1,2,5,12,33,90,261,766,2312,7068,21965.
\]
These totals independently match the published House of Graphs connected-cograph counts at every tested order (the counts verify the enumeration scale; correctness of enumeration follows from the cotree lemma, not the numerical agreement alone).

**Refinement lemma.** For graphs on \(n\) vertices, colour refinement makes at most \(n-1\) proper splits of the vertex partition on any individual graph; on the disjoint union of a pair of graphs with \(n\) vertices each, a priori at most \(2n-1\) splits may occur. The implementation nevertheless uses \(n\) globally synchronized rounds on **all graphs of a given order**. This is sufficient for the *pairwise comparison* at order \(n\): if the colour histograms ever differ they remain different thereafter, and if the final pair has identical colour histograms the balanced equitable refinement cannot subsequently separate them. Indeed when the two graphs have identical colour histograms at one stage, every joint colour class has equal cardinality on both sides; a genuine split among classes that preserves these equalities must cause a proper split in each graph, so at most \(n-1\) such rounds can occur. More directly, one may run until simultaneous stabilization on the disjoint union for an unconditional bound; the exact verifier uses \(n\) rounds, which exceeds this threshold for any previously indistinguishable pair.

For each \(n\), the verifier calculates the (shared) colour class counts after \(n\) rounds, grouping graphs by the resulting histogram. It asserts no collision for \(n<12\), and at \(n=12\) asserts precisely three two-element collision classes. It checks both graphs in each class are regular with equal degree and identifies their complement-component order-multisets. The three checked outputs are
\[
\begin{array}{c|c|c}
\text{degree}&\text{complement component orders of first graph}&\text{of second graph}\\
7&(5,7)&(6,6)\\
8&(4,4,4)&(6,6)\\
9&(3,3,3,3)&(4,4,4).
\end{array}
\]
No other repeated colour-histogram class occurs. This exhaustive finite computation, justified by the enumeration and refinement lemmas and exposed as source code, establishes the claimed lower cutoff and complete classification at order \(12\).

## Verification

Run `python3 verify_cograph_cr.py` using Python 3 and only the standard library. It constructs each canonical cotree and graph directly, synchronizes vertex colours between the complete population at each order, and asserts the exact connected-cograph counts and collision classes. Successful execution prints `NAMED_WITNESSES_VERIFIED` and ends with `CENSUS_VERIFIED`. The three witness pairs are reconstructed from their displayed graph operations, recognized by canonical cotree comparison with the enumerated collision classes, and checked for regularity and distinct complement component types; all computations operate with integer adjacency bitmasks and integer multisets.

## Relationship to prior work

Arvind, Köbler, Rattan and Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness* (2015), establish structural results about graphs recognized by colour refinement and explain that nonisomorphic regular graphs with the same order and degree are indistinguishable. This gives the easy half of each witness but does **not**, by itself, establish a first-failure order or enumerate all pairs inside the connected-cograph family. Standard equivalences with fractional isomorphism and two-variable counting logic change the phrasing, not the finite cutoff addressed here. The House of Graphs cograph catalogue independently publishes the connected-cograph counts; its displayed metadata does not provide the asserted colour-refinement collision classification. Work on cotree generation supplies general enumeration techniques but likewise has not been established here to imply the stated three-pair conclusion.

## Limitations

The finding concerns ordinary one-dimensional colour refinement on connected cographs of order at most \(12\). It makes no assertion about higher-dimensional Weisfeiler–Leman refinement, other graph classes, or subsequent orders. The exhaustive proof depends on the provided finite enumerator; external independent verification of the claim has not been performed. The literature comparison is necessarily best knowledge, and unindexed or inaccessible literature could contain this exact finite classification. The catalogue counts are used only as population-count cross-checks, not as evidence of the colour-refinement collision classification.

## References

1. V. Arvind, J. Köbler, G. Rattan, and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first submitted 4 February 2015. https://arxiv.org/abs/1502.01255
2. House of Graphs, *Cographs* graph collection (connected cograph counts and graph6 catalogue). https://houseofgraphs.org/meta-directory/cographs
3. A. A. Jones, F. Protti, and R. R. Del-Vecchio, *Cograph generation with linear delay*, Theoretical Computer Science 713 (2018), 1–10; arXiv:1612.05827. https://arxiv.org/abs/1612.05827
