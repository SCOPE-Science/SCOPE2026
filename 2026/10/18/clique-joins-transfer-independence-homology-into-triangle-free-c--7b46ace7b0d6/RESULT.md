# Clique joins transfer independence homology into triangle-free complexes with universal free loops

## Finding

Let \(H\) be a finite nonempty triangle-free simple graph for which the independence complex \(I=\operatorname{Ind}(H)\) is nonempty and path-connected, and let \(m\ge2\). Form the graph join \(G=K_m\vee H\). Define \(X=\operatorname{CF}_3(G)\) as the simplicial complex of vertex subsets inducing no triangle of \(G\). Then

\[
 X\simeq\left(\bigvee^{\binom m2}S^1\right)\vee\left(\bigvee_{j=1}^{m}\Sigma|I|\right),
 \qquad \pi_1(X)\cong F_{\binom m2}.
\]

Here \(\Sigma\) is the unreduced suspension and \(F_b\) is the free group on \(b\) generators. There is also a canonical action of \(S_m\times\operatorname{Aut}(H)\), preserving the two vertex classes. As **integral representations** of this group,

\[
 H_1(X;\mathbb Z)\cong\bigwedge^2\mathbb Z^m,
 \qquad
 \widetilde H_d(X;\mathbb Z)\cong
 \mathbb Z^m\otimes_{\mathbb Z}\widetilde H_{d-1}(I;\mathbb Z)
 \quad(d\ge2).
\]

The first \(\mathbb Z^m\) in the higher-degree formula is the vertex-permutation module for \(S_m\); the second factor is the natural \(\operatorname{Aut}(H)\)-module, so the formula retains any integral torsion of \(I\) rather than presuming a sphere wedge. The exterior square is formed from the same permutation module and is trivial under \(\operatorname{Aut}(H)\).

For the natural cycle family \(H=C_n\), \(n\ge5\), the classical independence-complex classification gives an explicit mixed-dimensional specialization:

\[
 \operatorname{CF}_3(K_m\vee C_n)\simeq
 \left(\bigvee^{\binom m2}S^1\right)\vee
 \begin{cases}
 \bigvee^{2m}S^{q},&n=3q,\\
 \bigvee^{m}S^{q},&n=3q+1,\\
 \bigvee^{m}S^{q+1},&n=3q+2.
 \end{cases}
\]

In particular, \(\operatorname{CF}_3(K_3\vee C_5)\simeq\bigvee^3S^1\vee\bigvee^3S^2\), and \(\operatorname{CF}_3(K_3\vee C_6)\simeq\bigvee^3S^1\vee\bigvee^6S^2\).

## Assumptions and scope

A graph join adds every edge from every vertex of \(K_m\) to every vertex of \(H\) and retains the edges within both graphs. A face of \(\operatorname{CF}_3(G)\) is a set that does not contain the three vertices of any triangle of \(G\). The geometric realization \(|I|\) is assumed path-connected; this is a topological hypothesis, not equivalent to requiring \(H\) connected. Degrees in the displayed homology formulas are integers \(d\ge2\), and all homology coefficients are integral. These claims concern the indicated canonical subgroup of graph automorphisms, not necessarily the entire automorphism group of \(G\).

## Proof

Write \(R=V(H)\), \(U=\{u_1,\ldots,u_m\}\), let \(\Delta_R\) be the full simplex on \(R\), and let \(D_m\) be the discrete zero-dimensional complex on \(U\). Since \(H\) has no triangles, a permitted face has exactly one of the following forms: (i) an arbitrary subset of \(R\); (ii) one apex \(u_i\) and a subset of \(R\) containing no edge of \(H\); (iii) exactly two apex vertices and no vertex of \(R\). Indeed, a pair of apex vertices and a vertex of \(R\) form a triangle, as do one apex and an edge of \(H\), whereas three apices form a triangle inside \(K_m\). This exhausts all forbidden triangles. Thus, as a **literal equality of simplicial complexes**, 

\[
 X=A\cup\left(\bigcup_{1\le i<j\le m}[u_i,u_j]\right),
 \qquad A=\Delta_R\cup_{I}(D_m*I).
\]

Every added edge meets \(A\) only in its two endpoints, and none belongs to a triangle in \(X\). Equivalently, if \(I_H(z)=\sum_{\sigma\in I}z^{|\sigma|}\), the full face-count polynomial (including the empty face once) is

\[
 \sum_{\sigma\in X}z^{|\sigma|}=(1+z)^{|R|}+mzI_H(z)+\binom m2z^2.
\]

The inclusion \(|I|\hookrightarrow|\Delta_R|\) is nullhomotopic because the simplex is contractible. The simplicial inclusions are cofibrations, so the displayed pushout for \(A\) is a homotopy pushout. Replacing \(\Delta_R\) by a cone on \(I\) yields

