# Spectral moment recovery and pathwise separation for two-mode Wigner Gaussian fields

## Statement

Consider the complex Hermitian \((a,b)\)-Wigner ensemble of Raposo, with independent diagonal and off-diagonal families,
\[
\mathbb E X_{11}=0,\qquad \mathbb E X_{11}^2=a,
\]
and, for \(i<j\),
\[
\mathbb E X_{ij}=0,\qquad \mathbb E X_{ij}^2=0,\qquad
\mathbb E|X_{ij}|^2=1,\qquad \mathbb E|X_{ij}|^4=b,
\]
with all moments finite. Let \(M_k\) be the \(k\times k\) upper-left corner, and suppose only the nested corner spectra are observed.

The two Wigner moment parameters are recoverable from the first two spectral power sums by explicit unbiased estimators. Moreover, in the Gaussian-field limit of Raposo, the same parameters are pathwise recoverable from dyadic quadratic variations of the first two angular modes. Consequently, distinct parameter pairs give mutually singular laws both for the infinite nested-corner spectral experiment and for the limiting generalized Gaussian field.

The finite-corner estimator for \(b\) has an exact variance formula whose leading term depends only on \(b\), not on higher off-diagonal moments.

## 1. Exact recovery from nested corner spectra

Write
\[
S_{1,k}=\operatorname{tr}M_k,\qquad
S_{2,k}=\operatorname{tr}(M_k^2),
\]
with \(S_{1,0}=S_{2,0}=0\), and define
\[
D_k=S_{1,k}-S_{1,k-1}.
\]
Then, identically for every realization,
\[
\boxed{D_k=X_{kk}.}
\]

For \(k\ge2\), define
\[
T_k=\frac12\left(S_{2,k}-S_{2,k-1}-D_k^2\right).
\]
Since
\[
\operatorname{tr}(M_k^2)
=\sum_{i=1}^k X_{ii}^2+2\sum_{1\le i<j\le k}|X_{ij}|^2,
\]
we have the second exact identity
\[
\boxed{T_k=\sum_{i<k}|X_{ik}|^2.}
\]

Thus the nested spectra deterministically reveal every diagonal entry and every newly added off-diagonal column energy, without observing eigenvectors.

Let
\[
Y=|X_{12}|^2,\qquad v=\operatorname{Var}(Y)=b-1,
\]
and
\[
Z_k=\frac{T_k-(k-1)}{\sqrt{k-1}},\qquad k\ge2.
\]
The random variables \(Z_2,Z_3,\ldots\) are independent, because they use disjoint sets of off-diagonal entries, and
\[
\mathbb EZ_k=0,\qquad \mathbb EZ_k^2=v.
\]

Define
\[
\boxed{\widehat a_n=\frac1n\sum_{k=1}^nD_k^2},
\qquad
\boxed{\widehat b_n=1+\frac1{n-1}\sum_{k=2}^nZ_k^2}.
\]
Then
\[
\mathbb E\widehat a_n=a,\qquad
\mathbb E\widehat b_n=b,
\]
and \(\widehat a_n\) and \(\widehat b_n\) are independent for every \(n\).

Let
\[
\tau_a^2=\operatorname{Var}(X_{11}^2)
=\mathbb E X_{11}^4-a^2,
\]
and
\[
\mu_4=\mathbb E(Y-1)^4.
\]
The diagonal estimator has
\[
\operatorname{Var}(\widehat a_n)=\frac{\tau_a^2}{n}.
\]

For the off-diagonal estimator, if \(m=k-1\), the standard fourth-moment identity for a sum of \(m\) centered independent variables gives
\[
\mathbb EZ_k^4
=
3v^2+\frac{\mu_4-3v^2}{k-1}.
\]
Hence
\[
\operatorname{Var}(Z_k^2)
=
2v^2+\frac{\mu_4-3v^2}{k-1},
\]
and therefore the exact finite-\(n\) variance is
\[
\boxed{
\operatorname{Var}(\widehat b_n)
=
\frac{2(b-1)^2}{n-1}
+
\frac{\bigl(\mu_4-3(b-1)^2\bigr)H_{n-1}}{(n-1)^2},
}
\]
where \(H_m=\sum_{j=1}^m j^{-1}\).

In particular,
\[
n\,\operatorname{Var}(\widehat b_n)\longrightarrow 2(b-1)^2.
\]
All dependence on moments of \(Y\) beyond \(b\) is confined to the lower-order harmonic correction.

