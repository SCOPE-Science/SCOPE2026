# A single-sky identifiability dichotomy for gamma-clock and global-clock grey spherical fields

## Finding

Two strongly isotropic, non-Gaussian spherical-field constructions can have **exactly the same covariance function** while exhibiting opposite high-resolution statistical behavior. With independent identically distributed gamma subordinators evaluated at one shared positive random time, the deterministic covariance-amplitude parameter and the realized common clock are both recoverable almost surely from one full-sky realization; an explicit conditional joint central limit theorem holds. With one global random variance instead, different positive amplitudes yield mutually absolutely continuous laws even for the entire infinite array of spherical harmonics: no sequence of tests or estimators can consistently discriminate every pair of amplitudes. These conclusions hold under the exact assumptions below.

## Assumptions and scope

Use a real orthonormal spherical-harmonic basis. Let \(C_\ell>0\) be known for every integer \(\ell\geq1\), with
\[
\sum_{\ell=1}^{\infty}(2\ell+1)C_\ell<\infty.
\]
Set the degree-zero coefficient to zero. Fix *known* constants \(a,b>0\). The deterministic amplitude \(\theta>0\) is unknown. Let \(T>0\) be independent of everything below, with \(\mathbb E T<\infty\) and a density positive almost everywhere on \((0,\infty)\). The inverse-stable/Mittag-Leffler clock \(T_\beta\) with \(0<\beta<1\) is a motivating example. Its distribution need not be used by the proposed estimators.

For each \(\ell\geq1\), let \(Z_{\ell m}\), \(-\ell\leq m\leq\ell\), be independent standard real Gaussian variables; Gaussian arrays at distinct degrees are independent. Put \(d_\ell=2\ell+1\). Define two *different* models:

**Gamma-clock field \(\mathsf G_\theta\).** Independently across degrees, let \(H_\ell\) be gamma subordinators with Laplace exponent \(a\log(1+s/b)\), independent of \(T\) and the Gaussians. Hence conditional on \(T=t\), the multipole variances \(H_\ell(T)\) are independent \(\operatorname{Gamma}(at,\mathrm{rate}\ b)\) variables. Set
\[
A^{\mathsf G}_{\ell m}=\sqrt{\theta C_\ell H_\ell(T)}\,Z_{\ell m}.
\]

**Global-clock field \(\mathsf D_\theta\).** Use the deterministic subordinator \(H_\ell(t)=at/b\) for *every* degree, giving
\[
A^{\mathsf D}_{\ell m}=\sqrt{\theta C_\ell(aT/b)}\,Z_{\ell m}.
\]

Both are well-defined centered square-integrable real spherical random fields, invariant under rotations. The positive multipole-energy observables, for either field, are
\[
S_\ell=\frac{1}{d_\ell C_\ell}\sum_{m=-\ell}^{\ell}A_{\ell m}^{2},\qquad
M_{r,L}=\frac1L\sum_{\ell=1}^{L}S_\ell^{r}\quad(r=1,2).
\]
The entire observation at resolution \(L\) means *all* harmonic coefficients through degree \(L\), not a single coefficient or one point of the field.

