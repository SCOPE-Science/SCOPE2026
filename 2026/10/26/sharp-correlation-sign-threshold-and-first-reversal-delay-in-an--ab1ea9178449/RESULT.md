# Sharp correlation-sign threshold and first-reversal delay in an inertial run-and-tumble trap

## Finding

For a stationary inertial run-and-tumble particle in a one-dimensional harmonic trap, the two-time position autocovariance is **strictly positive at every nonnegative lag** unless the mechanical oscillator is underdamped and the direction-switching is faster than one-half of its mechanical amplitude-decay rate. In that latter regime the autocovariance changes sign infinitely often, although its integrated value remains positive. The transition is sharp, and the first sign reversal is delayed by an explicit inverse-distance law when the switching rate approaches its threshold from above.

More precisely, let the orientation flip independently at rate \(\rho>0\), with \(m,\gamma,\mu,a_0>0\), and put
\[
\beta=\frac{\gamma}{2m},\qquad k=2\rho,\qquad \Omega^2=\frac{\mu}{m}.
\]
For the unique stationary process, define \(C(t)=\mathbb E[X(t)X(0)]\) for \(t\geq0\). Then
\[
\boxed{\ C(t)>0\ \text{for every }t\geq0\quad\Longleftrightarrow\quad
\bigl(\gamma^2\geq4m\mu\bigr)\ \text{or}\ \bigl(\rho\leq\gamma/(4m)\bigr).\ }
\]
Here the second alternative also covers an underdamped oscillator with sufficiently slow switching. If \(\gamma^2<4m\mu\) and \(\rho>\gamma/(4m)\), there are infinitely many alternating positive and negative lag intervals.

In the underdamped case, write \(\omega=\sqrt{\Omega^2-\beta^2}>0\), and let \(t_1(k)\) be the first positive zero when \(k>\beta\). At fixed \(\beta,\omega,a_0/m\),
\[
\boxed{\ t_1(k)=\frac{\log\!\left(\dfrac{2\sqrt{\beta^2+\omega^2}}{\sqrt{\omega^2+4\beta^2}}\right)}{k-\beta}+O(1),\qquad k\downarrow\beta.\ }
\]
The logarithm is strictly positive. The exact signed-correlation-area identity is
\[
\boxed{\ \int_0^\infty C(t)\,dt=\frac{a_0^2}{2\rho\mu^2}.\ }
\]
It is independent of inertia and friction, despite the sign-reversing lag bands above the threshold.

## Assumptions and scope

The particle obeys
\[
\dot X=V,\qquad m\dot V=-\mu X-\gamma V+a_0\sigma(t),
\]
where \(\sigma(t)\in\{-1,+1\}\) is a stationary, symmetric, two-sided continuous-time Markov chain with independent sign changes at rate \(\rho>0\). Hence \(\mathbb E[\sigma(t)\sigma(s)]=e^{-k|t-s|}\) with \(k=2\rho\). All coefficients \(m,\gamma,\mu,a_0,\rho\) are strictly positive. There is no additional thermal white noise or nonlinear force. Because the homogeneous oscillator has eigenvalues with strictly negative real parts, its causal convolution with the two-sided telegraph process defines the unique stationary position and velocity. Symmetry gives \(\mathbb E[X]=0\), so \(C\) is also the position autocorrelation without normalization.

The claim concerns two-time **stationary** covariance, not the single-time position variance, sample-path oscillations, or the nonstationary second moments initialized at the origin.

## Proof

**1. Stable convolution and the non-oscillatory regime.** Put \(f=a_0/m\). Let \(h\) be the causal impulse response of \(\partial_t^2+2\beta\partial_t+\Omega^2\), so \(X(t)=f\int_0^\infty h(s)\sigma(t-s)\,ds\). If \(\beta>\Omega\), then \(h(s)=e^{-\beta s}\sinh(\sqrt{\beta^2-\Omega^2}\,s)/\sqrt{\beta^2-\Omega^2}>0\) for \(s>0\). At \(\beta=\Omega\), \(h(s)=s e^{-\beta s}>0\). Therefore for every \(t\geq0\),
\[
C(t)=f^2\!\int_0^\infty\!\int_0^\infty h(s)h(u)e^{-k|t-s+u|}\,ds\,du>0.
\]
This proves the non-oscillatory part without any assumption on the flipping rate.

