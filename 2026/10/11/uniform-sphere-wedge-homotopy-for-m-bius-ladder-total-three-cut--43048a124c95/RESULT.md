# Uniform sphere-wedge homotopy for Möbius-ladder total three-cut complexes

## Finding
For every integer \(n\ge5\), the total three-cut complex of the Möbius ladder has the integral homotopy type
\[
\Delta_3^t(M_{2n})\simeq\bigvee^{1+\binom{n+1}{2}}S^{2n-6}.
\]
Equivalently, the third bounded-independence complex is
\[
BI_3(M_{2n})\simeq\bigvee^{1+\binom{n+1}{2}}S^3.
\]
In particular, the total three-cut complexes for \(n=5,6,7\) are, respectively, wedges of \(16\) four-spheres, \(22\) six-spheres, and \(29\) eight-spheres.

## Assumptions and scope
All graphs are finite, simple, undirected. Write \(V=\mathbb Z/(2n)\), with \(\{i,i+1\}\) for each rim edge (indices modulo \(2n\)) and \(\{i,i+n\}\) for each antipodal spoke. Thus \(M_{2n}\) has \(2n\) vertices, \(3n\) edges, and maximum degree three. For an induced subgraph \(G[U]\), \(\alpha(G[U])\) is its independence number, including \(\alpha(G[\emptyset])=0\). Define
\[
BI_3(G)=\{U\subseteq V(G):\alpha(G[U])<3\},\qquad
\Delta_3^t(G)=\{U\subseteq V(G):\alpha(G[V(G)\setminus U])\ge3\}.
\]
These are Alexander-dual complexes on the specified common vertex set; all (co)homology is integral unless a coefficient field is explicitly named.

## Proof
**1. A two-connectivity lemma.** For every connected graph \(G\), the complex \(K=BI_3(G)\) is two-connected. Choose a spanning tree \(T\). The inclusion \(BI_3(T)\subseteq K\) is simplicial, and both complexes have the same complete one-skeleton because every set of at most two vertices has independence number at most two. The tree subcomplex is contractible: repeatedly remove a leaf \(v\) adjacent to \(u\). Every face containing \(v\) can be enlarged to contain \(u\); otherwise an independent triple after adding \(u\), necessarily consisting of \(u\) and two other vertices, would also be independent before adding \(u\) after replacing \(u\) by the leaf \(v\). Thus \(v\) is dominated by \(u\), and deleting leaves gives a strong collapse onto a vertex. Since the one-skeleta agree, adjoining higher-dimensional cells to the simply connected tree subcomplex does not introduce fundamental-group generators. Hence \(\pi_1(K)=0\).

For any relative two-simplex \(\{a,b,c\}\in K\setminus BI_3(T)\), choose an edge \(ab\) of \(G\) within the triple which is not a tree edge; such an edge exists because every triple in \(BI_3(G)\) contains an edge. Follow the unique tree path from \(c\) towards \(a\) until its first vertex \(c_s\) adjacent in \(T\) to \(a\) or \(b\); write the preceding vertices as \(c=c_0,c_1,\ldots,c_s\). Each four-set \(\{a,b,c_i,c_{i+1}\}\) is a simplex of \(K\): it contains the two disjoint edges \(ab\) and \(c_ic_{i+1}\), so no independent triple. In its boundary relative to \(BI_3(T)\), the faces containing the tree edge \(c_ic_{i+1}\) vanish, and the other two faces differ by replacing \(c_i\) by \(c_{i+1}\). Summing with coherent orientation telescopes from \([a,b,c]\) to \([a,b,c_s]\), which is zero relative to \(BI_3(T)\). Therefore every relative two-chain generator bounds a relative three-chain over the integers. Consequently \(H_2(K,BI_3(T);\mathbb Z)=0\) and hence \(H_2(K;\mathbb Z)=0\). Hurewicz gives \(\pi_2(K)=0\), proving two-connectivity. This argument does not assert contractibility of \(K\).

**2. Dimension and face counts.** For \(n\ge5\), \(M_{2n}\) has no triangles or five-cycles. Indeed, a closed walk of odd length at most five with \(s\) antipodal-spoke steps and \(r\) rim steps would require a signed rim displacement congruent to \(-sn\pmod{2n}\). When \(s\) is even, \(r\) is odd and has absolute displacement less than \(2n\); when \(s\) is odd, \(r\le4<n\), also impossible. In any triangle-free graph, a five-vertex induced subgraph of independence number at most two must be a five-cycle: no vertex has degree at least three (its neighbors would form an independent triple), nor degree at most one (its at least three nonneighbors would need to form a triangle to avoid an independent triple). Thus the induced graph is two-regular on five vertices. By the elementary Ramsey fact \(R(3,3)=6\), no six-set of a triangle-free graph is in \(BI_3\). Hence \(K=BI_3(M_{2n})\) has dimension exactly three.

