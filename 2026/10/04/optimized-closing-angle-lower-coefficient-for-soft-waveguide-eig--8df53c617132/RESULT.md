# Optimized closing-angle lower coefficient for soft-waveguide eigenvalue accumulation
## Finding
Consider the soft-waveguide Hamiltonian of Exner--Spitzkopf with a positive finite transverse measure \(\mu_\perp\), asymptotic half-separation \(\rho>0\), and closing angle deficit \(\beta\in(0,\pi/2)\). Let \(e_\rho=\epsilon_{\mu_\perp,\rho}\) be the ground energy of the symmetric double-well transverse operator and \(e=\epsilon_{\mu_\perp}\) the single-well ground energy. For any fixed \(\nu\in(e_\rho,e)\), define
\[
N_\beta(\nu)=\dim\mathbf 1_{(-\infty,\nu)}(H_{\Gamma,\mu}).
\]
Write \(\phi_\rho\) for the double-well ground state and \(\eta_\rho=|\phi_\rho(0)|/\|\phi_\rho\|\). Put \(\Delta=\nu-e_\rho\), \(a=-\nu\), and \(q=\Delta/a\). Then
\[
\liminf_{\beta\downarrow0}\beta N_\beta(\nu)\ge C_\star(\nu),
\]
with
\[
y_\star=\frac{q-3+\sqrt{(q+1)(q+9)}}4,
\qquad
C_\star(\nu)=\frac{2y_\star}{\pi\eta_\rho^2}
\sqrt{\frac{\Delta-a y_\star}{1+y_\star}}.
\]
The constant is the exact maximum produced by the trial family used in the source when the longitudinal length obeys \(L\tan(\beta/2)\to x\in(0,\infty)\).

For the leaky profile \(\mu_\perp=\alpha\delta_0\), let \(\kappa>\alpha/2\) be the unique solution of
\[
2\kappa=\alpha\bigl(1+e^{-2\kappa\rho}\bigr).
\]
Then
\[
e_\rho=-\kappa^2,
\qquad
\eta_\rho^2=\left(\rho+\frac1{2\kappa-\alpha}\right)^{-1},
\]
so the lower coefficient is an explicit function of \(\alpha,\rho,\nu\).

## Assumptions and scope
The geometric and measure hypotheses are exactly assumptions (a), (b), and (e) in Exner--Spitzkopf. In particular, the curved part is compact, the two straight arms have angle deficit \(\beta\), the transverse measure is positive and compactly supported, and the parallel-coordinate strip is injective. The source proves \(e_\rho<e<0\), \(e_{\rho_\beta}\to e_\rho\), and \(\eta_{\rho_\beta}\to\eta_\rho>0\) as \(\beta\downarrow0\), where \(\rho_\beta=\rho\sec(\beta/2)\).

The counting function here is the entire spectral projection below \(\nu\). Since \(\nu<e\), these states lie below the essential-spectrum threshold for every positive \(\beta\). No claim is made that all counted states lie above \(e_\rho\), and no upper asymptotic is asserted.

## Proof
Let \(t_\beta=\tan(\beta/2)\). Equations (3.1)--(3.6) of the primary source give, for the published trial family with longitudinal interval length \(L\), negativity of the shifted quadratic form below \(\nu\) whenever the Dirichlet longitudinal quotient is smaller than
\[
R_\beta(L)=\frac{\nu-e_{\rho_\beta}+\nu\eta_{\rho_\beta}^2Lt_\beta}
{1+\eta_{\rho_\beta}^2Lt_\beta}.
\]
Choose a fixed \(x>0\) and set \(L_\beta=x/t_\beta\). Using the limits quoted above,
\[
R_\beta(L_\beta)\longrightarrow
R_0(x)=\frac{\Delta-a\eta_\rho^2x}{1+\eta_\rho^2x}.
\]
Thus \(R_0(x)>0\) precisely for
\[
0<x<\frac{\Delta}{a\eta_\rho^2}.
\]
For such an \(x\), the number \(m_\beta(x)\) of Dirichlet modes satisfying \((\pi n/L_\beta)^2<R_\beta(L_\beta)\) obeys
\[
m_\beta(x)=\frac{L_\beta}{\pi}\sqrt{R_\beta(L_\beta)}+O(1).
\]
The min--max principle applied to this trial subspace gives \(N_\beta(\nu)\ge m_\beta(x)\). Since \(\beta/t_\beta\to2\),
\[
\liminf_{\beta\downarrow0}\beta N_\beta(\nu)
\ge \frac{2x}\pi\sqrt{R_0(x)}.
\]
It remains to optimize the right-hand side. Put \(y=\eta_\rho^2x\). Squaring the positive factor to be maximized reduces the problem to
\[
g(y)=\frac{y^2(\Delta-a y)}{1+y},
\qquad 0<y<\frac{\Delta}a.
\]
Direct differentiation gives
\[
g'(y)=\frac{y\,[2\Delta+(\Delta-3a)y-2ay^2]}{(1+y)^2}.
\]
The bracket is positive at \(y=0\), negative at \(y=\Delta/a\), and has exactly one positive zero. Solving the quadratic yields
\[
y_\star=\frac{q-3+\sqrt{(q+1)(q+9)}}4,
\qquad q=\frac{\Delta}a.
\]
Because \(g\) vanishes at both endpoints, this critical point is the unique global maximizer. Substitution gives \(C_\star(\nu)\).

