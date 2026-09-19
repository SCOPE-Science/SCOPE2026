# Exact transverse stability equation for antiphase growth in a branched double pendulum

## Result

Consider the conservative branched double pendulum of Toda and Ooshida (arXiv:2609.20688v1), written in the exchange-symmetric coordinates
\[
x=\theta_1,\qquad y=\theta_{\mathrm m}=\frac{\theta_2+\theta_3}{2},\qquad d=\theta_{\mathrm d}=\frac{\theta_2-\theta_3}{2},
\]
and set \(\Delta=y-x\). The child-synchronous manifold \(d=\dot d=0\) is invariant. Along any trajectory \((x(t),y(t))\) on this manifold, the exact linearized transverse equation is
\[
\boxed{
M_2\ddot d+
\Bigl[
G_2\cos y+
\mu\cos(y-x)\dot x^2-
\mu\sin(y-x)\ddot x
\Bigr]d=0.
}
\tag{1}
\]
Thus the onset of the experimentally observed antiphase mode is a scalar transverse parametric-stability problem. No small-angle assumption on the in-phase variables \(x,y\) is used in (1).

Because (1) contains no \(\dot d\) term, the transverse Wronskian is conserved. In particular, when the symmetric base trajectory is periodic, its two-dimensional transverse monodromy matrix has determinant exactly one. The linear antiphase instability criterion is therefore the usual reciprocal-multiplier criterion for this scalar Hill equation.

There is also an exact acceleration-free form useful for trajectory data. Write
\[
s=\sin(y-x),\qquad c=\cos(y-x),\qquad
\mathcal D=M_1M_2-2\mu^2c^2.
\]
The normalized transverse equation \(\ddot d+Q(t)d=0\) has
\[
\boxed{
\begin{aligned}
Q={}&\frac{G_2}{M_2}\cos y
+\frac{\mu c\,(M_1M_2-2\mu^2)}{M_2\mathcal D}\dot x^2
+\frac{\mu G_1s\sin x}{\mathcal D}\\
&-\frac{2G_2\mu^2sc\sin y}{M_2\mathcal D}
-\frac{2\mu^2s^2}{\mathcal D}\dot y^2.
\end{aligned}}
\tag{2}
\]
Hence the transverse stiffness can be reconstructed from the symmetric-sector angles and first derivatives alone, without differentiating experimental position data twice.

## Derivation

The source gives the transformed mass matrix and potential
\[
\widetilde M=
\begin{pmatrix}
M_1&2\mu\cos\Delta\cos d&-2\mu\sin\Delta\sin d\\
2\mu\cos\Delta\cos d&2M_2&0\\
-2\mu\sin\Delta\sin d&0&2M_2
\end{pmatrix},
\]
\[
U=G_1(1-\cos x)+2G_2(1-\cos y\cos d).
\]
Expanding only in the transverse variable gives the quadratic transverse Lagrangian
\[
L_\perp^{(2)}=
M_2\dot d^2
-2\mu\sin\Delta\,\dot x\,d\dot d
-\mu\cos\Delta\,\dot x\dot y\,d^2
-G_2\cos y\,d^2.
\]
Its Euler--Lagrange equation is exactly (1).

On \(d=0\), the symmetric-sector equations are
\[
M_1\ddot x+2\mu c\ddot y-2\mu s\dot y^2+G_1\sin x=0,
\]
\[
\mu c\ddot x+M_2\ddot y+\mu s\dot x^2+G_2\sin y=0.
\]
Solving them for \(\ddot x\) and substituting into (1) yields (2). For the printed experimental parameters, \(M_1M_2-2\mu^2>0\), so \(\mathcal D>0\) for all \(\Delta\).

## Small-amplitude mechanism: a direct sum-frequency parametric channel

The source notes that its measured in-phase frequencies satisfy
\[
f_++f_-=2.46\,\mathrm{Hz}<2f_{\mathrm d}=2.52\,\mathrm{Hz}
\]
and speculates that nonlinear low-frequency components may fill the mismatch. Equation (1) shows a more direct structural fact: even before such sidebands are introduced, the quadratic transverse stiffness already contains a component at the sum of the two in-phase frequencies.

Let the two linear in-phase modes have frequencies \(\omega_L<\omega_H\) and eigenvectors normalized as \((x,y)=(1,r_j)\). For the source's parent-only release, write
\[
x=A\bigl(a_L\cos\omega_Lt+a_H\cos\omega_Ht\bigr)+O(A^3),
\]
\[
y=A\bigl(a_Lr_L\cos\omega_Lt+a_Hr_H\cos\omega_Ht\bigr)+O(A^3),
\]
with \(a_L+a_H=1\) and \(a_Lr_L+a_Hr_H=0\). Since the system is inversion-symmetric, the next base-motion correction is cubic. Expanding (1) gives
\[
Q(t)=\omega_{\mathrm d}^2+A^2\Bigl[
q_0+q_{2L}\cos(2\omega_Lt)+q_{2H}\cos(2\omega_Ht)
+q_{\Delta}\cos((\omega_H-\omega_L)t)
+q_{\Sigma}\cos((\omega_H+\omega_L)t)
\Bigr]+O(A^4),
\tag{3}
\]
where \(\omega_{\mathrm d}^2=G_2/M_2\) and
\[
\boxed{
q_{\Sigma}=a_La_H\left[
-\frac{\omega_{\mathrm d}^2}{2}r_Lr_H
+\frac{\mu}{M_2}\left(
-\omega_L\omega_H
+\frac{(r_L-1)\omega_H^2+(r_H-1)\omega_L^2}{2}
\right)
\right].
}
\tag{4}
\]
The mean correction is
\[
q_0=\sum_{j=L,H}a_j^2\left[
-\frac{\omega_{\mathrm d}^2r_j^2}{4}
+\frac{\mu r_j\omega_j^2}{2M_2}
\right].
\tag{5}
\]
The remaining coefficients are listed and checked in the verification artifact.

