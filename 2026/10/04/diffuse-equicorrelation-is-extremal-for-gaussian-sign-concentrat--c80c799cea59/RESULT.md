# Diffuse equicorrelation is extremal for Gaussian sign concentration at fixed coordinate condition number
## Finding
Fix \(K>1\). For every integer \(n\ge2\), define
\[
\rho_{K,n}=\frac{K-1}{K+n-2},\qquad
\Sigma_{K,n}=(1-\rho_{K,n})I_n+\rho_{K,n}\mathbf 1\mathbf 1^{\mathsf T}.
\]
For \(X_{K,n}\sim N(0,\Sigma_{K,n})\), put \(Y_{K,n}=\operatorname{sgn}(X_{K,n})\), with the sign applied coordinatewise. If
\[
\kappa_\star(\Sigma)=\lambda_{\max}\!\left(D^{1/2}\Sigma D^{1/2}\right),\qquad D=\operatorname{diag}(\Sigma^{-1}),
\]
then
\[
\kappa_\star(\Sigma_{K,n})=K,
\qquad
\kappa(\Sigma_{K,n})=K+\frac{K-1}{n-1}.
\]
The covariance matrix of the sign vector has largest eigenvalue
\[
L_{K,n}
=1+\frac{2(n-1)}{\pi}\arcsin\!\left(\frac{K-1}{K+n-2}\right).
\]
For each fixed \(K>1\), this quantity is strictly increasing in \(n\), and
\[
\sup_{n\ge2} L_{K,n}
=1+\frac{2(K-1)}{\pi}.
\]
Thus, within the positive equicorrelation family at fixed coordinate condition number, the strongest linear sign fluctuation occurs in a diffuse high-dimensional limit in which each pairwise Gaussian correlation tends to zero.

If \(\sigma^2_{K,n}\) is the smallest \(s^2\) such that
\[
\mathbb E\exp\!\left(\lambda\langle u,Y_{K,n}\rangle\right)
\le \exp\!\left(\frac{s^2\lambda^2}2\right)
\]
for every \(\lambda\in\mathbb R\) and every \(u\in S^{n-1}\), then
\[
L_{K,n}\le \sigma^2_{K,n}\le K.
\]
Hence the \(\sqrt{\kappa_\star}\) dependence in Gaussian sign concentration is order-sharp on an explicit nonsingular family. Since \(\kappa(\Sigma_{K,n})\downarrow K\), the ordinary-condition-number dependence in the Zou--Vershynin estimate is likewise order-sharp on a family whose individual correlations vanish. In the iterated limit \(n\to\infty\) and then \(K\to\infty\), the upper variance proxy \(K\) is at most a factor \(\pi/2\) above the displayed covariance lower bound.

## Assumptions and scope
The statement concerns centered nonsingular Gaussian vectors with positive equicorrelation, coordinatewise signs taking values in \(\{-1,1\}\), and the coordinate condition number \(\kappa_\star\) defined above. The extremal assertion is only over the positive equicorrelation slice with \(\kappa_\star=K\); no global extremality over all covariance matrices is claimed. The theorem gives an exact covariance lower bound and a matching-order concentration upper bound, not the exact optimal moment-generating-function proxy \(\sigma^2_{K,n}\).

## Proof
Write \(\rho=\rho_{K,n}\). The equicorrelation matrix has eigenvalue \(1+(n-1)\rho\) on \(\mathbf1\) and eigenvalue \(1-\rho\) on its orthogonal complement. Its inverse is
\[
\Sigma^{-1}=
\frac1{1-\rho}
\left(I_n-\frac{\rho}{1+(n-1)\rho}\mathbf1\mathbf1^{\mathsf T}\right).
\]
Every diagonal entry of \(\Sigma^{-1}\) is therefore
\[
d=\frac{1+(n-2)\rho}{(1-\rho)(1+(n-1)\rho)}.
\]
Thus \(D=dI_n\), and the largest eigenvalue of \(D^{1/2}\Sigma D^{1/2}=d\Sigma\) is
\[
\kappa_\star(\Sigma)
=\frac{1+(n-2)\rho}{1-\rho}.
\]
Substitution of \(\rho=(K-1)/(K+n-2)\) gives \(\kappa_\star=K\). The ordinary condition number is
\[
\kappa(\Sigma)=\frac{1+(n-1)\rho}{1-\rho}
=K+\frac{K-1}{n-1}.
\]

