# Explicit shrinking-window eigenvalue hierarchy for Dunkl–Hermite and Gegenbauer concentration

## Finding

The finite-band concentration matrices of the generalized Hermite and generalized Gegenbauer polynomial systems have **one eigenvalue at each successive power of the window radius**. For a fixed positive integer \(N\), a parameter \(\mu>-1/2\), and (in the Gegenbauer case) \(\beta>-1\), write their eigenvalues in nonincreasing order as \(\lambda_0(T),\ldots,\lambda_{N-1}(T)\). Then, for every \(0\le i<N\),

\[
\boxed{\lambda_i(T)=A_i T^{2\mu+2i+1}\left(1+O_{N,\mu,\beta}(T^2)\right),\qquad A_i>0.}
\]

The positive constants \(A_i\) are **explicit ratios of Selberg integrals and Hankel determinants**, evaluated below as finite gamma products. Consequently, for \(N\ge2\), the spectral condition number obeys the sharp law

\[
\boxed{\frac{\lambda_0(T)}{\lambda_{N-1}(T)}=\frac{A_0}{A_{N-1}}\,T^{-2(N-1)}\left(1+O_{N,\mu,\beta}(T^2)\right).}
\]

The powers do not depend on the Gegenbauer endpoint parameter \(\beta\). Even- and odd-degree sectors interlace asymptotically, so **every one** of the \(N\) eigenvalues has a different small-window power. The formula holds for arbitrary fixed real parameters in the specified ranges, not merely integral multiplicities.

## Assumptions and scope

Let \(\mathcal P_{N-1}\) be the polynomials of degree at most \(N-1\). Use one of the following even, strictly positive weights:

* **Generalized Hermite:** \(w(x)=|x|^{2\mu}e^{-x^2}\) on \(\mathbb R\), with \(\mu>-1/2\), and \(0<T<\infty\).
* **Generalized Gegenbauer:** \(w(x)=|x|^{2\mu}(1-x^2)^\beta\) on \((-1,1)\), with \(\mu>-1/2\), \(\beta>-1\), and \(0<T<1\).

Equip \(\mathcal P_{N-1}\) with \(\langle f,g\rangle=\int f(x)\overline{g(x)}w(x)\,dx\). The self-adjoint finite concentration operator \(C_N(T)\) is uniquely specified by

\[
\langle C_N(T)f,g\rangle=\int_{-T}^T f(x)\overline{g(x)}w(x)\,dx.
\]

Equivalently, in any global orthonormal polynomial basis its matrix consists of the truncated inner products. It has \(N\) eigenvalues strictly between \(0\) and \(1\) for every nontrivial window in the indicated range. They are ordered \(\lambda_0\ge\cdots\ge\lambda_{N-1}\). The asymptotics are for fixed \(N,\mu\) and, where applicable, fixed \(\beta\) as \(T\downarrow0\); they are not uniform in growing bandwidth or varying weight parameters.

For \(\varepsilon\in\{0,1\}\), define

\[
m_\varepsilon=\#\{n\in\{0,\ldots,N-1\}:n\equiv\varepsilon\pmod2\},\quad
\alpha_\varepsilon=\mu+\varepsilon-\tfrac12.
\]

Set \(v(y)=e^{-y}\) on \([0,\infty)\) in the Hermite case, and \(v(y)=(1-y)^\beta\) on \([0,1]\) in the Gegenbauer case. For integers \(m\ge0\), introduce

\[
H_m(\alpha)=\det\left[\int_0^R y^{\alpha+r+s}v(y)\,dy\right]_{r,s=0}^{m-1},\quad H_0(\alpha)=1,
\]

where \(R=\infty\) or \(R=1\) as appropriate. For integers \(k\ge0\) define the Selberg integral

\[
S_k(a,b)=\int_{[0,1]^k}\prod_{r=1}^k u_r^{a-1}(1-u_r)^{b-1}\prod_{1\le r<s\le k}(u_r-u_s)^2\,d\boldsymbol u,\quad S_0=1.
\]

For \(0\le k\le m\), put \(D_{m,0}(\alpha)=1\) and, when \(1\le k\le m\),

\[
D_{m,k}(\alpha)=\frac{H_{m-k}(\alpha+2k)}{H_m(\alpha)}\frac{S_k(\alpha+1,1)}{k!}.
\]

The formulas for \(A_i\) are: write \(i=2j+\varepsilon\), with \(\varepsilon\in\{0,1\}\), and take \(k=j+1\). Then

\[
\boxed{A_i=\frac{D_{m_\varepsilon,k}(\alpha_\varepsilon)}{D_{m_\varepsilon,k-1}(\alpha_\varepsilon)}.}
\]

