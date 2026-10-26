# Endpoint Hodge norms and a sharp projection-dominance transition on cyclic clique cylinders

## Finding
For integers \(m\ge3\) and \(n\ge5\), let \(G_{m,n}=K_m\square C_n\) be the undirected, simple, unweighted graph whose vertices are \((a,j)\) with \(a\in\{1,\ldots,m\}\) and \(j\in\mathbb Z/n\mathbb Z\). Clique edges change only \(a\); rim edges change \(j\) by one. Let \(Q\) be the Euclidean-orthogonal projection in the real edge-coordinate space onto the cut space, and let \(P=I-Q\) be the complementary cycle projection.

Define
\[
\delta=\sqrt{m(m+4)},\qquad \rho=\frac{m+2-\delta}{2}\in(0,1),\qquad
R_j=\frac{\rho^j+\rho^{n-j}}{\delta(1-\rho^n)}\quad(0\le j<n),
\]
\[
z=R_{\lfloor n/2\rfloor},\qquad h=R_0-z,\qquad
t=\frac1{mn},\qquad W=\sum_{j=0}^{n-1}|R_j-t|.
\]
**Theorem.** The exact induced real endpoint norms are
\[
\boxed{\|Q\|_{1\to1}=\|Q\|_{\infty\to\infty}=2-2t+(m-1)(W-2z)},
\]
\[
\boxed{\|P\|_{1\to1}=\|P\|_{\infty\to\infty}=1+(m-1)(W+2h)}.
\]
For both projections the absolute column sums along rim edges are strictly larger than those along clique edges. Moreover,
\[
\begin{cases}
\|P\|>\|Q\|,&m\ge4\text{ or }(m,n)=(3,5),\\
\|Q\|>\|P\|,&m=3,\ n\ge6.
\end{cases}
\]
Thus increasing a three-vertex clique cylinder's rim length from five to six reverses which canonical projection has larger endpoint norm, whereas the reversal never occurs for clique sizes at least four.

For each fixed \(m\ge3\), put \(\kappa_m=4(m-1)/[m\log(1/\rho)]\). The precise finite-size asymptotics are
\[
\boxed{\|Q\|=4-\frac2m-\kappa_m\frac{\log n}{n}+O_m(n^{-1})},
\]
\[
\boxed{\|P\|=3-\frac2m+\frac{2(m-1)}\delta-\kappa_m\frac{\log n}{n}+O_m(n^{-1})}
\]
as \(n\to\infty\), for fixed \(m\). Both projections have the same sharp logarithmic correction coefficient despite different limiting norms.

For instance, when \((m,n)=(3,5)\), the cut and cycle norms are \(352/145\) and \(353/145\), respectively; when \((m,n)=(3,6)\), they are \(53/21\) and \(158/63\).

## Assumptions and scope
Give the edge space \(\mathbb R^{E(G)}\) its standard unweighted \(\ell_1\) or \(\ell_\infty\) norm. The incidence matrix \(D\) has one column per edge, with one entry \(+1\) and one \(-1\). Put \(L=DD^{\mathsf T}\), \(Q=D^{\mathsf T}L^+D\), and \(P=I-Q\); the definition is independent of the chosen edge orientations. The theorem concerns these *canonical* projections only. Neither globally minimal projection constants nor non-endpoint operator norms are claimed.

The restrictions \(m\ge3\), \(n\ge5\) exclude the circular ladder with a two-vertex cross-section, the rook-graph case with a triangular rim, and the all-complete-factor decomposition of the square rim. These boundary graph families have distinct symmetry and prior calculations.

## Proof
**1. Cyclic Green function.** Write \(L_C\) for the combinatorial Laplacian of \(C_n\). The clique Laplacian is \(mI-J\). The vertex space of the product decomposes orthogonally into the constant-in-clique-label sector and its zero-sum counterpart. On the zero-sum sector the product Laplacian is \(mI+L_C\); its inverse has cyclic kernel \(R_j\), characterized by
\[
(m+2)R_j-R_{j-1}-R_{j+1}=\mathbf1_{j=0},\qquad \sum_jR_j=\frac1m.
\]
Solving the homogeneous second-order recurrence away from zero gives exactly the formula for \(R_j\) in the theorem. Positivity and symmetry imply \(R_0>R_1>\cdots>R_{\lfloor n/2\rfloor}>0\), followed by reflection. Thus
\[
\sum_{j=0}^{n-1}|R_j-R_{j-1}|=2(R_0-z)=2h,
\]
with indices interpreted cyclically.

