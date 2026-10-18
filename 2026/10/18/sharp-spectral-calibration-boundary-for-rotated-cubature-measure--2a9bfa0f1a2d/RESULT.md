# Sharp spectral calibration boundary for rotated cubature measurements

## Finding

A fully specified one-step nonlinear filtering benchmark has a **sharp spectral test for whether any orthogonal orientation of the usual third-degree cubature rule can correctly report its unconditional mean-squared error**. Let the Gaussian prior be isotropic and let the scalar measurement be the sum of an arbitrary nonzero linear form, an arbitrary nonzero quadratic form, and independent noise. Although every orthogonal covariance square root represents exactly the same prior, the predicted innovation variance fills an explicit nontrivial interval. Some frames can overstate measurement variance and other frames understate it precisely when a spectral trace-to-Frobenius threshold is crossed.

For \(n\ge2\), write \(F=\|B\|_F^2>0\), \(t=\operatorname{tr}B\), and \(w=R+\|\ell\|_2^2>0\). Over all \(U\in O(n)\), the innovation variance \(s_U\) of the \(2n\)-point spherical-radial cubature update attains **every** value in
\[
\boxed{\quad w\le s_U\le w+nF-t^2.\quad}
\]
The true innovation variance is \(s_*=w+2F\). The cubature reported covariance \(P_U^{\mathrm{rep}}\) and the actual **unconditional mean-squared error covariance** \(P_U^{\mathrm{mse}}\) of its updated mean satisfy
\[
\boxed{\quad P_U^{\mathrm{mse}}-P_U^{\mathrm{rep}}=
\frac{s_*-s_U}{s_U^2}\,\ell\ell^{\mathsf T}.\quad}
\]
Consequently, an exactly calibrated frame exists precisely when
\[
\boxed{\quad n\ge 2+\frac{(\operatorname{tr}B)^2}{\|B\|_F^2}.\quad}
\]
At strict inequality both signs of covariance mismatch occur, with exact calibration between them; at equality the calibrated frames are exactly orthogonal eigenframes of \(B\); and when the inequality fails every frame strictly underreports actual error along \(\ell\). These are *unconditional errors of a specific affine estimator*, not conditional Bayesian posterior covariances.

For instance, a rank-one quadratic form has critical ambient dimension three: at dimension three only the eigenframes achieve calibration, whereas dimension four already admits both signs. A traceless nonzero quadratic form admits both signs in every dimension at least three. A scalar quadratic form \(B=bI_n\), in contrast, is invisible to the rule's quadratic innovation variance for every orientation, no matter how large the dimension.

## Assumptions and scope

Fix an integer \(n\ge2\), a nonzero \(\ell\in\mathbb R^n\), a nonzero real symmetric \(n\times n\) matrix \(B\), and \(R>0\). Let \(X\sim N(0,I_n)\), independently of the mean-zero scalar Gaussian noise \(\eta\) of variance \(R\), and observe
\[
Y=h(X)+\eta,\qquad h(x)=\ell^{\mathsf T}x+x^{\mathsf T}Bx.
\]
There is one measurement update, no dynamics and no previous posterior approximation. Given any orthogonal \(U\), the standard positive-weight degree-three spherical-radial cubature rule samples \(\xi_j^\pm=\pm\sqrt n\,Ue_j\), each with weight \(1/(2n)\). Its predicted measurement mean, innovation covariance, state-measurement cross covariance, gain, updated mean and reported covariance are computed by the usual linear-Kalman-style moment formulas. Here the updated mean is the estimator \(\widehat X_U=K_U(Y-t)\), where \(t=\operatorname{tr}B\). All statements assume exact arithmetic. We use 'overconfident' to mean that the reported matrix is strictly smaller than the actual unconditional mean-squared error matrix along the nonzero direction \(\ell\); 'underconfident' means the reverse. These statements do not assert Gaussian conditional posteriors.

## Proof

**1. The complete cubature moments.** Write \(b_j=(U^{\mathsf T}BU)_{jj}\) and \(d_j=(U^{\mathsf T}\ell)_j\). On a signed pair of cubature points,
\[
h(\xi_j^\pm)=nb_j\pm\sqrt n\,d_j.
\]
Pairing signs, the predicted mean is \(\sum_j b_j=t\). The third-degree rule reproduces the state covariance \(I_n\), and its odd cubic contributions vanish. Thus the cross covariance equals exactly \(\ell\), while the estimated innovation variance is
\[
s_U=R+\|\ell\|_2^2+n\sum_{j=1}^n b_j^2-t^2.
\]
The Gaussian fourth-moment identity \(\operatorname{Var}(X^{\mathsf T}BX)=2\operatorname{tr}(B^2)=2F\), and cancellation of the mixed odd moment, yield \(s_*=w+2F\), with \(w=R+\|\ell\|_2^2\).

**2. Sharp, continuously attained extrema.** Because the diagonal entries of \(U^{\mathsf T}BU\) sum to \(t\), Cauchy–Schwarz gives \(\sum_j b_j^2\ge t^2/n\), so \(s_U\ge w\). An elementary equal-diagonal orthonormal basis exists for every symmetric \(B\): its average eigenvalue \(t/n\) lies between its smallest and largest eigenvalues, so there is a unit vector with Rayleigh quotient \(t/n\) by continuous interpolation between corresponding eigenvectors. Compress to its orthogonal complement. The compressed symmetric matrix has trace \((n-1)t/n\), hence the same mean Rayleigh quotient. Repeat inductively. The resulting orthogonal frame has \(b_j=t/n\) for every \(j\), attaining the lower bound.

