# Product-Gaussian critical torque and oscillatory memory in a sheared nonreciprocal trap

## Finding

For \(0\le g<3\), let \(X_t=(x_t,y_t,z_t)^\mathsf T\) be the **stationary** solution of
\[
 dX_t=K_gX_t\,dt+\sqrt2\,dW_t,\qquad
 K_g=\begin{pmatrix}-1&g&-1\\0&-1&1\\1&-1&-1\end{pmatrix},
\]
where the coordinates of \(W\) are independent standard Brownian motions. Define the **instantaneous deterministic-force torque**, rather than a white-noise velocity torque, by
\[
 L_g(t)=x_t(K_gX_t)_2-y_t(K_gX_t)_1
        =x_tz_t+y_tz_t-g y_t^2.
\]
Write \(\delta=3-g\). For every integer \(m\ge1\) and every fixed real times \(t_1,\ldots,t_m\),
\[
 (\sqrt\delta L_g(t_1),\ldots,\sqrt\delta L_g(t_m))
 \ \Longrightarrow\ (2Z\eta_{t_1},\ldots,2Z\eta_{t_m}),
\]
where \(Z\sim N(0,6/5)\) is a single time-independent random variable, independent of the entire centered stationary Gaussian process \(\eta\) with covariance
\[
 R_\eta(t)=e^{-3|t|/2}\left[5\cos\!\left(\frac{\sqrt{11}|t|}{2}\right)
 -\frac5{2\sqrt{11}}\sin\!\left(\frac{\sqrt{11}|t|}{2}\right)\right].
\]
In particular, the one-time limiting torque has characteristic function \((1+24u^2)^{-1/2}\) and probability density
\[
 f(\ell)=\frac1{2\pi\sqrt6}\,K_0\!\left(\frac{|\ell|}{2\sqrt6}\right),\qquad \ell\ne0,
\]
with its integrable logarithmic singularity at zero. Its variance is \(24\) and excess kurtosis is \(6\). The **critical two-time covariance** obeys, at every fixed \(t\in\mathbb R\),
\[
 \lim_{g\uparrow3}(3-g)\operatorname{Cov}(L_g(0),L_g(t))
 =24e^{-3|t|/2}\left[\cos\!\left(\frac{\sqrt{11}|t|}{2}\right)
 -\frac1{2\sqrt{11}}\sin\!\left(\frac{\sqrt{11}|t|}{2}\right)\right].
\]
For \(t\ge0\), this limiting covariance has simple zeros at
\[
 t_n=\frac2{\sqrt{11}}\left[\arctan(2\sqrt{11})+n\pi\right],\qquad n=0,1,2,\ldots,
\]
and alternates in sign between successive zeros. The first negative interval is \((t_0,t_1)\).

## Assumptions and scope

The three-dimensional noise covariance is exactly \(2I_3\); the restoring coefficients, auxiliary couplings and temperature are normalized to one. The first two coordinates are physical particle positions; the third is the hidden-medium coordinate. The shear is nonnegative and strictly below the stability threshold \(3\). We use stationary initialization for each \(g<3\). The limit concerns any *fixed finite set of physical times*, not a time window growing as \(g\uparrow3\). Only deterministic drift forces enter \(L_g\).

## Proof

**1. Gaussian stationary covariance.** The characteristic polynomial of \(K_g\) is \(\lambda^3+3\lambda^2+5\lambda+3-g\), so the Routh–Hurwitz conditions give exponential stability for \(0\le g<3\). The unique centered invariant Gaussian law has covariance \(\Sigma_g\) satisfying \(K_g\Sigma_g+\Sigma_gK_g^\mathsf T+2I_3=0\). Solving yields exactly
\[
 \Sigma_g=\frac1{(3-g)(g+12)}
 \begin{pmatrix}
 -g^3+9g^2-6g+36&g(15-g)&g(5g-3)\\
 g(15-g)&6(6-g)&g(g+3)\\
 g(5g-3)&g(g+3)&3(g^2-5g+12)
 \end{pmatrix}.
\]
Set \(v=(2,1,1)^\mathsf T\), \(a=(1,-5,3)^\mathsf T/2\), and \(K_*=K_3\). Direct calculation gives \(K_*v=0\) and \(a^\mathsf Tv=0\), and the Laurent expansion at the stability threshold is
\[
 \Sigma_g=\frac{6}{5\delta}vv^\mathsf T+B+O(\delta),\qquad
 B=\frac1{25}\begin{pmatrix}-27&-11&-41\\-11&12&-13\\-41&-13&-3\end{pmatrix}.
\]
All matrix identities are verified symbolically in `verify.py`.

**2. Slow and fast Gaussian coordinates.** Decompose \(X_t=\xi_g(t)v+Y_g(t)\), where \(\xi_g=v^\mathsf TX/6\) and \(Y_g=(I_3-vv^\mathsf T/6)X\). Let \(\eta_g(t)=a^\mathsf TX_t\). For every fixed time, \(Y_g(t)\) has uniformly bounded second moments, because the pole part of \(\Sigma_g\) is annihilated by the projection. Stationarity gives \(\operatorname{Cov}(X_t,X_s)=e^{K_g(t-s)}\Sigma_g\) for \(t\ge s\). Since \(K_*v=0\), at any fixed time pair,
\[
 \operatorname{Cov}(\sqrt\delta\,\xi_g(t),\sqrt\delta\,\xi_g(s))\to\frac65,
 \qquad \operatorname{Cov}(\sqrt\delta\,\xi_g(t),\eta_g(s))\to0.
\]
Meanwhile \(\eta_g\) converges in finite-dimensional distributions to a centered stationary Gaussian process with \(\operatorname{Cov}(\eta_0,\eta_t)=a^\mathsf Te^{K_*|t|}Ba\). The zero eigendirection vanishes because \(a^\mathsf Tv=0\). The remaining characteristic roots are \((-3\pm i\sqrt{11})/2\), so its covariance solves \(R''+3R'+5R=0\) for positive times. The initial values \(R(0)=a^\mathsf TBa=5\) and \(R'(0+)=a^\mathsf TK_*Ba=-35/4\) yield precisely the displayed damped oscillation. Finite-dimensional joint Gaussian convergence thus gives a **single** normal \(Z\) constant across the selected times, independent of \(\eta\).

