# Correcting the susceptible costate in a vaccinated SEIR optimal-control model

## Finding

The controlled model is
\[
\dot S=A_0-[1-u_2]\theta(I)SE-[\mu+z_0u_1]S,
\]
\[
\dot E=A_1+[1-u_2]\theta(I)SE-(\mu+\delta_1+\alpha+\omega_1)E,
\]
\[
\dot I=\alpha E-(\mu+\delta_2+\omega_2)I.
\]

Its Hamiltonian is
\[
H=C_1u_1^2+C_2u_2^2+C_3I+\lambda_1\dot S+\lambda_2\dot E+\lambda_3\dot I.
\]
Let
\[
a=(1-u_2)\theta(I),
\qquad
v=\mu+z_0u_1.
\]
Direct differentiation gives
\[
-\frac{\partial H}{\partial S}
=
\lambda_1(aE+v)-\lambda_2aE.
\]
Thus the correct susceptible costate is
\[
\dot\lambda_1
=
\lambda_1(aE+v)-\lambda_2aE.
\]

Equation (5.3) instead prints
\[
\dot\lambda_1^{\mathrm{print}}
=
\lambda_1(aE+v)-\lambda_2(aE+v),
\]
whose discrepancy is
\[
\dot\lambda_1^{\mathrm{print}}-\dot\lambda_1
=
-v\lambda_2.
\]

The discrepancy is generically active in the source's own terminal-value problem. Since
\[
\lambda_1(T)=\lambda_2(T)=\lambda_3(T)=0
\]
and \(C_3>0\), the correct adjoints imply
\[
\lambda_3(T-\tau)=C_3\tau+O(\tau^2),
\]
\[
\lambda_2(T-\tau)=\frac{\alpha C_3}{2}\tau^2+O(\tau^3)
\]
as \(\tau\downarrow0\). Therefore
\[
\dot\lambda_1^{\mathrm{print}}-\dot\lambda_1
=
-\frac{\mu\alpha C_3}{2}\tau^2+O(\tau^3),
\]
because \(v\ge\mu>0\).

So the printed first costate is not merely written in an equivalent form: it produces a different backward system on every sufficiently small terminal neighborhood.

## Assumptions and scope

The parameters satisfy the positivity assumptions of the source, in particular
\[
\mu>0,\qquad
z_0>0,\qquad
\alpha>0,\qquad
C_3>0.
\]
The controls lie in the source's bounded admissible sets.

The calculation concerns the necessary conditions obtained from the displayed controlled system and Hamiltonian. It does not dispute existence of an optimal control.

The second and third printed costate equations agree with direct differentiation, and the displayed pointwise stationarity formulas for the two controls are formally correct when paired with the corrected costates.

The conclusion is about the published equations. An unavailable numerical implementation could in principle have used a corrected first costate.

## Proof

From the Hamiltonian, the terms depending on \(S\) are
\[
\lambda_1[-aSE-vS]+\lambda_2[aSE].
\]
Hence
\[
\frac{\partial H}{\partial S}
=
-\lambda_1(aE+v)+\lambda_2aE.
\]
Pontryagin's adjoint equation gives
\[
\dot\lambda_1
=
-\frac{\partial H}{\partial S}
=
\lambda_1(aE+v)-\lambda_2aE.
\]

The printed equation contains the additional term
\[
-v\lambda_2.
\]
No term of the Hamiltonian contributes such a factor to the \(S\)-derivative.

To show that the extra term cannot disappear throughout the relevant terminal-value problem, set
\[
\tau=T-t.
\]
At the terminal point all costates vanish. The third correct costate has
\[
\dot\lambda_3(T)=-C_3,
\]
so backward Taylor expansion gives
\[
\lambda_3(T-\tau)=C_3\tau+O(\tau^2).
\]
The second correct costate is
\[
\dot\lambda_2
=
aS\lambda_1+(m_1-aS)\lambda_2-\alpha\lambda_3,
\]
where
\[
m_1=\mu+\delta_1+\alpha+\omega_1.
\]
The first two terms are of higher order at the terminal point, while
\[
-\alpha\lambda_3
=
-\alpha C_3\tau+O(\tau^2).
\]
Integrating backward yields
\[
\lambda_2(T-\tau)
=
\frac{\alpha C_3}{2}\tau^2+O(\tau^3).
\]
Since
\[
v=\mu+z_0u_1\ge\mu,
\]
the printed-minus-correct discrepancy is nonzero to leading order:
\[
-v\lambda_2
=
-\frac{\mu\alpha C_3}{2}\tau^2+O(\tau^3)
\]
or more negative if the vaccination control is positive.

Thus the two backward systems necessarily separate near \(T\).

## Verification

The bundled `verify.py` reconstructs the Hamiltonian symbolically and differentiates it with respect to all three state variables.

It verifies the corrected first costate exactly, verifies that the source's printed first equation differs by
\[
-v\lambda_2,
\]
and confirms that the second and third equations follow from direct differentiation.

It also checks the terminal expansion coefficient
\[
\frac{\alpha C_3}{2}
\]
for \(\lambda_2(T-\tau)\), and evaluates an exact interior witness where the printed-minus-correct first-costate derivative equals \(-7\).

No numerical optimization is used to establish the correction.

## Relationship to prior work

The motivating article defines the controlled SEIR system, its objective functional, the Hamiltonian, and equation (5.3), then uses the resulting optimal-control framework to display vaccination and contact-reduction controls.

A previous result for the same epidemiological model concerns endemic-equilibrium comparative statics under infected immigration. That equilibrium result does not analyze the Pontryagin system and does not imply the present derivative correction.

Optimal-control work on COVID-19 in South Africa uses related forward-backward methods, but with different state variables and control laws. Such work supplies methodological context rather than the source-specific correction.

Searches by DOI, exact title, equation number, costate terminology, adjoint terminology, and correction or erratum terminology did not locate a published replacement for equation (5.3).

## Limitations

The finding proves a mismatch between the printed Hamiltonian and the printed first costate.

It does not reconstruct the authors' unavailable implementation and therefore does not assert that every plotted control profile was generated from the erroneous equation.

It does not recompute the optimal trajectories with the corrected backward system.

## References

1. P. J. Witbooi, S. M. Vyambwera, M. U. Nsuami, “Control and elimination in an SEIR model for the disease dynamics of COVID-19 with vaccination,” AIMS Mathematics 8 (2023), 8144–8161. DOI: 10.3934/math.2023411.
2. S. P. Gatyeni, C. W. Chukwu, F. Chirove, Fatmawati, F. Nyabadza, “Application of Optimal Control to Long Term Dynamics of COVID-19 Disease in South Africa,” Scientific African 16 (2022), e01268. DOI: 10.1016/j.sciaf.2022.e01268.