On the other hand,
\[
F=\operatorname{tr}[(U^{\mathsf T}BU)^2]
=\sum_j b_j^2+2\sum_{i<j}(U^{\mathsf T}BU)_{ij}^2,
\]
so \(\sum_j b_j^2\le F\), with equality exactly when \(U^{\mathsf T}BU\) is diagonal. An eigenframe attains the upper bound \(w+nF-t^2\). The map from \(SO(n)\) to the real innovation variance is continuous, and \(SO(n)\) is connected for \(n\ge2\). Any two frames can have their determinant made positive by changing the sign of one column, without altering the diagonal values. Hence the entire closed interval between its two attained extrema is attained, with no gaps.

**3. Actual error versus reported covariance.** The gain is \(K_U=\ell/s_U\), and the reported covariance is
\[
P_U^{\mathrm{rep}}=I_n-\ell\ell^{\mathsf T}/s_U.
\]
Since the exact cross covariance of \(X\) and \(Y\) is \(\ell\), the unconditional covariance of \(X-K_U(Y-t)\) is
\[
P_U^{\mathrm{mse}}=I_n-2\ell\ell^{\mathsf T}/s_U
+s_*\ell\ell^{\mathsf T}/s_U^2.
\]
Subtracting gives the rank-one difference in the finding. In particular, calibration is equivalent to \(s_U=s_*\), because \(\ell\ne0\), and is achieved exactly when \(nF-t^2\ge2F\). This is the displayed spectral threshold. At equality, only a maximizer of \(\sum b_j^2\) calibrates, namely a diagonalizing frame. At strict inequality the two extrema straddle \(s_*\), producing opposite signs and a calibrated intervening frame. Below threshold even the largest \(s_U\) is strictly smaller than \(s_*\).

**4. Unbounded overconfidence under fixed prior and fixed gain.** Choose an equal-diagonal frame. For any fixed nonzero \(B_0\), replace \(B\) by \(\alpha B_0\) and retain the same constant-diagonal frame (the frame can be chosen independently of positive \(\alpha\)). Then \(s_U=w\), the gain and reported covariance are independent of \(\alpha\), while
\[
P_U^{\mathrm{mse}}-P_U^{\mathrm{rep}}
=\frac{2\alpha^2\|B_0\|_F^2}{w^2}\,\ell\ell^{\mathsf T}.
\]
Its nonzero eigenvalue diverges quadratically as \(\alpha\to\infty\). This is true statistical mean-squared error, not a numerical roundoff phenomenon. It also shows why exact positive-definiteness of the reported covariance does not guarantee its calibration.

## Verification

The accompanying standalone file `verify.py` checks the exact sign-paired cubature moment formulas directly from their \(2n\) points; the gain/covariance identity; constructive constant-diagonal frames; eigenframe maxima; and examples covering the strict, boundary and impossible-calibration regimes. Run `python verify.py` with NumPy installed. The script's output is a reproducibility check only: the connectedness, extremum and all-dimension classification follow from the proof above, not from a finite numerical search.

## Relationship to prior work

The classical third-degree spherical-radial cubature rule and its measurement-update formulas were established by Arasaratnam and Haykin (2009). Singh (2017) explicitly studies **orthogonally transformed** cubature-quadrature points and higher-order-moment errors, so *rotation sensitivity itself is not claimed as new*. Jiang, Shi and Moura's original July 2024 manuscript motivates accurate covariance reporting for nonlinear Kalman filters. Jiang and collaborators (2026) explicitly discuss CKF orientation sensitivity, provide general CKF moment equations and true-error-covariance equations, and derive a Haar-rotation-averaged quadratic benchmark. The present claim is narrower and distinct: it supplies the **entire exact attainable interval for every symmetric quadratic form**, a necessary-and-sufficient *spectral sign-transition criterion*, the precise equality frames, and an unconditional true-error consequence. Those conclusions require the optimization over all orthogonal conjugates and their extremal attainability, rather than merely the formulas for one fixed sigma-point frame. These building blocks are prior art; a matching special-case treatment elsewhere remains possible.

## Limitations

Only an isotropic Gaussian prior, one scalar quadratic-plus-linear measurement, independent additive Gaussian noise, and the unmodified positive-weight \(2n\)-point third-degree cubature update are covered. A specific SVD implementation may consistently select just one of the admissible frames; the theorem concerns the **mathematical nonuniqueness of covariance square roots**, not randomness in a fixed software implementation. The actual covariance is unconditional MSE of the affine cubature update, not the conditional Bayesian posterior covariance. Higher-degree cubature, modified compensation rules, noisy dynamics, repeated measurements, or nonisotropic priors require separate analysis. No assertion of independent audit or publication priority is made.

## References

1. I. Arasaratnam and S. Haykin, “Cubature Kalman Filters,” *IEEE Transactions on Automatic Control* **54** (2009), 1254–1269. DOI: 10.1109/TAC.2009.2019800.
2. A. K. Singh, “Transformed cubature quadrature Kalman filter,” *IET Signal Processing* (2017), DOI: 10.1049/iet-spr.2017.0074.
3. S. Jiang, J. Shi and S. Moura, “A New Framework for Nonlinear Kalman Filters,” first arXiv submission July 8, 2024, arXiv:2407.05717. Later revisions have other titles.
4. S. Jiang, J. Lee, S. Tao and S. Moura, “Design Guidelines for Nonlinear Kalman Filters via Covariance Compensation,” arXiv:2603.22992v1 (March 24, 2026), especially Sections II and III.
5. M. V. Kulikova and G. Yu. Kulikov, “SVD-based factored-form Cubature Kalman Filtering for continuous-time stochastic systems with discrete measurements,” *International Journal of Adaptive Control and Signal Processing* (2020), original publication preceding its 2024 arXiv upload.
