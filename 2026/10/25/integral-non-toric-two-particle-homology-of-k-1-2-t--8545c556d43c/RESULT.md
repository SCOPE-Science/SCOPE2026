# Integral non-toric two-particle homology of \(K_{1,2,t}\)

## Finding
For every integer \(t\ge4\), let \(G_t=K_{1,2,t}\), let \(X_t=\operatorname{UConf}_2(|G_t|)\) be the space of unordered configurations of two distinct particles on its geometric realization, and let
\[
B_t:\mathbb Z^{\binom{t}{2}}\longrightarrow\mathbb Z^t,\qquad B_t(e_{\{i,j\}})=e_i+e_j
\]
be the unsigned incidence map of the complete graph on the last \(t\) vertices. The full graph automorphism group is \(S_2\times S_t\). There is an explicitly defined integral equivariant isomorphism
\[
\boxed{H_2(X_t;\mathbb Z)\cong_{\mathbb Z[S_2\times S_t]}\operatorname{sgn}_{S_2}\boxtimes\ker B_t.}
\]
In particular, \(H_2(X_t;\mathbb Z)\cong\mathbb Z^{t(t-3)/2}\); the same formula gives zero at \(t=3\). Rationally the \(S_t\)-constituent is the irreducible Specht module \(S^{(t-2,2)}\). Although this homology is nonzero for all \(t\ge4\), **no two vertex-disjoint simple cycles exist in \(G_t\)**. Thus none of these top-dimensional classes is a product torus made from a pair of disjoint graph cycles. The contribution is the integral, natural symmetry lattice and its explicit cycles, not the previously available nonequivariant Betti-rank calculation.

## Assumptions and scope
The graph is simple, with vertex parts \(\{v\}\), \(\{a,b\}\), and \(W=\{w_0,\ldots,w_{t-1}\}\). Every pair of vertices in different parts is adjacent. Its edge set is \(\{va,vb,vw_i,aw_i,bw_i:0\le i<t\}\). Orient these edges as \(d_a:v\to a\), \(d_b:v\to b\), \(p_i:v\to w_i\), \(q_i:a\to w_i\), and \(r_i:b\to w_i\). All homology groups in the theorem use integral coefficients. The symmetric group \(S_t\) permutes the subscripts, while the group \(S_2\) exchanges \(a,b\). Their actions are induced by graph automorphisms. Because vertex valencies in the three parts are respectively \(t+2,t+1,3\), these form the entire automorphism group for \(t\ge3\).

For two particles, the unordered Abrams cubical deleted-product model \(D_2(G_t)\) is an equivariant deformation retract of \(X_t\). Indeed, the graph is simple, every path between distinct essential vertices has at least one edge, and each cycle has at least three edges, fulfilling the two-particle subdivision criterion. Its cells are unordered pairs of distinct vertices, pairs of an edge and a nonincident vertex, and pairs of edges with no shared endpoint, in dimensions zero, one, and two respectively. No higher-dimensional cells occur. The numbers of cells are
\[
(c_0,c_1,c_2)=\left(\binom{t+3}{2},(3t+2)(t+1),3t^2-t\right).
\]

## Proof
Orient a two-cell as \(e\wedge f=-f\wedge e\). For oriented edges \(e:x\to y\) and \(f:z\to u\), with disjoint endpoint sets, and an oriented one-cell \((g,w)\) recording one particle in edge \(g\) and the other at vertex \(w\), the cellular boundary is
\[
\partial(e\wedge f)=(f,y)-(f,x)-(e,u)+(e,z).
\]
This identity fixes all signs used below.

**Step 1 (exhaustive two-chain coordinates).** Every integral two-chain has a unique expression
\[
\begin{aligned}
z={}&\sum_i A_i(d_a\wedge r_i)+\sum_i C_i(d_b\wedge q_i)\\
&+\sum_{i\ne j}\bigl(P_{ij}\,p_i\wedge q_j+R_{ij}\,p_i\wedge r_j+T_{ij}\,q_i\wedge r_j\bigr).
\end{aligned}
\]
The displayed terms are all and only the unordered pairs of edges that have disjoint endpoints; their total number is \(2t+3t(t-1)=3t^2-t\).