For the delta profile, the even double-delta ground state has energy \(-\kappa^2\). Matching the derivative jump at \(x=\rho\) gives \(2\kappa=\alpha(1+e^{-2\kappa\rho})\). Choosing the central amplitude as one, the even eigenfunction equals \(\cosh(\kappa x)\) for \(0\le x\le\rho\) and continues exponentially for \(x\ge\rho\). Its squared norm is
\[
\|\phi_\rho\|^2=\rho+\frac{e^{2\kappa\rho}+1}{2\kappa}
=\rho+\frac1{2\kappa-\alpha},
\]
where the last equality uses the jump equation. Since \(|\phi_\rho(0)|=1\), the displayed formula for \(\eta_\rho^2\) follows.

## Verification
The proof uses only the exact variational quotient (3.6), the source's stated transverse limits, Dirichlet interval eigenvalues, and elementary one-variable optimization. The accompanying `verify.py` checks the stationary-point identity, positivity and uniqueness over representative parameter ranges, numerical domination over dense grids, and the double-delta normalization identity. These finite checks corroborate the algebra; they are not used as a proof of the limiting spectral statement.

## Relationship to prior work
Exner--Spitzkopf, Theorem 3.1, proves that for \(\nu\in(e_\rho,e)\) the number of eigenvalues in the closing-book regime grows at least on the order of \(\beta^{-1}\), but leaves the coefficient as an unspecified positive constant \(C_\nu\). Their proof replaces the exact quotient (3.6) by unspecified positive constants \(a_\nu,b_\nu\). The present calculation retains the exact quotient, scales \(L\) with \(\tan(\beta/2)\), and optimizes the surviving coefficient.

The earlier explicit-cut-locus work of Kondej--Krejčiřík--Kříž establishes bound-state existence for a particular bookcover geometry, not a quantitative closing-angle counting coefficient. Exner--Vugalter treats broad bent soft waveguides and qualitative bound-state existence, again without this closing-angle optimization.

## Limitations
The result is a one-sided lower bound. It does not prove a matching upper bound, an exact Weyl law, or optimality among all possible trial spaces. The phrase "exact optimum" refers only to the asymptotic coefficient obtained from the source's trial family under the scaling \(L\tan(\beta/2)\to x\). The lower bound counts all eigenvalues below \(\nu\); it deliberately does not strengthen the source's interval localization to an explicit-coefficient statement.

## References
1. P. Exner and D. Spitzkopf, *Tunneling in soft waveguides: closing a book*, arXiv:2307.01536v1; J. Phys. A: Math. Theor. 57 (2024), 125301, doi:10.1088/1751-8121/ad2c80. See Proposition 2.1, Theorem 3.1, and equations (3.1)--(3.6).
2. S. Kondej, D. Krejčiřík, and J. Kříž, *Soft quantum waveguides with an explicit cut-locus*, arXiv:2007.10946v1; J. Phys. A: Math. Theor. 54 (2021), 30LT01.
3. P. Exner and S. Vugalter, *Bound states in bent soft waveguides*, arXiv:2304.14776v2; J. Spectr. Theory 14 (2024), 427--457, doi:10.4171/JST/502.
