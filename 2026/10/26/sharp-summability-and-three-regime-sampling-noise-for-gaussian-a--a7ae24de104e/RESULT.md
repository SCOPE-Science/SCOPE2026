# Sharp summability and three-regime sampling noise for Gaussian additive ANOVA kernels

## Finding

Let \(\gamma_1\ge\gamma_2\ge\cdots>0\), with \(\gamma_j\le1\), be coordinate weights. For \(0<\rho\le1\), consider the **singleton-interaction** (additive, \(q=1\)) weight-adapted ANOVA kernel constructed from the normalized restriction of the radial Gaussian \(\phi(t)=2e^{-t^2}/\sqrt\pi\). Put \(a_j=\gamma_j^{1/4}\). Its dimension-\(d\) version is

\[
K_{d,\rho}(x)=1+\sum_{\substack{1\le j\le d\\a_j\ge\rho}}\bigl(\psi_{\rho/a_j}(x_j)-1\bigr),\qquad
\psi_\sigma(x)=\frac{\exp(2\sigma^{-2}\cos(2\pi x))}{I_0(2\sigma^{-2})},
\]

where \(I_0(z)=\int_0^1e^{z\cos(2\pi x)}\,dx\). Define

\[
E(\sigma)=\frac{I_0(4\sigma^{-2})}{I_0(2\sigma^{-2})^2}-1,\qquad
c=\sqrt{2\pi}.
\]

There are absolute constants \(0<c_-\le c_+<\infty\) such that, simultaneously for every \(d\ge1\) and \(0<\rho\le1\),

\[
c_-\sum_{\substack{j\le d\\a_j\ge\rho}}a_j\ \le\
\rho\bigl(\|K_{d,\rho}\|_{L^2(\mathbb T^d)}^2-1\bigr)
\ \le\ c_+\sum_{\substack{j\le d\\a_j\ge\rho}}a_j.
\]

In particular the following **sharp necessity-and-sufficiency statement** holds:

\[
\boxed{\quad\sup_{d\ge1,\ 0<\rho\le1}\rho\|K_{d,\rho}\|_2^2<\infty
\ \Longleftrightarrow\ \sum_{j=1}^{\infty}\gamma_j^{1/4}<\infty.\quad}
\]

For the natural power-law family \(\gamma_j=j^{-p}\), \(p>0\), set
\(V_p(\rho)=\sup_{d\ge1}(\|K_{d,\rho}\|_2^2-1)\). There is a **complete three-regime sharp asymptotic**, including exact constants:

\[
\boxed{
\begin{aligned}
p>4:\quad &\lim_{\rho\downarrow0}\rho V_p(\rho)=c\,\zeta(p/4),\\
p=4:\quad &\lim_{\rho\downarrow0}\frac{\rho V_p(\rho)}{\log(1/\rho)}=c,\\
0<p<4:\quad &\lim_{\rho\downarrow0}\rho^{4/p}V_p(\rho)=\int_0^1 E(u^{p/4})\,du\in(0,\infty).
\end{aligned}}
\]

For \(M\ge1\) independent uniform samples on \(\mathbb T^d\), the source's stochastic quasi-interpolant applied even to the constant function \(f\equiv1\) has the **exact** integrated mean-square error

\[
\mathbb E\big\|Q_{M,d,\rho}1-1\big\|_2^2
=\frac{\|K_{d,\rho}\|_2^2-1}{M}.
\]

Thus the \(\rho^{-1}/M\) dimension-independent sampling-noise rate is available for this Gaussian additive construction **if and only if** the fourth-root weights are summable. At the critical power-law boundary, a logarithmic loss is unavoidable, even on constant input; below it, the sharp scale exponent is \(4/p\).

## Assumptions and scope

The torus \(\mathbb T^d=[0,1)^d\) has normalized Lebesgue measure. The interaction order is fixed at \(q=1\). In the kernel construction of Sun (2026), choose Gaussian radial data \(\phi(t)=2\pi^{-1/2}e^{-t^2}\), moment order \(m=2\), Sobolev smoothness \(s\ge2\), approximation parameter \(a=\min(m,s)=2\), and maximum bandwidth \(\rho_0=1\). The source's active-coordinate threshold then becomes \(\gamma_j\ge\rho^4\) and the bandwidth of coordinate \(j\) becomes \(\rho\gamma_j^{-1/4}\). All factors are well defined and normalized for \(0<\rho\le1\). No high-dimensional limit of a single fixed \(d\) is taken: the sharp uniformity assertion quantifies over **all** finite dimensions.

