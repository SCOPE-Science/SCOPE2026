# Arbitrary peripheral spectra over one fixed microscopic doubling map

## Finding
For each integer \(m\geq1\) and each real monic polynomial
\[p(z)=z^m+c_1z^{m-1}+\cdots+c_m,\]
there exists an explicit smooth mean-field-coupled, degree-two expanding circle-map family whose uniform equilibrium has the *same microscopic map* \(y\mapsto2y\pmod1\), independently of \(p\), while its macroscopic linear-response operator has precisely the roots of \(p\), with algebraic multiplicity, in the spectral region \(|z|>1/2\). On zero-average \(C^1\) densities the exact spectral radius is
\[r(L_p)=\max\left\{\frac12,\max_{p(\lambda)=0}|\lambda|\right\}.\]
The roots in the outer region have an explicit finite-dimensional Fourier realization and can be prescribed freely, including repeated, negative, or nonreal conjugate modes. This is a *linearized* spectral realization, not an assertion about nonlinear stability outside a neighborhood of equilibrium.

## Assumptions and scope
Let \(\mathbb T=\mathbb R/\mathbb Z\). Put \(a(y)=\cos(2\pi y)\), and define the mean-field observable and smooth forcing
\[M(\rho)=\int_{\mathbb T}a(y)\rho(y)\,dy,\qquad g_p(y)=\sum_{j=1}^m\frac{c_j}{\pi2^{j-1}}\sin(2\pi2^jy).\]
For a probability density \(\rho\) sufficiently close to the constant density \(\rho_*=1\) in \(C^2\), define
\[f_\rho(y)=2y+M(\rho)g_p(y)\pmod1,\qquad\mathcal F_p(\rho)=(f_\rho)_*\rho.\]
Choose the neighborhood so \(|M(\rho)|\|g_p'\|_\infty<1\); then \(f_\rho'(y)>1\) everywhere. There is no uniform neighborhood size asserted as \(p\) varies. The density \(1\) is fixed, with microscopic Lyapunov exponent \(\log2\). Work on the real mean-zero Banach space \(X=C^1_0(\mathbb T)=\{\eta\in C^1(\mathbb T):\int\eta=0\}\), complexified for spectral statements. The map \(\mathcal F_p\) admits the linear expansion at \(1\), along \(C^2\) perturbations, in the \(C^1\) target topology; the resulting bounded operator extends to \(X\). We do **not** assert that \(\mathcal F_p\) is Fréchet differentiable as a \(C^1\)-to-\(C^1\) self-map.

