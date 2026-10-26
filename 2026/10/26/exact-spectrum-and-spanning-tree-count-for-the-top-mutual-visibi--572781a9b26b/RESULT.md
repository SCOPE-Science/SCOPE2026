# Exact spectrum and spanning-tree count for the top mutual-visibility layer of \(K_{m,m,m}\)

## Finding

**Theorem.** For each integer \(m\ge4\), let \(G_m=K_{m,m,m}\) with three distinguished parts \(A,B,C\), each of size \(m\), and let \(H_m=\mathcal R_{\mathcal M}^{3m-2}(G_m)\) denote its fixed-cardinality mutual-visibility reconfiguration graph under token sliding. Then

\[
\mu(G_m)=3m-2,\qquad |V(H_m)|=3m^2,\qquad \deg_{H_m}(v)=2m\quad(v\in V(H_m)).
\]

The graph \(H_m\) is connected and its complete adjacency spectrum, with superscripts indicating **multiplicity**, is

\[
\operatorname{Spec}_{A}(H_m)=\left\{(2m)^{[1]},\ m^{[3(m-1)]},\ (-m)^{[3m-1]},\ 0^{[3(m-1)^2]}\right\}.
\]

Consequently, its algebraic connectivity is \(m\), its Laplacian spectrum is

\[
\left\{0^{[1]},\ m^{[3(m-1)]},\ (3m)^{[3m-1]},\ (2m)^{[3(m-1)^2]}\right\},
\]

and its exact number of spanning trees is

\[
\boxed{\tau(H_m)=\frac{m^{3(m-1)}(3m)^{3m-1}(2m)^{3(m-1)^2}}{3m^2}.}
\]

It has exactly \(3m^3\) edges and \(m^3\) triangles.

## Assumptions and scope

All graphs are finite, simple, and undirected. A set \(S\subseteq V(G)\) is **mutually visible** when every two vertices of \(S\) admit a shortest path whose internal vertices lie outside \(S\). The maximum possible cardinality is \(\mu(G)\). Vertices of \(\mathcal R_{\mathcal M}^k(G)\) are mutually-visible subsets of cardinality \(k\); two distinct subsets are adjacent precisely if their symmetric difference is \(\{x,y\}\), where \(xy\) is an edge of \(G\). The condition \(m\ge4\) is essential to the stated hole-pair classification: at \(m=3\), two omitted vertices may lie in the same part without destroying feasibility.

## Proof

**1. Maximum configurations.** In \(G_m\), vertices in different parts are adjacent. Vertices in the same part are at distance two, and their geodesics have an intermediate vertex in another part. Thus \(S\) is mutually visible exactly when, for every part containing at least two selected vertices, at least one vertex outside that part is missing from \(S\). Omitting at most one vertex violates this condition in its own part, since \(m\ge4\). With exactly two omitted vertices in different parts, the condition holds for every part; with two omitted vertices in the same part, at least two vertices remain selected in that part but no vertex outside it is omitted. Therefore \(\mu(G_m)=3m-2\) and maximum sets are exactly complements of pairs \(\{u,v\}\) whose elements lie in distinct parts. There are \(3m^2\) such pairs.

**2. Adjacent configurations.** Identify a configuration with its two missing vertices; this is an edge of \(G_m\). A legal token slide replaces one of the two missing vertices by a vertex adjacent to it, keeping the other missing vertex. The new missing pair must still cross parts. From a missing pair \(\{a,b\}\) with \(a\in A\), \(b\in B\), the new missing pair is \(\{a,c\}\) or \(\{b,c\}\), where \(c\) ranges over all \(m\) vertices of \(C\). All these choices are legal and exhaust the neighbors. Cyclic symmetry covers the other pair types, so the degree is \(2m\) and the number of edges is \(3m^3\). The three edges \(ab,ac,bc\) of every host triangle form one triangle of \(H_m\); any triangle in the latter must use each of the three distinct pair types and hence is of this form. Thus the triangle count is \(m^3\).

**3. Exact spectral decomposition.** Write the real coordinate space of the layer as

\[
U=(\mathbb R^{A}\otimes\mathbb R^{B})\oplus(\mathbb R^{A}\otimes\mathbb R^{C})\oplus(\mathbb R^{B}\otimes\mathbb R^{C}).
\]

For each part \(X\), split \(\mathbb R^{X}=\langle\mathbf1_X\rangle\oplus W_X\), where \(W_X\) is the \((m-1)\)-dimensional zero-sum subspace. By Step 2, the adjacency operator \(T\) sends functions on one pair block to the other two blocks by summing over the coordinate that is replaced. This gives an invariant orthogonal splitting as follows.

