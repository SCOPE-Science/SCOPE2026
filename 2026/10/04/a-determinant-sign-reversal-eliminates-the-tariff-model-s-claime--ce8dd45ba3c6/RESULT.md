# A determinant sign reversal eliminates the tariff model’s claimed center regime

## Finding
For the two-population replicator system used in *The tariff game: Is the imposition of reciprocal tariff really a best response?*, write
\[
\dot x=x(1-x)(A_Ay+B_A),\qquad
\dot y=y(1-y)(A_Bx+B_B).
\]
If an interior equilibrium \((x^*,y^*)\in(0,1)^2\) exists, then
\[
A_Ay^*+B_A=0,\qquad A_Bx^*+B_B=0.
\]
The Jacobian there is
\[
J^*=\begin{pmatrix}
0&A_Ax^*(1-x^*)\\
A_By^*(1-y^*)&0
\end{pmatrix},
\]
so
\[
\det J^*=-A_AA_Bx^*(1-x^*)y^*(1-y^*).
\]
The minus sign is absent from Proposition 7.1 of the source. The local classification is therefore the reverse of the printed one: \(A_AA_B>0\) gives a hyperbolic saddle, whereas \(A_AA_B<0\) gives purely imaginary linear eigenvalues and, using the paper’s first integral, a nonlinear center surrounded by closed interior trajectories.

For the tariff model actually defined in the paper, the coefficients satisfy
\[
A_I=S_I+\operatorname{exp}^I(0)+\operatorname{exc}^I(0)\ge 0,
\]
where \(S_I\ge0\) and the other two terms are free-trade producer and consumer surpluses. At an interior equilibrium \(A_I\ne0\), so \(A_A>0\) and \(A_B>0\). Hence every interior equilibrium admitted by the stated tariff model is a saddle. In particular, the center and persistent closed-orbit regime asserted under \(A_AA_B>0\) cannot occur in this model.

## Assumptions and scope
The object is system (12) of Accinelli, Muñiz, Quintas, and Salas, with \(x\) and \(y\) denoting the shares or probabilities of tariff adoption in the two countries. The claim assumes an interior equilibrium exists and uses only the source’s displayed replicator equations, coefficient definitions, and first integral. The surplus terms are the source’s free-trade producer and consumer surpluses, defined by integrals over equilibrium traded quantities; they are nonnegative, and the source assumes nonnegative subsidies.

The correction concerns the dynamic classification of an interior equilibrium. It does not alter the static payoff matrix, the existence formula \((x^*,y^*)=(-B_B/A_B,-B_A/A_A)\), or the source’s conclusions for cases with a unique pure Nash equilibrium.

## Proof
Differentiate the vector field. At an interior equilibrium, the two payoff-difference factors vanish, so the diagonal entries of the Jacobian vanish and the off-diagonal entries are
\[
a=A_Ax^*(1-x^*),\qquad b=A_By^*(1-y^*).
\]
Therefore
\[
J^*=\begin{pmatrix}0&a\\ b&0\end{pmatrix},\qquad
\det J^*=-ab,
\]
which gives
\[
\det J^*=-A_AA_Bx^*(1-x^*)y^*(1-y^*).
\]
Because \(x^*(1-x^*)y^*(1-y^*)>0\), the sign of the determinant is the *opposite* of the sign of \(A_AA_B\). Equivalently, the characteristic equation is
\[
\lambda^2-A_AA_Bx^*(1-x^*)y^*(1-y^*)=0.
\]
Thus \(A_AA_B>0\) produces two real eigenvalues of opposite signs and a hyperbolic saddle.

