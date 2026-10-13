# Free-trade dominance forced by the bilateral tariff welfare matrix

## Finding

**Theorem (exact welfare-table dynamics).** Consider the two-country, two-action payoff table in Section 5.1 of Accinelli–Muñiz–Quintas–Salas [1] with no export subsidies. Let \(T\) mean impose a tariff and \(F\) mean refrain. Let \(D_A,D_B>0\) denote each country's own-tariff deadweight welfare loss; let \(L_A,L_B\) denote the respective losses of export surplus when the *other* country imposes a tariff. The table is, in row–column order \((T,F)\) for each player,

\[
U_A=\begin{pmatrix}-D_A-L_A&-D_A\\-L_A&0\end{pmatrix},\qquad
U_B=\begin{pmatrix}-D_B-L_B&-L_B\\-D_B&0\end{pmatrix}.
\]

Then for every opponent's pure or mixed action, \(F\) strictly dominates \(T\) for both countries, with payoff differences exactly \(-D_A\) and \(-D_B\). The **unique Nash equilibrium** is \((F,F)\). If \(x\) and \(y\) are the tariff probabilities of countries A and B, the associated two-population replicator dynamics are

\[
\dot x=-D_A x(1-x),\qquad \dot y=-D_B y(1-y).
\]

Every solution with \((x(0),y(0))\in(0,1)^2\) converges to \((0,0)\), with the exact formulas

\[
x(t)=\frac{x_0}{x_0+(1-x_0)e^{D_A t}},\qquad
y(t)=\frac{y_0}{y_0+(1-y_0)e^{D_B t}}.
\]

In particular there are no mixed Nash equilibria, distinct interior attracting policy states, or nonconstant periodic trajectories in this *welfare-table* game. Moreover, this table cannot produce the nonzero cross-strategy coefficients asserted for it in Eq. (8) of [1] when the paper's baseline export-industry producer surpluses are strictly positive. This establishes a structural incompatibility between the posted welfare table and the paper's coupled replicator model, rather than a claim about all conceivable tariff games.

## Assumptions and scope

The theorem uses only the displayed Section 5.1 national-welfare payoff matrix and the standard binary-strategy replicator rule stated in Eq. (11) of [1], **with \(S_A=S_B=0\)**. Deadweight losses are strictly positive, as stipulated for positive, distortionary tariffs in [1]; foreign-tariff export-loss quantities may be any fixed real numbers, although the motivating setting takes them nonnegative. These are fixed, one-shot payoffs: no strategic terms-of-trade gains, repeated-game punishments, political objective, market power, or state-dependent endogenous losses are appended. This is exactly the mathematical scope of the table as printed.

The replicator variables range over the closed square \([0,1]^2\). The **attraction assertion** is for the open square, since strategies absent initially remain absent under replicator dynamics and all corners are stationary even when not Nash equilibria. The comparative statement about Eq. (8) uses the separate, explicit source assumption of positive pre-tariff exporting-producer surplus.

## Proof

From the table, country A's payoff with tariff when B chooses tariff with probability \(y\) is \(-D_A-yL_A\), and its payoff without tariff is \(-yL_A\). Their difference is \(-D_A<0\), independent of \(y\). Analogously B's payoff difference between tariff and no tariff is \(-D_B<0\), independent of A's tariff probability \(x\). Thus the no-tariff action is strictly dominant for both, proving the unique Nash equilibrium.

The binary-strategy replicator identity is \(\dot x=x(1-x)[\pi_A(T;y)-\pi_A(F;y)]\), and analogously for \(y\); substituting the differences gives the two uncoupled logistic decay equations. Separation of variables (or direct differentiation) gives the displayed exact solutions, valid for \(0<x_0,y_0<1\) and every \(t\ge0\). Each denominator grows exponentially, so both tariff frequencies decay to zero. The flow stays strictly inside the open square for every finite time; both components strictly decrease there, excluding nonconstant interior periodic orbits. The strict-dominance result independently excludes mixed Nash equilibria. On the boundary, initial coordinates exactly zero or one remain fixed, so there is no claim of convergence from every boundary state.

