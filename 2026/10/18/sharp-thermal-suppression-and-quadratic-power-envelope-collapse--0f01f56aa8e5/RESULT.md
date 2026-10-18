# Sharp thermal suppression and quadratic power-envelope collapse in a one-dimensional active bath

## Finding

For a dilute, ideal one-dimensional bath of particles moving at propulsion speed \(v>0\), isotropically redrawing their velocity sign at rate \(\alpha>0\), and undergoing independent translational Brownian diffusion of strength \(D>0\), consider the leading weak-potential mechanical power imparted to a probe moving steadily at speed \(V\). Let the real probe interaction potential \(U\) be a Schwartz function. If \(P_U^{[2]}(V)\) denotes the coefficient of squared potential strength, the following is a sharp all-probe classification:

\[
\exists\, U\in\mathcal S(\mathbb R),\ U\geq0,\ P_U^{[2]}(V)>0
\quad\Longleftrightarrow\quad
0<|V|<\sqrt{v^2-4\alpha D}.
\]

The right side requires \(D<D_c:=v^2/(4\alpha)\). If \(V^2+4\alpha D\geq v^2\), then \(P_U^{[2]}(V)\leq0\) for every real Schwartz potential, with strict inequality for every nonzero potential when \(V\ne0\). The complete negative-response band, for \(V^2+4\alpha D<v^2\), is \(q_-(V)<|q|<q_+(V)\), where

\[
q_\pm(V)=\frac{\sqrt{v^2-V^2}\,\pm\sqrt{v^2-V^2-4\alpha D}}{2D},
\qquad q_-(V)q_+(V)=\frac\alpha D.
\]

The product identity gives a distinguished geometric-center wave number \(\sqrt{\alpha/D}\) that works for every permitted speed.

There is also a quantitative sharp *power envelope*. Define

\[
\mathscr E(D)=\sup_{V\in\mathbb R}\ \sup_{\substack{U\in\mathcal S(\mathbb R;\mathbb R)\\\|U\|_{L^2}=1}}
\frac{P_U^{[2]}(V)}{\mu\rho_0},
\]

where \(\mu>0\) is bath-particle mobility and \(\rho_0>0\) is far-field bath density. This is a supremum of the *leading weak-potential coefficient*, not the finite-strength power. It is zero when \(D\ge D_c\). Writing \(\eta=1-D/D_c\), its exact critical law is

\[
\boxed{\ \mathscr E(D)=\frac{4\alpha^2}{9v^2}\,\eta^2\,[1+o(1)]\qquad(D\uparrow D_c).\ }
\]

Near the threshold, nearly optimal spectral packets concentrate at \(q_c=2\alpha/v\), and their probe velocities obey \(|V|/(v\sqrt\eta)\to1/\sqrt2\). The positive-power region therefore collapses simultaneously in velocity and wave number, while the maximal normalized transferable power vanishes *quadratically*.

## Assumptions and scope

A single freely moving bath particle has dynamics

\[
\mathrm dX_t=v\sigma_t\,\mathrm dt+\sqrt{2D}\,\mathrm dW_t,
\]

where \(W_t\) is standard Brownian motion independent of \(\sigma_t\in\{-1,+1\}\). At each event of a rate-\(\alpha\) Poisson clock, \(\sigma_t\) is replaced by an independent fair sign. Thus actual sign reversals occur at rate \(\alpha/2\), while the propulsion correlation decays at rate \(\alpha\). Initially the sign is stationary and uniform.

The probe translates at fixed velocity \(V\), and each bath particle feels the force \(-\mu\partial_x(\lambda U)\), with \(U\in\mathcal S(\mathbb R;\mathbb R)\) fixed and \(\lambda\) a small potential-strength parameter. The bath is ideal (noninteracting) with homogeneous number density \(\rho_0\); there is no backreaction changing the prescribed probe speed. The leading bath force is \(F_{\rm bath}(V)=\lambda^2F_U^{[2]}(V)+O(\lambda^3)\) for fixed potential and other parameters. Here \(P_U^{[2]}(V)=VF_U^{[2]}(V)\). The results concern the exact quadratic response coefficient, not the full interacting or strong-probe problem. The separate limit used for the power envelope keeps \(D>0\) fixed while taking the coefficient in \(\lambda\), then considers \(D\uparrow D_c\).

The Fourier convention is \(U_q=\int_{\mathbb R}e^{-iqx}U(x)\,\mathrm dx\), with Plancherel normalization \(\|U\|_{L^2}^2=\int_{\mathbb R}|U_q|^2\,\mathrm dq/(2\pi)\). All suprema are over actual Schwartz functions; they need not be attained, but are approached by Gaussian wave packets.

## Proof

**1. A direct resolvent calculation.** In a frame moving with the probe, linearizing the orientation-resolved stationary transport equations about the uniform bath gives a two-state Fourier system. Its diagonal elements are \(s+\alpha/2\pm iqv\), its off-diagonal elements are \(-\alpha/2\), and its spectral parameter is \(s=Dq^2-i\omega\), with the moving-probe frequency \(\omega=qV\). Averaging the inverse over the stationary signs yields exactly