**Theorem.** The ensemble covariance functions of \(\mathsf G_\theta\) and \(\mathsf D_\theta\) coincide, with harmonic covariance
\[
\mathbb E[A_{\ell m}A_{\ell'm'}]=
\mathbf 1_{\{\ell=\ell',m=m'\}}\,\theta C_\ell\frac ab\,\mathbb ET.
\]
For \(L\geq2\), put \(D_L=M_{2,L}-M_{1,L}^{2}\). On \(D_L>0\), define
\[
\widehat T_L=\frac{M_{1,L}^{2}}{aD_L},\qquad
\widehat\theta_L=\frac{bD_L}{M_{1,L}}.
\]
Define these estimators arbitrarily on \(D_L=0\), which is a null event in the gamma-clock model for \(L\geq2\). Then, in \(\mathsf G_\theta\),
\[
(\widehat T_L,\widehat\theta_L)\longrightarrow(T,\theta)\quad\text{almost surely}.
\]
Moreover, conditional on \(T=t>0\), with \(k=at\),
\[
\sqrt L\begin{pmatrix}\widehat T_L-t\\\widehat\theta_L-\theta\end{pmatrix}
\ \xrightarrow{\ d\ }\
\mathcal N_2\left(0,\begin{pmatrix}
\frac{2k(k+1)}{a^2}&-\frac{2\theta(k+1)}a\\
-\frac{2\theta(k+1)}a&\frac{\theta^2(2k+3)}k
\end{pmatrix}\right).
\]
The unconditional limit is the corresponding centered Gaussian covariance mixture over \(T\), not generally a single Gaussian law.

In \(\mathsf D_\theta\), \(M_{1,L}\to\theta(aT/b)\) and \(D_L\to0\) almost surely. The infinite observation is statistically equivalent to observing just \(W=\theta(aT/b)\): it is simulable from \(W\) by a kernel independent of \(\theta\), while \(W\) itself is measurable from the infinite observation. Consequently, for every \(\theta_0\ne\theta_1\), the two infinite-observation laws of \(\mathsf D_{\theta_0}\) and \(\mathsf D_{\theta_1}\) are mutually absolutely continuous, whereas those of \(\mathsf G_{\theta_0}\) and \(\mathsf G_{\theta_1}\) are mutually singular. In particular, in the global-clock model no estimator based on growing multipole resolutions can converge in probability to the true amplitude at both distinct parameter values.

The two field families themselves can be consistently discriminated from one complete realization using the statistic \(D_L\): report gamma-clock exactly when \(D_L>L^{-1/4}\), for example. This test has vanishing error probabilities for every fixed admissible parameter and almost every realized clock.

## Proof

**Harmonic representation and moments.** Rotation by any element of \(SO(3)\) transforms a real degree-\(\ell\) harmonic coefficient vector by an orthogonal matrix. Conditional on the scalar variance at that degree, the vector is isotropic Gaussian, proving rotational invariance of the joint field. The trace condition and \(\mathbb ET<\infty\) ensure square-integrability. The conditional mean of each gamma subordinator value and the deterministic subordinator value are both \(at/b\). Different coefficients have zero covariance because the underlying normals are centered and independent. This proves the asserted common covariance.

Write \(R_\ell=d_\ell^{-1}\sum_mZ_{\ell m}^{2}\), so that \(d_\ell R_\ell\sim\chi^2_{d_\ell}\), independently across degrees and of the subordinators. In the gamma-clock model, conditional on \(T=t\), write \(G_\ell=H_\ell(t)\) and \(\eta=\theta/b\). Then
\[
S_\ell=\theta G_\ell R_\ell,\quad
\mathbb E(G_\ell^r\mid T=t)=\frac{(k)_r}{b^r},\quad
\mathbb ER_\ell^r=\prod_{j=0}^{r-1}\left(1+\frac{2j}{d_\ell}\right),\quad k=at.
\]
In particular, \(\mathbb ER_\ell=1\), \(\mathbb ER_\ell^2=1+2/d_\ell\), and its first four moments are uniformly bounded. Conditional on \(t\), the sequence \((S_\ell)_\ell\) is independent, but not identically distributed. For \(r=1,2\), its \(r\)-th powers have uniformly bounded conditional variances, so Kolmogorov's strong law for independent variables applies (the sum of the variances divided by squared indices is finite). Consequently,
\[
M_{1,L}\to\eta k,\qquad
M_{2,L}\to\eta^2k(k+1),\qquad
D_L\to\eta^2k>0
\]
almost surely conditional on every \(t>0\); for the second limit, the deterministic mean correction \(2\eta^2k(k+1)L^{-1}\sum_{\ell\leq L}d_\ell^{-1}\) tends to zero. Conditioning and integrating prove the unconditional almost-sure assertions. Taking the rational inverse of the two limiting moments gives the displayed consistent estimators.

