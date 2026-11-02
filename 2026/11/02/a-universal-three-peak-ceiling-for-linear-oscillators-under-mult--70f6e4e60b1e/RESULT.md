# A universal three-peak ceiling for linear oscillators under multiscale colored forcing

## Finding

**Theorem (spectral-mode ceiling, sharp for arbitrarily many positive relaxation channels).** Let \(m\ge 1\), \(\gamma>0\), \(\omega_0>0\), and \(A_j,\nu_j>0\) for \(1\le j\le m\). Consider the stable linear oscillator
\[
\ddot X(t)+2\gamma\dot X(t)+\omega_0^2X(t)=F(t),
\]
with a mean-zero, second-order stationary forcing whose covariance is
\[
\operatorname{Cov}(F(t),F(0))=\sum_{j=1}^m A_j e^{-\nu_j|t|}.
\]
Its stationary two-sided displacement power spectrum has **at most two distinct positive stationary frequencies** and **at most one nonzero local-maximum frequency**. Consequently the spectrum has **at most three local maxima on the whole real frequency axis**, one at zero and one symmetric pair; it cannot have two distinct pairs of off-center resonances. The ceiling is sharp already for \(m=1\), and it remains sharp with any prescribed finite number of distinct positive-rate channels by sufficiently small positive perturbations.

This statement holds for non-Gaussian forcing with the specified covariance as well as for independent Ornstein–Uhlenbeck components. It is a constraint on the stationary displacement power spectrum, not on the number of force components or on transient oscillations.

