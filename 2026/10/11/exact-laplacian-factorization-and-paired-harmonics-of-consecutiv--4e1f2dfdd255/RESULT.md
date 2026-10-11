# Exact Laplacian factorization and paired harmonics of consecutive-layer hypersimplex graphs

## Finding
For every integer \(d\ge2\) and integers \(0\le a<b\le d\), let
\[
P_{d;a,b}=\operatorname{conv}\{\mathbf1_A:A\subseteq[d],\ a\le |A|\le b\},
\qquad G_{d;a,b}=\operatorname{skel}_1(P_{d;a,b}).
\]
All graph edges are undirected and unweighted. Write \(L\) for the combinatorial graph Laplacian and \(N=\sum_{r=a}^b\binom dr\) for the number of vertices. Let \(\binom d{-1}=0\), and, for each \(0\le j\le\lfloor d/2\rfloor\), let
\[
I_j=\{r\in\mathbb Z:\max(a,j)\le r\le\min(b,d-j)\},\qquad
m_j=\binom dj-\binom d{j-1}.
\]
For each nonempty \(I_j\), define the symmetric tridiagonal matrix \(M_j\), indexed by \(r\in I_j\), by
\[
(M_j)_{rr}=(d-r)\mathbf1_{r<b}+r\mathbf1_{r>a}
+j(d+1-j)(\mathbf1_{r=a}+\mathbf1_{r=b}),
\]
\[
(M_j)_{r,r+1}=(M_j)_{r+1,r}
=-\sqrt{(r+1-j)(d-j-r)},
\]
with all nonadjacent entries zero. Then the **complete Laplacian characteristic polynomial** is
\[
\boxed{\det(tI_N-L)=\prod_{j:I_j\ne\varnothing}\det(tI_{|I_j|}-M_j)^{m_j}.}
\]
Every \(M_j\) with \(j\ge1\) is positive definite, \(M_0\) has a one-dimensional kernel, and the **exact number of spanning trees** is
\[
\boxed{\tau(G_{d;a,b})=
\frac{\prod_{r=a}^{b-1}(d-r)}{\binom db}
\prod_{\substack{j\ge1\\I_j\ne\varnothing}}(\det M_j)^{m_j}.}
\]
A further spectral pairing, valid whenever \(I_1\ne\varnothing\), is
\[
\boxed{t\det(tI-M_1)(t-2d)^{\mathbf1_{a=0}+\mathbf1_{b=d}}
=(t-2d)\det(tI-M_0).}
\]
Thus the radial block and the first nonconstant harmonic block share their nonzero spectral values, after the explicitly indicated endpoint factors. In the strict interior case \(1\le a<b\le d-1\), the zero eigenvalue of the radial block is replaced by \(2d\) in the first harmonic block. The result concerns the whole family, including full cubes and two-rank intervals; these boundary cases can also be analyzed by classical Johnson or hypercube methods.

## Assumptions and scope
The source's edge classification for consecutive-layer hypersimplices states: an edge joins two subset-indicator vertices exactly when their subsets differ by one element, or when their subsets have the same cardinality equal to \(a\) or \(b\) and differ by exchanging one element. There are no same-rank exchange edges at an interior rank. This is an essential combinatorial premise, not a consequence inferred from numerical tests.

For each rank \(r\), let \(V_r\) be the real vector space with standard orthonormal basis the \(r\)-subsets of \([d]\). Its upward incidence map \(U_r:V_r\to V_{r+1}\) sends a basis subset to the sum of all its one-element supersets. Its adjoint is \(D_{r+1}=U_r^*\). Distinct harmonics are treated only in ranks where they exist. The formula for the block indexed by \(j=1\) is valid for all intervals because \(a<b\) and \(d\ge2\) ensure \(I_1\ne\varnothing\).

## Proof
**1. Harmonic decomposition.** The Boolean incidence maps obey
\[
D_{r+1}U_r-U_{r-1}D_r=(d-2r)I_{V_r}.
\]
For \(0\le j\le\lfloor d/2\rfloor\), put \(H_j=\ker D_j\) (where \(D_0=0\)). The commutator shows that \(\dim H_j=m_j\). For a unit \(h\in H_j\), repeatedly apply the raising maps and normalize to obtain orthonormal copies \(h_r\in V_r\) for \(j\le r\le d-j\), with
\[
U_rh_r=\sqrt{(r+1-j)(d-j-r)}\,h_{r+1},\quad
D_rh_r=\sqrt{(r-j)(d-j-r+1)}\,h_{r-1}.
\]
Chains belonging to orthogonal harmonic vectors are mutually orthogonal. Dimension counting in each rank yields their complete orthogonal decomposition. Upon retaining only ranks \(a,\ldots,b\), each \(h\in H_j\) contributes precisely one copy of the rank interval \(I_j\).

