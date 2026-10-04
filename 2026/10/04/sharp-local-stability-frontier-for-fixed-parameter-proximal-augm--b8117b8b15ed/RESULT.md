# Sharp local stability frontier for fixed-parameter proximal augmented Lagrangian dynamics
## Finding

Let
\[
a>0,\qquad R>0,
\]
and consider the one-dimensional constrained composite problem
\[
\min_{x\in\mathbb R}
\left\{
-\frac a2x^2+\delta_{[-R,R]}(x)
:
x=0
\right\}.
\]
The indicator \(\delta_{[-R,R]}\) is zero on the box and \(+\infty\) outside it. The unique feasible point is \(x_\star=0\), and the objective is lower bounded because its effective domain is compact.

Consider the exact fixed-parameter proximal augmented Lagrangian update
\[
x_{k+1}\in
\arg\min_{|y|\le R}
\left\{
-\frac a2y^2+\lambda_k y+\frac{\rho}{2}y^2
+\frac{1}{2\gamma}(y-x_k)^2
\right\},
\]
followed by
\[
\lambda_{k+1}=\lambda_k+\rho x_{k+1},
\]
where
\[
\rho>0,\qquad \gamma>0.
\]
Put
\[
r=\frac1\gamma,\qquad D=r+\rho-a.
\]
Assume
\[
D>0.
\]
Then every primal subproblem is globally \(D\)-strongly convex and therefore has a unique minimizer.

Near the KKT point
\[
(x_\star,\lambda_\star)=(0,0),
\]
the box is inactive and the update is exactly
\[
\begin{pmatrix}
x_{k+1}\\
\lambda_{k+1}
\end{pmatrix}
=
M
\begin{pmatrix}
x_k\\
\lambda_k
\end{pmatrix},
\qquad
M=
\frac1D
\begin{pmatrix}
r&-1\\
\rho r&r-a
\end{pmatrix}.
\]

The KKT point is locally asymptotically stable if and only if
\[
\rho>a
\]
and
\[
4r+\rho>2a,
\]
equivalently
\[
\rho>a,
\qquad
\frac4\gamma+\rho>2a.
\]

Thus global strong convexity of every primal subproblem is not sufficient for local convergence of the fixed-parameter primal-dual iteration. For example, when
\[
\rho<a,\qquad r>a-\rho,
\]
the subproblem is strongly convex because \(D>0\), but the KKT point is linearly unstable.

For each fixed
\[
\rho>a,
\]
the local asymptotic factor is uniquely minimized over \(r>0\) at
\[
r_\star=\frac{a^2}{4\rho},
\qquad
\gamma_\star=\frac{4\rho}{a^2}.
\]
At this choice the two eigenvalues coalesce at
\[
-\frac{a}{2\rho-a},
\]
and the optimal local factor is
\[
q_\star(\rho)=\frac{a}{2\rho-a}.
\]

## Assumptions and scope

The problem is deliberately the simplest normal-curvature mode compatible with the structural assumptions of the recent proximal augmented Lagrangian framework: the smooth term is continuously differentiable and nonconvex, the box indicator is proper closed convex with an elementary proximal mapping, the equality constraint is smooth, a feasible start exists, and the composite objective is lower bounded.

The result studies the exact fixed-parameter P-ALM core consisting of the proximal augmented-Lagrangian primal minimization and the multiplier update. It does not claim that the adaptive feasible-start algorithm of the source paper has the same fixed-parameter dynamics. In particular, adaptive increases of the penalty and changes of the proximal parameter can move the method between the regions identified here.

The box radius \(R\) does not enter the local frontier. It ensures lower boundedness and leaves a neighborhood of the KKT point in which the exact minimizer is interior, so the local map is precisely linear.

## Proof

The primal subproblem differs by an additive constant from
\[
\frac D2y^2+(\lambda_k-rx_k)y
\]
on \([-R,R]\). Under \(D>0\), it is globally \(D\)-strongly convex. Whenever the unconstrained minimizer lies in the interior of the box,
\[
x_{k+1}=\frac{rx_k-\lambda_k}{D}.
\]
Substitution into the multiplier update gives
\[
\lambda_{k+1}
=
\frac{\rho r}{D}x_k+\frac{r-a}{D}\lambda_k.
\]
This proves the displayed local matrix \(M\).

The characteristic polynomial of \(M\) is
\[
p(z)=z^2-Tz+\Delta,
\]
where
\[
T=\frac{2r-a}{D},
\qquad
\Delta=\frac rD.
\]
For a real monic quadratic \(z^2-Tz+\Delta\), both roots lie strictly inside the unit disk exactly when
\[
1-\Delta>0,\qquad
1-T+\Delta>0,\qquad
1+T+\Delta>0.
\]
Here those three quantities are
\[
1-\Delta=\frac{\rho-a}{D},
\]
\[
1-T+\Delta=\frac{\rho}{D},
\]
and
\[
1+T+\Delta=\frac{4r+\rho-2a}{D}.
\]
Because \(D>0\) and \(\rho>0\), the Schur conditions reduce exactly to
\[
\rho>a,
\qquad
4r+\rho>2a.
\]
In this open region, the exact local linear map is a contraction in an equivalent norm, so the KKT point is locally asymptotically stable.

