# Hidden reset reflection and moment-rate tomography for contractive Brownian jumps

## Finding
Consider symmetric Brownian diffusion subjected to independent Poissonian jumps that multiply the instantaneous position by a random contractive factor. There is an exact separation between what magnitude-only observations can identify and what signed, time-resolved moments can identify.

**Theorem (magnitude blindness and complete moment-rate tomography).** Let \(D,r>0\), and let \(\nu\) be any probability law supported on \([-c,c]\) for some \(0\le c<1\). At rate \(r\), independently of a Brownian motion of diffusivity \(D\), replace \(X_{t-}\) by \(QX_{t-}\), where each \(Q\) is an independent draw from \(\nu\). There is a unique stationary law with all finite moments. Define \(m_n=\mathbb E_\nu Q^n\) and \(\lambda_n=r(1-m_n)\), for integers \(n\ge1\).

1. The entire stationary **magnitude trajectory** \((|X_t|)_{t\in\mathbb R}\), including all of its multi-time distributions, depends on \(\nu\) only through the law of \(|Q|\). The complete stationary one-time signed-position distribution also depends only on \(|Q|\). Hence neither arbitrarily long magnitude-only records nor any single-time position histogram can distinguish two reset laws having the same distribution of \(|Q|\).

2. For every \(n\ge1\) and \(t>0\), the conditional moment \(P_n(t,x)=\mathbb E[X_t^n\mid X_0=x]\) is a polynomial in \(x\) of degree \(n\), with leading coefficient
\[
[x^n]P_n(t,x)=e^{-\lambda_n t}.
\]
If these exact leading-coefficient relaxation rates are available for **all** positive integers \(n\), they determine the unknown reset rate and entire signed multiplier law uniquely:
\[
r=\lim_{n\to\infty}\lambda_n,\qquad m_n=1-\frac{\lambda_n}{r}.
\]
The stationary variance then determines the unknown diffusivity via
\[
D=\frac{r(1-m_2)}2\operatorname{Var}(X_0).
\]
If \(r\) is already known and \(\nu\) is supported on at most \(m\) points, the finite collection \(\lambda_1,\ldots,\lambda_{2m-1}\) identifies \(\nu\) uniquely.

3. In the deterministic case \(Q=q\in(-1,1)\), **only two time-correlation decay rates and the stationary variance** are needed even when \(D,r,q\) are all unknown. With
\[
\begin{aligned}
C_1(t)&=\operatorname{Cov}(X_0,X_t)
=V e^{-\lambda_1t},\\
C_2(t)&=\operatorname{Cov}(X_0^2,X_t^2)
=\operatorname{Var}(X_0^2)e^{-\lambda_2t},\\
V&=\operatorname{Var}(X_0)=\frac{2D}{r(1-q^2)},
\end{aligned}
\]
the unique reconstruction is
\[
\boxed{q=\frac{\lambda_2}{\lambda_1}-1,\qquad
r=\frac{\lambda_1}{1-q},\qquad D=\frac{V\lambda_2}{2}.}
\]
Thus \(q>0\) precisely when \(\lambda_2>\lambda_1\), and \(q<0\) precisely when \(\lambda_2<\lambda_1\). For example \(q=2/3\) and \(q=-2/3\), at the same \(r,D\), have indistinguishable stationary position histograms and entire magnitude trajectories, but their signed-position covariance decay rates are respectively \(r/3\) and \(5r/3\), while the squared-position decay rate is \(5r/9\) in both cases.

## Assumptions and scope
The process has generator, on smooth functions of polynomial growth,
\[
(Lf)(x)=D f''(x)+r\!\int_{[-c,c]}\!\bigl(f(qx)-f(x)\bigr)\,\nu(dq).
\]
The driving Brownian motion has quadratic variation \(2Dt\). Reset times are homogeneous Poisson, the multipliers are independent from each other and from the Brownian motion, and all initial values are real. The uniform contraction bound \(|Q|\le c<1\) is essential to the all-moment and infinite-rate reconstruction statements. The magnitude-process assertion compares models at the same \(r,D\) with identical laws of \(|Q|\). The inverse results are exact population-level statements, not finite-sample guarantees.

## Proof
**Existence and uniqueness.** On a two-sided marked stationary Poisson process, define the stationary stochastic integral
\[
X_t=\sqrt{2D}\int_{-\infty}^t\!\left(\prod_{s<\tau_j\le t}Q_j\right)dB_s.
\]
The product is one when the indexing set is empty. On going backward, successive interval lengths are independent exponential variables \(T_j\) of rate \(r\). Conditional variance is bounded by \(2D\sum_{j\ge0}c^{2j}T_j\), which has moments of every positive integer order. Hence the integral and all its moments exist. Starting from two different positions but with the same future driving noise and multipliers, their difference at time \(t\) is \((x-y)\prod_{j\le N_t}Q_j\); its mean square equals \((x-y)^2e^{-r(1-m_2)t}\). Since \(m_2\le c^2<1\), this coupling gives uniqueness of the invariant law among all initial distributions with finite second moment, and convergence to it. The contraction also gives uniqueness among arbitrary initial probability laws by synchronous pathwise convergence in probability.

**Magnitude blindness.** Set \(R_t=|X_t|\). Between jumps \(R\) is reflected Brownian motion on the half-line with diffusivity \(D\); at a jump it moves from \(R_{t-}\) to \(|Q|R_{t-}\). Its generator away from the reflecting endpoint, with Neumann condition at zero, is
\[
(\mathcal L_Rg)(u)=Dg''(u)+r\int\bigl(g(|q|u)-g(u)\bigr)\nu(dq).
\]
This completely determines the modulus path law and involves only \(|Q|\). In the two-sided integral above, conditional on the Poisson times and multipliers, \(X_t\) is centered Gaussian, with conditional variance
\[
2D\int_{-\infty}^t\prod_{s<\tau_j\le t}Q_j^2\,ds.
\]
Thus its stationary one-time law is unchanged by any alteration of reset signs that preserves the law of \(|Q|\). (The conclusion is not asserted for nonzero deterministic initial positions at nonstationary times.)

