# Sharp condition-number tails for sequential Gaussian-perturbed QR columns

## Finding

**Theorem.** Fix integers \(m\ge n\ge2\), noise scale \(\sigma>0\), and finite deterministic signal lengths \(\ell_1,\ldots,\ell_n\ge0\). Starting with an empty matrix, construct \(A_i=[q_1,\ldots,q_i]\in\mathbb R^{m\times i}\) by
\[
q_i=\frac{x_i+Y_i}{\|x_i+Y_i\|_2},\qquad
Y_i\overset{\mathrm{iid}}{\sim}N(0,\sigma^2I_m),
\]
where, conditional on all earlier noises, \(x_i\) is a measurable vector of norm \(\ell_i\), orthogonal to the span of the earlier columns. Put \(d=m-n+1\) and let \(\kappa\) denote the spectral condition number (largest divided by smallest singular value). Every \(A_i\) has full column rank almost surely.

Write \(B=A_{n-1}\); conditionally on \(B\), let \(u\) be a uniformly distributed unit vector in \(\operatorname{span}(B)\), independent of the construction given \(B\). Define
\[
D(B,u)=\bigl\|[B,u]\bigr\|_2\sqrt{1+\|B^\dagger u\|_2^2}.
\]
Then \(0<C_{m,n}<\infty\) and
\[
\boxed{\lim_{t\to\infty}t^d\Pr\{\kappa(A_n)>t\}=C_{m,n}
=e^{-\ell_n^2/(2\sigma^2)}
\frac{\Gamma(m/2)}{\Gamma((n-1)/2)\Gamma(d/2+1)}
\mathbb E_{B,u}\bigl[D(B,u)^d\bigr].}
\]
In particular, the exact positive-moment frontier is
\[
\mathbb E\bigl[\kappa(A_n)^p\bigr]<\infty
\quad\Longleftrightarrow\quad 0<p<d.
\]
For every square process (\(m=n\)) with nonzero Gaussian variance, \(\mathbb E\kappa(A_n)=\infty\), regardless of how small \(\sigma\) is or how large the finite signal lengths are. For \(m\ge n+1\), the first moment is finite. Thus a single extra row changes mean conditioning from infinite to finite in this model.

For two columns the earlier random history drops out of the constant:
\[
C_{m,2}=2^{m-1}e^{-\ell_2^2/(2\sigma^2)}
\frac{\Gamma(m/2)}{\Gamma(1/2)\Gamma((m+1)/2)}.
\]
In particular \(C_{2,2}=(4/\pi)e^{-\ell_2^2/(2\sigma^2)}\) and \(C_{3,2}=2e^{-\ell_2^2/(2\sigma^2)}\). These coefficients are for the exact condition number, not only for an upper certificate.

## Assumptions and scope

There are \(n\) normalized real columns in an ambient \(m\)-dimensional Euclidean space; \(m\) and \(n\) are fixed, not simultaneously asymptotic. At each step \(x_i\) is predictable, orthogonal to prior computed columns, and has **deterministic** length \(\ell_i\), although its direction may depend arbitrarily and measurably on the past. The added noises are independent isotropic Gaussians with common variance \(\sigma^2>0\). The theorem addresses the condition number of the **computed normalized columns**, not the condition number of an exact orthogonal \(Q\), an unnormalized iid Gaussian matrix, or finite-precision rounding errors without a stochastic noise model. Zero signal lengths are admitted as mathematically meaningful limits; the conclusions also hold for strictly positive signal lengths.

The constant involves an ordinary finite-dimensional expectation over the computed \((n-1)\)-column history and a uniform direction in its span. It is not asserted to simplify to elementary functions for general \(n\). No independence between the earlier computed columns is assumed or needed.

## Proof

**1. Conditional splitting and full rank.** Let \(d_i=m-i+1\). Conditional on the earlier columns \(A_{i-1}\), choose orthonormal coordinates in their span and its orthogonal complement. The fresh perturbation splits independently as \(V_i\sim N(0,\sigma^2I_{i-1})\) and \(Z_i\sim N(0,\sigma^2I_{d_i})\). The perpendicular part of the unnormalized new column is \(W_i=x_i+Z_i\), with \(\|x_i\|_2=\ell_i\). Consequently
\[
\rho_i:=\|P_{A_{i-1}}^\perp q_i\|_2
=\frac{\|W_i\|_2}{\sqrt{\|V_i\|_2^2+\|W_i\|_2^2}}.
\]
Since \(W_i\) has a continuous full-dimensional Gaussian density in dimension \(d_i\ge1\), \(\rho_i>0\) almost surely. Induction gives full column rank. The distribution of \(\|W_i\|_2\) depends on the predictable signal only through the deterministic \(\ell_i\).

