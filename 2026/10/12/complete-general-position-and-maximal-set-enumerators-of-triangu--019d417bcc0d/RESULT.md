# Complete general-position and maximal-set enumerators of triangular graphs

## Finding
Let \(T_n=L(K_n)\) be the triangular graph on the edges of the complete graph with labeled vertex set \([n]\). A subset \(S\) of vertices of \(T_n\) is in **general position** when no three distinct vertices in \(S\) lie on a shortest path, and it is **maximal** when no single vertex can be added while preserving general position. Define
\[
 A_n(z)=\sum_{S\text{ general position in }T_n}z^{|S|},\qquad
 M_n(z)=\sum_{S\text{ inclusion-maximal general position in }T_n}z^{|S|}.
\]
Then, as identities of formal power series in \(u\) with polynomial coefficients in \(z\),
\[
\boxed{\sum_{n\geq0} A_n(z)\frac{u^n}{n!}=
\exp\!\left(ue^{zu}-\frac{zu^2}{2}+\frac{z^3u^3}{6}\right),}
\]
and
\[
\boxed{\sum_{n\geq0} M_n(z)\frac{u^n}{n!}=
\exp\!\left(\frac{zu^2}{2}+\frac{z^3u^3}{6}
+u\left(e^{zu}-1-zu-\frac{z^2u^2}{2}\right)\right)
+u\exp\!\left(\frac{z^3u^3}{6}\right).}
\]
In particular, for even \(n\geq2\), the coefficient of the least nonzero power of \(M_n\) is
\[ [z^{n/2}]M_n(z)=\frac{n!}{2^{n/2}(n/2)!}.\]
For odd \(n\geq5\), it is
\[
[z^{(n+3)/2}]M_n(z)=
\frac{n!}{6\,2^{(n-3)/2}((n-3)/2)!}+
\frac{n!}{24\,2^{(n-5)/2}((n-5)/2)!}.
\]
For \(n=3\), the sole maximal set consists of all three edges, so \(M_3(z)=z^3\). When \(3\mid n\) and \(n\geq3\), the coefficient of the greatest degree is
\[
[z^n]M_n(z)=\frac{n!}{6^{n/3}(n/3)!}.
\]
The two complete polynomials are related by a common labeled component decomposition. They give, respectively, the full size profiles of retained vertex sets whose complements delete to a cluster graph and of inclusion-minimal cluster-vertex deletion sets in \(T_n\).

## Assumptions and scope
Every graph is finite, undirected, and simple; \(n\geq2\) for the graph statements. The conventional auxiliary coefficients \(A_0=M_0=A_1=M_1=1\) extend the exponential generating functions to all \(n\geq0\). General-position maximality means **inclusion-maximality**, not maximum cardinality. A star on \(k\) vertices includes \(k-1\) edges; a star on two vertices is just an edge. Every selected vertex of \(T_n\) is an edge of \(K_n\), so the exponents of \(z\) count selected edges, not the number of underlying vertices.

## Proof
For \(n\geq3\), \(T_n\) has diameter at most two (equal to two when \(n\geq4\)); hence a selected triple lies on a geodesic precisely when the selected induced subgraph contains an induced path on three vertices. Thus the selected vertices are in general position exactly when they induce a disjoint union of cliques in \(T_n\). Equivalently, their underlying selected edges \(F\subseteq E(K_n)\) have the property that every two edges of any edge-intersection component meet one another.

Every pairwise-intersecting family of distinct edges of a simple graph is either a star (all edges share a fixed endpoint) or the three edges of a triangle: after \(ab\) and \(ac\), any edge avoiding \(a\) must be \(bc\), and then no fourth edge may be added. Moreover, distinct components of the edge-intersection graph have disjoint supports in \([n]\). Consequently \(F\) is uniquely a labeled set partition of \([n]\) into blocks that are isolated vertices, stars, or triangles. For a block of size \(k\): an isolated vertex (\(k=1\)) has weight 1; a \(k=2\) block has one edge set of weight \(z\); a \(k=3\) block has three possible two-edge stars of weight \(z^2\), and one triangle of weight \(z^3\); a \(k\geq4\) block has \(k\) possible stars of weight \(z^{k-1}\). These are all possibilities and are counted uniquely.

The labeled exponential formula gives the first identity. Indeed, the block generating function is
\[
u+\frac{zu^2}{2}+\frac{(3z^2+z^3)u^3}{6}+
\sum_{k\geq4}\frac{kz^{k-1}u^k}{k!}
=ue^{zu}-\frac{zu^2}{2}+\frac{z^3u^3}{6}.
\]