**Conditional central limit theorem and its covariance.** Compare \(S_\ell\) with \(X_\ell=\theta G_\ell\), conditionally iid \(\operatorname{Gamma}(k,\mathrm{scale}\ \eta)\). The centered terms \(S_\ell-X_\ell=X_\ell(R_\ell-1)\) have conditional variance \(2\mathbb E(X_\ell^2\mid t)/d_\ell\). Likewise,
\[
S_\ell^2-X_\ell^2=X_\ell^2(R_\ell^2-1),\qquad
\mathbb E(R_\ell^2-1)=\frac2{d_\ell},\qquad
\mathbb E(R_\ell^2-1)^2=\frac8{d_\ell}+\frac{44}{d_\ell^2}+\frac{48}{d_\ell^3}.
\]
Thus, after summing over degrees, the conditional squared-mean errors have variance \(O_t(\log L)\), and the second-moment error has expectation \(O_t(\log L)\); division by \(\sqrt L\) makes both negligible in conditional probability. The ordinary bivariate iid central limit theorem for \((X_\ell,X_\ell^2)\) therefore applies to \((M_{1,L},M_{2,L})\). Its covariance is
\[
V=\begin{pmatrix}
 k\eta^2&2k(k+1)\eta^3\\
 2k(k+1)\eta^3&2k(k+1)(2k+3)\eta^4
\end{pmatrix}.
\]
For \(h(x,y)=(x^2/(y-x^2),(y-x^2)/x)\), the Jacobian at \((\eta k,\eta^2k(k+1))\) is
\[
J=\begin{pmatrix}
 2(k+1)/\eta&-1/\eta^2\\
 -(2k+1)/k&1/(k\eta)
\end{pmatrix}.
\]
The delta method gives \(JVJ^\mathsf T=\left(\begin{smallmatrix}2k(k+1)&-2\eta(k+1)\\-2\eta(k+1)&\eta^2(2k+3)/k\end{smallmatrix}\right)\). Transforming the first coordinate by \(1/a\) and the second by \(b\) proves the claimed conditional covariance. The determinant is \(2\theta^2(k+1)/a^2>0\). Conditional characteristic-function convergence for each fixed \(t\), followed by dominated convergence over \(T\), gives the corresponding unconditional covariance-mixture limit.

**Global-clock information obstruction.** Here \(S_\ell=W R_\ell\), where \(W=\theta(aT/b)>0\). The independent \(R_\ell\) satisfy \(R_\ell\to1\) almost surely by chi-square concentration (indeed exponentially summable concentration tails). Therefore \(S_\ell\to W\) almost surely, proving recovery of \(W\) from the infinite coefficient array. Conversely, conditional on \(W=w\), all coefficients are independent centered Gaussian with covariance \(wC_\ell\) within their degrees. Thus the entire array is sampled by a probability kernel \(K_w\) not depending on \(\theta\), establishing the experiment equivalence.

Because \(T\) has a density positive almost everywhere on \((0,\infty)\), so does \(W\) for any \(\theta>0\); any two such mixing laws are mutually absolutely continuous and have total-variation distance strictly less than one. Applying the same kernel preserves equivalence and bounds the total variation of every finite-resolution observation. No tests between two distinct amplitudes can have both error probabilities tend to zero; such tests would follow from any estimator consistent at both amplitudes. In the gamma-clock model, the events \(\{\lim_{L\to\infty}\widehat\theta_L=\theta_i\}\) separate the laws for distinct \(\theta_i\), giving mutual singularity.

