# Exact antiphase normal equation and quadratic combination forcing in a branched double pendulum

## Result

Consider the symmetric branched double pendulum of Toda and Ooshida, arXiv:2609.20688v1, in the coordinates
\[
\theta_m=\frac{\theta_2+\theta_3}{2},\qquad
\theta_d=\frac{\theta_2-\theta_3}{2},\qquad
\Delta_m=\theta_m-\theta_1.
\]
The child-exchange symmetry makes the in-phase set \(\theta_d=\dot\theta_d=0\) an exact invariant manifold. Along an arbitrary finite-amplitude trajectory \((\theta_1(t),\theta_m(t))\) on that manifold, an infinitesimal antiphase perturbation \(x=\delta\theta_d\) obeys the scalar normal variational equation
\[
\boxed{
M_2\ddot x+\kappa(t)x=0,
\qquad
\kappa(t)=G_2\cos\theta_m
+\mu\cos(\Delta_m)\dot\theta_1^{\,2}
-\mu\sin(\Delta_m)\ddot\theta_1 .
}
\]
No small-angle assumption is made on the in-phase base trajectory.

The in-phase equations themselves give a state-only expression
\[
\ddot\theta_1=
\frac{
2\mu M_2\sin\Delta_m\,\dot\theta_m^2
-M_2G_1\sin\theta_1
+2\mu^2\cos\Delta_m\sin\Delta_m\,\dot\theta_1^2
+2\mu G_2\cos\Delta_m\sin\theta_m
}{M_1M_2-2\mu^2\cos^2\Delta_m},
\]
so the normal coefficient can be evaluated without numerical differentiation whenever the mass matrix is nonsingular.

For a periodic in-phase base orbit this is a Hill equation. Its Wronskian is constant, hence the two transverse Floquet multipliers have product one. More generally the quadratic normal energy
\[
\mathcal E_N=M_2\dot x^2+\kappa(t)x^2
\]
satisfies the exact pumping identity
\[
\boxed{\dot{\mathcal E}_N=\dot\kappa(t)x^2.}
\]
Thus the onset of a small antiphase disturbance is a normal-stability problem for a parametrically modulated scalar oscillator, distinct from merely evaluating an approximate modal energy after growth has occurred.

## Exact obstruction to a release-point stiffness explanation

For the experimental release condition
\[
\theta_1(0)=A,\qquad \theta_m(0)=0,\qquad
\dot\theta_1(0)=\dot\theta_m(0)=0,
\]
the in-phase equations give
\[
\ddot\theta_1(0)=
-\frac{M_2G_1\sin A}{M_1M_2-2\mu^2\cos^2 A}
\]
and therefore
\[
\boxed{
\kappa(0;A)=G_2-
\frac{\mu M_2G_1\sin^2 A}
{M_1M_2-2\mu^2\cos^2 A}.
}
\]
Using the dimensions, masses, and inertias reported in arXiv:2609.20688v1 gives
\[
\begin{aligned}
M_1&=0.0181430108, & M_2&=0.00071071819,\\
\mu&=0.0012226491, & G_1&=0.664005546,\\
&&G_2&=0.0444229173,
\end{aligned}
\]
in SI units. On \(0<A<\pi/2\), the first zero of the release stiffness is
\[
\boxed{A_{\rm static}=84.4335888^\circ.}
\]
At the experimentally observed onset value \(A=47.8^\circ\),
\[
\kappa(0)=0.0169968904>0.
\]
Hence the reported transition near \(47.8^\circ\) cannot be an instantaneous sign loss of the antiphase stiffness at release. Any explanation within the conservative model must use the subsequent time dependence of the in-phase trajectory (parametric/transient normal dynamics), rather than a static release-point criterion.

## Complete quadratic modulation spectrum near the hanging equilibrium