The modified Bessel function \(I_0\) is specified by the integral above; \(\zeta\) is the Riemann zeta function. The stochastic operator is

\[
Q_{M,d,\rho}f(x)=\frac1M\sum_{r=1}^M f(X_r)K_{d,\rho}(x-X_r),
\]

where \(X_r\) are independent, uniformly distributed points in \(\mathbb T^d\). No noise in the sampled function values is needed for the variance obstruction: the randomness is solely in sampling locations.

## Proof

**Step 1: identify the exact Gaussian restriction.** The kernel restriction of the radial Gaussian has the form \(C_\sigma\exp[-4\sin^2(\pi x)/\sigma^2]\), with \(C_\sigma\) chosen to integrate to one. Since \(4\sin^2(\pi x)=2-2\cos(2\pi x)\), normalization yields exactly

\[
\psi_\sigma(x)=I_0(2\sigma^{-2})^{-1}e^{2\sigma^{-2}\cos(2\pi x)}.
\]

Squaring and integrating gives \(\|\psi_\sigma\|_2^2=I_0(4\sigma^{-2})/I_0(2\sigma^{-2})^2\). Thus \(\|\psi_\sigma-1\|_2^2=E(\sigma)>0\), the strict inequality following because \(\psi_\sigma\) is nonconstant with integral one.

**Step 2: uniform one-coordinate energy bounds.** Laplace's method applied to the defining integral gives

\[
I_0(z)=\frac{e^z}{\sqrt{2\pi z}}\bigl(1+O(z^{-1})\bigr)\quad(z\to\infty).
\]

Substitution at \(z=2/\sigma^2\) yields

\[
E(\sigma)=\frac{\sqrt{2\pi}}{\sigma}+O(1)\quad(\sigma\downarrow0).
\]

Continuity and strict positivity on \((0,1]\), together with \(\lim_{\sigma\downarrow0}\sigma E(\sigma)=c\), imply finite strictly positive extrema of \(\sigma E(\sigma)\) on the compactified interval \([0,1]\). Write these extrema as \(c_-\) and \(c_+\).

**Step 3: orthogonal supports and the exact energy.** Every \(\psi_{\rho/a_j}(x_j)-1\) has zero mean in coordinate \(j\). Distinct singleton components are orthogonal in \(L^2(\mathbb T^d)\) and orthogonal to the constant. Therefore

\[
\|K_{d,\rho}\|_2^2-1
=\sum_{\substack{j\le d\\a_j\ge\rho}}E(\rho/a_j).
\]

For each active \(j\), \(\sigma_j=\rho/a_j\in(0,1]\), and
\(\rho E(\sigma_j)=a_j[\sigma_jE(\sigma_j)]\). Step 2 immediately proves the two-sided bound.

**Step 4: necessity as well as sufficiency.** If \(\sum_ja_j<\infty\), Step 3 and \(\rho\le1\) bound \(\rho\|K_{d,\rho}\|_2^2\) uniformly. Conversely, for each fixed \(N\), choose \(0<\rho\le\min_{1\le j\le N}a_j\) and \(d\ge N\). The lower bound forces \(\sup_{d,\rho}\rho\|K_{d,\rho}\|_2^2\ge c_-\sum_{j=1}^Na_j\). If the supremum is finite, the partial sums are bounded, hence \(\sum_ja_j<\infty\).

**Step 5: sharp power-weight regimes.** Put \(t=p/4\). Active indices are \(1\le j\le N_\rho=\lfloor\rho^{-1/t}\rfloor\), so

\[
V_p(\rho)=\sum_{j=1}^{N_\rho}E(\rho j^t).
\]

