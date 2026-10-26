# Unique small-amplitude vaccine-pulse phase for a seasonal SEIRS invasion exponent

## Finding

For a seasonal SEIRS model with one annual susceptible-only instantaneous vaccination pulse, the unique invasion-minimizing phase, for sufficiently weak positive seasonality and sufficiently small pulse strength, has the universal leading form
\[
\boxed{\tau_{\min}=-\frac{1}{\omega}\arctan\!\left(\frac{\omega}{b+\delta}\right)+O(\epsilon+\eta)\pmod T.}
\]
Here the transmission maximum is at time zero, \(T=2\pi/\omega\), \(\epsilon>0\) is sinusoidal transmission amplitude, and \(\eta>0\) is the vaccinated proportion of susceptibles at each pulse. Thus the campaign occurs between zero and one quarter-period *before* peak transmission. The leading phase does not depend on exposed-stage progression, infectious-stage recovery, mean transmission, or newborn vaccination coverage. This independence concerns the optimizing phase, not the size of the epidemic-invasion reduction.

More precisely, let \(\Lambda(\epsilon,\eta,\tau)\) denote the principal per-unit-time Floquet exponent of the infected two-compartment linearization about the unique pulse-periodic disease-free orbit, and let \(\overline\Lambda\) denote its average over a uniform annual pulse phase. Define
\[
\begin{gathered}
 k=b+\delta,\qquad s_0=\frac{b(1-p)+\delta}{k},\qquad B=\alpha\beta s_0,\\
 g=\sqrt{(\alpha-\gamma)^2+4B},\qquad\vartheta=\arctan\!\left(\frac{\omega}{k}\right),\\
 K=\frac{\alpha\beta s_0}{gT\sqrt{k^2+\omega^2}}
 \left(1-\frac{2B}{g^2+\omega^2}\right)>0.
\end{gathered}
\]
Then, uniformly in the annual phase and with the first two phase derivatives,
\[
\boxed{\Lambda(\epsilon,\eta,\tau)-\overline\Lambda(\epsilon,\eta)
=-K\epsilon\eta\cos(\omega\tau+\vartheta)
+O\!\left(\epsilon\eta(\epsilon+\eta)\right).}
\]
For all sufficiently small positive \(\epsilon,\eta\), the exact exponent has exactly two critical phases on the annual circle, one strict global minimum and one strict global maximum. The maximizing phase is displaced from the minimizing one by \(T/2+O(\epsilon+\eta)\), where the error is in physical time. The sign \(K>0\) follows from \(g^2+\omega^2-2B=(\alpha-\gamma)^2+2B+\omega^2>0\).

## Assumptions and scope

Let \(s,e,i,r\geq0\) be fractions with \(s+e+i+r=1\). Between pulses the normalized equations are
\[
\begin{aligned}
\dot s&=b(1-p)+\delta r-\bigl(\beta(t)i+b\bigr)s,\\
\dot e&=\beta(t)si-(\alpha+b)e,\\
\dot i&=\alpha e-(\gamma+b)i,\\
\dot r&=bp+\gamma i-(\delta+b)r,\\
\beta(t)&=\beta[1+\epsilon\cos(\omega t)],\quad\omega=2\pi/T.
\end{aligned}
\]
All \(b,\delta,\alpha,\gamma,\beta,T\) are strictly positive, \(p\in[0,1]\), \(0\leq\epsilon<1\). Once per period at \(\tau+nT\), susceptible individuals are vaccinated instantaneously and transferred to immune status:
\[
(s,e,i,r)^+=((1-\eta)s^-,e^-,i^-,r^-+\eta s^-),\quad 0\leq\eta<1.
\]
There is no continuous vaccination rate between pulses and the exposed/infectious states do not jump at vaccination. Births and demographic turnover are already accounted for in normalized equations. The main asymptotic statement assumes both \(\epsilon\) and \(\eta\) tend independently to zero through positive values while all other parameters are held fixed; the implicit constants need not be uniform over different epidemiological parameter sets.

On the disease-free manifold \(e=i=0\), the susceptible fraction satisfies \(\dot s=c-ks\), with \(c=b(1-p)+\delta\), and has a unique positive globally attracting pulse-periodic orbit. Writing \(z\in[0,T)\) for time since the most recent pulse, this orbit is exactly
\[
s_\eta(z)=s_0\left(1-\frac{\eta e^{-kz}}{1-(1-\eta)e^{-kT}}\right).
\]
At zero pulse strength it reduces to the constant \(s_0\). The infected variational system is
\[
\frac{d}{dt}\binom e i=
\begin{pmatrix}-(\alpha+b)&\beta(t)s_\eta(t-\tau)\\
\alpha&-(\gamma+b)\end{pmatrix}\binom e i.
\]
Its one-period fundamental matrix is strongly positive, so its spectral radius is simple and the real principal logarithmic growth rate \(\Lambda=T^{-1}\log\rho(\Phi(T))\) is well-defined. This is a local invasion rate and is not the nonlinear attack rate, finite-time infections, or resource-optimal physical vaccine allocation.