**2. Exact underdamped covariance.** Now suppose \(\beta<\Omega\), and write \(\omega=\sqrt{\Omega^2-\beta^2}\). Define
\[
D=(\beta+k)^2+\omega^2,\qquad E=(\beta-k)^2+\omega^2,\qquad A=\frac{f^2}{DE}>0.
\]
Stationary generator balance gives
\[
\mathbb E[X\sigma]=\frac{f}{D},\qquad
\mathbb E[V\sigma]=\frac{kf}{D},\qquad
\mathbb E[XV]=0,\qquad
C(0)=\frac{f^2(2\beta+k)}{2\beta\Omega^2D}.
\]
For \(t>0\), the Markov property of the sign chain gives \(\mathbb E[\sigma(t)X(0)]=f e^{-kt}/D\). Consequently
\[
C''(t)+2\beta C'(t)+\Omega^2C(t)=\frac{f^2}{D}e^{-kt},\qquad C'(0)=0.
\]
Solving this scalar initial-value problem yields
\[
\boxed{\ C(t)=Ae^{-kt}+e^{-\beta t}\bigl(B\cos(\omega t)+H\sin(\omega t)\bigr),\quad
B=C(0)-A,\quad H=\frac{kA+\beta B}{\omega}.\ }
\]
The oscillatory amplitude \(R=\sqrt{B^2+H^2}\) is nonzero, since simultaneous vanishing of \(B,H\) would imply \(kA=0\). Elementary algebra gives
\[
\frac RA=\frac{k\sqrt{[(k-\beta)^2+\omega^2][(k+\beta)^2+\omega^2]}}{2\beta\omega\sqrt{\beta^2+\omega^2}}.
\]

**3. Positivity for slow switching.** If \(k=\beta\), the preceding expression reduces to
\[
\frac RA=\frac{\sqrt{\omega^2+4\beta^2}}{2\sqrt{\omega^2+\beta^2}}<1.
\]
The positive exponential therefore strictly dominates the oscillation at every time.

For \(0<k<\beta\), set \(q=k/\beta\in(0,1)\), \(x=(\omega/\beta)^2>0\), \(a=(\beta-k)/\omega>0\), \(\theta=\omega t\), and write \(b=B/A\), \(h_*=H/A\). One obtains
\[
\frac{e^{\beta t}C(t)}A=e^{a\theta}+b\cos\theta+h_*\sin\theta,
\quad b=\frac{q(q^2+x-3)}{2(1+x)},\quad
h_*=\frac{q(q^2+3x-1)}{2\sqrt x(1+x)}.
\]
If \(h_*\geq0\), then \(x\geq(1-q^2)/3\). The sign of \(b^2+h_*^2-1\) is the sign of
\[
F_q(x)=(q^2-4)x^2+2(q^4+q^2-2)x+q^2(q^2-1)^2.
\]
For \(0<q<1\), this polynomial decreases strictly for \(x>0\), and
\[
F_q\!\left(\frac{1-q^2}{3}\right)=\frac49(q-2)(q-1)^2(q+1)^2(q+2)<0.
\]
Thus \(b^2+h_*^2<1\), whence \(e^{a\theta}+b\cos\theta+h_*\sin\theta>0\).

If \(h_*<0\), then \(b<0\). Let \(P=-b\), \(Q=-h_*\). The stationary variance identity gives \(0<P<1\), and direct subtraction gives
\[
2(1-q)(1+x)-q(1-q^2-3x)=(1-q)^2(q+2)+(q+2)x>0,
\]
so \(0<Q<a\). For any \(a\geq0\), \(0\leq P\leq1\), \(0\leq Q\leq a\), and \(\theta\geq0\),
\[
P\cos\theta+Q\sin\theta\leq e^{a\theta}.
\]
Indeed, reduce \(\theta\) modulo \(2\pi\): on the first quadrant use \(\cos\theta+a\sin\theta\leq e^{a\theta}\), obtained by differentiating \(e^{-a\theta}(\cos\theta+a\sin\theta)\); on the second use \(Q\sin\theta\leq a\leq e^{a\theta}\); on the third the trigonometric sum is nonpositive; on the fourth it is at most one. Periodicity and \(a\geq0\) finish the bound. Here the strict coefficient inequalities yield a strictly positive difference. This completes the all-lag positivity proof.

**4. Sign-changing regime and singular first delay.** For \(k>\beta\), choose a phase \(\phi\) so that
\[
e^{\beta t}C(t)=Ae^{-(k-\beta)t}+R\cos(\omega t-\phi).
\]
The nonzero oscillatory component dominates the vanishing exponential along arbitrarily late sequences of alternating cosine peaks and troughs. Continuity supplies infinitely many sign changes. As \(k\downarrow\beta\), the smooth ratio \(r(k)=R/A\) tends to
\[
r_0=\frac{\sqrt{\omega^2+4\beta^2}}{2\sqrt{\omega^2+\beta^2}}<1.
\]
For sufficiently small \(\varepsilon=k-\beta>0\), define \(T_\varepsilon=\varepsilon^{-1}\log(1/r(k))\). Before \(T_\varepsilon\), the exponential strictly dominates the oscillation; within the next full cosine period there is a negative trough. Hence
\[
T_\varepsilon\leq t_1(k)\leq T_\varepsilon+\frac{2\pi}{\omega}.
\]
Since \(\log(1/r(k))=\log(1/r_0)+O(\varepsilon)\), the claimed first-reversal asymptotic follows with a bounded remainder.

