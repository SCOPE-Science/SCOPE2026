# Finite-shell equality rigidity for the planar strongly convex level-set bound

## Finding

Let \(\Omega\subset\mathbb R^2\) be a bounded convex domain and let \(f\in C^2(\Omega)\) satisfy
\[
D^2f\ge aI_2
\]
for some \(a>0\). Let \(x_*\in\Omega\) be the unique critical point and put
\[
m=f(x_*).
\]
For \(c>m\) and \(\delta>0\), define
\[
E_{c,\delta}
=
\{x\in\Omega:c\le f(x)<c+\delta\}.
\]

The sharp planar level-set estimate of Chen and Yang gives
\[
|E_{c,\delta}|\le \frac{2\pi\delta}{a}.
\]
Equality at one positive-thickness shell is completely rigid.

Set
\[
R=
\sqrt{\frac{2(c+\delta-m)}{a}}.
\]
Then
\[
\boxed{
|E_{c,\delta}|=\frac{2\pi\delta}{a}
}
\]
if and only if
\[
\boxed{
B(x_*,R)\subset\Omega
}
\]
and
\[
\boxed{
f(x)=m+\frac a2|x-x_*|^2
\quad\text{for every }x\in B(x_*,R).
}
\]

Consequently, equality for a single shell forces
\[
\{x\in\Omega:f(x)<c+\delta\}=B(x_*,R)
\]
and
\[
\{x\in\Omega:f(x)<c\}
=
B\!\left(
x_*,
\sqrt{\frac{2(c-m)}a}
\right).
\]

Thus the quadratic-ball model used to prove sharpness of the constant is not merely one extremizing example in the plane: it describes every finite-scale equality case around the relevant sublevel region.

## Assumptions and scope

The statement is deliberately restricted to the two-dimensional \(C^2\) critical-point setting of the source's Proposition 3.1. The assumption \(c>m\) keeps the shell away from the minimizer and makes the radial equality argument transparent.

The Hessian inequality is understood in the quadratic-form sense:
\[
v^{\mathsf T}D^2f(x)v\ge a|v|^2
\qquad
(x\in\Omega,\ v\in\mathbb R^2).
\]

After translating \(x_*\) to the origin and subtracting \(m\), the auxiliary function
\[
g(x)=f(x)-\frac a2|x|^2
\]
is convex, satisfies
\[
g(0)=0,
\qquad
Dg(0)=0,
\]
and therefore has a minimum at the origin.

No assertion is made here about equality cases in dimensions \(n\ge3\), where the source's constant also contains the circumradius factor \(r(\Omega)^{n-2}\).

## Proof

Translate coordinates so that
\[
x_*=0
\]
and subtract \(m\), so
\[
f(0)=0,
\qquad
Df(0)=0.
\]

For each unit vector \(\theta\in S^1\), let
\[
\rho_\Omega(\theta)
=
\sup\{r>0:r\theta\in\Omega\}
\]
be the radial boundary function. Since \(\Omega\) is bounded, convex, and contains the origin in its interior, \(\rho_\Omega\) is positive and continuous.

Define the radial restriction
\[
\phi_\theta(r)=f(r\theta),
\qquad
0\le r<\rho_\Omega(\theta).
\]
The Hessian lower bound gives
\[
\phi_\theta''(r)\ge a.
\]
Because
\[
\phi_\theta'(0)=0,
\]
we have
\[
\phi_\theta'(r)\ge ar
\qquad
(r>0).
\]
Hence every radial restriction is strictly increasing away from the origin.

Along a fixed direction, the shell
\[
\{r:c\le\phi_\theta(r)<c+\delta\}
\]
is either empty or a radial interval. Let \(r_0(\theta)\) be its lower endpoint when it is nonempty, and let \(r_1(\theta)\) denote its upper endpoint, allowing \(r_1(\theta)=\rho_\Omega(\theta)\) when the shell is cut off by the boundary. Monotonicity gives
\[
\phi_\theta(r_0)=c
\]
and
\[
\phi_\theta(r_1)-c\le\delta
\]
in the limiting sense at a boundary endpoint.

Integrating
\[
\phi_\theta'(r)\ge ar
\]
from \(r_0\) to \(r_1\) yields
\[
\frac{r_1^2-r_0^2}{2}
\le
\frac{\phi_\theta(r_1)-\phi_\theta(r_0)}{a}
\le
\frac{\delta}{a}.
\]
The left-hand side is exactly the radial contribution to planar area. Therefore polar integration gives
\[
|E_{c,\delta}|
=
\int_{S^1}
\frac{r_1(\theta)^2-r_0(\theta)^2}{2}\,d\theta
\le
\int_{S^1}\frac{\delta}{a}\,d\theta
=
\frac{2\pi\delta}{a}.
\]

