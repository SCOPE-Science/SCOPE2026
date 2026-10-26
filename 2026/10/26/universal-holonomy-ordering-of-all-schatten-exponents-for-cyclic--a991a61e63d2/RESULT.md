# Universal holonomy ordering of all Schatten exponents for cyclic rank-one frames

## Finding
Fix an integer \(m\ge4\), and positive real numbers \(r_1,\ldots,r_m\) satisfying \(r_{j-1}+r_j<1\) for every cyclic index \(j\) (with \(r_0=r_m\)). Consider \(m\) unit vectors \(v_1,\ldots,v_m\in\mathbb C^m\) whose Gram matrix \(G_\phi\) has diagonal entries \(1\), consecutive overlaps of moduli \(r_j\), all other overlaps zero, and total cycle phase \(e^{i\phi}\). Put \(S_\phi=\sum_{j=1}^m |v_j\rangle\langle v_j|\). Every phase \(\phi\in\mathbb R\) is feasible, and the eigenvalues of \(S_\phi\) are the positive eigenvalues of \(G_\phi\).

Write \(R=\prod_{j=1}^m r_j>0\), \(t=\cos\phi\), and \(F_p(t)=\operatorname{tr}(S_\phi^p)=\|S_\phi\|_{\mathcal S_p}^{p}\) for every real \(p>0\). This is well defined as a function of \(t\) alone. Its complete phase-ordering law is:

\[
\operatorname{sgn}(F_p(t_2)-F_p(t_1))
=\operatorname{sgn}\!\left(\prod_{k=1}^{m-1}(p-k)\right)
\quad(-1\le t_1<t_2\le1),
\]
whenever \(p\notin\{1,\ldots,m-1\}\). For integer \(p=1,\ldots,m-1\), \(F_p\) is exactly phase independent. Thus, for all other positive exponents, the *unique extremal phase classes* are \(\phi\equiv0\) and \(\phi\equiv\pi\pmod{2\pi}\), with their maximum/minimum roles alternating across each of \(1,\ldots,m-1\). For the operator norm (\(p=\infty\)), \(\|S_\phi\|\) is strictly increasing in \(t\) and is maximized only at \(\phi\equiv0\).

There is also a quantitative finite-gap bound. Put \(\delta=\max_j(r_{j-1}+r_j)<1\), \(L=1-\delta\), \(U=1+\delta\), and \(A_{m,p}=4R\,|p(p-1)\cdots(p-m+1)|/(m-1)!\). For every \(p>0\) outside \(\{1,\ldots,m-1\}\),

\[
A_{m,p}\min\{L^{p-m},U^{p-m}\}
\le |F_p(1)-F_p(-1)|
\le A_{m,p}\max\{L^{p-m},U^{p-m}\}.
\]
The full finite-exponent sharp envelope is exactly the closed interval between \(F_p(-1)\) and \(F_p(1)\), each endpoint realized by a Gram matrix with the same pairwise overlap magnitudes. In particular, for \(p=m\), \(F_m(1)-F_m(-1)=4mR\).

## Assumptions and scope
The Gram matrix is concretely specified by \((G_\phi)_{jj}=1\), \((G_\phi)_{j,j+1}=(G_\phi)_{j+1,j}=r_j\) for \(1\le j<m\), \((G_\phi)_{m,1}=r_m e^{i\phi}\), and \((G_\phi)_{1,m}=r_m e^{-i\phi}\); all remaining entries are zero. The strict cyclic row-dominance assumption guarantees \(L I\preceq G_\phi\preceq U I\), hence positivity for every phase. By Gram factorization there are unit vectors \(v_j\) realizing each such matrix. The map \(V:\mathbb C^m\to\mathbb C^m\), \(Ve_j=v_j\), satisfies \(G_\phi=V^*V\) and \(S_\phi=VV^*\), so their spectra agree. For \(0<p<1\), \(\|\cdot\|_{\mathcal S_p}\) denotes the usual Schatten quasi-norm. No statement is made about general overlap graphs or amplitudes outside the stated sufficient positivity region.

## Proof
**1. Single phase-bearing determinant term.** Let \(\chi_t(\lambda)=\det(\lambda I-G_\phi)\). Expand by permutations. The undirected nonzero off-diagonal graph is a simple cycle. A contributing permutation can therefore consist only of fixed points and paired adjacent transpositions, *unless* it is one of the two oriented full \(m\)-cycles. Transpositions use each edge together with its complex conjugate and hence erase its phase. Each oriented full cycle contributes \(-R e^{i\phi}\) or \(-R e^{-i\phi}\). Accordingly,

\[\chi_t(\lambda)=Q(\lambda)-2Rt,\]
where \(Q\) is a real monic polynomial of degree \(m\) independent of \(t\). In particular, the spectrum depends only on \(\cos\phi\).

**2. Strict all-exponent order.** For a value \(t\) at which the positive roots \(\lambda_1(t),\ldots,\lambda_m(t)\) are distinct, implicit differentiation gives

\[\lambda_j'(t)=\frac{2R}{\chi_t'(\lambda_j(t))}.\]
Consequently,

