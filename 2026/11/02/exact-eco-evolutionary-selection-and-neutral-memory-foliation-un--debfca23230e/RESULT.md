# Exact eco-evolutionary selection and neutral-memory foliation under constant aggregate payoffs

## Finding

In a predator-dependent two-prey replicator flow, the **aggregate birth and capture rates can be independent of prey composition even when the individual prey have genuinely different birth and capture payoffs**. On this natural balanced-payoff family, the complete three-population asymptotics admit an exact solution for the prey-composition odds. There is a sharp threshold separating fixation of opposite prey types; at equality a whole normally attracting coexistence segment survives. Which point on that segment is selected is given exactly by the initial prey and predator totals.

Put \(P=A+B\), \(x=A/P\), and define
\[
P_* = 1/\delta,\qquad Y_* = \frac{r-1/(K\delta)}{\delta},\qquad c=e-gY_*.
\]
For every strictly positive initial state and every \(t\geq0\),
\[
\boxed{\frac{x(t)}{1-x(t)}=\frac{x_0}{1-x_0}
\left(\frac{P(t)}{P_0}\right)^{g/\delta}
\left(\frac{Y(t)}{Y_0}\right)^{g/(K\beta\delta^2)}e^{ct}.}
\]
In particular, \(c>0\) implies \(x\to1\), while \(c<0\) implies \(x\to0\). At \(c=0\), the entire segment \(\{(A,B,Y)=(xP_*,(1-x)P_*,Y_*):0\leq x\leq1\}\) consists of equilibria and each positive orbit converges to exactly one of them, whose frequency \(x_\infty\) satisfies
\[
\boxed{\frac{x_\infty}{1-x_\infty}=\frac{x_0}{1-x_0}
\left(\frac{P_*}{P_0}\right)^{g/\delta}
\left(\frac{Y_*}{Y_0}\right)^{g/(K\beta\delta^2)}.}
\]
The threshold \(e_c=gY_*\) lies strictly inside the admissible interval \((0,r)\).

## Assumptions and scope

Let \(r,\delta,K,\beta>0\), \(0<e<r\), \(0<g<\delta\), and \(Kr\delta>1\). The reproduction and predation payoff matrices in the model of Braga–Wardil, as written by Cruz–Neves, are
\[
M_R=\begin{pmatrix}r&r+e\\r-e&r\end{pmatrix},\qquad
M_P=\begin{pmatrix}\delta&\delta+g\\\delta-g&\delta\end{pmatrix}.
\]
Every entry is strictly positive. For \(A(0),B(0),Y(0)>0\), the original variables obey
\[
\begin{aligned}
\dot A&=A\left[\frac{rA+(r+e)B}{A+B}-\frac{A+B}{K}
-Y\frac{\delta A+(\delta+g)B}{A+B}\right],\\
\dot B&=B\left[\frac{(r-e)A+rB}{A+B}-\frac{A+B}{K}
-Y\frac{(\delta-g)A+\delta B}{A+B}\right],\\
\dot Y&=\beta Y\left[-1+\frac{\delta A+(\delta+g)B}{A+B}A
+\frac{(\delta-g)A+\delta B}{A+B}B\right].
\end{aligned}
\]
All limits and classifications are forward-time statements for strictly positive initial populations. The boundary initial conditions are not asserted to be in the same interior convergence class.

## Proof

**1. Balanced payoff cancellation.** For \(x=A/P\), the individual reproduction rates are \(r+e(1-x)\) and \(r-ex\), and their capture rates are \(\delta+g(1-x)\) and \(\delta-gx\). Hence their population averages are exactly \(r\) and \(\delta\), and their individual differences exactly \(e\) and \(g\). Therefore the complete three-dimensional system is conjugate on the strictly positive cone to
\[
\dot x=x(1-x)(e-gY),\qquad
\dot P=P(r-P/K-\delta Y),\qquad
\dot Y=\beta Y(-1+\delta P).
\tag{1}
\]
The last two equations are independent of \(x\); positive solutions cannot cross any coordinate face.

**2. Global convergence of the ecological subsystem.** The positive equilibrium is uniquely \((P_*,Y_*)\), as defined above. Let \(\Phi(u;u_*)=u-u_*-u_*\log(u/u_*)\), and use
\[
V(P,Y)=\Phi(P;P_*)+\beta^{-1}\Phi(Y;Y_*).
\]
Direct differentiation yields the exact identity
\[
\dot V=-\frac{(P-P_*)^2}{K}\leq0.
\]
Positive sublevel sets are compact within the positive quadrant, so the flow is globally forward-complete and precompact there. The only invariant subset of \(\{P=P_*\}\) is \((P_*,Y_*)\): otherwise \(\dot P=-\delta P_*(Y-Y_*)\ne0\). LaSalle's principle gives \((P(t),Y(t))\to(P_*,Y_*)\) for all positive initial data. The Jacobian there has trace \(-P_*/K<0\) and determinant \(\beta\delta^2P_*Y_*>0\), so the convergence is eventually exponential.

