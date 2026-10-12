# Two boundary layers for zero-crossing and centered-energy covariance in Gaussian AR(1) samples

## Finding

Let \(X_1,\ldots,X_n\) be a zero-mean stationary Gaussian AR(1) sample of variance \(\sigma^2>0\), autoregressive correlation \(-1<\rho<1\), and integer \(n\ge2\). Define the adjacent zero-crossing count and the **mean-centered energy**
\[
 Z_n=\sum_{i=1}^{n-1}\mathbf1\{X_iX_{i+1}<0\},\qquad
 V_n=\sum_{j=1}^n(X_j-\bar X)^2,
 \quad \bar X=n^{-1}\sum_{j=1}^nX_j.
\]
The principal result is a pair of sharply separated positive-correlation sign-transition layers for \(\operatorname{Cov}(Z_n,V_n)\):

**Finite sign transition.** For every \(n\ge7\), the covariance has at least two distinct zeros in \(0<\rho<1\). It is positive at \(\rho=0\), negative at \(\rho=1/2\), and positive for \(\rho<1\) sufficiently close to one. Uniqueness of either positive-correlation zero is *not* asserted.

**Two scaling limits.** There is an explicit polynomial \(F_n\) such that \(\operatorname{Cov}(Z_n,V_n)=\sigma^2 F_n(\rho)/(\pi\sqrt{1-\rho^2})\). At any fixed \(c\ge0\),
\[
 \lim_{n\to\infty}F_n(c/n)=2(1-c).
\]
At any fixed \(c>0\),
\[
 \lim_{n\to\infty}n^2F_n(1-c/n^2)
 =\frac23c^2-\frac1{10}c^3.
\]
Consequently there exist two sequences of covariance zeros, \(\rho_n^{(0)}\) and \(\rho_n^{(1)}\), defined for all sufficiently large \(n\), with
\[
 n\rho_n^{(0)}\longrightarrow1,
 \qquad n^2(1-\rho_n^{(1)})\longrightarrow\frac{20}{3}.
\]
For any fixed \(\rho\in(0,1)\), the covariance is instead negative for all sufficiently large \(n\), since
\[
 \lim_{n\to\infty}\frac1n\operatorname{Cov}(Z_n,V_n)
 =-\frac{2\sigma^2\rho}{\pi\sqrt{1-\rho^2}}.
\]
The limiting boundary covariance itself is \(\sigma^2\,2(1-c)/\pi\) at \(\rho=c/n\); in the near-unit layer \(\rho=1-c/n^2\), it satisfies
\[
 \lim_{n\to\infty}\frac n{\sigma^2}\operatorname{Cov}(Z_n,V_n)
 =\frac{(2/3)c^2-(1/10)c^3}{\pi\sqrt{2c}}.
\]

## Assumptions and scope

Every \(X_j\) is Gaussian; the covariance matrix has entries \(\sigma^2\rho^{|j-k|}\). The sample is not conditioned on its mean, and \(V_n\) is the unnormalized centered sum of squares, not the raw energy \(\sum_jX_j^2\). Dividing \(V_n\) by \(n-1\) to obtain the unbiased sample variance rescales covariance without changing any sign or root. All finite assertions allow arbitrary \(\sigma>0\); the two existence sequences concern \(n\to\infty\). No independence is inferred from any vanishing covariance.

Put \(a_i(\rho)=(\rho^{|j-i|})_{j=1}^n\), the orthogonal projector \(P=I_n-\mathbf1\mathbf1^\top/n\), and
\[
 F_n(\rho)=\sum_{i=1}^{n-1}
 \left[\rho\big(\|Pa_i\|^2+\|Pa_{i+1}\|^2\big)
 -2\langle Pa_i,Pa_{i+1}\rangle\right].
\]
This is a finite polynomial in \(\rho\); the apparent covariance denominator is positive on \((-1,1)\).

## Proof

