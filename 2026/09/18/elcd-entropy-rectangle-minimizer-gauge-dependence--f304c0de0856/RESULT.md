# Exact entropy-rectangle minimization and gauge dependence of ELCD corner selection

## Statement

Consider the ideal-gas mathematical entropy used in the entropy-based local characteristic decomposition (ELCD) of Chu, Herty and Kurganov,
\[
\eta_0(\rho,p)
=-\frac{\rho}{\gamma-1}\log\!\left(\frac{p}{\rho^\gamma}\right),
\qquad \gamma>1,\quad \rho,p>0.
\]
More generally, allow the physically immaterial additive constant in specific entropy,
\[
\eta_C(\rho,p)
=-\frac{\rho}{\gamma-1}
\left[\log\!\left(\frac{p}{\rho^\gamma}\right)+C\right]
=\frac{\rho}{\gamma-1}
\bigl(\gamma\log\rho-\log p-C\bigr).
\]
Let
\[
R=[\rho_-,\rho_+]\times[p_-,p_+],
\qquad 0<\rho_-\le\rho_+,
\quad 0<p_-\le p_+.
\]
Then the continuous minimization problem over the full rectangle has the exact solution
\[
\boxed{
 p^*=p_+,
 \qquad
 \rho^*=\Pi_{[\rho_-,\rho_+]}
 \left(e^{-1+C/\gamma}p_+^{1/\gamma}\right),
}
\]
where \(\Pi\) denotes interval projection. In particular, whenever
\[
\rho_-<e^{-1+C/\gamma}p_+^{1/\gamma}<\rho_+,
\]
the minimizer lies in the relative interior of the top edge of the rectangle and has strictly smaller entropy than all four corners.

This corrects the convexity argument used in arXiv:2609.19838. That paper states that the interface state is obtained by minimizing entropy within the \((\rho,p)\)-rectangle and then concludes that, because the entropy is convex, it suffices to compare the four corners. Convexity does not imply that a minimum over a polytope occurs at a vertex. The implemented four-corner rule is therefore a different discrete selection rule from continuous rectangle minimization.

A second structural issue is that the four-corner rule is not invariant under the natural additive normalization of specific entropy. The shift \(C\) leaves the Hessian of \(\eta_C\) unchanged and corresponds to adding a multiple of the conserved mass density to the entropy pair, but it can change which density endpoint minimizes the corner values. Thus raw entropy-density ranking of states with different densities depends on an arbitrary entropy gauge.

## Strict convexity and the exact minimizer

Direct differentiation gives
\[
\nabla^2\eta_C(\rho,p)
=\frac1{\gamma-1}
\begin{pmatrix}
\gamma/\rho & -1/p\\
-1/p & \rho/p^2
\end{pmatrix},
\]
with
\[
\det\nabla^2\eta_C
=\frac1{(\gamma-1)p^2}>0.
\]
Hence \(\eta_C\) is strictly convex on the positive \((\rho,p)\)-quadrant for every \(C\). However,
\[
\partial_p\eta_C=-\frac{\rho}{(\gamma-1)p}<0,
\]
so any rectangle minimizer must lie at \(p=p_+\). Along that edge,
\[
\partial_\rho\eta_C(\rho,p_+)
=\frac{\gamma\log\rho+\gamma-\log p_+-C}{\gamma-1}.
\]
The unique unconstrained minimizer is therefore
\[
r_C=e^{-1+C/\gamma}p_+^{1/\gamma},
\]
and projection onto the allowed density interval gives the displayed formula.

There is also an exact expression for the loss incurred by replacing the interior minimizer by another density. When \(r_C\in(\rho_-,\rho_+)\), set \(x=\rho/r_C\). Then
\[
\boxed{
\eta_C(\rho,p_+)-\eta_C(r_C,p_+)
=\frac{\gamma r_C}{\gamma-1}
\bigl(x\log x-x+1\bigr).
}
\]
Since \(x\log x-x+1\ge0\), with equality only at \(x=1\), this quantifies the strict corner excess.

## The four-corner rule reduces to two endpoints

For each fixed density, entropy is strictly decreasing in pressure. Consequently, among the four corners of \(R\), the two corners with pressure \(p_-\) can never beat their same-density counterparts at \(p_+\). Thus the source four-corner comparison is algebraically equivalent to comparing only
\[
\eta_C(\rho_-,p_+)
\quad\text{and}\quad
\eta_C(\rho_+,p_+).
\]

The crossover has a closed form. For \(0<a<b\), define the identric mean
\[
I(a,b)
=\exp\!\left(
\frac{b\log b-a\log a}{b-a}-1
\right).
\]
Then
\[
\boxed{
\eta_C(a,p_+)=\eta_C(b,p_+)
\iff
r_C=I(a,b).
}
\]
Moreover, the corner rule selects \(a\) when \(r_C<I(a,b)\), and \(b\) when \(r_C>I(a,b)\). Equivalently, the endpoint selected by the corner heuristic flips at
\[
\boxed{
C_{\rm flip}
=\gamma\frac{b\log b-a\log a}{b-a}-\log p_+.
}
\]
This formula makes the normalization dependence explicit.

## A concrete ideal-gas counterexample

