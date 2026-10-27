# Profile-sensitive two-circle Gaussian Jensen covariance and sharp radial decorrelation

## Finding

Let \(w\in C^1([0,1];(0,\infty))\), let \(G_0,G_1,\ldots\) be independent standard circular complex Gaussian variables, and for each integer \(n\ge 1\) set
\[
P_{n,w}(z)=\sum_{j=0}^{n-1}\sqrt{w(j/n)}\,G_j z^j,
\qquad
J_{n,w}(t)=\frac1{2\pi}\int_0^{2\pi}\log\left|P_{n,w}(e^{t/n+i\theta})\right|\,d\theta
\quad(t\in\mathbb R).
\]
Write
\[
\Phi_w(z)=\int_0^1 w(s)e^{zs}\,ds,
\qquad
H_w(t,u)=\frac1{8\pi}\int_{\mathbb R}
\operatorname{Li}_2\!\left(
\frac{|\Phi_w(t+u+ix)|^2}{\Phi_w(2t)\Phi_w(2u)}
\right)dx,
\]
where \(\operatorname{Li}_2(q)=\sum_{k\ge1}q^k/k^2\) for \(0\le q\le1\).

**Theorem.** For every real \(t,u\), and locally uniformly in the pair \((t,u)\),
\[
\lim_{n\to\infty}n\,\operatorname{Cov}(J_{n,w}(t),J_{n,w}(u))=H_w(t,u).
\tag{1}
\]
The integral defining \(H_w\) is absolutely convergent and strictly positive. For every fixed \(m\in\mathbb R\), the function \(d\mapsto H_w(m+d,m-d)\) is even and strictly decreasing on \([0,\infty)\). Moreover, for fixed \(m\), as \(d\to+\infty\),
\[
H_w(m+d,m-d)\sim
\frac{d^2e^{-2d-2m}}{w(0)w(1)}
\int_0^1w(s)^2e^{4ms}\,ds.
\tag{2}
\]
Thus the decay is exponentially sharp with an explicitly nonzero coefficient involving both endpoint weights and the bulk squared weight. With the reversed profile \(w^\leftarrow(s)=w(1-s)\), the exact limiting radial-duality identity is
\[
H_{w^\leftarrow}(-t,-u)=H_w(t,u).
\tag{3}
\]
For the uniform profile \(w\equiv1\), the coefficient in (2) simplifies to \(\sinh(2m)/(2m)\), continuously valued \(1\) at \(m=0\); in particular \(H_1(d,-d)\sim d^2e^{-2d}\).

## Assumptions and scope

Only the first \(n\) independent complex-Gaussian coefficients are used in the degree-\(n-1\) polynomial. Their variances are \(w(j/n)\). Positivity of the entire \(C^1\) profile gives constants \(0<c\le w\le C\), and its derivative is bounded. All circular logarithmic averages are almost surely finite and belong to \(L^2\). The scale \(e^{t/n}\) is the microscopic multiplicative radial window about the unit circle. The limit \(n\to\infty\) in (1) holds for fixed \(t,u\), uniformly on compact real parameter sets; the subsequently stated \(d\to\infty\) asymptotic (2) concerns the **limiting covariance** \(H_w\), not an unspecific simultaneous limit with \(n\). No assertion of a central limit theorem or independence of distinct radii is made.

## Proof