\[
F_p'(t)=2Rp\sum_{j=1}^m
\frac{\lambda_j(t)^{p-1}}{\prod_{i\ne j}(\lambda_j(t)-\lambda_i(t))}
=2Rp\,[x^{p-1};\lambda_1(t),\ldots,\lambda_m(t)].
\]
The final expression is the divided difference of order \(m-1\). Its Hermite--Genocchi integral is

\[
F_p'(t)=2R p(p-1)\cdots(p-m+1)
\int_{\Delta_{m-1}}\!\left(\sum_{j=1}^m\alpha_j\lambda_j(t)\right)^{p-m}d\alpha,
\]
where \(\Delta_{m-1}=\{\alpha_j\ge0,\ \sum_j\alpha_j=1\}\), equipped with Lebesgue measure of total mass \(1/(m-1)!\). The integral is strictly positive for all \(p>0\), since every eigenvalue lies in \([L,U]\subset(0,\infty)\). This proves the stated sign wherever the roots are simple, and phase independence when \(p\in\{1,\ldots,m-1\}\).

The discriminant of \(Q(\lambda)-2Rt\) is a nonzero polynomial in \(t\): for sufficiently large complex \(t\), its \(m\) roots asymptotically separate as the roots of \(\lambda^m=2Rt\). Thus there are only finitely many exceptional \(t\) with repeated roots. Continuity of the symmetric spectral-power sum across these points proves strict order on the entire closed interval and phase independence at the indicated integer exponents.

**3. Exact extrema, gap, and operator norm.** Every \(t\in[-1,1]\) occurs as \(\cos\phi\) and is feasible by the uniform positivity estimate, so continuous strict order yields the full interval of attainable values and the endpoint equality cases. Integrating the divided-difference identity from \(-1\) to \(1\), using \(L\le\sum_j\alpha_j\lambda_j(t)\le U\) and the simplex volume \(1/(m-1)!\), yields the stated two-sided gap estimate. For \(p=m\), the integrand equals \(1\), giving the exact difference \(4mR\). Finally, the largest positive root of \(Q(\lambda)-2Rt\) is strictly increasing with \(t\) wherever it is simple because \(\chi_t'(\lambda_{\max})>0\). The same finite-exception continuity argument gives strict monotonicity of the operator norm.

## Verification
The companion `check_phase.py` symbolically verifies for four consecutive cycle lengths that all phase dependence in the characteristic polynomial is exactly \(-2R\cos\phi\), and numerically checks positive spectra, the signed Schatten-power difference over exponents crossing the integer thresholds, phase blindness of lower integer moments, and the exact \(p=m\) gap. Its 82 supplementary checks passed. These finite checks do not establish the theorem for arbitrary \(m\) or real \(p\); the determinant and divided-difference proof above does.

## Relationship to prior work
Chen, Ivanisvili, Madrid, and Wang (2026) prove a general almost-orthogonality inequality for Schatten sums, with constants determined by pairwise products of operators. For the rank-one projections here, those pairwise data depend only on the edge magnitudes and do not see the cycle phase. The result above determines precisely how that missing holonomy affects every Schatten exponent and gives sharp extremizing phase classes, rather than replacing the general inequality.

Mitchison and Jozsa (2003) describe three-state Gram spectra and establish monotonicity of *von Neumann entropy* in elementary symmetric coefficients; their appendix supplies the general divided-difference calculus used in the proof. Fannes and Vanpeteghem (2004) establish the necessity of three-state phases for unitary reconstruction. Zhang and Xie (2026) survey Bargmann invariants and Gram-phase geometry. The determinant expansion and integer-moment phase blindness of magnetic cycles are classical tools; the claimed contribution is their all-real-exponent strict phase ordering, sharp extrema, and quantitative gaps for heterogeneous positive cycle Gram matrices.

## Limitations
The result is a finite-rank, positive, single-cycle statement under strict cyclic row dominance. It does not optimize over variable edge magnitudes, assert comparable ordering for graphs with several independent cycles, or establish novelty against every historical magnetic-Jacobi reference. The explicit gap bounds are guaranteed rather than generally best possible. The all-exponent structural conclusion follows analytically; the companion program is supplementary, not an infinite proof. Independent scientific verification has not been performed.

## References
1. Z. Chen, P. Ivanisvili, J. Madrid, and H. Wang, *Carbery's inequality in the Schatten--von Neumann classes*, arXiv:2606.04116 (first submitted 2026-06-02), https://arxiv.org/abs/2606.04116.
2. G. Mitchison and R. Jozsa, *Towards a geometrical interpretation of quantum information compression*, arXiv:quant-ph/0309177 (2003), https://arxiv.org/abs/quant-ph/0309177.
3. M. Fannes and D. Vanpeteghem, *A three state invariant*, arXiv:quant-ph/0402045 (2004), https://arxiv.org/abs/quant-ph/0402045.
4. L. Zhang and B. Xie, *A Survey of Bargmann Invariants: Geometric Foundations and Applications*, arXiv:2601.01858 (first submitted 2026-01-05), https://arxiv.org/abs/2601.01858.
