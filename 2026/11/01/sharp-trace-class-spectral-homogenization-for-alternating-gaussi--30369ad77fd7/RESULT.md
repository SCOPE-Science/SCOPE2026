# Sharp trace-class spectral homogenization for alternating Gaussian annuli

## Finding
An infinite alternating family of occupied and vacant annuli has infinite planar area, yet its analytic Gaussian localization operator becomes a trace-class perturbation of a scalar. The eigenvalues converge exponentially to one half, retaining a sharp, sign-changing oscillation. The full spectral bias has the exact trace \(1/4\).

Let \(T\) be the operator defined below. Its eigenvalues \(\lambda_n\) have generating function
\[
\sum_{n=0}^\infty\lambda_n w^n=\frac{1}{(1-w)(1+e^{w-1})}\quad(|w|<1).
\]
Furthermore,
\[
T-\frac12 I\in\mathcal S_1,\quad \operatorname{Tr}\left(T-\frac12 I\right)=\frac14,\quad\sigma_{\mathrm{ess}}(T)=\{1/2\}.
\]
Set \(\rho=(1+\pi^2)^{-1/2}\), \(\theta=\arctan\pi\), \(\rho_3=(1+9\pi^2)^{-1/2}\). The sharp high-degree law is
\[
\lambda_n-\frac12=\frac2\pi\rho^{n+1}\sin((n+1)\theta)+O(\rho_3^{n+1}).
\]
The angle \(\theta/\pi\) is irrational. Therefore infinitely many eigenvalues lie strictly on either side of the homogenized value, and
\[
\limsup_{n\to\infty}\frac{\lambda_n-1/2}{\rho^{n+1}}=\frac2\pi,\quad
\liminf_{n\to\infty}\frac{\lambda_n-1/2}{\rho^{n+1}}=-\frac2\pi.
\]

