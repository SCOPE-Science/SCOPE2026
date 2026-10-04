# Corrected Floquet factor for the bilateral Leslie–Gower cycle
## Finding
Consider a positive transversal order-2 periodic orbit of the bilateral impulsive system (2.1) in Xu, Shen, and Cao (2026). Write the orbit as two smooth legs \(A\to B\) and \(C\to D\), separated by the upper and lower impulses. The endpoint relations are
\[
x_A=(1+p_1)h_1,\quad x_B=h_2,\quad x_C=(1-p_2)h_2,\quad x_D=h_1,
\]
and
\[
y_C=y_B+\tau_2,\qquad y_D=y_A+\tau_1.
\]
With \(\Delta_1\), \(\Delta_2\), and \(L_2\) exactly as defined in Theorem 3.5, the paper's preceding unsimplified Floquet formula gives
\[
\mu=\Delta_1\Delta_2L_2\,
\frac{y_B(y_A+\tau_1)}{(1+p_1)(1-p_2)y_A(y_B+\tau_2)}.
\]
The final displayed formula in Theorem 3.5 instead uses
\[
\mu_{\rm print}=\Delta_1\Delta_2L_2\,
\frac{1-p_2}{1+p_1}
\frac{(y_A+\tau_1)(y_B+\tau_2)}{y_Ay_B}.
\]
Therefore
\[
\frac{\mu_{\rm print}}{\mu}
=(1-p_2)^2\left(\frac{y_B+\tau_2}{y_B}\right)^2.
\]
The two expressions agree exactly on the codimension-one relation
\[
(1-p_2)(y_B+\tau_2)=y_B.
\]
Away from that relation, the upper-threshold \(x\)- and \(y\)-endpoint ratios in the printed simplification are inverted.

## Assumptions and scope
Assume the order-2 orbit exists, remains in the positive quadrant on both smooth legs, and meets both switching lines transversally, so that the analogue-of-Poincare/Floquet formula used in the source applies. No claim is made here about existence of the orbit, global attraction, grazing cases, or the sign of the stability verdict for every parameter choice. In particular, this result does not assert that the numerical example in the source changes from stable to unstable or conversely.

## Proof
The proof starts from the source's own unsimplified stability expression
\[
\mu=\Delta_1\Delta_2
\exp\left(\int_0^{T_1+T_2}(P_x+Q_y)\,dt\right).
\]
On every positive smooth leg,
\[
\frac{P}{x}=\frac{d}{dt}\log x,
\qquad
\frac{Q}{y}=\frac{d}{dt}\log y.
\]
The quantity \(L_2\) displayed in Theorem 3.5 is the exponential of the remaining terms after subtracting these two logarithmic derivatives from \(P_x+Q_y\). Hence
\[
\mu=\Delta_1\Delta_2L_2
\exp\left(\int\frac{P}{x}\,dt\right)
\exp\left(\int\frac{Q}{y}\,dt\right),
\]
where each integral is taken over both smooth legs.

The \(x\)-endpoint contribution is
\[
\exp\left(\int\frac{P}{x}\,dt\right)
=\frac{x_B}{x_A}\frac{x_D}{x_C}
=\frac{1}{(1+p_1)(1-p_2)}.
\]
The \(y\)-endpoint contribution is
\[
\exp\left(\int\frac{Q}{y}\,dt\right)
=\frac{y_B}{y_A}\frac{y_D}{y_C}
=\frac{y_B(y_A+\tau_1)}{y_A(y_B+\tau_2)}.
\]
Multiplication yields
\[
\mu=\Delta_1\Delta_2L_2\,
\frac{y_B(y_A+\tau_1)}{(1+p_1)(1-p_2)y_A(y_B+\tau_2)}.
\]
Dividing the printed factor in Theorem 3.5 by this expression gives
\[
(1-p_2)^2\left(\frac{y_B+\tau_2}{y_B}\right)^2.
\]
Since all quantities are positive and \(0<p_2<1\) in the bilateral reset, equality of the two formulas is equivalent to \((1-p_2)(y_B+\tau_2)=y_B\).

## Verification
The derivation is symbolic and uses only the endpoint identities of the two impulses and the source's unsimplified divergence formula. The accompanying `verify.py` independently checks the endpoint-product algebra with exact rational arithmetic at a representative admissible set of positive endpoint values and checks the exact ratio and equality condition. The finite check is not used as a proof of the general identity.

## Relationship to prior work
Xu, Shen, and Cao give the general impulsive stability expression immediately before their final simplification, so the corrected factor is obtained without changing their Floquet framework. Their order-1 calculation also explicitly exhibits the same logarithmic-endpoint mechanism. Earlier state-dependent impulsive Leslie–Gower work develops the analogue-of-Poincare stability method, and later impulsive predator-prey papers use the same divergence-based multiplier form, but the inspected literature does not state this source-specific two-leg correction.

A separate prior finding concerning this same 2026 paper addresses a successor-function proof gap for unilateral order-1 existence. It neither states nor implies the bilateral order-2 Floquet correction proved here.

## Limitations
The statement is conditional on a positive transversal order-2 orbit and concerns only the algebraic simplification of its nontrivial Floquet multiplier. It does not prove or disprove the existence conditions in Theorem 3.4, does not cover grazing impacts or nonpositive states, and does not claim a stability-classification reversal for the paper's plotted parameter set. A non-indexed corrigendum or later comment could remain outside the literature searches.

## References
1. J. Xu, H. Shen, X. Cao, “Dynamics of a modified Leslie–Gower model with dual Allee effects under unilateral and bilateral control,” *AIMS Mathematics* 11(6) (2026), 17820–17837. DOI: 10.3934/math.2026726.
2. J. Xu, Y. Tian, H. Guo, X. Song, “Dynamical analysis of a pest management Leslie–Gower model with ratio-dependent functional response,” *Nonlinear Dynamics* 93 (2018), 705–720. DOI: 10.1007/s11071-018-4219-9.
3. “Impulsive Effects and Complexity Dynamics in the Anti-Predator Model with IPM Strategies,” *Mathematics* 12 (2024), 1043. DOI: 10.3390/math12071043.
