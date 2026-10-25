# A connected well-covered clique-tail family separating packing and Grundy packing coloring

## Finding

For each integer \(m\ge3\), let \(H_m\) be the graph obtained from a clique \(K_m\) by choosing a vertex \(c\) and adding two new vertices \(d,e\) and precisely the new edges \(cd,de\). Thus \(|V(H_m)|=m+2\). Every \(H_m\) is connected and well-covered, yet its ordinary packing chromatic number and its Grundy packing chromatic number differ:

\[
\chi_\rho(H_m)=m,\qquad \Gamma_\rho(H_m)=m+1.
\]

The graph \(H_3\), a triangle with an attached two-edge pendant path, is (up to graph isomorphism) the unique graph on **at most five vertices** that is well-covered and has \(\Gamma_\rho>\chi_\rho\). Here \(\chi_\rho(H_3)=3\) and \(\Gamma_\rho(H_3)=4\). This gives a negative answer to the well-covered-graph question in Problem 6.3 of Gözüpek and Peterin [1]. The uniqueness assertion is an exhaustive finite classification, while the family identities have unrestricted proofs.

## Assumptions and scope

Graphs are finite, simple, undirected. Distances between vertices in distinct components are infinite. An \(i\)-packing is a vertex set whose distinct elements are at distance strictly greater than \(i\). A packing \(k\)-coloring is a map \(f:V(G)\to\{1,\dots,k\}\) whose color-\(i\) class is an \(i\)-packing. Its least possible palette size is \(\chi_\rho(G)\). In a first-fit greedy packing coloring, vertices are processed in some order, each receiving the smallest positive color whose packing constraint is consistent with all earlier assignments. The maximum color used over all vertex orders is \(\Gamma_\rho(G)\). A graph is well-covered if all inclusion-maximal independent sets have equal cardinality.

Write \(Q=V(K_m)\), \(R=Q\setminus\{c\}\). Notice that \(|R|=m-1\ge2\), and that the only pairs of vertices at distance three in \(H_m\) are \((e,r)\) with \(r\in R\).

## Proof

**1. Well-coveredness.** An independent set contains at most one vertex of \(Q\) and at most one of \(d,e\), because \(Q\) is complete and \(de\) is an edge. Thus its size is at most two. Every singleton can be extended: \(\{c\}\) extends with \(e\), \(\{r\}\) for \(r\in R\) extends with \(d\) (or \(e\)), \(\{d\}\) extends with any \(r\in R\), and \(\{e\}\) extends with any vertex of \(Q\). Therefore every maximal independent set has cardinality exactly two. In particular \(H_m\) is well-covered.

**2. Packing minimum.** The maximum size of a 1-packing is two. Since the only distance-three pairs are \((e,r)\), the maximum size of a 2-packing is also two. The diameter is three, so every \(i\)-packing for \(i\ge3\) contains at most one vertex. A packing coloring with \(k\ge2\) colors therefore covers at most \(2+2+(k-2)=k+2\) vertices. As \(H_m\) has \(m+2\) vertices, its packing chromatic number is at least \(m\); one color is clearly impossible. Conversely, choose distinct \(a,b\in R\). Give color 1 to \(a,d\) (distance two), color 2 to \(b,e\) (distance three), and assign distinct colors \(3,\ldots,m\) to the remaining \(m-2\) clique vertices. This is a packing \(m\)-coloring. Hence \(\chi_\rho(H_m)=m\).

**3. Greedy maximum.** In every first-fit coloring, the color-1 class is a maximal independent set: if another vertex could receive color 1 without violating its constraint, it would have received 1 upon processing. The first part shows this class has exactly two vertices. Every color below the largest used color must occur (a vertex assigned a larger color must have found each smaller color unavailable). Thus a first-fit coloring using \(t\) colors consumes at least \(2+(t-1)\) vertices. Since there are \(m+2\), necessarily \(t\le m+1\).

