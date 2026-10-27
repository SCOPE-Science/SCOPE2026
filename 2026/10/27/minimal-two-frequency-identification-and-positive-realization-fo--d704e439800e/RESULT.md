# Minimal two-frequency identification and positive realization for a two-layer climate energy-balance model

## Finding

For the positive four-parameter two-layer energy-balance system below, two *distinct positive* forcing frequencies and their exact **complex** surface-temperature response ratios are necessary and sufficient for global identification. In particular, the existence of a physically positive fit to two arbitrary measured phasors has an explicit if-and-only-if test: two ordered impedance increments are positive, and the resulting reconstructed radiative feedback and upper-layer heat capacity are positive. The four physical parameters are then unique. One frequency leaves a two-parameter family of positive fits; even adding equilibrium gain to that frequency leaves a one-parameter family. A quantitative perturbation bound identifies the ill-conditioning associated with small frequency contrasts.

## Assumptions and scope

The model uses upper-layer temperature anomaly \(T\), deep-layer anomaly \(U\), externally prescribed radiative forcing \(F\), and four strictly positive constant parameters \(C,C_D,\lambda,\gamma\):
\[
C\dot T=F-\lambda T-\gamma(T-U),\qquad C_D\dot U=\gamma(T-U).
\]
Here \(C,C_D\) are effective thermal capacities, \(\lambda\) is linear net radiative feedback, and \(\gamma\) is the exchange coefficient. The absolute magnitude and phase of the forcing are known. For each chosen angular frequency \(\omega_j>0\), measure the *steady-periodic* complex transfer ratio \(H_j=\widehat T_j/\widehat F_j\), with \(\widehat F_j\ne0\), relative to a common phase convention \(e^{i\omega_j t}\). Transient initial conditions are not part of the phasor data. Fix \(0<\omega_1<\omega_2\), and assume \(H_1,H_2\) are finite and nonzero complex numbers. No measurement noise or unknown instrument gain is included in the exact inverse theorem.

From each observed ratio compute real data
\[
R_j=\operatorname{Re}(H_j^{-1}),\qquad J_j=\frac{\operatorname{Im}(H_j^{-1})}{\omega_j},\qquad a=R_2-R_1,\quad b=J_1-J_2,\quad d=\omega_2^2-\omega_1^2.
\]

**Positive-realization theorem.** The phasors are the responses of one and only one model with all four parameters strictly positive if and only if \(a>0\), \(b>0\), and the two values \(\lambda,C\) reconstructed below are strictly positive. With \(\tau=b/a\), the unique reconstruction is
\[
\gamma=\frac{a(1+\omega_1^2\tau^2)(1+\omega_2^2\tau^2)}{\tau^2d},\qquad C_D=\gamma\tau,
\]
\[
C=J_1-\frac{\gamma\tau}{1+\omega_1^2\tau^2},\qquad
\lambda=R_1-\frac{\gamma\omega_1^2\tau^2}{1+\omega_1^2\tau^2}.
\]
The checks \(a>0,b>0\) alone do **not** guarantee positive \(C,\lambda\). Equivalently, the final two inequalities can be evaluated directly from the observations as
\[
J_1>\frac{a^2/b+\omega_2^2b}{d},\qquad
R_1>\frac{\omega_1^2(a+\omega_2^2b^2/a)}{d}.
\]

**Sharpness.** For any positive parameter tuple and any single positive observation frequency, an open two-dimensional family of positive parameter tuples has the same one-frequency complex response. If the equilibrium gain \(H(0)=1/\lambda\) is measured as well, a nontrivial one-dimensional positive family remains. Thus the two nonzero complex frequencies constitute a minimal scheme among schemes using at most one positive frequency, even if a zero-frequency datum is allowed.

**Conditioning of the recovered exchange time.** Suppose observed impedance components \(R_j,J_j\) are perturbed by at most \(\epsilon_R,\epsilon_J\), respectively, in absolute value for each \(j\). If \(a>2\epsilon_R\), then the perturbed ratio \(\widehat\tau=\widehat b/\widehat a\) is well defined whenever \(\widehat b>0\), and obeys
\[
|\widehat\tau-\tau|\le\frac{2\epsilon_J+2\tau\epsilon_R}{a-2\epsilon_R}.
\]
If \(\widehat b\) is not positive, the perturbed data fail the positive-realization test rather than defining a positive exchange time. This error estimate concerns impedance-component errors, not unprocessed temperature errors.