**5. Integrated covariance.** Integrating the exact three-term formula, or evaluating the zero-frequency spectral density, gives
\[
\int_0^\infty C(t)\,dt=\frac{f^2}{k\Omega^4}=\frac{a_0^2}{2\rho\mu^2}.
\]
The same identity holds in the non-oscillatory regime by the stable-filter zero-frequency gain and the telegraph covariance integral. All steps are exact for every admissible strictly positive parameter.

## Verification

The supplied standalone `verification.py` evaluates the closed form against an independent stationary three-dimensional Gaussian Ornstein–Uhlenbeck covariance calculation. This is valid for the two-time covariance because the Gaussian driver and the telegraph driver have the same mean and autocovariance, although their higher-order laws differ. It also checks a separate Fourier cosine integral for the spectral density, the explicit amplitude ratio, the sharp threshold inequalities, and first-zero brackets near the phase boundary. The script performs 200 random matrix comparisons (maximum relative discrepancy \(6.22\times10^{-15}\)), 35 spectral quadratures, 500 random all-lag positivity sweeps, and critical/overdamped tests. Numerical tests are corroboration and do not replace the analytical proof above.

For \(m=1\), \(\gamma=2\), \(\mu=2\), \(a_0=1.3\), the threshold is \(\rho_c=0.5\). At \(\rho=0.505\), the first covariance zero is approximately \(t_1=23.6974613845\). Its divergence coefficient when written in terms of \(k-\beta\) is approximately \(0.2350018146\).

## Relationship to prior work

Dutta, Kundu, Sabhapandit, and Basu, *Harmonically trapped inertial run-and-tumble particle in one dimension* (arXiv:2406.06120v1; Phys. Rev. E 110, 044107, 2024), establish the same physical model, its formal causal response, stationary position/velocity moments, and nonstationary second moments. The present result does **not** claim these prior formulas as new. Its added statement is the all-parameter sharp sign classification of the **stationary two-time position covariance** and the first-negative-lag boundary law; the source's time-dependent second moments at a single observation time do not themselves assert that classification.

Garcia-Millan and Pruessner, *Run-and-tumble motion in a harmonic potential: field theory and entropy production* (J. Stat. Mech. 063203, 2021), derive two-time correlations for an overdamped active particle, without the inertial complex-pole competition in the present theorem. Smith and Farago, *Nonequilibrium steady state for harmonically confined active particles* (Phys. Rev. E 106, 054118, 2022), analyze stationary spatial large deviations under short-correlated active forcing, rather than an all-lag correlation-sign threshold. Nguyen, Wittmann, and Löwen, *Active Ornstein–Uhlenbeck model for self-propelled particles with inertia* (arXiv:2108.14005v1), study the corresponding Gaussian colored-noise inertial oscillator, including harmonic-potential displacement statistics and damping regimes. Because its forcing has the same exponential two-time covariance after matching parameters, its linear-response calculations can reproduce the present covariance formula; **the covariance expression and damping eigenvalues are therefore not claimed as new**. In the harmonic-potential discussion and analytical appendix inspected, the authors do not formulate the sharp all-lag sign-positivity criterion or the inverse-distance first-zero law. The theorem's originality is restricted to those model-specific global classifications, including the nontrivial positivity boundary proof.

## Limitations

The theorem assumes a symmetric two-state Markov orientation, constant harmonic trapping, linear viscous damping, a strictly positive propulsion amplitude, and no independent white noise. Adding thermal noise contributes a second covariance and can alter the correlation-sign boundary. No statement is made about nonlinear trapping, non-Poisson switching, asymmetry, experimentally resolvable negative lobes, or higher-order multi-time laws. An unlocated earlier analysis of colored-noise oscillator covariance might imply the same phase boundary; therefore originality remains subject to external verification. A mathematical proof of the sign classification does not identify who first observed it in the wider oscillator literature.

## References

1. D. Dutta, A. Kundu, S. Sabhapandit, and U. Basu, *Harmonically trapped inertial run-and-tumble particle in one dimension*, arXiv:2406.06120v1 (posted 10 June 2024), Phys. Rev. E **110**, 044107 (2024). https://arxiv.org/html/2406.06120v1 ; https://doi.org/10.1103/PhysRevE.110.044107
2. R. Garcia-Millan and G. Pruessner, *Run-and-tumble motion in a harmonic potential: field theory and entropy production*, J. Stat. Mech. **2021**, 063203. https://doi.org/10.1088/1742-5468/ac014d
3. N. R. Smith and O. Farago, *Nonequilibrium steady state for harmonically confined active particles*, Phys. Rev. E **106**, 054118 (2022). https://doi.org/10.1103/PhysRevE.106.054118
4. G. H. P. Nguyen, R. Wittmann, and H. Löwen, *Active Ornstein–Uhlenbeck model for self-propelled particles with inertia*, arXiv:2108.14005v1 (31 August 2021), J. Phys.: Condens. Matter **34**, 035101 (2022). https://arxiv.org/pdf/2108.14005 ; https://doi.org/10.1088/1361-648X/ac2c3f
