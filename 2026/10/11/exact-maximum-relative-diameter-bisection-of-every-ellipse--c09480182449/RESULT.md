# Exact maximum-relative-diameter bisection of every ellipse
## Finding
Let
\[
E_{a,b}=\left\{(x,y):\frac{x^2}{a^2}+\frac{y^2}{b^2}\le1\right\},
\qquad a\ge b>0.
\]
For a bisection \(P\) of \(E_{a,b}\) into two connected subsets, define
\[
d_M(P)=\max\{\operatorname{diam}(C_1),\operatorname{diam}(C_2)\}.
\]
Then
\[
\min_P d_M(P)=
\begin{cases}
2b,&a^2\le2b^2,\\[4pt]
\dfrac{a^2}{\sqrt{a^2-b^2}},&a^2\ge2b^2.
\end{cases}
\]
The two branches agree at \(a/b=\sqrt2\).

A minimizing bisection is the line through the minor axis. If \(a>b\), this is the unique minimizing direction among bisections by lines through the center. No uniqueness claim is made among arbitrary nonlinear bisection curves.

There is a geometric phase transition at
\[
\frac ab=\sqrt2.
\]
For \(a/b\le\sqrt2\), the diameter of either half is the minor-axis chord itself. For \(a/b>\sqrt2\), the controlling pair is an endpoint of that chord and another boundary point.

## Assumptions and scope
A bisection is a decomposition into two connected subsets determined by a simple curve whose endpoints lie on the boundary. This is the convention used in the cited maximum-relative-diameter literature; the two subsets need not have equal areas.

The ellipse is centered at the origin with semimajor axis \(a\) on the horizontal axis and semiminor axis \(b\) on the vertical axis. The functional is scale homogeneous.

The proof imports one structural theorem from the literature: for every centrally symmetric planar convex body, the minimum over arbitrary bisections is attained by some straight line through the center. The exact optimization over those center lines is proved here.

## Proof
Parameterize the boundary by
\[
r(t)=(a\cos t,b\sin t).
\]
A center-line bisection whose one endpoint is \(r(t_0)\) cuts the ellipse into congruent halves bounded by the arc
\[
t_0\le t\le t_0+\pi.
\]
By dihedral symmetry we may assume
\[
0\le t_0\le\frac\pi2.
\]
For two boundary parameters \(t,s\), put
\[
m=\frac{t+s}{2},\qquad d=\frac{t-s}{2}.
\]
A direct trigonometric calculation gives
\[
\lVert r(t)-r(s)\rVert^2
=4\sin^2d\left(a^2\sin^2m+b^2\cos^2m\right).
\tag{1}
\]

Consider first the minor-axis bisection \(t_0=\pi/2\). For fixed \(d\in[0,\pi/2]\), the admissible midpoint interval is
\[
\frac\pi2+d\le m\le\frac{3\pi}{2}-d.
\]
On this interval the bracket in (1) is maximized at an endpoint, where \(\sin^2m=\cos^2d\). Hence the squared diameter of a half-ellipse is
\[
\max_{0\le d\le\pi/2}
4\sin^2d\left(a^2\cos^2d+b^2\sin^2d\right).
\]
With \(u=\sin^2d\), this becomes
\[
\max_{0\le u\le1}4u\left(a^2-(a^2-b^2)u\right).
\tag{2}
\]
If \(a^2\le2b^2\), the concave quadratic in (2) is increasing through \(u=1\), so its maximum is \(4b^2\). Thus
\[
d_M=2b.
\]
If \(a^2>2b^2\), its vertex lies at
\[
u_*=\frac{a^2}{2(a^2-b^2)}\in(0,1),
\]
and (2) equals
\[
\frac{a^4}{a^2-b^2}.
\]
Therefore
\[
d_M=\frac{a^2}{\sqrt{a^2-b^2}}.
\]
Writing \(d_*\in(0,\pi/2)\) for the corresponding half-separation,
\[
\sin^2d_*=\frac{a^2}{2(a^2-b^2)}.
\]
This proves the claimed value for the minor-axis bisection.