To characterize maximality, note first that a selected two-edge star on three vertices can be completed to a triangle by adding its missing edge; therefore no maximal configuration contains such a block. If any star component exists and any underlying vertex is isolated, attaching that isolated vertex to the star center produces a strict general-position extension. If there are no star components but at least two isolated vertices, joining two of them also produces an extension. Conversely, if there are no isolated vertices and every component is a star with one or at least three edges or a triangle, no additional edge is legal: adding an internal edge to a star on at least four vertices destroys the star/triangle classification, and adding an edge between two components merges them into a non-star, non-triangle component. The same argument shows that disjoint triangles with precisely one isolated underlying vertex form maximal configurations. These are the only maximal configurations.

Thus maximal configurations are of two disjoint types: spanning block partitions comprising two-vertex edge-stars, triangles, and stars on at least four vertices, or triangles together with exactly one isolated vertex. The exponential formula and the independent distinguished isolated vertex give the second identity. The spanning block series is
\[
\frac{zu^2}{2}+\frac{z^3u^3}{6}+
\sum_{k\geq4}\frac{kz^{k-1}u^k}{k!}
=\frac{zu^2}{2}+\frac{z^3u^3}{6}+u(e^{zu}-1-zu-z^2u^2/2).
\]

The least-degree coefficient for even \(n\) comes only from a partition into \(n/2\) pair blocks. For odd \(n\geq5\), minimum cardinality \((n+3)/2\) occurs exactly for a triangle together with \((n-3)/2\) pair blocks, or a five-vertex star together with \((n-5)/2\) pair blocks. Counting labeled blocks produces the two stated summands: choose the triangle (respectively, five-vertex block), choose its center in the latter case, and pair the other vertices. For \(3\mid n\), a selected-edge count of \(n\) can be attained only by triangle blocks, because a star loses one edge relative to its support size; counting partitions of \([n]\) into triples yields \(n!/(6^{n/3}(n/3)!)\). These arguments cover the boundaries explicitly.

## Verification
The accompanying `verify.py` computes exact coefficients from independent labeled-block recurrences. It also independently enumerates all subsets of the \(\binom n2\) vertices of \(T_n\), testing forbidden induced three-vertex paths and maximality by all single-vertex additions, for every \(2\leq n\leq6\). All coefficients of both families agree on these orders. A further exact recurrence checks the already established extremal cardinalities for \(3\leq n\leq49\). Run `python3 verify.py` with Python 3 and no nonstandard dependencies. The arbitrary-order statements are proved combinatorially above; the finite checks are not substitutes for that proof.

## Relationship to prior work
Cluster Vertex Deletion and its induced-path characterization were established before 2016 [1]. General-position sets in diameter-two graphs are characterized through induced clique unions, and the largest cardinality for \(L(K_n)\) was computed in [2]. The classification underlying maximal general-position sets and the smallest possible maximal size was explicitly used in [3]; **those statements are prior work, not new classification claims here**. The general-position polynomial as an enumerative invariant and results on other graph families are in [4]. The evaluated, parameter-uniform complete labeled size enumerators above (including maximal sets), and the accompanying precise extremal multiplicities, are the contribution addressed here. They refine earlier cardinality and structural descriptions; any older exact enumeration under different terminology remains an originality risk.

## Limitations
No novelty claim is made for the underlying diameter-two clique-union characterization, the general shape of maximal sets, or their smallest/largest cardinalities. The main contribution is the evaluated generating functions and size multiplicities. The formulas count labeled vertex subsets, not isomorphism types of graph decompositions; the \(n=0,1\) coefficients are generating-function conventions. This is not an independent mathematical certification. An equivalent unpublished or poorly indexed enumerator may exist, especially given earlier complete structural characterizations.

## References
1. Boral, Cygan, Kociumaka, and Pilipczuk, *Fast branching algorithm for Cluster Vertex Deletion*, arXiv:1306.3877v1, 17 June 2013. https://arxiv.org/abs/1306.3877
2. Ghorbani, Klavžar, Maimani, Momeni, Mahid, and Rus, *The general position problem on Kneser graphs and on some graph operations*, arXiv:1903.04286, Section 4.2. https://arxiv.org/abs/1903.04286
3. Di Stefano et al., *Lower General Position Sets in Graphs*, arXiv:2306.09965, Theorem 5.2. https://arxiv.org/abs/2306.09965
4. Iršič, Klavžar, Rus, and Tuite, *General Position Polynomials*, Results in Mathematics 79 (2024), article 110. https://doi.org/10.1007/s00025-024-02133-3