**Step 2 (solve the integral boundary equations).** Fix an oriented graph edge \(g\). The coefficients of \(\partial z\) along all one-cells \((g,x)\) vanish exactly when the partner-edge coefficients form a circulation in the graph obtained by deleting both endpoints of \(g\). This is an exact integral equivalence, with the incidence signs specified above; it requires no division. For \(g=d_a\) or \(g=d_b\), the partner graph is a star, so \(A_i=C_i=0\) for every \(i\). For \(g=p_i\), each other vertex \(w_j\) forces \(R_{ij}=-P_{ij}\) and the vertex \(a\) forces \(\sum_{j\ne i}P_{ij}=0\). For \(g=q_j\), each \(w_i\) with \(i\ne j\) forces \(T_{ji}=P_{ij}\). For \(g=r_j\), the analogous equation forces \(T_{ij}=P_{ij}\); applying the former equation with interchanged indices gives \(P_{ij}=P_{ji}\). All remaining incidence equations then follow from symmetry and the zero row sums. Conversely, these conditions make every incidence equation vanish. Thus
\[
\partial z=0\quad\Longleftrightarrow\quad
\begin{cases}
A_i=C_i=0,\\
R_{ij}=-P_{ij},\quad T_{ij}=P_{ij},\\
P_{ij}=P_{ji},\quad P_{ii}=0,\\
\sum_{j\ne i}P_{ij}=0 \text{ for all }i.
\end{cases}
\]
There is no degree-three chain group, so \(H_2(X_t;\mathbb Z)=\ker\partial_2\) as an *integral sublattice* of the free two-chain group.

**Step 3 (equivariant identification).** Associate to such a symmetric zero-diagonal integer matrix \(P\) the geometric cellular cycle
\[
\boxed{z(P)=\sum_{i\ne j}P_{ij}\left(p_i\wedge q_j-p_i\wedge r_j+q_i\wedge r_j\right).}
\]
Its coordinate on \(p_i\wedge q_j\) is exactly \(P_{ij}\), so the construction is injective and Step 2 proves surjectivity onto the full integral cycle group. Regard \(P\) as a vector with one coordinate per unordered edge \(\{i,j\}\) of a complete graph. The equations \(\sum_{j\ne i}P_{ij}=0\) are precisely \(B_tP=0\). Therefore \(P\mapsto[z(P)]\) is an integral lattice isomorphism, without passing to rational coefficients or saturating a subgroup.

A permutation of the \(w_i\) carries \(z(P)\) to the cycle obtained by permuting rows and columns of \(P\). Exchanging \(a,b\) sends \(q_i\leftrightarrow r_i\) and changes \(z(P)\) to \(-z(P)\) (the symmetry \(P_{ij}=P_{ji}\) removes the apparent index reversal in the last term). This proves the claimed integral \(S_2\times S_t\)-equivariance.

**Step 4 (rank, first occurrence, and geometry).** For \(t\ge3\), the columns \(e_i+e_j\) of \(B_t\) span \(\mathbb Q^t\), since a row functional vanishing on all columns satisfies \(y_i+y_j=0\) for all pairs, and any three indices force \(y_i=0\). Hence \(\ker B_t\) is free abelian of rank \(\binom t2-t=t(t-3)/2\). For \(t=4\), the nonzero matrix \(P\) with \(P_{01}=P_{23}=1\), \(P_{12}=P_{30}=-1\), and all other entries zero supplies an explicit nonzero class; it embeds by zero extension for all larger \(t\). The rational decomposition of the two-subset permutation module \(\mathbb Q^{\binom t2}\cong\mathbf1\oplus S^{(t-1,1)}\oplus S^{(t-2,2)}\), together with the surjective incidence map onto \(\mathbb Q^t\cong\mathbf1\oplus S^{(t-1,1)}\), identifies the kernel as \(S^{(t-2,2)}\).

