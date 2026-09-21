# Sharp Rayleigh-residual distortion under normal spectral filtering

## Result

Let \(A\in\mathbb C^{n\times n}\) be normal with at least two distinct eigenvalues, let \(x\) be a unit vector, and define the Rayleigh quotient and Rayleigh residual by
\[
\rho(x)=x^*Ax,\qquad r(x)=Ax-\rho(x)x.
\]
Let \(\phi\) be any finite-valued scalar function on \(\sigma(A)\), let \(F=\phi(A)\), and whenever \(Fx\ne0\) set
\[
y=\frac{Fx}{\|Fx\|_2}.
\]
This includes polynomial filters and rational filters with no poles on the spectrum. All statements below are in exact arithmetic and concern one pure filtering-and-normalization step, before any Rayleigh--Ritz extraction.

Write
\[
m=\min_{\lambda\in\sigma(A)}|\phi(\lambda)|,\qquad
M=\max_{\lambda\in\sigma(A)}|\phi(\lambda)|.
\]
If \(m>0\), then for every non-eigenvector \(x\), with \(s=\|Fx\|_2\),
\[
\boxed{
\frac{m}{s}\,\|r(x)\|_2
\le \|r(y)\|_2
\le \frac{M}{s}\,\|r(x)\|_2 .
}
\]
Consequently,
\[
\boxed{
\frac{m}{M}\le
\frac{\|r(y)\|_2}{\|r(x)\|_2}
\le\frac{M}{m}.
}
\]
Both global constants are sharp:
\[
\boxed{
\sup_{r(x)\ne0}\frac{\|r(y)\|_2}{\|r(x)\|_2}=\frac{M}{m},
\qquad
\inf_{r(x)\ne0}\frac{\|r(y)\|_2}{\|r(x)\|_2}=\frac{m}{M}.
}
\]
Thus the gain dynamic range \(M/m\) is exactly the worst-case one-step amplification factor of the standard Rayleigh residual.

The zero-gain case has a sharp dichotomy. If \(m=0\) and \(\phi\) is nonzero on at least two distinct eigenvalues while vanishing on another distinct eigenvalue, then
\[
\boxed{
\sup_{Fx\ne0,\ r(x)\ne0}
\frac{\|r(y)\|_2}{\|r(x)\|_2}=\infty .
}
\]
If instead the nonzero support of \(\phi\) lies in one eigenspace, every defined filtered vector is an exact eigenvector and its output residual is zero.

## Proof

Choose an orthonormal eigenbasis \(Au_i=\lambda_i u_i\) and write
\[
x=\sum_i c_i u_i,\qquad w_i=|c_i|^2,\qquad \sum_iw_i=1.
\]
Normality gives
\[
\rho(x)=\sum_iw_i\lambda_i,
\qquad
\|r(x)\|_2^2
=\sum_iw_i|\lambda_i-\rho(x)|^2
=\min_{z\in\mathbb C}\sum_iw_i|\lambda_i-z|^2.
\]
Let \(g_i=|\phi(\lambda_i)|\). Since
\[
s^2=\|Fx\|_2^2=\sum_iw_i g_i^2,
\]
the normalized filtered vector has spectral weights
\[
q_i=\frac{w_i g_i^2}{s^2}.
\]
Therefore
\[
\|r(y)\|_2^2
=\frac1{s^2}\min_{z\in\mathbb C}
\sum_iw_i g_i^2|\lambda_i-z|^2.
\]
If \(m>0\), then for every \(z\)
\[
m^2\sum_iw_i|\lambda_i-z|^2
\le
\sum_iw_i g_i^2|\lambda_i-z|^2
\le
M^2\sum_iw_i|\lambda_i-z|^2.
\]
Taking minima and square roots proves the state-dependent bound, and \(m\le s\le M\) yields the global bound.

For sharpness, choose distinct eigenvalues \(a,b\) whose gains are \(m,M\), with corresponding unit eigenvectors \(u_a,u_b\), and set
\[
x_p=\sqrt{1-p}\,u_a+\sqrt p\,u_b,\qquad 0<p<1.
\]
A two-point variance calculation gives the exact ratio
\[
\frac{\|r(y_p)\|_2}{\|r(x_p)\|_2}
=
\frac{mM}{(1-p)m^2+pM^2}.
\]
As \(p\downarrow0\) this tends to \(M/m\), and as \(p\uparrow1\) it tends to \(m/M\). If \(M=m\), filtering preserves all spectral weights, so the residual norm is exactly preserved for every input.

