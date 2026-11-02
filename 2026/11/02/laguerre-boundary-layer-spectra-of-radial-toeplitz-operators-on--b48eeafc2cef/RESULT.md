# Laguerre boundary-layer spectra of radial Toeplitz operators on polyanalytic Bergman spaces

## Finding

For every integer \(q\ge 2\), every \(\alpha>-1\), and every positive boundary order \(\sigma>0\), a bounded radial Toeplitz symbol with nonzero asymptotic coefficient \(a(t)=c(1-t)^\sigma+o((1-t)^\sigma)\), \(c\in\mathbb C\setminus\{0\}\), produces a compact operator on the full weighted \(q\)-analytic Bergman space of the unit disk. Its entire ordered singular-value sequence obeys the exact limit

\[
\lim_{N\to\infty}N^\sigma s_N(T_a)=|c|\left(\sum_{j=1}^{q}\nu_j^{1/\sigma}\right)^\sigma,
\]

where \(\nu_1,\ldots,\nu_q>0\) are the eigenvalues of the explicit Laguerre moment matrix

\[
C_{jk}^{(\alpha,\sigma)}=\sqrt{\frac{j!k!}{\Gamma(j+\alpha+1)\Gamma(k+\alpha+1)}}\int_0^\infty y^{\alpha+\sigma}e^{-y}L_j^{(\alpha)}(y)L_k^{(\alpha)}(y)\,dy,\quad 0\le j,k<q.
\]

In particular, \(T_a\in\mathcal S_p\) exactly when \(p>1/\sigma\), and at the excluded endpoint

\[
\lim_{N\to\infty}\frac1{\log N}\sum_{n=1}^{N}s_n(T_a)^{1/\sigma}=|c|^{1/\sigma}\sum_{j=1}^q\nu_j^{1/\sigma}.
\]

The especially natural first-order boundary zero has an elementary coefficient: for \(\sigma=1\), the \(\nu_j\) are the positive zeros of \(L_q^{(\alpha)}\), and

\[
\boxed{\lim_{N\to\infty}N s_N(T_a)=|c|q(q+\alpha).}
\]

For order \(q=2\), the Laguerre matrix for any \(\sigma>0\) is explicitly

\[
C^{(\alpha,\sigma)}=\frac{\Gamma(\alpha+\sigma+1)}{\Gamma(\alpha+1)}
\begin{pmatrix}
1&-\sigma/\sqrt{\alpha+1}\\
-\sigma/\sqrt{\alpha+1}&1+\sigma(\sigma+1)/(\alpha+1)
\end{pmatrix}.
\]

This matrix is positive definite, so both spectral branches survive the boundary limit.

## Assumptions and scope

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) and \(d\mu_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha\,dA(z)/\pi\), where \(dA\) is planar Lebesgue area. The **full** polyanalytic Bergman space \(\mathcal A^2_{q,\alpha}(\mathbb D)\) is the closed subspace of \(L^2(\mathbb D,d\mu_\alpha)\) consisting of functions satisfying \(\partial_{\overline z}^{q}f=0\) distributionally. It includes all analytic and lower-polyanalytic orders; no subtraction of an order-\((q-1)\) subspace is intended.

For a bounded measurable function \(a:[0,1)\to\mathbb C\), define \(T_af=P_{q,\alpha}[a(|z|^2)f]\), where \(P_{q,\alpha}\) is the orthogonal projection onto this space. Assume \(\lim_{t\uparrow1}a(t)/(1-t)^\sigma=c\ne0\), with fixed \(q\ge2\), \(\alpha>-1\), \(\sigma>0\). No differentiability or reality/positivity assumption on \(a\) is needed. Singular values are ordered nonincreasingly and counted with multiplicities. \(L_j^{(\alpha)}\) is the standard generalized Laguerre polynomial, positive at zero.

## Proof

