# Degree-sequence collapse of concept-stability spectra for graph-incidence lattices

## Finding

**Theorem (exact stability spectrum, faithful lattice, unbounded collisions).** Let \(G=(V,E)\) be any finite simple undirected graph with \(n=|V|\geq3\), \(m=|E|\), and minimum degree at least two. Form the formal context \(K_G=(E,V,I)\), with the **edges as objects**, **vertices as attributes**, and \(eIv\) exactly when \(v\) is an endpoint of \(e\). Let \(L_G\) be its concept lattice and \(\sigma(C)\) the intensional stability of a concept under uniform thinning of its extent.

1. There are exactly \(m+n+2\) concepts. Their extents are precisely \(\varnothing\), the singleton edge sets \(\{e\}\), the incident-edge stars \(S_v=\{e\in E:v\in e\}\), and \(E\). Their complete **unlabelled** multiset of stability values is
   \[
   \left\{\!\left\{1,\ \underbrace{\tfrac12,\ldots,\tfrac12}_{m\text{ edge concepts}},\ \left(1-\frac{d(v)+1}{2^{d(v)}}\right)_{v\in V},\ 1-\frac{\sum_{v\in V}2^{d(v)}-n-m+1}{2^m}\right\}\!\right\},
   \]
   with multiplicity, where \(d(v)=|S_v|\). Hence the entire unlabelled stability distribution depends only on the graph's degree multiset.
2. In contrast, the **unlabelled order structure** of \(L_G\) reconstructs the graph uniquely up to isomorphism. Its coatoms are exactly the star concepts; two different coatoms have a nonbottom meet exactly when the corresponding vertices are adjacent. Thus \(L_G\cong L_H\) if and only if \(G\cong H\) within this class.
3. The loss of information can be arbitrarily large. For each integer \(t\geq1\), define \(G_{t,j}\), for \(0\leq j\leq t\), as the disjoint union of \(j\) copies of \(K_{3,3}\) and \(t-j\) copies of the triangular prism graph. These \(t+1\) pairwise nonisomorphic graphs have pairwise nonisomorphic concept lattices, yet they have precisely the same stability multiset:
   \[
   \left\{\!\left\{1,\ \underbrace{\tfrac12,\ldots,\tfrac12}_{15t\text{ times}},\ 1-\frac{33t+1}{2^{9t}}\right\}\!\right\}.
   \]
   For \(t=1\), the distinct connected cubic graphs \(K_{3,3}\) and the triangular prism each have fifteen concepts of stability \(1/2\), one concept of stability \(1\), and one of stability \(239/256\), despite nonisomorphic lattices.

The distinction between the complete stability multiset and the lattice **with** its stability labels is essential: the latter still contains the graph through its order alone.

## Assumptions and scope