Now suppose \(m=0\). Let \(u_0\) be an eigenvector at a zero-gain eigenvalue \(\lambda_0\). If two distinct retained eigenvalues exist, choose a unit vector \(z\) with nonzero components in both retained eigenspaces, so \(r(Fz/\|Fz\|_2)\ne0\), and define
\[
x_\varepsilon=\sqrt{1-\varepsilon}\,u_0+\sqrt\varepsilon\,z.
\]
Then \(\|r(x_\varepsilon)\|_2=\Theta(\sqrt\varepsilon)\), while
\[
\frac{Fx_\varepsilon}{\|Fx_\varepsilon\|_2}
=\frac{Fz}{\|Fz\|_2}
\]
is independent of \(\varepsilon\) and has positive residual. The ratio therefore diverges like \(\varepsilon^{-1/2}\). If the nonzero support is a single eigenspace, the filtered vector lies in that eigenspace and has zero residual. This proves the dichotomy.

## Exact universal monotonicity classification

For a fixed normal \(A\), a nonzero spectral filter is Rayleigh-residual nonexpansive for every input on which it is defined if and only if one of the following holds:

1. \(|\phi|\) is constant and nonzero on \(\sigma(A)\). Then the spectral weights are unchanged and \(\|r(y)\|_2=\|r(x)\|_2\) for every input.
2. The nonzero support of \(\phi\) is contained in one eigenspace. Then \(\|r(y)\|_2=0\) for every defined input.

Indeed, unequal nonzero gains give a two-eigenvalue input with residual growth by the sharpness construction, while a zero together with two distinct retained eigenvalues gives unbounded relative growth.

Hence every genuinely selective nonvanishing filter has some input on which the raw Rayleigh residual increases, even though its purpose is to improve spectral separation.

## Sharp separation-versus-residual tradeoff

Let \(\Lambda\subsetneq\sigma(A)\) be a nonempty target spectral set, and suppose all filter gains are nonzero. Define the standard wanted/unwanted separation factor
\[
\eta(\phi;\Lambda)
=
\frac{\max_{\mu\in\sigma(A)\setminus\Lambda}|\phi(\mu)|}
{\min_{\lambda\in\Lambda}|\phi(\lambda)|},
\qquad 0<\eta<1.
\]
Filtered subspace iteration is designed so that wanted gains dominate unwanted gains, exactly the type of condition used in the filtered-subspace literature. Since
\[
M\ge \min_{\lambda\in\Lambda}|\phi(\lambda)|,
\qquad
m\le \max_{\mu\notin\Lambda}|\phi(\mu)|,
\]
the sharp distortion law implies
\[
\boxed{
\sup_x\frac{\|r(y)\|_2}{\|r(x)\|_2}
=\frac{M}{m}\ge \frac1\eta .
}
\]
Moreover this is a sharp minimax tradeoff over spectral multipliers:
\[
\boxed{
\inf_{\phi:\ \eta(\phi;\Lambda)\le\eta}
\ \sup_x\frac{\|r(y)\|_2}{\|r(x)\|_2}
=\frac1\eta,
\qquad 0<\eta<1,
}
\]
where the infimum is over filters nonzero on the spectrum. Equality is attained by any two-level magnitude filter that has one constant magnitude on \(\Lambda\) and a factor \(\eta\) times that magnitude on its complement. On a finite spectrum such values can be realized by polynomial interpolation, although the interpolating degree may be impractical.

Thus a filter that improves the standard spectral-separation factor by making \(\eta\) smaller necessarily worsens the worst-case raw Rayleigh-residual spike by at least the reciprocal factor. This is a worst-case statement about the pure filtering stage, not about a complete eigensolver with orthogonalization and Rayleigh--Ritz extraction.

