# Hermite law and asymptotic corner rigidity for total-degree Legendre projections on cubes

## Finding
Fix an integer \(m\ge2\). Equip \(Q_d=[-1,1]^d\) with normalized Lebesgue measure \(\mu_d=\bigotimes_{i=1}^d(dt_i/2)\), and let \(P_{d,m}\) be the \(L^2(\mu_d)\)-orthogonal projection onto all real polynomials of **total** degree at most \(m\). For \(a\in Q_d\), let \(\Lambda_{d,m}(a)\) be the sharp norm of the evaluation functional \(f\mapsto(P_{d,m}f)(a)\) on \(C(Q_d)\) in the uniform norm.

Let \(Z\) be standard normal, let the *probabilists'* Hermite polynomials satisfy \(H_0(z)=1\), \(H_1(z)=z\) and \(H_{j+1}(z)=zH_j(z)-jH_{j-1}(z)\), and set
\[
 c_m=\frac{3^{m/2}}{m!}\,\mathbb E|H_m(Z)|>0.
\]
Then the following **uniform local asymptotic law** holds:
\[
 \lim_{d\to\infty}\sup_{a\in Q_d}
 \left|\frac{\Lambda_{d,m}(a)}{d^{m/2}}
 -c_m\left(\frac1d\sum_{i=1}^d a_i^2\right)^{m/2}\right|=0.
\]
Consequently the sharp operator norm obeys
\[
 \lim_{d\to\infty}\frac{\|P_{d,m}\|_{C(Q_d)\to C(Q_d)}}{d^{m/2}}=c_m.
\]
A sequence \(a^{(d)}\in Q_d\) is asymptotically norm-maximizing, in the precise sense that \(\Lambda_{d,m}(a^{(d)})/\|P_{d,m}\|\to1\), **if and only if**
\[
 \frac1d\sum_{i=1}^d\bigl(1-(a_i^{(d)})^2\bigr)\longrightarrow0.
\]
In particular every cube vertex is asymptotically maximizing, while any family with a positive limiting mean-square deficit is separated from the sharp limit. The quadratic example has the explicit coefficient
\[
 c_2=\frac{6}{\sqrt{2\pi e}}=1.451824347115\ldots.
\]
This is an asymptotic result; it does **not** claim that a vertex is exactly maximizing in each finite dimension.

## Assumptions and scope
The dimension \(d\) tends through positive integers with the total degree \(m\ge2\) fixed; the measure is independent uniform probability on the coordinates, with no boundary weight, interpolation nodes, or cubature discretization. Real and complex operator norms coincide because the reproducing kernel is real and evaluation norms equal its absolute integral. Every polynomial projection is defined for bounded measurable functions and has the same uniform operator norm when restricted to continuous inputs. The result is about this specified \(L^2\)-orthogonal projector, not the minimum norm over all possible projections onto the polynomial subspace.

Write \(L_j\) for the ordinary Legendre polynomial with \(L_j(1)=1\), and define \(\phi_j(t)=\sqrt{2j+1}\,L_j(t)\). These polynomials are orthonormal for \(dt/2\), and \(|\phi_j(t)|\le\sqrt{2j+1}\) on \([-1,1]\). The reproducing kernel is
\[
 K_{d,m}(a,y)=\sum_{\alpha\in\mathbb N_0^d:\,|\alpha|\le m}\prod_{i=1}^d\phi_{\alpha_i}(a_i)\phi_{\alpha_i}(y_i),
 \qquad \Lambda_{d,m}(a)=\int_{Q_d}|K_{d,m}(a,y)|\,d\mu_d(y).
\]

## Proof
**1. Sharp evaluation formula.** Orthonormal expansion gives \((P_{d,m}f)(a)=\int f(y)K_{d,m}(a,y)\,d\mu_d(y)\), so \(\Lambda_{d,m}(a)\) is an upper bound for evaluation. Conversely \(f_n(y)=\tanh(nK_{d,m}(a,y))\) is continuous, has uniform norm at most one, and converges pointwise to the kernel sign away from its zeros; dominated convergence yields equality. Continuity in \(a\) and compactness show that the global operator norm is \(\max_{a\in Q_d}\Lambda_{d,m}(a)\).

