# The published SEIQHRA control system fails its unit-control and transfer-balance checks
## Finding
In the SEIQHRA model of Aldawsari and Al Basir, the state system used for optimal control is not a controlled extension of the preceding uncontrolled model in two exact senses.

First, the uncontrolled incidence term is
\[
\frac{\lambda S I}{1+cA},
\]
whereas the controlled system uses
\[
\frac{\lambda S I}{1+A}.
\]
Thus setting \(u_1=u_2=u_3=1\) does not recover the uncontrolled vector field whenever \(c\ne1\) and \(ASI\ne0\).

Second, the controlled equations multiply recovery losses from \(I,Q,H\) by \(u_1\), but the gain in \(R\) is left unmultiplied. If
\[
N=S+E+I+Q+H+R,
\]
then direct summation of the printed controlled equations gives
\[
\dot N=\Pi-dN-\delta(I+Q+H)+(1-u_1)A(r_1I+r_2Q+r_3H).
\]
The last term is an artificial population source whenever \(u_1<1\) and the recovery flux is positive.

A minimal flow-consistent repair is to keep the original incidence denominator \(1+cA\) and replace the recovered equation by
\[
\dot R=u_1A(r_1I+r_2Q+r_3H)-dR.
\]
For that repaired state system, if \(\xi_3,\xi_4,\xi_5,\xi_6\) are the costates paired with \(I,Q,H,R\), respectively, the interior stationarity condition for a quadratic control cost \(\tfrac12 B_1u_1^2\) is
\[
u_1^*=\frac{(\xi_3-\xi_6)r_1AI+(\xi_4-\xi_6)r_2AQ+(\xi_5-\xi_6)r_3AH}{B_1},
\]
before projection onto \([0,1]\). Hence the printed control characterization, which contains no \(\xi_6\) contribution, is not the Pontryagin stationarity law of the flow-consistent repair.

## Assumptions and scope
The statement concerns the equations as printed in the 2026 AIMS Mathematics article. States and rate parameters are taken nonnegative. The incidence mismatch requires \(c\ne1\) and \(ASI\ne0\). The transfer-balance defect requires \(u_1<1\) and \(A(r_1I+r_2Q+r_3H)>0\). The costate formula assumes the repaired recovery transfer above and a running control penalty \(\tfrac12 B_1u_1^2\) with \(B_1>0\); if the paper's convention uses \(B_1u_1^2\) instead, the denominator is correspondingly \(2B_1\). The structural point is the unavoidable \(\xi_6\) contribution, not this normalization convention.

## Proof
For the first claim, compare the \(S\)-equations. With all controls set to one, the controlled equation still contains \(\lambda SI/(1+A)\), while the uncontrolled equation contains \(\lambda SI/(1+cA)\). Equality for positive \(ASI\) is equivalent to \(1+A=1+cA\), hence to \(c=1\). The same mismatch appears with opposite sign in the \(E\)-equation.

For the second claim, add the printed equations for \(S,E,I,Q,H,R\). Incidence cancels between \(S\) and \(E\); progression \(\mu E\), quarantine \(qAI\), and hospitalization \(u_2hAQ\) cancel internally. The controlled recovery losses are
\[
-u_1A(r_1I+r_2Q+r_3H),
\]
while the printed recovered gain is
\[
+A(r_1I+r_2Q+r_3H).
\]
Their sum is
\[
(1-u_1)A(r_1I+r_2Q+r_3H),
\]
which proves the stated total-population identity.

For the stationarity correction, write the \(u_1\)-dependent part of the repaired Hamiltonian as
\[
\frac{B_1}{2}u_1^2-u_1\xi_3r_1AI-u_1\xi_4r_2AQ-u_1\xi_5r_3AH+u_1\xi_6A(r_1I+r_2Q+r_3H).
\]
Differentiation with respect to \(u_1\) gives
\[
B_1u_1+(\xi_6-\xi_3)r_1AI+(\xi_6-\xi_4)r_2AQ+(\xi_6-\xi_5)r_3AH.
\]
Setting this derivative to zero yields the formula in the finding.

## Verification
The paper's Table 1 gives \(c=1/2\), \(\omega=0.003\), \(\theta=0.015\), and \(\lambda=0.000025\). At the awareness baseline \(A=\omega/\theta=1/5\), with the exact witness \(S=100\), \(I=10\), the uncontrolled and controlled incidence terms are
\[
\frac{\lambda SI}{1+cA}=\frac1{44},\qquad
\frac{\lambda SI}{1+A}=\frac1{48},
\]
so their difference is \(1/528>0\).

For the recovery-balance witness, use the paper's values \(r_1=0.002\), \(r_2=0.023\), \(r_3=0.02\), and take \(A=1/5\), \(I=10\), \(Q=5\), \(H=2\), \(u_1=1/2\). Then
\[
A(r_1I+r_2Q+r_3H)=\frac7{200},
\]
so the artificial source is exactly
\[
(1-u_1)A(r_1I+r_2Q+r_3H)=\frac7{400}>0.
\]
The bundled verifier reproduces these identities with exact rational arithmetic and checks the corrected Hamiltonian derivative algebraically.

## Relationship to prior work
The motivating article introduces the controlled system as the optimal-control version of its SEIQHRA model and derives state, adjoint, and control equations from it. The finding above is a consistency result about those printed equations; it does not depend on a competing epidemiological closure.

A closely related awareness-and-treatment control model by Al Basir, Rajak, Rahman, and Hattaf (2023) pairs its controlled treatment loss \(-u_1rMI\) with the recovered gain \(+u_1rMI\). That earlier construction illustrates the usual transfer-balanced form but does not state or imply the two exact consistency failures proved here for the 2026 seven-state model.

Targeted searches for the title, DOI, unit-control reduction, recovery transfer balance, and alternative optimality formulas did not locate a published correction or an earlier statement of this source-specific result.

## Limitations
This result does not claim that the uncontrolled SEIQHRA model is invalid, nor does it solve the optimal-control problem for a repaired model. It identifies exact incompatibilities between the printed uncontrolled and controlled vector fields and gives the minimal algebraic repair needed to restore their intended relationship. If the authors intended a reparameterized awareness variable in the control section, that rescaling would also have to transform every other \(A\)-dependent rate and would need to be stated; no such transformation is used in the printed equations examined here.

The costate formula is given under the explicit \(\tfrac12B_1u_1^2\) convention. A different quadratic normalization changes only the scalar denominator, not the required \(\xi_6\) terms.

## References
1. K. Aldawsari and F. Al Basir, “Dynamics of an SEIQHR-based mathematical model for infectious disease with awareness-driven optimal control,” AIMS Mathematics 11(3) (2026), 7659–7686. DOI: 10.3934/math.2026315.
2. F. Al Basir, B. Rajak, B. Rahman, and K. Hattaf, “Hopf Bifurcation Analysis and Optimal Control of an Infectious Disease with Awareness Campaign and Treatment,” Axioms 12(6) (2023), 608. DOI: 10.3390/axioms12060608.