The endpoint \(\eta=0\) is singular. An exact projector onto a single eigenvalue annihilates the residual, while an exact projector retaining at least two distinct eigenvalues has unbounded relative residual amplification over inputs approaching a killed eigendirection.

## Corollaries

### Normalized power iteration

For invertible normal \(A\), one normalized power step corresponds to \(\phi(\lambda)=\lambda\). Since a normal matrix has singular values \(|\lambda_i|\),
\[
\boxed{
\sup_x
\frac{\|r(Ax/\|Ax\|_2)\|_2}{\|r(x)\|_2}
=\kappa_2(A).
}
\]
Thus even for an SPD matrix the usual Rayleigh residual can increase by almost the full spectral condition number in one power step.

For the sharp two-dimensional SPD model \(A=\operatorname{diag}(1,\kappa)\), if \(p\) is the spectral weight on the \(\kappa\)-eigenvector, then
\[
\boxed{
\frac{\|r(x_+)\|_2}{\|r(x)\|_2}
=
\frac{\kappa}{1+p(\kappa^2-1)}.
}
\]
The residual increases exactly when \(p<1/(\kappa+1)\), is unchanged at equality, and decreases above that threshold. The Rayleigh quotient nevertheless moves monotonically toward the dominant eigenvalue for this SPD power iteration.

### Fixed-shift inverse iteration with the updated Rayleigh residual

For \(\phi(\lambda)=(\lambda-\sigma)^{-1}\), with \(\sigma\notin\sigma(A)\),
\[
\boxed{
\sup_x\frac{\|r(y)\|_2}{\|r(x)\|_2}
=
\frac{\max_{\lambda\in\sigma(A)}|\lambda-\sigma|}
{\min_{\lambda\in\sigma(A)}|\lambda-\sigma|}.
}
\]
This uses the Rayleigh residual \((A-\rho(y)I)y\) recomputed at each iterate. It does not contradict the classical monotonicity result for normal inverse iteration proved for the fixed-shift residual \((A-\sigma I)x_k\); these are different diagnostics.

### Exact-zero example and minimal dimension

Take
\[
A=\operatorname{diag}(0,1,3),\qquad \phi(t)=t,
\]
and
\[
x_\varepsilon=
\left(\sqrt{1-\varepsilon},\sqrt{\varepsilon/2},\sqrt{\varepsilon/2}\right)^T.
\]
Then
\[
\|r(x_\varepsilon)\|_2=\sqrt{\varepsilon(5-4\varepsilon)},
\]
while the normalized filtered vector is
\[
y=(0,1/\sqrt{10},3/\sqrt{10})^T,
\qquad \|r(y)\|_2=0.6.
\]
Hence the relative amplification diverges as \(\varepsilon^{-1/2}\). Three distinct eigenvalues are minimal for this exact-zero/unbounded phenomenon: in dimension two, killing one eigendirection leaves only one distinct eigendirection and therefore gives zero output residual.

### Generalized Hermitian definite eigenproblems

Let \(A=A^*\), \(B\succ0\), and \(T=B^{-1}A\). The operator \(T\) is self-adjoint in the \(B\)-inner product. For \(B\)-normalized \(x\), define
\[
\rho_B(x)=\frac{x^*Ax}{x^*Bx}.
\]
Then
\[
\|Ax-\rho_B(x)Bx\|_{B^{-1}}
=
\|(T-\rho_B(x)I)x\|_B.
\]
Applying the theorem to \(\phi(T)\) and normalizing in the \(B\)-norm yields the same sharp distortion law, zero-gain dichotomy, and separation tradeoff with the generalized eigenvalues replacing \(\sigma(A)\).

## Relation to prior work

Classical and modern filtered-subspace methods measure filter quality by separation of wanted and unwanted spectral gains. Gopalakrishnan, Grubišić, and Ovall explicitly use a ratio of a supremum unwanted gain to an infimum wanted gain below one in their filtered-subspace analysis. Polynomial-filtered Lanczos and rational-filtered subspace methods likewise design filters to amplify wanted spectral components. These works establish eigenspace/eigenvalue convergence and practical filter design; the present result instead identifies the exact worst-case distortion of the single-vector Rayleigh residual under the pure filter map and shows a reciprocal minimax tradeoff with spectral separation.