**2. The squarefree top-degree term.** Let \(Y_1,\ldots,Y_d\) be independent uniform random variables on \([-1,1]\). The sum of the reproducing-kernel terms with exactly \(m\) distinct degree-one coordinates is
\[
 T_{d,m}(a,Y)=\sum_{\substack{S\subseteq\{1,\ldots,d\}\\|S|=m}}\prod_{i\in S}3a_iY_i.
\]
Every other multi-index in the kernel expansion has at most \(m-1\) nonzero entries; for fixed \(m\), their number is at most \(C_m d^{m-1}\). By orthogonality of the product Legendre basis and the bounds on \(\phi_j\), uniformly over \(a\in Q_d\),
\[
 \mathbb E|K_{d,m}(a,Y)-T_{d,m}(a,Y)|^2\le C'_m d^{m-1}.
\]
Thus replacing \(K_{d,m}\) by \(T_{d,m}\) changes the normalized absolute expectation by at most \(C''_m d^{-1/2}\), uniformly in \(a\). No finite-sample approximation is used in this step.

**3. A triangular-array Hermite limit.** For an arbitrary sequence of evaluation points \(a^{(d)}\in Q_d\), pass to a subsequence on which
\[
 s_d=\frac1d\sum_{i=1}^d(a_i^{(d)})^2\longrightarrow s\in[0,1].
\]
Define \(W_i=\sqrt3Y_i\) and \(b_{d,i}=\sqrt3a_i^{(d)}/\sqrt d\). Thus the \(W_i\) are independent, centered, variance one and bounded, and \(|b_{d,i}W_i|\le3/\sqrt d\). If \(e_m\) denotes the \(m\)-th elementary symmetric polynomial, then
\[
 d^{-m/2}T_{d,m}(a^{(d)},Y)=e_m(b_{d,1}W_1,\ldots,b_{d,d}W_d).
\]
Let \(p_j=\sum_i(b_{d,i}W_i)^j\). The Lindeberg central limit theorem yields \(p_1\Rightarrow\sqrt{3s}\,Z\); this is also true for \(s=0\), where convergence is in probability to zero. Independence and bounded fourth moments yield
\[
 p_2-\sum_i b_{d,i}^2\longrightarrow0\quad\text{in }L^2,
 \qquad\sum_i b_{d,i}^2=3s_d\to3s.
\]
For every fixed \(j\ge3\), \(|p_j|\le 3^j d^{1-j/2}\to0\). Newton's identities, equivalently the finite generating identity
\[
 \sum_{j=0}^{d}e_j t^j
 =\exp\left(\sum_{j\ge1}\frac{(-1)^{j-1}}j p_jt^j\right)
 \quad\text{as an identity of formal power series},
\]
show that for each fixed \(m\), the right-hand coefficient converges in distribution to the \(t^m\) coefficient of \(\exp(\sqrt{3s}\,Zt-3st^2/2)\), namely \((3s)^{m/2}H_m(Z)/m!\). This conclusion also covers \(s=0\) by the same polynomial coefficient identity.

**4. Absolute expectations and uniformity.** Orthogonality of distinct squarefree monomials gives
\[
 \mathbb E\left|e_m(b_{d,1}W_1,\ldots,b_{d,d}W_d)\right|^2
 =\sum_{|S|=m}\prod_{i\in S}b_{d,i}^2
 \le\frac{(\sum_i b_{d,i}^2)^m}{m!}\le\frac{3^m}{m!}.
\]
This common \(L^2\) bound implies uniform integrability, so absolute expectations converge to \((3s)^{m/2}\mathbb E|H_m(Z)|/m!\). Combined with step 2 this proves the required local formula along every sequence for which \(s_d\) converges. If the displayed uniform supremum in the finding failed, one could choose a sequence of points violating it and pass to a convergent subsequence of \(s_d\), contradicting the just-proved statement. This proves uniformity without assuming that the maximizing evaluation points have any prescribed symmetry.