## Proof

**Disease-free orbit.** Solving the affine susceptible equation between pulses and composing it with \(s^+=(1-\eta)s^-\) gives the stated formula. The return map has strictly contractive slope \((1-\eta)e^{-kT}\), hence the unique attracting periodic orbit. Differentiating at zero pulse strength yields
\[
q(z):=\left.\partial_\eta s_\eta(z)\right|_{\eta=0}
=-\frac{s_0e^{-kz}}{1-e^{-kT}}.
\]
The fundamental first Fourier coefficient \(\widehat q_1=T^{-1}\int_0^Tq(z)e^{-i\omega z}\,dz\) is
\[
\widehat q_1=-\frac{s_0}{T(k+i\omega)}.
\]

**Scalar reduction and periodic Floquet branch.** Eliminating the exposed variable from the infectious equation gives
\[
\ddot i+(\alpha+\gamma+2b)\dot i+
\bigl[(\alpha+b)(\gamma+b)-\alpha\beta(t)s_\eta(t-\tau)\bigr]i=0.
\]
Set \(i(t)=e^{-(\alpha+\gamma+2b)t/2}u(t)\). Then
\[
\ddot u=\left[\frac{(\alpha-\gamma)^2}{4}
+\alpha\beta(1+\epsilon\cos(\omega t))s_\eta(t-\tau)\right]u.
\]
The principal positive Floquet solution has a periodic logarithmic derivative \(R=\dot u/u\). In coordinates \(z=t-\tau\) the Riccati equation is
\[
R'=\frac{(\alpha-\gamma)^2}{4}
+\alpha\beta[1+\epsilon\cos(\omega(z+\tau))]s_\eta(z)-R^2.
\]
At \(\epsilon=\eta=0\), \(R_0=g/2\). Since \(D+g\) is invertible on periodic functions, the periodic solution branch is analytic in the small amplitudes and in the phase, and coincides with the logarithmic derivative of the dominant positive Floquet solution. Consequently
\[
\Lambda=-\frac{\alpha+\gamma+2b}{2}+\frac1T\int_0^TR(z)\,dz.
\]
For discontinuous \(s_\eta\) at pulse times, this equation is solved on each open inter-pulse interval, with the continuous infected state and logarithmic derivative across the pulse. Keeping the pulse fixed at \(z=0\) makes the periodic coefficient a smooth parameter-dependent member of the same piecewise-smooth function space.

**Mixed sensitivity.** Write \(R=R_0+\epsilon R_\epsilon+\eta R_\eta+\epsilon\eta R_{\epsilon\eta}+\cdots\). Equating coefficients gives
\[
\begin{aligned}
(D+g)R_\epsilon &=B\cos(\omega(z+\tau)),\\
(D+g)R_\eta &=\alpha\beta q(z),\\
(D+g)R_{\epsilon\eta}
&=\alpha\beta q(z)\cos(\omega(z+\tau))-2R_\epsilon R_\eta.
\end{aligned}
\]
Using \(\widehat q_1\) and the fact that the first Fourier harmonics are divided by \(g\pm i\omega\) under \((D+g)^{-1}\), the period averages satisfy
\[
\begin{aligned}
\langle q\cos(\omega(z+\tau))\rangle
&=-\frac{s_0\cos(\omega\tau+\vartheta)}{T\sqrt{k^2+\omega^2}},\\
\langle R_\epsilon R_\eta\rangle
&=\frac{B\alpha\beta}{g^2+\omega^2}
\langle q\cos(\omega(z+\tau))\rangle.
\end{aligned}
\]
Averaging the mixed Riccati equation (the average of a derivative is zero) therefore gives
\[
\langle R_{\epsilon\eta}\rangle
=\frac{\alpha\beta}{g}
\left(1-\frac{2B}{g^2+\omega^2}\right)
\langle q\cos(\omega(z+\tau))\rangle
=-K\cos(\omega\tau+\vartheta).
\]

**Uniform remainder and unique optimizing phase.** When \(\epsilon=0\), shifting the pulse only translates an autonomous transmission problem; when \(\eta=0\), the pulse phase is irrelevant. Hence every nonconstant phase-dependent term of analytic \(\Lambda\) is divisible by \(\epsilon\eta\). Taylor expansion in a periodic \(C^2\)-phase norm gives the displayed uniform remainder. After dividing the phase-dependent exponent by \(K\epsilon\eta\), the resulting functions converge in \(C^2\) to \(-\cos(\omega\tau+\vartheta)\). For small amplitudes their first derivatives have no zeros away from disjoint neighborhoods of the two zeros of \(\sin(\omega\tau+\vartheta)\); their second derivatives have a fixed, opposite sign inside those neighborhoods. Thus there is precisely one critical point in each neighborhood, yielding exactly one strict global minimum and one strict global maximum, with the claimed leading phases.

## Verification