It remains to show that no other center-line direction improves it. The chord of the bisection at direction \(t_0\) has length
\[
L(t_0)=2\sqrt{a^2\cos^2t_0+b^2\sin^2t_0}.
\tag{3}
\]
This chord is contained in both closed halves, so it is always a lower bound for their common diameter.

Suppose first that \(a^2\le2b^2\). From (3),
\[
L(t_0)\ge2b,
\]
with equality only at \(t_0=\pi/2\) when \(a>b\). Since the minor-axis cut attains \(2b\), it is optimal, and its center-line direction is unique for a noncircular ellipse.

Now suppose \(a^2>2b^2\), and let
\[
M=\frac{a^2}{\sqrt{a^2-b^2}}.
\]
If \(t_0\le d_*\), then \(L(t_0)\ge L(d_*)\), while
\[
L(d_*)^2=2a^2>M^2
\]
because \(a^2>2b^2\). Hence such a direction is strictly worse than the minor-axis cut.

If \(d_*\le t_0<\pi/2\), choose two points of the same half with
\[
m=\frac\pi2+d_*,
\qquad
d=\frac\pi2+d_*-t_0.
\]
They are admissible because \(d_*\le t_0\le\pi/2\), and \(d>d_*\) unless \(t_0=\pi/2\). In (1), their bracket equals
\[
a^2\cos^2d_*+b^2\sin^2d_*=\frac{a^2}{2}.
\]
Therefore their distance is at least \(M\), with strict inequality for every \(t_0<\pi/2\). Thus the minor-axis line is the unique minimizing center-line direction for every noncircular ellipse.

Finally, the cited center-line reduction theorem for centrally symmetric planar convex bodies says that every arbitrary bisection can be replaced by a center-line bisection with no larger maximum relative diameter. Hence the minimum over all bisections equals the center-line minimum computed above.

## Verification
The supplied `verify.py` checks the chord identity (1), the quadratic reduction (2), both branch values, the threshold agreement, and the two lower-bound arguments for arbitrary center-line directions. It also performs dense numerical regression checks for several aspect ratios on both sides of \(\sqrt2\).

The finite scan is not used as proof. The all-parameter result follows from the exact concave quadratic and the two analytic orientation bounds in the proof.

## Relationship to prior work
The 2016 paper on maximum relative diameter for multi-rotationally symmetric planar convex bodies records that in the twofold-symmetric case a minimizing equal-area two-partition is known to be a line through the center, but states that a more precise description was not known there. Its first public preprint appeared in 2015.

The 2018 paper devoted to centrally symmetric bisections proves a stronger center-line reduction for arbitrary bisections and explicitly states that the standard bisection of an ellipse is minimizing. It does not give a formula in terms of the semiaxes, identify the \(a/b=\sqrt2\) transition, or classify the active farthest-pair mechanism.

Targeted searches for the maximum-relative-diameter value of an ellipse, the semiaxis formula, the \(\sqrt2\) transition, and the expression \(a^2/\sqrt{a^2-b^2}\) did not locate a covering formula or table.

## Limitations
The result computes the optimum value and proves uniqueness only among center-line directions. General diameter-based bisection problems can have many nonlinear minimizers, and no classification of all such curves is asserted.

The result is specific to Euclidean ellipses. It does not extend automatically to arbitrary centrally symmetric smooth convex bodies.

The literature contains the prior fact that the minor-axis standard bisection is minimizing for ellipses; novelty is claimed only for the exact all-aspect-ratio value, transition, and center-line uniqueness proof.

## References
1. A. Cañete, *The maximum relative diameter for multi-rotationally symmetric planar convex bodies*, Mathematical Inequalities & Applications 19 (2016), 335--347. DOI: 10.7153/mia-19-25. First public preprint: arXiv:1511.08009v1, 2015-11-25.
2. A. Cañete and S. Segura Gomis, *Bisections of centrally symmetric planar convex bodies minimizing the maximum relative diameter*, arXiv:1803.00321v1, 2018-03-01.
3. C. Miori, C. Peri, and S. Segura Gomis, *On fencing problems*, Journal of Mathematical Analysis and Applications 300 (2004), 464--476.