The boundary cases are genuinely non-attracting. If \(\rho=a\), then
\[
\det M=1.
\]
When the eigenvalues are nonreal they lie on the unit circle; at the repeated real boundary an eigenvector with eigenvalue \(-1\) gives an arbitrarily small two-cycle. If
\[
\rho>a,\qquad 4r+\rho=2a,
\]
then \(p(-1)=0\), so an arbitrarily small \(-1\)-eigenvector gives a two-cycle while the box remains inactive. If \(\rho<a\), then
\[
\det M>1,
\]
so at least one eigenvalue has modulus greater than one. If
\[
\rho>a,\qquad 4r+\rho<2a,
\]
then \(p(-1)<0\), forcing a real root below \(-1\). Hence none of the excluded parameter regimes is locally asymptotically stable.

It remains to optimize the stable local factor for fixed \(\rho>a\). The eigenvalue discriminant is
\[
T^2-4\Delta
=
\frac{a^2-4\rho r}{D^2}.
\]
Define
\[
r_\star=\frac{a^2}{4\rho}.
\]
For \(r\ge r_\star\), the roots are a complex-conjugate pair or a double root, and their common modulus is
\[
q(r)=\sqrt{\frac r{r+\rho-a}},
\]
which is strictly increasing in \(r\).

For \(r<r_\star\), the roots are real and negative in the stable region. Put
\[
s=\sqrt{1-\frac{4\rho r}{a^2}},
\qquad
\kappa=\frac{\rho}{a}>1.
\]
Their spectral radius simplifies to
\[
q(r)=\frac{1+s}{2\kappa-1-s}.
\]
This expression is strictly increasing in \(s\), while \(s\) is strictly decreasing in \(r\). Hence \(q(r)\) is strictly decreasing for \(r<r_\star\). The unique minimizer is therefore \(r_\star\).

At \(r=r_\star\),
\[
\frac{r_\star}{r_\star+\rho-a}
=
\frac{a^2}{(2\rho-a)^2},
\]
so the double eigenvalue is
\[
-\frac{a}{2\rho-a},
\]
and the optimal local factor is
\[
q_\star(\rho)=\frac{a}{2\rho-a}.
\]

## Verification

The standalone script `artifacts/verify_palm_scalar.py` uses exact rational arithmetic. It verifies the matrix trace, determinant, the three Schur numerators, the double-root identity at the optimal proximal parameter, a strongly-convex-but-unstable instance, and exact small-amplitude two-cycles on both stability boundaries.

These finite calculations are consistency checks. The all-parameter result is the algebraic Schur analysis above.

## Relationship to prior work

Adeoye, Latafat, and Bemporad formulate the proximal augmented Lagrangian update used here and emphasize that a suitable proximal term can make a nonconvex subproblem strongly convex. Their analysis focuses on finite termination at an approximate KKT point under adaptive penalty and proximal schedules rather than sequential convergence of a fixed-parameter exact recurrence. The present result isolates the local dynamical condition that strong convexification alone does not supply.

Hermans, Themelis, and Patrinos also use proximal augmented Lagrangian ideas for nonconvex quadratic programs. Their QPALM scheme has a materially different two-level structure: a proximity point can be held fixed while augmented-Lagrangian inner iterations enforce feasibility. Their full text therefore permits positive dual penalties without the fixed-one-step stability restriction derived here.

Earlier local convergence analyses of the proximal method of multipliers prove linear convergence once penalty parameters exceed problem-dependent thresholds under second-order regularity assumptions. The accessible statements do not give the exact two-parameter frontier
\[
\rho>a,\qquad \frac4\gamma+\rho>2a
\]
for this normal negative-curvature mode, nor the unique rate-optimal value
\[
\gamma_\star=\frac{4\rho}{a^2}.
\]

Targeted database searches over proximal augmented Lagrangian aliases, fixed penalties, negative curvature, scalar equality constraints, Schur stability, and strongly convex subproblems returned no equivalent statement. The closest records concern different proximal-convexification certificates and unrelated first-order stability frontiers.

## Limitations

This is a local classification for one scalar normal-curvature mode. The box is inactive in the neighborhood where the classification applies. Multidimensional KKT systems can couple tangent and normal modes and need not reduce to this \(2\times2\) matrix.

The result concerns exact fixed parameters. It does not analyze the source paper's adaptive parameter rules, inexact inner solves, inequality multipliers, or changing proximal centers beyond the standard one-step update.

A 2020 nonlinear-programming paper on rates of the proximal method of multipliers was available only at abstract level in the literature check. It establishes broad local linear-rate results above a penalty threshold; the possibility that its inaccessible theorem constants specialize to part of this scalar frontier is therefore retained as a residual originality risk.

## References

1. A. D. Adeoye, P. Latafat, A. Bemporad, *A proximal augmented Lagrangian method for nonconvex optimization with equality and inequality constraints*, arXiv:2509.02894v1, 2025.
2. B. Hermans, A. Themelis, P. Patrinos, *QPALM: A Proximal Augmented Lagrangian Method for Nonconvex Quadratic Programs*, arXiv:2010.02653v1, 2020.
3. Y. Zhang, J. Wu, L. Zhang, *The rate of convergence of proximal method of multipliers for nonlinear programming*, Optimization Methods and Software 35(5), 2020, DOI: 10.1080/10556788.2020.1738435.
4. R. T. Rockafellar, *Augmented Lagrangians and Applications of the Proximal Point Algorithm in Convex Programming*, Mathematics of Operations Research 1(2), 1976, DOI: 10.1287/moor.1.2.97.
