# Exact scale frontier for the one-sided Wolfe grid in robust steepest descent
## Finding

Consider the Wolfe-type steepest descent algorithm for the robust counterpart in the scalar, single-objective, single-scenario case
\[
\kappa(x)=\frac12 a x^2,
\qquad
a>0.
\]
Fix a nonstationary point
\[
x\ne0
\]
and Wolfe parameters
\[
0<\beta<\gamma<1.
\]

The source auxiliary problem reduces exactly to
\[
\min_Y \; axY+\frac12Y^2,
\]
so the robust steepest descent direction and optimality measure are
\[
Y=-ax,
\qquad
\Theta(x)=-\frac12a^2x^2.
\]

For a positive trial step \(\alpha\), put
\[
s=\alpha a.
\]
Then the source's standard Wolfe conditions hold if and only if
\[
1-\gamma\le s\le2(1-\beta).
\]
Equivalently,
\[
\frac{1-\gamma}{a}
\le
\alpha
\le
\frac{2(1-\beta)}{a}.
\]

Algorithm 1 restricts the search to
\[
\alpha\in\{2^{-r}:r=0,1,2,\ldots\}.
\]
On the scalar quadratic above, that one-sided dyadic grid contains an admissible Wolfe step if and only if
\[
a\ge1-\gamma.
\]

Thus the algorithm as written has an exact scale frontier. For every
\[
0<a<1-\gamma,
\]
Wolfe steps exist, but every admissible one is larger than \(1\), while Algorithm 1 tests only steps at most \(1\). The line-search subroutine therefore has no admissible output at the first nonstationary iterate.

A concrete instance is
\[
\beta=\frac14,
\qquad
\gamma=\frac34,
\qquad
a=\frac18.
\]
The exact Wolfe interval is
\[
2\le\alpha\le12,
\]
whereas the algorithm tests only
\[
1,\frac12,\frac14,\ldots.
\]

A minimal scale-complete repair is to use the two-sided dyadic family
\[
\{2^r:r\in\mathbb Z\},
\]
or an equivalent bracketing phase that expands the trial step before backtracking. On the scalar family this always finds a Wolfe-grid point, because
\[
\frac{2(1-\beta)}{1-\gamma}>2.
\]

## Assumptions and scope

The construction is a valid specialization of the source robust quadratic model: dimension, number of objectives, and number of uncertainty scenarios are all one; the quadratic matrix is the positive scalar \(a\); and the linear and constant terms vanish.

The result concerns the standard Wolfe conditions used in Algorithm 1. It does not claim failure of the source's continuous step-existence theorem. In fact, that theorem remains valid on this example; the obstruction is the later restriction to a one-sided dyadic trial grid.

The finding also does not assert that every implementation based on the paper fails. An implementation that enlarges the initial trial step, uses a bracketing phase, or searches an unbounded positive grid avoids this particular obstruction.

## Proof

For
\[
\kappa(x)=\frac12ax^2,
\]
the gradient is
\[
g(x)=ax.
\]
In the scalar single-scenario case, the source's auxiliary problem has zero max-offset and becomes
\[
P(x):\quad
\min_Y \left\{axY+\frac12Y^2\right\}.
\]
Its unique minimizer is
\[
Y=-ax,
\]
and substitution gives
\[
\Theta(x)
=
ax(-ax)+\frac12a^2x^2
=
-\frac12a^2x^2.
\]

After a step of length \(\alpha>0\),
\[
x^+
=
x+\alpha Y
=
(1-\alpha a)x
=
(1-s)x.
\]
The sufficient-decrease condition is
\[
\kappa(x^+)
\le
\kappa(x)+\beta\alpha V(x,Y).
\]
Here
\[
V(x,Y)=g(x)Y=-a^2x^2.
\]
Dividing the sufficient-decrease inequality by the positive quantity \(\tfrac12ax^2\) yields
\[
(1-s)^2
\le
1-2\beta s.
\]
For \(s>0\), this is equivalent to
\[
s\le2(1-\beta).
\]