For \(X\subseteq E\), define \(X'=\{v\in V:\forall e\in X,\ eIv\}\). This is the intersection of all endpoints of edges in \(X\), with the empty intersection interpreted as \(V\). For \(B\subseteq V\), define \(B'=\{e\in E:\forall v\in B,\ eIv\}\). A formal concept is a pair \((A,B)\) satisfying \(A'=B\) and \(B'=A\). Its extent is \(A\), and the concept order is extent inclusion. Its intensional stability is
\[
\sigma(A,B)=2^{-|A|}\bigl|\{X\subseteq A:X'=B\}\bigr|.
\]
The domain is *all* finite simple graphs with at least three vertices and minimum degree at least two, including disconnected graphs. No random-graph assumption is made. The results concern the **unlabelled multiset of stability values over all concepts**, not merely their average, and distinguish this from the complete concept-lattice order.

## Proof

**Step 1: Exhaustive classification of extents.** Each edge has exactly two endpoints. For \(X=\varnothing\), we have \(X'=V\) and \(X''=\varnothing\), since \(n\geq3\). For a singleton \(X=\{e\}\), its derivation is the two endpoints of \(e\); simplicity implies that only \(e\) has both endpoints, so \(X''=\{e\}\). If \(|X|\geq2\), two different edges have at most one common endpoint. Thus either the edges in \(X\) have a unique common endpoint \(v\), in which case \(X'=\{v\}\) and \(X''=S_v\), or their common endpoint set is empty, in which case \(X''=E\). Conversely, every \(S_v\) is obtained by intersecting the endpoints of any two distinct edges incident to \(v\), which exist by the minimum-degree hypothesis; and \(E\) is obtained from a pair of edges with no common endpoint, or from three edges with no common endpoint, both of which exist because no vertex is incident to all edges when every vertex has degree at least two. More directly, \(E'=\varnothing\), since a vertex incident to all edges would force each other vertex to have degree at most one. The listed extents are distinct: stars have at least two edges, are different from \(E\), and two vertex stars can coincide only if every incident edge at either endpoint were the same single edge. This gives exactly \(m+n+2\) concepts.

**Step 2: Individual stability values.** The bottom concept has extent \(\varnothing\), whose sole subset has derivation \(V\), giving stability \(1\). The singleton-edge concept has one good subset, the singleton itself, among two, giving \(1/2\). For a star \(S_v\) of cardinality \(d(v)\), precisely its subsets of cardinality at least two have derivation \(\{v\}\): the empty subset derives \(V\), and a singleton edge derives two endpoints. Consequently, the number of good subsets is \(2^{d(v)}-1-d(v)\), yielding \(1-(d(v)+1)/2^{d(v)}\).

For the top concept, the good subsets \(X\subseteq E\) are exactly those with \(X'=\varnothing\). A *bad* subset has a common vertex. Such subsets are: the one empty set; the \(m\) singleton-edge sets; and, for each \(v\), the \(2^{d(v)}-1-d(v)\) subsets of \(S_v\) of size at least two. Every such subset of size at least two has **at most one** common vertex because the graph is simple, so the counts do not overlap. Therefore, the number of bad subsets is
\[
1+m+\sum_{v\in V}(2^{d(v)}-1-d(v))
=\sum_{v\in V}2^{d(v)}-n-m+1,
\]
using \(\sum_v d(v)=2m\). Dividing the complementary count by \(2^m\) proves the asserted top stability and the full multiset.

**Step 3: Order reconstruction.** The singleton-edge extents are exactly the atoms (minimal nonbottom elements) of \(L_G\), and the stars \(S_v\) are exactly its coatoms (maximal proper elements): the complete list of extents in Step 1 has no other intermediates. For different vertices \(u,v\), their coatom meet has extent \(S_u\cap S_v\). Simplicity implies that this intersection is \(\{uv\}\) if \(uv\in E\), and is empty otherwise. Thus the graph on the coatoms in which two vertices are joined when their meet exceeds the lattice bottom is canonically isomorphic to \(G\). This reconstruction works up to vertex relabelling, proving the stated isomorphism equivalence.

**Step 4: Unbounded collisions.** Both \(K_{3,3}\) and the triangular prism have six vertices, nine edges, and every vertex of degree three. The former has no triangles; the latter has exactly two triangles. Disjoint unions of \(t\) copies in proportions \(j:(t-j)\) therefore have \(6t\) vertices, \(9t\) edges, all degrees three, and \(2(t-j)\) triangles. Distinct \(j\) yield nonisomorphic graphs and hence nonisomorphic lattices by Step 3. Substitution into Step 2 gives \(15t\) middle concepts of stability \(1/2\), bottom stability \(1\), and top stability \(1-(33t+1)/2^{9t}\), independent of \(j\). This proves every assertion.

## Verification

The supplied standalone `verify_graph_stability.py` recomputes derivations, double-prime closures, all concepts, and each intensional stability directly from the edge-vertex incidence relation. It then compares the complete resulting multiset with the formula and tests that atom/coatom meets recover adjacency. It runs exhaustively through all labelled simple graphs of orders three through five with minimum degree at least two and through the two six-vertex witness graphs. The execution reported `VERIFY_OK graphs=266 enumerated_object_subsets=37624 witness=K33_vs_triangular_prism spectrum=1:1,1/2:15,239/256:1`. These finite checks supplement, but do not establish, the proof for arbitrary graph size.

## Relationship to prior work

Concept stability is an established formal-concept quality measure; Mouakher, Ragobert, Gerin and Ko (2021) use stability in conceptual coverage. Mouakher and Ko (2022) give a general exact-computation approach based on concept covers. Rawson, Myers, Green, Robinson and Joslyn (2023) establish a general concept-lattice/intersection-complex correspondence for hypergraphs. Their accessible substantive statements describe the measure and general lattice encoding, rather than an exact degree-sequence collapse or the unbounded loss of graph isomorphism information proved here. A general exact stability algorithm can evaluate the particular instances but does not by itself state the graph-uniform closed form or the nonidentifiability theorem. No claim is made that the general stability definition, closure computation or the intersection-complex correspondence is new.

## Limitations

The hypothesis of simplicity is used to make two incident stars intersect in at most one edge; the minimum-degree assumption prevents singleton and star concepts from merging, and excludes isolated vertices. Thus the displayed spectrum is **not** asserted for graphs with leaves, isolates, multiple edges, or for arbitrary hypergraphs. The theorem does not say that the degree multiset can be recovered from the numerical stability multiset, nor that the stability-labelled lattice loses information. An exact-stability study from 2022 was accessible only at the abstract and bibliographic level; equivalent graph-specialized statements in its full text or elsewhere remain a literature risk. The computational enumerations do not prove the general theorem. Independent mathematical review has not been performed.

## References

1. A. Mouakher, A. Ragobert, S. Gerin, A. Ko, *Conceptual Coverage Driven by Essential Concepts: A Formal Concept Analysis Approach*, Mathematics 9 (2021), 2694, first public 2021-10-23. https://doi.org/10.3390/math9212694 .
2. A. Mouakher, A. Ko, *Efficient assessment of formal concept stability in the Galois lattice*, International Journal of General Systems 51 (2022), 791–821, public online 2022-07-31. https://doi.org/10.1080/03081079.2022.2084728 .
3. M. G. Rawson, A. Myers, R. Green, M. Robinson, C. Joslyn, *Formal Concept Lattice Representations and Algorithms for Hypergraphs*, arXiv:2307.11681, first public 2023-07-21. https://arxiv.org/abs/2307.11681 .
