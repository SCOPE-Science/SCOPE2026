# Sharp strong-damping observability envelope for three-time oscillator sampling

## Finding

For a damped two-state rotational mode with known decay \(a>0\) and frequency \(\omega>0\), a single scalar output observed at the three equally spaced times \(0,h,2h\) has an exact determinant of the Fisher information matrix. Across **all** ratios \(\omega/a>0\) and all positive spacings, this determinant obeys a sharp universal envelope. The envelope constant is

\[
C_3=\max_{u>0}u^2\big(e^{-2u}+4e^{-4u}+e^{-6u}\big)
=0.2493790619596159528\ldots.
\]

The maximizer \(u_3=0.6312899580741505384\ldots\) is unique. For every \(a,\omega,h>0\),

\[
0\le\det G(h)<C_3\left(\frac{\omega}{a}\right)^2,
\]

and the constant is best possible, attained as a supremum in the strong-damping limit \(\omega/a\to0\). For all sufficiently small ratios \(\omega/a>0\), the exact three-time determinant has **one and only one global maximizing spacing**, satisfying

\[
h_*=\frac{u_3}{a}+c_3\frac{\omega^2}{a^3}
+O\!\left(\frac{\omega^4}{a^5}\right),
\qquad c_3=-0.2388090255494174146\ldots.
\]

The optimum itself has the two-term expansion

\[
\max_{h>0}\det G(h)
=C_3\left(\frac{\omega}{a}\right)^2
-K_3\left(\frac{\omega}{a}\right)^4
+O\!\left(\frac{\omega^6}{a^6}\right),
\qquad K_3=0.0839806238672237666\ldots.
\]

This is an exact design benchmark for recovering both unknown initial-state coordinates from three scalar observations of one damped rotational mode. The leading strong-damping information determinant is larger by the factor \(e^2 C_3=1.8426758787\ldots\) than the optimally spaced **two-observation** design with the same first observation at zero; this is a comparison of different sample budgets, not an equal-cost efficiency claim.

## Assumptions and scope

Let \(A,B\in\mathbb R\) be unknown deterministic initial-state coordinates, and \(a>0\) and \(\omega>0\) known. The measurements at \(t_j=jh\), for \(j\in\{0,1,2\}\), are

\[
Y_j=e^{-at_j}\big(A\cos(\omega t_j)+B\sin(\omega t_j)\big)+\eta_j.
\]

The errors \(\eta_j\) are independent with mean zero and common variance one; if likelihood-based Fisher information is intended, assume further that they are standard Gaussian. The \(3\times2\) design matrix \(H(h)\) has row \(j\) equal to \(e^{-ajh}(\cos(j\omega h),\sin(j\omega h))\). Then \(G(h)=H(h)^\top H(h)\) is the least-squares information/normal matrix, and in the Gaussian case the Fisher information matrix. With noise variance \(\sigma^2\), replace \(G\) by \(G/\sigma^2\) and every determinant by its value divided by \(\sigma^4\).

There is no assumption that this discrete decaying sinusoid is the trajectory of a second-order damped mechanical oscillator with a particular relation among its physical damping/frequency parameters. The claim is for a stable planar rotation generator with eigenvalues \(-a\pm i\omega\) and a fixed scalar output. The time-zero observation is prescribed; only the common positive spacing varies. No arbitrary-time, variable-budget, unknown-frequency, correlated-noise, or process-noise optimality is claimed.

## Proof

**1. Exact determinant.** The Cauchy--Binet identity for a \(3\times2\) matrix gives \(\det(H^\top H)\) as the sum of the squares of its three \(2\times2\) minors. The minor from rows \(i<j\) equals

\[
e^{-a(i+j)h}\sin((j-i)\omega h).
\]

Consequently, for every positive spacing,

\[
D(h):=\det G(h)
=e^{-2ah}\sin^2(\omega h)+e^{-4ah}\sin^2(2\omega h)
+e^{-6ah}\sin^2(\omega h).
\tag{1}
\]