## Proof
**1. Differential.** The unperturbed Perron–Frobenius operator is
\[(P\eta)(x)=\frac12\left[\eta(x/2)+\eta((x+1)/2)\right].\]
For a zero-average smooth direction \(\eta\), write \(\rho_\epsilon=1+\epsilon\eta\). Then \(M(\rho_\epsilon)=\epsilon M(\eta)\). For a smooth test function \(\phi\), differentiate the pushforward identity
\[\int\phi\,\mathcal F_p(\rho_\epsilon)=\int\phi(2y+\epsilon M(\eta)g_p(y))(1+\epsilon\eta(y))\,dy.\]
Integration by parts gives the coefficient density
\[L_p\eta=P\eta-M(\eta)(Pg_p)'\tag{1}.\]
The inverse branches of \(f_\rho\) depend smoothly on the scalar \(M(\rho)\), and Taylor expansion of the two branch densities (including their first derivatives) gives, for sufficiently small \(\eta\in C^2_0\),
\[\|\mathcal F_p(1+\eta)-1-L_p\eta\|_{C^1}\leq C_p\|\eta\|_{C^2}^2.\]
Thus (1) is a justified strong-to-weaker-topology linearization; it is bounded on \(X\).

**2. Fourier companion sector.** Define \(e_k(x)=2\cos(2\pi2^kx)\) for \(0\leq k\leq m-1\) and \(V_m=\operatorname{span}\{e_0,\ldots,e_{m-1}\}\). Orthogonality and the doubling branches imply
\[M(e_0)=1,\quad M(e_k)=0\ (k\geq1),\quad Pe_0=0,\quad Pe_k=e_{k-1}\ (k\geq1).\]
Differentiating the forcing and applying \(P\) yields \((Pg_p)'=\sum_{j=1}^m c_je_{j-1}\). Hence
\[L_pe_0=-\sum_{j=1}^mc_je_{j-1},\qquad L_pe_k=e_{k-1}\quad(1\leq k<m).\]
In the ordered basis \((e_0,\ldots,e_{m-1})\), \(L_p|_{V_m}\) is the companion matrix with first column \((-c_1,\ldots,-c_m)^{\mathsf T}\), ones immediately above the main diagonal, and remaining entries zero. Expansion of its determinant along the last row, or the standard companion recurrence, gives \(\det(zI-L_p|_{V_m})=p(z)\), including algebraic multiplicities.

**3. No additional outer spectrum.** For \(\eta\in X\), \((P^n\eta)'=2^{-n}P^n\eta'\), and \(P^n\eta\) has mean zero. A continuous mean-zero real-valued function has a zero; for a complex function use the integral representation and its oscillation bound. In both cases \(\|P^n\eta\|_\infty\leq\|(P^n\eta)'\|_\infty\). Therefore \(\|P^n\|_{X\to X}\leq2^{1-n}\) and the resolvent \((z-P)^{-1}\) exists for \(|z|>1/2\). Equation (1) differs from \(P\) by a rank-one operator with range in \(V_m\), a \(P\)-invariant subspace. For \(|z|>1/2\), \(z-L_p\) is invertible precisely when its restriction to \(V_m\) is invertible: apply the invertible \(z-P\) and its finite-rank resolvent factorization. Since \((z-P)^{-1}\) preserves \(V_m\), every associated eigenvector and generalized eigenvector lies in \(V_m\). Thus the complete outer spectral multiset is exactly \(\{\lambda:p(\lambda)=0,\ |\lambda|>1/2\}\).

**4. Sharp spectral-radius floor.** The preceding bounds give \(r(L_p)\leq\max\{1/2,\max|\lambda|\}\). To prove the reverse inequality for the floor, fix \(n\) and take \(h_n(x)=2\cos(2\pi2^{2n+2}x)\). Along the first \(n\) iterates, \(M(P^jh_n)=0\), so \(L_p^nh_n=P^nh_n\). The ratio of their \(C^1\) norms is at least \(2^{-n-1}\). Hence \(\|L_p^n\|^{1/n}\geq(2^{-n-1})^{1/n}\to1/2\). Each root of \(p\) is already an eigenvalue on \(V_m\). This proves the displayed spectral-radius equality.

## Verification
An accompanying standard-library-only Python checker verifies the companion characteristic polynomials exactly for two degree-three examples and independently evaluates the two-sided directional pushforward derivative against all nine Fourier test pairs per example by periodic-grid quadrature. The numerical checks supplement, not replace, the universal proof.

For illustration, choosing the root multiset \(\{6/5,-4/5,3/4\}\) produces a simple positive growing mode, an alternating decaying mode, and a positive decaying mode while the equilibrium microscopic map remains doubling. Choosing \(\{6/5,3i/4,-3i/4\}\) instead produces oscillatory macroscopic modes. Both are exterior to \(|z|=1/2\). The cosine observable reads every nonzero eigenvalue mode of the companion matrix: an eigenvector with vanishing \(e_0\)-coordinate would, from the successive coordinate equations, vanish identically.

## Relationship to prior work
Ahmad and Tanzi (arXiv:2609.27484v1, publicly submitted 2026-09-23) introduce observable Lyapunov exponents and relate their mean-field limits to the differential of the self-consistent transfer operator. Castorrini, Galatolo and Tanzi (arXiv:2407.09314v1) supply a rigorous strong/weak topology framework for that differential and sufficient spectral criteria for equilibrium stability. Neither inspected presentation gives a prescribed-polynomial realization at a common fixed microscopic doubling map. The nearest public mathematical record, *Arithmetic resonance and exact linear-response radius for mean-field expanding circle maps*, treats one sine forcing harmonic and a scalar spectral-radius resonance; a multi-harmonic companion polynomial, prescribed nonreal modes, and the full outer spectral multiset are not consequences of that stated single-harmonic formula. Galatolo’s 2022 optimal-coupling result (Section 11) optimizes the equilibrium expectation of a prescribed observable, not the arbitrary characteristic polynomial of the equilibrium differential. The complete text of the nearest mathematical record was not accessible for comparison, and its possible unreported extensions remain a priority risk.

## Limitations
The construction engineers the *linearized* operator near the uniform equilibrium, not global nonlinear statistical dynamics, a globally expanding family for arbitrary densities, or finite-population Lyapunov limits. Spectral radius is not, without further hypotheses, a nonlinear instability/bifurcation certificate. The operator is formulated on zero-average \(C^1\) functions with its derivative justified via \(C^2\)-to-\(C^1\) linearization; no differentiability assertion on identical Banach spaces is intended. This example does not classify the entire spectrum inside \(|z|\leq1/2\). Priority remains conditional on available literature and the inaccessible highly related full text.

## References
1. M. Ahmad and M. Tanzi, *Observable Lyapunov Exponents for Globally Coupled Maps in the Mean-Field Limit*, arXiv:2609.27484v1 (2026-09-23), https://arxiv.org/abs/2609.27484.
2. R. Castorrini, S. Galatolo and M. Tanzi, *The differential of self-consistent transfer operators and the local convergence to equilibrium of mean field strongly coupled dynamical systems*, arXiv:2407.09314v1 (2024-07-12), https://arxiv.org/abs/2407.09314, Journal of Nonlinear Science 35, 78 (2025), https://doi.org/10.1007/s00332-025-10177-0.
3. M. Tanzi, *Mean-field coupled systems and self-consistent transfer operators: a review*, Bollettino dell'Unione Matematica Italiana 16 (2023), https://doi.org/10.1007/s40574-023-00350-2.
4. *Arithmetic resonance and exact linear-response radius for mean-field expanding circle maps*, indexed mathematical-record entry, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-arithmetic-resonance-and-exact-linear-response-radius-for-mean-f--3ccc7c7409d3 (abstract/summary only accessible during comparison).
5. S. Galatolo, *Self-Consistent Transfer Operators: Invariant Measures, Convergence to Equilibrium, Linear Response and Control of the Statistical Properties*, Communications in Mathematical Physics 395 (2022), Section 11, https://doi.org/10.1007/s00220-022-04444-4.