For the matching lower bound choose distinct \(a,b\in R\) and process the vertices in the order \(e,a,b,c,d\), followed by the remaining \(m-3\) clique vertices in arbitrary order. First fit gives the colors \(1,1,2,3,4,5,\ldots,m+1\), in that processing order. Indeed, \(d(e,a)=3\), so the first two receive color 1; \(b\) is adjacent to \(a\), so receives 2; \(c\) is adjacent to \(a,b\), so receives 3; \(d\) is adjacent to \(e\), at distance two from \(b\), and adjacent to \(c\), so receives 4. Every remaining clique vertex is adjacent to the vertices with colors 1, 2, 3 and to earlier colored clique vertices, and is at distance two from the vertex with color 4. It therefore receives the next new color. This attains \(m+1\), proving \(\Gamma_\rho(H_m)=m+1\).

**4. Minimum size and uniqueness of the first obstruction.** For \(m=3\), label the graph by \(\{0,1,2,3,4\}\), with edges \(04,12,13,23,34\). The five maximal independent sets are precisely \(\{0,1\},\{0,2\},\{0,3\},\{1,4\},\{2,4\}\). Processing vertices \(0,1,2,3,4\) in that order gives greedy colors \((1,1,2,3,4)\); the ordinary three-color packing assignment indexed by \(0,1,2,3,4\) is \((2,1,2,3,1)\).

Uniqueness among graphs on at most five vertices follows by an exhaustive, finite, independently re-executable enumeration of all unlabeled simple graphs of orders one through five (see `verify.py`). The search constructs all \(2^{\binom n2}\) labeled adjacency masks, reduces by all \(n!\) vertex permutations, tests every nonempty vertex subset for maximal independence, and checks every \(n^n\) coloring map into \(\{1,\ldots,n\}\). For the greedy condition, an assignment is realizable by first fit exactly when it is a packing coloring and, at each vertex assigned \(i\), for every \(j<i\) some vertex of color \(j\) lies within distance \(j\). Necessity is immediate; sufficiency follows by processing vertices in nondecreasing assigned color. This tests all possible orders without omission. The numbers of unlabeled graphs of orders one through five are \(1,2,4,11,34\); of these, the numbers that are well-covered are \(1,2,3,7,14\). None below order five separates the two parameters, and exactly one well-covered isomorphism type at order five does. The verifier checks its isomorphism to \(H_3\) explicitly. Because all finite adjacency masks and all relevant colorings are exhausted, this is a proof of the bounded uniqueness claim, not an inference from a sample.

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter, without external packages. The standalone program reconstructs graph distances by breadth-first search; tests maximal independent sets directly; builds unlabeled graph classes through vertex permutations; enumerates packing and first-fit-realizable color maps through order five; and checks the clique-tail witnesses, with exhaustive color testing for clique orders three through five and direct witness checks through order ten. The expected output is recorded in `verification_output.txt`. The finite computation supports the precise minimum-order and uniqueness conclusion; the infinite-family identities have the elementary proof above.

## Relationship to prior work

Gözüpek and Peterin [1] introduced the Grundy packing chromatic number and proved formulas using maximal independent sets and diametrical graphs, particularly Theorems 5.3 and 5.6 for diameter-three graphs. Corollary 6.2 establishes equality of the two numbers for diameter-two well-covered graphs; Problem 6.3 explicitly asks whether equality persists for all well-covered graphs. The new family has diameter three, so Corollary 6.2 does not apply. Their general optimization formulas can be evaluated **after** a graph is specified but do not present the connected counterexample family or the minimum-order uniqueness classification. The claim here is the explicit sharp negative answer with a connected infinite construction and a fully checked smallest obstruction, not a new definition or a replacement for those general formulas. Searches of alternate terminology (first-fit, greedy packing, lollipop and clique-tail graphs) and mathematical research records did not locate a directly covering result; negative search results do not establish priority.

## Limitations

The result does not classify every well-covered graph with a packing/Grundy packing gap or make the gap unbounded on well-covered connected graphs. The gap in the demonstrated family is one. The minimum-order uniqueness classification is proved by exhaustive finite enumeration only through five vertices; it is not a census of larger graphs. Literature priority is subject to uncatalogued or inaccessible later work. Independent mathematical review has not been performed.

## References

[1] D. Gözüpek and I. Peterin, *Grundy Packing Coloring of Graphs*, arXiv:2409.00697, first posted 2024-09-01. Full text: https://arxiv.org/html/2409.00697v1; arXiv record: https://arxiv.org/abs/2409.00697. In particular, Sections 2, 3, 5 and Problem 6.3 in Section 6.
