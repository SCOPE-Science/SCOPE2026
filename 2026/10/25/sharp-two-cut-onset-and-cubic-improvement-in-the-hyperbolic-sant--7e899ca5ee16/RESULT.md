# Sharp two-cut onset and cubic improvement in the hyperbolic Santaló problem

## Finding

Consider the two-cut convex surfaces \(\Gamma(r,\alpha)\) in hyperbolic three-space of sectional curvature \(-1\), obtained by intersecting a radius-\(r\) geodesic ball with two symmetrically placed totally geodesic half-spaces, with \(r>0\) and \(0\le\alpha<\pi/2\). The parameter \(\alpha=0\) recovers the round geodesic sphere. Let \(S\) denote surface area and \(M\) denote total mean curvature, including edge curvature. The fixed-area spherical benchmark is \(M_1(S)=\sqrt{16\pi S+4S^2}\).

For each fixed \(S>0\), there is a unique real-analytic radius adjustment \(r=r(S,\alpha)\) for sufficiently small \(\alpha\) preserving area \(S\). Put \(t=S/(4\pi)\). Uniformly for \(t\) in any compact positive interval, the deficit has the exact expansion

\[
M(r(S,\alpha),\alpha)-M_1(S)
=4\pi\sqrt{t(1+t)}\left[
\frac{1-2t}{24}\alpha^4
+\frac{54t^2+13t-11}{720}\alpha^6
+O_t(\alpha^8)\right].
\]

Consequently the **sharp local two-cut threshold** is \(S_c=2\pi\): for \(0<S\le 2\pi\) the sphere is a strict one-sided local minimum in this family, whereas for every \(S>2\pi\), arbitrarily small positive symmetric truncations at the same area have strictly less total mean curvature than the sphere. At the threshold the first nonzero deficit is

\[
M(r(2\pi,\alpha),\alpha)-M_1(2\pi)
=\frac{\pi\sqrt3}{40}\alpha^6+O(\alpha^8)>0
\]

for all sufficiently small positive \(\alpha\).

There is also a sharp continuous onset of optimal small truncations on the unstable side. For \(S>2\pi\) sufficiently close to \(2\pi\), exactly one positive stationary truncation sufficiently close to zero is a strict local minimum. Its angle and improvement satisfy

\[
\alpha_*(S)^2=\frac{10}{9\pi}(S-2\pi)+O((S-2\pi)^2),
\]

\[
M_1(S)-M(r(S,\alpha_*(S)),\alpha_*(S))
=\frac{25\sqrt3}{1458\pi^2}(S-2\pi)^3
+O((S-2\pi)^4).
\]

In particular, writing \(\widehat S=8\pi(\pi^2-8)/(16-\pi^2)\), **for every** \(2\pi<S\le\widehat S\) there are two-cut convex surfaces of area \(S\) with curvature below both the equal-area sphere and the equal-area flat double disk. This gives a full explicit interval of counterexamples to the proposed sphere/double-disk lower envelope, rather than an example at a single area.

## Assumptions and scope

The ambient manifold is the simply connected constant-curvature \(-1\) hyperbolic three-space. In the Beltrami–Klein ball model, \(\Gamma(r,\alpha)\) bounds the convex set

\[
\left\{x\in\mathbb R^3:\|x\|^2\le\tanh^2 r,\quad
|x_3|\le\tanh r\cos\alpha\right\}.
\]

Here \(r>0\), \(\alpha\ge0\) is small, and the full nonsmooth curvature measure includes both circular edges. This theorem makes claims **only** within the indicated symmetric two-plane truncation family. Its threshold is a *local* statement at the sphere, and the optimal branch statement is restricted to sufficiently small excess area and sufficiently small truncation angle. The global minimizer among all hyperbolic convex bodies is not determined.

The exact starting formulas, established for this family in Fang Hong, *On Santaló's Problem*, Section 4, equations (4.1)–(4.2), are

\[
\begin{aligned}
S(r,\alpha)&=4\pi\left(\sinh^2r\cos\alpha
+\sqrt{1+\sinh^2r\sin^2\alpha}-1\right),\\
M(r,\alpha)&=4\pi\left(2\sinh r\cosh r\cos\alpha
+\sinh r\sin\alpha\arctan(\cosh r\tan\alpha)\right).
\end{aligned}
\]

No assertion is made that these exact input formulas are new.

## Proof

Write \(u=\sinh^2 r>0\), \(c=\sqrt{1+u}\) and set \(z=S(r,\alpha)/(4\pi)\), \(m=M(r,\alpha)/(4\pi)\). The preceding exact formulas become

\[
z=u\cos\alpha+\sqrt{1+u\sin^2\alpha}-1,
\qquad m=2\sqrt{u(1+u)}\cos\alpha
+\sqrt u\sin\alpha\arctan(c\tan\alpha).
\]

Ordinary analytic expansions at fixed positive \(u\) give

\[
\begin{aligned}
z&=u-\frac{u(1+u)}8\alpha^4
+\frac{u(1+u)(1+3u)}{48}\alpha^6+O_u(\alpha^8),\\
m&=2\sqrt{u(1+u)}
-\frac{\sqrt{u(1+u)}(1+4u)}{12}\alpha^4
+\frac{\sqrt{u(1+u)}(36u^2+22u+1)}{180}\alpha^6
+O_u(\alpha^8).
\end{aligned}
\]