### Strong consistency and joint CLT

Under the natural infinite-array coupling,
\[
\boxed{\widehat a_n\to a,\qquad \widehat b_n\to b\quad\text{almost surely}.}
\]
The first assertion is the ordinary strong law. For the second, the centered independent variables
\[
W_k=Z_k^2-v
\]
have uniformly bounded variance, so
\[
\sum_{k=2}^{\infty}\frac{\operatorname{Var}(W_k)}{k^2}<\infty,
\]
and Kolmogorov's strong law applies.

If \(b>1\), then, using the all-moments assumption to verify Lyapunov's condition,
\[
\boxed{
\sqrt n
\begin{pmatrix}
\widehat a_n-a\\
\widehat b_n-b
\end{pmatrix}
\Longrightarrow
N\!\left(
0,
\begin{pmatrix}
\tau_a^2&0\\
0&2(b-1)^2
\end{pmatrix}
\right).
}
\]
If \(b=1\), then \(Y=1\) almost surely and \(\widehat b_n\equiv1\).

A direct consequence is a parameter-separation statement for the infinite corner process: any two infinite Wigner ensembles satisfying the assumptions but having different pairs \((a,b)\) induce mutually singular laws on the sequence of nested corner spectra. The event on which the two displayed spectral estimators converge to a prescribed pair has probability one under that pair and zero under any different pair. This conclusion allows arbitrary nuisance differences in the entry laws beyond the stated moments.

## 2. Pathwise recovery from the limiting Gaussian field

Raposo's limiting generalized Gaussian field \(\mathfrak C_{a,b}\) has its first angular mode scaled by \(\sqrt a\) and its second angular mode scaled by \(\sqrt{b-1}\). In the circle-integrated sense used to define those modes, put
\[
L_1(t)=\int_0^\pi
\mathfrak C_{a,b}(\sqrt t\,e^{i\theta})\sin\theta\,d\theta
\]
and
\[
L_2(t)=\int_0^\pi
\mathfrak C_{a,b}(\sqrt t\,e^{i\theta})\sin(2\theta)\,d\theta.
\]
Using the mode normalization in Raposo's Theorem 1.6 and
\(\int_0^\pi\sin^2(j\theta)\,d\theta=\pi/2\),
\[
L_1(t)
=
-\frac{\sqrt{\pi a}}{2\sqrt t}\,B_1(t),
\]
and
\[
L_2(t)
=
-\frac{\sqrt{\pi(b-1)}}{2\sqrt2\,t}\,B_2(t^2),
\]
for independent standard Brownian motions \(B_1,B_2\).

Define
\[
U_1(t)=-\frac{2\sqrt t}{\sqrt\pi}L_1(t)
=\sqrt a\,B_1(t),
\]
and, with \(s=t^2\),
\[
U_2(s)=-\sqrt{\frac{8s}{\pi}}L_2(\sqrt s)
=\sqrt{b-1}\,B_2(s).
\]

On any fixed interval, for example \([1,2]\), their dyadic quadratic variations satisfy almost surely
\[
\boxed{
\lim_{m\to\infty}
\sum_{j=1}^{2^m}
\left(
U_1\!\left(1+\frac{j}{2^m}\right)
-
U_1\!\left(1+\frac{j-1}{2^m}\right)
\right)^2
=a,
}
\]
and
\[
\boxed{
\lim_{m\to\infty}
\sum_{j=1}^{2^m}
\left(
U_2\!\left(1+\frac{j}{2^m}\right)
-
U_2\!\left(1+\frac{j-1}{2^m}\right)
\right)^2
=b-1.
}
\]

Thus \((a,b)\) is a measurable pathwise functional of the first two radial mode processes. In particular,
\[
\boxed{
(a,b)\ne(a',b')
\quad\Longrightarrow\quad
\mathcal L(\mathfrak C_{a,b})
\perp
\mathcal L(\mathfrak C_{a',b'}).
}
\]
The separating event is explicit: it is the event that the two dyadic quadratic variations equal \(a\) and \(b-1\). Boundary cases \(a=0\) or \(b=1\) are included, with the corresponding mode identically zero.

This source-specific construction is consistent with the classical Feldman--Hájek dichotomy for infinite-dimensional Gaussian measures; the generic dichotomy itself is not a novelty claim here.

