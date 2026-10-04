# A 19% quantitative binding gap for quadratic interaction on the half-line

## Finding

For every \(\omega>0\), consider the two-particle Hamiltonian
\[
H_\omega
=-\partial_{x_1}^2-\partial_{x_2}^2
+\frac{\omega^2}2(x_1-x_2)^2
\]
in \(L^2(\mathbb R_+^2)\), with the natural Neumann boundary conditions at the two half-line endpoints. This is the quadratic-interaction case \(v(r)=\omega^2r^2\) in the normalization of Egger--Kerner--Pankrashkin.

Its essential spectrum is
\[
\sigma_{\mathrm{ess}}(H_\omega)=[\omega,\infty).
\]
If \(E_0(\omega)\) denotes the lowest eigenvalue, then
\[
E_0(\omega)<\frac{81}{100}\,\omega.
\]
Consequently the boundary-induced binding gap is uniformly bounded below by
\[
\omega-E_0(\omega)>\frac{19}{100}\,\omega.
\]

## Assumptions and scope

The parameter satisfies \(\omega>0\). The interaction is exactly quadratic in the relative distance, with no additional one-body trapping potential. The half-line boundary conditions are the natural Neumann conditions coming from the quadratic form of the primary model.

The claim is only an upper bound on the lowest eigenvalue. It does not assert that \(81/100\) is the optimal universal constant, does not determine the exact eigenvalue, and does not count the remaining discrete spectrum.

## Proof

Introduce rotated coordinates
\[
r=\frac{|x_1-x_2|}{\sqrt2},
\qquad
s=\frac{x_1+x_2}{\sqrt2}.
\]
The symmetric sector reduces to the wedge
\[
\Omega_0=\{(r,s):0<r<s\}
\]
with quadratic form
\[
q_+[u]
=\int_{\Omega_0}
\left(|\partial_r u|^2+|\partial_su|^2+\omega^2r^2|u|^2\right)\,dr\,ds.
\]
The associated one-dimensional transverse operator is the Neumann half-line oscillator
\[
h_\omega=-\frac{d^2}{dr^2}+\omega^2r^2.
\]
For its form domain,
\[
\int_0^\infty\left(|f'|^2+\omega^2r^2|f|^2\right)dr
=\omega\int_0^\infty|f|^2dr
+\int_0^\infty|f'+\omega r f|^2dr.
\]
Thus its ground energy is \(\omega\), attained by a multiple of \(e^{-\omega r^2/2}\). The primary theorem therefore gives \(\sigma_{\mathrm{ess}}(H_\omega)=[\omega,\infty)\).

For \(b>0\), use the form-domain trial function
\[
u_b(r,s)=\exp\!\left(-\frac{\omega r^2}2-b\sqrt\omega\,s\right).
\]
After scaling \(t=\sqrt\omega\,r\), its Rayleigh quotient is
\[
\frac{q_+[u_b]}{\|u_b\|^2}
=\omega F(b),
\qquad
F(b)=1+3b^2-2bM(b),
\]
where
\[
M(b)=\frac{e^{-b^2}}{\sqrt\pi\,\operatorname{erfc}(b)}.
\]
Indeed, if
\[
I_b=\int_0^\infty e^{-t^2-2bt}dt,
\qquad
J_b=\int_0^\infty t e^{-t^2-2bt}dt,
\]
then \(J_b/I_b=M(b)-b\), which follows from one integration by parts, and substitution gives the displayed formula for \(F\).

Choose \(b=1/3\). Since \(e^{-x}>1-x\) for \(x>0\),
\[
e^{-1/9}>\frac89.
\]
Also \(e^{-t^2}>1-t^2\) on \((0,1/3]\), so
\[
\sqrt\pi\,\operatorname{erfc}\!\left(\frac13\right)
=\sqrt\pi-2\int_0^{1/3}e^{-t^2}dt
<\sqrt\pi-\frac{52}{81}.
\]
Using the classical inequality \(\pi<22/7\) and
\[
\left(\frac{1773}{1000}\right)^2>\frac{22}7,
\]
we get
\[
\sqrt\pi\,\operatorname{erfc}\!\left(\frac13\right)
<\frac{1773}{1000}-\frac{52}{81}
=\frac{91613}{81000}.
\]
Hence
\[
M\!\left(\frac13\right)
>\frac{8/9}{91613/81000}
=\frac{72000}{91613}
>\frac{157}{200}.
\]
Therefore
\[
F\!\left(\frac13\right)
=\frac43-\frac23M\!\left(\frac13\right)
<\frac43-\frac23\frac{157}{200}
=\frac{81}{100}.
\]
By the min--max principle,
\[
\inf\sigma(H_\omega)
\le \frac{q_+[u_{1/3}]}{\|u_{1/3}\|^2}
<\frac{81}{100}\omega.
\]
This lies strictly below the essential threshold \(\omega\), so it is a discrete eigenvalue and proves the claim.

## Verification

The proof uses only the exact wedge reduction, the elementary factorization of the half-line oscillator, a closed-form Rayleigh quotient, and rational inequalities. A standalone standard-library checker verifies the rational comparisons, the closed-form value of the Rayleigh quotient at \(b=1/3\), and the scaling for several positive \(\omega\). These finite checks are corroborative; the all-\(\omega\) statement is proved analytically above.

## Relationship to prior work

Egger, Kerner, and Pankrashkin treat a broad class of interactions that explicitly includes quadratic potentials. They prove that the essential spectrum begins at the one-dimensional ground energy and that at least one lower eigenvalue exists, but their theorem and general trial-function construction are qualitative. In the quadratic case the transverse ground state is explicit, which makes the elementary exponential center-of-mass trial above possible and yields a scale-invariant numerical gap.

Roos and Seiringer extend the strict boundary-energy lowering mechanism to higher dimensions and corners, again at the qualitative level. Kerner's separate exact one-eigenvalue theorem concerns a hard-wall interaction and therefore does not imply an energy bound for the smooth quadratic interaction.

Targeted searches for the harmonic/quadratic half-line model, explicit binding-energy bounds, the wedge Rayleigh quotient, and equivalent rescaled formulations did not locate a published statement implying the \(81/100\) estimate.

## Limitations

The constant \(81/100\) is chosen for a clean fully elementary certificate and is not claimed optimal. Numerically, the same one-parameter trial family has a slightly smaller minimum, but that numerical optimization is not part of the theorem. The result does not identify the exact ground energy, prove uniqueness of the discrete eigenvalue for the quadratic interaction, or treat Dirichlet endpoint conditions.

## References

1. S. Egger, J. Kerner, K. Pankrashkin, *Bound states of a pair of particles on the half-line with a general interaction potential*, arXiv:1812.06500v1; J. Spectr. Theory 10 (2020), 1413--1444; DOI 10.4171/JST/331.
2. B. Roos, R. Seiringer, *Two-Particle Bound States at Interfaces and Corners*, arXiv:2105.04874v1; J. Funct. Anal. 282 (2022), 109455.
3. J. Kerner, *On the number of isolated eigenvalues of a pair of particles on the half-line*, Operators and Matrices 14 (2020), 717--722; DOI 10.7153/oam-2020-14-45.