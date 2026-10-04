# Closed-form Euclidean projection onto the two-ball lens in certified stochastic acceleration
## Finding

Let
\[
C=B(a,r)\cap B(b,R)\subset\mathbb R^n,
\qquad
r>0,\quad R>0,
\]
and assume \(C\) has nonempty interior. The Euclidean projection of an arbitrary point \(z\in\mathbb R^n\) onto \(C\) has a finite closed-form active-set formula.

For a single ball, write
\[
P_{a,r}(z)
=
a+\min\left\{1,\frac{r}{\|z-a\|}\right\}(z-a),
\]
with the evident convention when \(z=a\). Define
\[
p_a=P_{a,r}(z),
\qquad
p_b=P_{b,R}(z).
\]

The exact projector \(\Pi_C(z)\) is obtained as follows.

If
\[
z\in C,
\]
then
\[
\Pi_C(z)=z.
\]

If
\[
p_a\in B(b,R),
\]
then
\[
\Pi_C(z)=p_a.
\]

Otherwise, if
\[
p_b\in B(a,r),
\]
then
\[
\Pi_C(z)=p_b.
\]

In one ambient dimension these cases are exhaustive. In dimensions \(n\ge2\), suppose neither single-ball projection is feasible. Then both ball constraints are active. Put
\[
D=\|b-a\|,
\qquad
e=\frac{b-a}{D},
\]
and
\[
s=\frac{r^2-R^2+D^2}{2D}.
\]
The common sphere of the two active boundaries lies in the radical hyperplane and has center
\[
c=a+se
\]
and radius
\[
\rho=\sqrt{r^2-s^2}.
\]
Let
\[
w=(I-ee^\top)(z-c).
\]
In this branch,
\[
D>0,\qquad \rho>0,\qquad w\ne0,
\]
and the projection is
\[
\boxed{
\Pi_C(z)=c+\rho\frac{w}{\|w\|}
}.
\]

Thus projection onto an intersection of two Euclidean balls with nonempty interior needs no iterative inner solver. The computation uses a constant number of vector differences, norms, and inner products, so its arithmetic cost is \(O(n)\).

This applies directly to the constrained stochastic similar-triangles method in the recent certified-localization framework, whose inner iteration projects onto
\[
Q_k=B(y^{(k)},r_k)\cap B(c,r).
\]
The source states that this projection generally requires a two-multiplier dual problem or Dykstra iteration. The formula above gives the same exact Euclidean projector by a finite active-set test followed, only when both boundaries are active, by a radical-hyperplane projection formula.

## Assumptions and scope

The balls are ordinary closed Euclidean balls in finite-dimensional real space and their intersection has nonempty interior. This is exactly the regularity assumed for the two-ball sets in the source framework.

The statement concerns exact-real arithmetic. A floating-point implementation evaluates norms and a square root and therefore still incurs numerical roundoff. No claim is made here that finite-precision output satisfies the source's exact projection optimality condition without tolerance.

If the centers coincide, the intersection is the smaller ball, and one of the single-ball branches applies. If one ball contains the other, the same is true. The simultaneous-active formula is needed only when neither single-ball projection is feasible.

The formula does not alter any stochastic-gradient query bound. It replaces the computational implementation of the exact projection oracle assumed by the analysis.

## Proof

Because \(C\) is nonempty, closed, and convex, the Euclidean projection \(\Pi_C(z)\) exists and is unique.

First suppose \(z\in C\). Then zero distance is attainable, so
\[
\Pi_C(z)=z.
\]

Now let
\[
p_a=P_{a,r}(z).
\]
If \(p_a\in B(b,R)\), then \(p_a\in C\). Since
\[
C\subseteq B(a,r)
\]
and \(p_a\) minimizes distance from \(z\) over the larger set \(B(a,r)\), it also minimizes distance over \(C\). Thus
\[
\Pi_C(z)=p_a.
\]
The same argument proves the \(p_b\) branch.

Assume next that neither single-ball projection is feasible, and let
\[
p=\Pi_C(z).
\]
The point \(p\) cannot be interior to both balls, because then the normal cone of \(C\) at \(p\) would be trivial, forcing \(p=z\), contrary to \(z\notin C\).

Suppose only the first ball constraint were active at \(p\). Since the second constraint would be inactive, the projection optimality condition would reduce to the normal cone of \(B(a,r)\). Therefore \(p\) would equal the unique single-ball projection \(p_a\), contradicting the fact that \(p_a\notin B(b,R)\). The same contradiction excludes the case in which only the second ball is active. Hence
\[
\|p-a\|=r,
\qquad
\|p-b\|=R.
\]

This simultaneous-active branch cannot occur for concentric balls or strict containment. Because \(C\) has nonempty interior, external tangency is also excluded. Hence, in dimensions at least two, the two boundary spheres have a nontrivial intersection.