(a) The three-dimensional sector of functions constant on each block is acted on by \(m(J_3-I_3)\). Its eigenvalues are \(2m\) once and \(-m\) twice.

(b) For each \(X\in\{A,B,C\}\), a vector of \(W_X\) occurs, independently, in the two pair blocks containing \(X\). On these two copies the operator is
\[
\begin{pmatrix}0&m\\m&0\end{pmatrix}\otimes I_{W_X}.
\]
It contributes eigenvalues \(+m\) and \(-m\), each with multiplicity \(m-1\) for each of three parts.

(c) Each two-zero-sum tensor space \(W_X\otimes W_Y\) in its pair block is killed by every summation map. Together these three spaces contribute eigenvalue zero with multiplicity \(3(m-1)^2\).

The sector dimensions add to \(3+6(m-1)+3(m-1)^2=3m^2\), so no eigenspaces are missing. Combining the contributions yields precisely the stated adjacency spectrum. The degree eigenvalue \(2m\) is simple; in any finite regular graph its multiplicity equals the number of connected components, hence \(H_m\) is connected.

**4. Tree complexity.** Because \(H_m\) is \(2m\)-regular, its Laplacian is \(L=2mI-T\). The positive Laplacian eigenvalues are \(m\) with multiplicity \(3(m-1)\), \(3m\) with multiplicity \(3m-1\), and \(2m\) with multiplicity \(3(m-1)^2\). Kirchhoff's matrix-tree theorem divides their product by \(|V(H_m)|=3m^2\), producing the displayed exact integer formula. This completes the proof. \(\square\)

## Verification

The standalone standard-library script `verify.py` reconstructs each maximum layer from the original shortest-path feasibility condition, rather than assuming the hole-pair characterization. For \(m=4,5,6\), it checks vertex/edge/triangle counts, degrees, connectedness, and the matrix identity \(T(T^2-m^2I)(T-2mI)=0\). Coupled with exact traces and connectedness, that identity independently forces the listed four eigenvalues with their multiplicities. For \(m=4,5\), it also independently computes two modular principal Laplacian determinants and compares them with the asserted tree formula. All tests return `VERIFY_OK`. These finite tests do not replace the infinite eigenspace proof.

## Relationship to prior work

Fresán-Figueroa, Goldfeder, and Lozano-Piña (arXiv:2610.24324v1, first posted 16 October 2026) define this mutual-visibility reconfiguration model. Their Section 4 proves that for balanced complete bipartite graphs with both part sizes at least four, the maximum layer consists solely of isolated vertices, and Section 7 summarizes that contrast. The current theorem concerns three equal nontrivial parts: adding the third part yields a connected regular maximum layer whose full spectrum and spanning-tree count are determined. Their inspected Sections 2, 4, and 7 neither state nor imply these spectral formulas. Generic token-graph connectivity results do not directly settle this **feasibility-restricted** induced layer. Alternative formulations as an edge-triangle adjacency graph, a constrained two-hole token graph, or a three-block summation operator were considered in the novelty comparison; no matching formula was located in the checked sources.

## Limitations

The formula is for three equal parts of size at least four, not arbitrary complete multipartite graphs or smaller parts. This is a proven theorem with a self-contained linear-algebraic proof and finite consistency checks; historical priority has not been independently certified. Existing general work on token graphs or triangle-based edge graphs could contain an equivalent spectral result not found in the inspected literature. No assertion is made about the full reconfiguration graph beyond its maximum layer.

## References

1. J. A. Fresán-Figueroa, I. A. Goldfeder, and A. Lozano-Piña, *Reconfiguration graphs of mutual-visibility sets*, arXiv:2610.24324v1 (2026-10-16), https://arxiv.org/html/2610.24324v1.
2. R. Fabila-Monroy, D. Flores-Peñaloza, C. Huemer, F. Hurtado, J. Urrutia, and D. R. Wood, *Token graphs*, Graphs and Combinatorics 28 (2012), 365–380. DOI:10.1007/s00373-011-1055-9. (General token-graph background.)
3. G. Kirchhoff, *Über die Auflösung der Gleichungen, auf welche man bei der Untersuchung der linearen Vertheilung galvanischer Ströme geführt wird*, Annalen der Physik und Chemie 72 (1847), 497–508. (Classical matrix-tree theorem.)