For the curvature condition,
\[
V(x^+,Y)
=
g(x^+)Y
=
-a^2x^2(1-s).
\]
Therefore
\[
V(x^+,Y)\ge\gamma V(x,Y)
\]
is equivalent to
\[
-(1-s)\ge-\gamma,
\]
hence
\[
s\ge1-\gamma.
\]
Combining the two inequalities proves the exact Wolfe interval
\[
1-\gamma
\le
\alpha a
\le
2(1-\beta).
\]

Now impose the source algorithm's trial grid
\[
\alpha_r=2^{-r},
\qquad
r=0,1,2,\ldots.
\]
Then
\[
s_r=a2^{-r}\le a.
\]
If
\[
a<1-\gamma,
\]
every grid point violates the curvature lower bound, so no step is admissible.

Conversely, assume
\[
a\ge1-\gamma.
\]
If
\[
a\le2(1-\beta),
\]
the unit step is admissible. If
\[
a>2(1-\beta),
\]
choose the smallest integer \(r\ge1\) satisfying
\[
a2^{-r}\le2(1-\beta).
\]
Minimality gives
\[
a2^{-r}>1-\beta.
\]
Because
\[
\beta<\gamma,
\]
we have
\[
1-\beta>1-\gamma.
\]
Thus
\[
1-\gamma
<
a2^{-r}
\le
2(1-\beta),
\]
so that grid point is admissible. This proves the if-and-only-if frontier
\[
a\ge1-\gamma.
\]

For the repaired two-sided grid, the admissible interval in the scaled variable \(s\) has ratio
\[
\frac{2(1-\beta)}{1-\gamma}>2.
\]
Successive dyadic values differ by a factor \(2\), so every positive scale \(a\) has some integer shift \(r\in\mathbb Z\) with
\[
a2^r
\in
[1-\gamma,2(1-\beta)].
\]

## Verification

The bundled script `artifacts/verify_wolfe_grid.py` checks the symbolic interval formulas numerically over many parameter choices, verifies the exact counterexample
\[
\beta=\frac14,
\qquad
\gamma=\frac34,
\qquad
a=\frac18,
\]
and exhaustively confirms the one-sided-grid frontier on a rational test lattice.

The computation is not the proof. The quantified result follows from the exact algebra above.

## Relationship to prior work

Kumar and Deep formulate the robust steepest direction through a strongly convex auxiliary problem, prove existence of standard and strong Wolfe steps under a lower-boundedness condition, and then specify Algorithm 1 with trial lengths restricted to
\[
\{2^{-r}:r=0,1,2,\ldots\}.
\]
The paper does not compare the continuous Wolfe-existence interval with that discrete one-sided grid.

Classical Wolfe line-search algorithms do not rely on shrinking alone. Standard bracketing procedures increase the trial step when necessary and then apply a zoom or interpolation phase. This distinction is essential here: on the scalar quadratic family, the curvature condition rejects every sufficiently small step, so shrinking from \(1\) can never repair an initial step that is already too small.

The exact threshold
\[
a=1-\gamma
\]
and the corresponding scale-complete dyadic repair were not found in targeted searches of the source, published-result database, or standard line-search references.

## Limitations

The exact frontier is proved for the scalar single-objective specialization. It is sufficient to show that the published discrete line-search rule is not scale-complete, but it is not a classification of all multidimensional robust quadratic instances.

The repair statement guarantees existence of a two-sided dyadic Wolfe point on this scalar family. It does not analyze evaluation complexity for general nonsmooth max-of-quadratics robust counterparts.

The source's continuous Wolfe existence theorem is not contradicted by this finding.

## References

1. S. Kumar, A. Deep, *A Wolfe-Type Steepest Descent Algorithm for Uncertain Quadratic Multiobjective Optimization Problems*, Boletim da Sociedade Paranaense de Matemática 44(7), 1--13, 2026. DOI: 10.5269/bspm.81660.
2. J. Nocedal, S. J. Wright, *Numerical Optimization*, 2nd ed., Springer, 2006. ISBN: 978-0-387-40065-5.
