# Corrected endemic-equilibrium algebra and a rigorous forward branch in an awareness-driven SEIQHRA model
## Finding
For the awareness-driven SEIQHRA system
\[
\dot S=\Pi-\frac{\lambda SI}{1+cA}-dS,
\qquad
\dot E=\frac{\lambda SI}{1+cA}-(\mu+d)E,
\]
\[
\dot I=\mu E-\bigl(d+\delta+(q+r_1)A\bigr)I,
\]
\[
\dot Q=qAI-\bigl(d+\delta+(h+r_2)A\bigr)Q,
\]
\[
\dot H=hAQ-\bigl(d+\delta+r_3A\bigr)H,
\]
\[
\dot R=A(r_1I+r_2Q+r_3H)-dR,
\qquad
\dot A=\omega+\gamma(I+Q+H)-\theta A,
\]
the endemic infected-coordinate formula printed in the source contains an extra factor \(1+cA^*\) in its denominator.

Write
\[
A_0=\frac{\omega}{\theta},
\qquad
B_0(A)=d+\delta+(q+r_1)A.
\]
The source prints
\[
S^*=
\frac{(1+cA^*)(\mu+d)B_0(A^*)}{\mu\lambda},
\]
together with an infected coordinate equal to
\[
I_{\mathrm{src}}
=
\frac{\mu(\Pi-dS^*)}
{(1+cA^*)(\mu+d)B_0(A^*)}.
\]
Substituting these two expressions into the susceptible equation gives the exact residual
\[
\Pi-dS^*-\frac{\lambda S^*I_{\mathrm{src}}}{1+cA^*}
=
(\Pi-dS^*)\frac{cA^*}{1+cA^*}.
\]
For a positive endemic state with \(c>0\), \(A^*>0\), and \(I^*>0\), this residual is strictly positive. Hence the printed coordinate tuple is not an equilibrium of the displayed ODE system.

The corrected equilibrium algebra reduces the full endemic problem to one scalar equation and yields a rigorous local forward branch at the disease-free threshold.

## Assumptions and scope
All model parameters are positive. The claim concerns the autonomous uncontrolled system printed in the source. The result corrects the endemic equilibrium coordinates algebraically and proves the local direction of the endemic branch near \(R_0=1\).

No global uniqueness theorem for all endemic equilibria is asserted. No statement is made about the validity or invalidity of the source's later Hopf computations away from the disease-free threshold. The correction is source-specific, although the derivation uses standard equilibrium elimination and the implicit-function theorem.

## Proof
Define
\[
B_1(A)=d+\delta+(h+r_2)A,
\qquad
B_2(A)=d+\delta+r_3A,
\]
and
\[
L(A)=1+\frac{qA}{B_1(A)}
+\frac{hqA^2}{B_1(A)B_2(A)}.
\]

At a positive endemic equilibrium, the quarantine and hospitalization equations give
\[
Q=\frac{qAI}{B_1(A)},
\qquad
H=\frac{hqA^2I}{B_1(A)B_2(A)}.
\]
The awareness balance then becomes
\[
\theta A-\omega
=
\gamma(I+Q+H)
=
\gamma I L(A).
\]
Thus \(A>A_0=\omega/\theta\) and
\[
I(A)=\frac{\theta A-\omega}{\gamma L(A)}.
\]

The infected equation gives
\[
E(A)=\frac{B_0(A)}{\mu}I(A).
\]
Using this in the exposed equation yields
\[
\frac{\lambda S I}{1+cA}
=
(\mu+d)E
=
\frac{(\mu+d)B_0(A)}{\mu}I.
\]
Since \(I>0\),
\[
S(A,\lambda)=
\frac{(1+cA)(\mu+d)B_0(A)}{\mu\lambda}.
\]
The recovered coordinate is then
\[
R(A)=
\frac{A}{d}
\bigl(r_1I(A)+r_2Q(A)+r_3H(A)\bigr).
\]

It remains only to impose the susceptible equilibrium equation. Because the incidence term equals
\[
\frac{\mu+d}{\mu}B_0(A)I(A),
\]
that equation is exactly
\[
\Psi(A,\lambda)
=
\Pi-dS(A,\lambda)
-\frac{\mu+d}{\mu}B_0(A)I(A)
=0.
\]
Every positive endemic equilibrium therefore yields a root \(A>A_0\), and conversely any such root reconstructs all seven positive coordinates through the formulas above. This proves the exact scalar reduction.