Write \(f_j\) for its number of \(j\)-faces. Any vertex or pair is a simplex, so \(f_0=2n\), \(f_1=\binom{2n}{2}\). A triple is a simplex exactly when it contains an edge. Count edge–third-vertex incidences and correct for the \(\sum_v\binom{3}{2}=6n\) pairs of incident graph edges (triangles are absent):
\[
f_2=3n(2n-2)-6n=6n(n-2).
\]
A four-set is a simplex precisely when its induced subgraph contains a matching of two disjoint edges. The number of pairs of disjoint graph edges is \(\binom{3n}{2}-6n\). Each four-cycle contributes a second perfect matching to its four vertices and must be counted once rather than twice. There are exactly \(n\) four-cycles: they each consist of a rim edge, its antipodal rim edge, and the two joining spokes. Therefore
\[
f_3=\binom{3n}{2}-7n.
\]
As \(K\) is two-connected and three-dimensional, its only possibly nonzero reduced integral homology is its free top group \(\widetilde H_3(K;\mathbb Z)\). Its rank is the negative reduced Euler characteristic:
\[
-\widetilde\chi(K)=1-2n+\binom{2n}{2}-6n(n-2)+\binom{3n}{2}-7n
=1+\binom{n+1}{2}.
\]
The Hurewicz and homological Whitehead theorems now give \(K\simeq\bigvee^{1+\binom{n+1}{2}}S^3\).

**3. Alexander dual.** On \(2n\) vertices, combinatorial Alexander duality gives
\[
\widetilde H_i(\Delta_3^t(M_{2n});\mathbb Z)
\cong\widetilde H^{2n-i-3}(K;\mathbb Z),
\]
so the only nonzero reduced integral homology group of \(\Delta_3^t\) is free of rank \(1+\binom{n+1}{2}\), in degree \(2n-6\). This dual complex is simply connected because it contains the complete two-skeleton on the \(2n\) vertices. To see this, after removing any three vertices there remain \(2n-3\) vertices. For \(n\ge6\), a graph of maximum degree three has an independent set of size at least \(\lceil(2n-3)/4\rceil\ge3\) by the greedy bound. For \(n=5\), the Möbius ladder is bipartite with five vertices in each color class, so any seven remaining vertices include at least four independent vertices of one class. Therefore every triple is a face of the dual. Since its only reduced integral homology is free in dimension \(2n-6\ge4\), the Hurewicz–Whitehead wedge criterion proves the asserted integral homotopy equivalence.

## Verification
The accompanying standalone `verify.py` generates the graph and simplicial complexes directly from their definitions, without numerical topology libraries. It checks all face counts and exact mod-two homology of \(BI_3(M_{2n})\) for every \(5\le n\le14\). It also constructs explicit spanning-tree relative-chain telescopes for every non-tree two-simplex in that range. A separate direct enumeration computes full simplicial mod-two homology of the *dual* total three-cut complexes at \(n=5,6\). It returns `VERIFY_OK`. Finite checks corroborate but do not replace the uniform proof.

## Relationship to prior work
Carnero Bravo, arXiv:2602.21427, introduces the bounded-independence/total-cut duality and proves contractibility for chordal graphs and simple connectivity for \(BI_3\) of connected graphs (Propositions 15 and 21). Its homotopy classifications treat powers of cycles, complete multipartite graphs, and other classes, not the Möbius ladders treated here. The proof above supplies the additional two-connectivity argument, exact Möbius-ladder face count, and dual-space connectivity needed for the infinite-family result. Agarwal and Basak, arXiv:2608.30601, prove nonequivariant homotopy classifications of independence and perfect-matching complexes of Möbius and circular ladders; their Problem 26 names total-cut homotopy as a future direction. Those complexes do not imply the present total three-cut formula. A separately indexed calculation of the Wagner graph \(M_8\) handles the different parameter \(n=4\), outside the stated range.

## Limitations
The theorem applies only to \(n\ge5\) and to the *total three-cut complex*, not the ordinary three-cut, independent-set, or perfect-matching complex. It computes the nonequivariant integral homotopy type, not symmetry representations or a canonical equivariant equivalence. The finite numerical verification is not an infinite-family proof. Full comparisons cannot rule out unpublished or unindexed equivalent arguments.

## References
- Andrés Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427, first public 2026-02-24; version 3, §§3–5, Proposition 15, Proposition 21, Theorem 8.
- Anshu Agarwal and Biplab Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, first public 2026-08-31; version 2, §6, Problem 26.
- Minki Kim and Alan Lew, *Complexes of graphs with bounded independence number*, arXiv:1912.12605; *Israel Journal of Mathematics* 249 (2022), 83–120 (general collapsibility framework).
- Allen Hatcher, *Algebraic Topology*, Cambridge University Press, 2002 (Hurewicz and Whitehead theorems and Alexander duality background).
