# Sharp cycle and cut projection constants for nonbinary Hamming graphs

## Finding
For every pair of integers \(d\ge 2\) and \(q\ge 3\), let \(H(d,q)\) be the Cartesian power of the complete graph on \(q\) vertices: its vertices are \(\{0,\ldots,q-1\}^d\), and two vertices are adjacent when they differ in exactly one coordinate. Orient its edges arbitrarily, let \(B:\mathbb R^E\to\mathbb R^V\) be the signed incidence operator, and put \(Z=\ker B\) (circulations) and \(C=\operatorname{ran}B^{\mathsf T}\) (cut space). Equip \(\mathbb R^E\) with its coordinate \(\ell_1\) norm. Then
\[
\boxed{\inf_{P^2=P,\ \operatorname{ran}P=C}\|P\|_{1\to1}=\frac{(d+1)(q-1)}q,}
\]
and
\[
\boxed{\inf_{Q^2=Q,\ \operatorname{ran}Q=Z}\|Q\|_{1\to1}
=1+\frac{(d+1)(q-1)}q-\frac{4(q^d-1)}{d q^d(q-1)}.}
\]
Both optima are attained simultaneously by the complementary Euclidean orthogonal projections \(P_*=B^{\mathsf T}(BB^{\mathsf T})^+B\) and \(Q_*=I-P_*\), where the superscript \(+\) denotes the Moore--Penrose inverse. These are the unique projections onto their respective ranges that commute with every graph automorphism (acting on oriented edges with signs). Uniqueness among *all* norm-minimizing projections is not asserted.

For fixed \(q\ge3\) the two optima grow linearly with \(d\), with common leading slope \((q-1)/q\). Their difference is exactly \(1-4(q^d-1)/(d q^d(q-1))>0\). The binary \(q=2\) formula follows from the same computation but is previously known and is not claimed as a new case.

## Assumptions and scope
All graph edges have length one. The edge norm is real \(\ell_1(E)\), not a quotient or vertex-function norm. A projection means a real linear idempotent with exactly the stated range; the infimum is over *all* such projections, without symmetry assumptions. An edge orientation affects only coordinate signs, hence not the norms. The claimed new range is all integer pairs \(d\ge2,q\ge3\); no primeness or field structure is assumed for the alphabet.

## Proof
**1. Symmetry forces the orthogonal projections to be optimal.** Let \(\Gamma=(S_q)^d\rtimes S_d\) act on vertices by independent alphabet permutations and coordinate permutations, and on the signed oriented edge vectors by the induced signed permutation matrices. Both \(Z\) and \(C\) are invariant. Averaging any projection onto either invariant subspace over \(\Gamma\) preserves its projection property and never increases its \(\ell_1\)-operator norm.

We show that the Euclidean orthogonal cycle projection is the *only* \(\Gamma\)-equivariant projection onto \(Z\). Put \(o=(0,\ldots,0)\), and let \(X_o=B^{\mathsf T}\mathbf1_o\), the oriented star at \(o\). It is fixed by the vertex stabilizer \(\Gamma_o\). Any \(\Gamma_o\)-invariant circulation \(z\) must vanish: a same-Hamming-level edge changes one nonzero symbol to another, and a transposition of those two nonzero symbols fixing \(o\) reverses that edge, forcing its coefficient to zero. All edges increasing Hamming distance from \(o\) from level \(k\) to level \(k+1\) form a single \(\Gamma_o\)-orbit, so an invariant flow has common coefficient \(c_k\) on such edges. Its divergence at \(o\) gives \(d(q-1)c_0=0\); divergence at level \(k\) gives \((d-k)(q-1)c_k-kc_{k-1}=0\). Induction gives every \(c_k=0\).

If \(Q\) is an equivariant projection onto \(Z\), then \(QX_o\) is an invariant circulation and therefore zero. Vertex transitivity implies \(QX_v=0\) for all vertex-star cut vectors \(X_v=B^{\mathsf T}\mathbf1_v\). These span \(C\), so \(Q\) kills \(C\) and fixes \(Z\); hence \(Q=Q_*\). Complementing any equivariant cut projection produces an equivariant cycle projection, so \(P_*\) is also the unique equivariant cut projection. Averaging proves their *global* minimality.

**2. One column of the cut projection.** Edge transitivity reduces its induced \(\ell_1\)-norm to any single column. Take \(u=(0,\ldots,0)\), \(v=(1,0,\ldots,0)\), and the oriented edge \(e=(u,v)\). Write \(L=BB^{\mathsf T}\). As \(\mathbf1_v-\mathbf1_u\) has zero sum,
\[
 f=L^+(\mathbf1_v-\mathbf1_u)
 =\int_0^\infty e^{-tL}(\mathbf1_v-\mathbf1_u)\,dt.
\]
The Laplacian is the sum of independent coordinate Laplacians \(qI-J\), so its heat kernel is the product of
\[
 h_t(a,b)=\frac{1-e^{-qt}}q+e^{-qt}\mathbf1_{\{a=b\}}.
\]
Consequently, writing \(x=(x_1,y)\) with \(y\in\{0,\ldots,q-1\}^{d-1}\),
\[
 f(x)=(\mathbf1_{\{x_1=1\}}-\mathbf1_{\{x_1=0\}})A(y),\qquad
 A(y)=\int_0^\infty e^{-qt}\prod_{j=2}^d h_t(y_j,0)\,dt>0.
\]
The column \(P_*\mathbf1_e=B^{\mathsf T}f\) consists of the differences of \(f\) across graph edges.

