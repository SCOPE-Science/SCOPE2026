# Fourier-mode memory cusp and exact critical variance in a heterochaos baker family

## Finding
For the two-dimensional heterochaos baker family introduced by Takahasi and Yamamoto, the stationary temporal autocovariance of every odd Fourier harmonic of the center coordinate is an exact weighted Catalan number. This gives a parameter-uniform solution of the center-harmonic correlation problem, a sharp cusp of the Green–Kubo variance at the neutral-center parameter, and the first square-root correction to finite-time variance at criticality.

Precisely, for every \(a\in(0,1/2)\), every positive odd integer \(k\), and either \(\phi_k(y)=\cos(2\pi k y)\) or \(\phi_k(y)=\sin(2\pi k y)\), writing \(\mathrm{Cat}_m=\frac1{m+1}\binom{2m}{m}\) and \(d=2a(1-2a)\), normalized two-dimensional Lebesgue measure gives
\[
\operatorname{Cov}(\phi_k(Y_0),\phi_k(Y_n))=
\begin{cases}\frac12\,\mathrm{Cat}_m d^m,&n=2m,\\0,&n\text{ odd}.\end{cases}
\]
Distinct positive odd frequencies and distinct sine/cosine coordinates have zero mutual cross-correlations at all nonnegative and negative integer lags. The partial sum \(S_N=\sum_{j=0}^{N-1}\phi_k(Y_j)\) has the exact finite-time variance
\[
\operatorname{Var}(S_N)=\frac N2+\sum_{m=1}^{\lfloor(N-1)/2\rfloor}(N-2m)\mathrm{Cat}_m d^m.
\]
The asymptotic variance exists for every parameter and equals
\[
\sigma^2(a)=\lim_{N\to\infty}\frac{\operatorname{Var}(S_N)}N
=\frac1{\max\{2a,1-2a\}}-\frac12.
\]
Its unique maximum is \(\sigma^2(1/4)=3/2\). Its one-sided parameter derivatives there are \(+8\) and \(-8\). The original \(a=1/3\) map has \(\sigma^2(1/3)=1\).

At the neutral-center parameter \(a=1/4\), correlations have the sharp critical asymptotic \(\operatorname{Cov}(\phi_k(Y_0),\phi_k(Y_{2m}))\sim(2\sqrt\pi)^{-1}m^{-3/2}\) and
\[
\operatorname{Var}(S_N)=\frac32N-4\sqrt{\frac{2N}{\pi}}+4+O(N^{-1/2}).
\]
For each fixed \(a\ne1/4\), the correlations instead have an exponential factor \((8a(1-2a))^m\) at even lag \(2m\), and
\[
\operatorname{Var}(S_N)=\sigma^2(a)N-\frac{2\min\{2a,1-2a\}}{\max\{2a,1-2a\}\,|4a-1|}+O_a\bigl(N^{-3/2}\rho(a)^N\bigr),
\qquad\rho(a)=\sqrt{8a(1-2a)}<1.
\]
For every \(a>1/4\), the centered partial sums of any fixed finite collection of distinct odd-frequency sine/cosine observables, divided by \(\sqrt N\), converge jointly to a centered Gaussian vector with covariance \(\sigma^2(a)I\). No central limit theorem is claimed at or below \(a=1/4\).

## Assumptions and scope
Work on \([0,1)^2\) modulo null boundary sets. Fix \(0<a<1/2\), put \(p=1-2a\), \(q=2a\), and define
\[
\tau_a(x)=\begin{cases}x/a,&0\le x<a,\\(x-a)/a,&a\le x<2a,\\(x-2a)/p,&2a\le x<1.\end{cases}
\]
The map \(T_a(x,y)=(\tau_a(x),H_a(x,y))\) has
\[
H_a(x,y)=\begin{cases}y/2,&0\le x<a,\\(y+1)/2,&a\le x<2a,\\2y\pmod1,&2a\le x<1.\end{cases}
\]
These are the \(M=2\) generalized heterochaos baker maps in the cited 2022 source. Start the deterministic map in normalized two-dimensional Lebesgue measure; write \((X_n,Y_n)=T_a^n(X_0,Y_0)\). The measure is invariant and the statement is for its stationary law, not for arbitrary deterministic initial points or other invariant probabilities. Here \(O_a\) allows constants depending on fixed \(a\), and the Fourier frequency \(k\) must be a positive odd integer; the extension to a general nonzero frequency follows by dividing out its largest power of two.

