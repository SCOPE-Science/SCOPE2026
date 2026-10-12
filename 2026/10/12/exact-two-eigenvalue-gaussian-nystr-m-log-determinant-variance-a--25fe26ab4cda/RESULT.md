# Exact two-eigenvalue Gaussian Nyström log-determinant variance and its square-root spectral-gap penalty
## Finding

Let \(A\) be a real symmetric positive-definite \(2\times2\) matrix with prescribed eigenvalues \(a\ge b>0\). Let \(\omega,w\in\mathbb R^2\) be independent vectors whose coordinates are independent standard normal variables. Define
\[
\widehat A=A\omega(\omega^{\mathsf T}A\omega)^{-1}\omega^{\mathsf T}A,\quad P=I+\widehat A,\quad M=P^{-1/2}(I+A)P^{-1/2},
\]
and the one-probe preconditioned estimator
\[
\widehat L=\log\det P+w^{\mathsf T}(\log M)w,\qquad L_*=\log\det(I+A).
\]
The denominator is positive almost surely, and both matrix logarithms are the real principal logarithms of positive-definite matrices. The estimator is unbiased. Put
\[
u=\frac{\sqrt a-\sqrt b}{\sqrt a+\sqrt b},\quad
v=\frac{\sqrt{a(1+a)}-\sqrt{b(1+b)}}{\sqrt{a(1+a)}+\sqrt{b(1+b)}},
\]
\[
m=\log((1+a)(1+b))+2\log\frac{\sqrt a+\sqrt b}{\sqrt{a(1+a)}+\sqrt{b(1+b)}},
\qquad \operatorname{Li}_2(z)=\sum_{k=1}^{\infty}\frac{z^k}{k^2}\quad(0\le z<1).
\]
Then, with expectation over **both independent Gaussian vectors**, the exact mean-squared error is
\[
\boxed{\mathbb E(\widehat L-L_*)^2
=2m^2+4\bigl[\operatorname{Li}_2(u^2)+\operatorname{Li}_2(v^2)-2\operatorname{Li}_2(uv)\bigr].}
\]
The corresponding ideal top-eigenvector rank-one preconditioner has mean-squared error \(2\log^2(1+b)\). For \(a>b\), the random Nyström error is strictly larger; equality holds for \(a=b\).

For every fixed \(b>0\), the high-contrast limit is the **sharp expansion**
\[
\boxed{\mathbb E(\widehat L-L_*)^2
=2\log^2(1+b)+8[\log(1+b)+2\log 2]\sqrt{\frac ba}
+o\!\left(\sqrt{\frac ba}\right)\quad(a\to\infty).}
\]
The excess decays only with the square root of the inverse spectral contrast. The formulas hold unchanged under any real orthogonal change of eigenbasis.

## Assumptions and scope

The input dimension is exactly two, the regularization is the identity, the Nyström sketch has exactly one standard Gaussian column, and the independent trace probe is standard Gaussian. Both \(a\) and \(b\) are strictly positive, although repeated eigenvalues \(a=b\) are allowed. The matrix logarithm is evaluated exactly; in this dimension it is also recovered by at most two Lanczos steps in exact arithmetic. All integrability statements concern the joint law of \(\omega\) and \(w\), not just the conditional trace-estimation law. No claim concerns arbitrary sketch sizes, dimensions, non-Gaussian probes or floating-point errors.

## Proof

**1. Reduction to one scalar random logarithm.** Orthogonal invariance of two independent standard Gaussian vectors lets us set \(A=\operatorname{diag}(a,b)\). Almost surely \(\omega\ne0\), and the Nyström residual \(A-\widehat A\) is positive semidefinite of rank one (it is an orthogonal residual after conjugation by \(A^{1/2}\)). Thus
\[
M=I+P^{-1/2}(A-\widehat A)P^{-1/2}
\]
has eigenvalues \(1\) and \(\exp Z>1\), where \(Z=\log\det M\). Consequently \(\log M\) has rank one with nonzero eigenvalue \(Z\). Conditional on \(\omega\), rotational invariance of the independent \(w\) gives
\[
\widehat L-L_*=Z(\chi_1^2-1),\qquad
\mathbb E[(\widehat L-L_*)^2\mid\omega]=2Z^2,
\]
where \(\chi_1^2\) has the chi-square law with one degree of freedom. In particular the estimator is unbiased and \(\mathbb E(\widehat L-L_*)^2=2\mathbb E Z^2\). This scalar reduction is exact, not a concentration bound.