**Moment-rate inversion.** Over any finite interval the process is affine in its initial state: \(X_t=Z_tx+U_t\), where \(Z_t=\prod_{j\le N_t}Q_j\), and \(U_t\) is independent of \(x\). Expanding the integer power, the coefficient of \(x^n\) is exactly \(\mathbb E Z_t^n\). The compound Poisson generating function gives
\[
\mathbb EZ_t^n=\exp\bigl(rt(\mathbb EQ^n-1)\bigr)=e^{-\lambda_nt}.
\]
Since \(|m_n|\le c^n\to0\), the limit of \(\lambda_n\) is \(r\); all the power moments of \(\nu\) are recovered. Two probability laws on the compact interval \([-c,c]\) with the same integer moments are equal: polynomials are uniformly dense in continuous functions there. The stationary generator identity applied to \(x^2\) yields \(0=2D-r(1-m_2)\mathbb EX^2\), proving the formula for \(D\). If two laws have at most \(m\) atoms and their first \(2m-1\) power moments agree, their signed difference has at most \(2m\) distinct support points. Including moment order zero gives a square or tall Vandermonde system with full column rank, so every difference weight vanishes; this proves finite atomic identification.

**Two-correlation reconstruction for fixed \(q\).** From the generator,
\[
Lx=-r(1-q)x,\qquad
Lx^2=2D-r(1-q^2)x^2.
\]
It follows exactly that
\[
\mathbb E[X_t\mid X_0=x]=xe^{-\lambda_1t},\quad
\mathbb E[X_t^2\mid X_0=x]=V+(x^2-V)e^{-\lambda_2t}.
\]
The invariant state is centered and nondegenerate, so multiplying by the initial observables gives the two covariance formulas. Since \(\lambda_1,\lambda_2,V>0\), the displayed inverse formulas follow algebraically, including the boundary \(q=0\). The equations also establish that the relaxation-order reversal is strict away from that boundary.

## Verification
The standalone file `check.py` uses exact symbolic and rational arithmetic to check 211 identities: moment balances, excess-kurtosis normalization, parameter inversion, sign-paired stationary moments, random-multiplier polynomial-generator diagonals, and Poisson-product coefficients. Running `python check.py` reproduces `check_output.txt`. A deterministic illustration with \(q=\pm2/3\), \(r=5/4\), and \(D=3/7\) yields the same stationary variance \(216/175\) and excess kurtosis \(15/13\), but signed covariance rates \(5/12\) versus \(25/12\), with squared covariance rate \(25/36\) for either sign. These finite computations check algebra but do not replace the structural proof of moment determinacy or equality of modulus path laws.

## Relationship to prior work
Di Bello et al. (arXiv:2305.13722, first submitted 2023-05-23) develop time-dependent distributions for partial resetting with **positive** fixed contraction \(0<c<1\), including the stationary Fourier product. Pierce (arXiv:2204.07215) and Tal-Friedman, Roichman, and Reuveni (arXiv:2205.03363) derive moments and stationary laws for positive proportional resetting; their fixed-factor results are retained as established background. Dahlenburg et al. (arXiv:2104.14866) analyze random resetting amplitudes, with random signed **additive** jumps independent of position in one protocol and state-dependent nonnegative multiplicative factors in another. General polynomial-jump-diffusion correlator methods (Benth and Lavagnini, DOI:10.1137/21M141556X) provide a broad computational setting for moment formulas. The fixed-factor stationary sign-blindness already follows from the known even-power Fourier product and is treated as background, not a standalone novelty. The present combined claim is the sign-blindness of **complete magnitude trajectories** under random signed state-dependent multipliers and their exact signed-law recovery using conditional polynomial decay coefficients, including finite-atomic and two-correlation identification. General moment-generation machinery should not itself be claimed as novel.

## Limitations
No finite-record estimator, uncertainty bound, or robustness-to-measurement-noise theorem is proved. The infinite hierarchy is a theoretical identification criterion, while the finite atomic criterion presupposes known reset rate and a finite support bound. The sign-blindness conclusion uses symmetric driftless Brownian forcing; a nonzero drift can reveal reset signs in magnitude data. Uniform strict contraction excludes \(|Q|=1\), expansive multipliers, and heavy-tailed stationary regimes. The observations establish no priority or uniqueness beyond the cited and searched literature; a later or unexamined specialized result could overlap. Independent mathematical audit has not been performed.

## References
- C. Di Bello, A. V. Chechkin, A. K. Hartmann, Z. Palmowski, R. Metzler, “Time-dependent probability density function for partial resetting dynamics,” arXiv:2305.13722 (first public 2023-05-23).
- M. Dahlenburg, A. V. Chechkin, R. Schumer, R. Metzler, “Stochastic resetting by a random amplitude,” arXiv:2104.14866 (2021), DOI:10.1103/PhysRevE.103.052123.
- J. K. Pierce, “An advection-diffusion process with proportional resetting,” arXiv:2204.07215 (2022).
- O. Tal-Friedman, Y. Roichman, S. Reuveni, “Diffusion with partial resetting,” arXiv:2205.03363 (2022), DOI:10.1103/PhysRevE.106.054116.
- F. E. Benth, S. Lavagnini, “Correlators of Polynomial Processes,” SIAM Journal on Financial Mathematics, DOI:10.1137/21M141556X (2021).