Now set
\[
\lambda_c=
\frac{d(1+cA_0)(\mu+d)B_0(A_0)}{\mu\Pi}.
\]
The source's next-generation formula is precisely
\[
R_0=\frac{\lambda}{\lambda_c}.
\]
At \(A=A_0\), \(I(A_0)=0\), so
\[
\Psi(A_0,\lambda_c)=0.
\]
Also,
\[
\frac{\partial\Psi}{\partial\lambda}
=
\frac{d(1+cA)(\mu+d)B_0(A)}{\mu\lambda^2},
\]
hence
\[
\frac{\partial\Psi}{\partial\lambda}(A_0,\lambda_c)
=
\frac{\Pi}{\lambda_c}>0.
\]
Because
\[
I'(A_0)=\frac{\theta}{\gamma L(A_0)}>0,
\]
we obtain
\[
\frac{\partial\Psi}{\partial A}(A_0,\lambda_c)
=
-\frac{d(\mu+d)}{\mu\lambda_c}
\frac{d}{dA}\left[(1+cA)B_0(A)\right]_{A=A_0}
-\frac{\mu+d}{\mu}B_0(A_0)
\frac{\theta}{\gamma L(A_0)}<0.
\]
The implicit-function theorem therefore supplies a unique local function \(A=A(\lambda)\) satisfying \(\Psi(A(\lambda),\lambda)=0\) near \(\lambda_c\), with
\[
\frac{dA}{d\lambda}(\lambda_c)
=
-\frac{\Psi_\lambda}{\Psi_A}(A_0,\lambda_c)>0.
\]
Since \(I'(A_0)>0\), the endemic infected coordinate also has positive derivative with respect to \(\lambda\) at onset. The branch therefore emerges toward \(\lambda>\lambda_c\), establishing the forward local direction rigorously.

Finally, the correct infected coordinate obtained directly from the susceptible balance is
\[
I^*
=
\frac{\mu(\Pi-dS^*)}
{(\mu+d)B_0(A^*)},
\]
without the extra factor \(1+cA^*\). Substitution into all equilibrium equations is exact.

## Verification
The bundled script `verification/verify.py` performs three checks using only the Python standard library.

First, it reconstructs the source's baseline parameter set and verifies
\[
R_0=\frac{\lambda}{\lambda_c}.
\]
Second, it solves the corrected scalar equation \(\Psi(A,\lambda)=0\) by bisection at the source's baseline transmission rate and verifies all seven equilibrium residuals numerically. Third, it evaluates the source's printed infected-coordinate formula at the same \(S^*\) and \(A^*\), confirming the predicted nonzero susceptible residual and the exact algebraic residual identity.

For the source baseline values, the corrected scalar reduction gives approximately
\[
A^*=1.5052135785,
\qquad
I^*=4.9765388413,
\]
whereas the source's printed infected coordinate gives approximately
\[
I_{\mathrm{src}}=2.8395067689.
\]
The corresponding susceptible residual is approximately
\[
0.1210750023,
\]
rather than zero.

The proof of the correction and the local branch direction is analytic; the numerical calculation is only a reproducibility check.

## Relationship to prior work
The motivating 2026 article states that the model has a disease-free equilibrium and an endemic equilibrium, prints the endemic coordinate formulas, derives the next-generation threshold, and then studies a numerically observed forward bifurcation and later Hopf behavior. The correction here is obtained directly from those same printed equations.

A related 2023 awareness-and-treatment epidemic model by Al Basir, Rajak, Rahman, and Hattaf also studies equilibrium stability, awareness feedback, and Hopf bifurcation, but its compartments and transition laws are different. Its formulas therefore do not imply the present SEIQHRA correction.

A 2025 extended SIQR model with public awareness by overlapping authors likewise uses an awareness state and awareness-dependent control mechanisms, but it is a different compartmental system. Searches for the exact 2026 title together with endemic-equilibrium corrections, the factor \(1+cA\), and forward-branch formulas did not locate a published source-specific correction.

## Limitations
The result proves a locally unique forward endemic branch near \(R_0=1\), not global uniqueness for all \(R_0>1\). It does not recompute the endemic Jacobian or certify the source's Hopf points. A correct numerical continuation performed from the original ODEs could still produce valid later dynamics even though the printed equilibrium coordinate formula is algebraically wrong.

No claim is made that the general phenomenon of awareness-driven forward bifurcation is new. The contribution is the exact correction and scalar reduction for this particular 2026 SEIQHRA system.

## References
1. K. Aldawsari and F. Al Basir, “Dynamics of an SEIQHR-based mathematical model for infectious disease with awareness-driven optimal control,” AIMS Mathematics 11 (2026), 7659–7686. DOI: 10.3934/math.2026315.
2. F. Al Basir, B. Rajak, B. M. Rahman, and K. Hattaf, “Hopf bifurcation analysis and optimal control of an infectious disease with awareness campaign and treatment,” Axioms 12 (2023), 608. DOI: 10.3390/axioms12060608.
3. F. Al Basir, K. S. Nisar, I. M. Alsulami, and A. N. Chatterjee, “Dynamics and optimal control of an extended SIQR model with protected human class and public awareness,” European Physical Journal Plus 140 (2025), 152. DOI: 10.1140/epjp/s13360-025-06108-3.