## Proof

**1. Harmonic transfer and strict stability.** The homogeneous dynamics matrix has trace \(- (\lambda+\gamma)/C-\gamma/C_D<0\) and determinant \(\lambda\gamma/(CC_D)>0\); both eigenvalues therefore have negative real part. Every nonzero harmonic forcing has a unique limiting steady-periodic response. Put \(\tau=C_D/\gamma\). For a complex forcing \(\widehat F e^{i\omega t}\), the second equation gives \(\widehat U=\widehat T/(1+i\omega\tau)\). Substitution into the first equation shows that \(H(i\omega)=\widehat T/\widehat F\) satisfies
\[
H(i\omega)^{-1}=\lambda+i\omega C+\frac{\gamma i\omega\tau}{1+i\omega\tau}.
\]
Consequently its measured impedance components are exactly
\[
R(\omega)=\lambda+\frac{\gamma\omega^2\tau^2}{1+\omega^2\tau^2},\qquad
J(\omega)=C+\frac{\gamma\tau}{1+\omega^2\tau^2}.
\]

**2. Necessity and inversion.** Subtracting the two frequencies yields
\[
a=\frac{\gamma\tau^2d}{(1+\omega_1^2\tau^2)(1+\omega_2^2\tau^2)},\qquad
b=\frac{\gamma\tau^3d}{(1+\omega_1^2\tau^2)(1+\omega_2^2\tau^2)}.
\]
All factors are positive, and \(b/a=\tau\). Solving the first difference for \(\gamma\), followed by either first-frequency real and imaginary equation, gives the displayed unique reconstruction. These equations prove necessity of every positivity test and global injectivity.

**3. Sufficiency and boundaries.** Conversely, assume the four stated strict inequalities. The formulas give \(\tau>0\), \(\gamma>0\), \(C_D>0\), \(C>0\), and \(\lambda>0\). Their constructed real and imaginary impedances equal \(R_1,J_1\) by definition; the difference identities then force \(R_2,J_2\) as well. Since the observed phasors are nonzero, equality of impedances is equality of the two complex transfers. Strict boundaries matter: \(a=0\) or \(b=0\) is impossible for a positive two-layer model at distinct positive frequencies; the limiting cases \(\gamma=0\), \(C_D=0\), and coincident frequencies belong outside the stated domain. The two direct observational inequalities follow by substituting \(\tau=b/a\) into the formulas for \(C\) and \(\lambda\).

**4. Why one harmonic, even with equilibrium gain, is insufficient.** Fix true one-frequency data \(R,J\) at angular frequency \(\omega>0\). For any nearby freely chosen positive pair \((\tau,\gamma)\), put
\[
C_D=\gamma\tau,\quad C=J-\frac{\gamma\tau}{1+\omega^2\tau^2},\quad \lambda=R-\frac{\gamma\omega^2\tau^2}{1+\omega^2\tau^2}.
\]
At the true pair these are strictly positive, so continuity preserves positivity throughout a neighborhood. Every such tuple has exactly the same observed complex response, giving two free dimensions. Even if \(\lambda\) is fixed externally from the equilibrium transfer, the continuum persists: freely perturb \(\tau\) and choose
\[
\gamma=\frac{(R-\lambda)(1+\omega^2\tau^2)}{\omega^2\tau^2},\quad
C=J-\frac{R-\lambda}{\omega^2\tau},\quad C_D=\gamma\tau.
\]
All reconstructed parameters remain positive for sufficiently small perturbations of the true \(\tau\). This proves the claimed one-dimensional ambiguity even with \(H(0)\).

**5. Conditioning.** Let \(\widehat a=a+\Delta a\), \(\widehat b=b+\Delta b\). The component error bounds imply \(|\Delta a|\le2\epsilon_R\) and \(|\Delta b|\le2\epsilon_J\). On \(a>2\epsilon_R\),
\[
\left|\frac{\widehat b}{\widehat a}-\frac ba\right|=\frac{|a\Delta b-b\Delta a|}{a|a+\Delta a|}\le\frac{2\epsilon_J+2\tau\epsilon_R}{a-2\epsilon_R}.
\]
No numerical experiment is needed for these universal claims.

