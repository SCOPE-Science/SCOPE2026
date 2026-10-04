# Correct Pontryagin adjoints for a variable-population SQEIAR media-control model

## Finding

Consider the controlled SQEIAR model of Shi, Gao, Zhou, and Li, with
\[
N=S+Q+E+I+A+R,
\]
and controlled incidence
\[
F=\beta e^{-U/N}\frac{SV}{N},\qquad U=u_1I+u_2A,\qquad V=I+\theta A.
\]
The source explicitly treats \(N\) as the total population and gives
\[
\dot N=\Lambda-\mu N-\mu_I I,
\]
so \(N\) is not a fixed parameter in the Hamiltonian differentiation.

Define
\[
C=\frac{U}{N^2}-\frac1N,\qquad D=\lambda_1-\lambda_3.
\]
Then the exact state derivatives of the incidence are
\[
F_S=F\left(\frac1S+C\right),\qquad F_Q=F_E=F_R=FC,
\]
\[
F_I=F\left(\frac1V-\frac{u_1}{N}+C\right),\qquad
F_A=F\left(\frac{\theta}{V}-\frac{u_2}{N}+C\right).
\]
Consequently, for state order \((S,Q,E,I,A,R)\), the Pontryagin adjoints are
\[
\dot\lambda_1=DF\left(\frac1S+C\right)+(\lambda_1-\lambda_2)u_3+\mu\lambda_1,
\]
\[
\dot\lambda_2=DFC+(\lambda_2-\lambda_1)\lambda+\mu\lambda_2,
\]
\[
\dot\lambda_3=DFC+\sigma\left[\lambda_3-\rho\lambda_4-(1-\rho)\lambda_5\right]+\mu\lambda_3,
\]
\[
\dot\lambda_4=-A_1+DF\left(\frac1V-\frac{u_1}{N}+C\right)+(\lambda_4-\lambda_6)\gamma_I+(\mu_I+\mu)\lambda_4,
\]
\[
\dot\lambda_5=-A_2+DF\left(\frac{\theta}{V}-\frac{u_2}{N}+C\right)+(\lambda_5-\lambda_6)\gamma_A+\mu\lambda_5,
\]
\[
\dot\lambda_6=DFC+\mu\lambda_6.
\]
These equations differ structurally from Eq. (6.2) in the paper. Two discrepancies already suffice to rule out equality with the stated Hamiltonian: the paper prints \(\dot\lambda_6=\mu\lambda_6\), omitting \(DFC\), and its quarantine contribution to \(\dot\lambda_1\) uses \((\lambda_1-\lambda_3)u_3\), whereas the flows \(-u_3S\) and \(+u_3S\) in the susceptible and quarantined equations force \((\lambda_1-\lambda_2)u_3\).

The interior control derivatives are nevertheless
\[
H_{u_1}=B_1u_1+DF\frac{I}{N},\qquad
H_{u_2}=B_2u_2+DF\frac{A}{N},\qquad
H_{u_3}=B_3u_3+(\lambda_2-\lambda_1)S,
\]
so the source's control-stationarity relations can retain their formal shape only when coupled to the corrected adjoints.

## Assumptions and scope

All compartments are treated as independent state coordinates before imposing \(N=S+Q+E+I+A+R\), exactly as required when differentiating the six-state Hamiltonian. Parameters and controls are in the positive/interior regime used by the source, with \(0\le u_i\le1\). The correction concerns the necessary Pontryagin conditions for the controlled system; it does not alter the uncontrolled threshold analysis by itself.

For an interior positive state, \(U\le I+A<N\) when \(0\le u_1,u_2\le1\), hence
\[
C=\frac{U-N}{N^2}<0.
\]
Thus the omitted common incidence contribution \(DFC\) is generically nonzero whenever \(D\ne0\) and \(F>0\).

## Proof

The Hamiltonian contains the incidence only through
\[
-\lambda_1F+\lambda_3F=-DF.
\]
Since
\[
\log F=\log\beta+\log S+\log V-\log N-\frac{U}{N},
\]
differentiation gives
\[
\partial_x\log F=C
\]
for \(x\in\{Q,E,R\}\), with the additional direct factors \(1/S\), \(1/V-u_1/N\), and \(\theta/V-u_2/N\) for \(S,I,A\), respectively. Multiplication by \(F\) yields the six displayed derivatives.

Applying \(\dot\lambda_j=-\partial H/\partial x_j\) gives the corrected adjoint system. The quarantine term is immediate: its Hamiltonian contribution is
\[
-\lambda_1u_3S+\lambda_2u_3S,
\]
whose negative derivative with respect to \(S\) is
\[
(\lambda_1-\lambda_2)u_3.
\]
The recovered coordinate \(R\) enters the incidence only through \(N\), so
\[
-\frac{\partial H}{\partial R}=DF_R+\mu\lambda_6=DFC+\mu\lambda_6.
\]
This proves both structural discrepancies without any numerical approximation.

Finally, differentiating \(-DF\) with respect to the controls while holding the state fixed gives
\[
\frac{\partial F}{\partial u_1}=-F\frac{I}{N},\qquad
\frac{\partial F}{\partial u_2}=-F\frac{A}{N},
\]
which yields the stated stationarity equations.

## Verification

The bundled script evaluates the Hamiltonian at a strictly positive interior state, computes all six state derivatives and all three control derivatives by centered finite differences, and compares them with the analytic formulas above. It also isolates the two source-level discrepancies: with media transmission active, the corrected recovered costate has a nonzero \(DFC\) term, and with the incidence switched off the quarantine contribution to the susceptible costate depends on \(\lambda_2\), not \(\lambda_3\). The script exits with `VERIFY_OK` only if every analytic derivative agrees with finite differences within tolerance.

## Relationship to prior work

Shi, Gao, Zhou, and Li (2021), DOI 10.3934/math.2021712, is the primary source. It defines \(N\) as the sum of the six compartments, states \(\dot N=\Lambda-\mu N-\mu_I I\), writes the controlled model and Hamiltonian, and prints Eq. (6.2) as the adjoint system used in its optimal-control section. The correction follows by differentiating that displayed Hamiltonian without freezing \(N\).

Searches by exact title, DOI, adjoint-equation terminology, and the state-dependent standard-incidence denominator found no erratum or later source that supplies these corrected six adjoints. Qiu and Hou (2024), DOI 10.1016/j.jmaa.2024.128192, study a different SEIAQR media-coverage optimal-control model and therefore do not imply this source-specific correction.

## Limitations

The result establishes that the printed adjoint system is not the Pontryagin adjoint of the printed controlled model. It does not prove that every plotted trajectory in the source is numerically wrong, because an implementation could in principle have used equations different from those printed. Recomputing the full optimal-control experiment with the corrected backward equations is a separate numerical task.

## References

1. X. Shi, X. Gao, X. Zhou, Y. Li, “Analysis of an SQEIAR epidemic model with media coverage and asymptomatic infection,” AIMS Mathematics 6 (2021), 12298–12320. DOI: 10.3934/math.2021712.
2. H. Qiu, R. Hou, “Dynamics and optimal control of an SEIAQR epidemic model with media coverage,” Journal of Mathematical Analysis and Applications 535 (2024), 128192. DOI: 10.1016/j.jmaa.2024.128192.