**2. A finite-moment domination lemma.** For each real \(0<p<d_i\) there is a finite constant \(M_{i,p}\), depending only on \(m,i,p,\sigma\), such that
\[
\mathbb E[\rho_i^{-p}\mid A_{i-1}]\le M_{i,p}.
\]
Indeed \(\rho_i^{-p}=(1+\|V_i\|^2/\|W_i\|^2)^{p/2}\); its expectation is bounded by a fixed multiple of \(1+\mathbb E\|V_i\|^p\mathbb E\|W_i\|^{-p}\). The noncentral chi-square variable \(\|W_i\|^2/\sigma^2\) stochastically dominates a central chi-square variable of \(d_i\) degrees (e.g. use its Poisson mixture by central chi-squares of degrees \(d_i+2j\)). The latter has finite inverse \(p/2\)-moment exactly for \(p<d_i\), giving a bound uniform in signal direction and length.

For unit-length columns the deterministic append-column estimate
\[
\kappa(A_i)\le\kappa(A_{i-1})
\frac{1+\sqrt{1-\rho_i^2}}{\rho_i}
\le\frac{2\kappa(A_{i-1})}{\rho_i}
\]
holds for \(i\ge2\); here \(\kappa(A_1)=1\). Taking conditional expectations and inducting yields \(\mathbb E[\kappa(A_i)^p]<\infty\) whenever \(0<p<d_i\). In particular \(\mathbb E[\kappa(B)^d]<\infty\), because the final perpendicular dimension of \(B=A_{n-1}\) is \(d+1\).

**3. Singular-column coefficient.** Fix a full-rank \(B\) with unit columns and a unit \(u\in\operatorname{span}(B)\). For any unit \(v\perp\operatorname{span}(B)\), let
\[
q(\rho)=\sqrt{1-\rho^2}\,u+\rho v,\qquad 0<\rho<1.
\]
The Gram matrix of \([B,q(\rho)]\) is independent of \(v\). At \(\rho=0\) its null vector is \((-B^\dagger u,1)\); all its other eigenvalues are strictly positive. Differentiating the Gram matrix with respect to \(\rho^2\) at zero and taking its Rayleigh quotient on the normalized null vector gives
\[
\sigma_{\min}([B,q(\rho)])
=\frac{\rho}{\sqrt{1+\|B^\dagger u\|_2^2}}(1+o(1)).
\]
Simultaneously \(\sigma_{\max}([B,q(\rho)])\to\|[B,u]\|_2\). Thus, **uniformly in the perpendicular direction**,
\[
\lim_{\rho\downarrow0}\rho\,\kappa([B,q(\rho)])=D(B,u).
\]
This step uses the actual smallest singular value rather than treating the upper condition-number certificate as equality.

**4. Conditional small-ball tail.** At the last step, condition on \(B\). Let \(R=\|V_n\|_2\), \(u=V_n/R\) interpreted in the embedded span of \(B\), and \(W=W_n\) in the perpendicular \(d\)-space. Here \(V_n\) is a centered \((n-1)\)-dimensional isotropic Gaussian, so \(R>0\) almost surely and \(u\) is uniform in the span, independent of \(R\) and \(W\). The density of \(W\) at the origin is
\[
f_W(0)=(2\pi\sigma^2)^{-d/2}e^{-\ell_n^2/(2\sigma^2)}.
\]
The normalized appended column has perpendicular length
\[
\rho=\frac{\|W\|}{\sqrt{R^2+\|W\|^2}}.
\]
For fixed full-rank \(B\), \(R>0\), and \(u\), step 3 gives
\[
\kappa([B,q_n])=\frac{R D(B,u)}{\|W\|}(1+o(1))
\quad\text{as }\|W\|\downarrow0.
\]
The little-oh is uniform in the direction of \(W\). The Gaussian small-ball law \(\Pr(\|W\|<h)\sim f_W(0)\,\omega_d h^d\), \(\omega_d=\pi^{d/2}/\Gamma(d/2+1)\), implies
\[
\lim_{t\to\infty}t^d\Pr\{\kappa(A_n)>t\mid B,V_n\}
=\omega_d f_W(0)R^dD(B,u)^d.
\]

**5. Validating the exchange of limit and expectation.** Let \(K=\kappa(B)\ge1\). The append-column bound gives
\[
\kappa(A_n)\le2K\frac{\sqrt{R^2+\|W\|^2}}{\|W\|}.
\]
If \(t>4K\), the event \(\kappa(A_n)>t\) requires
\[
\|W\|<\frac{2KR}{\sqrt{t^2-4K^2}}\le\frac{4KR}{t}.
\]
The Gaussian density is bounded, hence in this case \(t^d\Pr(\kappa(A_n)>t\mid B,V_n)\le c_d K^dR^d\) with a deterministic constant \(c_d\). For \(t\le4K\), the same left-hand side is at most \((4K)^d\). Therefore it is dominated by a constant times \(K^d(1+R^d)\), integrable by step 2 and Gaussian moments. Dominated convergence applies.