## Proof
**1. Stationarity and center Markov operator.** Each of the three branches of the expanding base \(\tau_a\) maps onto \([0,1)\), with source lengths \(a,a,p\). Thus the base branch labels of a Lebesgue-typical orbit are independent with those probabilities. The initial center coordinate is independent of all labels. Every center branch is either an inverse binary branch or doubling; the corresponding center Markov kernel is
\[
(Pf)(y)=a f(y/2)+a f((y+1)/2)+p f(2y\bmod1).
\]
Lebesgue measure in \(y\) is stationary: the two inverse branches together contribute \(q\int_0^1 f\), and doubling contributes \(p\int_0^1 f\). Independence of future branch labels from earlier center coordinates establishes the Markov property of the stationary center process. In particular, for \(n\ge0\),
\[\mathbb E[\phi(Y_0)\psi(Y_n)]=\int_0^1\phi(y)(P^n\psi)(y)\,dy.\]

**2. Fourier-frequency walk.** Put \(e_j(y)=\exp(2\pi i j y)\). Direct substitution gives, for every nonzero integer \(j\),
\[
Pe_j=\begin{cases}p e_{2j},&j\text{ odd},\\q e_{j/2}+p e_{2j},&j\text{ even}.\end{cases}
\]
This exact identity remains valid for cosine and sine by taking real and imaginary parts. Every frequency has a unique decomposition \(j=2^h k\) with \(h\ge0\) and odd \(k\ne0\); the operator never changes the odd part. Starting at level \(h=0\), a return to level zero in \(n\) steps is possible only for \(n=2m\). Its paths are precisely the Dyck paths on the nonnegative integers with \(m\) upward and \(m\) downward steps, none below zero. There are \(\mathrm{Cat}_m\) such paths, each weighted \(p^m q^m=d^m\). Orthogonality of the real sine/cosine Fourier basis yields the advertised \(\frac12\mathrm{Cat}_m d^m\). Distinct odd parts, and the orthogonal real/imaginary directions, remain orthogonal for every lag. Negative lags follow by stationarity and interchanging the observables.

**3. Finite-time and integrated variances.** The variance of a stationary centered sum is
\[\operatorname{Var}(S_N)=NC_0+2\sum_{n=1}^{N-1}(N-n)C_n,\]
which, after inserting the exact even-lag covariances, is the displayed finite sum. Let
\[\mathcal C(u)=\sum_{m\ge0}\mathrm{Cat}_m u^m=\frac{1-\sqrt{1-4u}}{2u},\quad\mathcal C(0)=1.\]
Since \(0<d\le1/4\), the covariance series is absolutely summable even at the critical parameter. Hence the finite-time variance divided by \(N\) tends to
\[C_0+2\sum_{n\ge1}C_n=\mathcal C(d)-\frac12.\]
Because \(p+q=1\) and \(4pq\le1\), \(\mathcal C(pq)=2/(1+|p-q|)=1/\max\{p,q\}\). This proves the closed form and its strict monotonicity on either side of \(q=p=1/2\). Differentiation gives the stated \(+8\) and \(-8\) one-sided slopes.