\[
 A\simeq D_{m+1}*I\simeq\bigvee^m\Sigma|I|,
\]

where \(D_{m+1}\) consists of the \(m\) original apices and one added apex. Since \(|I|\) is path-connected, each suspension is simply connected, so \(A\) is path-connected and simply connected. Adjoining any one new edge \([u_i,u_j]\) between points already in the same component adds exactly one free circle to the homotopy type. Repeating for the \(\binom m2\) edges proves the homotopy equivalence and the free fundamental group formula. No asphericity, spectral-sequence convergence or extrapolation from finite computations is used.

For naturality, the barycenter of \(\Delta_R\) is fixed by every automorphism of \(H\). The straight-line contraction to that barycenter gives an \(\operatorname{Aut}(H)\)-equivariant nullhomotopy of \(I\hookrightarrow\Delta_R\); the hub permutations fix the barycenter. Hence the replacement of \(A\) by \(D_{m+1}*I\) is equivariant for \(S_m\times\operatorname{Aut}(H)\), with the extra apex fixed. Reduced join homology, or the shifted tensor-product model for augmented simplicial chains, gives

\[
 \widetilde H_d(A;\mathbb Z)\cong
 \widetilde H_0(D_{m+1};\mathbb Z)\otimes\widetilde H_{d-1}(I;\mathbb Z)\quad(d\ge1).
\]

There is no \(\operatorname{Tor}\) term because \(\widetilde H_0(D_{m+1};\mathbb Z)\) is free. Its basis \([u_i]-[\ast]\) makes it precisely the \(m\)-dimensional permutation module, including integrally. Because \(I\) is connected, \(H_1(A;\mathbb Z)=0\). The pair \((X,A)\) has one relative one-cell for each hub pair and no other relative cells, so its long exact homology sequence identifies \(H_1(X;\mathbb Z)\) with the free abelian group on oriented unordered hub pairs, and identifies \(H_d(X;\mathbb Z)\) with \(H_d(A;\mathbb Z)\) for \(d\ge2\). Under hub permutations an oriented edge \([u_i,u_j]\) transforms with the sign of the endpoint reorder; thus the integral first-homology module is \(\bigwedge^2\mathbb Z^m\), and the higher-degree representation formula follows. The cycle specialization uses the standard independence complexes of cycles, which have the homotopy type of two spheres in the \(3q\) case and one sphere in the other congruence classes, with the dimensions stated above.

## Verification

The standalone script `verify_clique_join.py` enumerates clique-free faces independently by generating all triangles of each input graph and rejecting their supersets. It computes simplicial boundary ranks over \(\mathbf F_2\), compares the resulting reduced Betti numbers to the theorem, separately calculates base independence complexes, and verifies signed Lefschetz identities for sampled hub transpositions, rotations and reflections. The cases \((m,H)=(2,C_5),(3,C_5),(2,C_6),(3,C_6),(3,P_5),(4,\overline K_3)\) all pass; recorded output is included as `verify_output.txt`. This finite verification does not replace the general integral homotopy and equivariant argument above.

## Relationship to prior work

Ghosh and Selvaraja, *Shellability in Clique-Free Complexes of Graphs* (arXiv:2602.09623, first public February 10, 2026) introduce and study clique-free complexes, proving shellability/decomposability results under chordality and for localized clique attachments. Their results do not state this global clique-join homotopy decomposition, nor its integral \(S_m\times\operatorname{Aut}(H)\)-module structure. In particular, taking \(H=C_n\) with \(n\ge5\) retains an induced nonchordal cycle and is outside their chordal hypotheses. Previously known cycle independence/matching-complex sphere formulas provide the input for the specialized cycle expression but not the universal clique-join transfer theorem.

The Lovász neighborhood complex of a clique join, graph-metric Rips complexes of clique products, ordinary discrete-Morse wheel complexes and robust clique complexes are distinct constructions. Their homotopy formulas cannot by themselves be substituted for the three-clique-free complex of this graph join.

## Limitations

The path-connectedness assumption on \(\operatorname{Ind}(H)\) is used to obtain the precise free fundamental group and clean exterior-square first-homology module. No statement is made here for a disconnected independence complex, for higher thresholds \(\operatorname{CF}_t\) with \(t\ne3\), or for an arbitrary group of automorphisms mixing the two vertex classes. The cycle calculation relies on established cycle independence-complex homotopy formulas. Bibliographic coverage cannot rule out unindexed equivalent statements.

## References

1. Rakesh Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623 (first submitted 2026-02-10), https://arxiv.org/abs/2602.09623.
2. Michał Adamaszek, *Splittings of independence complexes and the powers of cycles*, arXiv:1106.6250 (2011), https://arxiv.org/abs/1106.6250 (for the cycle-specialization only; the main theorem is proved here).
