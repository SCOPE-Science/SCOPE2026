# Dual general-position spectra of triangular graphs \(T_n\)

## Finding

**Theorem.** For each integer \(n\geq3\), let \(T_n=L(K_n)=J(n,2)\) be the triangular graph, whose vertices are the two-element subsets of \([n]\), adjacent precisely when they intersect. Call a subset \(X\subseteq V(T_n)\) *dual general position* when no member of \(X\) lies internally on a shortest path between two other members of \(X\), and no member of \(X\) lies internally on a shortest path between two members of its complement. Let \(d_{n,k}\) count such subsets of cardinality \(k\), including the empty subset, and put \(D_n(z)=\sum_k d_{n,k}z^k\).

For \(n=3\), every subset qualifies. For \(n=4\), the only nonempty qualifying subsets are the four stars of three edges and the four edge sets of triangles in \(K_4\). For every \(n\geq5\), the only nonempty qualifying subsets are the \(n\) full stars
\[
X_u=\{\{u,v\}:v\in[n]\setminus\{u\}\},\qquad u\in[n].
\]
Therefore, with all terms understood as ordinary cardinality enumerators,
\[
\boxed{D_n(z)=\begin{cases}
(1+z)^3,&n=3,\\
1+8z^3,&n=4,\\
1+nz^{n-1},&n\geq5.
\end{cases}}
\]
In particular, the dual general-position number is \(3\) for \(n=3,4\) and \(n-1\) for \(n\geq5\). For every \(n\geq5\), all nonempty dual general-position sets are maximum, and the integers \(1,2,\ldots,n-2\) are *all missing* from their size spectrum. Their number of missing nonzero sizes grows without bound. Every proper nonempty subset of a qualifying nonempty set is nonqualifying for \(n\geq4\).

The novelty claim is the classification for the infinite regime \(n\geq5\), its exact size enumerator, and its all-or-nothing inclusion structure; the exceptional complete and complete-multipartite cases are included only to state the exact boundary.

## Assumptions and scope

All graphs are finite, simple, undirected, and distances are graph distances. The underlying base graph \(K_n\) has labeled vertices \([n]\), and a vertex of \(T_n\) is a base edge \(\{u,v\}\). A *full star* at \(u\) consists of all \(n-1\) base edges incident with \(u\). A *triangle edge set* is the set of the three base edges induced by three labels. A subset is **convex** if every geodesic between any two of its members lies entirely in that subset. Empty and singleton sets are convex by vacuity.

The dual condition is equivalent to the conjunction that \(X\) is an ordinary general-position set and \(V(T_n)\setminus X\) is geodesically convex, as in Tian–Klavžar (2024, Theorem 3.1). The proof below establishes its precise consequences directly for triangular graphs; it does not assume the desired classification.

For \(n\geq4\), \(T_n\) has diameter two: disjoint base edges are joined by any of their four cross edges. Consequently, if \(e=ab\) and \(f=cd\) are disjoint base edges, the internal vertices of all length-two geodesics between their corresponding vertices are exactly the four cross edges \(ac,ad,bc,bd\) of \(K_n\). This geodesic description is used in both directions.

## Proof

For \(n=3\), \(T_3\cong K_3\). Since every geodesic has length one, all subsets satisfy the dual condition. Hence \(D_3(z)=(1+z)^3\).

Now let \(n\geq4\) and let \(X\) be a nonempty dual general-position set. Identify it with a nonempty collection \(F\) of base edges of \(K_n\). Choose \(uv\in F\), and define the two missing-neighbor label sets
\[
A=\{w\in[n]\setminus\{u,v\}:uw\notin F\},\qquad
B=\{w\in[n]\setminus\{u,v\}:vw\notin F\}.
\]
If \(b\in A\), \(d\in B\), and \(b\ne d\), then the base edges \(ub\) and \(vd\) are disjoint, are both outside \(F\), and have \(uv\in F\) as a common neighbor in \(T_n\). The shortest path \(ub,uv,vd\) contradicts convexity of the complement. Thus **no pair of distinct labels can lie one in \(A\) and one in \(B\)**.

**Case 1: \(A=\varnothing\) or \(B=\varnothing\).** If \(A=\varnothing\), all edges at \(u\) lie in \(F\); the other possibility is symmetric. Suppose an additional selected base edge \(ab\in F\) avoids \(u\). Because \(n\geq4\), choose \(d\in[n]\setminus\{u,a,b\}\). The three selected vertices of \(T_n\) represented by \(ab,ua,ud\) occur in that order on the geodesic \(ab,ua,ud\): the endpoint edges \(ab\) and \(ud\) are disjoint, and each intersects \(ua\). This violates ordinary general position. Hence \(F\) equals exactly the full star at \(u\).

**Case 2: both \(A\) and \(B\) are nonempty.** Pick \(b\in A\) and \(d\in B\). The preceding prohibition forces \(b=d=w\). Any additional member of either \(A\) or \(B\) would differ from \(w\) in the other set, so \(A=B=\{w\}\). It follows that \(uv\in F\), and \(up,vp\in F\) for every \(p\in[n]\setminus\{u,v,w\}\).