All three terms are nonnegative. They vanish simultaneously precisely when \(\omega h\in\pi\mathbb Z\), so the sharp global lower bound is zero. The maximum over positive spacings is strictly positive, as proved next.

**2. Sharp global envelope.** Set \(u=ah\) and \(\varepsilon=\omega/a\), and write \(\Phi_\varepsilon(u)=D(u/a)/\varepsilon^2\). The strict inequality \(\sin^2 x<x^2\) for every real \(x\ne0\) yields

\[
0\le\Phi_\varepsilon(u)<g(u):=u^2(e^{-2u}+4e^{-4u}+e^{-6u})\le C_3.
\tag{2}
\]

For each fixed \(u>0\), \(\Phi_\varepsilon(u)\to g(u)\) as \(\varepsilon\to0\). This proves sharpness of \(C_3\) by choosing the maximizing \(u\). Because \(\Phi_\varepsilon\) is continuous, tends to zero at both boundaries, and is positive for some \(u>0\), its global maximum is positive and attained at a finite positive spacing. Even though \(\det G(h)\) may vanish at resonant spacings, the **maximum** is strictly positive.

**3. Unique envelope maximizer.** Put \(r=e^{-2u}\) and

\[
m(u)=\frac{1+8r+3r^2}{1+4r+r^2},\qquad
v(u)=\frac{4r(1+r+r^2)}{(1+4r+r^2)^2}.
\]

Direct differentiation gives \(g'(u)/g(u)=2(1/u-m(u))\) and \(m'(u)=-2v(u)\). For \(u>0\), \(1<m(u)<2\). Therefore \(g'(u)>0\) when \(0<u\le1/2\) and \(g'(u)<0\) for \(u\ge1\). The exact identity

\[
(1+4r+r^2)^2-12r(1+r+r^2)=(1-r)^4\ge0
\]

shows \(v(u)\le1/3\). Hence on \([1/2,1]\),

\[
\frac{d}{du}\left(\frac1u-m(u)\right)
=-\frac1{u^2}+2v(u)\le-\frac13<0.
\]

There is exactly one zero \(u_3\) of \(1/u-m(u)\), necessarily in \((1/2,1)\), and \(g''(u_3)<0\). The displayed equation uniquely defines \(u_3\) with no reliance on floating-point computation.

**4. Uniqueness of the actual high-damping design.** For \(\varepsilon>0\), \(\Phi_\varepsilon(u)\le g(u)\) and \(\Phi_\varepsilon\to g\) uniformly with derivatives up to any fixed order on compact intervals, by analytic sine expansion. Since \(g\to0\) at zero and infinity, the upper bound localizes every global maximizer of \(\Phi_\varepsilon\) to any prescribed neighborhood of \(u_3\) when \(\varepsilon\) is sufficiently small. On a small interval around \(u_3\), \(g''<0\); uniform derivative convergence implies \(\Phi_\varepsilon''<0\) there. Existence plus strict concavity then proves the global maximizer is unique.

**5. Two-term expansions.** On any fixed neighborhood of \(u_3\), Taylor expansion gives, uniformly together with its first two derivatives,

\[
\Phi_\varepsilon(u)=g(u)-\varepsilon^2 k(u)+O(\varepsilon^4),
\qquad k(u)=\frac{u^4}{3}(e^{-2u}+16e^{-4u}+e^{-6u}).
\tag{3}
\]

The stationarity equation and \(g''(u_3)<0\) yield by the implicit-function theorem