For edges in coordinate 1, each fixed \(y\) gives one difference of magnitude \(2A(y)\) between 0 and 1, and \(2(q-2)\) differences of magnitude \(A(y)\) between one of 0,1 and another alphabet symbol. Summing and using \(\sum_y\prod_{j=2}^d h_t(y_j,0)=1\) gives
\[
 S_1=2(q-1)\sum_y A(y)
 =2(q-1)\int_0^\infty e^{-qt}dt
 =\frac{2(q-1)}q.
\]
For each coordinate \(j\ge2\), only the two first-coordinate slices \(x_1=0,1\) contribute. Among the edges changing coordinate \(j\), only edges between symbol 0 and one of the \(q-1\) nonzero symbols have nonzero differences. The magnitude for such an edge, at fixed other coordinates, is
\[
\int_0^\infty e^{-qt}\bigl(h_t(0,0)-h_t(a,0)\bigr)
 \prod_{i\ne1,j}h_t(y_i,0)dt
 =\int_0^\infty e^{-2qt}\prod_{i\ne1,j}h_t(y_i,0)dt,
\quad a\ne0.
\]
Summing over all other coordinates, two first-coordinate slices, and \(q-1\) nonzero symbol choices yields
\[
 S_j=2(q-1)\int_0^\infty e^{-2qt}dt=\frac{q-1}q.
\]
Thus every column has absolute sum \(S_1+\sum_{j=2}^d S_j=(d+1)(q-1)/q\). This gives the first sharp constant.

**3. The complementary cycle projection.** Since \(P_*\) is an orthogonal projection of rank \(q^d-1\), and the automorphism group acts transitively on its \(d(q-1)q^d/2\) edge coordinates, its common diagonal entry is
\[
 \alpha=\frac{q^d-1}{d(q-1)q^d/2}
 =\frac{2(q^d-1)}{d(q-1)q^d},\qquad 0\le\alpha\le1.
\]
For each edge column, \(Q_*=I-P_*\) changes only the diagonal entry from \(\alpha\) to \(1-\alpha\) and negates all off-diagonal entries. Hence
\[
 \|Q_*\|_{1\to1}=\|P_*\|_{1\to1}+1-2\alpha
 =1+\frac{(d+1)(q-1)}q-\frac{4(q^d-1)}{d(q-1)q^d}.
\]
By Step 1 it is the second global optimum. Finally, for \(d\ge2,q\ge3\), \(d(q-1)\ge4>4(1-q^{-d})\), which proves the strict comparison; the stated asymptotics follow directly from the exact expressions. \(\square\)

## Verification
The standalone `check_hamming.py` reconstructs the complete signed incidence and reduced graph Laplacian over exact rational numbers, computes the orthogonal cut and cycle projections without using the heat-semigroup formula, and checks their entire matrices. It verifies column norms, constant diagonals, symmetry, idempotence, and zero divergence. On nine finite instances, including ternary and quinary graphs, it passed 88,858 exact rational assertions. These checks do not establish the infinite-parameter theorem; the proof above does.

Run with `python3 check_hamming.py` from a directory containing the supplied script. It requires only the Python standard library.

## Relationship to prior work
Dilworth, Kutzarova, and Ostrovskii, *Cycle Spaces: Invariant Projections and Applications to Transportation Cost*, arXiv:2305.12582, Theorem 43, prove uniqueness of the invariant projection for all Hamming graphs. Their Theorem 45 and Corollary 60 compute the endpoint projection norms for the binary cube only. The present calculation supplies the explicit nonbinary constants, both complementary optima, and their all-alphabet asymptotics. It does not claim novelty for the known binary specialization or for the invariant-projection uniqueness principle.

The same authors' *Lipschitz Free Spaces on Finite Metric Spaces*, arXiv:1807.03814, establishes the edge-space quotient framework and projection-averaging motivation, with detailed examples concerning diamond and Laakso graphs. Its inspected sections and search of the text did not identify these nonbinary Hamming constants. Other similarly named Hamming spectral projections act on different vertex-function or free-space Fourier subspaces and do not directly imply the stated edge-space circulation norms.

## Limitations
The result concerns **relative** projections in the canonical real unit-edge \(\ell_1(E)\) space, not absolute projection constants, minimum Banach--Mazur distortion, weighted edges, arbitrary Cartesian products with unequal alphabet sizes, or all norm-minimizing projections. Historical priority under alternative names (electrical transfer-current norms, cut/flow complementability) has not been exhaustively settled; no independent mathematical validation is claimed.

## References
1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582 (first arXiv posting 2023-05-21), especially Sections 2.6--2.7, Theorems 43 and 45 and Corollary 60. https://arxiv.org/abs/2305.12582
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814 (first arXiv posting 2018-07-10). https://arxiv.org/abs/1807.03814
