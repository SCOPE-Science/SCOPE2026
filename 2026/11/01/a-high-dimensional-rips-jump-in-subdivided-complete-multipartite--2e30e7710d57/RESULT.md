# A high-dimensional Rips jump in subdivided complete multipartite graphs

## Finding
Let \(k\ge3\) and let \(a_1,\ldots,a_k\) be integers at least \(2\). For the once-subdivided complete multipartite graph \(G=S(K_{a_1,\ldots,a_k})\) with the shortest-path metric on its **vertices**, the entire inclusive Vietoris--Rips homotopy filtration is
\[
K_r\simeq
\begin{cases}
\bigvee^{v+e-1}S^0,&0\le r<1,\\
\bigvee^gS^1,&1\le r<2,\\
(\bigvee^bS^{k-1})\vee(\bigvee^tS^2),&2\le r<3,\\
\bigvee^{bc}S^{k+2},&3\le r<4,\\
\text{point},&r\ge4.
\end{cases}
\]
Here
\[
\begin{aligned}
v&=\sum_{i=1}^k a_i, & e&=\sum_{i<j}a_ia_j, &t&=\sum_{i<j<\ell}a_ia_ja_\ell,\\
g&=e-v+1, & b&=\prod_{i=1}^k(a_i-1), & c&=v-e+t-1.
\end{aligned}
\]
In particular, the **scale-three high-dimensional sphere wedge** has exactly \(bc\) spheres in dimension \(k+2\). The scale-two wedge formula is previously known (Adamaszek's Theorem 5.1) and is included solely to state the full filtration.

All integral homology groups are torsion-free. The reduced persistence barcode over **every coefficient field**, and also in each integral degree as a persistence module, consists of \(v+e-1\) degree-zero intervals \([0,1)\), \(g\) degree-one intervals \([1,2)\), \(t\) degree-two intervals \([2,3)\), \(b\) degree-\(k-1\) intervals \([2,3)\), and \(bc\) degree-\(k+2\) intervals \([3,4)\). When \(k=3\), the two degree-two multiplicities add.

For example, when all three part sizes are \(2\), the scale-two complex is \(\bigvee^9S^2\) and the scale-three complex is \(S^5\). For part sizes \((2,2,3)\), these become \(\bigvee^{14}S^2\) and \(\bigvee^4 S^5\).

## Assumptions and scope
An original vertex of \(H\) remains a vertex of \(G\); the edge \(uv\) of \(H\) is replaced by the two edges \(u-m_{uv}\) and \(m_{uv}-v\), where \(m_{uv}\) is a new midpoint vertex. Every edge of \(G\) has combinatorial length \(1\). The complex \(K_r\) consists of all nonempty subsets of \(V(G)\) having diameter at most \(r\), together with the empty face. It is **not** the Vietoris--Rips complex of the continuously realized metric graph.

Here \(\operatorname{Cl}(Q)\) is the simplicial clique complex of a graph \(Q\); \(L(H)\) is the ordinary line graph whose vertices are the edges of \(H\); \(A*B\) denotes the simplicial join; and a wedge with \(0\) spheres denotes a point. All integers \(k\ge3\) and all sizes \(a_i\ge2\) are covered; the two-part case is excluded from the novelty statement.

## Proof
**1. Exact graph-distance classification and the scale-three join.** For original vertices \(u,w\), their distance in \(G\) is twice their distance in \(H\). Because \(H\) is complete multipartite, distinct original vertices from different parts have distance \(2\), while distinct vertices from the same part have distance \(4\).

For two distinct midpoint vertices \(m_e,m_f\), the distance is \(2\) if the two edges of \(H\) share an endpoint, and \(4\) otherwise: the first statement follows from a path through a shared endpoint, and the second from the bipartition of \(G\) into original and midpoint vertices, which precludes a shorter path and provides a length-four path through an original endpoint of each edge. Finally, for an original vertex \(u\) and midpoint \(m_{vw}\), the distance is \(1\) if \(u\in\{v,w\}\) and is \(3\) otherwise. Indeed, when \(u\) is not an endpoint, it is adjacent in \(H\) to at least one endpoint (every edge of a complete multipartite graph has endpoints in different parts), yielding a three-edge path in \(G\). No shorter odd path exists.

Thus at the inclusive radius \(3\), every original vertex is adjacent to every midpoint vertex in the threshold graph. The graph induced on originals is exactly \(H\), and that induced on midpoints is exactly \(L(H)\). Therefore there is an **equality of simplicial complexes**, not just an abstract homotopy equivalence:
\[
K_3=\operatorname{Cl}(H)*\operatorname{Cl}(L(H)).
\]
The underlying criterion is sharp: for any finite connected simple graph \(F\), this exact join equality for \(S(F)\) holds precisely when each edge \(uv\) of \(F\) dominates all vertices, meaning every other vertex is adjacent to \(u\) or \(v\). Equivalently \(F\) has no induced \(K_2\sqcup K_1\), so its complement has no induced three-vertex path, and \(F\) is complete multipartite. (The equivalence of being induced-three-path-free to being a disjoint union of cliques follows because any connected noncomplete component admits a shortest path between nonadjacent vertices with an induced three-vertex subpath.)

**2. Homotopy type of each join factor.** The clique complex of the complete multipartite graph is the join of the discrete sets \(D_{a_i}\) of the respective part sizes:
\[
\operatorname{Cl}(H)=D_{a_1}*\cdots*D_{a_k}\simeq\bigvee^b S^{k-1},
\qquad b=\prod_i(a_i-1).
\]
This is a consequence of the based join/smash-product identity and \(\widetilde H_0(D_{a_i};\mathbb Z)\cong\mathbb Z^{a_i-1}\); it can also be proved inductively by splitting each discrete set into a chosen base vertex and its remaining isolated vertices. The complex is \((k-2)\)-connected, in particular simply connected.

Adamaszek's general line-graph theorem (2011, Theorem 5.2), independently reproved by Goyal--Shukla--Singh (2020, Lemma 3.2), gives
\[
\operatorname{Cl}(L(H))\simeq\operatorname{Cl}(H)^{(2)},
\]
where the superscript means the two-dimensional skeleton. The latter is connected and simply connected: cells of dimension at least three cannot alter the fundamental group of a complex, and \(\operatorname{Cl}(H)\) is simply connected. It has exactly \(v\) vertices, \(e\) edges and \(t\) triangular faces, so Euler characteristic gives
\[
\widetilde H_2(\operatorname{Cl}(H)^{(2)};\mathbb Z)
\cong\mathbb Z^c,\qquad c=v-e+t-1.
\]
Indeed, the first homology vanishes and the second homology is free as the kernel of an integer cellular boundary into one-chains. Since this is a simply connected two-dimensional CW complex, the Hurewicz theorem and the homological Whitehead theorem yield a homotopy equivalence to a wedge of \(c\) two-spheres. Consequently
\[
\operatorname{Cl}(L(H))\simeq\bigvee^c S^2.
\]
Joining these two factors gives, by \(A*B\simeq\Sigma(A\wedge B)\) for based connected CW complexes,
\[
K_3\simeq (\bigvee^b S^{k-1})*(\bigvee^c S^2)
\simeq\bigvee^{bc}S^{k+2}.
\]
The integer \(c\) is positive: choosing two vertices from each of any three parts produces an octahedral two-sphere as a subcomplex of the two-skeleton. Its oriented fundamental cycle is a nonzero integral two-cycle and cannot bound in a two-dimensional complex, so \(c\ge1\).

**3. Other radii and persistence.** At radius \(0\) the complex is a discrete set of \(v+e\) vertices. At radius \(1\) it is exactly the connected bipartite subdivision graph with \(v+e\) vertices and \(2e\) edges, so it has cycle rank \(2e-(v+e)+1=e-v+1=g\). At radius \(2\), Adamaszek's already published Theorem 5.1 gives
\[
K_2\simeq\operatorname{Cl}(H)\vee\bigvee^t S^2
\simeq(\bigvee^b S^{k-1})\vee(\bigvee^t S^2).
\]
Every pair of vertices of \(G\) is at distance at most \(4\), as shown in step 1; hence \(K_4\) is the full simplex. All possible distances are integers, so these are all filtration stages. The only positive-degree nontrivial groups at successive stages occur in disjoint degrees: degree one at radius \(1\), degrees two and \(k-1\) at radius \(2\), and degree \(k+2\) at radius \(3\). Therefore the persistence maps between distinct stages vanish in positive degrees, giving the asserted complete integral and all-field barcodes. Zero-degree bars die at the first connecting threshold. This also proves torsion-freeness throughout.

## Verification
The bundled `verify.py` independently constructs shortest-path distances by breadth-first search for several boundary cases and three configurations with at least three parts, enumerates every face at scales \(1,2,3\), checks the exact three-scale adjacency taxonomy, and performs exhaustive mod-two boundary-rank calculations whenever the face count is below \(6,500\). Computed results include \((2,2,2)\): \(K_2\) has mod-two second Betti number \(9\), \(K_3\) has mod-two fifth Betti number \(1\); and \((2,2,3)\): these Betti numbers are \(14\) and \(4\), respectively. For \((2,2,2,2)\), the radius-three complex has \(41,552\) nonempty simplices and the script verifies its metric taxonomy and face census, but does **not** compute its full radius-three boundary ranks. The full theorem rests on the symbolic join and skeleton proof, not on extrapolation from these finite cases. See `verification_output.txt` for the actual finite output.

## Relationship to prior work
Adamaszek (2011, Sections 5.1--5.2) already determines \(\operatorname{Cl}(S(H)^2)\simeq\operatorname{Cl}(H)\vee\bigvee^{t(H)}S^2\) for **arbitrary graphs**, and establishes \(\operatorname{Cl}(L(H))\simeq\operatorname{Cl}(H)^{(2)}\). Neither is claimed as new. His Section 5 compares radius two with the **subcomplex** of the join and does not establish the radius-three exact equality for complete multipartite graphs or the resulting high-dimensional filtration.

Goyal, Shukla and Singh (2020, Theorem 3.9 and Proposition 3.8) determine the line-graph clique complex of complete multipartite graphs, but do not analyze Vietoris--Rips graph powers or their subdivision graphs. Combining their result with the present sharp exact-join criterion gives the radius-three answer, which is not their stated theorem.

A published result for the once-subdivided complete graph treats the distinct all-singleton-part case and shows radius three is contractible; that case has \(b=0\) and does not imply the noncontractible \(k\ge3,a_i\ge2\) family here. A separate published Tutte--Coxeter calculation treats a different incidence graph. Previously studied two-part bipartite subdivision cases and their three-dimensional sphere wedges are excluded from the new claim. The new assertions are the exact radius-three factorization, its high-dimensional homotopy result for multipartite parts of size at least two, and their barcode consequences.

## Limitations
This is the finite **vertex-metric** inclusive Vietoris--Rips filtration of a graph subdivided exactly once; neither continuous metric realizations nor weighted, repeated, or partial subdivisions are addressed. No equivariant representation decomposition or persistent homotopy-module calculation is asserted. Novelty is qualified by comparison with the primary sources and indexed records inspected; an equivalent result under unusual graph-power terminology may still exist. Independent mathematical audit has not been performed.

## References
1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first publicly posted 2011-04-03, Section 5, Theorems 5.1 and 5.2. https://arxiv.org/abs/1104.0433.
2. S. Goyal, S. Shukla and A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130, first publicly posted 2020-09-25, Section 3, Lemma 3.2, Proposition 3.8 and Theorem 3.9. https://arxiv.org/abs/2009.12130.