## Verification

An exact rational witness is \((C,C_D,\lambda,\gamma)=(2,6,1,3)\), \((\omega_1,\omega_2)=(1,2)\), with inverse phasors \(H_1^{-1}=(17+16i)/5\) and \(H_2^{-1}=(65+80i)/17\). These give \(a=36/85\), \(b=72/85\), \(\tau=2\), hence the original four parameters exactly. This witness satisfies the strict positivity tests.

The standalone file `verify.py` independently implements the forward transfer and inverse formulas, checks this witness, runs 12,000 reproducible positive-parameter forward/inverse tests with frequencies chosen away from singular conditioning, and checks an explicit two-dimensional one-frequency ambiguity family. The tests are finite supplementary checks, not the proof of global uniqueness. The forward/inverse equations and their algebraic identities above are the universal certificate.

## Relationship to prior work

MacMynowski, Shin and Caldeira (2011) already present the two-box climate transfer function and fit frequency-domain responses of a coupled climate model across multiple forcing periods. This result does not claim discovery of the climate equations, sinusoidal forcing, or transfer functions. Geoffroy and colleagues (2013) solve and calibrate the two-layer model with step/ramp forcing and derive modal parameters. Soldatenko and Colman (2022) study the frequency-domain transfer and power-spectrum parameter sensitivities for the same two-box system. In the accessible primary material, none gives a two-*sample*, complex, positivity-preserving exact inverse with its realizability inequalities and one-tone/DC sharpness. Bortner and Sullivant (2021) give far more general *full input–output* local-identifiability criteria for RC networks; such structural identifiability is established work, not claimed as new. Their statement does not itself give the two discrete-frequency sampling formula or the strictly positive physical-data criterion for this climate parameterization. The result is also a special instance of reconstructing low-order passive rational transfer functions; general rational-interpolation literature may imply components of the argument.

## Limitations

The exact theorem needs perfectly known complex gain and phase at two distinct nonzero frequencies; magnitude-only spectra, an unknown radiative-input calibration, stochastic forcing, and parameter time variation lie outside its assumptions. The condition number worsens when frequencies are too close or ocean coupling is too weak, and the estimate above only controls the reconstructed exchange time from errors in the *inverse* transfer components. Measured real climate data need not fit a positive four-parameter two-box model. Model mismatch, climate sensitivity uncertainty, nonlinear feedback, efficacy corrections, uncertainty quantification, experimental forcing feasibility, and optimal frequency selection are not resolved. The full 2013 publisher article/appendices were not retrievable in this investigation; relevant indexed portions and independent full-text sources were compared. General rational-interpolation or RC-circuit results may contain a prior equivalent minimal-sampling statement. Historical priority has not been independently verified.

## References

1. MacMynowski, D. G., H.-J. Shin, and K. Caldeira (2011), *The frequency response of temperature and precipitation in a climate model*, Geophysical Research Letters **38**, L16711, doi:10.1029/2011GL048623. Public date: 2011-08-25. Sections 2–5 discuss sinusoidal forcing, complex transfer, and multi-frequency fitting.
2. Geoffroy, O., D. Saint-Martin, D. J. L. Olivié, A. Voldoire, G. Bellon, and S. Tytéca (2013), *Transient Climate Response in a Two-Layer Energy-Balance Model. Part I: Analytical Solution and Parameter Calibration Using CMIP5 AOGCM Experiments*, Journal of Climate **26**, 1841–1857, doi:10.1175/JCLI-D-12-00195.1. Published 2013-03-15.
3. Soldatenko, S. A., and R. A. Colman (2022), *Power Spectrum Sensitivity Analysis of the Global Mean Surface Temperature Fluctuations Simulated in a Two-Box Stochastic Energy Balance Model*, Tellus A, doi:10.16993/tellusa.40. Full open-access HTML, especially Sections 2.1–2.2.
4. Bortner, C., and S. Sullivant (2021), *Structural Identifiability of Series-Parallel LCR Systems*, arXiv:2107.06271, especially Theorem 1.1, Section 3 and Section 5 (RC duality and identifiability).