Take the value \(\gamma=1.4\) used in the numerical experiments of arXiv:2609.19838 and the rectangle
\[
\rho\in[0.1,1],\qquad p\in[0.8,1],\qquad C=0.
\]
Then
\[
r_0=e^{-1}=0.367879441171442\ldots
\]
lies strictly inside the density interval, so the true rectangle minimizer is
\[
(\rho^*,p^*)=(e^{-1},1).
\]
The relevant entropy values are
\[
\eta_0(0.1,1)=-0.805904782547916\ldots,
\]
\[
\eta_0(e^{-1},1)=-1.287578044100048\ldots,
\]
\[
\eta_0(1,1)=0.
\]
Thus the best corner is worse than the actual rectangle minimum by
\[
0.481673261552132\ldots.
\]
For these same density endpoints,
\[
I(0.1,1)=0.475134569010839\ldots,
\]
and the four-corner choice flips at
\[
C_{\rm flip}=0.358179903354629\ldots.
\]
At \(C=0\) the lower-density endpoint is selected, while at \(C=1\) the higher-density endpoint is selected.

## Why the entropy gauge is mathematically immaterial to Euler but not to the selector

For the Euler equations, the specific thermodynamic entropy is defined only up to an additive constant. Harten, Lax, Levermore and Morokoff explicitly note this normalization freedom. In the present convention, changing the specific entropy by \(C\) changes the mathematical entropy density by
\[
\eta_C=\eta_0-\frac{C}{\gamma-1}\rho.
\]
Because mass is itself conserved,
\[
\rho_t+\nabla\!\cdot(\rho u)=0,
\]
adding \(a\rho\) to an entropy density and \(a\rho u\) to its entropy flux preserves the entropy-pair identity for smooth solutions and the corresponding distributional inequality. It also leaves the entropy Hessian unchanged.

Therefore \(\eta_C\) and \(\eta_0\) represent the same convexity and admissibility structure, but an argmin over candidate states of different densities need not be the same. In general, if an entropy density is changed by a linear combination of conserved quantities, pairwise raw entropy differences acquire the corresponding linear state differences. A selection rule based on the absolute value of the entropy density is consequently not invariant under this standard affine entropy-pair equivalence.

The same issue can be viewed through nondimensionalization. Changing reference scales inside the logarithm can add a constant to the specific entropy and hence a term proportional to \(\rho\) to the entropy density. Unless a normalization convention is treated as part of the numerical method, the selected corner may change under an otherwise immaterial reference choice.

## Numerical-algorithm consequence

If the intended subproblem is genuinely
\[
\min_{(\rho,p)\in R}\eta_C(\rho,p),
\]
then its \((\rho,p)\)-solution requires no multidimensional optimization or corner enumeration: it is given by the closed form above. This does not by itself define a complete replacement ELCD state, because the entropy is independent of velocity and an interior density does not specify how the velocity components should be chosen. A modified ELCD would need an additional, explicitly stated velocity rule and numerical validation.

If instead the intended method is exactly the discrete four-corner heuristic implemented in Algorithm 1 of the source paper, then the calculus result does not invalidate that heuristic as a numerical choice; it invalidates the claim that convexity makes it equivalent to minimization over the full rectangle. In that discrete interpretation, only two corner entropy evaluations are necessary, and the gauge-dependence theorem still applies.

## Reproducibility

`artifacts/verify_entropy_rectangle.py` uses only the Python standard library. It evaluates the explicit counterexample and gauge crossover, checks the exact excess identity, and compares the analytic rectangle minimizer against dense grids on 50 deterministic random positive rectangles. `artifacts/verification_output.txt` records the output.

## Originality boundary

The ELCD construction, the ideal-gas entropy formula, the four-corner algorithm, and the numerical evidence reported for ELCD are from Chu, Herty and Kurganov. Convex Euler entropies, the additive normalization freedom of specific entropy, and entropy-pair equivalence under addition of conserved linear quantities are standard. The identric mean is also classical.

The contribution here is restricted to the exact minimizer of the particular ELCD entropy over its stated \((\rho,p)\)-rectangle, the resulting open family of interior-minimum counterexamples to the convexity-to-corners claim, the two-corner reduction and identric crossover formula, and the explicit demonstration that the ELCD raw-entropy corner selector depends on the additive entropy gauge. Searches by the preprint identifier and title, the rectangle/corner formulation, entropy normalization, and equivalent minimization formulations found no inspected prior correction or statement of these formulas. Originality is claimed only to the best of our knowledge.

## Limitations

This result is an analytic correction and structural diagnostic, not an empirical comparison of competing interface-state selectors. It does not show that the published ELCD numerical experiments are inaccurate, unstable, or inferior to arithmetic averaging. A four-corner heuristic may remain useful even though it is not the continuous rectangle minimizer. The closed-form minimizer is specific to the ideal-gas entropy used in the source paper. The gauge-dependence objection is broader, but this record does not propose or benchmark a definitive gauge-invariant replacement. An exact rectangle minimizer determines only density and pressure; a complete interface state still requires a velocity prescription. Floating-point tie handling and near-vacuum regularization are also outside the present analysis.

## References

1. S. Chu, M. Herty, A. Kurganov, *Entropy-Based Local Characteristic Decomposition*, arXiv:2609.19838 (2026). https://arxiv.org/abs/2609.19838
2. A. Harten, P. D. Lax, C. D. Levermore, W. J. Morokoff, *Convex Entropies and Hyperbolicity for General Euler Equations*, SIAM Journal on Numerical Analysis 35(6), 2117–2127 (1998). https://doi.org/10.1137/S0036142997316700
3. E. Tadmor, *A Minimum Entropy Principle in the Gas Dynamics Equations*, Applied Numerical Mathematics 2, 211–219 (1986).