**2. Angular determinant identity.** The matrix determinant lemma gives
\[
\det P=1+\frac{a^2\omega_1^2+b^2\omega_2^2}{a\omega_1^2+b\omega_2^2}
=\frac{a(1+a)\omega_1^2+b(1+b)\omega_2^2}{a\omega_1^2+b\omega_2^2}.
\]
Writing the random direction as \((\cos\theta,\sin\theta)\) with \(\theta\) uniform modulo \(\pi\), the log residual is
\[
Z(\theta)=\log[(1+a)(1+b)]
+\log[a\cos^2\theta+b\sin^2\theta]
-\log[a(1+a)\cos^2\theta+b(1+b)\sin^2\theta].
\]

**3. Exact first and second moments.** For \(\alpha\ge\beta>0\) and \(r=(\sqrt\alpha-\sqrt\beta)/(\sqrt\alpha+\sqrt\beta)\in[0,1)\), the elementary factorization
\[
\alpha\cos^2\theta+\beta\sin^2\theta
=\left(\frac{\sqrt\alpha+\sqrt\beta}{2}\right)^2
\lvert1+r\exp(2i\theta)\rvert^2
\]
yields the uniformly convergent Fourier expansion
\[
\log[\alpha\cos^2\theta+\beta\sin^2\theta]
=2\log\frac{\sqrt\alpha+\sqrt\beta}{2}
+2\sum_{k=1}^{\infty}\frac{(-1)^{k+1}r^k}{k}\cos(2k\theta).
\]
Apply it to the two bracketed terms in \(Z\). The constants give \(\mathbb E Z=m\), while orthogonality of nonconstant cosines gives
\[
\operatorname{Var}(Z)
=2\sum_{k=1}^{\infty}\frac{(u^k-v^k)^2}{k^2}
=2[\operatorname{Li}_2(u^2)+\operatorname{Li}_2(v^2)-2\operatorname{Li}_2(uv)].
\]
Combining \(\mathbb E Z^2=m^2+\operatorname{Var}(Z)\) with Step 1 establishes the boxed exact error formula, including \(a=b\).

**4. Strict comparison with ideal preconditioning.** The Nyström approximation is rank one, positive semidefinite, and obeys \(\widehat A\preceq A\). Since \(\operatorname{tr}\widehat A\le a\), the determinant identity implies \(\det P=1+\operatorname{tr}\widehat A\le1+a\). Therefore \(\exp Z=\det(I+A)/\det P\ge1+b\). If \(a>b\), equality would require the random Nyström direction to be the top eigenvector, an event of probability zero; hence \(Z>\log(1+b)\) almost surely. Since \(Z\ge0\), its second moment is strictly larger. For \(a=b\), \(Z\equiv\log(1+b)\). This proves the comparison.

**5. Sharp square-root high-contrast expansion.** Let \(R=\omega_2/\omega_1\), a standard Cauchy variable, and set
\[
\varepsilon=\sqrt{b/a},\qquad s=\varepsilon R,\qquad
\rho=\frac{1+b}{1+a},\qquad \ell_b=\log(1+b).
\]
Then \(s\) has density \(\varepsilon/[\pi(s^2+\varepsilon^2)]\), and the determinant identity reduces exactly to
\[
Z=\ell_b+h_\rho(s),\qquad h_\rho(s)=\log(1+s^2)-\log(1+\rho s^2).
\]
For \(a\ge b\), \(0\le h_\rho(s)\le\log(1+s^2)\). Hence
\[
\frac{\mathbb E(\widehat L-L_*)^2-2\ell_b^2}{\varepsilon}
=\frac2\pi\int_{\mathbb R}
\frac{2\ell_bh_\rho(s)+h_\rho(s)^2}{s^2+\varepsilon^2}\,ds.
\]
As \(a\to\infty\) at fixed \(b>0\), \(\rho\to0\) and \(\varepsilon\to0\). The integrand is dominated by
\[
\frac{2\ell_b\log(1+s^2)+\log^2(1+s^2)}{s^2},
\]
which is integrable near the origin and at infinity. Dominated convergence applies. Integration by parts (and \(s=\tan t\)) gives
\[
\int_{\mathbb R}\frac{\log(1+s^2)}{s^2}\,ds=2\pi,
\qquad
\int_{\mathbb R}\frac{\log^2(1+s^2)}{s^2}\,ds=8\pi\log2.
\]
The limiting excess divided by \(\varepsilon\) is therefore
\[
\frac2\pi(4\pi\ell_b+8\pi\log2)=8[\ell_b+2\log2],
\]
which proves the exact leading coefficient and the stated little-oh remainder.

