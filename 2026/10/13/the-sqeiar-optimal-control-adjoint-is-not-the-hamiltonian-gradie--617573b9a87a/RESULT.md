# The SQEIAR optimal-control adjoint is not the Hamiltonian gradient

## Finding

For the controlled SQEIAR model, define
\[
N=S+Q+E+I+A+R,
\qquad
U=u_1I+u_2A,
\qquad
V=I+\theta A,
\]
and
\[
F=\beta e^{-U/N}\frac{SV}{N}.
\]

The source states Pontryagin's adjoint condition
\[
\dot\lambda=-\frac{\partial H}{\partial x},
\]
but the displayed equation (6.2) is not the state gradient of its own Hamiltonian.

On the positive interior,
\[
F_S=F\left(\frac1S-\frac1N+\frac{U}{N^2}\right),
\]
\[
F_Q=F_E=F_R=F\left(-\frac1N+\frac{U}{N^2}\right),
\]
\[
F_I=F\left(\frac1V-\frac{u_1+1}{N}+\frac{U}{N^2}\right),
\]
and
\[
F_A=F\left(\frac{\theta}{V}-\frac{u_2+1}{N}+\frac{U}{N^2}\right).
\]

Therefore the correct adjoints are
\[
\dot\lambda_1=(\lambda_1-\lambda_3)F_S+(\lambda_1-\lambda_2)u_3+\mu\lambda_1,
\]
\[
\dot\lambda_2=(\lambda_1-\lambda_3)F_Q+(\lambda_2-\lambda_1)\lambda+\mu\lambda_2,
\]
\[
\dot\lambda_3=(\lambda_1-\lambda_3)F_E+(\lambda_3-\lambda_5)\sigma+(\lambda_5-\lambda_4)\sigma\rho+\mu\lambda_3,
\]
\[
\dot\lambda_4=-A_1+(\lambda_1-\lambda_3)F_I+(\lambda_4-\lambda_6)\gamma_I+(\mu_I+\mu)\lambda_4,
\]
\[
\dot\lambda_5=-A_2+(\lambda_1-\lambda_3)F_A+(\lambda_5-\lambda_6)\gamma_A+\mu\lambda_5,
\]
\[
\dot\lambda_6=(\lambda_1-\lambda_3)F_R+\mu\lambda_6.
\]

The published system instead uses the incidence flow itself in the first costate, couples the quarantine control to the wrong costate difference, drops incidence derivatives from three costates, omits the state-dependence of \(N\) from two more, and misses a factor \(\sigma\) in the exposed costate.

These discrepancies are active in the terminal-value problem and are not equivalent rewritings.

## Assumptions and scope

The state variables and controls are those in the source's controlled system (6.1), with
\[
N=S+Q+E+I+A+R
\]
and
\[
0\le u_i\le1.
\]
The derivative formulas above are written on the positive interior, where \(S>0\), \(V>0\), and \(N>0\). Equivalent unfactored formulas extend to boundary points where the Hamiltonian is differentiable.

The finding concerns the necessary Pontryagin system printed in Theorem 6.2. It does not dispute existence of an optimal control.

The pointwise stationarity derivative with respect to \(u_3\) printed later in the source is consistent with the Hamiltonian; the problem is that it is coupled to an incorrect adjoint system.

## Proof

The incidence contribution to the Hamiltonian is
\[
(\lambda_3-\lambda_1)F.
\]
Because the source defines
\[
N=S+Q+E+I+A+R,
\]
every state variable changes both the normalization \(1/N\) and the exponent \(-U/N\).

Writing
\[
\log F=\log\beta+\log S+\log V-\log N-\frac{U}{N}
\]
on the positive interior gives the five derivative identities in the finding immediately.

The remaining Hamiltonian terms then give the six corrected adjoint equations by direct differentiation.

Several source discrepancies can be isolated without any numerical approximation. For example, the recovered costate must satisfy
\[
\dot\lambda_6=(\lambda_1-\lambda_3)F_R+\mu\lambda_6,
\]
while equation (6.2) prints only
\[
\dot\lambda_6=\mu\lambda_6.
\]
Likewise, differentiating the quarantine transfer terms
\[
-\lambda_1u_3S+\lambda_2u_3S
\]
with respect to \(S\) contributes
\[
(\lambda_1-\lambda_2)u_3
\]
to \(\dot\lambda_1\), not the printed
\[
(\lambda_1-\lambda_3)u_3.
\]

To show that the missing population-normalization derivative is active in the actual terminal-value problem, let
\[
\tau=T-t.
\]
The transversality conditions give all costates equal to zero at \(T\). Since the running objective contains \(A_1I+A_2A\), direct backward Taylor expansion of the correct equations yields
\[
\lambda_4(T-\tau)=A_1\tau+O(\tau^2),
\qquad
\lambda_5(T-\tau)=A_2\tau+O(\tau^2).
\]
The exposed costate then satisfies
\[
\lambda_3(T-\tau)
=
\frac{\sigma}{2}\bigl(\rho A_1+(1-\rho)A_2\bigr)\tau^2
+O(\tau^3),
\]
while the susceptible costate is only
\[
\lambda_1(T-\tau)=O(\tau^3).
\]
Thus \(\lambda_1-\lambda_3\) is nonzero to leading order.

For a positive interior state,
\[
U=u_1I+u_2A\le I+A<N,
\]
so
\[
F_R=F\frac{U-N}{N^2}<0.
\]
Hence the incidence term omitted from the printed recovered costate is nonzero on every sufficiently small terminal neighborhood of an interior optimal trajectory.

## Verification

The bundled `verify.py` reconstructs the full Hamiltonian symbolically with
\[
N=S+Q+E+I+A+R
\]
and differentiates it with respect to all six state variables.

It verifies every corrected adjoint identity and verifies that the printed recovered costate omits exactly
\[
(\lambda_1-\lambda_3)F_R.
\]
It also verifies the quarantine-control coefficient in the susceptible costate and the missing \(\sigma\) factor in the exposed costate.

No numerical optimal-control trajectory is used to establish the correction.

## Relationship to prior work

The motivating article explicitly defines the total population as the sum of all six compartments and later uses the same \(N\) inside the controlled incidence. Its numerical section states that an iterative fourth-order Runge–Kutta method solves the optimality system and presents the resulting controls and state trajectories in Figure 7.

Yan and Zou apply Pontryagin optimal control to quarantine and isolation in a different SARS model. That work supplies methodological context for forward–backward epidemic control, but it does not contain the state-normalized media incidence used here and does not imply the source-specific Hamiltonian-gradient correction.

Searches by the motivating DOI, exact title, Theorem 6.2, adjoint and costate terminology, population-normalization terminology, and correction or erratum terminology did not locate a published replacement for equation (6.2).

## Limitations

The finding corrects the published necessary optimality system. It does not reconstruct unavailable implementation code, which could in principle have used corrected equations.

It does not recompute Figure 7 under the corrected adjoints and therefore does not assert the quantitative size of any change in the plotted controls.

The result is specific to the model and Hamiltonian as printed.

## References

1. X. Shi, X. Gao, X. Zhou, Y. Li, “Analysis of an SQEIAR epidemic model with media coverage and asymptomatic infection,” AIMS Mathematics 6 (2021), 12298–12320. DOI: 10.3934/math.2021712.
2. X. Yan, Y. Zou, “Optimal and sub-optimal quarantine and isolation control in SARS epidemics,” Mathematical and Computer Modelling 47 (2008), 235–245. DOI: 10.1016/j.mcm.2007.04.003.
