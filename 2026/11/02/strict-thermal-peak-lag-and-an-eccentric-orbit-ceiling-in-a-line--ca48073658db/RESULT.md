# Strict thermal-peak lag and an eccentric-orbit ceiling in a linear radiative proxy

## Finding
For every Keplerian eccentricity \(0<e<1\), a globally averaged, **linear first-order** orbital heating response has exactly one peak in the outgoing half-orbit, and that peak occurs strictly later for every increase in the response time constant. Its peak phase continuously and bijectively covers an explicit interval \((0,M_e)\), where \(M_e<\pi/2\). Thus a peak lag determines a unique response time constant in this specified proxy, and can never reach one-quarter of an orbital period, even as the response time tends to infinity. This is a theorem about a linear response proxy, **not** about a nonlinear atmospheric temperature, a rotating hot spot, or an observed disk-integrated light curve.

Write
\[
E_e=\arccos\!\left(\frac{1-(1-e^2)^{1/4}}{e}\right),\qquad
M_e=E_e-e\sin E_e.
\]
For the periodic response described below, if \(m_e(\theta)\) is the angular location of the unique maximum after periastron, then
\[
0<m_e(\theta_1)<m_e(\theta_2)<M_e<\frac\pi2
\quad\text{whenever}\quad0<\theta_1<\theta_2,
\]
with \(m_e(\theta)\to0\) as \(\theta\downarrow0\) and \(m_e(\theta)\to M_e\) as \(\theta\to\infty\). In particular, \(\theta\mapsto m_e(\theta)\) is a strictly increasing bijection from \((0,\infty)\) to \((0,M_e)\).

## Assumptions and scope
Take a bound elliptic Kepler orbit with eccentricity \(0<e<1\), mean motion \(n>0\), orbital period \(P=2\pi/n\), and periastron at mean anomaly \(M=0\). For each \(M\in\mathbb R/(2\pi\mathbb Z)\), let the eccentric anomaly \(E(M)\) be the unique solution of Kepler's equation \(M=E-e\sin E\), modulo \(2\pi\). Set the dimensionless globally averaged inverse-square stellar forcing
\[
f_e(M)=(1-e\cos E(M))^{-2}.
\]
For a positive physical relaxation time \(\tau\), let \(\theta=n\tau>0\). The output \(y_\theta\) is the unique \(2\pi\)-periodic solution of
\[
\theta\,\frac{dy_\theta}{dM}+y_\theta=f_e(M).
\]
The output is a normalized **linear** thermal/energy-balance proxy. There is no longitudinal advection, nonlinear Stefan–Boltzmann cooling, atmospheric circulation, phase-dependent viewing geometry or transient initial condition in the theorem. The maximum concerns the stationary periodic output, not a pass-band light curve.

## Proof
**1. Orbital forcing and its mean.** Differentiate Kepler's equation: \(dM/dE=1-e\cos E>0\). On \((0,\pi)\), \(df_e/dM=-2e\sin E/(1-e\cos E)^4<0\); the forcing is strictly increasing on \((\pi,2\pi)\), with unique global maximum at \(M=0\) and minimum at \(M=\pi\). It is even about periastron. Integrating with \(dM=(1-e\cos E)dE\) gives
\[
\mu_e=\frac1{2\pi}\int_0^{2\pi}f_e(M)\,dM=\frac1{\sqrt{1-e^2}}.
\]
The strictly decreasing half-orbit crosses this mean exactly once. Solving \(f_e(M_e)=\mu_e\) yields the stated \(E_e,M_e\), with \(0<E_e<\pi/2\) and therefore \(0<M_e<\pi/2\).