For \(t>1\), pointwise convergence \(\rho E(\rho j^t)\to cj^{-t}\) and the summable majorant \(c_+j^{-t}\) prove the claimed zeta limit by dominated convergence for series. For \(t=1\), divide the range at \(\delta/\rho\) for fixed \(0<\delta<1\). On the lower range, \(\sigma E(\sigma)\to c\) uniformly after taking \(\delta\) small, giving \((c+o_\delta(1))\rho^{-1}\log(1/\rho)\); the upper range contributes \(O_\delta(\rho^{-1})\). Let \(\rho\downarrow0\), then \(\delta\downarrow0\). For \(t<1\), substitute \(j/\rho^{-1/t}\) and use Riemann sums on \([\delta,1]\). The omitted interval \((0,\delta)\) contributes at most \(C\delta^{1-t}\) after multiplication by \(\rho^{1/t}\), using \(E(\sigma)\le c_+/\sigma\). This yields \(\int_0^1E(u^t)\,du\), finite and positive because \(E(u^t)\sim cu^{-t}\) and \(t<1\).

**Step 6: exact Monte Carlo obstruction.** Each translated \(K_{d,\rho}\) integrates to one. For \(f\equiv1\), the random functions \(K_{d,\rho}(\cdot-X_r)-1\) are independent and have mean zero in the Hilbert space \(L^2(\mathbb T^d)\). Cross terms vanish in the expected squared norm. Translation preserves \(L^2\) norm, hence the expectation equals \(M^{-1}(\|K_{d,\rho}\|_2^2-1)\) exactly.

## Verification

A standalone numerical script, `CHECKER.py`, recomputes the Bessel-ratio energy using a quadrature representation of the scaled \(I_0\) function and checks the exact one-dimensional normalization, strict energy positivity, and the predicted approach to each of the three constants for representative powers. The analytic limit and necessity statements above do not rely on finite sampling or numerical checks. In a separate calculation, using exponentially scaled Bessel evaluation, the normalized ratios for \(p=2,4,8\) at \(\rho=0.015\) were approximately \(0.9857,1.0309,0.9000\), respectively; these illustrate convergence without proving it.

## Relationship to prior work

Sun (2026), Sections 3 and 5 and especially Proposition 5.1, defines the weight-adapted kernel and proves its orthogonal-support energy identity and **sufficient** \(O(\rho^{-q})\) energy bound under \(\sum_j\gamma_j^{1/(2a)}<\infty\). Theorem 5.3 then gives a sampling-error upper bound. Those identities are explicitly used here rather than claimed as new. The additional result is **necessity** at \(q=1\) for a concrete admissible Gaussian restriction, together with the exact critical logarithmic and subcritical polynomial constants, and the constant-input lower-bound interpretation. The published upper bound does not establish these lower bounds or sharp borderline rates.

Di Marzio, Panzera and Taylor (2011) develop von Mises and product toroidal density kernels, including risk calculations, but do not study the weight-truncated additive ANOVA multiplier here or the fourth-root weight summability barrier. Ebert and Pillichshammer (2021) analyze **optimal information complexity** in weighted Korobov spaces, which differs from the sampling variance of this specific kernel quasi-interpolant. Neither result implies the present three-regime exact asymptotics for this operator. Searches of published mathematical records located no equivalent statement; an unindexed equivalent remains possible.

## Limitations

The necessity threshold and exact power-weight constants concern the singleton-interaction construction with Gaussian radial restriction, bandwidth rule \(\rho_j=\rho\gamma_j^{-1/4}\), and independent uniform sampling. They do not show that every possible approximation algorithm, every ANOVA interaction order, or every periodic kernel must incur the same penalty. No independent audit has been performed. The comparison against older literature is limited to materially accessible sources and searchable published records.

## References

1. Z. Sun, *Weight-adapted ANOVA kernels for high-dimensional periodic approximation*, arXiv:2610.19409v1 (first public 2026-10-14), https://arxiv.org/pdf/2610.19409. Especially Sections 3–5 and Proposition 5.1/Theorem 5.3.
2. M. Di Marzio, A. Panzera, C. C. Taylor, *Kernel density estimation on the torus*, Journal of Statistical Planning and Inference 141 (2011), 2156–2173, author manuscript https://eprints.whiterose.ac.uk/id/eprint/42947/8/taylorcc1.pdf. Especially Sections 2 and 7.
3. A. Ebert, F. Pillichshammer, *Tractability of approximation in the weighted Korobov space in the worst-case setting — a complete picture*, arXiv:2102.01449v2 (2021), https://arxiv.org/pdf/2102.01449. Especially Sections 2–3.