\[
\mathcal G_D(q,\omega)=\frac{s+\alpha}{s(s+\alpha)+v^2q^2},\qquad s=Dq^2-i\omega.
\]

Equivalently, the stationary spatial density perturbation is \(\delta\rho_q=-\lambda\mu\rho_0q^2U_q\mathcal G_D(q,qV)\). This formula follows also by taking the Laplace transform of the independent Brownian convolution of the telegraph-particle displacement law; the direct two-state inverse independently fixes its normalization.

Set \(d=Dq^2\) and

\[
A=d^2+\alpha d+v^2q^2-\omega^2,\qquad B=(2d+\alpha)\omega.
\]

Complex division, with continuous extension through \(\omega=0\) at every \(q\ne0\), gives

\[
\mathcal K_D(q,\omega):=\frac{\Im\mathcal G_D(q,\omega)}\omega
=\frac{(\alpha+Dq^2)^2+\omega^2-v^2q^2}
{[D^2q^4+\alpha Dq^2+v^2q^2-\omega^2]^2+(2Dq^2+\alpha)^2\omega^2}.
\tag{1}
\]

For \(q\ne0\), the denominator is strictly positive for every real \(\omega\): when \(\omega\ne0\) its second summand is positive, and when \(\omega=0\) its first summand is strictly positive. The sign is therefore **exactly** the sign of the numerator.

**2. Mechanical-power sign and the sharp threshold.** The bath force is the integral of density against the derivative of the probe potential. Fourier pairing of \(q\) and \(-q\) gives

\[
P_U^{[2]}(V)=-\mu\rho_0V^2
\int_{\mathbb R}\frac{\mathrm dq}{2\pi}\,q^4|U_q|^2\mathcal K_D(q,qV).
\tag{2}
\]

At \(\omega=qV\), the sign numerator becomes

\[
N_V(q)=(\alpha+Dq^2)^2-(v^2-V^2)q^2.
\tag{3}
\]

Since \(\alpha+Dq^2\ge2\sqrt{\alpha D}\,|q|\), formula (3) is nonnegative for every wave number if \(V^2+4\alpha D\ge v^2\). Thus (2) cannot transfer positive power. At equality the response can vanish only at isolated nonzero wave numbers, so every nonzero Schwartz potential has strictly negative leading power for \(V\ne0\).

If \(V^2+4\alpha D<v^2\), then at \(q_0=\sqrt{\alpha/D}\),

\[
N_V(q_0)=\frac\alpha D\,(V^2+4\alpha D-v^2)<0.
\]

The quadratic inequality \(Dq^2-\sqrt{v^2-V^2}\,|q|+\alpha<0\) identifies precisely the open interval between the two stated roots. Their product is \(\alpha/D\). At fixed \(q\), the whole finite-frequency negative-response set satisfies

\[
|\omega|<\sqrt{v^2q^2-(\alpha+Dq^2)^2};
\]

it is nonempty exactly when \(D<D_c\). Its maximum frequency is \(\frac{v}{2D}\sqrt{v^2-4\alpha D}\), attained at \(q^2=(v^2-2\alpha D)/(2D^2)\).

**3. A nonnegative localized probe attaining positive leading power.** Fix a nonzero \(V\) satisfying the strict inequality, set \(q_0=\sqrt{\alpha/D}\), and define

\[
U_L(x)=e^{-x^2/(2L^2)}[1+\cos(q_0x)],\qquad L>0.
\]

This is smooth, nonnegative, and rapidly decaying. Its Fourier transform is three Gaussian packets centered at \(0,\pm q_0\). Write \(g(q)=q^4\mathcal K_D(q,qV)\). Since \(V\ne0\), the formula (1) shows \(g\) extends continuously to \(g(0)=0\); also \(g(q_0)<0\). Elementary Gaussian packet localization and negligible cross terms yield

\[
\int_{\mathbb R}\frac{\mathrm dq}{2\pi}|(U_L)_q|^2g(q)
=\frac{\sqrt\pi}{2}L\,g(q_0)+o(L).
\tag{4}
\]

The packet at zero gives \(o(L)\) because \(g(0)=0\); the packets at \(\pm q_0\) give the displayed term. Equation (4) is negative for all sufficiently large finite \(L\), so (2) is strictly positive. The limit \(L\to\infty\) is used only to establish existence of one finite smooth probe; any potential-strength limit is taken subsequently at that fixed \(L\).

**4. Exact variational power envelope.** For each fixed nonzero \(V\), Plancherel and arbitrary sharp Fourier localization show that the supremum over real Schwartz functions of unit \(L^2\) norm of the normalized power coefficient is the supremum over wave numbers of \(-V^2q^4\mathcal K_D(q,qV)\). Such localization uses two equal Fourier packets at opposite wave numbers; no delta distribution is treated as an admissible potential. If all modes are nonnegative, the supremum of nonpositive power over \(V\) is zero (attained at \(V=0\)). Therefore \(\mathscr E(D)=0\) when \(D\ge D_c\).