**2. Laplacian on the chains.** Edges that add or delete one element give the vertical degree \((d-r)\mathbf1_{r<b}+r\mathbf1_{r>a}\). Their off-diagonal operator is minus the incidence map; hence its action between consecutive members of a normalized harmonic chain is the displayed square root with a negative sign. At either boundary rank, the same-rank exchange graph is the Johnson graph. Its adjacency operator on \(V_r\) is \(U_{r-1}D_r-rI\), and its degree is \(r(d-r)\). Its graph Laplacian therefore acts on the harmonic chain with scalar
\[
r(d-r+1)-(r-j)(d-j-r+1)=j(d+1-j).
\]
The Johnson contribution occurs exactly at ranks \(a\) and \(b\). This proves the given tridiagonal blocks and all multiplicities, hence the characteristic-polynomial factorization. The vertical incidence edges alone connect every allowed subset to the bottom layer and connect all bottom subsets through two-step exchanges. Therefore the full graph is connected; its Laplacian has precisely one zero eigenvalue, in \(M_0\).

**3. Matrix-tree product.** The radial block has dimension \(k+1\) where \(k=b-a\), and factors as \(M_0=B^{\mathsf T}B\), with \(B\) the \(k\times(k+1)\) bidiagonal matrix whose row indexed by \(r\in[a,b-1]\) has entries
\[
B_{r,r}=\sqrt{d-r},\qquad B_{r,r+1}=-\sqrt{r+1}.
\]
Its kernel is spanned by \(v=(\sqrt{\binom dr})_{r=a}^{b}\), whose squared norm is \(N\). Put \(C_r=\binom dr\) and \(w_r=C_r(d-r)=C_{r+1}(r+1)\). Congruence by \(\operatorname{diag}(\sqrt{C_r})\) identifies \(M_0\) with the weighted-path Laplacian of edge weights \(w_r\). The weighted path has tree number \(\prod_{r=a}^{b-1}w_r\). The adjugate identity, together with the normalized null vector \(v/\sqrt N\), gives
\[
\frac{1}{N}\prod_{\lambda>0\atop\lambda\in\operatorname{spec}(M_0)}\lambda
=\frac{\prod_{r=a}^{b-1}w_r}{\prod_{r=a}^bC_r}
=\frac{\prod_{r=a}^{b-1}(d-r)}{\binom db}.
\]
The graph matrix-tree theorem says the full tree number is the product of all nonzero Laplacian eigenvalues divided by \(N\). Inserting every positive harmonic block yields the asserted exact formula.

**4. The first-harmonic pairing.** Define a formal matrix \(\widehat M_1\) on *all* ranks \(a,\ldots,b\) using the same entries as \(M_1\). If \(a=0\) and/or \(b=d\), its corresponding artificial rank is an isolated row with eigenvalue \(2d\), and deleting these rows recovers the genuine \(M_1\). Define a second \(k\times(k+1)\) bidiagonal matrix \(X\) by
\[
X_{r,r}=\sqrt r,\qquad X_{r,r+1}=\sqrt{d-r-1}
\qquad(a\le r<b).
\]
A direct entrywise calculation proves three identities:
\[
M_0=B^{\mathsf T}B,\qquad
2dI-\widehat M_1=X^{\mathsf T}X,\qquad
BB^{\mathsf T}+XX^{\mathsf T}=2dI_k.
\]
The last equality follows because the diagonal entries of the two summands are \(d+1\) and \(d-1\), while the respective off-diagonal entries cancel. The determinant identity \(\det(sI+X^{\mathsf T}X)=s\det(sI+XX^{\mathsf T})\), valid for a one-column-wider matrix, now yields
\[
\det(tI-\widehat M_1)
=(t-2d)\det(tI-BB^{\mathsf T})
=\frac{t-2d}{t}\det(tI-M_0).
\]
Dividing by the \(2d\)-eigenvalue factor for each artificial endpoint proves the boxed polynomial identity (with cancellation understood as an identity of polynomials). This concludes the proof.