**1. Gaussian crossing-quadratic identity.** Let \((U,V,W)\) be centered jointly Gaussian, with \(\operatorname{Var}(U)=\operatorname{Var}(V)=1\), \(\operatorname{Cov}(U,V)=r\in(-1,1)\), and \(a=\operatorname{Cov}(W,U)\), \(b=\operatorname{Cov}(W,V)\). Gaussian integration by parts, first for smooth approximations to \(f(u,v)=\mathbf1\{uv<0\}\) and then by dominated convergence, yields
\[
 \operatorname{Cov}(f(U,V),W^2)
 =a^2\mathbb E f_{uu}(U,V)+2ab\mathbb E f_{uv}(U,V)
 +b^2\mathbb E f_{vv}(U,V).
\]
Gaussian-density evaluation of the distributional derivatives gives
\[
 \mathbb E f_{uu}=\mathbb E f_{vv}
 =\frac{r}{\pi\sqrt{1-r^2}},
 \qquad \mathbb E f_{uv}=-\frac1{\pi\sqrt{1-r^2}}.
\]
Hence
\[
 \operatorname{Cov}(f(U,V),W^2)
 =\frac{r(a^2+b^2)-2ab}{\pi\sqrt{1-r^2}}.
\]
For \(W=(PX)_j/\sigma\), its correlations with \(X_i/\sigma\) and \(X_{i+1}/\sigma\) are the \(j\)-th entries of \(Pa_i\) and \(Pa_{i+1}\), respectively. Sum the identity over \(j\) and \(i\), and restore \(\sigma^2\), to obtain the stated exact covariance formula. This ingredient is also obtainable by subtracting existing raw-energy and squared-sample-sum mixed-moment formulas; the exact identity itself is not claimed as new.

**2. Cancellation identity and finite signs.** Let \(d_i=(|j-i|)_{j=1}^n\). Completing squares gives
\[
 F_n(\rho)=\sum_{i=1}^{n-1}\|P(a_i-a_{i+1})\|^2
 -(1-\rho)\sum_{i=1}^{n-1}
   (\|Pa_i\|^2+\|Pa_{i+1}\|^2).
\]
At \(\rho=0\), \(F_n(0)=2(n-1)/n>0\). For fixed \(n\), write \(\rho=1-\varepsilon\). The expansions \(Pa_i=-\varepsilon Pd_i+O_n(\varepsilon^2)\) and \(P(a_i-a_{i+1})=-\varepsilon P(d_i-d_{i+1})+O_n(\varepsilon^2)\) give
\[
 F_n(1-\varepsilon)=\frac23(n^2-1)\varepsilon^2
 +O_n(\varepsilon^3)>0
\]
for sufficiently small positive \(\varepsilon\). Here \(\|P(d_i-d_{i+1})\|^2=4i(n-i)/n\), and summing this equality gives \(2(n^2-1)/3\).

To prove the negative intermediate sign without numerical extrapolation, define \(b_i=\sum_{j=1}^n\rho^{|j-i|}\). Expanding the projector yields
\[
 F_n(\rho)=T_n(\rho)-\frac{U_n(\rho)}n,
\]
where
\[
 T_n(\rho)=-2\rho(1-\rho^2)
 \sum_{k=0}^{n-2}(n-1-k)\rho^{2k},
\]
\[
 U_n(\rho)=\sum_{i=1}^{n-1}
 [\rho(b_i^2+b_{i+1}^2)-2b_ib_{i+1}].
\]
At \(\rho=1/2\), \(T_n=-n+4/3-4^{-(n-1)}/3\). Since \(0<b_i<3\),
\[
 U_n(1/2)=\sum_{i=1}^{n-1}
 \left[\frac12(b_i-b_{i+1})^2-b_ib_{i+1}\right]>-9(n-1).
\]
It follows that \(F_n(1/2)<-n+4/3+9(n-1)/n<0\) for all \(n\ge10\). The three remaining orders satisfy exactly
\[
 F_7(1/2)=-\frac{4311}{14336},\quad
 F_8(1/2)=-\frac{115161}{131072},\quad
 F_9(1/2)=-\frac{75563}{49152}.
\]
Thus, continuity furnishes one zero between \(0\) and \(1/2\) and another between \(1/2\) and \(1\) for every \(n\ge7\).

**3. Small-correlation layer and fixed-correlation bulk.** For fixed \(c\ge0\), set \(\rho=c/n\). In the preceding decomposition, \(T_n\to-2c\), while \(b_i=1+O(n^{-1})\) uniformly and therefore \(U_n/n\to-2\). This proves \(F_n(c/n)\to2(1-c)\). For fixed \(0<\rho<1\), the geometric sum gives \(T_n/n\to-2\rho\) and the uniform bound on \(b_i\) gives \(U_n/n^2\to0\). This yields the bulk limit.

