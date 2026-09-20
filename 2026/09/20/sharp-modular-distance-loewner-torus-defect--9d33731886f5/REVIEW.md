# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The argument separates into one established input and one elementary sharp
optimization.

Horowitz--Katz--Katz Theorem 4.1 states, for the reduced modular parameter
\(\tau=x+iy\),
\[
\operatorname{area}(G)-y\operatorname{sys}(G)^2\ge\operatorname{Var}(f).
\]
Thus the proposed refinement is correct once the minimum possible \(y\) at
fixed modular distance from the Eisenstein class is identified.

For the standard half fundamental domain, the equilateral point is
\(\rho=1/2+i\sqrt3/2\), and the hyperbolic distance satisfies
\[
\cosh d=
\frac{(x-\frac12)^2+y^2+\frac34}{\sqrt3\,y}.
\]
At fixed height \(y\), this is maximized by making \(x\) as small as the
fundamental-domain constraints allow. For
\(\sqrt3/2\le y\le1\), this puts the point on \(|\tau|=1\); for \(y\ge1\),
it puts the point on \(x=0\). Inverting the distance along those two
boundary pieces gives exactly
\[
y_{\min}(d)=
\frac{2\sqrt3 e^d}{3+e^{2d}}
\]
up to \(d=\log\sqrt3\), and
\[
y_{\min}(d)=
\frac{\sqrt3\cosh d+\sqrt{3\cosh^2d-4}}2
\]
afterward. Both branches give \(y=1\) at the transition.

The standard \((2,3,\infty)\) modular tessellation identifies the distance
from a point in the half fundamental domain to the equilateral orbifold
point with its hyperbolic distance to the adjacent order-three lift
\(\rho\). Reflection handles the other half of the domain.

Substitution into the 2009 inequality gives the claimed result. Sharpness
is exact: for the boundary conformal classes used in the minimization, a
flat metric has zero variance and saturates the conformal-class inequality.
The Taylor expansion at \(d=0\) was independently checked from the closed
formula.

## Originality — PASS (to the best of our knowledge)

The primary 2009 source was checked at theorem/proof level. It retains the
stronger coefficient \(y=\operatorname{Im}\tau\) before deriving the
classical Loewner constant, but it does not express \(y-\sqrt3/2\) as a
function of intrinsic distance in the modular orbifold.

Searches covered exact and synonymous formulations involving Loewner's
torus inequality, systolic/isosystolic defect, conformal class, modular or
hyperbolic distance, the Hermite invariant, flat/hexagonal/Eisenstein
lattices, and stability. No source located stated the piecewise optimal
distance function or an equivalent global theorem.

The 2025 work of Eyll is a particularly relevant comparison because it
treats stability for the Möbius strip and Klein bottle and separates
conformal-class from conformal-factor effects. It does not supply this
torus modular-distance formula. Recent Loewner work on nonpositively curved
surfaces addresses a different extension.

Residual originality risk remains because the modular optimization is
elementary and could appear under geometry-of-numbers terminology, for
example as a quantitative statement about the two-dimensional Hermite
invariant. No specifically identified inaccessible paper was found whose
metadata indicates such coverage.

## Value — PASS

The 2009 inequality already contains a conformal-class-dependent coefficient,
but the quantitative meaning of its excess above the Hermite optimum is
left implicit in the coordinate \(y\). The present theorem converts that
excess into an intrinsic distance-to-extremizer statement on moduli space.

The result is global, explicit, and pointwise sharp for every distance,
rather than only asymptotic near the equilateral torus. It also reveals a
linear small-distance law
\[
\Phi(d)=\frac{\sqrt3}{4}d+O(d^2),
\]
which is stronger than a generic quadratic stability conclusion and reflects
the orbifold/corner geometry of the extremal class.

## Scientific limitations

1. Modular hyperbolic distance measures conformal-class displacement, not a
   full metric-space distance between arbitrary Riemannian metrics.
2. The theorem does not by itself give Gromov--Hausdorff, bi-Lipschitz, or
   Sobolev closeness to an equilateral flat metric.
3. The variance term is inherited from the 2009 theorem; the new contribution
   is the exact modular-distance interpretation and optimization of the
   conformal-class term.
4. Originality remains “to the best of our knowledge,” with residual risk
   from unindexed or differently phrased geometry-of-numbers literature.
