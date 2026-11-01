# Layer-exchange fixed spaces of robust clique complexes of graph prisms

## Finding
For a finite simple graph \(H\) on a nonempty vertex set \(V\) and every integer \(k\ge2\), form the Cartesian prism \(G=H\square K_2\) and let \(\sigma(v,a)=(v,1-a)\) exchange its layers. Write
\[
\beta_H(S)=\max\{|T|:T\subseteq S\text{ and }H[T]\text{ is bipartite}\},\qquad
\mathcal B_k(H)=\{S\subseteq V:\beta_H(S)<k\}.
\]
If \(I_k(G)\) is the simplicial complex of vertex subsets that contain no independent \(k\)-set, then there is a canonical piecewise-linear homeomorphism
\[
\boxed{\ |I_k(H\square K_2)|^{\langle\sigma\rangle}\ \cong_{\mathrm{PL}}\ |\mathcal B_k(H)|\ }.
\]
The homeomorphism identifies the vertex \(v\) on the right with the midpoint of the rung edge \([(v,0),(v,1)]\) on the left.

If \(H\) is bipartite and \(m=|V|\), this becomes the \((k-2)\)-skeleton of the simplex on \(m\) vertices. Consequently,
\[
\boxed{\ |I_k(H\square K_2)|^{\langle\sigma\rangle}
\simeq \bigvee^{\binom{m-1}{k-1}}S^{k-2}\ },
\]
with a zero-fold wedge interpreted as a point. In particular, for \(2\le k\le m\), the only nonzero reduced integral homology group is \(\widetilde H_{k-2}\cong\mathbb Z^{\binom{m-1}{k-1}}\), and all its integral homology is torsion-free. For \(k>m\), the fixed locus is a simplex and hence contractible. These statements include disconnected bipartite base graphs.

For the ladder \(H=P_m\), \(m\ge3\), and \(k=3\), the previously established nonequivariant type is \(I_3(P_m\square K_2)\simeq\bigvee^{\binom{m-1}{2}}S^3\) [1], while its geometric fixed locus is \(\bigvee^{\binom{m-1}{2}}S^1\). Thus the reflection saturates the mod-two Smith total-Betti inequality for every ladder length, although the nonzero reduced homology occurs in different degrees. The fixed-space correspondence and its bipartite specialization, not the known ambient sphere count or an already-determined ambient representation, are the new assertions.

## Assumptions and scope
A graph is finite, undirected, and simple. The independent-set convention is \(I_k(G)=\{W\subseteq V(G):\alpha(G[W])<k\}\), with the empty face included. The prism has edges between \((v,0)\) and \((v,1)\), together with \((u,a)(v,a)\) when \(uv\in E(H)\). We take the ordinary geometric realization of the entire finite simplicial complex, and fixed points are **geometric** fixed points, not invariant homology or an orbit-space quotient.

A graph on the empty set is considered bipartite. For the displayed homotopy formula, \(m\ge1\), \(k\ge2\), and \(\binom{m-1}{k-1}=0\) if \(k>m\). When \(k=2\), the wedge-of-zero-spheres convention means a discrete set of \(m\) points. The case \(H=P_m\) uses the path on \(m\) vertices, with \(m\ge3\) only to make the positive first Betti number visible.

## Proof
**Step 1: independent sets in complete rung unions.** For \(S\subseteq V\), let \(R_S=S\times\{0,1\}\). Any independent set \(A\) in \(G[R_S]\) uses at most one end of each rung, because each rung is an edge. If \(T\subseteq S\) denotes the rung indices met by \(A\), the selected layer labels define a proper two-coloring of \(H[T]\): adjacent vertices of \(H[T]\) cannot be assigned the same label, because same-layer horizontal edges would then join the selected prism vertices. Conversely, any bipartite induced subgraph \(H[T]\) admits a proper two-coloring \(c:T\to\{0,1\}\), and \(\{(v,c(v)):v\in T\}\) is independent in the prism. Therefore the exact equality
\[
\boxed{\alpha(G[R_S])=\beta_H(S)}
\]
holds for every graph \(H\) and every \(S\). In particular, the rung union \(R_S\) is a simplex of \(I_k(G)\) precisely when \(S\in\mathcal B_k(H)\).

**Step 2: exact geometric fixed triangulation.** The vertices of \(I_k(G)\) form disjoint two-element orbits \(O_v=\{(v,0),(v,1)\}\) under \(\sigma\), each spanning an edge. In barycentric coordinates, a point fixed by \(\sigma\) has equal coefficients at the two ends of every rung. Its carrier simplex is invariant, so it is a union of complete rung orbits. Conversely, each admissible union of complete orbits has a fixed simplex equal to the convex hull of their midpoints \(b_v=\frac12[(v,0)+(v,1)]\). These midpoint simplices meet along their common faces. By Step 1, their indexing face collection is exactly \(\mathcal B_k(H)\). Sending \(v\) to \(b_v\) therefore gives the claimed canonical piecewise-linear homeomorphism (and no extra invariant-face vertices or fixed points are omitted).