**2. Existence and uniqueness of the peak.** The periodic solution is the positive, normalized convolution
\[
y_\theta(M)=\frac1{\theta(1-e^{-2\pi/\theta})}
\int_0^{2\pi} e^{-s/\theta}f_e(M-s)\,ds.
\]
Hence \(f_e(\pi)<y_\theta(M)<f_e(0)\) for every \(M\). Put \(q_\theta=y_\theta-f_e\). Its differential equation is
\[
q_\theta'+\theta^{-1}q_\theta=-f_e'.
\]
We have \(q_\theta(0)<0\), \(q_\theta(\pi)>0\). At every zero of \(q_\theta\) in \((0,\pi)\), its derivative equals \(-f_e'>0\), so there is exactly one zero (any second zero would require a non-upward crossing). The response derivative is \(y_\theta'=-q_\theta/\theta\): this zero is its unique maximum. The same argument on \((\pi,2\pi)\), where \(f_e'>0\), gives the unique minimum. Because the maximum exceeds the orbital mean \(\mu_e\) strictly and at the maximum \(y_\theta=f_e\), its location satisfies \(m_e(\theta)<M_e\).

**3. Strict monotonicity with relaxation time.** Let \(G_\theta=(I+\theta D)^{-1}\) denote the positive periodic convolution operator in step 2. For \(0<\theta_1<\theta_2\), the elementary resolvent identity gives
\[
G_{\theta_2}=
\frac{\theta_1}{\theta_2}G_{\theta_1}+
\left(1-\frac{\theta_1}{\theta_2}\right)G_{\theta_2}G_{\theta_1}.
\]
Set \(y_j=G_{\theta_j}f_e\), and let \(m_1\) be the unique maximum of \(y_1\). Since \(y_1\) is nonconstant and \(G_{\theta_2}\) is a strictly positive averaging operator, \((G_{\theta_2}y_1)(m_1)<y_1(m_1)\). The identity implies \(y_2(m_1)<y_1(m_1)=f_e(m_1)\), so \(y_2'(m_1)>0\). As \(m_1\in(0,\pi)\), step 2 forces \(m_1<m_e(\theta_2)\). This proves strict monotonicity without truncating the Kepler forcing to a single sinusoid.

**4. Exact endpoint limits and invertibility.** The positive kernel becomes an approximate identity as \(\theta\downarrow0\), hence \(y_\theta\to f_e\) uniformly and the unique maxima converge to \(M=0\). As \(\theta\to\infty\), the periodic kernel converges uniformly to the constant \(1/(2\pi)\), so \(y_\theta\to\mu_e\) uniformly. At every maximum \(f_e(m_e(\theta))=y_\theta(m_e(\theta))\). The unique decreasing-half-orbit solution of \(f_e(M)=\mu_e\) is \(M_e\), so the maximum converges to \(M_e\). Smoothness and transversality at the maximum give continuity; strict monotonicity and both limits prove the bijection.

**5. Limiting rates (optional sharpening).** Because \(f_e\) is smooth and \(f_e''(0)<0\), expansion of \((I+\theta D)^{-1}\) yields \(m_e(\theta)=\theta+O_e(\theta^2)\) as \(\theta\downarrow0\). For large \(\theta\), define the true anomaly \(\nu_e=2\arctan\bigl(\sqrt{(1+e)/(1-e)}\tan(E_e/2)\bigr)\). The mean-zero first correction \(y_\theta(M)=\mu_e+\theta^{-1}g_e(M)+O_e(\theta^{-2})\) satisfies \(g_e'=f_e-\mu_e\) and \(g_e(0)=0\), so \(g_e(M_e)=(\nu_e-M_e)/\sqrt{1-e^2}\). The maximum condition and \(f_e'(M_e)=-2e\sin E_e/(1-e\cos E_e)^4\) give
\[
M_e-m_e(\theta)=
\frac{(\nu_e-M_e)\sqrt{1-e^2}}{2e\sin E_e}\frac1\theta+O_e(\theta^{-2}).
\]
This positive coefficient quantifies the approach to the sharp but unattained ceiling.

## Verification
A standalone script, `verify_thermal_peak.py`, solves Kepler's equation by bounded bisection, constructs the periodic response independently by Fourier multipliers, and compares 32 peak locations for four eccentricities and eight dimensionless time constants. It verifies strict ordering, the exact orbital ceiling, and a finite-resolution differential-equation residual. It is a stress test only; steps 1–5 establish the continuum theorem. With \(e=1/2\), the exact ceiling is approximately \(0.9363956600\) radians of mean anomaly, corresponding to approximately \(0.1490319980P\); with \(e=0.9\), it is approximately \(0.3502685523\) radians, or \(0.0557469715P\). The bound is much tighter than a quarter-orbit for eccentric trajectories.

## Relationship to prior work
Iro and Deming's 2008 proceedings preprint and their 2010 atmospheric calculation treat time-dependent stellar heating on eccentric orbits, including numerically delayed thermal peaks. Cowan and Agol's 2010 preprint develops a nonlinear parcel-energy balance with re-radiation and atmospheric advection. These sources establish the scientific motivation and more elaborate models; neither inspected account states the present sharp monotone bijection or Keplerian mean-crossing ceiling for the isolated linear response. The strictly positive first-order low-pass convolution is classical. This finding claims neither its invention nor extension of the theorem to the nonlinear source models. Uninspected general peak-lag theorems in linear-systems literature remain a possible priority risk.

## Limitations
The result applies to a single scalar, constant-time-constant, periodic linear filter of globally averaged inverse-square forcing. The actual observed thermal phase peak depends on planetary rotation, wind transport, bandpass, emission law, visibility and depth-dependent, possibly variable radiative time; it can lie outside this idealized ceiling without contradicting the theorem. At large \(\theta\) the output modulation vanishes, so peak-time inversion becomes ill-conditioned even though it is structurally one-to-one. Circular orbits \(e=0\) have constant forcing, hence no unique peak and are excluded. No measurement-noise or inference-uncertainty statement is proved.

## References
1. N. Iro and D. Deming, *A time-dependent radiative model for the atmosphere of the eccentric transiting planets*, arXiv:0807.0266v1, posted 2008-07-02, https://arxiv.org/abs/0807.0266.
2. N. Iro and L. D. Deming, *A time-dependent radiative model for the atmosphere of the eccentric exoplanets*, arXiv:1001.1171, first posted 2010-01-07, https://arxiv.org/abs/1001.1171.
3. N. B. Cowan and E. Agol, *A Model for Thermal Phase Variations of Circular and Eccentric Exoplanets*, arXiv:1011.0428v1, posted 2010-11-01, https://arxiv.org/abs/1011.0428.
