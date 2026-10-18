# A sharp counting-logic identification threshold for powers of paths

## Finding

For integers \(n\geq 1\) and \(k\geq1\), write \(P_n^{[k]}\) for the simple graph on \(\{0,\ldots,n-1\}\) in which distinct vertices \(i,j\) are adjacent exactly when \(|i-j|\leq k\). In the adjacency-only language, the following conditions are equivalent:

1. \(P_n^{[k]}\) is identified up to isomorphism *among all finite simple graphs* by two-variable first-order logic with counting, \(C^2\).
2. Ordinary colour refinement distinguishes \(P_n^{[k]}\) from every nonisomorphic finite simple graph.
3. Either \(k=1\) or \(n\leq k+4\).

For every \(k\geq2\) and \(n\geq k+5\), there is an explicit nonisomorphic \(C^2\)-equivalent graph on the same \(n\) vertices, obtained by switching just two edges of \(P_n^{[k]}\). Thus \(k+5\) is the sharp first nonidentification order for each fixed \(k\geq2\), and the first obstruction in the two-parameter family is at \((n,k)=(7,2)\).

## Assumptions and scope

All graphs here are finite, simple, undirected, uncoloured, and without distinguished vertices. Two graphs are identified by \(C^2\) when their common \(C^2\)-sentence theory forces isomorphism, *without* assuming that a comparison graph belongs to the path-power family. Colour refinement starts with one vertex colour and repeatedly replaces each colour by that colour together with the multiset of neighbouring colours. We use the standard correspondence between colour-refinement indistinguishability and \(C^2\)-equivalence [1,2].

## Proof

**Case 1: complete graphs.** If \(n\leq k+1\), every two different vertices are adjacent. Its vertex count and full degree are detected by the first refinement step, so an indistinguishable graph is the same complete graph.

**Case 2: the range \(k\geq2\), \(k+2\leq n\leq k+4\).** Put \(t=n-k-1\in\{1,2,3\}\), and define the pairs \(A_i=\{i,n-1-i\}\), for \(0\leq i<t\), and the possibly empty central set \(U=\{t,t+1,\ldots,k\}\). Each vertex in \(U\) is universal. The two vertices of \(A_i\) have degree \(k+i\), and these degrees are mutually distinct and strictly below \(n-1\). Reflection of the path interchanges the members of each pair, so the first degree partition \(\{A_0,\ldots,A_{t-1},U\}\), omitting empty \(U\), is equitable and hence is the stable colour partition.

Every vertex in a pair \(A_i\) has a uniquely determined number of neighbours in each other colour class, as does every vertex in \(U\). The induced graph on a two-element colour class is either an edge or two isolates, uniquely determined by its internal neighbour count. Connections to \(U\) are complete. For \(0\leq i<j<t\), the bipartite graph between \(A_i\) and \(A_j\) is complete if \(i+j\geq t\); if \(i+j<t\), it is a perfect matching. This follows because the same-side distances are \(j-i\leq2\leq k\), whereas opposite-side distance is \(n-1-i-j=k+t-i-j\). Thus the graph formed on the pair classes by *matching* connections is empty for \(t=1\), one edge for \(t=2\), and the two-edge tree \(A_1-A_0-A_2\) for \(t=3\).

Let \(H\) be any graph colour-refinement-equivalent to \(P_n^{[k]}\). Its stable classes have corresponding cardinalities and the same within-class and between-class degrees. Hence its two-vertex classes are joined by precisely the same pattern of complete, empty or matching bipartite blocks; \(U\) is universally adjacent, and the internal edges of each pair are determined. Since the matching-block graph is a forest, label the vertices of one pair arbitrarily and propagate labels along the forest edges: every matching can then be made the same standard matching. Independent flips of the two labels inside pair classes preserve all complete/empty blocks and internal pair edges. This constructs a colour-preserving graph isomorphism \(H\cong P_n^{[k]}\).

**Case 3: the path \(k=1\).** If \(n\geq3\), the first step singles out the two degree-one endpoints (orbits under reflection). In each further refinement, the two next vertices inward are singled out as the unique vertices of the still-undistinguished interval adjacent to the most recently distinguished outer layer. Inductively, the stable classes are exactly the distance-from-nearest-end pairs \(\{i,n-1-i\}\), together with a singleton middle vertex when \(n\) is odd. Between consecutive two-vertex layers there is a matching, while the central singleton, if any, is adjacent to both vertices of the preceding layer. Internal edges are determined. As the matching connections form a path, the same label-propagation argument as in Case 2 reconstructs any refinement-equivalent graph uniquely. The cases \(n\leq2\) are complete.