Finally, each edge of \(G_t\) has at least one endpoint in the three-element vertex set \(\{v,a,b\}\), whose complement \(W\) is independent. Every simple cycle therefore contains at least two vertices of that three-element set. Two disjoint cycles would require at least four such vertices, which is impossible. This proves the asserted absence of disjoint-cycle product-torus representatives, without claiming that **all** maps from tori to the configuration space are homologically trivial.

## Verification
The accompanying standalone `verify.py` reconstructs the entire two-dimensional cubical chain complex and uses the stated boundary formula, not a saved matrix. For \(3\le t\le8\), exact integer boundaries of explicit quadrilateral matrices vanish, the rank of \(\partial_2\) over \(\mathbb F_{101}\) equals \(3t^2-t-t(t-3)/2\), and the rank over \(\mathbb F_2\) is one smaller. For \(4\le t\le8\), all ordered-index quadrilateral test cycles attached to four-element subsets are checked under adjacent transpositions in \(S_t\) and the nontrivial \(S_2\) element. These computations corroborate the algebraic proof; they do not extrapolate finite ranks to infinite \(t\). Run `python verify.py` with Python 3 and no extra dependencies.

## Relationship to prior work
Barnett–Farber (arXiv:0903.2180v1) develop graph two-point configuration models and intersection theory, obtaining their main explicit descriptions for **ordered** configurations on planar graphs. Ko–Park (arXiv:1101.2648v1, Theorem 3.16 and Corollary 3.17) already determine the first homology and ordinary second Betti number for unordered two-point graph configurations, so the bare rank in Step 4 is **not** claimed as new. Their cited statements do not give the integral \(S_2\times S_t\) lattice or the explicit full two-cycle coordinate parameterization here.

An–Knudsen (arXiv:2008.10371v2) establish geometric generators of degree-two homology for planar graphs, pose a nonplanar extension problem, and exhibit a different nonplanar graph with non-toric degree-two classes in Example 6.8. Therefore non-toric classes as a general phenomenon are already known; the specific infinite fan-graph family and exact integral symmetry-lattice classification are the proposed contribution. Ramos–Yun (arXiv:2606.13813v1) discuss stable **rational** homology representations for several different graph families, including a balanced tripartite family; their abstract does not resolve the present integral unbalanced-family theorem.

## Limitations
The theorem is specifically for two unordered particles on \(K_{1,2,t}\), not for arbitrary complete tripartite graphs or higher particle numbers. Although no classes arise from pairs of disjoint graph-cycle tori, other torus mappings or other natural geometric constructions are not excluded. The nonequivariant rank and the existence of non-toric graph-configuration classes have precedents; neither is asserted to be novel alone. Originality rests on the explicit integral module and uniform cycle coordinates. Publication priority cannot be established solely from indexed searches: relevant less-indexed literature may contain equivalent statements, and the 2026 stable-representation paper could be inspected only at abstract level. All computations are exact for the stated finite test ranges; the infinite-family proof is the integral chain argument above.

## References
- Kathryn Barnett and Michael Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, arXiv:0903.2180v1, first posted 2009-03-12, https://arxiv.org/abs/0903.2180.
- Ki Hyoung Ko and Hyo Won Park, *Characteristics of graph braid groups*, arXiv:1101.2648v1, first posted 2011-01-13; specifically Theorem 3.16 and Corollary 3.17, https://arxiv.org/abs/1101.2648.
- Byung Hee An and Ben Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371v2, §1 and Example 6.8, https://arxiv.org/abs/2008.10371.
- Eric Ramos and Claudia He Yun, *Computing stable homology representations of graph configuration spaces*, arXiv:2606.13813v1, 2026, https://arxiv.org/abs/2606.13813.