## Assumptions and scope
The analytic Bargmann--Fock space \(\mathcal F^2(\mathbb C)\) uses \(d\gamma(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\). Its orthonormal monomials are \(e_n(z)=z^n/\sqrt{n!}\), \(n=0,1,\ldots\). The symbol is the bounded measurable indicator
\[
a(z)=\mathbf1_{\{\,|z|^2\in\bigcup_{j=0}^{\infty}[2j,2j+1)\,\}}.
\]
Define \(T f=P(af)\), where \(P:L^2(\mathbb C,d\gamma)\to\mathcal F^2(\mathbb C)\) is the orthogonal projection. This is an analytic (not harmonic) Fock-space result with exactly unit-width occupied bands alternating with unit-width gaps in the variable \(|z|^2\). The value of \(a\) on circle boundaries is immaterial.

## Proof
**1. Complete diagonalization.** Radiality and angular orthogonality give \(T e_n=\lambda_n e_n\), with
\[
\lambda_n=\frac1{n!}\int_0^\infty b(t)e^{-t}t^n\,dt=\frac1{n!}\sum_{j=0}^\infty\int_{2j}^{2j+1}e^{-t}t^n\,dt,
\]
where \(b(t)=\mathbf1_{\bigcup_{j\ge0}[2j,2j+1)}(t)\). All eigenvalues lie in \((0,1)\).

**2. Exact generating function.** For \(|w|<1\), absolute convergence and Tonelli/Fubini allow summation of the gamma moments, yielding
\[
\sum_{n=0}^{\infty}\lambda_n w^n=\int_0^\infty b(t)e^{-(1-w)t}\,dt
=\sum_{j=0}^{\infty}\int_{2j}^{2j+1}e^{-(1-w)t}\,dt
=\frac{1-e^{-(1-w)}}{(1-w)(1-e^{-2(1-w)})}
=\frac1{(1-w)(1+e^{w-1})}.
\]

**3. Fourier--Gamma identity with justified interchange.** The square wave \(b\) has mean \(1/2\) and its sine series (interpreted initially through Fejér means) is
\[
b(t)=\frac12+\frac2\pi\sum_{k\ge1,\ k\ \mathrm{odd}}\frac{\sin(\pi k t)}k
\]
for almost every \(t>0\). Its Fejér means are uniformly bounded between zero and one and converge almost everywhere; dominated convergence against \(e^{-t}t^n/n!\) justifies integration. Integration of each harmonic uses
\[
\frac1{n!}\int_0^\infty e^{-t}t^n e^{i\pi k t}\,dt=(1-i\pi k)^{-n-1}.
\]
The resulting series is absolutely convergent for every \(n\ge0\), because the summands are \(O(k^{-n-2})\). Thus
\[
\lambda_n-\frac12=\frac2\pi\sum_{k\ge1,\ k\mathrm{\ odd}}\frac1k\operatorname{Im}(1-i\pi k)^{-n-1}.
\]
The \(k=1\) term is exactly \((2/\pi)\rho^{n+1}\sin((n+1)\theta)\). For the remaining odd \(k\ge3\), write \(\rho_k=(1+\pi^2k^2)^{-1/2}\). For \(n\ge1\),
\[
\sum_{k\ge3,\ k\mathrm{\ odd}}\frac{\rho_k^{n+1}}k
\le \rho_3^{n-1}\sum_{k\ge3,\ k\mathrm{\ odd}}\frac{\rho_k^2}k=O(\rho_3^{n+1}),
\]
where the last constant absorbs \(\rho_3^{-2}\) and the displayed series converges. This proves the stated sharp asymptotic and a uniform geometric bound on \(|\lambda_n-1/2|\).

**4. Trace class and exact trace.** The geometric bound proves \(\sum_{n\ge0}|\lambda_n-1/2|<\infty\), hence the diagonal operator \(T-\tfrac12 I\) belongs to \(\mathcal S_1\). Subtracting the scalar generating series and invoking absolute summability,
\[
\sum_{n=0}^\infty(\lambda_n-\tfrac12)=\lim_{w\uparrow1}\frac1{1-w}\left(\frac1{1+e^{w-1}}-\frac12\right)=\frac14,
\]
because \((1+e^{-h})^{-1}=1/2+h/4+O(h^3)\) as \(h\to0\). A scalar plus a compact diagonal operator has essential spectrum consisting of the scalar alone.

**5. Irrationality and both sharp oscillation envelopes.** The number \(\theta=\arctan\pi\) satisfies \(\tan\theta=\pi\). If \(\theta/\pi\) were rational, \(e^{2i\theta}\) would be a root of unity and hence algebraic. But \(\tan\theta=(e^{2i\theta}-1)/(i(e^{2i\theta}+1))\) would then be algebraic, contradicting transcendence of \(\pi\). Thus \(\theta/\pi\) is irrational. Density of the irrational rotation modulo \(2\pi\), together with \(\rho_3/\rho<1\), proves the two normalized envelope limits and infinitely many deviations of each sign.

## Verification
A standalone high-precision checker evaluates the exact generating-function coefficients, separately evaluated incomplete-gamma ring integrals, Fourier--Gamma truncations with tail bounds, asymptotic leading terms and the convergent trace. It executes 71 deterministic assertions. The proof above does not depend on finite sampling, on a numerical zero search, or on extrapolating checked degrees to infinity.

## Relationship to prior work
Esmeral--Maximenko (2015 preprint) and Dewage--Ólafsson (2021 preprint) establish general radial and quasi-radial Fock Toeplitz diagonalization and operator-algebra descriptions. In particular, the gamma-moment eigenvalue formula is previously known and is not a claim of novelty. Galbis (2021) proves bounds for integrable radial symbols, while the present indicator has infinite planar support and is not integrable. The contribution here is the simultaneous explicit generating function, trace-class scalar homogenization with nonzero exact trace, and sharp infinitely sign-changing high-mode asymptotic for this canonical alternating infinite annular aperture. The literature comparison does not certify absolute historical priority.

## Limitations
The result applies only to analytic Gaussian Fock space in one complex variable and the stated period-two binary indicator in squared radius; it does not assert arbitrary radial-mask behavior, noisy measurement stability, or any general inverse reconstruction theorem. The original gamma-eigenvalue representation is established background. The exact theorem is mathematically derived here but has not undergone independent external validation; unexamined historical sources could cover the explicit specialization.

## References
1. K. Esmeral and E. A. Maximenko, *Radial Toeplitz operators on the Fock space and square-root-slowly oscillating sequences*, arXiv:1505.07906v1 (first public 2015-05-29), https://arxiv.org/html/1505.07906v1 .
2. V. Dewage and G. Ólafsson, *Toeplitz operators on the Fock space with quasi-radial symbols*, arXiv:2107.01465v1 (first public 2021-07-03), https://arxiv.org/abs/2107.01465 .
3. A. Galbis, *Norm estimates for selfadjoint Toeplitz operators on the Fock space*, arXiv:2102.02031v1 (first public 2021-02-03), https://arxiv.org/abs/2102.02031 .