**1. Exact finite covariance.** Put
\[
\Phi_{n,w}(z)=\frac1n\sum_{j=0}^{n-1}w(j/n)e^{zj/n}.
\]
The variance of the circularly invariant complex Gaussian random variable \(P_{n,w}(e^{t/n+i\theta})\) is \(n\Phi_{n,w}(2t)\). Consequently
\[
\mathbb E J_{n,w}(t)=\frac12\log\bigl(n\Phi_{n,w}(2t)\bigr)-\frac\gamma2,
\]
where \(\gamma\) is Euler's constant. For standard jointly circular complex Gaussian variables with normalized correlation \(\rho\), the elementary Laguerre expansion gives
\[
\operatorname{Cov}(\log|Z_1|,\log|Z_2|)
=\frac14\operatorname{Li}_2(|\rho|^2).
\tag{4}
\]
For clarity, with \(X=|Z|^2\) of unit exponential law, the Laguerre basis \(L_k\) has \(\mathbb E[\log X\,L_k(X)]=-1/k\) for \(k\ge1\), and the two-Gaussian generating function yields \(\mathbb E[L_k(|Z_1|^2)L_\ell(|Z_2|^2)]=\mathbf1_{k=\ell}|\rho|^{2k}\). Equation (4) follows by \(L^2\)-expansion; it holds also when \(|\rho|=1\) by continuity. Rotation invariance reduces the double angular integral to one angle, hence the **exact identity**
\[
\operatorname{Cov}(J_{n,w}(t),J_{n,w}(u))=
\frac1{8\pi}\int_{-\pi}^{\pi}
\operatorname{Li}_2\!\left(
\frac{|\Phi_{n,w}(t+u+in\theta)|^2}
{\Phi_{n,w}(2t)\Phi_{n,w}(2u)}\right)d\theta.
\tag{5}
\]
This is not merely an asymptotic relation.

**2. The boundary-layer limit.** On each compact set of real \((t,u)\), the denominators in (5) are bounded below by a positive constant. Summation by parts applied to \(j\mapsto w(j/n)e^{(t+u)j/n}\) gives, uniformly on the compact parameter set and on \(-\pi\le\theta\le\pi\),
\[
|\Phi_{n,w}(t+u+in\theta)|\le \frac{C_K}{1+n|\theta|}.
\tag{6}
\]
Indeed, the coefficient sequence has bounded total variation independent of \(n\); combine the geometric-sum bound with its trivial \(O(n)\) bound before dividing by \(n\). Since \(0\le \operatorname{Li}_2(q)\le(\pi^2/6)q\) on \([0,1]\), after \(x=n\theta\) the integrand in \(n\) times (5) is bounded by \(C_K(1+|x|)^{-2}\), including all finite \(n\). Riemann sums yield \(\Phi_{n,w}(v)\to\Phi_w(v)\) uniformly for \(v\) in compact complex sets. Dominated convergence, together with uniformity of these bounds, proves (1) and absolute convergence. Positivity follows because \(\Phi_w(t+u)>0\), so the limiting integrand is positive near \(x=0\). Covariance positivity here is a property of this specific pair of circular means, not a general claim about arbitrary Gaussian log observables.

**3. Strict radial separation monotonicity.** Fix \(m\) and put \(t=m+d\), \(u=m-d\). The numerator \(|\Phi_w(2m+ix)|^2\) in (1) is independent of \(d\), while the denominator is
\[
D_m(d)=\Phi_w(2m+2d)\Phi_w(2m-2d).
\]
Let \(f(v)=\log\Phi_w(v)\) for real \(v\). Under the probability density proportional to \(w(s)e^{vs}\) on \([0,1]\), one has \(f''(v)=\operatorname{Var}_v(s)>0\). Therefore for \(d>0\),
\[
\frac{d}{dd}\log D_m(d)
=2\bigl(f'(2m+2d)-f'(2m-2d)\bigr)>0.
\]
Strict increase of the real dilogarithm and positivity of the numerator on an interval around \(x=0\) yield strict decrease of \(H_w(m+d,m-d)\). Evenness follows directly from the product defining \(D_m\).

**4. Sharp large-separation law.** One-sided Laplace asymptotics, valid because \(w\) is continuous and positive at the endpoints, give
\[
\Phi_w(2m+2d)\sim\frac{w(1)e^{2m+2d}}{2(m+d)},
\qquad
\Phi_w(2m-2d)\sim\frac{w(0)}{2(d-m)}.
\]
Thus \(D_m(d)\sim w(0)w(1)e^{2m+2d}/(4d^2)\). Since \(|\Phi_w(2m+ix)|\le\Phi_w(2m)\), the entire dilogarithm argument is \(O(D_m(d)^{-1})\), uniformly in \(x\). Expand \(\operatorname{Li}_2(q)=q+O(q^2)\) and integrate; \(\Phi_w(2m+ix)\) is the Fourier transform of the compactly supported function \(s\mapsto w(s)e^{2ms}\mathbf1_{[0,1]}(s)\). Plancherel gives
\[
\int_{\mathbb R}|\Phi_w(2m+ix)|^2dx
=2\pi\int_0^1 w(s)^2e^{4ms}\,ds.
\]
The \(O(D_m(d)^{-2})\) integrated remainder is finite because this Fourier transform is bounded and square-integrable. Substitution proves (2) including the exact constant. The constant is positive and finite.