**4. Sharp fixed-parameter and critical finite-time laws.** The classical central-binomial asymptotic \(\mathrm{Cat}_m\sim 4^m/(\sqrt\pi m^{3/2})\) gives the exact even-lag coefficient, both at and away from criticality. For fixed \(d<1/4\), exchanging the convergent sums shows
\[\operatorname{Var}(S_N)=\sigma^2(a)N-2d\mathcal C'(d)+O_a(N^{-3/2}\rho(a)^N).\]
Differentiate the identity \(\mathcal C=1+d\mathcal C^2\) to obtain
\[2d\mathcal C'(d)=\frac{2\min\{p,q\}}{\max\{p,q\}|p-q|}.\]
At \(p=q=1/2\), set \(V(z)=\sum_{N\ge1}\operatorname{Var}(S_N)z^N\). The finite-time convolution gives the exact function, for \(|z|<1\),
\[
V(z)=\frac z{(1-z)^2}\left(\frac{2(1-\sqrt{1-z^2})}{z^2}-\frac12\right).
\]
Near \(z=1\), expand this algebraic function as
\[
V(z)=\frac{3}{2}(1-z)^{-2}-2\sqrt2(1-z)^{-3/2}+\frac52(1-z)^{-1}+O((1-z)^{-1/2}).
\]
The only other unit-circle singularity is the square-root point \(z=-1\), whose coefficient contribution is \(O(N^{-3/2})\). Coefficient extraction gives \(\frac32(N+1)-4\sqrt{2N/\pi}+\frac52+O(N^{-1/2})\), exactly the critical variance expansion.

**5. Joint central limit theorem in the contracting-center regime.** Suppose \(q>p\), equivalently \(a>1/4\). For each odd harmonic and either sine or cosine form \(\phi\), define the bounded, uniformly convergent Fourier series
\[
g(y)=\frac1q\sum_{h=0}^{\infty}\left(\frac pq\right)^h\phi(2^h y).\]
Using the exact Fourier transitions shows directly that \((I-P)g=\phi\); this includes the boundary level \(h=0\), since the coefficient is \(1\). Thus \(\sum_{j<N}\phi(Y_j)\) is the sum of a bounded telescoping remainder and bounded stationary martingale differences \(g(Y_{j+1})-(Pg)(Y_j)\). The stationary center process is ergodic because the original map is mixing for these parameters (as established in the cited literature), so the conditional martingale quadratic variation obeys the ergodic theorem. The martingale central limit theorem applies, and the asymptotic variance equals the already calculated Green–Kubo value. Applying the same argument to arbitrary finite linear combinations and using the exact vanishing cross-correlations proves joint Gaussian convergence with diagonal covariance. This argument is not asserted to produce a bounded Poisson solution at \(a\le1/4\).

## Verification
The standalone Python program `verify_fourier.py` checks 600 exact rational Fourier-transition instances, 136 rational Poisson-coefficient identities, and 204 exact finite-variance instances. It also checks the Catalan generating identity for six rational parameters and compares stationary Monte Carlo covariances for three parameters and eight positive lags. These finite checks passed; the largest sampled covariance discrepancy was about \(0.00292\). The critical square-root formula was separately checked at three finite horizons. The infinite statements rest on the analytic proof above, not on sampling or a finite search.

For the classical map \(a=1/3\), the first even covariances at lags \(0,2,4,6\) are exactly \(1/2,1/9,4/81,20/729\). The critical parameter \(a=1/4\) yields asymptotic variance \(3/2\), whereas \(a=1/3\) yields \(1\).

## Relationship to prior work
Saiki, Takahasi and Yorke introduced the classical parameter \(a=1/3\). Takahasi and Yamamoto subsequently introduced the full parameter family used here, including its invariant-measure setting. Takahasi established exponential mixing in the nonneutral regimes. Saiki, Takahasi, Yamamoto and Yorke surveyed both the broad mixing results and numerical center-coordinate correlations. Takahasi and Tsujii proved optimal critical \(n^{-3/2}\) correlation decay and used an absorbing random-walk comparison for a reduced transfer operator. These foundational observations, including the random-walk mechanism and critical exponent, are not claimed as new. The present theorem instead evaluates the signed Fourier-mode correlations for every lag and every parameter, the resulting piecewise-exact variance cusp, the critical square-root finite-time term, and the contracting-regime multivariate limit for this specific harmonic family. The Fourier frequency walk is a distinct exact representation compatible with, but not supplied as an explicit formula by, the examined Haar-wavelet mixing analysis.

## Limitations
The quantitative conclusions concern stationary Lebesgue-typical orbits of the two-dimensional \(M=2\) family and Fourier observables depending only on the center. They do not give formulas for arbitrary observables or initial distributions. The central limit theorem here is proved only for \(a>1/4\). The algebraic upper and lower critical correlation exponents were already established in broader literature; novelty rests on the exact harmonic coefficients and variance laws, not on rediscovering the exponent. An equivalent calculation hidden in differently indexed published work cannot be ruled out by the inspected sources. No independent mathematical audit or external certification has been carried out.

## References
1. Y. Saiki, H. Takahasi and J. A. Yorke, *Piecewise-linear maps with heterogeneous chaos*, first public preprint 2018-11-02, arXiv:1811.01009, https://arxiv.org/abs/1811.01009.
2. H. Takahasi and K. Yamamoto, *Heterochaos baker maps and the Dyck system: maximal entropy measures and a mechanism for the breakdown of entropy approachability*, first public preprint 2022-09-11, arXiv:2209.04905, https://arxiv.org/html/2209.04905v1.
3. H. Takahasi, *Exponential mixing for heterochaos baker maps and the Dyck system*, 2023, arXiv:2307.08119, https://arxiv.org/abs/2307.08119.
4. Y. Saiki, H. Takahasi, K. Yamamoto and J. A. Yorke, *The dynamics of the heterochaos baker maps*, arXiv:2401.00836, https://arxiv.org/html/2401.00836v2, especially Sections 2.5–2.7.
5. H. Takahasi and M. Tsujii, *Polynomial rate of mixing for the heterochaos baker maps with mostly neutral center*, first public preprint 2024-08-29, arXiv:2408.16618, https://arxiv.org/html/2408.16618v1, especially Sections 2.1–2.5.