Run `python verify.py` with Python 3, NumPy and SciPy installed. It constructs the exact disease-free orbit, numerically integrates the two-dimensional infection fundamental matrix with a high-accuracy solver, and compares mixed finite differences at four phases against the explicit analytic mixed coefficient. It additionally tests the direction of strict phase separation at a positive small amplitude. Finite-dimensional numerical agreement is a consistency check, not a proof of the analytic uniform remainder or all-parameter theorem; those follow from the Riccati and implicit-function arguments above.

For the source's representative parameters \(b=0.02\), \(\delta=0.25\), \(\alpha=\gamma=100\), \(\beta=270\), \(p=0\), and \(T=1\), the asymptotic optimal phase is \(\tau_0\approx0.7568349749\pmod 1\), slightly after the rising-inflection phase \(0.75\). This comparison is **not** an exact prediction of its larger-amplitude pulse simulations; the numerical paper's campaign is a finite-duration pulse superimposed on a continuous baseline, unlike the instantaneous, no-baseline pulse analyzed here.

## Relationship to prior work

Gabrick and collaborators' 2024 open preprint `arxiv:2402.16883` derives the SEIRS seasonal equations and compares pulsed campaigns at selected phases, numerically favoring vaccination near the rising-transmission inflection. It does not derive the analytic two-amplitude infection Floquet coefficient or prove uniqueness of its optimum. The proposed statement explains the near-inflection phase **only in a carefully restricted weak-amplitude linear-invasion regime**, not their finite-amplitude nonlinear infection count.

Moneim and Greenhalgh (2005) derive periodic SEIRS threshold conditions for smooth periodic vaccination; they do not treat this local instantaneous-pulse phase-sensitivity calculation. Onyango and Müller (2014), and the related freely available Onyango–Müller–Kibet (2013) paper, explicitly optimize seasonal **SIR** vaccination using scalar infected thresholds and susceptible profiles. Their result warns against claiming the entire idea of optimal seasonal timing as new. The present SEIRS calculation is two-stage and proves an explicit stage-independent phase law despite a noncommuting infected Floquet matrix. Wang et al. (2019) optimize constrained time-varying SEIR vaccination through a different finite-horizon Pontryagin problem. Yan and Xiang (2014) establish SEIR impulsive extinction/persistence thresholds for saturating incidence, without establishing the sinusoidal small-pulse unique optimum. Gavish and Katriel (2026) analyze a distinct seasonally forced SIRVS optimization problem. The author's inability to inspect the 2014 Onyango–Müller full original paper and the 2019 Wang article completely is a publication-priority uncertainty, not mathematical evidence of noncoverage.

## Limitations

The result is local to the disease-free periodic orbit and requires both seasonality amplitude and vaccinated susceptible fraction to be sufficiently small; no explicit universal finite-amplitude cutoff is asserted. There is one pulse per period with constant perfect vaccine efficacy, no continuous susceptible vaccination between pulses, exponentially distributed exposed/recovery stages, identical seasonal contact for every exposed/infectious individual, constant population fractions, and homogeneous mixing. The limit does not optimize the **number of doses**, which depends on the pre-pulse susceptible fraction, nor nonlinear cumulative infections. The uniqueness proof is perturbative and need not hold for arbitrary forcing/pulse amplitudes. No assertion of independently validated publication priority is made.

## References

- Enrique C. Gabrick et al., *Impact of periodic vaccination in SEIRS seasonal model*, arXiv:2402.16883 (first public 2024-02-20), full preprint HTML https://arxiv.org/abs/2402.16883.
- Ismail Moneim and David Greenhalgh, *Use of a periodic vaccination strategy to control the spread of epidemics with seasonally varying contact rate*, Mathematical Biosciences and Engineering 2 (2005), 591–611, https://doi.org/10.3934/mbe.2005.2.591.
- Nelson O. Onyango and Johannes Müller, *Determination of optimal vaccination strategies using an orbital stability threshold from periodically driven systems*, Journal of Mathematical Biology 68 (2014), 763–784, https://doi.org/10.1007/s00285-013-0648-8.
- N. O. Onyango, J. Müller and S. K. Moindi, *Optimal Vaccination Strategies in an SIR Epidemic Model with Time Scales*, Applied Mathematics 4 (2013), 1–14, https://doi.org/10.4236/am.2013.410A2001.
- Mei Yan and Zhongyi Xiang, *Dynamic behaviors of an SEIR epidemic model in a periodic environment with impulse vaccination*, Discrete Dynamics in Nature and Society (2014), Article 262535, https://doi.org/10.1155/2014/262535.
- Xinwei Wang et al., *Optimal vaccination strategy of a constrained time-varying SEIR epidemic model*, Communications in Nonlinear Science and Numerical Simulation 67 (2019), 37–48, https://doi.org/10.1016/j.cnsns.2018.07.003.
- Nir Gavish and Guy Katriel, *Optimal Vaccination for Contagious Diseases with Seasonal Transmission*, Bulletin of Mathematical Biology (2026), https://doi.org/10.1007/s11538-026-01741-0.