**3. Exact composition law.** The first equation in (1) gives \(\frac{d}{dt}\log\frac{x}{1-x}=e-gY\). Substitute the ecological logarithmic derivatives:
\[
\frac{d}{dt}\log P=r-P/K-\delta Y,\qquad
\frac{d}{dt}\log Y=\beta(\delta P-1).
\]
Eliminating \(P\) and \(Y\) gives the *exact cohomological identity*
\[
\frac{d}{dt}\left[
\log\frac{x}{1-x}-\frac{g}{\delta}\log P
-\frac{g}{K\beta\delta^2}\log Y\right]=e-gY_*=c.
\]
Integration proves the boxed all-time odds equation. Since \(P,Y\) approach strictly positive limits, the factors multiplying \(e^{ct}\) approach a finite strictly positive number. Thus the sign of \(c\) selects a boundary equilibrium, with the exact logarithmic odds drift rate \(c\).

**4. Neutral segment and global memory.** When \(c=0\), the bracket in the last display is a first integral. Its finite limit gives the second boxed formula. The limit \(x_\infty\) is strictly between zero and one for every positive initial datum. Every point on the stated segment is a fixed state, and no other positive fixed state exists. The linearization along this segment is block triangular, with one tangent zero eigenvalue and two strictly negative-real-part ecological eigenvalues. Thus the segment is normally attracting; the explicit conserved quantity defines its global positive stable foliation. Since all positive trajectories converge to fixed states, no nonconstant positive periodic or compact recurrent trajectories exist.

**5. Feasibility of the sharp threshold.** Since \(Kr\delta>1\) and \(0<g<\delta\),
\(0<e_c=g(r-1/(K\delta))/\delta<r\). Hence every regime, including true neutrality with distinct individual payoff rates, occurs with strictly positive payoff matrices.

## Verification

The accompanying standalone `check.py` checks the four payoff cancellations, the invariant derivative, and the Lyapunov identity by symbolic algebra. It then numerically integrates three parameter cases on opposite sides and at the neutral threshold, checks the exact finite-time identity against 35 time samples, and verifies the asymptotic selection. A concrete neutral example is \(r=2\), \(\delta=1\), \(K=2\), \(\beta=1\), \(g=2/5\), \(e=3/5\) with \((x_0,P_0,Y_0)=(3/10,2,1/2)\); it converges to \(P_*=1\), \(Y_*=3/2\) and \(x_\infty\approx0.2880580664\), in agreement with the exact formula. Finite integration is illustrative; the full assertion is proved above.

To reproduce: run `python check.py` with Python, SymPy, NumPy and SciPy installed. The script exits with a failure if any analytical assertion or sampled numerical assertion fails.

## Relationship to prior work

Braga and Wardil (2021/2022) introduced the predator-dependent replicator system and identified evolutionary scenarios. Cruz and Neves (2026), sections 2–7 and Appendix A, established the frequency-dependent ecological decomposition, equilibrium and bifurcation analysis, and globally attracting positive equilibria for the *ordinary* two-dimensional logistic Lotka–Volterra subsystem. These prior facts are not claimed as new. The present theorem makes a special but natural balanced-payoff choice for which the ecological projection becomes exactly autonomous while individual prey rates remain distinct; the *new global statement* is the exact composition invariant, the initial-condition-to-limit selection formula, and the resulting entire normally attracting neutral-coexistence foliation. The known two-dimensional convergence theorem alone does not determine which prey survives or how its neutral composition depends on transient predator history. A related published study proves local stability exchange at nondegenerate boundary collisions, rather than this global degenerate neutral manifold.

## Limitations

The payoff cancellation imposes relations on the matrices: if aggregate reproduction or capture rates depend on composition, the exact formula and neutral foliation need not hold. The theorem assumes predators persist, \(Kr\delta>1\). It does not claim persistence under perturbations that break payoff balance: neutrality is codimension one within this balanced family. The exact compositional asymptotics concern deterministic solutions, not demographic noise or stochastic extinction. Priority remains subject to specialized literature outside the inspected full texts and accessible indexed records.

## References

1. H. M. Cruz and A. G. M. Neves, *Predator-dependent replicator dynamics or a predator-prey model with two prey types and frequency dependence*, arXiv:2607.13281v1, first posted 2026-07-14. https://arxiv.org/abs/2607.13281
2. I. Braga and L. Wardil, *The predator-dependent replicator dynamics*, Journal of Physics A: Mathematical and Theoretical **55** (2022), 025601, DOI:10.1088/1751-8121/ac40e4. Original article publicly available by 2021-12. https://doi.org/10.1088/1751-8121/ac40e4
3. *A determinant-sign proof of stability exchange in the predator-dependent replicator model* (2026), published mathematical research record; scope: nondegenerate boundary stability exchange rather than balanced-payoff neutral global selection.
