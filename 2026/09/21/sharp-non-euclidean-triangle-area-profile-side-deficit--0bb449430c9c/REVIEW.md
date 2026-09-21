# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The proof was checked through the slack parametrization \(x=s-a,y=s-b,z=s-c\). Fixed perimeter fixes \(x+y+z=s\), and the side deficit satisfies
\[
Q=3\sum (x-s/3)^2.
\]
Thus fixed \((p,Q)\) is a circle in the slack plane. L'Huilier's spherical formula and its hyperbolic Heron analogue turn the area into a monotone function of \(\prod\tau_\kappa(x_i)\).

For \(g=\log\tau_\kappa\), one has \(g'=\csc t\) in curvature \(+1\) and \(g'=\operatorname{csch}t\) in curvature \(-1\). Their second derivatives as functions \(g'\) are strictly positive on the relevant domains. The Lagrange equation therefore has at most two distinct coordinate values, reducing all interior extrema to the two displayed isosceles branches. The comparison derivative
\[
D'(d)=2\bigl(h(m+2d)+h(m-2d)-h(m+d)-h(m-d)\bigr)>0
\]
follows from strict convexity of \(h=g'\), proving which branch is upper and lower.

The lower branch stays positive exactly for \(u<1/2\), equivalent to \(Q/p^2<1/8\). At and beyond this threshold the fixed-moment circle meets a coordinate plane, so degenerate triangles give zero in the closure; each positive arc has the upper isosceles critical point as its sole interior maximum. This also proves realization of every intermediate positive area.

A standalone numerical check independently parameterized the moment circle for representative spherical and hyperbolic parameters and agreed with all formula bounds. The numerical check is not used as a substitute for the analytic proof.

## Originality

PASS, to the best of our knowledge.

The closest older source inspected was Svrtan--Veljan, *Non-Euclidean versions of some classical triangle inequalities*, Forum Geometricorum 12 (2012), 197--209. Its Theorems 3.3 and 3.4 give hyperbolic and spherical Finsler--Hadwiger inequalities derived from Cagnolli formulas and Jensen convexity. Sections 3 and 4 do not state a complete fixed-perimeter, fixed-side-deficit area range or classify both extremal isosceles branches.

The most important current-status comparison is Bogosel, *Optimal Finsler-Hadwiger Inequalities* (Results in Mathematics, 2025; arXiv:2508.06285). That paper explicitly determines the sharp Euclidean diagram for perimeter, area, and \(Q=(a-b)^2+(b-c)^2+(c-a)^2\). Accordingly the Euclidean profile is prior work and excluded from the present novelty claim.

Searches also used the equivalent terms side variance, sum of squared side differences, non-Euclidean triangle inequalities, spherical/hyperbolic Finsler-Hadwiger, fixed perimeter, triangle area, and Blaschke-Santaló diagram. No located source stated the two-sided constant-curvature profiles, the exact \(Q/p^2=1/8\) transition, or the full interval-realization statement.

Residual risk is nonzero because the proof becomes short after passing to L'Huilier slack variables, and older spherical/hyperbolic triangle-inequality literature may encode the same result differently. No specific unresolved source was found that gives concrete evidence of coverage.

## Value

PASS.

The theorem completes, for the chosen three quantities, the vertical fixed-\((p,Q)\) slices that one-sided non-Euclidean Finsler-Hadwiger inequalities do not determine. It gives explicit sharp formulas, equality families, a universal degeneracy threshold, and all intermediate values, while connecting directly to the known sharp Euclidean diagram.

## Limitations

- Spherical perimeter is restricted to \(p<2\pi\) to stay in the principal minor-arc regime of L'Huilier's formula.
- Other constant curvatures require the stated rescaling.
- Only the quadratic side deficit \(Q\) is treated.
- The Euclidean exact profile is prior work.
- Equivalent older non-Euclidean formulations may exist under different notation.