## Verification
The standalone Python standard-library file `artifacts/verify_slab_spectra.py` reconstructs the graph from the published edge criterion and computes integer determinants by the Bareiss algorithm. It checks the complete harmonic block dimension and the first-harmonic polynomial identity over **219 parameter intervals** in dimensions \(2\le d\le10\). For all **34 intervals** in dimensions \(2\le d\le5\), it independently compares the block-product tree count with a direct graph-Laplacian cofactor determinant, up to \(N=32\) vertices. For dimensions \(2\le d\le4\), it also checks full characteristic-polynomial evaluations against the directly constructed graph Laplacians. Running `python3 artifacts/verify_slab_spectra.py` reports:

`VERIFY_OK rank-slab spectral blocks and tree counts intervals= 219 paired= 219 matrix_tree= 34 max_vertices= 32 full_characteristic_test_d<=4=True`

For example, when \((d,a,b)=(4,1,3)\), the graph has \(N=14\) vertices and \(\tau(G)=113799168\). The radial block polynomial is \(t(t^2-10t+21)\), the first-harmonic polynomial is \((t-8)(t^2-10t+21)\), and the second-harmonic polynomial is \(t-4\), appearing with multiplicities \(1,3,2\), respectively. These finite checks are not used as proofs of the universal identities.

## Relationship to prior work
Manecke, Sanyal, and So established the general \(S\)-hypersimplex construction, face and edge descriptions, subdivisions, and monotone-path properties. Their Theorem 2.1 supplies the essential graph-edge criterion here; the source's full text does not give the evaluated Laplacian spectral decomposition, its first-harmonic pairing, or a spanning-tree product for consecutive rank intervals. A separate published result, *Exact graph metric of consecutive-layer S-hypersimplices*, computes shortest-path distances and diameter for exactly this same graph; those invariants are not equivalent to its full eigenvalue multiplicities or tree complexity. Earlier spectral work by Qiu, Qiu, Jiang, and Shen concerns the **induced** middle-two-layer hypercube graph; the boundary Johnson edges of the polytope's one-skeleton change the adjacency relation and its spectrum. Classical Johnson-graph and hypercube spectra cover special two-rank and full-interval cases, which are included for completeness rather than claimed as independently novel. The new contribution is the all-interval block factorization, the exact tree product, and in particular the paired radial/first-harmonic factor identity.

## Limitations
The theorem is for **consecutive** allowed cardinalities and the standard unweighted one-skeleton. It does not give an analogous result for gapped \(S\), weighted transition graphs, or the spectra of higher-dimensional face-adjacency graphs. The harmonic decomposition and determinant identity are general proofs; the finite verifier covers only explicitly stated dimensions. General Boolean-lattice \(\mathfrak{sl}_2\) decompositions and Johnson eigenvalues are established tools, so the harmonic method is not claimed new. A residual originality risk is an unindexed spectral theorem for the same polytope graphs under older names such as cardinality-homogeneous set-system polytopes or rank-slab Boolean graphs; the targeted searches and inspected sources did not identify one. Independence from published results is not asserted beyond the specific source comparisons documented here.

## References
1. S. Manecke, R. Sanyal, and J. So, *S-hypersimplices, pulling triangulations, and monotone paths*, Electronic Journal of Combinatorics 27(3) (2020), P3.16, DOI `10.37236/8457`. First public arXiv version `1812.07491v1`, 2018-12-18. The edge classification is Theorem 2.1.
2. *Exact graph metric of consecutive-layer S-hypersimplices*, publicly available mathematical finding, 2026-10-04, `https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-graph-metric-of-consecutive-layer-s-hypersimplices--aed724149739`.
3. L. Qiu, J. Qiu, Z. Jiang, and C. Shen, *On the Spectrum of Middle-Cubes*, arXiv `0911.0126`, 2009. The graph in that article has only adjacent-rank inclusion edges, not the boundary Johnson exchange edges required here.
4. G. Kirchhoff, matrix-tree theorem (classical); standard Boolean-lattice up/down-operator decomposition and Johnson-scheme eigenvalues (classical).