Recent work of Di Napoli and Wu studies the condition number of the *matrix of filtered vectors* in Chebyshev subspace iteration in order to choose a stable QR factorization. That conditioning problem is distinct from the one-vector Rayleigh-residual distortion here. Recent residual-based Chebyshev filtered subspace iteration reformulates recurrences to tolerate inexact matrix-vector products; its residual analysis addresses approximation error and convergence rather than the exact gain-dynamic-range law above.

Ipsen's classical inverse-iteration analysis proves monotonicity of the fixed-shift residual for normal matrices. The inverse-iteration corollary above concerns the standard Rayleigh residual with the Rayleigh quotient recomputed after each iterate, and therefore addresses a different residual quantity.

To the best of our knowledge, searches across power/inverse iteration, polynomial and rational filtering, filtered subspace iteration, Rayleigh-residual bounds, spectral transformations, and recent filtered-eigensolver conditioning work did not locate the exact \(M/m\) distortion law, the zero-gain classification, or the sharp \(1/\eta\) separation-versus-residual minimax tradeoff. The algebra is elementary once the residual is recognized as a spectral variance, so older spectral-transformation, simultaneous-iteration, or general variance-comparison literature remains a meaningful historical-equivalence risk.

## Limitations

- Exact arithmetic and finite-dimensional normal matrices only for the main theorem. Nonnormal matrices are outside scope.
- The filter is applied exactly. Roundoff, inexact linear solves, and approximation error in evaluating polynomial or rational filters are not included.
- The result concerns a single normalized filtering step before orthogonalization or Rayleigh--Ritz extraction; it does not claim that residuals produced by a complete filtered eigensolver obey the same one-step law.
- Relative amplification can be unbounded when the input residual tends to zero; no unbounded absolute residual is claimed.
- The minimax separation result is over unrestricted spectral multipliers (equivalently, over values on a finite spectrum). Degree-constrained polynomial or pole-constrained rational filter design can impose additional costs.
- Older subspace-iteration and spectral-transformation literature is broad and was not exhaustively checked theorem by theorem, leaving residual originality uncertainty.

## Reproducibility

`artifacts/verify.py` performs deterministic numerical checks of the normal-matrix bound, the exact two-eigenvalue sharpness formula, the power-iteration corollary, and the three-dimensional exact-zero example. `artifacts/verification.txt` contains the verified output. These checks are sanity tests; the theorem is established by the proof above.

## References

1. I. C. F. Ipsen, *Computing an Eigenvector with Inverse Iteration*, SIAM Review 39 (1997), 254--291. https://doi.org/10.1137/S0036144596300773
2. Y. Zhou and Y. Saad, *A Chebyshev--Davidson Algorithm for Large Symmetric Eigenproblems*, SIAM J. Matrix Anal. Appl. 29 (2007), 954--971. https://doi.org/10.1137/050630404
3. R. Li, Y. Xi, E. Vecharynski, C. Yang, and Y. Saad, *A Thick-Restart Lanczos Algorithm with Polynomial Filtering for Hermitian Eigenvalue Problems*, SIAM J. Sci. Comput. 38 (2016), A2512--A2534. https://doi.org/10.1137/15M1054493
4. Y. Xi and Y. Saad, *Computing Partial Spectra with Least-Squares Rational Filters*, SIAM J. Sci. Comput. 38 (2016), A3020--A3045. https://doi.org/10.1137/16M1061965
5. J. Gopalakrishnan, L. Grubišić, and J. S. Ovall, *Spectral Discretization Errors in Filtered Subspace Iteration*, Math. Comp. 89 (2020), 203--228. https://doi.org/10.1090/mcom/3483
6. N. Kodali, K. Ramakrishnan, and P. Motamarri, *Residual-based Chebyshev filtered subspace iteration for sparse Hermitian eigenvalue problems tolerant to inexact matrix-vector products*, arXiv:2503.22652. https://arxiv.org/abs/2503.22652
7. E. Di Napoli and X. Wu, *Estimating the condition number of Chebyshev filtered vectors with application to the ChASE library*, arXiv:2603.10514. https://arxiv.org/abs/2603.10514