## 3. Finite radial resolution

The singularity only appears after radial resolution tends to infinity. For \(m\) equal subintervals of \([1,2]\), normalize the increments of a Brownian mode by the square root of the subinterval length. Under variance parameters \(v,v'>0\), the resulting \(m\)-vectors have laws
\[
P_v^{(m)}=N(0,vI_m),\qquad
P_{v'}^{(m)}=N(0,v'I_m).
\]
Their Hellinger affinity is exactly
\[
\boxed{
\mathcal A(P_v^{(m)},P_{v'}^{(m)})
=
\left(
\frac{2\sqrt{vv'}}{v+v'}
\right)^{m/2},
}
\]
and
\[
\boxed{
D_{\mathrm{KL}}(P_v^{(m)}\|P_{v'}^{(m)})
=
\frac m2
\left(
\frac v{v'}-1-\log\frac v{v'}
\right).
}
\]
The first and second modes are independent, so affinities multiply and KL divergences add across the two parameters. If one variance is zero and the other is positive, the corresponding finite-dimensional laws are already singular.

The quadratic-variation estimator on this grid has the exact chi-square law
\[
\boxed{
\frac{m\widetilde v_m}{v}\sim\chi_m^2,
}
\]
where \(\widetilde v_m\) is the sum of squared increments over \([1,2]\). Hence
\[
\operatorname{Var}(\widetilde v_m)=\frac{2v^2}{m}.
\]
For the second mode, this is the same leading variance \(2(b-1)^2/m\) found above for the corner-spectral estimator.

## 4. Relation to prior work and originality boundary

Borodin established Gaussian fluctuation limits for spectra of Wigner submatrices and identified the Gaussian-free-field structure in the standard fourth-moment case. Raposo's 2026 preprint makes the dependence on the diagonal second moment \(a\) and off-diagonal fourth moment \(b\) explicit and identifies these parameters with the first two Fourier modes of the limiting field.

The algebraic trace identities used here are elementary, and the singularity of differently scaled infinite-dimensional Gaussian processes is consistent with classical Gaussian-measure theory. Neither fact is claimed as new in isolation.

The contribution claimed here, to the best of our knowledge, is the combined source-specific inference statement:

1. explicit **spectra-only**, finite-\(n\), unbiased recovery of \(a\) and \(b\) from nested corners;
2. the exact variance formula for \(\widehat b_n\), including its higher-moment harmonic correction and the universal leading variance \(2(b-1)^2/n\);
3. strong recovery and the resulting mutual singularity of infinite nested-corner spectral laws across parameter pairs, even with arbitrary nuisance entry laws satisfying the assumptions;
4. an explicit quadratic-variation separator for Raposo's two-parameter limiting fields, together with finite-grid Hellinger and KL separation formulas.

Targeted literature checks for equivalent Wigner-corner moment estimators and for a parameter-identifiability statement for this new two-mode field did not locate these formulations. A residual originality risk is that the finite-corner estimator may be implicit in older work on low-degree trace statistics or principal-minor processes, while the field singularity is a direct specialization of classical Gaussian-measure principles.

## Limitations

The finite-matrix statements are written for the complex Hermitian normalization in Raposo's Definition 1.1. Analogous real-symmetric and quaternionic formulas require the corresponding moment normalization.

The estimator \(\widehat b_n\) is not claimed to be minimax or efficient for the full nested-spectrum experiment; it is an explicit low-degree spectral construction. Its central limit theorem uses the all-moments assumption of the source model, although substantially weaker moment assumptions would suffice.

The field-law singularity uses arbitrarily fine radial observation of the first or second angular mode. For every fixed finite grid and strictly positive mode variances, the Gaussian laws are mutually absolutely continuous.

The circle integrals are interpreted as the generalized-field mode variables in the sense used by Raposo; no pointwise realization of the two-dimensional generalized field is assumed.

## References

- Gabriel Raposo, *Interpolation of Gaussian Free Fields via Random Matrices*, arXiv:2609.20707 (2026).
- Alexei Borodin, *CLT for spectra of submatrices of Wigner random matrices*, arXiv:1010.0898; Moscow Mathematical Journal 14 (2014), 29--38.
- Classical Feldman--Hájek equivalence/singularity theory for Gaussian measures; see, for example, V. I. Bogachev, *Gaussian Measures*, Theorem 2.7.2.