For \(A_AA_B<0\), linearization alone gives a purely imaginary pair. The source’s Appendix 9 supplies the first integral
\[
H(x,y)=A_B\bigl[x^*\log x+(1-x^*)\log(1-x)\bigr]
-A_A\bigl[y^*\log y+(1-y^*)\log(1-y)\bigr].
\]
A direct differentiation along the vector field gives \(\dot H=0\). At the interior equilibrium,
\[
H_{xx}(x^*,y^*)=-\frac{A_B}{x^*(1-x^*)},\qquad
H_{yy}(x^*,y^*)=\frac{A_A}{y^*(1-y^*)},\qquad H_{xy}=0.
\]
If \(A_AA_B<0\), these two diagonal Hessian entries have the same sign, so \(H\) has a strict extremum at the equilibrium. The two logarithmic brackets tend to \(-\infty\) on their corresponding boundary faces; because their coefficients have the same sign when \(A_AA_B<0\), finite regular level sets sufficiently near the extremum stay in the open square and are closed curves. The nonstationary planar flow on each such level curve is periodic. This is the center case, with the opposite sign from the source’s statement.

In the paper’s tariff model,
\[
A_A=S_A+\operatorname{exp}^A(0)+\operatorname{exc}^A(0),\qquad
A_B=S_B+\operatorname{exp}^B(0)+\operatorname{exc}^B(0).
\]
Each term is nonnegative by construction. An interior equilibrium formula divides by both \(A_A\) and \(A_B\), so an actual interior equilibrium requires both coefficients to be nonzero and therefore positive. Thus \(A_AA_B>0\) throughout the interior-equilibrium regime of the stated tariff model, forcing a saddle. Under the coordination conditions in Proposition 5.1, \(B_I<0<A_I+B_I\) already implies \(A_I>0\) directly. The paper’s later Section 7.4 correspondingly describes the coordination equilibrium as a saddle whose stable manifold separates the two pure-equilibrium basins; that later statement is consistent with the corrected determinant, not with Proposition 7.1.

## Verification
A minimal exact witness takes \(A_A=A_B=1\) and \(B_A=B_B=-1/2\), for which \(x^*=y^*=1/2\). Then
\[
J^*=\begin{pmatrix}0&1/4\\ 1/4&0\end{pmatrix},\qquad
\det J^*=-1/16,
\]
with eigenvalues \(1/4\) and \(-1/4\). The printed determinant sign would instead give \(+1/16\) and incorrectly label this point a center.

The accompanying `verify.py` checks this witness with exact rational arithmetic, checks \(\dot H=0\) at several independent rational states using the analytic gradient of the first integral, and checks the Hessian sign pattern for both sign regimes. Running it returns `VERIFY_OK`.

## Relationship to prior work
The motivating article prints the replicator system, the interior equilibrium, the Jacobian, Proposition 7.1, Proposition 7.2, and the Appendix 9 first integral. Proposition 7.1 omits the minus sign in the determinant of a zero-diagonal \(2\times2\) matrix and consequently reverses the local classification. Appendix 9 then assigns closed level curves to the same wrong sign. The paper’s later Section 7.4, however, states that the coordination mixed equilibrium is a saddle separating the basins of the two pure equilibria; that special-case description agrees with the correction and exposes an internal inconsistency.

The corrected qualitative phase portrait is standard in two-population two-strategy replicator theory. Szabó and Fáth’s review classifies the bi-matrix coordination case as a saddle class and the matching-pennies-type case as a center class. That prior general theory does not identify the sign error in the 2026 tariff article or the source-specific consequence that its own coefficient definitions force \(A_A,A_B>0\), eliminating the claimed center regime.

## Limitations
This finding diagnoses and corrects the interior-equilibrium stability classification of the printed continuous-time replicator model. It does not claim that every policy conclusion in the article fails, does not alter the static welfare accounting, and does not address alternative adaptive dynamics. The closed-orbit statement for \(A_AA_B<0\) is a property of the generic two-population system; the tariff coefficients defined in the source do not realize that sign regime at an interior equilibrium.

## References
1. E. Accinelli, H. Muñiz, L. Quintas, and O. Salas, “The tariff game: Is the imposition of reciprocal tariff really a best response?”, *Journal of Dynamics and Games*, early access 2026. DOI: 10.3934/jdg.2026036.
2. G. Szabó and G. Fáth, “Evolutionary games on graphs”, *Physics Reports* 446 (2007), 97–216. DOI: 10.1016/j.physrep.2007.04.004.