Since
\[
\mathbb E R^d=\sigma^d2^{d/2}\frac{\Gamma(m/2)}{\Gamma((n-1)/2)},
\]
multiplying by \(\omega_d f_W(0)\) yields the displayed \(C_{m,n}\). Positivity follows from strictly positive Gaussian density and \(D(B,u)>0\) for full-rank \(B\); finiteness follows, for example, from \(D(B,u)\le\sqrt{2n}\,\kappa(B)\) and step 2. Step 2 already proves moments finite for \(p<d\); the positive \(t^{-d}\) tail and the tail-integration identity prove divergence for every \(p\ge d\).

**6. Two-column constant.** When \(n=2\), \(B\) consists of one unit column, \(u=\pm B\), and \(D(B,u)=2\) deterministically. Substitution gives the stated closed form. In the zero-signal limiting case with \(m=n=2\), the exact formula \(\Pr\{\kappa(A_2)>t\}=(4/\pi)\arctan(1/t)\) for \(t>1\) supplies an independent check of the coefficient; for \(m=3,n=2\), it is \(2/(t^2+1)\). These elementary checks are not used to prove the general theorem.

## Verification

The standalone script `verify_qr_tail.py` checks 300 random full-rank bordered singular-value limits, 255 smallest-singular-value expansions, the two independent exact zero-signal formulas, and noncentral-Gaussian quadratures at two thresholds in ambient dimensions two and three. Run `python verify_qr_tail.py` with NumPy and SciPy installed. These finite tests are diagnostics; the general statement is proved by steps 1–6 above. The expectation in \(C_{m,n}\) is a mathematically exact representation, not an experimentally estimated universal constant.

## Relationship to prior work

Lotfi, Langou and Meysami (arXiv:2409.18905, first submitted 2024-09-27) analyze the same normalized Gaussian-perturbation model. Their Theorem 6.1 gives the exact noncentral-\(F\) law of a single normalized projection residual; Corollary 7.3 bounds the condition multiplier by that residual; Corollary 7.5 yields a multi-step probability/product bound. Those inputs control rare events but do **not** give the actual full-matrix spectral-condition-number tail coefficient, nor establish that it is governed exactly by the final perpendicular dimension after integrating over the potentially ill-conditioned history. The singular-column coefficient \(D(B,u)\), integrable history control, exact asymptotic, and moment classification are the additional statements here.

Edelman and Sutton, *Tails of Condition Number Distributions* (2005), prove sharp tail laws for independent Gaussian-entry (Wishart) matrices. Their square/rectangular exponent illustrates a parallel phenomenon, but their input matrix has iid, **unnormalized** columns. The present columns are normalized and generally depend nonlinearly on all previous columns through predictable perpendicular signal directions, so the Wishart result cannot directly provide the present coefficient. Liesen, Rozložník and Strakoš (2002) give deterministic residual/conditioning relations for adding a column; these do not compute stochastic constants. Their deterministic ideas are acknowledged rather than claimed as new.

## Limitations

The conclusions depend on exact isotropic Gaussian perturbations, full normalization of each computed column, fixed dimensions, and predictable finite-length perpendicular signals. They are not an assertion that real floating-point QR always has infinite expected condition number, nor a statement about algorithmic error beyond the specified model. The formula does not give a closed elementary value for general random earlier histories, and it does not address noise that is confined strictly to the earlier span, complex-valued perturbations, correlated noise, or a random unbounded final signal length. The theorem is a same-model mathematical analysis; it has not received independent external audit.

## References

1. A. Lotfi, J. Langou, M. Meysami, *Probabilistic Analysis of Least Squares, Orthogonal Projection, and QR Factorization Algorithms Subject to Gaussian Noise*, arXiv:2409.18905, first submitted 2024-09-27; sections 6–7 of accessible revision. https://arxiv.org/abs/2409.18905
2. A. Edelman, B. D. Sutton, *Tails of Condition Number Distributions*, SIAM J. Matrix Anal. Appl. 27 (2005), 547–560. https://doi.org/10.1137/040614256 ; lawful author copy: https://math.mit.edu/~edelman/homepage/papers/conditions.pdf
3. J. Liesen, M. Rozložník, Z. Strakoš, *Least squares residuals and minimal residual methods*, SIAM J. Sci. Comput. 23 (2002), 1503–1525 (bibliography verified against the reference list of Lotfi–Langou–Meysami).
