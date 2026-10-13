# Zero-crossing count has exact opposite-sign covariance with Gaussian AR(1) energy
## Finding
Let \((X_k)\) be a stationary mean-zero Gaussian AR(1) process with \(\operatorname{Var}(X_k)=\sigma^2>0\), correlation parameter \(\rho\in(-1,1)\), and hence \(\operatorname{Corr}(X_j,X_k)=\rho^{|j-k|}\). For \(n\ge2\), define the zero-crossing indicators
\[
I_i=\mathbf 1\{X_iX_{i+1}<0\},\qquad 1\le i<n,
\]
the crossing count \(T_n=\sum_{i=1}^{n-1}I_i\), and the uncentered sample energy \(Q_n=\sum_{j=1}^n X_j^2\).

For an edge \(i\) and a site \(j\), put
\[
d(i,j)=\begin{cases}i-j,&j\le i,\\ j-i-1,&j\ge i+1.\end{cases}
\]
Then, with the usual convention that a zeroth power equals one,
\[
\operatorname{Cov}(I_i,X_j^2)
=-\frac{\sigma^2\rho\sqrt{1-\rho^2}}{\pi}\,(\rho^2)^{d(i,j)}.
\]
Consequently,
\[
\boxed{\operatorname{Cov}(T_n,Q_n)
=-\frac{2\sigma^2\rho}{\pi\sqrt{1-\rho^2}}
\sum_{r=1}^{n-1}(1-\rho^{2r}).}
\]
The sum is strictly positive. Therefore the covariance has sign exactly opposite to \(\rho\), and it is zero exactly when \(\rho=0\). For fixed \(|\rho|<1\),
\[
\frac1n\operatorname{Cov}(T_n,Q_n)
\longrightarrow -\frac{2\sigma^2\rho}{\pi\sqrt{1-\rho^2}}.
\]

## Assumptions and scope
The process is Gaussian, stationary, mean zero, and first-order autoregressive. Equivalently one may write \(X_{k+1}=\rho X_k+\varepsilon_{k+1}\), where the innovations are independent centered Gaussians with variance \(\sigma^2(1-\rho^2)\), and the initial variable has the stationary \(N(0,\sigma^2)\) law. The result concerns the uncentered quadratic energy \(Q_n\), not the sample variance after estimating a mean. No claim is made for non-Gaussian AR processes or for general stationary Gaussian covariance sequences.

## Proof
First consider a standardized adjacent pair \((Z_0,Z_1)\) with unit variances and correlation \(\rho\). Let \(I=\mathbf 1\{Z_0Z_1<0\}\) and set \(a=\rho/\sqrt{1-\rho^2}\). The classical bivariate normal orthant formula gives
\[
p:=\mathbb P(I=1)=\frac{\arccos\rho}{\pi}.
\]
By symmetry and the conditional normal law,
\[
\mathbb E[Z_0^2 I]
=2\int_0^\infty z^2\phi(z)\Phi(-az)\,dz,
\]
where \(\phi\) and \(\Phi\) are the standard normal density and distribution function. Since \(z^2\phi(z)=\phi(z)-(z\phi(z))'\), integration by parts yields
\[
\mathbb E[Z_0^2 I]
=p-2a\int_0^\infty z\phi(z)\phi(az)\,dz
=p-\frac{a}{\pi(1+a^2)}
=p-\frac{\rho\sqrt{1-\rho^2}}{\pi}.
\]
Hence, after restoring the scale,
\[
\operatorname{Cov}(I_i,X_i^2)
=\operatorname{Cov}(I_i,X_{i+1}^2)
=-\frac{\sigma^2\rho\sqrt{1-\rho^2}}{\pi}.
\]

For \(j\le i\), stationarity and the Gaussian AR(1) Markov property give
\[
\mathbb E[X_j^2-\sigma^2\mid X_i]
=\rho^{2(i-j)}(X_i^2-\sigma^2).
\]
The past before time \(i\) is conditionally independent of \(X_{i+1}\) given \(X_i\), so taking covariance with \(I_i\) gives
\[
\operatorname{Cov}(I_i,X_j^2)
=\rho^{2(i-j)}\operatorname{Cov}(I_i,X_i^2).
\]
The time-reversed argument for \(j\ge i+1\) gives the same decay away from \(X_{i+1}\). This proves the local kernel formula.

Summing over \(j\) first,
\[
\operatorname{Cov}(I_i,Q_n)
=-\frac{\sigma^2\rho\sqrt{1-\rho^2}}{\pi}
\left(\sum_{d=0}^{i-1}\rho^{2d}+\sum_{d=0}^{n-i-1}\rho^{2d}\right).
\]
Summing over \(i=1,\ldots,n-1\) and collecting equal geometric powers gives
\[
\operatorname{Cov}(T_n,Q_n)
=-\frac{2\sigma^2\rho}{\pi\sqrt{1-\rho^2}}
\sum_{r=1}^{n-1}(1-\rho^{2r}).
\]
Each factor \(1-\rho^{2r}\) is positive for \(|\rho|<1\), proving the sign statement. Dividing by \(n\) and using \(n^{-1}\sum_{r=1}^{n-1}\rho^{2r}\to0\) proves the stated limit.

## Verification
The proof is analytic. The accompanying `verify.py` independently checks the only nontrivial integral numerically for seven positive, negative, and zero correlations; compares the closed covariance against the unsimplified edge-by-site geometric sum on 632 finite parameter pairs; and checks the sign law plus the independent case on 731 cases. Its expected terminal line is `VERIFY_OK`.

## Relationship to prior work
Sinn and Keller study the same discrete zero-crossing indicator for stationary Gaussian processes, derive crossing-crossing covariances, analyze the variance of the empirical crossing rate, and treat Gaussian AR(1) explicitly. Their AR(1) section notes that the crossing covariance sequence is unchanged when the autoregressive parameter changes sign. The inspected full text does not state a mixed covariance with squared amplitude or total quadratic energy. Finch later studies the same finite AR(1) sign-change count and focuses on its variance and higher crossing-count moments. The present result instead couples a crossing statistic to the continuous amplitude energy and supplies an exact geometric cross-covariance kernel at every edge and site.

## Limitations
The theorem does not extend automatically to arbitrary stationary Gaussian processes because the geometric propagation step uses the AR(1) Markov structure. It also does not address centered sample variance, unknown-mean corrections, non-Gaussian innovations, or threshold crossings away from zero. The literature comparison cannot exclude an older signal-processing derivation under different notation; in particular, a local sign/amplitude identity could appear as a corollary of a more general Gaussian nonlinear-functional calculation.

## References
1. M. Sinn and K. Keller, “Covariances of Zero Crossings in Gaussian Processes,” *Teoriya Veroyatnostei i ee Primeneniya* 55(3), 548–570 (2010); English translation *Theory of Probability and Its Applications* 55(3), 485–504 (2011). DOI 10.1137/S0040585X97984991; MathNet tvp4241.
2. S. Finch, “Number of Sign Changes: Segment of AR(1),” arXiv:1909.02556 (2019).
3. M. Nyberg, L. Lizana, and T. Ambjörnsson, “Zero-crossing statistics for non-Markovian time series,” *Physical Review E* 97, 032114 (2018). DOI 10.1103/PhysRevE.97.032114.
