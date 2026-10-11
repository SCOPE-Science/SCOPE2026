# A three-page collapse threshold for quadrilateral book matching complexes
## Finding
Let \(B_n\) be the graph with vertices \(u,v,a_i,b_i\) for \(1\le i\le n\), common edge \(c=uv\), and page edges \(p_i=ua_i\), \(q_i=a_ib_i\), and \(r_i=b_iv\). Thus the \(i\)-th page is the four-cycle \(u,a_i,b_i,v,u\), and all pages share exactly the edge \(c\). Let \(\mathcal M(B_n)\) denote the ordinary matching complex, whose vertices are edges of \(B_n\) and whose simplices are pairwise vertex-disjoint edge sets.

For every integer \(n\ge 1\),
\[
\mathcal M(B_n)\simeq
\begin{cases}
S^0,& n=1,\\
S^1\vee S^1,& n=2,\\
\ast,& n\ge 3.
\end{cases}
\]
In the last case the conclusion is stronger: \(\mathcal M(B_n)\) is simplicially collapsible for every \(n\ge 3\).

## Assumptions and scope
All graphs are finite and simple. The matching complex is the flag complex on the graph edges with two vertices adjacent exactly when the corresponding graph edges are disjoint. The statement concerns the quadrilateral book, meaning pages that are copies of \(C_4\) sharing one edge; it does not use the alternative convention in which “book graph” may mean triangles sharing an edge.

The argument uses the standard star-cluster fact for flag complexes: if \(K\) is flag and \(\sigma\) is a simplex of \(K\), then the union of the closed stars of the vertices of \(\sigma\) is collapsible.

## Proof
Put \(Q=\{q_1,\ldots,q_n\}\). The edges \(q_i\) are pairwise disjoint, so \(Q\) is a simplex of \(\mathcal M(B_n)\). Write
\[
C=\bigcup_{i=1}^n \operatorname{st}_{\mathcal M(B_n)}(q_i).
\]
Because a matching complex is flag, the star-cluster fact implies that \(C\) is collapsible.

Take any matching \(F\) in \(B_n\). If \(c\in F\), then no \(p_i\) or \(r_i\) belongs to \(F\), so every \(q_k\) is compatible with \(F\); hence \(F\in C\). Suppose instead that \(c\notin F\). Since all \(p_i\) meet at \(u\), at most one edge of the form \(p_i\) lies in \(F\). Likewise, at most one edge of the form \(r_j\) lies in \(F\). The edge \(q_k\) conflicts only with \(p_k\) and \(r_k\). Therefore at most two indices \(k\) are blocked by \(F\). If \(n\ge 3\), choose an unblocked index \(k\); then \(F\cup\{q_k\}\) is again a matching, so \(F\in\operatorname{st}(q_k)\subseteq C\). Thus \(\mathcal M(B_n)=C\), proving collapsibility for \(n\ge 3\).

For \(n=2\), the only simplices outside \(C\) are the two edges \(\{p_1,r_2\}\) and \(\{p_2,r_1\}\); all four endpoints lie in \(C\). Since \(C\) is a nonempty contractible subcomplex, quotienting \(C\) to a point is a homotopy equivalence for the ambient CW complex. The two remaining intervals then become two loops with disjoint interiors, giving
\[
\mathcal M(B_2)\simeq S^1\vee S^1.
\]

For \(n=1\), the graph is \(C_4\). Its matching complex has exactly two maximal simplices, \(\{c,q_1\}\) and \(\{p_1,r_1\}\), which are disjoint edges. Hence it is homotopy equivalent to two points, namely \(S^0\).

## Verification
The standalone script `verify_book_matching.py` exactly enumerates every matching for \(1\le n\le 7\), reconstructs the matching complex, computes reduced homology over \(\mathbf F_2\), and checks membership in the star cluster of \(Q\). It confirms that the faces outside the star cluster are exactly the three nonempty faces supported on \(\{p_1,r_1\}\) for \(n=1\), exactly the two exceptional edges in the proof for \(n=2\), and none for \(3\le n\le 7\). The computed reduced Betti vectors are \((1,0)\) for \(n=1\), \((0,2,0)\) for \(n=2\), and zero in all degrees for \(3\le n\le 7\).

These finite calculations are checks rather than the proof for arbitrary \(n\); the all-\(n\) collapsibility statement follows from the blocked-index argument above and the star-cluster theorem.

## Relationship to prior work
Donovan and Scoville study matching complexes using star clusters and compute Dutch windmill families, in which cycles meet at a common vertex. Their paper supplies the flag/star-cluster mechanism used here but does not treat edge-sharing quadrilateral books; a full-text search for “book” in that source is empty.

Bayer, Jelić Milutinović, and Vega study polygonal line tilings, where each new polygon meets the preceding structure in an edge and no three polygons intersect. The quadrilateral book with at least three pages lies outside that hypothesis because every page contains the same common edge. Their results may subsume small boundary instances such as two pages, but they do not imply the sharp all-page collapse threshold proved here.

A later theorem on matching complexes of outerplanar graphs also does not cover the family from three pages onward: \(B_n\) contains a subdivision of \(K_{2,3}\) whenever \(n\ge 3\), and hence is nonouterplanar.

## Limitations
The theorem is specific to ordinary matching complexes of quadrilateral books. It does not classify books made from longer cycles, generalized matching complexes, or alternative triangular-book conventions. The finite verifier only checks \(n\le 7\); it is not used to infer the arbitrary-n result. The literature comparison cannot exclude uncatalogued results under different terminology, especially edge-amalgamated cycle families.

## References
1. Connor Donovan and Nicholas A. Scoville, “Star clusters in the matching, Morse, and generalized complex of discrete Morse functions,” New York Journal of Mathematics 29 (2023), 1393–1412; arXiv:2207.13780. First public version: 2022-07-27.
2. Margaret Bayer, Marija Jelić Milutinović, and Julianne Vega, “General polygonal line tilings and their matching complexes,” arXiv:2211.12559. First public version: 2022-11-22.
3. Margaret Bayer, Marija Jelić Milutinović, and Julianne Vega, “Matching Complexes of Outerplanar Graphs,” arXiv:2411.04601.