**Step 3: the bipartite specialization.** If \(H\) is bipartite, every induced subgraph \(H[S]\) is bipartite. Hence \(\beta_H(S)=|S|\), and
\[
\mathcal B_k(H)=\{S\subseteq V:|S|\le k-1\},
\]
the full \((k-2)\)-skeleton of an \((m-1)\)-simplex, where it is the full simplex if \(k>m\). For \(2\le k\le m\), put \(r=k-2\). The \(r\)-skeleton of a simplex is \((r-1)\)-connected for \(r\ge1\): any map from a sphere of dimension at most \(r-1\) contracts inside the full simplex, and relative cellular approximation moves the contraction into the \(r\)-skeleton. Its augmented cellular chain complex agrees through dimension \(r\) with the exact augmented chain complex of the full simplex. The only possible nonzero reduced integral homology is thus in degree \(r\); its rank, from the alternating face count, is
\[
\left|\sum_{j=0}^{r+1}(-1)^{j+1}\binom mj\right|=\binom{m-1}{r+1}=\binom{m-1}{k-1}.
\]
There is no torsion, because this top group is the kernel of a homomorphism between free abelian groups. For \(r\ge2\), the Hurewicz and simply connected homology Whitehead theorems identify the complex with a wedge of that many \(r\)-spheres. For \(r=1\), it is the complete graph on \(m\) vertices, whose circle rank is \(\binom{m-1}{2}\); for \(r=0\), it consists of \(m\) points. This proves the complete homotopy classification.

**Step 4: ladder Smith equality.** Filakovský [1, Theorem 1] proves that for the two-row grid \(P_m\square K_2\), \(m\ge2\), its three-robust clique complex has the homotopy type \(\bigvee^{\binom{m-1}{2}}S^3\). Step 3 gives the geometric fixed locus \(\bigvee^{\binom{m-1}{2}}S^1\). Both have mod-two total Betti number \(1+\binom{m-1}{2}\), so the standard Smith inequality is an equality. No equivariant homotopy equivalence between these spaces is asserted.

## Verification
The standalone standard-library program `verify_prism.py` checks the definition of \(I_k(G)\) directly: it enumerates all rung-orbit unions for 20 bipartite base-graph instances (paths, stars, disconnected matchings, even cycles), with \(1\le m\le6\), performing 73 pairs of graph-and-threshold checks. It separately calculates ordinary simplicial mod-two boundary ranks for ladder complexes at \(2\le m\le6\) and \(k=2,3\), matching the known ambient wedge multiplicities in all ten cases. For \(H=K_3\), \(k=3\), it confirms \(\alpha(K_3\square K_2)=2\) and detects failure of the bipartite-skeleton conclusion: the fixed complex contains a triangle. Executing `python3 verify_prism.py` prints `VERIFY_OK ...`.

The exhaustive finite checks test examples only. All-graph and all-parameter statements are proved in Steps 1–3; the ladder Smith equality additionally uses the explicitly cited established ambient homotopy theorem.

## Relationship to prior work
Filakovský [1] introduced the robust-clique terminology and proved sphere-wedge homotopy types for grids and square sequences, including two-row grids. It does **not** state a geometric fixed-point identification under the rung exchange; the present theorem determines that fixed space for arbitrary base graphs, with a universal simplex skeleton for all bipartite bases and all robust thresholds.

Kim and Lew [2] previously defined the same avoidance complex under the notation \(I_k(G)\), and investigated collapsibility and Leray bounds; those results do not identify the prism-layer fixed-point space. Published equivariant Euler-character results [3] compute an alternating homology character for \(I_3(G)\) on connected bipartite graphs; those characters do not determine actual fixed-space PL types. The related all-bipartite three-sphere-wedge result [4] supplies ambient homotopy types but likewise does not give the fixed-space homeomorphism. The computation of the representation of the layer-swap on the ladder's ambient homology is not claimed as a new outcome here.

## Limitations
The skeleton simplification needs a bipartite base graph. For example, when \(H=K_3\) and \(k=3\), the full three-rung union is permitted and the fixed complex is a filled triangle, not a circle. For arbitrary nonbipartite graphs the exact induced-bipartite-subset complex \(\mathcal B_k(H)\) is obtained, but its homotopy type is not classified in general. The Smith-saturation corollary is asserted only for the specified two-row grids at parameter three; there is no assertion of integral equivariant homology representations or equivariant homotopy equivalences. Search coverage cannot exclude unindexed equivalent results. No independent audit has been performed.

## References
1. M. Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first public 2026-02-11, especially Theorem 1 and Definition 9; https://arxiv.org/abs/2602.11365.
2. M. Kim and A. Lew, *Complexes of graphs with bounded independence number*, arXiv:1912.12605, first public 2019-12-29; https://arxiv.org/abs/1912.12605.
3. *Equivariant Euler characters of 3-robust clique complexes of connected bipartite graphs*, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-equivariant-euler-characters-of-3-robust-clique-complexes-of-con--f9d874df12e5 (full RESULT.md inspected).
4. *A three-sphere wedge theorem for robust clique complexes of all connected bipartite graphs*, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-three-sphere-wedge-theorem-for-robust-clique-complexes-of-all--8d06720b1a2b (full RESULT.md inspected).
