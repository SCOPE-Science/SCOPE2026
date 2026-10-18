# Minimal fort hypergraph and fractional forcing of triangular graphs

## Finding
For every integer \(n\ge4\), let \(T(n)=L(K_n)=J(n,2)\) be the triangular graph. Identifying each vertex of \(T(n)\) with one edge of the base complete graph \(K_n\), its **inclusion-minimal forts** are precisely:

1. Edge sets of spanning star forests, where each component is a star with at least two vertices (equivalently, inclusion-minimal edge covers of \(K_n\));
2. Edge sets of simple cycles on \(k\) base vertices, for \(3\le k<n\).

Consequently the exact number of minimal forts is
\[
M_n=n!\,[z^n]\exp\!\left(z(e^z-1)-\frac{z^2}{2}\right)
+\sum_{k=3}^{n-1}\binom nk\frac{(k-1)!}{2}.
\]
The minimum cardinality of a fort is \(r_n=\min\{3,\lceil n/2\rceil\}\). For the standard fort-cover linear programming relaxation of zero forcing, \(Z^*(T(n))=\binom n2/r_n\). In particular, \(Z^*(T(n))=\binom n2/3\) for \(n\ge5\) and \(Z^*(T(4))=3\).

For \(n\ge7\) satisfying \(n\equiv1,3\pmod6\), a Steiner triple system on \(n\) base vertices partitions the edges of \(K_n\) into \(\binom n2/3\) triangle forts, proving
\[\operatorname{ft}(T(n))=\binom n2/3.\]

## Assumptions and scope
All graphs are finite, simple, undirected; \(n\) is an integer at least four. A fort of a graph \(G\) is a nonempty vertex set \(F\) such that every vertex outside \(F\) has either zero or at least two neighbors in \(F\). The qualifier *minimal* means inclusion-minimal, not minimum-cardinality. The fort number \(\operatorname{ft}(G)\) is the maximum number of pairwise vertex-disjoint forts. Fractional zero forcing \(Z^*(G)\) is the minimum \(\sum_{v\in V(G)}x_v\) subject to \(x_v\ge0\) and \(\sum_{v\in F}x_v\ge1\) for every fort \(F\) (equivalently every minimal fort). The coefficient notation extracts the \(n\)-th coefficient of the indicated exponential series.

## Proof
**Fort test.** For an edge set \(F\subseteq E(K_n)\), put \(d_F(u)\) for its degree at the base vertex \(u\). If \(uv\notin F\), the vertex \(uv\) of \(T(n)\) has exactly \(d_F(u)+d_F(v)\) neighbors in \(F\). If no base vertex is isolated in \(F\), this sum is at least two. If an isolated base vertex exists, the fort condition fails exactly when another base vertex has degree one, since the missing edge joining them has exactly one neighbor in \(F\). Hence a nonempty \(F\) is a fort precisely when it is a spanning edge cover, or is nonspanning and every nonisolated base vertex has degree at least two.

**Minimality.** Every spanning edge cover contains an inclusion-minimal edge cover. An edge cover is inclusion-minimal exactly when each edge has an endpoint of degree one, which forces every connected component to be a star with at least one edge. Such a spanning star forest is itself a fort. Removing any edge from it leaves a degree-one base vertex (or an isolated vertex) and cannot produce a nonspanning fort: the remaining forest either has a degree-one vertex together with an isolated vertex, or consists only of isolated vertices, and is nonempty when potentially relevant. More generally, no proper subset of a spanning star forest is a fort: a nonspanning subset that contains a cycle is impossible, and any nonspanning fort must contain a cycle because its nontrivial components have minimum degree at least two.

Every nonspanning fort contains a cycle (all vertices of positive degree have degree at least two), and that cycle is itself a fort since it omits at least one base vertex. A simple nonspanning cycle has no proper fort subset: every proper subset is a forest, is nonspanning, and therefore cannot have all positive degrees at least two. It follows that the two listed classes exhaust precisely all inclusion-minimal forts. In particular, this argument uses the existence of a minimal fort *inside* any fort; the converse inclusion property is false because forts are not an upward-closed family.