For coefficient compatibility, any affine payoff-gap representation of the displayed table must have \(\pi_A(T;y)-\pi_A(F;y)=A_Ay+B_A=-D_A\), hence \(A_A=0\) and \(B_A=-D_A\), with corresponding \(A_B=0\), \(B_B=-D_B\). In contrast, Eq. (8) of [1] explicitly prints \(A_I=S_I+\operatorname{exp}^{I}(0)+\operatorname{exc}^{I}(0)\). Under the no-subsidy assumption \(S_I=0\), positive initial exporting producer surplus \(\operatorname{exp}^{I}(0)>0\), and nonnegative initial domestic consumer surplus \(\operatorname{exc}^{I}(0)\ge0\), these coefficients are strictly positive. They therefore cannot be the slopes of the table's payoff differences. This is an algebraic comparison of two separately printed expressions, not an assumption that the affine system is itself impossible as a different game.

## Verification

`verify.py` uses exact symbolic matrix calculations to reconstruct both expected payoff differences, show both derivatives with respect to the opponent's policy frequency vanish, check the unique logistic solution by differentiation, and compare the forced zero slopes with the nonzero expressions in [1]. It also independently checks the correct determinant sign of the coupled system's Jacobian at any interior stationary state; that last check is secondary and not required for the theorem. Execute `python verify.py` with SymPy installed. The actual test returned `VERIFY_OK`.

## Relationship to prior work

The explicit matrix, welfare definitions, no-subsidy benchmark and the stated coupled replicator rule are from [1] (Sections 5.1, 5.2 and 7.1). The same paper discusses a general *conditional* free-trade regime, but also asserts a no-subsidy prisoner-dilemma tariff equilibrium and multiple dynamical regimes based on a different, state-dependent payoff-gap formula. A conditional standard 2-by-2 dominance observation is not equivalent to the present **unconditional derivation from the very welfare table**: the published table fixes both strategic cross-effects to zero, contradicting those independently printed coefficients for positive baseline surplus. The standard replicator calculation is not claimed as a novel general theorem; the source-specific compatibility obstruction and its sharp dynamical consequence constitute the finding.

Martins–Pinto–Zubelli [2] consider a different, endogenous strategic tariff game in which prisoner-dilemma equilibria can occur. Passacantando–Raciti [3] study variable tariff quotas through generalized Nash equilibria and variational inequalities, not the exact additive two-action welfare matrix of [1]. Such related tariff-game models do not imply the incompatibility in the particular printed table, nor are they ruled out by it.

## Limitations

This result evaluates the equations as published; it does not establish which formula the authors intended, which model was simulated, or whether richer policy objectives could support retaliation. The payoff table may be a deliberately simplified welfare accounting rather than a comprehensive political-economy model. It establishes attraction only from the interior of the strategy-probability square; replicator boundary points are invariant. No empirical, causal, or policy-optimality conclusion for real tariffs follows. Independent audit has not been performed.

## References

1. E. Accinelli, H. Muñiz, L. Quintas, and O. Salas, “The tariff game: Is the imposition of reciprocal tariff really a best response?”, *Journal of Dynamics and Games*, early access June 8, 2026, DOI: 10.3934/jdg.2026036. Sections 5.1, 5.2, 7, 8, and Appendix 9. Full text: https://www.researchgate.net/publication/406398478_The_tariff_game_Is_the_imposition_of_reciprocal_tariff_really_a_best_response ; publisher: https://www.aimsciences.org/article/doi/10.3934/jdg.2026036 .
2. F. Martins, A. A. Pinto, and J. P. Zubelli, “Nash and social welfare impact in an international trade model”, *Journal of Dynamics and Games* **4** (2017), 149–173, DOI: 10.3934/jdg.2017009.
3. M. Passacantando and F. Raciti, “A game theory model of tariff rate quotas in international trade”, *Journal of Dynamics and Games* **13** (2026), 72–90, DOI: 10.3934/jdg.2025011.