**4. Near-unit-correlation layer.** Put \(\varepsilon=c/n^2\). The difference between neighboring columns has the exact coordinatewise form \(\pm\varepsilon(1-\varepsilon)^k\) for some \(0\le k\le n\), so uniformly
\[
 P(a_i-a_{i+1})=-\varepsilon P(d_i-d_{i+1})
 +O(\varepsilon^2 n)
\]
coordinatewise. Likewise \(Pa_i=-\varepsilon Pd_i+O(\varepsilon^2 n^2)\) coordinatewise. These bounds are uniform in \(i,j\) for fixed \(c\), and substituting into the cancellation identity produces
\[
 F_n(1-\varepsilon)=\varepsilon^2Q_n-\varepsilon^3S_n+o(n^{-2}),
\]
where
\[
 Q_n=\sum_{i=1}^{n-1}\|P(d_i-d_{i+1})\|^2
 =\frac23(n^2-1),
\]
\[
 S_n=\sum_{i=1}^{n-1}
 (\|Pd_i\|^2+\|Pd_{i+1}\|^2)
 =\frac{(n^2-1)(3n^2-5n+8)}{30}.
\]
For the last equality, use \(\|Pd_i\|^2=\sum_j|j-i|^2-n^{-1}(\sum_j|j-i|)^2\) and the ordinary sums of integers and squares. Thus \(n^{-2}Q_n\to2/3\) and \(n^{-4}S_n\to1/10\), proving \(n^2F_n(1-c/n^2)\to (2/3)c^2-(1/10)c^3\). Since \(1-\rho^2\sim2c/n^2\), the covariance scaling follows.

**5. Sharp location existence.** The first limiting polynomial is positive at any fixed \(c<1\) and negative at any fixed \(c>1\). The second is positive at any fixed \(0<c<20/3\) and negative for \(c>20/3\). Continuity yields roots between the corresponding scaled parameters for all sufficiently large \(n\). Shrinking those brackets along a diagonal sequence establishes roots with limits \(n\rho_n^{(0)}\to1\) and \(n^2(1-\rho_n^{(1)})\to20/3\), without requiring uniqueness. The two roots are distinct because one tends to zero and the other tends to one.

## Verification

Run `python3 verification.py` using the accompanying standalone file. It checks 65 independent exact-rational evaluations of the projected-vector formula against its raw-energy/squared-sum expansion, three exact negative cases at \(\rho=1/2\), 23 exact identities for the near-unit coefficients, and diagnostic convergence at both scales. A separate seeded numerical Gaussian-sample experiment was used as a nonproof plausibility check; no Monte Carlo conclusion is used in any deduction. The elementary uniform Taylor bounds, not finite checking, justify all asymptotic limits.

## Relationship to prior work

Lindgren (1974) compares crossing-based spectral estimators with continuous-time squared-derivative estimators; these are not the discrete mean-centered squared amplitudes or two AR(1) boundary layers considered here. Sinn and Keller (2010/2011) study covariances between crossing indicators and crossing-rate variances, not mixed crossing/centered-energy moments. Classical Gaussian integration by parts/Price's theorem provides the mixed-moment calculation and is not claimed as new. Existing exact AR(1) crossing covariances with *raw energy* and with the *squared sample sum* algebraically imply the finite projected-vector covariance identity here; accordingly, **the novel claim is restricted to the finite two-root sign theorem and two distinct sharp asymptotic boundary layers**, not the exact finite covariance itself. An exact expression for a moment does not by itself identify the nonuniform limits and their contrasting signs; the cancellation and geometric-moment estimates above supply those additional conclusions.

## Limitations

The theorem establishes at least two positive-correlation covariance zeros for each \(n\ge7\), without proving they are the only ones or that any root is simple. Only fixed \(c\) scaling limits are established; no uniform global approximation over every \(\rho\), no distributional independence, no nonlinear predictability theorem, and no general non-Gaussian extension is asserted. Historical priority is provisional: the complete Lindgren (1974) paper was inaccessible and some broad classical Gaussian moment formulas can implicitly encode these calculations. The exact earlier raw-energy/squared-sum identities fully cover the finite mixed covariance and are specifically excluded from novelty.

## References

1. G. Lindgren, “Spectral moment estimation by means of level crossings,” *Biometrika* 61(2) (1974), 401–418; https://doi.org/10.1093/biomet/61.2.401 (abstract examined; full text inaccessible).
2. M. Sinn and K. Keller, “Covariances of zero crossings in Gaussian processes,” *Theory of Probability and Its Applications* 55(3) (2011), 485–504; Russian original 2010; https://doi.org/10.4213/tvp4241.
3. I. G. Vladimirov, “A quantum mechanical version of Price's theorem for Gaussian states,” arXiv:1409.4377 (2014), Section II on classical Gaussian Price identities; https://arxiv.org/abs/1409.4377.
4. E. Di Bernardino, J. León, and T. Tchumatchenko, “Cross-Correlations and Joint Gaussianity in Multivariate Level Crossing Models,” *Journal of Mathematical Neuroscience* 4 (2014), 22; https://doi.org/10.1186/2190-8567-4-22.