**2. Clique-edge columns.** Inject current at \((a,0)\) and remove it at \((b,0)\), where \(a\ne b\) lie in the same clique. The induced potential is \(R_j(\mathbf1_{c=a}-\mathbf1_{c=b})\) at \((c,j)\). Summing absolute edge gradients yields \(2(m-1)\sum_jR_j=2(m-1)/m\) along all clique edges and \(2\sum_j|R_j-R_{j-1}|=4h\) along all rim edges. Hence the cut-column absolute sum is
\[
A_V=\frac{2(m-1)}m+4h.
\]
Its diagonal entry is \(2R_0\), so the complementary cycle-column sum is
\[
B_V=1+A_V-4R_0=3-\frac2m-4z.
\]

**3. Rim-edge columns.** Inject current at \((a,0)\) and remove it at \((a,1)\). Choose a mean-zero cycle potential \(H\) satisfying \(L_CH=\mathbf1_0-\frac1n\mathbf1\). The product potential at \((c,j)\), up to an additive constant, is
\[
u_{c,j}=\frac1m(H_j-H_{j-1})+\Bigl(\mathbf1_{c=a}-\frac1m\Bigr)(R_j-R_{j-1}).
\]
Its rim-edge gradient in the distinguished clique label \(c=a\) is \(\mathbf1_{j=0}-t-(m-1)R_j\), and in each other label it is \(R_j-t\). Because \(R_0\le1/m\), the former gradient is positive at \(j=0\) and negative at all other rim positions. Their total absolute sum is \(2-2t-2(m-1)R_0+(m-1)W\). Clique-edge absolute gradients sum to \(2(m-1)h\). Consequently the rim-edge cut column has norm
\[
A_H=2-2t+(m-1)(W-2z).
\]
Its diagonal value is \(1-t-(m-1)R_0\), and therefore its cycle-column norm is
\[
B_H=1+A_H-2[1-t-(m-1)R_0]
=1+(m-1)(W+2h).
\]
The graph symmetries act transitively on the clique-edge orbit and on the rim-edge orbit. Thus the global \(\ell_1\) projection norms are the larger of \(A_V,A_H\) and \(B_V,B_H\), respectively. Since both matrices are symmetric, their \(\ell_\infty\) norms equal their \(\ell_1\) norms.

**4. Strict dominance of rim columns.** Put \(k=\lfloor n/2\rfloor\). The kernel formula gives
\[
h=\frac{(1-\rho^k)(1-\rho^{n-k})}{\delta(1-\rho^n)}\ge\frac1{m+2}
\quad(n\ge5).
\]
For even \(n=2k\), the rightmost expression becomes \((1-\rho^k)/[\delta(1+\rho^k)]\), increasing in \(k\); for odd \(n=2k+1\), it strictly exceeds the even expression with the same \(k\), because the comparison numerator exceeds its denominator by \(\rho^k(1-\rho)\). At \(n=4\), the expression equals \(1/(m+2)\).

Since the positive sequence \(R_j\) has mean \(t\), we have \(z\le t\) and \(W\ge2(R_0-t)\). Using these inequalities yields
\[
A_H-A_V\ge\frac2m-\frac2n+2(m-3)h
\ge\frac{4(2m^2-6m+5)}{5m(m+2)}>0.
\]
For \(m\ge4\), the same estimates, \(R_0\ge1/(m+2)\) and \(n\ge5\) yield
\[
B_H-B_V\ge\frac{6(m-3)(m-2)}{5m(m+2)}>0.
\]
For \(m=3\), use the absolutely convergent nonnegative walk series \((5I-A(C_n))^{-1}=\sum_{r\ge0}5^{-r-1}A(C_n)^r\). It implies \(R_0\ge1/5+2/125\), since the cycle has exactly two closed walks of length two starting at a vertex. Hence
\[
B_H-B_V\ge-\frac43+8R_0-\frac4{3n}\ge\frac{16}{125}>0.
\]
Therefore the rim columns are strictly maximal for both projections.