**Step 1: radial blocks.** The disk-polynomial decomposition of Barrera-Castelán, Maximenko and Ramos-Vazquez splits \(\mathcal A^2_{q,\alpha}\) into finitely many low negative-angular-frequency blocks and full \(q\)-dimensional angular-frequency blocks indexed by integers \(\xi\ge0\). Since radial symbols preserve angular frequency, \(T_a\) is the orthogonal direct sum of their compressed multiplication matrices. In a suitable sign-normalized Jacobi basis the \(\xi\)-block is the degree-\(<q\) matrix of multiplication by \(a(t)\) on polynomials in \(t=|z|^2\) for the probability measure

\[
\frac{t^\xi(1-t)^\alpha}{B(\xi+1,\alpha+1)}\,dt,\qquad 0<t<1.
\]

Only finitely many exceptional blocks have negative \(\xi\), so they do not influence tail asymptotics.

**Step 2: a Gamma scaling limit including polynomial bases.** If \(U_\xi\) has that beta distribution and \(Y_\xi=\xi(1-U_\xi)\), then for every fixed real \(r\ge0\)

\[
\mathbb E[Y_\xi^r]=\xi^r\frac{\Gamma(\alpha+r+1)}{\Gamma(\alpha+1)}\frac{\Gamma(\xi+\alpha+2)}{\Gamma(\xi+\alpha+r+2)}\longrightarrow\frac{\Gamma(\alpha+r+1)}{\Gamma(\alpha+1)}.
\]

These are the moments of the probability law \(y^\alpha e^{-y}dy/\Gamma(\alpha+1)\). All fixed higher moments are uniformly bounded, and the probability laws converge weakly to this Gamma law. Since \(q\) is fixed and every limiting Hankel moment determinant is strictly positive, Gram–Schmidt is continuous in the finitely many moments involved. Consequently, the degree-\(j\) beta-orthonormal Jacobi polynomial in \(Y_\xi\), chosen positive at \(0\), converges coefficientwise to

\[
p_j(y)=\sqrt{\frac{\Gamma(\alpha+1)j!}{\Gamma(j+\alpha+1)}}L_j^{(\alpha)}(y),\quad 0\le j<q.
\]

**Step 3: boundary-layer matrix.** The symbol hypothesis and boundedness imply a global estimate \(|a(1-u)|\le C u^\sigma\) for \(0<u\le1\). Hence \(\xi^\sigma|a(1-Y_\xi/\xi)|\le C Y_\xi^\sigma\). Fixed-degree polynomial coefficient bounds from Step 2 and uniform higher moments from Step 2 give uniform integrability of all \(q^2\) matrix integrands. Their pointwise limit is \(cy^\sigma p_j(y)p_k(y)\), and therefore

\[
\xi^\sigma M_\xi\longrightarrow c C^{(\alpha,\sigma)}
\]

in matrix norm. For nonzero \(v\in\mathbb C^q\),

\[
v^*Cv=\frac1{\Gamma(\alpha+1)}\int_0^\infty y^{\alpha+\sigma}e^{-y}\left|\sum_{j=0}^{q-1}v_jp_j(y)\right|^2dy>0,
\]

so \(C\) has \(q\) strictly positive eigenvalues. This also proves \(\|M_\xi\|\to0\) and compactness, since the finitely many negative-frequency blocks are finite-dimensional.

**Step 4: order the singular values and identify the sharp coefficient.** Matrix-norm convergence and continuity of finite-dimensional singular values imply, for each of the \(q\) branches counted with multiplicity,

\[
s_j(M_\xi)=|c|\nu_j\xi^{-\sigma}(1+o(1)),\qquad \xi\to\infty.
\]

Because there are finitely many branches, the number \(\mathcal N(\varepsilon)\) of singular values of \(T_a\) exceeding \(\varepsilon\) satisfies

\[
\mathcal N(\varepsilon)\sim |c|^{1/\sigma}\varepsilon^{-1/\sigma}\sum_{j=1}^q\nu_j^{1/\sigma}\quad(\varepsilon\downarrow0).
\]

Inverting this monotone counting relation gives the displayed ordered \(s_N\) limit. Comparison with the \(p\)-series proves the Schatten dichotomy. At \(p=1/\sigma\), the same limit says \(n s_n(T_a)^p\to |c|^p\sum_j\nu_j^p\); summing against \(1/n\) proves the logarithmic endpoint coefficient.