There is also a structural small-amplitude selection rule. Let \(\omega_\ell<\omega_h\) be the two linear in-phase frequencies and \(\omega_d=\sqrt{G_2/M_2}\) the antiphase frequency. Normalize the in-phase eigenvectors as \((\theta_1,\theta_m)=(1,r_j)\), where
\[
r_j=\frac{\mu\omega_j^2}{G_2-M_2\omega_j^2}.
\]
For a parent-only release of small amplitude \(A\), write
\[
\theta_1=A\bigl(a\cos\omega_\ell t+b\cos\omega_h t\bigr)+O(A^3),
\]
\[
\theta_m=A\bigl(ar_\ell\cos\omega_\ell t+br_h\cos\omega_h t\bigr)+O(A^3),
\]
with
\[
a=-\frac{r_h}{r_\ell-r_h},\qquad b=\frac{r_\ell}{r_\ell-r_h}.
\]
Expanding the exact normal coefficient gives, on fixed time intervals,
\[
\kappa(t)=G_2+A^2\Bigl[
K_0+K_{2\ell}\cos 2\omega_\ell t+K_{2h}\cos 2\omega_h t
+K_\Sigma\cos(\omega_\ell+\omega_h)t
+K_\Delta\cos(\omega_h-\omega_\ell)t
\Bigr]+O(A^4).
\]
In particular the sum-frequency coefficient is
\[
\boxed{
K_\Sigma=ab\left[
-\frac{G_2r_\ell r_h}{2}-\mu\omega_\ell\omega_h
+\frac{\mu}{2}\left((r_\ell-1)\omega_h^2+(r_h-1)\omega_\ell^2\right)
\right].
}
\]
For the reported apparatus,
\[
f_\ell=0.87331875\ \mathrm{Hz},\qquad
f_h=1.58282697\ \mathrm{Hz},\qquad
f_d=1.25827322\ \mathrm{Hz},
\]
consistent with the measured \(0.88,1.58,1.26\) Hz. The quadratic modulation frequencies and their distances from the principal parametric target \(2f_d\) are
\[
\begin{array}{c|c|c}
\text{channel}&\text{frequency (Hz)}&|f-2f_d|\ \text{(Hz)}\\ \hline
2f_\ell&1.74663750&0.76990894\\
2f_h&3.16565394&0.64910749\\
f_\ell+f_h&2.45614572&0.06040072\\
f_h-f_\ell&0.70950822&1.80703823.
\end{array}
\]
Moreover
\[
\boxed{K_\Sigma=0.00589770176\neq0.}
\]
Thus the experimentally noted near relation \(f_\ell+f_h\approx2f_d\) is not only a frequency coincidence: the exact normal equation contains a nonzero quadratic sum-frequency stiffness modulation, and it is by far the closest of the four quadratic combination channels to the principal antiphase parametric resonance.

This does **not** by itself produce a controlled formula for the finite-amplitude critical angle. At amplitudes near the observed threshold, nonlinear shifts of the in-phase frequencies, the mean \(O(A^2)\) stiffness correction, damping in the physical apparatus, and higher-order terms are quantitatively relevant. A naive Mathieu-tongue extrapolation from the quadratic expansion is therefore not claimed here.

## Derivation

The source Lagrangian in \((\theta_1,\theta_m,\theta_d)\) has kinetic matrix
\[
\widetilde M=
\begin{pmatrix}
M_1&2\mu\cos\Delta_m\cos\theta_d&-2\mu\sin\Delta_m\sin\theta_d\\
2\mu\cos\Delta_m\cos\theta_d&2M_2&0\\
-2\mu\sin\Delta_m\sin\theta_d&0&2M_2
\end{pmatrix}
\]
and potential
\[
U=G_1(1-\cos\theta_1)+2G_2(1-\cos\theta_m\cos\theta_d).
\]
The quadratic part in \(x=\theta_d\), along an in-phase base trajectory, is
\[
L^{(2)}=M_2\dot x^2
-2\mu\sin\Delta_m\,\dot\theta_1 x\dot x
-\bigl(\mu\cos\Delta_m\,\dot\theta_1\dot\theta_m+G_2\cos\theta_m\bigr)x^2.
\]
Integrating the mixed term by parts and using \(\dot\Delta_m=\dot\theta_m-\dot\theta_1\), this is equivalent modulo a total time derivative to
\[
L^{(2)}\equiv M_2\dot x^2-\kappa(t)x^2,
\]
with \(\kappa\) as stated above. The Euler--Lagrange equation gives the normal variational equation immediately. The release formula follows by solving the two in-phase acceleration equations at \(t=0\). The quadratic spectral expansion follows by inserting the linear in-phase mode decomposition into
\[
\kappa-G_2=
-\frac{G_2}{2}\theta_m^2
+\mu\dot\theta_1^2
-\mu(\theta_m-\theta_1)\ddot\theta_1
+O(A^4).
\]