For two standard Gaussian coordinates with correlation \(\rho\), the classical arcsine identity gives
\[
\mathbb E[\operatorname{sgn}(X_i)\operatorname{sgn}(X_j)]
=\frac2\pi\arcsin(\rho).
\]
Consequently \(\operatorname{Cov}(Y_{K,n})\) is itself equicorrelated, with off-diagonal entry
\[
\tau_{K,n}=\frac2\pi\arcsin\!\left(\frac{K-1}{K+n-2}\right),
\]
and its top eigenvalue is \(L_{K,n}=1+(n-1)\tau_{K,n}\).

To optimize this at fixed \(K\), put \(a=K-1>0\) and \(t=n-1\). Apart from the positive factor \(2/\pi\), the varying term is
\[
F(t)=t\arcsin\!\left(\frac a{a+t}\right).
\]
With \(r=a/(a+t)\in(0,1)\), differentiation gives
\[
F'(t)=\arcsin(r)-r\sqrt{\frac{1-r}{1+r}}.
\]
Since \(\arcsin(r)>r\) and \(\sqrt{(1-r)/(1+r)}<1\), one has \(F'(t)>0\). Finally,
\[
\lim_{t\to\infty}t\arcsin\!\left(\frac a{a+t}\right)=a,
\]
which proves the claimed supremum and shows that it is approached as the individual correlation tends to zero.

For the concentration sandwich, any common moment-generating-function variance proxy must dominate the variance of every unit linear functional. Hence it is at least \(\lambda_{\max}(\operatorname{Cov}Y_{K,n})=L_{K,n}\). Roth's Gaussian Hamming-Lipschitz inequality, applied to the sign vector, gives the upper proxy \(\kappa_\star(\Sigma_{K,n})=K\). The asymptotic factor follows from
\[
\frac{K}{1+2(K-1)/\pi}\longrightarrow\frac\pi2.
\]
The same covariance lower bound also certifies sharp order for a bounded-difference scalar witness: \(n^{-1/2}\sum_i\operatorname{sgn}(X_i)\) has coordinate oscillations at most \(2/\sqrt n\) and variance \(L_{K,n}\).

## Verification
All identities are exact. Substituting \(\rho=(K-1)/(K+n-2)\) into the inverse and eigenvalue formulas gives \(\kappa_\star=K\) and \(\kappa=K+(K-1)/(n-1)\) by direct algebra. The covariance formula follows from the Gaussian sign arcsine identity. Strict monotonicity reduces to the displayed one-variable derivative, whose two terms have an elementary strict inequality for every \(0<r<1\). The lower bound on any moment-generating-function proxy follows by taking the second derivative at \(\lambda=0\). No simulation, finite enumeration, or unproved limiting interchange is used.

## Relationship to prior work
Zou and Vershynin proved a Gaussian bounded-differences estimate with ordinary condition-number dependence and used a singular rank-one Gaussian example to show that some conditioning dependence is necessary. Roth independently sharpened the Gaussian parameter to \(\kappa_\star\) and showed that coordinatewise sign vectors admit the corresponding sub-Gaussian upper proxy. Barber and Kolar gave an earlier condition-number upper bound for Gaussian sign vectors, while Han and Liu treated compound-symmetric Gaussian signs among their sign-sub-Gaussian examples. Those results supply upper bounds or special-family concentration statements. The present result instead exactly calibrates the positive equicorrelation family by the newer \(\kappa_\star\), optimizes its sign-covariance spectral norm over dimension at fixed \(\kappa_\star\), and obtains a nonsingular vanishing-correlation sharpness family with an explicit asymptotic \(\pi/2\) gap between the known upper proxy and the covariance obstruction.

## Limitations
The covariance lower bound need not equal the optimal sub-Gaussian variance proxy. No claim is made that positive equicorrelation is extremal among all covariance matrices having a given \(\kappa_\star\), nor that the factor \(\pi/2\) is globally best possible. The construction addresses sign quantization and the associated bounded-difference witness, not arbitrary nonlinear coordinate maps. The originality comparison cannot exclude an equivalent observation hidden in older Gaussian sign literature under different terminology.

## References
1. G. Zou and R. Vershynin, *On the Subgaussianity of Quantized Linear Maps*, arXiv:2605.27563v1, first public 2026-05-26.
2. V. Roth, *A McDiarmid-Type Inequality for Dependent Random Variables*, arXiv:2606.12720v1, first public 2026-06-10.
3. R. F. Barber and M. Kolar, *ROCKET: Robust Confidence Intervals via Kendall's Tau for Transelliptical Graphical Models*, arXiv:1502.07641v3.
4. F. Han and H. Liu, *Statistical Analysis of Latent Generalized Correlation Matrix Estimation in Transelliptical Distribution*, arXiv:1305.6916v4.