**5. Radial reversal.** Changing variables in the defining integral gives \(\Phi_{w^\leftarrow}(z)=e^z\Phi_w(-z)\). In the normalized ratio of (1), the exponential factors cancel, and complex conjugation leaves the absolute value unchanged. Therefore (3) holds.

## Verification

The standalone file `circular_covariance_check.py` evaluates (5) by FFT sampling and evaluates the limiting integral by adaptive quadrature for three strictly positive affine profiles. Its run passed 34 comparisons: finite-to-limit convergence across three parameter pairs, strict separation checks, large-separation leading constants, reversal duality, and the exact single-coefficient Gaussian variance \(\pi^2/24\). The quadrature truncation at \(|x|=1000\) is not an exact evaluation; the proof's \(O((1+|x|)^{-2})\) integrable majorant is the analytical tail control. Execute with `python circular_covariance_check.py` (NumPy and SciPy required). The checker corroborates, rather than replaces, steps 1–5.

## Relationship to prior work

Kiro and Nishry, *Fluctuations for Zeros of Gaussian Taylor Series* (arXiv:1911.13051; 2019), establish broad results on zero-count fluctuations and record the general dilogarithm covariance machinery for Gaussian analytic functions in their appendix. Their circle-zero-count variance is not the present two-radius covariance of logarithmic **circular means** for finite polynomials with macroscopic profiles, and their conclusions do not give the strict fixed-midpoint radial decorrelation or the sharp endpoint-weight coefficient in (2). Buckley and Nishry, *Gaussian Complex Zeroes are not Always Normal* (arXiv:2104.12598; 2021), analyze hyperbolic Gaussian analytic-function zero counts and their limiting laws, a distinct regime and observable. The general two-point Gaussian identity (4) is acknowledged as classical input, not claimed as new. Earlier single-radius Mahler variance asymptotics for the constant profile arise from the specialization \(w\equiv1,t=u=0\), but do not yield the full two-parameter profile law or the sharp distance monotonicity and asymptotic coefficient. A historical-priority risk persists for possible equivalent formulations of the covariance kernel under Jensen potentials or Gaussian log-field terminology.

## Limitations

The profile must be positive on the closed interval and continuously differentiable for the stated uniform Fourier domination. Profiles vanishing at either endpoint can have different large-separation powers. The \(d\to\infty\) statement is **after** the \(n\to\infty\) limit. The result concerns covariances; it neither proves Gaussian limiting distributions nor characterizes zero-count covariance in annuli. All originality comparisons are conditional on inspected accessible sources; independence and historical uniqueness are not certified.

## References

1. A. Kiro and A. Nishry, *Fluctuations for Zeros of Gaussian Taylor Series*, arXiv:1911.13051 (first submitted 2019-11-29), *Journal of the London Mathematical Society* **104** (2021), 1172–1203, https://doi.org/10.1112/jlms.12457 . Full text, Sections 1, 3 and Appendix.
2. J. Buckley and A. Nishry, *Gaussian Complex Zeroes are not Always Normal: Limit Theorems on the Disc*, arXiv:2104.12598 (first submitted 2021-04-26), *Probability and Mathematical Physics* **3** (2022), 675–706, https://doi.org/10.2140/pmp.2022.3.675 . Full text, Section 1 and related-work discussion.
3. The Laguerre expansion and Fourier-Plancherel identity used in the proof are reproduced directly above; no result on asymptotic distributions is imported.