Suppose now that equality holds globally. The pointwise radial contribution is bounded above by \(\delta/a\), so equality of the integral forces equality for almost every \(\theta\). For such a direction,
\[
\phi_\theta(r_1)-\phi_\theta(r_0)=\delta
\]
and
\[
\int_{r_0}^{r_1}
\bigl(\phi_\theta'(r)-ar\bigr)\,dr
=
0.
\]
The integrand is continuous and nonnegative, hence
\[
\phi_\theta'(r)=ar
\qquad
(r_0\le r\le r_1).
\]

Now write
\[
h_\theta(r)
=
\phi_\theta(r)-\frac a2r^2.
\]
Since
\[
h_\theta''(r)\ge0
\]
and
\[
h_\theta'(0)=0,
\]
the derivative \(h_\theta'\) is nondecreasing and nonnegative on its interval of definition. Since it vanishes on the shell interval, it must vanish on the whole interval
\[
0\le r\le r_1.
\]
Thus
\[
\phi_\theta(r)=\frac a2r^2
\qquad
(0\le r\le r_1)
\]
for almost every direction.

At the upper endpoint,
\[
\frac a2r_1^2=c+\delta,
\]
so
\[
r_1=R
=
\sqrt{\frac{2(c+\delta)}a}
\]
in the normalized coordinates. Therefore
\[
\rho_\Omega(\theta)\ge R
\]
for almost every \(\theta\). Continuity of the radial boundary function upgrades this to every direction, giving
\[
B(0,R)\subset\Omega.
\]

For each fixed \(0<r<R\), the identity
\[
f(r\theta)=\frac a2r^2
\]
holds for almost every \(\theta\). Continuity of \(f\) on the circle then gives the same identity for every \(\theta\). Hence
\[
f(x)=\frac a2|x|^2
\qquad
(x\in B(0,R)).
\]

Undoing the translation and additive normalization proves the necessity.

Conversely, suppose
\[
B(x_*,R)\subset\Omega
\]
and
\[
f(x)=m+\frac a2|x-x_*|^2
\]
throughout that ball. The function
\[
g(x)
=
f(x)-m-\frac a2|x-x_*|^2
\]
is convex with a minimum value \(0\) at \(x_*\), so \(g\ge0\) on all of \(\Omega\). Consequently every point outside radius \(R\) satisfies
\[
f(x)\ge m+\frac a2|x-x_*|^2>c+\delta.
\]
Thus the shell is exactly the Euclidean annulus
\[
\sqrt{\frac{2(c-m)}a}
\le
|x-x_*|
<
\sqrt{\frac{2(c+\delta-m)}a},
\]
whose area is
\[
\pi
\left(
\frac{2(c+\delta-m)}a
-
\frac{2(c-m)}a
\right)
=
\frac{2\pi\delta}{a}.
\]
This proves sufficiency and completes the equality classification.

## Verification

The proof was reconstructed directly from the radial mechanism behind the source's planar estimate.

The critical equality chain is
\[
\frac{r_1^2-r_0^2}{2}
\le
\frac{\phi_\theta(r_1)-\phi_\theta(r_0)}a
\le
\frac{\delta}{a}.
\]
Every term is nonnegative and the final bound is independent of direction. Therefore global equality forces equality in this chain for almost every direction, rather than merely on average.

The rigidity step uses the convex remainder
\[
h_\theta(r)
=
f(r\theta)-f(0)-\frac a2r^2.
\]
Its derivative is nondecreasing, starts at \(0\), and is forced to vanish on the shell. Hence it vanishes from the critical point all the way to the outer shell radius. This is the step that upgrades shell equality to quadraticity on the entire enclosed disk.

The converse was checked directly: the quadratic annulus has area \(2\pi\delta/a\), while strong convexity prevents any additional shell points outside the outer radius.

There is no finite computation, numerical sampling, or unproved exhaustion argument in the proof.

## Relationship to prior work

Chen and Yang prove the sharp estimate
\[
|\{c\le f<c+\delta\}|
\le
\frac{2\pi\delta}{a}
\]
in the planar critical-point setting under
\[
D^2f\ge aI_2.
\]
Their proof uses radial integration and the lower bound on radial derivatives. They state optimality of the general constant using the Euclidean ball and the quadratic function, with an asymptotic sharpness parameter.

The inspected full text contains no equality-case or rigidity statement. The present result follows the equality conditions in the radial proof and shows that one exact finite-shell equality forces the whole enclosed upper sublevel to be a Euclidean disk and the phase to be the extremal quadratic there.

Older work on strongly convex sublevel sets concerns geometric convexity of sublevel sets, while classical uniform sublevel-set estimates under Hessian conditions use different curvature hypotheses and constants. Targeted searches for finite-shell equality, quadratic rigidity, and the exact constant \(2\pi\) did not locate a prior classification implying this statement.

## Limitations

The result is two-dimensional and assumes \(C^2\) regularity plus an interior critical point. It does not classify equality in the source's higher-dimensional estimate or in its nondegenerate-hyperbolic theorem.

Only local quadraticity up to the outer shell level is forced. The function may depart from the quadratic model outside
\[
\{f<c+\delta\}.
\]

The literature comparison cannot prove absolute uniqueness of the statement under every possible terminology; the residual risk is that an older equality theorem for strongly convex shell-volume bounds exists under a formulation not captured by the targeted searches.

## References

1. Xianghong Chen and Tongou Yang, *Level set estimates for strictly convex and hyperbolic functions*, arXiv:2609.32697v1, 26 September 2026.
2. Alexander Weber and Gunther Reissig, *Classical and Strong Convexity of Sublevel Sets and Application to Attainable Sets of Nonlinear Systems*, SIAM Journal on Control and Optimization 52 (2014), 2857--2876.
3. Anthony Carbery, *A uniform sublevel set estimate*, in *Harmonic Analysis and Partial Differential Equations*, Contemporary Mathematics 505, American Mathematical Society, 2008, 97--103.