If \(n\geq5\), choose distinct \(p,q\) in that latter set. Then \(up,vp,vq\) is a geodesic of \(T_n\) with all three vertices selected: the endpoint edges \(up\) and \(vq\) are disjoint and the central edge \(vp\) meets both. This is impossible. Thus **Case 2 never occurs for \(n\geq5\)**.

For \(n=4\), there is a unique remaining label \(p\), so \(F\) already contains the triangle edges \(uv,up,vp\) and omits \(uw,vw\). The only additional possible base edge is \(wp\). If \(wp\in F\), then \(wp,up,uv\) is a three-selected-vertex geodesic, another contradiction. Therefore \(F=\{uv,up,vp\}\), exactly a triangle edge set.

It remains to check sufficiency. Any full star in \(K_n\) is a clique of \(T_n\), so it is in ordinary general position. Its complement corresponds to all edges of \(K_{n-1}\) on the other labels. The four cross edges of any two disjoint complementary base edges also avoid the star center and hence belong to the complement. Therefore the complement is convex, and each full star is dual general position. When \(n=4\), each base triangle forms a clique of \(T_4\), and its complement consists of the three edges incident with the fourth label, which also form a clique; the complement is convex. Thus these exceptional triangles also qualify.

Different centers give different full stars, and distinct three-element base label sets give different triangles. Counting yields exactly four stars and four triangles when \(n=4\), and exactly \(n\) full stars when \(n\geq5\). Together with the empty set and \(n=3\), this proves the displayed polynomial, dual number, missing-size spectrum, and all-or-nothing inclusion claims. \(\square\)

## Verification

The accompanying standalone Python program `verify_dual_gp.py` constructs the triangular graph from its base-edge adjacency, computes all-pairs shortest distances by breadth-first search, and checks the dual definition directly: for every two graph vertices in the same membership class, no selected vertex may be internal to any shortest path between them. It does not use the proof's star-or-triangle implication in the definition-level decision; that implication is separately tested as the expected result.

Exhaustive tests examine every one of the \(2^{\binom n2}\) subsets for each \(n\in\{3,4,5,6\}\), totaling \(33864\) subsets. They return coefficient multisets \(\{0:1,1:3,2:3,3:1\}\), \(\{0:1,3:8\}\), \(\{0:1,4:5\}\), and \(\{0:1,5:6\}\), respectively. Additional deterministic membership checks sample \(5009\) subsets when \(n=7\) and \(5010\) when \(n=8\). Run with `python3 verify_dual_gp.py`; a sample transcript is embedded as `verification_output.txt`.

These finite checks are corroboration, **not** an infinite proof. The infinite result follows from the preceding exhaustive structural case analysis for arbitrary \(n\geq5\).

## Relationship to prior work

Tian and Klavžar (2024) defined the dual general-position variant and established the criterion ordinary general position plus a convex complement. Their source develops general structural tests and Cartesian products, rather than classifying \(L(K_n)\) or enumerating its dual sets. The present proof uses that foundation but determines an infinite family for which every nonempty solution is a whole star.

Di Stefano and collaborators (2023) analyzed the ordinary *lower* general-position number of \(L(K_n)\) and described maximal ordinary general-position configurations in terms of stars and triangles. The lower ordinary parameter, however, neither imposes convexity of the complement nor classifies the dual solutions. Earlier work on ordinary general-position numbers of line graphs likewise concerns a less restrictive invariant. The \(n=4\) exception is a complete-multipartite special case and is not advanced as a new separate result.

A direct theorem implication comparison is essential: even knowing the ordinary maximal-set classification leaves the convex-complement test unresolved. The requirement that all four cross edges avoid a selected edge is the additional structural obstruction responsible for the formula for \(n\geq5\).

## Limitations

No independent audit has been performed. Originality has been evaluated against the identified foundational and closely related accessible full texts, targeted published-result searches, and related variant terminology; unindexed equivalent formulas remain a bibliographic priority risk. This finding does not claim a new result for ordinary general position or a new characterization of the generic dual criterion. The finite verifier tests only the stated small orders and samples; it cannot settle arbitrarily large orders by computation. All statements concern labeled simple triangular graphs as defined, with no assertion for general Johnson graphs of higher subset size.

## References

1. J. Tian and S. Klavžar, *Variety of general position problems in graphs*, arXiv:2402.17338v1 (first posted 2024-02-27), especially Theorem 3.1. https://arxiv.org/html/2402.17338v1
2. G. Di Stefano, S. Klavžar, A. Krishnakumar, J. Tuite, and I. G. Yero, *Lower General Position Sets in Graphs*, arXiv:2306.09965v1 (first posted 2023-06-16), especially Section 5 and Theorem 5.2. https://ar5iv.labs.arxiv.org/html/2306.09965
3. A. Ghorbani and coauthors, *The general position problem on Kneser graphs and on some graph operations*, arXiv:1903.04286v1 (first posted 2019-03-11). https://arxiv.org/abs/1903.04286
