# A hidden fractional time arrow at zero signed circulation in a two-bath gyrator

## Finding

Two independent fractional Gaussian baths driving a coupled harmonic particle can be tuned to have **zero infinitesimal mean signed circulation** while their stationary position trajectory remains **strictly time irreversible at every sufficiently short positive lag**. Its antisymmetric cross-covariance then has a sharp noninteger (generically) fractional cusp, with an exponent fixed by the bath with the smaller memory exponent.

Specifically, set \(F(u,\alpha)=(1+u)^{2-\alpha}-(1-u)^{2-\alpha}\). At the unique positive bath-strength ratio
\[
\frac{T_y}{T_x}=\frac{\Gamma(1+\alpha_x)F(u,\alpha_x)}{\Gamma(1+\alpha_y)F(u,\alpha_y)},
\]
we have \(A'(0^+)=0\), where \(A(t)=\mathbb E[X_tY_0-Y_tX_0]\). Yet at that ratio,
\[
\lim_{t\downarrow0}\frac{A(t)}{t^{1+\min(\alpha_x,\alpha_y)}}=
\begin{cases}
\dfrac{2uT_x}{1+\alpha_x},&\alpha_x<\alpha_y,\\[5pt]
-\dfrac{2uT_y}{1+\alpha_y},&\alpha_y<\alpha_x.
\end{cases}
\]
The nonzero sign and exact amplitude yield a short-lag witness of time reversal asymmetry even when the usual signed-circulation mean has been balanced to zero.

## Assumptions and scope

Fix \(0<u<1\), distinct \(\alpha_x,\alpha_y\in(0,2)\), and \(T_x,T_y>0\). For each coordinate take an independent, two-sided centered fractional Brownian input \(B_i\) with stationary increments normalized by
\[
\mathbb E[(B_i(t)-B_i(s))^2]=2T_i|t-s|^{\alpha_i}.
\]
Let \(\xi_i\) be its generalized stationary time derivative. Define the **stationary** continuous Gaussian position process \(Z_t=(X_t,Y_t)^{\mathsf T}\) by the stable linear filter
\[
\dot Z_t=-KZ_t+\xi_t,\qquad
K=\begin{pmatrix}1&-u\\-u&1\end{pmatrix}.
\]
Equivalently, this is the stationary convolution with the causal matrix exponential, interpreted as a fractional-Gaussian integral. Both eigenvalues \(1\pm u\) are positive, so the stationary law exists and its covariances are finite. Time reversal means equality of the complete finite-dimensional distributions of \((Z_t)_{t\in\mathbb R}\) and \((Z_{-t})_{t\in\mathbb R}\), without reversing spatial coordinates. No classical path derivative is assumed for the individual fractional-Gaussian positions.

## Proof

**1. Spectrum and chronological covariance.** Use Fourier covariance convention \(C_{ij}(t)=(2\pi)^{-1}\int_{\mathbb R}e^{i\omega t}\Phi_{ij}(\omega)\,d\omega\). The independent generalized inputs have spectral densities
\[
S_i(\omega)=2T_i\Gamma(1+\alpha_i)\sin(\pi\alpha_i/2)|\omega|^{1-\alpha_i}.
\]
This normalization follows by integrating the spectrum twice and using \(\int_0^\infty(1-\cos z)z^{-1-\alpha}\,dz=\pi/[2\Gamma(1+\alpha)\sin(\pi\alpha/2)]\). Define
\[
D_u(\omega)=[\omega^2+(1-u)^2][\omega^2+(1+u)^2].
\]
The transfer matrix \((K+i\omega I)^{-1}\) gives
\[
\Phi_{xy}(\omega)=\frac{u\{S_x(\omega)+S_y(\omega)+i\omega[S_x(\omega)-S_y(\omega)]\}}{D_u(\omega)},
\]
while \(\Phi_{yx}=\overline{\Phi_{xy}}\). Hence for every real lag,
\[
A(t)=-\frac{2u}{\pi}\int_0^\infty\frac{\omega[S_x(\omega)-S_y(\omega)]\sin(\omega t)}{D_u(\omega)}\,d\omega.
\tag{1}
\]
The integral converges absolutely for every \(\alpha_i\in(0,2)\); its derivative at zero exists by the same spectral bounds.

**2. Exactly one zero-circulation calibration.** Differentiating (1) at \(t=0^+\) is justified by absolute integrability of \(\omega^2 S_i/D_u\). The beta-integral identity
\[
\int_0^\infty\frac{\omega^{3-\alpha}}{D_u(\omega)}\,d\omega
=\frac{\pi}{2\sin(\pi\alpha/2)}\frac{(1+u)^{2-\alpha}-(1-u)^{2-\alpha}}{4u}
\]
for \(0<\alpha<2\) gives
\[
A'(0^+)=-\frac12\big[T_x\Gamma(1+\alpha_x)F(u,\alpha_x)-T_y\Gamma(1+\alpha_y)F(u,\alpha_y)\big].
\tag{2}
\]
Both \(F(u,\alpha_i)>0\), since \(u>0\) and \(2-\alpha_i>0\). Consequently (2) has exactly one solution in the positive ratio \(T_y/T_x\), namely that in the finding.

**3. The uncancelled fractional cusp.** At this calibration, subtract \(\omega t\) from \(\sin(\omega t)\) inside (1); the added term integrates to zero by (2). For one bath of exponent \(\alpha\) and amplitude \(T\), make the substitution \(z=\omega t\) in the resulting expression. Its contribution to \(A(t)\), divided by \(t^{1+\alpha}\), tends by dominated convergence to
\[
-\frac{2u}{\pi}\,2T\Gamma(1+\alpha)\sin(\pi\alpha/2)
\int_0^\infty \frac{\sin z-z}{z^{2+\alpha}}\,dz.
\]
Indeed, after rescaling the denominator is \([z^2+(1-u)^2t^2][z^2+(1+u)^2t^2]\), bounded below by \(z^4\). The integrand is dominated by a constant times \(z^{1-\alpha}\) near zero and \(z^{-1-\alpha}\) at infinity; both are integrable precisely for \(0<\alpha<2\). One integration by parts and the cosine-integral formula used in Step 1 give
\[
\int_0^\infty\frac{\sin z-z}{z^{2+\alpha}}\,dz
=-\frac{\pi}{2(1+\alpha)\Gamma(1+\alpha)\sin(\pi\alpha/2)}.
\]
Thus the single-bath leading contribution is \(2uTt^{1+\alpha}/(1+\alpha)\) for the first bath and its negative for the second. Because the two exponents are distinct, the smaller exponent dominates, giving exactly the displayed alternatives. This asymptotic is nonzero, so \(A(t)\ne0\) for all sufficiently small \(t>0\).

**4. Irreversibility.** For a stationary real Gaussian vector process, path time reversibility implies \(C_{xy}(t)=C_{yx}(t)\) at every lag (and conversely all covariance symmetry conditions suffice). The short-lag inequality just proved rules out time reversibility of the stationary observed position process. No entropy-production formula is needed.

## Verification

The included standalone script `verify_fractional_gyrator.py` computes (2) independently from convergent real-frequency quadrature, checks its agreement with the beta-integral expression for several distinct fractional pairs, and checks the positive/negative short-lag cusp predictions by a cancellation-stable integral with the exact linear term removed. These finite checks test normalization and signs; the all-parameter theorem rests on the analytic proof above, not finite sampling.

## Relationship to prior work

Squarcini, Solon, Viot and Oshanin (2022) introduced this fractional-Gaussian gyrator and computed equal-time covariance, currents, and mean angular velocity. In particular, their expression for mean angular velocity and its weak-coupling cancellation motivate the zero-circulation setting. The novelty assessed here is **not** the fractional-gyrator model, its stationary current formulas, or the existence of cancellation: it is the rigorously evaluated two-time, zero-instantaneous-circulation fractional cusp and its exact exponent and coefficient. The white-noise spectral analysis of Cerasoli and collaborators (2022) addresses a different bath class; Nascimento and Morgado (2020) analyze finite-memory thermal reservoirs with matched fluctuation-dissipation structure; Viot and collaborators (2023) analyze finite-increment rotational fluctuations in the conventional Brownian gyrator. None of those cited results was found to state the calibrated fractional-Gaussian cusp. General spectral Abelian theorems may imply the analytic asymptotic after nontrivial specialization; independent priority verification remains outstanding.

## Limitations

The theorem requires distinct exponents strictly between zero and two, independent Gaussian baths, linear stable trapping, and stationary initialization. It establishes only sufficiently short positive-lag chronology and does not classify the sign at arbitrary lag, entropy production, or estimation accuracy under discrete noisy sampling. The circulation is specifically \(A'(0^+)\), the mean signed-chord derivative; do not conflate it with a pathwise instantaneous angular velocity for rough fractional trajectories. Numerical experiments alone do not prove the small-lag limit. Broader published fractional-Gaussian irreversibility theory could potentially subsume the specialization and is a residual originality risk.

## References

1. A. Squarcini, A. Solon, P. Viot and G. Oshanin, *Fractional Brownian Gyrator*, arXiv:2204.12145 (first publicly available 2022-04-26), https://arxiv.org/abs/2204.12145.
2. S. Cerasoli, S. Ciliberto, E. Marinari, G. Oshanin, L. Peliti and L. Rondoni, *Spectral fingerprints of non-equilibrium dynamics: The case of a Brownian gyrator*, arXiv:2201.04903 (2022), https://arxiv.org/abs/2201.04903.
3. E. dos S. Nascimento and W. A. M. Morgado, *Stationary properties of a Brownian gyrator with non-Markovian baths*, arXiv:2002.07254 (2020), https://arxiv.org/abs/2002.07254.
4. P. Viot, A. Argun, G. Volpe, A. Imparato, L. Rondoni and G. Oshanin, *Destructive effect of fluctuations on the performance of a Brownian gyrator*, arXiv:2307.05248 (2023), https://arxiv.org/abs/2307.05248.