**Case 4: explicit nonidentification for \(k\geq2\), \(n\geq k+5\).** Define \(A_i=\{i,n-1-i\}\) for \(i=0,1,2\). The degree colours distinguish \(A_0\) and \(A_1\) as exact two-element classes of degrees \(k\) and \(k+1\). If \(k\geq3\), the degree colour of \(A_2\) is the distinct degree \(k+2\). For \(k=2\), vertices of \(A_2\) are exactly the degree-four vertices having a neighbour in the degree-two class \(A_0\); one extra refinement round distinguishes this pair from any interior degree-four vertices. Consequently \(A_0,A_1,A_2\) are distinct two-element stable colour classes for every permitted \(n,k\).

Among each pair of classes \(A_0,A_1\), \(A_1,A_2\), and \(A_0,A_2\), the cross-edges consist exactly of the same-side matching (the two edges joining smaller indices together and larger indices together). Indeed, differences between small indices are at most two, while cross-side differences are at least \(n-4\geq k+1\).

Construct \(H\) on the same vertices by **deleting** \(\{0,2\}\) and \(\{n-1,n-3\}\), and **inserting** \(\{0,n-3\}\) and \(\{n-1,2\}\), leaving every other edge unchanged. This switches the matching between the stable classes \(A_0\) and \(A_2\) and preserves the number of neighbours each vertex has in every stable class. Induction on the refinement round therefore shows that every vertex receives exactly the same refinement colour in \(H\) as in \(P_n^{[k]}\), in every round. In particular these graphs satisfy the same \(C^2\) sentences.

The two graphs are not isomorphic. The subgraph on \(A_0\cup A_1\cup A_2\) contains exactly two triangles with one vertex in each of the three *distinct stable colour classes* in \(P_n^{[k]}\), but **none** in \(H\): the three matchings give two parallel triangles before the switch and a six-cycle after it, as far as edges between the three classes are concerned. Isomorphisms preserve stable colour classes and hence preserve this rainbow-triangle count. Therefore no isomorphism exists. This completes the if-and-only-if proof and its sharpness assertion.

## Verification

Run `python3 verify.py` and `python3 verify_alt.py` from this package. The first independently forms adjacency sets, verifies the small-order degree quotient, computes synchronised colour-refinement histories after switching, and checks the differing three-class triangle counts over \(1\leq k\leq24\), \(1\leq n\leq84\). The second uses a separate adjacency-matrix implementation, tests the small-degree patterns, and checks the same collision phenomenon over \(1\leq k\leq17\), \(1\leq n\leq74\). These tests corroborate the derivation; the all-parameter proof above, rather than any finite enumeration, establishes the theorem.

## Relationship to prior work

Arvind, Köbler, Rattan and Verbitsky [1] give a general structural characterization of graphs amenable to colour refinement, including the exclusion of uniform anisotropic cell cycles (their Lemma 7(D)) and the recognition criterion (Theorem 9). Kiefer, Schweitzer and Selman [2] also give a general classification of graphs identified by \(C^2\) (their Theorem 17). The present statement is **not** a new general characterization of amenability. It evaluates identification exactly across the natural two-parameter family of powers of paths and supplies an explicit sharp threshold and two-edge witnesses; these parameter-specific conclusions were not stated in the inspected primary texts. The switching argument is an instance of the classical equitable-cell switching obstruction [1], not a new equivalence method.

## Limitations

The theorem concerns uncoloured, unrooted path powers and identifiability *against arbitrary finite simple graphs*. The nonisomorphic witnesses are not claimed to be path powers, and the theorem does not assert that any two different path powers are \(C^2\)-equivalent. It makes no claim about higher-dimensional Weisfeiler–Leman, unrestricted first-order logic, or independent verification. An unlocated specialized earlier treatment of path powers could supersede the asserted priority of the exact threshold.

## References

[1] V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first publicly posted 2015-02-04, version 3 (2015), in particular Sections 2–5, Lemmas 6–7 and Theorem 9. https://arxiv.org/abs/1502.01255

[2] S. Kiefer, P. Schweitzer and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792, first publicly posted 2015-03-30, in particular Theorem 17. https://arxiv.org/abs/1503.08792
