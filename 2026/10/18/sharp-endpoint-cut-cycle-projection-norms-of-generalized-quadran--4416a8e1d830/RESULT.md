# Sharp endpoint cut–cycle projection norms of generalized-quadrangle incidence graphs

## Finding
For any existing finite generalized quadrangle of order \((q,q)\), where \(q\ge2\) is an integer, let \(G\) be its unweighted point–line incidence graph. Let \(Q\) be the Euclidean orthogonal projection onto the graph cut subspace of the real coordinate edge space and let \(C=I-Q\) project onto cycle flows. Set \(H=(q+1)^2(q^2+1)\). Their exact endpoint operator norms are
\[
\boxed{\|Q\|_{\ell_1(E)\to\ell_1(E)}=\|Q\|_{\ell_\infty(E)\to\ell_\infty(E)}=1+\frac{6q^4}{H}},
\qquad
\boxed{\|C\|_{\ell_1(E)\to\ell_1(E)}=\|C\|_{\ell_\infty(E)\to\ell_\infty(E)}=\frac{8q^4}{H}}.
\]
All edge columns have the same absolute column sum, without an edge-transitivity assumption. The exact identity \(\|Q\|=1+3\|C\|/4\) holds. The cut norm exceeds the cycle norm for \(q=2\), while the cycle norm exceeds the cut norm for every integer \(q\ge3\). Both increase strictly with \(q\) and have sharp suprema \(7\) and \(8\), approached by generalized quadrangles of prime-power order. At \(q=2\) the norms are \(47/15\) and \(128/45\); at \(q=3\) they are \(323/80\) and \(81/20\).

## Assumptions and scope
A finite generalized quadrangle of order \((q,q)\) has \((q+1)(q^2+1)\) points and the same number of lines; each point lies on \(q+1\) lines, each line contains \(q+1\) points, and a nonincident point–line pair determines exactly one shortest length-three incidence path. Its incidence graph is connected, bipartite, \((q+1)\)-regular, of girth \(8\) and diameter \(4\), with
\[
N=2(q+1)(q^2+1)\text{ vertices},\qquad |E|=(q+1)^2(q^2+1)=H.
\]
Fix an arbitrary orientation and write \(D:\mathbb R^E\to\mathbb R^V\) for the signed incidence matrix; put \(L=DD^{\mathsf T}\). The matrices \(Q=D^{\mathsf T}L^+D\) and \(C=I-Q\) are defined using the Moore–Penrose inverse on the vertex subspace orthogonal to constants. They are orthogonal idempotents on \(\ell_2(E)\), and the claim evaluates their norms after equipping the same finite-dimensional edge space with \(\ell_1\) or \(\ell_\infty\) norms. No claim of minimality among all possible projections is made. Existence of the geometry is assumed, not claimed for every integer \(q\); the symplectic examples \(W(3,q)\) exist for prime powers \(q\).

## Proof
**Radial Green kernel.** For a fixed vertex \(r\), the four nontrivial distance shells have cardinalities \(n_1=q+1\), \(n_2=q(q+1)\), \(n_3=q^2(q+1)\) and \(n_4=q^3\), while \(n_0=1\). The incidence graph has no edges within shells. Across shell boundaries the counts are respectively \(m_0=q+1\), \(m_1=q(q+1)\), \(m_2=q^2(q+1)\) and \(m_3=q^3(q+1)\). These are consequences of girth \(8\), diameter \(4\), and the unique-nonincident-path axiom. In particular the uniform shell partition is equitable, so a radial solution to \(L g=\delta_r-\mathbf1/N\) exists. Since \(G\) is connected it is unique after imposing zero mean and equals the column \(L^+\delta_r\).

Write \(g_i=g(w)\) for vertices at distance \(i\) from \(r\) and \(\Delta_i=g_i-g_{i+1}\), for \(0\le i\le3\). Summing the Poisson equation over the first \(i+1\) shells telescopes the edge flux and gives the exact identity
\[
m_i\Delta_i=1-\frac{1}{N}\sum_{j=0}^i n_j.
\]
Consequently, writing \(H=(q+1)^2(q^2+1)\),
\[
(\Delta_0,\Delta_1,\Delta_2,\Delta_3)=\frac{1}{2H}
(2q^3+2q^2+2q+1,\;2q^2+2q+1,\;2q+1,\;1).
\]
All four quantities are positive and strictly decreasing, with successive differences \(q^3/H\), \(q^2/H\), and \(q/H\).

**The flow from an edge.** Fix an oriented edge \(e=(u,v)\). The girth-eight condition makes the radius-three nonbacktracking neighborhoods of \(u\) and \(v\), with \(e\) removed, into disjoint rooted \(q\)-ary trees. Their levels \(i=0,1,2,3\) each have exactly \(q^i\) vertices per side. Together they use \(2(1+q+q^2+q^3)=N\) vertices; thus the two trees exhaust \(V(G)\). By regularity, every level-three vertex has \(q\) unused neighbors, and all such remaining edges run between the opposing level-three sets. Their total is \(q^4\). There can be no earlier cross edge, since it would create a cycle shorter than eight. Therefore \(E\) consists of the original edge, \(2q^{i+1}\) tree edges between levels \(i\) and \(i+1\), for \(i=0,1,2\), and \(q^4\) cross edges at the terminal level.