**Discriminating the constructions.** Under the global clock, the strong law gives \(M_{1,L}\to W\) and \(M_{2,L}\to W^2\), hence \(D_L\to0\). More quantitatively, conditional on \(W=w\),
\[
0\leq\mathbb E(D_L\mid W=w)
\leq\frac1L\sum_{\ell=1}^{L}\operatorname{Var}(wR_\ell)
=\frac{2w^2}{L}\sum_{\ell=1}^{L}\frac1{d_\ell}
=O_w\left(\frac{\log L}{L}\right).
\]
Markov's inequality then bounds the probability of \(D_L>L^{-1/4}\) by \(O_w((\log L)L^{-3/4})\); integrate the conditional probabilities. In the gamma-clock model, \(D_L\to\eta^2k>0\) almost surely, hence the proposed classifier succeeds with probability tending to one. This proves the final assertion.

## Verification

An accompanying standalone Python script checks the exact gamma and normalized chi-square moment identities, the finite-degree energy bias, the gamma moment covariance, and the delta-method matrix by rational arithmetic at numerous positive rational parameter values. Its currently verified output is `CHECK_OK: 780 exact rational moment, degeneracy and covariance identities`. These finite checks do not replace the strong laws, asymptotic central limit theorem, or measure-equivalence argument above. To reproduce: `python3 checker.py` with Python 3 and no third-party packages.

## Relationship to prior work

Beghin, Leonenko and Marinucci (2026, arXiv:2610.11806, §§3–4, Appendix A) introduce grey spherical fields with common random times, independent gamma subordinators, and global random-variance counterparts, derive coefficient moments, and prove marginal high-frequency mixture limits. Their results supply the model and the gamma identities used here; the *single-realization joint recovery, conditional estimator covariance and singularity-versus-equivalence comparison* are different inferential statements, not claims of novelty for the distributions themselves.

Marinucci and Peccati (2009, arXiv:0911.2502, §§1–2) study high-frequency ergodicity of **individual** angular-power-spectrum estimates, especially for Gaussian subordinated fields. Their normalized single-multipole limits neither recover a latent gamma-clock shape from many degrees nor prove the global-clock equivalence obstruction. Papadatos (2022, arXiv:2205.10799, §2) studies estimators for ordinary iid gamma samples; gamma method-of-moments algebra is classical and is *not claimed as new*. Unlike an iid gamma sample, the observable multipole energies are gamma times degree-dependent chi-square noise, and the shared random time and global-clock comparison are essential to the statement. The present proof uses these standard statistical tools explicitly.

## Limitations

The spectral shape \((C_\ell)\) and gamma subordinator parameters \(a,b\) must be known, every \(C_\ell\) must be positive, and increasingly many complete harmonic degrees must be observable without measurement noise. The result does not apply unchanged to a fixed finite resolution, unknown frequency-varying spectra, correlated subordinator increments, or a deterministic clock: the positive-density hypothesis is crucial for the global-model indistinguishability. The central limit theorem is conditional on the latent time and its covariance is not uniform as that time approaches zero. It does not claim efficiency or optimal finite-sample risk. Inverse-stable clock laws with \(0<\beta<1\) satisfy the stated assumptions, but estimation of \(\beta\) itself is not treated. The positive-density global-clock obstruction is an exact identifiability statement, not a claim that the amplitude's distribution is wholly uninformative.

## References

1. L. Beghin, N. Leonenko, D. Marinucci, *Grey Random Fields on the Sphere*, arXiv:2610.11806v1 (first publicly posted 2026-10-08). https://arxiv.org/html/2610.11806v1
2. D. Marinucci, G. Peccati, *Ergodicity and Gaussianity for Spherical Random Fields*, arXiv:0911.2502 (2009). https://arxiv.org/abs/0911.2502
3. N. Papadatos, *On point estimators for Gamma and Beta distributions*, arXiv:2205.10799 (2022). https://arxiv.org/html/2205.10799v1
4. Standard tools used: Kolmogorov's strong law for independent nonidentically distributed sequences, the iid multivariate central limit theorem, the delta method, and data processing for total variation.
