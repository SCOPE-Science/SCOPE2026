# Local class groups and a non-\(\mathbb Q\)-Gorenstein threshold for crown-graph toric varieties

## Finding

For every integer \(n\ge4\), let \(G_n\) be the bipartite crown graph with left vertices \(L_1,\ldots,L_n\), right vertices \(R_1,\ldots,R_n\), and edges \((L_i,R_j)\) exactly when \(i\ne j\). Let \(X_n\subset\mathbb P^{n(n-1)-1}_{\mathbb C}\) be the closure of the monomial parametrization
\[
(u_1,\ldots,u_n;v_1,\ldots,v_n)\longmapsto [u_i v_j]_{i\ne j}.
\]
The variety \(X_n\) is normal of dimension \(2n-2\). Its \(n(n-1)\) coordinate torus-fixed points \(p_{ij}\) have isomorphic affine toric neighborhoods, and every such point satisfies
\[
\operatorname{Cl}(\mathcal O_{X_n,p_{ij}})\cong\mathbb Z^2,
\qquad
\operatorname{edim}(\mathcal O_{X_n,p_{ij}})=4n-7.
\]
In a natural basis for the local class group, the local canonical divisor has class \((n-3,n-3)\). Hence \(K_{X_n}\) is not \(\mathbb Q\)-Cartier at any torus-fixed point for \(n\ge4\). The degree-six cycle at \(n=3\) is the sharp boundary: its corresponding local canonical class vanishes and its fixed-point charts are Gorenstein. No global claim about the entire singular locus is made.

## Assumptions and scope

All varieties and local rings are over \(\mathbb C\). Here \(\operatorname{Cl}\) is the Weil-divisor class group of the indicated normal local ring; \(\operatorname{edim}\) is its Zariski tangent-space dimension. The statement applies to all integers \(n\ge4\), all allowed ordered pairs \((i,j)\) with \(i\ne j\), and to the projective edge-monomial toric variety, not to the affine cone, edge ideal, or perfectly matchable subgraph polytope.

By simultaneously permuting the vertex labels, it suffices to analyze the chart \(D_+(z_{12})\) at \(p_{12}\). Put \(r=n-2\), and let \(I=\{3,\ldots,n\}\), so \(|I|=r\). Use the lattice \(M=\mathbb Z^{2r+2}\) with ordered coordinates \((a_p)_{p\in I},(b_q)_{q\in I},X,Y\). Denote standard basis vectors by \(e_{a_p},e_{b_q},e_X,e_Y\).

## Proof

**1. The coordinate semigroup and its saturation.** In \(D_+(z_{12})\), the edge ratios \(z_{ij}/z_{12}\) have exponent vectors
\[
\begin{aligned}
 z_{p2}/z_{12}&\longleftrightarrow e_{a_p},&
 z_{1q}/z_{12}&\longleftrightarrow e_{b_q},\\
 z_{2q}/z_{12}&\longleftrightarrow e_X+e_{b_q},&
 z_{p1}/z_{12}&\longleftrightarrow e_Y+e_{a_p},\\
 z_{21}/z_{12}&\longleftrightarrow e_X+e_Y,&
 z_{pq}/z_{12}&\longleftrightarrow e_{a_p}+e_{b_q}
 \quad(p\ne q).
\end{aligned}
\]
The final vectors are redundant. Thus the chart semigroup \(S_n\) has generating set
\[
\mathcal H_n=\{e_{a_p},e_{b_q},e_X+e_{b_q},e_Y+e_{a_p}:p,q\in I\}\cup\{e_X+e_Y\},
\]
with \(4r+1=4n-7\) distinct elements. Its group completion equals \(M\): the vectors \(e_{a_p},e_{b_q}\) occur, and subtracting these from the corresponding mixed generators recovers \(e_X,e_Y\) as lattice differences.

Set \(C_n\subset M_{\mathbb R}\) to be the rational cone defined by
\[
 a_p,b_q,X,Y\ge0,\qquad
 X-Y\le\sum_{q\in I}b_q,\qquad
 Y-X\le\sum_{p\in I}a_p.
\tag{1}
\]
Every generator of \(S_n\) satisfies (1). Conversely let \((a,b,X,Y)\in C_n\cap M\). If \(X\ge Y\), subtract \(Y\) copies of \(e_X+e_Y\); then choose nonnegative integers \(t_q\le b_q\) with \(\sum_qt_q=X-Y\), which exist by the first sum inequality, and subtract \(t_q\) copies of \(e_X+e_{b_q}\). The remaining vector is a nonnegative integral sum of \(e_{a_p},e_{b_q}\). If \(Y\ge X\), reverse the roles of \(a\) and \(b\), subtract \(X\) copies of \(e_X+e_Y\), and allocate \(Y-X\) among \(e_Y+e_{a_p}\). This is a constructive integer decomposition, proving
\[
 S_n=C_n\cap M.
\]
Consequently \(D_+(z_{12})=\operatorname{Spec}\mathbb C[S_n]\) is normal. The same argument applies to each edge chart, which together cover \(X_n\); hence \(X_n\) is normal. The lattice rank establishes \(\dim X_n=2r+2=2n-2\).