**3. Torque cancellation and product limit.** Let
\[
 H_g=\begin{pmatrix}0&0&1/2\\0&-g&1/2\\1/2&1/2&0\end{pmatrix},
 \qquad L_g=X^\mathsf TH_gX.
\]
The identities \(H_3v=a\), \(v^\mathsf TH_3v=0\) and \(H_g=H_3+\delta E_{22}\) show
\[
 L_g(t)=2\xi_g(t)\eta_g(t)+Y_g(t)^\mathsf TH_3Y_g(t)+\delta y_t^2.
\]
The last two terms multiplied by \(\sqrt\delta\) vanish in probability at each fixed time: the first by bounded moments of \(Y_g\), and the second because \(\delta\mathbb E[y_t^2]\) remains bounded. Joint Gaussian convergence and Slutsky's theorem prove the stated finite-dimensional product limit. At a single time the product \(2Z\eta_0\) has variance \(4(6/5)5=24\); its Gaussian-product characteristic function is \((1+24u^2)^{-1/2}\), whose inversion is the stated modified-Bessel density. Wick's rule gives excess kurtosis \(6\).

**4. Exact mean, variance, and lag covariance.** Wick's theorem for the centered Gaussian quadratic form yields \(\mathbb EL_g=\operatorname{tr}(H_g\Sigma_g)\) and \(\operatorname{Var}L_g=2\operatorname{tr}[(H_g\Sigma_g)^2]\). Simplification gives
\[
 \mathbb EL_g=-\frac{12g}{g+12},\quad
 \operatorname{Var}L_g=
 \frac{864+144g+834g^2-123g^3-g^4}{(3-g)(g+12)^2}
 =\frac{24}{3-g}+O(1).
\]
Similarly \(48\operatorname{tr}[(H_g\Sigma_g)^4]\) is the fourth cumulant, and \(\delta^2\kappa_4(L_g)\to3456\). The finite-lag quadratic-form cross covariance is
\[
 \operatorname{Cov}(L_g(0),L_g(t))
 =2\operatorname{tr}\!\left(H_g\Sigma_g e^{K_g^\mathsf T|t|}H_g e^{K_g|t|}\Sigma_g\right).
\]
All fixed-lag torque moments of order four are bounded after multiplying by \(\delta^2\), so the product-limit convergence is uniformly integrable at second order. Consequently \(\delta\operatorname{Cov}(L_g(0),L_g(t))\to4(6/5)R_\eta(t)\), which is the claimed kernel. Its zeros and strict alternating signs follow from the explicit sine–cosine representation.

## Verification

Running `python verify.py` with Python 3 and SymPy establishes 101 exact symbolic identities. These include the characteristic polynomial, all nine Lyapunov residuals, independent solutions at rational parameters, covariance pole and finite part, mean/variance/fourth-cumulant limits, the limiting quadratic-form characteristic determinant, and the first derivatives plus differential equation of the lag kernel. The analytic proof, rather than any finite checks, establishes distributional convergence and the statements for all fixed times.

## Relationship to prior work

Fernandez, Hess and Klapp established this three-coordinate nonreciprocal shear-trap system, its second-moment stationary law, loss of stability at shear \(3\), and its finite ensemble-averaged torque/angular momentum. Their later analysis explicitly pointed toward higher-order distributions and reported qualitative critical divergence of angular-momentum fluctuations. The present theorem does **not** claim the model, Gaussian stationary state, divergence of unnormalized second moments, mean torque, or existence of diverging fluctuations as new. It resolves the *specific deterministic-force torque* by giving the exact divergence coefficient, the non-Gaussian product-normal critical law, and the fixed-lag oscillatory covariance with a complete zero sequence. Angular-momentum definitions involving stochastic velocities are not identified with this instantaneous drift-force torque. These calculations follow from the earlier Gaussian covariance machinery but are not the conclusions asserted in those sources.

## Limitations

The theorem uses exactly the normalized three-coordinate linear model and stationary states with \(g<3\). It does not cover the unstable, source–sink-controlled model above the threshold, finite-time parameter scaling on the order of \((3-g)^{-1}\), integrated entropy production or path-space fluctuation relations. Finite-dimensional convergence is not claimed to hold uniformly over growing observation windows. The comparison with literature is a best-knowledge assessment, not a claim of exhaustive priority or independent certification.

## References

1. L. Fernandez, S. Hess and S. H. L. Klapp, *Shear-flow-induced distortion of the density distribution and transition from a stationary to an instationary non-equilibrium state of a colloidal particle in a trap*, Atti della Accademia Peloritana dei Pericolanti 101 (2023), DOI:10.1478/AAPP.1011A3 (public online February 17, 2023).
2. L. Fernandez, S. Hess and S. H. L. Klapp, *Nonequilibrium dynamics and entropy production of a trapped colloidal particle in a complex nonreciprocal medium*, arXiv:2402.10579v1 (February 16, 2024), especially sections III–VI and appendix C.
3. Standard Gaussian quadratic-form identities, Lyapunov covariance theory and the Routh–Hurwitz criterion; all needed algebra for this specialization is provided above and checked in `verify.py`.