An exact mode classifier is furnished by \(G\) below. When \(G(0)<0\), precisely three maxima occur if and only if \(G\) becomes positive somewhere on \((0,\infty)\); otherwise the central maximum is the sole maximum (with possible stationary shoulders at equality). When \(G(0)>0\), precisely the two symmetric off-center maxima occur and zero is a strict local minimum. If \(G(0)=0\), the sign of \(G'(0)\) determines the alternative: positive gives two off-center maxima, while nonpositive gives only the central maximum.

## Assumptions and scope

All frequencies and rates are finite positive real numbers. The \(m\) force components need not have distinct rates; the coefficients \(A_j\) are strictly positive. The covariance model is positive definite and includes sums of independent Ornstein–Uhlenbeck or symmetric telegraph forces. We use the Fourier convention \(S_F(\omega)=\int_{-\infty}^{\infty}e^{-i\omega t}\operatorname{Cov}(F(t),F(0))\,dt\), without division by \(2\pi\). Since \(\gamma,\omega_0>0\), the oscillator has a unique stable stationary linear-filter solution of finite variance.

Set \(a_j=2A_j\nu_j>0\), \(t_j=\nu_j^2>0\), \(z=\omega^2\), and
\[
B(z)=\sum_{j=1}^m\frac{a_j}{z+t_j},\qquad P(z)=z^2+cz+d,
\quad c=4\gamma^2-2\omega_0^2,\quad d=\omega_0^4.
\]
For all \(z\ge0\), \(P(z)=(\omega_0^2-z)^2+4\gamma^2z>0\). The spectrum is \(S_X(\omega)=B(\omega^2)/P(\omega^2)\).

## Proof

The Fourier transfer function is \((\omega_0^2-\omega^2+2i\gamma\omega)^{-1}\). A single exponential covariance has Fourier transform \(2A_j\nu_j/(\nu_j^2+\omega^2)\). Positivity and linearity therefore give the displayed stationary spectrum. Let \(f(z)=B(z)/P(z)\) and
\[
G(z)=P(z)B'(z)-P'(z)B(z).
\]
Then \(f'(z)=G(z)/P(z)^2\), and \(S_X'(\omega)=2\omega f'(\omega^2)\) for \(\omega>0\).

If \(c\ge0\), both \(P'(z)=2z+c\ge0\) and \(B'(z)<0\), so \(G(z)<0\) for all \(z\ge0\): there is only the central peak.

Suppose \(c<0\). Differentiating cancels the mixed terms:
\[
G'(z)=P(z)B''(z)-2B(z)
=2\sum_j\frac{a_j}{(z+t_j)^3}\,[d+cz-2zt_j-t_j^2].
\]
Define \(Z(z)=\sum_j a_j/(z+t_j)^3>0\), and probability weights \(p_j(z)=a_j/((z+t_j)^3 Z(z))\). Thus
\[
\frac{G'(z)}{2Z(z)}=H(z):=d+cz-2z\mathbb E_z[t]-\mathbb E_z[t^2].
\]
As \(z\) increases, \(p_j(z)\) shifts monotonically toward larger \(t_j\). Indeed, for every nondecreasing \(h\),
\[
\frac{d}{dz}\mathbb E_z[h(t)]
=-3\operatorname{Cov}_z\!\left(h(t),\frac1{z+t}\right)\ge0,
\]
since \(h\) is nondecreasing and \(1/(z+t)\) is decreasing. Both \(\mathbb E_z[t]\) and \(\mathbb E_z[t^2]\) are nondecreasing. Because \(c<0\), \(H(z)\) is **strictly decreasing** for \(z\ge0\). Therefore \(G'\) changes sign at most once, and only from positive to negative. Hence \(G\) is nonincreasing or has exactly one strict maximum. On the other hand, writing \(a_\Sigma=\sum_j a_j>0\), the expansions \(B(z)=a_\Sigma z^{-1}+O(z^{-2})\), \(B'(z)=-a_\Sigma z^{-2}+O(z^{-3})\) give
\[
\lim_{z\to\infty}G(z)=-3a_\Sigma<0.
\]
A function with that negative limit and at most one increase-to-decrease turnover has at most two distinct positive zeros. Consequently \(f'\) can change sign from positive to negative at most once, giving at most one positive-frequency maximum. The signs of \(G(0)\), \(G'(0)\), and the maximum of \(G\) give the exact classifications stated above; a tangential zero of \(G\) is a stationary shoulder, not an extra maximum. Symmetry of \(S_X\) yields the stated peak ceiling.

For sharpness take \(m=1\), \(\omega_0=1\), \(\gamma=1/10\), \(\nu_1=1/10\), and any \(A_1>0\). The two positive roots of \(G\) are the roots of
\[
3z^2-\frac{39}{10}z+\frac{2451}{2500}=0,
\]
namely \(z_-=0.34064583403483967\ldots\) and \(z_+=0.9593541659651603\ldots\). The spectrum has strict local maxima at \(\omega=0\) and \(\omega=\pm\sqrt{z_+}\), separated by strict local minima at \(\omega=\pm\sqrt{z_-}\). Each extremum is nondegenerate, so adding any finite number of sufficiently weak positive components with distinct rates preserves the three-peak pattern by continuity.

## Verification

Run `python verify_spectral_bound.py` with NumPy and SciPy. The program independently constructs the first-order stochastic state-space transfer matrix and compares its frequency-domain displacement spectrum with the sum-of-Lorentzians formula. It checks the monotone normalized derivative \(H\), counts sampled positive critical points for random parameter sets, and verifies the explicit sharp example. This finite computation does not establish the all-parameter theorem; that is the analytical proof above.

## Relationship to prior work

Masoliver and Porrà (1993) derived spectra for linear oscillators under **a single exponential force covariance** and explicitly classified their one-, two-, and three-peak regimes, including the Ornstein–Uhlenbeck case. The existence of three peaks for one rate, the transfer function, and the elementary single-rate spectral formula are **not new claims here**. Their published single-rate formulas do not logically establish a peak bound for arbitrary sums: a positive sum of functions, each with one off-center peak, need not in general preserve the number of maxima. The new argument uses the joint Stieltjes structure of all rates and proves a universal bound independent of the channel count.

Milotti (1995) investigates mixtures of relaxation rates and \(1/f\)-type noise spectra, but does not furnish this filtered-oscillator peak constraint. Grahovac and collaborators (2016) study superpositions of Ornstein–Uhlenbeck-type processes and intermittency, rather than the number of displacement spectral maxima after a second-order stable filter. Both help motivate heterogeneous noise, not a prior derivation of this bound. The result is also distinct from multi-resonance effects of coupled oscillators, because there is only one mechanical degree of freedom.

## Limitations

The conclusion requires a passive linear scalar oscillator, strictly positive damping and stiffness, and a nonnegative mixture of exponential force covariance channels. Oscillatory or sign-changing covariance kernels, correlated forces with signed cross-spectra, nonlinear oscillators, coupled mechanical modes, and extra independent measurement noise are outside the theorem. The result is about the *ensemble stationary power spectrum*, not finite-sample estimated periodograms. Literature priority is provisional pending comprehensive expert examination; a missing textual match is not proof of novelty. No independent scientific audit has been conducted.

## References

1. J. Masoliver and J. M. Porrà, "Harmonic oscillators driven by colored noise: Crossovers, resonances, and spectra," *Physical Review E* 48, 4309–4319 (1993), DOI: 10.1103/PhysRevE.48.4309; open repository https://hdl.handle.net/2445/18797.
2. E. Milotti, "Linear processes that produce 1/f or flicker noise," *Physical Review E* 51, 3087 (1995), DOI: 10.1103/PhysRevE.51.3087.
3. D. Grahovac, N. Leonenko, A. Sikorskii, and I. Tesnjak, "Intermittency of superpositions of Ornstein–Uhlenbeck type processes," *Journal of Statistical Physics* 165 (2016), DOI: 10.1007/s10955-016-1616-7, open accepted version https://orca.cardiff.ac.uk/id/eprint/94423/.