**5. Projection-dominance transition.** The two rim-column formulas simplify to
\[
B_H-A_H=-1+2t+2(m-1)R_0.
\]
For \(m\ge4\), one has \(R_0>1/\delta\) and \(2(m-1)/\delta>1\), because \(4(m-1)^2-m(m+4)=3m(m-4)+4>0\). Thus \(B_H>A_H\) for every allowed \(n\). For \(m=3\), \(R_0=(1+\rho^n)/[\sqrt{21}(1-\rho^n)]\) decreases strictly in \(n\); so does \(2/(3n)\). Exact evaluation at \(n=5\) gives \(B_H-A_H=1/145>0\), whereas at \(n=6\) it gives \(B_H-A_H=-1/63<0\). This proves the complete dichotomy.

**6. Logarithmic finite-size correction.** Keep \(m\) fixed. The values \(R_j\) decrease with cyclic distance, and for distances small compared with \(n\) they are \(\delta^{-1}\rho^j(1+o(1))\). Let \(s_n\) be the largest integer \(0\le j\le\lfloor n/2\rfloor\) for which \(R_j>t\). Then
\[
s_n=\frac{\log n}{\log(1/\rho)}+O_m(1).
\]
There are \(2s_n+1\) cyclic positions with \(R_j>t\), and the total \(R\)-mass outside them is \(O_m(n^{-1})\). The equality \(\sum_j(R_j-t)=0\) therefore gives
\[
W=2\sum_{R_j>t}(R_j-t)
=\frac2m-\frac{4}{m\log(1/\rho)}\frac{\log n}{n}+O_m(n^{-1}).
\]
Also \(z=O_m(\rho^{n/2})\) and \(R_0=\delta^{-1}+O_m(\rho^n)\). Substituting into \(A_H\) and \(B_H\) proves both asymptotic expansions. All remainder estimates here hold for fixed \(m\), not uniformly in growing clique size.

## Verification
The standalone standard-library file `verify_clique_cycle.py` builds each graph Laplacian over exact rational arithmetic, inverts a grounded minor for every edge source, calculates all cut and cycle projection column norms, and compares them with independent cyclic-kernel formulas. It checks all \(398\) columns for the seven pairs \((m,n)=(3,5),(3,6),(3,7),(4,5),(4,6),(5,5),(6,5)\), including the two exact transition values. Its successful execution corroborates but does not replace the uniform analytical proof.

## Relationship to prior work
The study of invariant graph cycle projections and their relation to transportation cost is developed by Dilworth, Kutzarova and Ostrovskii (2023; published 2024). Their detailed results concern discrete tori and Hamming graphs and do not state the mixed cycle–complete-factor formulas or the rim-orbit/dominance classification proved here. Lim (2020) surveys algebraic graph Hodge decomposition, a standard starting point for the incidence/Laplacian identities.

Previously calculated nearby families include the circular ladder \(C_n\square K_2\), rook graphs \(K_m\square K_q\), and all-complete-factor Hamming products. These respectively have \(m=2\), a complete second factor, or only complete factors. The present theorem is limited to \(m\ge3,n\ge5\), so none contains the asserted parameter range. General pseudoinverse formulas for an arbitrary graph alone do not evaluate these specific finite sums, sharp orbit inequalities, and asymptotic coefficients.

## Limitations
The findings concern canonical real Euclidean-orthogonal projections of unweighted finite graph edge spaces at the two endpoints. They do not assert minimum norms among all real-linear projections, weighted-edge generalizations, complex-space minimality, or formulas for intermediate \(\ell_p\) exponents. The asymptotic statements fix \(m\) before sending \(n\) to infinity. Literature-search coverage is not exhaustive, and no independent mathematical audit has been performed.

## References
1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle Spaces: Invariant Projections and Applications to Transportation Cost*, arXiv:2305.12582v1 (first posted 21 May 2023); Proceedings of Symposia in Pure Mathematics 106 (2024), DOI: 10.1090/pspum/106/01929.
2. L.-H. Lim, *Hodge Laplacians on Graphs*, SIAM Review 62 (2020), 685–715, DOI: 10.1137/18M1223101.