**5. Global sharpness and rigidity.** Since \(0\le s_d\le1\), the local formula gives \(\limsup d^{-m/2}\|P_{d,m}\|\le c_m\). At any corner, all coordinates have square one, so \(\liminf\ge c_m\). The limit is therefore exactly \(c_m\). Moreover \(c_m>0\) and \(s\mapsto s^{m/2}\) is strictly increasing on \([0,1]\); by uniformity, the ratio of an evaluation norm to the global norm tends to one precisely when \(s_d\to1\), which is the stated mean-square condition.

**6. Quadratic constant.** With \(H_2(z)=z^2-1\) and standard-normal density \(\varphi(z)=e^{-z^2/2}/\sqrt{2\pi}\), direct integration at the two zeros gives \(\mathbb E|H_2(Z)|=4\varphi(1)\). Substituting into the coefficient formula yields \(c_2=6/\sqrt{2\pi e}\).

## Verification
The accompanying standalone numerical checker evaluates the entire truncated Legendre product kernel by a degree-coefficient recurrence, independently compares the exact quadratic closed expression in 120 random configurations, and checks normalized local evaluations at corners and at two interior-point profiles for dimensions 16, 64, and 256 and degrees 1, 2, and 3. Its deterministic outputs agree with the stated Hermite coefficients within the documented sampling tolerances. These finite computations diagnose formula and normalization errors only; the asymptotic and uniform claims are proved in steps 2–5 rather than inferred from numerical experiments.

## Relationship to prior work
De Marchi–Vianello–Xu (2008) describe total-degree orthogonal polynomial projections and hyperinterpolation on product Chebyshev cubes, with constructive cubature in three variables. De Marchi–Sommariva–Vianello (2014) give product Jacobi reproducing kernels and estimates through their diagonal Christoffel functions; their continuous Legendre case provides the relevant orthonormal basis and a general Cauchy–Schwarz upper bound, but not this sharp high-dimensional absolute-kernel limit. In particular a bound from \(\sqrt{K_{d,m}(a,a)}\) has corner leading constant \(3^{m/2}/\sqrt{m!}\), strictly larger than \(c_m\) for \(m\ge1\). Trefethen (2016) studies analytic approximation rates associated with total, Euclidean, and maximal degrees rather than the norm of this fixed-degree projector. Later work on Boolean-cube and complex polynomial projection constants concerns different measures or subspaces. The displayed uniform law and rigidity conclusion are not implied by those identified statements.

## Limitations
The limit fixes \(m\) while \(d\to\infty\). Neither a uniform result for growing \(m\), a finite-\(d\) exact norm, nor finite-dimensional vertex maximality is asserted. The result concerns product **uniform** measures and ordinary Legendre polynomials; Chebyshev-weighted or correlated measures need separate analysis. The comparison with published literature cannot exclude unindexed or differently named equivalent results. One closely related 2014 paper on Chebyshev hyperinterpolation was accessible only through its abstract, not a complete text; it has a different measure and studies a different asymptotic regime.

## References
1. S. De Marchi, M. Vianello, Y. Xu, *New cubature formulae and hyperinterpolation in three variables*, arXiv:0805.3529v1, made public 22 May 2008, https://arxiv.org/abs/0805.3529.
2. S. De Marchi, A. Sommariva, M. Vianello, *Multivariate Christoffel functions and hyperinterpolation*, Dolomites Research Notes on Approximation **7** (2014), 26–33, DOI:10.14658/pupj-drna-2014-Special_Issue-6.
3. L. N. Trefethen, *Multivariate polynomial approximation in the hypercube*, arXiv:1608.02216v1, made public 7 August 2016, https://arxiv.org/abs/1608.02216.
4. H. Wang, K. Wang, X. Wang, *On the norm of the hyperinterpolation operator on the d-dimensional cube*, Computers & Mathematics with Applications **68** (2014), 632–638, DOI:10.1016/j.camwa.2014.07.009 (abstract inspected; full text unavailable).
5. A. Defant, D. Galicer, M. Mansilla, M. Mastyło, S. Muro, *Projection constants for spaces of multivariate polynomials*, arXiv:2208.06467v1 (2022), https://arxiv.org/abs/2208.06467 (abstract, contents, and relevant scope inspected).
