# Universal endpoint norms for Steiner-design incidence graphs

## Finding
Let \(\mathcal D\) be any existing Steiner \(2\)-design with \(v\) points, block size \(k\), and precisely one block through each pair of distinct points, where \(2\le k<v\). Give its bipartite point–block incidence graph \(G_{\mathcal D}\) unit edge lengths and identify its real edge space with \(\ell_1(E)\) or \(\ell_\infty(E)\). Let \(B\) be an oriented vertex–edge incidence matrix, and define the canonical Euclidean-orthogonal cut and cycle projections by
\[
Q=B^{\mathsf T}(BB^{\mathsf T})^+ B,\qquad P=I-Q.
\]
The exact induced endpoint norms are
\[
\boxed{\|Q\|_{1\to1}=\|Q\|_{\infty\to\infty}=5-\frac4k-\frac{4(k-1)}v},
\]
\[
\boxed{\|P\|_{1\to1}=\|P\|_{\infty\to\infty}=6-\frac6k-\frac{6(k-1)}v}.
\]
Every edge column has the respective displayed absolute column sum, regardless of the automorphism group of \(\mathcal D\). In particular,
\[
\|P\|-\|Q\|=1-\frac2k-\frac{2(k-1)}v.
\]
Thus for \(k\ge3\) the cycle projection is larger exactly when \((k-2)v>2k(k-1)\); equality and the reverse inequality are covered by the same criterion. For \(k=2\) the cut norm is strictly larger. For Steiner triple systems (\(k=3\)), cut dominance holds at admissible orders \(v=7,9\), while cycle dominance holds for every existing system with \(v\ge13\). For finite affine planes of order \(q\ge2\), with \(v=q^2\) and \(k=q\), the specializations are \(5-8/q+4/q^2\) and \(6(1-1/q)^2\); cycle dominance begins at \(q=4\) among integer orders for which a plane exists.

## Assumptions and scope
A Steiner \(2\)-\((v,k,1)\) design has \(v\) distinct points and a family of distinct \(k\)-point blocks, with every pair of distinct points in exactly one block. We quantify over existing designs only; the theorem makes no existence claim for unavailable parameter pairs. Elementary double counting gives the constant replication number \(r=(v-1)/(k-1)\) and the number of blocks \(b=vr/k\). The incidence graph has \(v+b\) vertices and \(vr\) point–block edges. It is connected because every two points share a block and every block contains points. The Moore–Penrose inverse in the definitions is taken in the ordinary real Euclidean inner product, while operator norms are measured in standard edge coordinates. No edge weights, arbitrary projections, or optimality among nonorthogonal projections are asserted.

## Proof
Orient every incidence edge from its point to its block. Write \(M\) for the \(v\)-by-\(b\) zero–one point–block matrix. Since each point belongs to \(r\) blocks and every distinct point-pair belongs to exactly one block,
\[
MM^{\mathsf T}=(r-1)I+J.
\]
The graph Laplacian in point and block coordinates is
\[
L=\begin{pmatrix}rI&-M\\-M^{\mathsf T}&kI\end{pmatrix}.
\]
Fix an arbitrary incident point–block pair \((p_0,B_0)\), and apply a unit source at \(p_0\) and unit sink at \(B_0\). Let \(x\) be the vector of point potentials and \(y\) the vector of block potentials. The equations are
\[
r x-My=e_{p_0},\qquad k y-M^{\mathsf T}x=-e_{B_0}.
\]
Eliminating \(y\), using \(r(k-1)+1=v\), gives
\[
\frac1k(vI-J)x=e_{p_0}-\frac1k\mathbf1_{B_0}.
\]
A valid gauge choice has mean-zero point potentials
\[
x=\frac{k}{v}e_{p_0}-\frac1v\mathbf1_{B_0},\qquad
 y=\frac1k(M^{\mathsf T}x-e_{B_0}).
\]
Consequently \(x\) equals \((k-1)/v\) at \(p_0\), equals \(-1/v\) on the other \(k-1\) points of \(B_0\), and is zero elsewhere. The block potential \(y\) equals \(-1/k\) on \(B_0\), \((k-1)/(vk)\) on the \(r-1\) other blocks through \(p_0\), \(-1/(vk)\) on blocks meeting \(B_0\) at a point other than \(p_0\), and zero on blocks disjoint from \(B_0\). The last classification is exhaustive: two distinct blocks cannot share two points in a Steiner \(2\)-design.

The electrical edge-current vector is the \((p_0,B_0)\)-column of \(Q\); at an incidence \((p,B)\) it equals \(x(p)-y(B)\). Here are the nonzero current classes, their exact cardinalities, and their absolute currents:

| Edge class | Number | Absolute current |
| --- | ---: | ---: |
| \(p_0\) to \(B_0\) | \(1\) | \(R=1/k+(k-1)/v\) |
| \(p_0\) to another block through \(p_0\) | \(r-1\) | \((k-1)^2/(vk)\) |
| Another point of \(B_0\) to \(B_0\) | \(k-1\) | \((v-k)/(vk)\) |
| Another point of \(B_0\) to a different block | \((k-1)(r-1)\) | \((k-1)/(vk)\) |
| A point outside \(B_0\) to a block through \(p_0\) other than \(B_0\) | \((r-1)(k-1)\) | \((k-1)/(vk)\) |
| A point outside \(B_0\) to a block meeting \(B_0\) elsewhere | \((k-1)^2(r-1)\) | \(1/(vk)\) |

The other incidences have zero current: they join points outside \(B_0\) to blocks disjoint from \(B_0\). These are genuine counts, not orbit or edge-transitivity assumptions. Since \(r-1=(v-k)/(k-1)\), summing the six rows gives
\[
\begin{aligned}
\sum_{e\in E}|Q_{e,(p_0,B_0)}|
&=R+\frac{(k-1)(v-k)}{vk}+\frac{4(k-1)^2(r-1)}{vk}\\
&=\frac1k+\frac{k-1}{v}+\frac{5(k-1)(v-k)}{vk}\\
&=5-\frac4k-\frac{4(k-1)}v.
\end{aligned}
\]
The diagonal entry \(Q_{(p_0,B_0),(p_0,B_0)}=R\), and \(0<R<1\) because \(v>k\). Hence the absolute sum of the corresponding column of \(P=I-Q\) is
\[
1-R+\sum_{e\ne(p_0,B_0)}|Q_{e,(p_0,B_0)}|
=1+\sum_e|Q_{e,(p_0,B_0)}|-2R
=6-\frac6k-\frac{6(k-1)}v.
\]
The chosen incidence was arbitrary; every column has the claimed sum. The induced \(\ell_1\) norm is the maximum absolute column sum, and the real symmetric matrices \(Q,P\) have equal maximum absolute row and column sums, proving the \(\ell_\infty\) assertions. Subtraction yields the dominance criterion, including its equality boundary. Substitution \(v=q^2,k=q\) yields the affine-plane consequences; \((q-2)q^2>2q(q-1)\) is equivalent to \(q^2-4q+2>0\), giving integer cutoff \(q\ge4\).

## Verification
The standalone `verify.py` uses an independent exact-rational grounded Laplacian inverse, reconstructs the full edge projections, and checks symmetry, idempotence, every diagonal, and **every** absolute column sum for six different existing Steiner designs: all-pairs \(2\)-\((5,2,1)\), the Fano plane, the affine plane of order \(3\), a cyclic Steiner triple system on \(13\) points, the projective plane of order \(3\), and the affine plane of order \(5\). All \(357\) individual columns passed. A symbolic calculation verifies the six-class sum and both norm identities. Run `python verify.py` after installing the dependency specified in `requirements.txt`. This finite verification is independent corroboration of the general proof, not a replacement for its all-parameter argument.

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii (2023) study the invariant and minimal projections onto cycle spaces, with explicit calculations primarily for tori and Hamming graphs. Their Theorem 45 computes the orthogonal cut-projection norm of a Boolean cube. Their full-text section survey and Hamming section do not state this parameter-only theorem for incidence graphs of arbitrary Steiner \(2\)-designs.

The published treatment *Twin circle wedges in neighborhood complexes of Steiner-design incidence graphs* concerns exactly the same point–block incidence graphs, but calculates the simple-homotopy type of their Lovász neighborhood complexes, not real edge-space operator norms. Dayioglu's work on affine planes constructs a different point graph from cyclic arrangements of points along lines and computes topological graph indices, not the cut and cycle norms of the bipartite incidence graph.

General graph Laplacian formulas express the orthogonal cut projector but do not automatically give the signs and complete absolute sums of its edge columns. The present calculation uses the Steiner pair-uniqueness identity and requires no flag-transitivity. Known special-family computations, such as projective-plane incidence graphs, do not alone cover the full non-symmetric Steiner-design class, including cyclic Steiner triple systems and affine planes.

## Limitations
The results do not establish minimum projection constants among arbitrary linear projections, any weighted incidence-graph version, or intermediate \(\ell_p\) norms. The theorem concerns real operators, though the real symmetric projection matrix has the same induced complex endpoint norms by absolute column/row summation. The parameter formulas apply only when a Steiner design actually exists; they do not settle design existence. A search of indexed literature and closely related full texts did not establish universal novelty against every less-indexed treatment of electrical flows or block-design incidence matrices; an equivalent prior formulation remains a residual risk. Finite verification dimensions do not prove the infinite statement without the analytic argument above.

## References
1. S. J. Dilworth, D. Kutzarova, and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first publicly posted 2023-05-21. https://arxiv.org/abs/2305.12582
2. *Twin circle wedges in neighborhood complexes of Steiner-design incidence graphs*, public mathematical research record, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-twin-circle-wedges-in-neighborhood-complexes-of-steiner-design-i--5b757c0a694f
3. A. Dayioglu, *Affine Graphs and their Topological Indices*, Journal of Mathematics (2021), article 9983771, first published 2021-05-04. https://doi.org/10.1155/2021/9983771