Subtracting
\[
\|x-a\|^2=r^2
\]
and
\[
\|x-b\|^2=R^2
\]
shows that every common boundary point lies in a hyperplane orthogonal to \(e\). Solving along the center line gives its center
\[
c=a+se,
\qquad
s=\frac{r^2-R^2+D^2}{2D},
\]
and Pythagoras gives the radius
\[
\rho=\sqrt{r^2-s^2}>0.
\]
Therefore the simultaneous-active feasible set is exactly
\[
S=\left\{
c+u:\ u\perp e,\ \|u\|=\rho
\right\}.
\]

Decompose
\[
z-c=\alpha e+w,
\qquad
w\perp e.
\]
For any \(c+u\in S\),
\[
\|z-(c+u)\|^2
=
\alpha^2+\|w-u\|^2.
\]
The first term is constant, so minimizing over \(S\) is equivalent to maximizing
\[
\langle w,u\rangle
\]
over \(\|u\|=\rho\) in \(e^\perp\). By Cauchy--Schwarz the maximum is attained at
\[
u=\rho\frac{w}{\|w\|},
\]
provided \(w\ne0\).

It remains to justify \(w\ne0\). If \(w=0\), then every point of the positive-radius sphere \(S\) would be at the same distance from \(z\). This would give more than one nearest point to the convex set \(C\), contradicting uniqueness of Euclidean projection. Thus
\[
w\ne0
\]
and the displayed formula follows.

In one dimension the intersection of the two balls is an interval. Projection onto an interval is obtained by clamping to an endpoint, which is always captured by the inside or one-single-ball-feasible branches, so the simultaneous-active branch is unnecessary.

## Verification

The standalone script `artifacts/verify_two_ball_projection.py` implements the closed-form projector and a separate Dykstra projector using only the Python standard library. It checks deterministic edge cases and hundreds of random overlapping-ball instances in dimensions \(2\) through \(8\), including instances where both boundaries are active. It verifies feasibility and compares the closed-form output with a high-accuracy Dykstra iterate.

The numerical replay is supporting evidence only. The quantified formula is proved by the convex active-set argument and the radical-hyperplane geometry above.

## Relationship to prior work

Dvinskikh, Gasnikov, Lobanov, and Latypov use exact Euclidean projections onto intersections of two balls inside their constrained restarted stochastic similar-triangles method. Their projection-model paragraph and Remark 4 explicitly state that simultaneous activity leads to a two-multiplier KKT system, and they propose either a two-dimensional dual solve or Dykstra's algorithm. They do not give the finite active-set closed form above, and their practical implementation avoids the two-ball case.

Caseiro, Facas Vicente, and Vitória give explicit formulas for the center and radius of the intersection of two sphere boundaries and for projection of a point onto that boundary intersection. Their result supplies the geometry of the simultaneous-active seam. It does not state the complete convex projector onto the intersection of two closed balls: the inside and one-active branches and the proof that failure of both single-ball projections forces the sphere-intersection branch are additional ingredients needed for the lens projector.

Thouvenin, Dobigeon, and Tourneret use a nonempty intersection of two closed Frobenius balls in an optimization algorithm and approximate its projection by Dykstra's method. This is a concrete earlier example showing that iterative projection onto a two-ball lens has been used in numerical optimization rather than replaced by the present finite active-set formula.

Targeted searches for Euclidean projection onto an intersection of two balls, lens projection, two-ball KKT projection, and closed-form nearest points did not locate a published statement equivalent to the complete piecewise formula above. A residual risk remains that the same elementary active-set synthesis appears in computational-geometry or software literature under different terminology.

## Limitations

The main mathematical step in the simultaneous-active branch uses classical sphere-intersection geometry. The originality claim is the complete convex lens projector and its consequence for the recent exact projection oracle, not the radical-hyperplane formula by itself.

The exact-real formula does not constitute an inexact-projection robustness theorem. Finite-precision implementations should still test feasibility with tolerances and guard the radicand against small negative roundoff.

The result applies to exactly two Euclidean balls. Intersections of three or more balls generally require a larger active-set analysis and are not covered.

## References

1. D. Dvinskikh, A. Gasnikov, A. Lobanov, I. Latypov, *Localize, Restart, Accelerate: Stochastic Optimization under Generalized Smoothness*, arXiv:2609.06555v1, 2026.
2. R. Caseiro, M. A. Facas Vicente, J. Vitória, *Projection of a Point onto the Intersection of Spheres in Linear Varieties*, Linear Algebra and its Applications 610, 40--51, 2021. DOI: 10.1016/j.laa.2020.09.013.
3. P.-A. Thouvenin, N. Dobigeon, J.-Y. Tourneret, *Online Unmixing of Multitemporal Hyperspectral Images Accounting for Spectral Variability*, IEEE Transactions on Image Processing 25(9), 3979--3990, 2016. DOI: 10.1109/TIP.2016.2579309.