Both quadratic coefficients cancel; this fact is crucial. Let \(g(z)=2\sqrt{z(1+z)}\), so \(M_1(S)=4\pi g(S/(4\pi))\). Because \(g'(u)=(1+2u)/\sqrt{u(1+u)}\), subtracting \(g(z)\) from \(m\) gives

\[
m-g(z)=\sqrt{u(1+u)}\left[
\frac{1-2u}{24}\alpha^4
+\frac{54u^2+13u-11}{720}\alpha^6
+O_u(\alpha^8)\right].
\]

At \(\alpha=0\), \(z=u\); also \(\partial z/\partial u=1\). The analytic implicit-function theorem supplies the unique area-preserving \(u=u(t,\alpha)\) near \(u=t>0\). The displayed area expansion implies \(u(t,\alpha)=t+O_t(\alpha^4)\). Since the deficit already starts at order four, this substitution changes its coefficients only at order eight. This proves the fixed-area expansion and its uniformity on compact positive \(t\)-intervals.

The fourth-order coefficient changes sign only at \(t=1/2\), i.e. \(S=2\pi\). At that point the sixth-order coefficient inside brackets is \(1/80\) and \(\sqrt{t(1+t)}=\sqrt3/2\), giving \(\pi\sqrt3/40\). Positivity and negativity follow by dominating remainder estimates for each fixed \(S\).

For the optimal branch, let \(\delta=t-1/2\) and \(y=\alpha^2\). Analyticity and the preceding expansion give the normalized deficit

\[
F(\delta,y):=\frac{M(r(S,\sqrt y),\sqrt y)-M_1(S)}{4\pi}
=A(\delta)y^2+B(\delta)y^3+O(y^4),
\]

where \(A(\delta)=\sqrt{(1/2+\delta)(3/2+\delta)}\,(-2\delta)/24\) and \(B(0)=\sqrt3/160>0\). The stationary equation for \(y>0\) reduces, after dividing \(\partial_yF\) by \(y\), to

\[
0=2A(\delta)+3B(\delta)y+O(y^2).
\]

Its derivative with respect to \(y\) at \((\delta,y)=(0,0)\) is \(3B(0)>0\). The implicit-function theorem therefore yields a unique analytic critical curve near the origin, with

\[
y_*(\delta)=\frac{40}{9}\delta+O(\delta^2).
\]

This curve is positive when \(\delta>0\) is small; \(\partial_y^2F(\delta,y_*)>0\) there, proving strict local minimality and local uniqueness. Substitution gives

The exact coefficient is computed without numerical approximation:

\[
F(\delta,y_*)
=\frac{\sqrt3}{2}\left(-\frac{\delta}{12}\cdot\frac{1600}{81}\delta^2
+\frac1{80}\cdot\frac{64000}{729}\delta^3\right)+O(\delta^4)
=-\frac{200\sqrt3}{729}\delta^3+O(\delta^4).
\]

Because \(S-2\pi=4\pi\delta\), multiplying by \(4\pi\) yields the asserted exact cubic improvement coefficient \(25\sqrt3/(1458\pi^2)\).

Finally, the flat-double-disk benchmark is \(M_2(S)=\sqrt{2\pi^3S+(\pi^2/4)S^2}\), and direct comparison yields \(M_2(S)\ge M_1(S)\) for \(S\le\widehat S\), with equality at \(\widehat S\). Since \(\widehat S>2\pi\), the strict local improvement over the sphere for each \(S>2\pi\) supplies the claimed full interval of surfaces strictly below both benchmarks.

## Verification

The standalone file `verification/check_drum.py` reconstructs the exact Taylor coefficients directly from the two primary trigonometric formulas in symbolic algebra, verifies the critical sixth-order coefficient and the implicit-branch/cubic constants, and performs independent 75-digit fixed-area computations for representative subcritical, critical, and supercritical areas. The code derives the adjusted radius numerically by solving the exact area equation, rather than inserting a truncated radius expansion. Run `python verification/check_drum.py` after installing the dependencies listed in `verification/requirements.txt`. All assertions passed on the embedded files.

Finite numerical checks are corroboration only; the all-area conclusion follows from exact analytic expansions, uniform remainders, and the implicit-function theorem.

## Relationship to prior work

Fang Hong, *On Santaló's Problem* (arXiv:2606.01771, first submitted 2026-06-01), provides the exact area and total-curvature equations used here and constructs counterexamples near the classical sphere/double-disk crossover. In Section 4 and Note 4.1, its stated results do not determine the local critical area \(2\pi\), the positive critical sixth-order coefficient, the uniquely selected small-angle optimizing branch, the cubic improvement law, or the full interval \((2\pi,\widehat S]\) of counterexamples. The present theorem derives these additional variational consequences from those acknowledged source formulas; it does **not** rediscover the source family or input identities.

General hyperbolic Minkowski inequalities, including Ghomi–Spruck and Hong's volume-dependent inequality, concern broader body classes and retain different data. They do not directly state the fixed-area local bifurcation within the two-cut drum family. This claim is local in its asymptotics and does not solve global Santaló minimization.

## Limitations

The critical threshold and the small-angle optimizing branch are established only within the specified symmetric two-plane truncated-ball family, not all convex variations. All asymptotics assume fixed positive area; the optimizing branch is analyzed only close to \(2\pi\). The counterexample interval is an existence statement using sufficiently small angles and does not supply globally minimizing angles at each area. The underlying two-parameter formulas are already published, and historical specialized literature may contain equivalent asymptotic analysis not found in the accessible comparisons. No independent audit was performed.

## References

F. Hong, *On Santaló's Problem*, arXiv:2606.01771 (first public version 2026-06-01; especially Section 4, equations (4.1)–(4.2), Note 4.1), https://arxiv.org/html/2606.01771v4 .

M. Ghomi and J. Spruck, *Minkowski inequality in Cartan–Hadamard manifolds*, arXiv:2206.06554, https://arxiv.org/abs/2206.06554 .

F. Hong, *Sharp Minkowski Type Inequality in Cartan–Hadamard 3-Spaces*, arXiv:2603.19646, https://arxiv.org/abs/2603.19646 .