For \(D<D_c\), put \(\eta=1-D/D_c\), \(q_c=2\alpha/v\), and on every possible positive-power mode rescale

\[
q=q_c(1+\sqrt\eta\,z),\qquad V=v\sqrt\eta\,y.
\]

The exact root bounds from step 2 imply \(|y|<1\) and uniformly \(z=O(1)\) on the negative region. Direct expansion of the numerator and denominator in (1), uniform on that bounded region, gives

\[
\begin{aligned}
N_V(q)&=4\alpha^2\eta\,(z^2+y^2-1)+O(\eta^{3/2}),\\
A^2+B^2&=36\alpha^4+O(\sqrt\eta),\\
q^4&=16\alpha^4/v^4+O(\sqrt\eta).
\end{aligned}
\]

Thus, uniformly on candidate positive-power modes,

\[
-\frac{V^2q^4\mathcal K_D(q,qV)}{\eta^2}
=\frac{16\alpha^2}{9v^2}\,y^2(1-z^2-y^2)+o(1).
\]

In the limit the admissible region is the unit disk \(z^2+y^2\le1\), and \(y^2(1-z^2-y^2)\) has exact maximum \(1/4\), only at \(z=0\) and \(|y|=1/\sqrt2\). Choosing Fourier packets centered at these locations achieves the supremum asymptotically. The claimed coefficient \(4\alpha^2/(9v^2)\), quadratic exponent, and near-optimal speed/wave-number localization follow.

## Verification

The standalone script `verify.py` reconstructs the orientational resolvent independently from a two-by-two matrix and tests it against the closed expression at 72 parameter points. It checks the sharp velocity–diffusion sign criterion on 12 independent parameter pairs, verifies the nonnegative Gaussian-modulated probe with numerical Fourier quadrature for three widths, and checks the critical normalized envelope using direct numerical two-parameter maximization at five small values of \(\eta\). At the three smallest values \(\eta=0.01,0.003,0.001\), the ratio of optimized numerical power to the asymptotic prediction is approximately \(1.02088,1.00620,1.00206\). These finite checks corroborate algebra and normalization; the quantified statements about all potentials and the critical limit are proved analytically in the previous section.

Run with `python verify.py` in an environment with NumPy and SciPy. No external files are needed.

## Relationship to prior work

Woo, Choi and Rieger (2026), arXiv:2609.17047v1, derive the leading weak-probe response from free-particle trajectory statistics. Their equations (18), (20), (25) and Appendix A supply the general response framework and the diffusion-free one-dimensional run-and-tumble resolvent; their Section III.6 establishes a positivity-preserving smoothing relation for independent translational Brownian motion. These foundational results are **prior work**, not part of the novelty claim. The new statement extracts the finite-diffusion necessary-and-sufficient all-probe threshold, the speed-dependent wave-number bands and the sharp quadratic normalized power-envelope law. The generic response representation of the source mathematically determines the quantities analyzed here, but does not explicitly classify or optimize them at the thermal critical point.

Kim, Choe and Baek (2023/2024), arXiv:2304.01645, examine negative drag and spontaneous motion of penetrable symmetric objects in an ideal one-dimensional run-and-tumble gas under a negligible-thermal-noise assumption. Pei and Maes (2025/2026), arXiv:2504.03210, analyze velocity-dependent probe friction and noise in a run-and-tumble active medium without the present finite translational Brownian diffusivity threshold. The present theorem treats only the weak-potential, prescribed-speed ideal-bath response coefficient; it does not assert a finite-density, finite-coupling or autonomous-probe phase transition.

## Limitations

The diffusivity cutoff applies to the precise independent Brownian translational perturbation of the two-state complete-reset run-and-tumble process and to leading order in a weak localized probe potential. Interacting bath particles, state-dependent diffusivities, strong probes and the dynamics of a free probe may behave differently. The quantity \(\mathscr E(D)\) is optimized over potentials of fixed \(L^2\) norm at the response-coefficient level; maximizers are approached through increasingly narrow spectral packets and are not necessarily achieved by a fixed localized potential. A nonnegative probe demonstrates the sharp *existence* half of the classification, but the envelope coefficient optimizes over all real potentials, not just nonnegative ones. No assertion of experimental negative drag at finite coupling or uniform perturbative control over all packet widths is made. More abstract spectral-optimization principles could subsume parts of this explicit specialization.

## References

1. C.-U. Woo, J. Choi and H. Rieger, *Trajectory Statistics Govern Mechanical Power Transfer in Active Baths*, arXiv:2609.17047v1, submitted 2026-09-15. https://arxiv.org/html/2609.17047v1
2. K.-W. Kim, Y. Choe and Y. Baek, *Symmetry-breaking motility of penetrable objects in active fluids*, arXiv:2304.01645, first submitted 2023-04-04; Physical Review E 109 (2024), 014614. https://arxiv.org/abs/2304.01645
3. J.-H. Pei and C. Maes, *Transfer of active motion from medium to probe via the induced friction and noise*, arXiv:2504.03210, first submitted 2025-04-04; Physical Review Letters 136 (2026), 038301. https://arxiv.org/abs/2504.03210