Using the physical constants printed in the source gives
\[
f_L=0.873318750578\,\mathrm{Hz},\qquad
f_H=1.582826967915\,\mathrm{Hz},\qquad
f_{\mathrm d}=1.258273221537\,\mathrm{Hz},
\]
so
\[
f_L+f_H=2.456145718494\,\mathrm{Hz},\qquad
2f_{\mathrm d}=2.516546443073\,\mathrm{Hz}.
\]
For parent-only release,
\[
q_{\Sigma}=8.298228243023\,\mathrm{s}^{-2},\qquad
q_0=-47.204403461999\,\mathrm{s}^{-2}
\]
per unit \(A^2\). Thus the near-\(2\omega_{\mathrm d}\) sum-frequency modulation is present directly in the transverse variational equation. At the same asymptotic order there is also a substantial mean frequency renormalization, so a threshold estimate based on the resonant harmonic alone would be inconsistent.

The result therefore sharpens the mechanism without claiming a numerical critical angle: the observed antiphase onset is governed by transverse parametric instability of the invariant child-synchronous manifold, and the two in-phase modes generate a direct sum-frequency modulation close to twice the antiphase frequency. Determining the experimental threshold near \(47.8^\circ\) requires the finite-amplitude symmetric trajectory (and, for the apparatus, dissipation and imperfections), not only the leading small-amplitude harmonic.

## Relation to prior work and originality boundary

Toda and Ooshida derive an antiphase sub-Hamiltonian and an approximate energy-transfer function, observe significant antiphase growth for parent release angles at and above about \(47.8^\circ\), and state that systematic theoretical study of the critical value is future work. Their earlier 2024 meeting abstract reports an experimental generation condition, and the 2025 meeting record reports image-based mode-to-mode energy transfer. These sources do not provide the transverse variational equation above in the accessible material.

Parametric resonance, Floquet theory, variational equations, and nonlinear resonance analysis for other double-pendulum systems are established topics and are not claimed as new. The source-specific contribution here is the exact scalar transverse equation (1), its acceleration-free observable form (2), and the explicit sum-frequency content (3)--(5) for the newly introduced branched-double-pendulum model.

Two locally cited theses are the main residual originality risk: T. Miura's 2024 master's thesis and K. Kato's 2026 graduation thesis are cited by the source for preliminary numerical simulations, but their full contents were not inspected. They could contain related stability calculations. No broad priority claim beyond the source-specific formulas is made.

## Limitations

- Equation (1) is an exact linearization in the antiphase direction, not a nonlinear saturation model after \(d\) becomes large.
- Equations (3)--(5) are a small-amplitude expansion around the equilibrium. The experimental onset occurs at a large parent angle, so they do not by themselves predict the observed critical angle.
- The source model is conservative, whereas a real apparatus has dissipation, asymmetry, release imperfections, and measurement noise.
- For a quasiperiodic symmetric base trajectory, ordinary single-period Floquet theory is not directly applicable, although the scalar transverse equation remains exact.

## Verification

`artifacts/verify_transverse_antiphase.py` symbolically checks the quadratic Euler--Lagrange reduction and the acceleration-free identity, then verifies the full \(O(A^2)\) Fourier decomposition against direct evaluation. With the printed source parameters it reproduces the numerical frequencies and modulation coefficients quoted above. The recorded output is in `artifacts/verification.txt`.

## References

1. Y. Toda and T. Ooshida, *Experimental detection of energy transfer into the antiphase mode in a branched double pendulum*, arXiv:2609.20688v1 (2026). https://arxiv.org/abs/2609.20688v1
2. Y. Toda and T. Ooshida, *Experiment on generation of antiphase oscillations of the secondary limbs in a branched double pendulum*, Meeting Abstracts of the Physical Society of Japan 79.2 (2024), 3613. https://doi.org/10.11316/jpsgaiyo.79.2.0_3613
3. Y. Toda and T. Ooshida, *Energy transfer processes between oscillation modes of a branched double pendulum observed with image analysis*, 80th Annual Meeting of the Physical Society of Japan, 18pPS-113 (2025).
4. T. S. Amer et al., *Vibrational and stability analysis of planar double pendulum dynamics near resonance*, Nonlinear Dynamics 112 (2024), 21667--21699. https://doi.org/10.1007/s11071-024-10169-x
5. R. Sarkar, S. P. Khastgir, and K. Kumar, *Spontaneous parametric down-conversion like oscillations in a partially inverted double pendulum*, Europhysics Letters 148 (2024), 61004. https://doi.org/10.1209/0295-5075/ad9ed6
