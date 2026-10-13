# Exact one-versus-rest risk crossover for selected exponential locations
## Finding
Let \(k\ge2\) independent populations have density
\[
f_i(x)=\sigma^{-1}e^{-(x-\mu_i)/\sigma}\mathbf 1_{\{x\ge\mu_i\}},
\]
with common unknown \(\sigma>0\), and take \(n\ge2\) observations from each. Write \(M_i=\min_jX_{ij}\),
\[
S=\sum_{i=1}^k\sum_{j=1}^n(X_{ij}-M_i),\qquad Z=\max_iM_i,
\]
and select \(J\) by \(M_J=Z\). Under scaled squared-error loss \(((d-\mu_J)/\sigma)^2\), consider
\[
\delta_U=Z-\frac{S}{nk(n-1)},\qquad
\delta_B=Z-\frac{S}{n\{k(n-1)+1\}}.
\]
The first correction makes each component estimator \(M_i-cS\) unbiased before selection; the second minimizes its componentwise scaled mean squared error over constant \(c\).

On
\[
\mu_1=\cdots=\mu_{k-1}=\theta,\qquad
\mu_k=\theta+\frac{t\sigma}{n},\qquad t\ge0,
\]
put \(K=k(n-1)\) and
\[
H_{k-1}(t)=\sum_{j=1}^{k-1}(-1)^{j+1}\binom{k-1}{j}\frac{(jt+1)e^{-jt}}{j(j+1)}.
\]
Then
\[
R_t(\delta_U)-R_t(\delta_B)=\frac{1-2KH_{k-1}(t)}{n^2K(K+1)}.
\]
There is exactly one \(t_{k,n}>0\) with
\[
H_{k-1}(t_{k,n})=\frac1{2k(n-1)}.
\]
The estimator \(\delta_U\) has smaller risk below this threshold, and \(\delta_B\) has smaller risk above it.

For \(k=3\),
\[
H_2(t)=(t+1)e^{-t}-\frac{(2t+1)e^{-2t}}6,
\]
and
\[
t_{3,3}=4.111450606420\ldots,\quad
t_{3,5}=4.961181135319\ldots,\quad
t_{3,10}=5.923005815333\ldots,\quad
t_{3,15}=6.436753036096\ldots.
\]

## Assumptions and scope
All populations have equal sample size and a common unknown scale. The parameter geometry is the canonical one-best versus \(k-1\) tied-rest ray. The result does not classify arbitrary unequal location vectors. The notation \(\delta_U\) and \(\delta_B\) denotes natural componentwise analogues; no claim is made that either is globally optimal after selection for \(k>2\).

## Proof
Set
\[
E_i=\frac{n(M_i-\mu_i)}\sigma.
\]
Then the \(E_i\)'s are iid standard exponentials. The exponential-spacing decomposition gives
\[
V=\frac S\sigma\sim\operatorname{Gamma}(K,1),\qquad K=k(n-1),
\]
independently of all sample minima. Thus \(E[V]=K\) and \(E[V^2]=K(K+1)\). For one unselected component, unbiasedness of \(M_i-cS\) gives \(c_U=1/(nK)\), while direct quadratic-risk minimization gives \(c_B=1/[n(K+1)]\).

On the one-versus-rest ray let
\[
M^\star=\max(E_1,\ldots,E_{k-1}),\qquad E=E_k,
\]
and put \(D=M^\star-E\). If
\[
A=\frac{Z-\mu_J}{\sigma},
\]
then
\[
nA=E+D\mathbf 1_{\{D>t\}}.
\]
For \(s\ge0\),
\[
\Pr(D>s)=\int_0^\infty e^{-x}\left[1-\left(1-e^{-(x+s)}\right)^{k-1}\right]dx
=\sum_{j=1}^{k-1}(-1)^{j+1}\binom{k-1}{j}\frac{e^{-js}}{j+1}.
\]
Using
\[
E[D\mathbf 1_{\{D>t\}}]=t\Pr(D>t)+\int_t^\infty\Pr(D>s)\,ds
\]
gives \(E[A]=(1+H_{k-1}(t))/n\).

For \(\delta_c=Z-cS\), independence of \(A\) and \(V\) yields
\[
R_t(\delta_c)=E[A^2]-2cE[A]K+c^2K(K+1).
\]
Substitution of \(c_U\) and \(c_B\) cancels \(E[A^2]\) and gives the displayed risk difference.

Finally,
\[
H_{k-1}(t)=E[D\mathbf 1_{\{D>t\}}]
\]
has derivative \(-tf_D(t)<0\) for \(t>0\). At \(t=0\), the selected residual is the maximum of \(k\) standard exponentials, whose mean is \(\sum_{\ell=1}^k1/\ell\); hence \(H_{k-1}(0)=\sum_{\ell=1}^k1/\ell-1\). This exceeds \(1/[2k(n-1)]\), while \(H_{k-1}(t)\to0\), proving existence, uniqueness, and the sign pattern.

## Verification
The bundled `verify.py` checks the excess-residual formula against deterministic two-dimensional quadrature, checks the closed risk difference against its unsimplified quadratic form, and solves the threshold equation by bisection for several \((k,n)\). A successful run ends with `VERIFY_OK k3n3=4.111450606420 k3n5=4.961181135319 k3n10=5.923005815333 k3n15=6.436753036096`. Finite checks are not used as the proof.

## Relationship to prior work
Masihuddin and Misra treat the same shifted-exponential/common-unknown-scale problem for two populations. Their open manuscript records the independence of the two sample minima and pooled spacing statistic, gives the two natural estimators that specialize to \(\delta_U\) and \(\delta_B\), and compares them numerically. Their closing remarks explicitly identify extension of the decision-theoretic results to \(k\ge2\) populations as further research.

Vellaisamy (2003) is the most important broader prior source. It already considers \(k\) exponential populations with unequal locations and common unknown scale, selects by the largest sample minimum, and studies natural estimators of a selected quantile. The accessible abstract and the later paper's discussion do not expose the one-versus-rest risk identity above. The full 2003 article was not available through the checked lawful routes, so equivalent prior coverage remains a material risk.

Targeted searches over \(k\)-population, one-versus-rest, selected-location, natural-estimator, and risk-threshold formulations did not locate the displayed phase diagram.

## Limitations
The theorem is restricted to the one-best versus tied-rest ray and two simple affine corrections. It does not solve arbitrary unequal-location geometry or establish global admissibility/minimaxity. The unavailable full text of Vellaisamy (2003) is the principal bibliographic uncertainty.

## References
1. Masihuddin and N. Misra, “Equivariant Estimation of the Selected Guarantee Time,” arXiv:2110.13842v1, 26 October 2021; published as “Equivariant estimation of the selected location parameter,” *Statistical Papers* 65 (2024), 1733–1771, DOI: 10.1007/s00362-023-01460-x.
2. P. Vellaisamy, “Quantile estimation of the selected exponential population,” *Journal of Statistical Planning and Inference* 115 (2003), 461–470, DOI: 10.1016/S0378-3758(02)00156-8.