The eigenvalues of \(M\) are \(1\) and \(\exp Z\), so a Krylov subspace has dimension at most two. Therefore two-step Lanczos quadrature computes \(w^{\mathsf T}\log M w\) exactly in exact arithmetic (or terminates earlier at exact breakdown).

## Verification

Run `python verify.py` with the packages in `requirements.txt`. The independently written numerical checker evaluates the dilogarithm expression and angular integrals for 100 positive spectral pairs, reconstructs the preconditioner and two-step Lanczos quadratic form for 480 randomly rotated positive-definite matrices, and tests the high-contrast coefficient at four widely separated spectral scales using a Cauchy-variable integral that resolves rare events. A successful run prints `VERIFY_OK`. The analytic proof—not the finite tests—establishes the universal and asymptotic statements.

## Relationship to prior work

Cortinovis and Toni (2026), arXiv:2601.05778, introduce and analyze the single-Gaussian-probe Nyström-preconditioned log-determinant method. Their conditional Gaussian trace variance identity motivates Step 1. Their Nyström analysis gives broad bounds (in particular Theorem 2 in arXiv v2, under an oversampling assumption \(\ell\ge4\)), rather than the exact two-dimensional unconditional risk of a rank-one sketch. The present statement integrates over the random preconditioner and determines the sharp high-contrast excess over ideal preconditioning.

Saibaba, Alexanderian and Ipsen (2017) study different randomized subspace-iteration log-determinant estimators; their Theorem 7 concerns error bounds for a compressed determinant \(\log\det(I+Q^{\mathsf T}AQ)\), not the independent-probe, preconditioned estimator here. Persson and Kressner (2023) develop randomized approximations of monotone matrix functions from Nyström sketches, including \(\log(I+A)\), and general approximation bounds. Their estimator is not the same scalar preconditioned single-probe quantity. Standard chi-square moments, Fourier series and the dilogarithm are used as known identities.

## Limitations

This is a complete exact calculation for a two-dimensional benchmark, not a multivariate rate theorem. The spectral-gap asymptotic fixes the smaller eigenvalue \(b>0\); it makes no uniform assertion as \(b\) also varies. Lanczos exactness is specific to the two-eigenvalue setting and exact arithmetic. No finite-precision performance, higher-dimensional sharp constant, adaptive probe-allocation rule or application-level runtime improvement is claimed. The original paper gives general estimates; the possible presence of an equivalent angular integration in less easily indexed stochastic matrix-estimation literature remains a literature risk. An independent scientific audit has not been performed.

## References

1. A. Cortinovis and D. Toni, *Detecting when one probe vector is enough for preconditioned log-determinant approximation*, arXiv:2601.05778v1 (first posted 2026-01-09); later published in *Numerical Linear Algebra with Applications* 33 (2026), e70106, doi:10.1002/nla.70106. Open full text: https://arxiv.org/html/2601.05778v2.
2. A. K. Saibaba, A. Alexanderian, and I. C. F. Ipsen, *Randomized matrix-free trace and log-determinant estimators*, *Numerische Mathematik* 137 (2017), 353–395, doi:10.1007/s00211-017-0880-z, arXiv:1605.04893. Author-hosted full text: https://ipsen.math.ncsu.edu/ps/SaibabaAlexanderianIpsen.pdf.
3. D. Persson and D. Kressner, *Randomized low-rank approximation of monotone matrix functions*, *SIAM Journal on Matrix Analysis and Applications* 44 (2023), 894–918, arXiv:2209.11023, doi:10.1137/22M1523923.