All quantities are positive. The promised gamma products are

\[
S_k(a,b)=\prod_{\ell=0}^{k-1}\frac{\Gamma(a+\ell)\Gamma(b+\ell)\Gamma(\ell+2)}{\Gamma(a+b+k+\ell-1)},
\]

\[
H_m^{\mathrm H}(\alpha)=\prod_{\ell=0}^{m-1}\ell!\,\Gamma(\alpha+\ell+1),\qquad
H_m^{\mathrm G}(\alpha)=\frac{S_m(\alpha+1,\beta+1)}{m!}.
\]

For \(N=1\) the condition number is identically one. For illustration, in the ordinary Hermite case \(\mu=0\), \(N=2\), one obtains \(\lambda_0(T)\sim(2/\sqrt\pi)T\) and \(\lambda_1(T)\sim(4/(3\sqrt\pi))T^3\); their ratio is asymptotic to \((3/2)T^{-2}\).

## Proof

**1. Parity and the change of variables.** Since the weight and window are even, the even and odd polynomial sectors are orthogonal and invariant. Each polynomial in the \(\varepsilon\)-sector is \(x^\varepsilon p(x^2)\), where \(\deg p<m_\varepsilon\). With \(y=x^2\), the full inner product in this sector becomes the moment inner product for \(y^{\alpha_\varepsilon}v(y)\,dy\) on \([0,R]\), while the truncated inner product is the same integral over \([0,b]\), \(b=T^2\). There are no hidden factors of two: the contributions from positive and negative \(x\) exactly cancel the Jacobian \(dx=dy/(2\sqrt y)\).

**2. A general finite polynomial concentration lemma.** Fix \(m\ge1\), \(\alpha>-1\) and a function \(v\) positive on \([0,R)\) and analytic at zero with \(v(0)=1\). In the monomial basis \(1,y,\ldots,y^{m-1}\), let \(H\) be the full moment matrix and \(G(b)\) the moment matrix truncated to \([0,b]\). The generalized eigenvalues of \((G(b),H)\) equal those of the positive matrix \(H^{-1/2}G(b)H^{-1/2}\). Write \(e_k(b)\) for the \(k\)-th elementary symmetric function of these eigenvalues, with \(e_0=1\).

The reproducing kernel is \(K_m(y,z)=\boldsymbol p(y)^\mathsf T H^{-1}\boldsymbol p(z)\), with \(\boldsymbol p(y)=(1,y,\ldots,y^{m-1})^\mathsf T\). The standard exterior-power trace identity, or its direct Cauchy–Binet expansion, gives

\[
e_k(b)=\frac1{k!}\int_{[0,b]^k}\det[K_m(y_r,y_s)]_{r,s=1}^k\prod_{r=1}^k y_r^\alpha v(y_r)\,d\boldsymbol y.
\]

By Cauchy–Binet, the leading minor in the kernel determinant uses monomial degrees \(0,\ldots,k-1\). Since all other degree choices have greater sum, uniformly for \(u_r\in[0,1]\), after factoring the squared Vandermonde,

\[
\det[K_m(bu_r,bu_s)]
=b^{k(k-1)}\prod_{r<s}(u_r-u_s)^2
\left(\det[(H^{-1})_{r,s}]_{r,s=0}^{k-1}+O(b)\right).
\]

This identity also holds at coincident points by polynomial divisibility, so no division by a vanishing Vandermonde is required. The Jacobi complementary-minor formula identifies

\[
\det[(H^{-1})_{r,s}]_{r,s=0}^{k-1}
=\frac{\det[H_{r+k,s+k}]_{r,s=0}^{m-k-1}}{\det H}
=\frac{H_{m-k}(\alpha+2k)}{H_m(\alpha)}.
\]

The empty determinant is one. Substituting \(y_r=bu_r\), using \(v(bu_r)=1+O(b)\), and evaluating the remaining Selberg integral proves

\[
\boxed{e_k(b)=D_{m,k}(\alpha)b^{k(\alpha+k)}(1+O(b)),\quad 1\le k\le m.}
\]

The formula is valid for real \(\alpha>-1\), including nonintegral exponents, because the transformed weight is integrable. The \(O(b)\) term is uniform across the compact \(k\)-cube for each fixed \(m,k\).