The edge source \(D\mathbf e=\delta_u-\delta_v\) produces vertex potential \(f=L^+(\delta_u-\delta_v)\). On the \(u\)-side level \(i\), the distance pair to \(u,v\) is \((i,i+1)\), giving \(f=+\Delta_i\); on the \(v\)-side it is \((i+1,i)\), giving \(f=-\Delta_i\). Hence the transfer-current vector \(Q\mathbf e=D^{\mathsf T}f\) has absolute magnitude \(2\Delta_0\) on the original edge, \(\Delta_i-\Delta_{i+1}\) on each of the \(2q^{i+1}\) corresponding tree edges, and \(2\Delta_3\) on each of the \(q^4\) cross edges. Consequently
\[
\begin{aligned}
\|Q\mathbf e\|_1
 &=2\Delta_0+2\sum_{i=0}^2 q^{i+1}(\Delta_i-\Delta_{i+1})+2q^4\Delta_3\\
 &=\frac{2q^3+2q^2+2q+1+7q^4}{H}
 =1+\frac{6q^4}{H}.
\end{aligned}
\]
This is independent of the chosen edge. In addition \(Q_{ee}=2\Delta_0=(2q^3+2q^2+2q+1)/H\in(0,1)\). The complementary column has absolute sum
\[
\|C\mathbf e\|_1=1+\|Q\mathbf e\|_1-2Q_{ee}
=\frac{8q^4}{H}.
\]
The induced \(\ell_1\)-norm of a finite matrix is its maximum absolute column sum. Since \(Q\) and \(C\) are symmetric, their induced \(\ell_\infty\)-norms equal their \(\ell_1\)-norms. These observations prove the exact formulas for every generalized quadrangle in scope, independently of edge transitivity.

**Transition and sharpness.** Subtracting gives
\[
\|C\|-\|Q\|=\frac{q^4-2q^3-2q^2-2q-1}{H}.
\]
It is negative at \(q=2\) and positive at all integers \(q\ge3\) (the numerator is strictly increasing for \(q\ge3\) and positive at \(3\)). As functions of real \(q\ge2\), the derivatives are \(12q^3(q^2+q+2)/((q+1)^3(q^2+1)^2)>0\) for the cut expression and \(16q^3(q^2+q+2)/((q+1)^3(q^2+1)^2)>0\) for the cycle expression. Their exact deficits from the limits are
\[
7-\|Q\|=\frac{6(2q^3+2q^2+2q+1)}{H},\qquad
8-\|C\|=\frac{8(2q^3+2q^2+2q+1)}{H}.
\]
Thus \(7-\|Q\|\sim12/q\) and \(8-\|C\|\sim16/q\). Generalized quadrangles \(W(3,q)\) exist for every prime power \(q\), hence these limits are attained as sharp suprema over an actual unbounded sequence of geometries.

## Verification
The self-contained standard-library-only program `check.py` constructs \(W(3,2)\) and \(W(3,3)\) directly from projective points and totally isotropic symplectic lines. It computes the full incidence-graph Laplacian, inverts a grounded Laplacian exactly over \(\mathbb Q\), and checks the diagonal and absolute column sums of both operators for **every** oriented edge. All \(45\) and \(160\) columns, respectively, passed. Run `python check.py` in the directory containing this file. Finite exact checks support the symbolic proof; the all-order theorem does not depend on exhaustive computation.

## Relationship to prior work
Dilworth, Kutzarova, and Ostrovskii (arXiv:2305.12582, publicly posted 21 May 2023) develop cut/cycle projection constants and study discrete tori and Hamming graphs, not generalized-quadrangle incidence graphs. Schild, Rao, and Srivastava (arXiv:1708.01632) prove general electrical-flow localization bounds rather than these exact norms. Exoo and Jajcay's *Dynamic Cage Survey* records generalized-quadrangle incidence graphs as regular girth-eight Moore cages; it does not evaluate electrical-flow projection norms. Sorgun and Ertaş (doi:10.22061/jdma.2024.10798.1070) study the incidence graph as an octographic graph without the operator-norm calculation. Earlier exact results for symmetric block-design incidence graphs concern the distinct diameter-three/girth-six regime; they neither state nor imply these diameter-four/girth-eight constants without a new current analysis. No identified inspected primary source gives the two formulas or the reversal at order three.

## Limitations
The claim concerns canonical Euclidean orthogonal projections equipped with endpoint coordinate norms; it does not determine minimum norms among all projections, intermediate \(\ell_p\) norms, or nonsymmetric generalized quadrangles of order \((s,t)\). It assumes existence of an order-\((q,q)\) geometry and does not assert existence for every integer \(q\). Originality assessments can miss an equivalent theorem in less well indexed electrical-network literature. Independent scientific validation has not been performed.

## References
1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1 (21 May 2023). https://arxiv.org/abs/2305.12582
2. A. Schild, S. Rao and N. Srivastava, *Localization of Electrical Flows*, arXiv:1708.01632v1 (4 August 2017). https://arxiv.org/abs/1708.01632
3. G. Exoo and R. Jajcay, *Dynamic Cage Survey*, Electronic Journal of Combinatorics 18 (2011), DS16, §2.2.2. https://www.combinatorics.org/files/Surveys/ds16/ds16v2-2011.pdf
4. S. Sorgun and A. G. Ertaş, *A unified approach to the incidence graphs of (weak) generalized quadrangles*, Journal of Discrete Mathematics and Its Applications 9 (2024), 65–72. doi:10.22061/jdma.2024.10798.1070