**Step 5: identify the first-order constant.** When \(\sigma=1\), the Laguerre three-term recurrence makes \(C\) the leading \(q\)-by-\(q\) symmetric Jacobi matrix of multiplication by \(y\). Its diagonal entries are \(2j+\alpha+1\), and its neighboring off-diagonals are \(-\sqrt{(j+1)(j+\alpha+1)}\), for \(0\le j<q\) where defined. Its characteristic polynomial is a nonzero scalar multiple of \(L_q^{(\alpha)}\), and its trace is \(\sum_{j=0}^{q-1}(2j+\alpha+1)=q(q+\alpha)\). Since \(1/\sigma=1\), this trace is exactly the ordered singular-value coefficient. The two-dimensional explicit matrix follows by integrating \(p_0=1\) and \(p_1=(\alpha+1-y)/\sqrt{\alpha+1}\) against the Gamma law weighted by \(y^\sigma\).

## Verification

A standalone Python checker (`checker.py`, requiring NumPy) directly assembles the beta/Jacobi tridiagonal compressed multiplication matrices for several positive integer powers of \(1-t\), rescales them by high angular frequencies, and compares against the Laguerre Jacobi matrix powers. It also checks the two-dimensional Gamma-moment formula and the \(\sigma=1\) Laguerre-zero trace. It passed **230** finite numerical assertions when executed before packaging. These samples only check finite identities and convergence examples; the infinite theorem, arbitrary real \(\sigma>0\), and ordering follow from Steps 1–5, not the checker.

## Relationship to prior work

Barrera-Castelán, Maximenko and Ramos-Vazquez (arXiv:2009.14301) establish the radial disk-polynomial block representation. Their subsequent arXiv:2306.06231 gives qualitative scalar limits for matrix blocks when the symbol approaches its boundary value; that conclusion yields compactness after subtracting the scalar but **not** the leading Laguerre matrix, its \(q\) eigenvalues, the sharp ordered singular-value coefficient, or the endpoint trace law. Pushnitski (arXiv:1710.02652) studies power-boundary spectral asymptotics for ordinary **analytic** Bergman Toeplitz operators, without the full-polyanalytic Jacobi blocks; its conclusions therefore do not imply the \(q\ge2\) matrix coefficient. Rozenblum and Vasilevski (arXiv:1907.06878) study polyanalytic Toeplitz operators for singular symbols on the half-plane, a different operator and symbol regime. The novelty claim is confined to the explicit full-polyanalytic boundary-layer and quantitative singular-value law, not to existing block formulas, Laguerre recurrence, or classical Gamma asymptotics.

## Limitations

The theorem assumes fixed finite polyanalytic order, a bounded radial symbol with a nonzero power-law boundary term, and the standard weighted disk measure. No uniform statement for increasing order, nonradial symbols, non-power asymptotics, or general disk weights is proved. The literature comparison is a best-knowledge, non-exhaustive historical-priority assessment and has not been independently validated. The numerical checker is not an infinite-dimensional proof.

## References

1. R. M. Barrera-Castelán, E. A. Maximenko and G. Ramos-Vazquez, *C*-algebras generated by radial Toeplitz operators on polyanalytic weighted Bergman spaces*, arXiv:2306.06231, first public June 9, 2023. https://arxiv.org/abs/2306.06231 .
2. R. M. Barrera-Castelán, E. A. Maximenko and G. Ramos-Vazquez, *Radial operators on polyanalytic weighted Bergman spaces*, arXiv:2009.14301. https://arxiv.org/abs/2009.14301 .
3. A. Pushnitski, *Spectral asymptotics for a class of Toeplitz operators on the Bergman space*, arXiv:1710.02652. https://arxiv.org/abs/1710.02652 .
4. G. Rozenblum and N. Vasilevski, *Toeplitz operators with singular symbols in polyanalytic Bergman spaces on the half-plane*, arXiv:1907.06878. https://arxiv.org/abs/1907.06878 .