**3. Resolving every individual eigenvalue.** Write \(D_k=D_{m,k}(\alpha)\), with \(D_0=1\), and let \(p_k=k(\alpha+k)\). For a fixed \(1\le k\le m\), scale the characteristic polynomial \(\sum_{\ell=0}^m(-1)^\ell e_\ell(b)z^{m-\ell}\) by \(z=b^{\delta_k}u\), where \(\delta_k=\alpha+2k-1\). The exponents \(p_\ell+(m-\ell)\delta_k\) attain their common minimum precisely at \(\ell=k-1,k\): indeed, their excess over that minimum is \((\ell-k)(\ell-k+1)\), a positive even integer for all other \(\ell\). After division by the smallest power of \(b\), the limiting polynomial is

\[
(-1)^{k-1}u^{m-k}(D_{k-1}u-D_k).
\]

It has a simple positive nonzero root \(u=D_k/D_{k-1}\). Continuity of simple polynomial roots (or the implicit function theorem) and the \(O(b)\) coefficient estimates give an eigenvalue

\[
\eta_{k-1}(b)=\frac{D_k}{D_{k-1}}\,b^{\alpha+2k-1}(1+O(b)).
\]

The exponents differ by two for successive \(k\). Consequently, the \(m\) detected eigenvalues are distinct for all sufficiently small \(b\), exhaust the \(m\)-dimensional spectrum, and are in the claimed decreasing order. Positivity is automatic from \(H,G(b)>0\).

**4. Evaluation and global ordering.** For Laguerre weight \(y^\alpha e^{-y}\), monic Laguerre polynomial norms give the stated \(H_m^{\mathrm H}\) product. For Jacobi weight \(y^\alpha(1-y)^\beta\), the Vandermonde-square integral identity gives \(H_m^{\mathrm G}=S_m(\alpha+1,\beta+1)/m!\). The standard Selberg evaluation gives the stated expression for \(S_k\). Both are strictly positive in the assumed parameter ranges.

Apply step 3 to each parity sector, substitute \(b=T^2\), and write \(i=2j+\varepsilon\), \(k=j+1\). Its exponent becomes

\[
2(\alpha_\varepsilon+2k-1)=2\mu+2i+1.
\]

These exponents are strictly increasing as \(i=0,\ldots,N-1\); hence the two parity spectra merge into precisely that order for sufficiently small positive \(T\). Taking the ratio of the first and last terms proves the condition-number asymptotic. This completes the proof.

## Verification

The standalone script `CHECK.py` (dependencies in `requirements.txt`) reproduces exact Hankel determinant identities, gamma-product coefficients, finite-dimensional eigenvalue comparisons for both weights and multiple parameter choices, and an independent exact symbolic calculation of all three elementary-symmetric leading coefficients in a three-dimensional Laguerre example. Run `python CHECK.py` from the directory containing both files; a successful execution reports `CHECK_OK 525`. These finite tests support normalization and algebra but are not substituted for the all-parameter proof above.

## Relationship to prior work

Castro and Grünbaum's 2026 preprint constructs commuting sparse operators for the generalized Hermite and Gegenbauer time–band limiting matrices and discusses their severe spectral ill-conditioning. The inspected full-text mathematical sections state commuting-operator formulas and numerical illustrations; they do not state the fixed-band shrinking-window exponents, all spectral constants, or the gamma-product condition-number law obtained here. The commutation framework does not itself supply the individual eigenvalue asymptotics. Earlier work of Grünbaum on classical reproducing kernels and its descendants supplies the general time–band limiting context but was not fully accessible in all cases. Selberg and Hankel determinant identities supply standard ingredients, explicitly credited rather than claimed new. The combination of the general eigenvalue separation argument with the two exact weight evaluations is the claim under review, not the classical identities in isolation.

## Limitations

The asymptotics are only for fixed finite \(N\) and fixed weight parameters. No large-bandwidth, double-scaling, eigenfunction asymptotics, uniform error constants or numerical-stability algorithm is asserted. This derivation assumes both weight families have a common even center and uses the complete consecutive-degree polynomial band; arbitrary degree masks need not have the same exponent list. Novelty is assessed relative to inspected accessible literature, not guaranteed against unindexed or inaccessible earlier equivalent results. Independent mathematical validation has not been performed.

## References

1. M. M. Castro and F. A. Grünbaum, *Time-and-band limiting for symmetric classical Dunkl orthogonal polynomials*, arXiv:2610.24100v1, publicly posted October 16, 2026. https://arxiv.org/abs/2610.24100
2. F. A. Grünbaum, *A new property of reproducing kernels for classical orthogonal polynomials*, Journal of Mathematical Analysis and Applications **95** (1983), 491–500. https://doi.org/10.1016/0022-247X(83)90123-3 (full text not accessed).
3. A. Selberg, *Bemerkninger om et multipelt integral*, Norsk Matematisk Tidsskrift **26** (1944), 71–78. The beta-type Vandermonde integral evaluation is used in its standard \(\gamma=1\) case.