\[
u_*(\varepsilon)=u_3+\frac{k'(u_3)}{g''(u_3)}\varepsilon^2+O(\varepsilon^4).
\]

Since \(h_*=u_*(\varepsilon)/a\), this is the asserted spacing expansion with \(c_3=k'(u_3)/g''(u_3)\). Substituting the optimized \(u\) into (3), where the first-order displacement of \(g\) vanishes, gives \(C_3=g(u_3)\) and \(K_3=k(u_3)\). The quoted decimal values follow from the unique root equation with standard high-precision evaluation. Finally, the two-observation information determinant is \(e^{-2ah}\sin^2(\omega h)\); after the same normalization its limiting envelope is \(\max_{u>0}u^2e^{-2u}=e^{-2}\), uniquely attained at \(u=1\).

## Verification

Run \(\texttt{python3 verify.py}\) using the provided standalone standard-library script. It checks exact integer Cauchy--Binet identities, the exact polynomial identity in the uniqueness proof, the unique root bracket, the sharp constant/curvature, the sign and magnitude of the second-order correction, and independently evaluates the original normal matrix determinant versus (1). It also compares optimizing spacings at multiple small positive frequency-to-decay ratios with the asymptotic formula. Numerical tests check computational consequences; the infinite-parameter theorem and uniqueness use the explicit mathematical proof above, not the tests.

## Relationship to prior work

- Baran, Szák-Kocsis and Stehlík (2017, arXiv:1704.05719) prove D-optimal **time designs for a stationary complex Ornstein--Uhlenbeck process** with two-coordinate observations, correlated process noise and parameters consisting of stationary trend and/or process covariance parameters. Their trend Fisher determinant is \((1+\sum_j g_{\rm OU}(d_j))^2\), and their covariance-parameter formulas are different. In contrast, (1) is the information determinant for two **unknown deterministic initial coordinates** with known damping/frequency, **one scalar output** and independent observation noise; its Cauchy--Binet pair interactions are not an instance of the OU formulas. In particular, the source's joint covariance-parameter optimal scaled lag is about \(0.4930\), rather than the \(0.63129\ldots\) found here in a different statistical model.
- Siami and Jadbabaie (2020, arXiv:2005.03143) analyze sparse sensing/actuation schedules and multiplicative observability-Gramian approximation guarantees for general dynamics. Their spectral sparsification theorem does not determine the sharp three-observation objective, the limiting envelope constant, or the optimizer correction here.
- Calle and Bopardikar (2023, arXiv:2303.07903) provide covariance concentration bounds and sampling policies for randomly chosen sensors in Kalman filtering with process noise; those results do not specialize to an exact deterministic three-time design with known initial-state dynamics and no process noise.

These distinctions are comparisons of actual mathematical hypotheses and objective functions, not assertions that all D-optimal designs are new. The broader history of oscillatory experiment design may contain an unlocated equivalent calculation.

## Limitations

The exact information determinant vanishes at resonant spacings \(h=k\pi/\omega\) for positive integers \(k\); therefore the universal lower bound is zero. Only the optimal determinant is strictly positive.

The global optimizer is proved unique only for sufficiently strong relative damping; no explicit universal numerical cutoff is certified. No assertion is made about general irregular sampling, process-noise-correlated observations, unknown damping/frequency, or the optimization of other risk metrics. Constants are sharp for the restricted three-time design, not across all sensing strategies. The embedded checks rely on finite tests and numerical approximations for illustration, not as proofs of analyticity or uniqueness.

## References

1. S. Baran, C. Szák-Kocsis, M. Stehlík, *D-optimal designs for complex Ornstein--Uhlenbeck processes*, arXiv:1704.05719, first posted April 19, 2017. https://arxiv.org/abs/1704.05719
2. M. Siami, A. Jadbabaie, *A Separation Theorem for Joint Sensor and Actuator Scheduling with Guaranteed Performance Bounds*, arXiv:2005.03143, first posted May 6, 2020. https://arxiv.org/abs/2005.03143
3. C. I. Calle, S. D. Bopardikar, *A Concentration-Based Approach for Optimizing the Estimation Performance in Stochastic Sensor Selection*, arXiv:2303.07903, first posted March 14, 2023. https://arxiv.org/abs/2303.07903