## Relation to prior work and originality scope

Toda and Ooshida derive an approximate antiphase sub-Hamiltonian and an energy-transfer observable, and experimentally locate a sharp growth transition between about \(47.6^\circ\) and \(47.8^\circ\). They also note that the two linear in-phase frequencies sum to a value close to \(2f_d\). Their v1 text does not formulate the exact normal variational equation, a transverse-stability criterion, or the complete quadratic stiffness spectrum above.

Autoparametric/internal-resonance mechanisms in other pendulum systems are established prior art; no general claim about their novelty is made. The contribution here is source-specific: the exact finite-amplitude normal equation for the symmetric manifold of arXiv:2609.20688v1, the exact release-point stiffness obstruction for its reported apparatus, and the explicit quadratic combination spectrum of that normal equation.

A 2025 Physical Society of Japan meeting contribution by the same authors, *Energy transfer processes between oscillation modes of a branched double pendulum observed with image analysis*, is bibliographically visible but its full text was not inspected here. It is the most plausible uninspected source that could reduce the originality of the source-specific claims. The accessible 2024 meeting abstract reports the experimental onset phenomenon but not this normal-stability calculation.

## Limitations

The normal equation is for infinitesimal antiphase perturbations about the ideal symmetric, conservative Lagrangian model. It does not include pivot friction, aerodynamic damping, construction asymmetry, or finite \(\theta_d\) saturation. The release-stiffness calculation rules out only an instantaneous sign-loss explanation at \(t=0\); a positive \(\kappa(0)\) does not imply later-time normal stability. The quadratic spectral calculation is a local small-amplitude expansion and is not asserted to predict the finite-amplitude experimental threshold.

## Reproducibility

`artifacts/verify_antiphase_variational.py` symbolically derives the normal coefficient from the source Lagrangian, reconstructs the reported physical parameters and linear frequencies, verifies the release-stiffness zero, and evaluates the quadratic combination coefficients. `artifacts/verification_output.txt` contains its deterministic output.

## References

1. Y. Toda and T. Ooshida, *Experimental detection of energy transfer into the antiphase mode in a branched double pendulum*, arXiv:2609.20688v1 (2026). https://arxiv.org/abs/2609.20688
2. Y. Toda and T. Ooshida, *Experiment on generation of antiphase oscillations of the secondary limbs in a branched double pendulum*, Meeting Abstracts of the Physical Society of Japan 79.2 (2024), DOI: 10.11316/jpsgaiyo.79.2.0_3613. https://doi.org/10.11316/jpsgaiyo.79.2.0_3613
3. Y. Toda and T. Ooshida, *Energy transfer processes between oscillation modes of a branched double pendulum observed with image analysis*, Meeting Abstracts of the Physical Society of Japan 80.2 (2025), 18pPS-113. https://jglobal.jst.go.jp/detail?JGLOBAL_ID=202602238071926748
4. M. P. Cartmell, I. Kovacic, and M. Zukovic, *Autoparametric interaction in a double pendulum system*, Proc. IMechE Part C 226 (2012), 1971–1986. https://doi.org/10.1177/0954406212441748
5. J. Warminski, *Autoparametric vibrations of a nonlinear system with pendulum*, Mathematical Problems in Engineering 2006, 80705. https://doi.org/10.1155/MPE/2006/80705