**Counting.** For a fixed block of \(j\) labeled base vertices, a star component has exactly one realization at \(j=2\), and exactly \(j\) choices of center at \(j\ge3\). The labeled exponential generating function of allowable components is
\[\frac{z^2}{2}+\sum_{j\ge3}\frac{jz^j}{j!}=z(e^z-1)-\frac{z^2}{2}.\]
By the exponential formula, the number of spanning star forests is \(n![z^n]\exp(z(e^z-1)-z^2/2)\). For each \(k\)-element subset of base vertices, the number of unoriented undirected simple cycles is \((k-1)!/2\). Summing over \(3\le k<n\) proves the stated formula. A star forest covering \(n\) vertices has at least \(\lceil n/2\rceil\) edges, attained by a matching plus one three-vertex star when \(n\) is odd; a nonspanning simple cycle has at least three edges. These prove \(r_n=\min\{3,\lceil n/2\rceil\}\).

**Fractional parameter.** The automorphism group induced by permutations of the \(n\) base vertices acts transitively on the \(N=\binom n2\) vertices of \(T(n)\). Taking \(x_v=1/r_n\) for every vertex is fractionally feasible because every fort contains a minimal fort of size at least \(r_n\); its value is \(N/r_n\). Conversely, fix a fort of size \(r_n\). For any feasible \(x\), sum its constraints over all images of this fort under all base permutations. Transitivity yields \((r_n/N)\sum_vx_v\ge1\). Thus \(Z^*(T(n))=N/r_n\).

**Disjoint packing.** For \(n\ge5\), all forts have size at least three, so \(\operatorname{ft}(T(n))\le N/3\). If \(n\ge7\) and \(n\equiv1,3\pmod6\), a Steiner triple system exists, partitioning \(E(K_n)\) into triangles. Each triangle omits at least one base vertex and so is a fort; these forts are disjoint as vertices of \(T(n)\). Thus the upper bound is reached.

## Verification
The accompanying `verify_triangular.py` constructs \(T(n)\) independently from base edges and directly checks the fort predicate on every vertex subset for \(4\le n\le6\) (\(33,856\) subsets in total). The resulting exact minimal-fort counts are \(11,60,308\), matching the formula. At \(n=7\), the verifier generates all \(1,659\) classified candidate minimal forts and checks their fort property and every proper subset, then checks that each of \(80,000\) reproducibly sampled forts contains a listed minimal fort. Counts and the precise command appear in `VERIFICATION.md`. Computational evidence is finite and is not a substitute for the preceding general proof.

## Relationship to prior work
Cameron, Hogben, Kenter, Mojallal and Schuerger introduced the fort hypergraph, disjoint fort number, and fort-cover fractional zero forcing framework (arXiv:2310.17904; first posted 27 October 2023), proving general results and values for several common families. Becker, Cameron, Hanely, Ong and Previte (arXiv:2404.05963, 2024) developed minimal-fort enumeration for other graph families. Afzali, Ghodrati and Maimani (2024) determined failed zero forcing numbers for Johnson graphs, including the scalar minimum-fort size for \(J(n,2)\); that scalar consequence is not claimed here as new. The new contribution is the **entire inclusion-minimal fort hypergraph of \(J(n,2)\)**, its exact number, the fractional parameter, and a design-theoretic infinite family of equality cases for disjoint fort packing. Steiner triple system existence is classical; it is applied rather than rediscovered.

## Limitations
The classification concerns the triangular Johnson graphs, not all Johnson graphs. The disjoint-fort packing equality is established only for the stated admissible orders; no exact packing assertion is made for other orders. Neither an unexamined full text on Johnson-graph failed forcing nor unindexed literature can be ruled out as a possible equivalent source. A review of the cited sources and mathematical-record queries is not an exhaustive novelty proof. Independent scientific review has not been performed.

## References
1. T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal, H. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904 (first public version 2023-10-27), https://arxiv.org/abs/2310.17904.
2. P. Becker, T. R. Cameron, D. Hanely, B. Ong, J. P. Previte, *On the Number of Minimal Forts of a Graph*, arXiv:2404.05963 (2024), https://arxiv.org/abs/2404.05963.
3. F. Afzali, A. H. Ghodrati, H. R. Maimani, *Failed zero forcing numbers of Kneser graphs, Johnson graphs, and hypercubes*, Journal of Applied Mathematics and Computing 70 (2024), 2665–2675, DOI 10.1007/s12190-024-02064-w.
4. Classical Steiner triple system existence criterion: orders congruent to \(1\) or \(3\) modulo \(6\).