**2. The exact facet system.** The \(2r+2\) coordinate inequalities in (1) have primitive inward normals \(e_{a_p}^{*},e_{b_q}^{*},e_X^{*},e_Y^{*}\). The other two have primitive normals
\[
 \nu_+=\sum_{q\in I}e_{b_q}^{*}-e_X^{*}+e_Y^{*},
 \qquad
 \nu_-=\sum_{p\in I}e_{a_p}^{*}+e_X^{*}-e_Y^{*}.
\tag{2}
\]
These are exactly the facets, giving \(2r+4=2n\) rays in the dual cone. To see that none of the inequalities is redundant, note that the tight generators for \(\nu_+\) include the \(r\) independent vectors \(e_{a_p}\), the \(r\) vectors \(e_X+e_{b_q}\), and \(e_X+e_Y\), together spanning a hyperplane of dimension \(2r+1\); the argument for \(\nu_-\) is symmetric. For \(a_p=0\), tight generators include all \(r\) vectors \(e_{b_q}\), the other \(r-1\) vectors \(e_{a_s}\), a vector \(e_X+e_{b_q}\), and \(e_X+e_Y\), again giving dimension \(2r+1\). The \(b_q=0\) facets are symmetric. For \(X=0\), all the \(2r\) coordinate generators and any vector \(e_Y+e_{a_p}\) are independent; the \(Y=0\) case is symmetric. Since (1) already gives the complete cone, this list is exhaustive.

**3. Class groups and the canonical obstruction.** For a normal affine toric variety with maximal-dimensional cone, the invariant Weil-divisor presentation gives
\[
 M\longrightarrow\mathbb Z^{\Sigma(1)}\longrightarrow\operatorname{Cl}(D_+(z_{12}))\longrightarrow0,
 \qquad m\longmapsto (\langle m,\nu\rangle)_{\nu\in\Sigma(1)}.
\tag{3}
\]
The first \(2r+2\) rows of this integer matrix form an identity matrix. Therefore the cokernel is free of rank two, with basis the classes \([D_+],[D_-]\) of (2). Localizing at the unique closed torus orbit (the fixed point) does not change this group: every torus-invariant prime divisor contains the orbit, and a torus-invariant divisor Cartier near that orbit is Cartier throughout the affine chart, hence principal. Thus
\[
\operatorname{Cl}(\mathcal O_{X_n,p_{12}})
 =\mathbb Z[D_+]\oplus\mathbb Z[D_-].
\]
Choose \(m_0\in M\) whose \(2r+2\) coordinates all equal \(1\). It pairs to \(1\) with each coordinate ray and to \(r\) with both \(\nu_+\) and \(\nu_-\). Since the canonical divisor of a normal toric variety equals minus the sum of its invariant prime divisors, adding the principal divisor \(\operatorname{div}(\chi^{m_0})\) gives
\[
 [K_{X_n}]_{p_{12}}=(r-1)([D_+]+[D_-])
 =(n-3,n-3)\in\mathbb Z^2.
\]
For \(n\ge4\), the class has infinite order. On a local normal ring, a rational Weil divisor is \(\mathbb Q\)-Cartier precisely when some nonzero positive multiple is principal. Hence the canonical divisor is not \(\mathbb Q\)-Cartier at the fixed point. When \(n=3\), the class is zero.

**4. Embedding dimension and all fixed points.** Every member of \(\mathcal H_n\) is indecomposable: its \(X,Y\) pattern and coordinate supports forbid a decomposition as two nonzero elements of \(S_n\); conversely the vectors from \(z_{pq}\) with distinct \(p,q\in I\) are decomposable. Thus the maximal monomial ideal of \(\mathbb C[S_n]\) has \(4r+1=4n-7\) minimal monomial generators, which form a basis of its cotangent space. The simultaneous label-permutation action is transitive on allowed edges; each support monomial corresponds to a vertex of the edge polytope. Therefore all \(n(n-1)\) fixed points have these same invariants. Since \(4n-7>2n-2\) for \(n\ge4\), every fixed point is singular.

## Verification

The accompanying independent Python 3 standard-library script `checker.py` recomputes exponent vectors from all ordered edges, tests the proposed Hilbert-basis list, verifies the exact rank of the cone generators and of every facet's tight set, checks the canonical pairings, and implements the constructive integer decomposition. It completed rational/integer tests for \(3\le n\le8\) and exactly \(6{,}933\) bounded integral cone points for \(3\le n\le5\), producing `checker_output.txt`. The symbolic proof, rather than the finite tests, establishes the unbounded assertions.

## Relationship to prior work

Ohsugi and Hibi developed the geometry and combinatorics of edge polytopes and classified simple and smooth cases; their smoothness criterion does not determine the fixed-point local class groups or the \(\mathbb Q\)-Cartier status of the canonical divisor for this family [1]. Their results on graph toric ideals concern defining relations rather than these local invariants [2]. Higashitani and Matsushita give general class-group results for affine graph edge rings [3], but those global graded rings must not be identified with the local rings at fixed points of the projectivized variety. More general classifications of Gorenstein **global** edge polytopes [4] do not by themselves determine this local non-\(\mathbb Q\)-Gorenstein threshold. The contribution here is the explicit local cone, class-group basis, and canonical class for every crown-graph edge chart.

## Limitations

The theorem does not classify the whole singular locus, singularities on nonzero-dimensional torus orbits, discrepancies, or resolutions. All results concern the complex normal projective edge-monomial toric variety and its coordinate fixed points. Existing general toric formulas underlie the proof; the literature comparison leaves a possibility of an unindexed prior specialization to crown graphs. No independent external audit of this classification has been performed.

## References

[1] H. Ohsugi and T. Hibi, *Simple polytopes arising from finite graphs*, arXiv:0804.4287v1 (first posted 2008-04-27), especially Theorem 1.8.

[2] H. Ohsugi and T. Hibi, *Toric ideals of finite graphs and adjacent 2-minors*, arXiv:1108.2850 (first posted 2011).

[3] A. Higashitani and K. Matsushita, *Three families of toric rings arising from posets or graphs with small class groups*, arXiv:2108.01347, especially Theorem 3.6 and Section 4.3.

[4] K. Mori, *Toric Rings of Perfectly Matchable Subgraph Polytopes*, Graphs and Combinatorics (2023), especially Section 5 and Proposition 5.5.
