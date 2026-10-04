# A one-dimensional derivative law for orthogonal-disk mean width
## Finding
For \(\delta\ge 0\), let \(D_-(\delta)\) be the unit disk in the plane \(z=0\) centered at \((0,-\delta/2,0)\), let \(D_+(\delta)\) be the unit disk in the plane \(x=0\) centered at \((0,\delta/2,0)\), and set \(K_\delta=\operatorname{conv}(D_-(\delta)\cup D_+(\delta))\). Let \(W(\delta)\) denote the mean width of \(K_\delta\), normalized as the spherical average of directional width.

For \(u=(a,b,c)\in S^2\), put \(A=\sqrt{a^2+b^2}\) and \(B=\sqrt{b^2+c^2}\). Then
\[
w_\delta(u)=A+B+\max\{|A-B|,\delta |b|\}.
\]
For every \(\delta>0\), write \(t_\delta=(1+\delta)^{-1}\) and
\[
r_\delta(t)=\frac{\delta t\sqrt{2+(2-\delta^2)t^2}}{1-t^2}.
\]
Then
\[
W'(\delta)=\frac{2}{\pi}\int_0^{t_\delta} t\arcsin(r_\delta(t))\,dt+\frac12(1-t_\delta^2),
\]
and
\[
W''(\delta)=\frac{4}{\pi}\int_0^{t_\delta}
\frac{t^2[1+(1-\delta^2)t^2]}
{\sqrt{2+(2-\delta^2)t^2}\sqrt{[1-(\delta-1)^2t^2][1-(\delta+1)^2t^2]}}\,dt>0.
\]
Consequently \(W\) is strictly convex on \((0,\infty)\), is strictly increasing for \(\delta>0\), satisfies \(W'(0+)=0\), and has asymptotic slope \(\lim_{\delta\to\infty}W'(\delta)=1/2\).

## Assumptions and scope
The disks have equal radius one, lie in perpendicular coordinate planes, and their centers are displaced symmetrically by \(\delta\) along their common line. The result concerns mean width only. Scaling both disks by a common factor scales \(W\) by the same factor. The result does not give a closed form for \(W(\delta)\) at every separation and, in particular, does not claim to settle the closed-form evaluation of the classical two-circle roller at its distinguished separation.

## Proof
The support functions of the two disks are
\[
h_-(u)=A-\frac{\delta b}{2},\qquad h_+(u)=B+\frac{\delta b}{2}.
\]
Since the support function of a convex hull is the maximum of the support functions of its generators,
\[
w_\delta(u)=h_{K_\delta}(u)+h_{K_\delta}(-u)
=\max\{A-\delta b/2,B+\delta b/2\}+\max\{A+\delta b/2,B-\delta b/2\}.
\]
Using \(\max(q,r)=(q+r+|q-r|)/2\) gives the stated formula \(A+B+\max\{|A-B|,\delta|b|\}\).

For a uniformly distributed direction on \(S^2\), \(t=|b|\) is uniform on \([0,1]\). Conditional on \(t\), write
\[
a=\sqrt{1-t^2}\cos\phi,\qquad c=\sqrt{1-t^2}\sin\phi,
\]
with \(\phi\) uniform modulo the symmetries. It is enough to take \(0\le\phi\le\pi/4\), where \(A\ge B\). The switching condition \(A-B=\delta t\) implies
\[
(A+B)^2=2+(2-\delta^2)t^2,
\]
and therefore
\[
\cos(2\phi)=\frac{\delta t\sqrt{2+(2-\delta^2)t^2}}{1-t^2}=r_\delta(t).
\]
At \(\phi=0\), \(A-B=1-t\), so switching exists precisely for \(0<t<t_\delta\). The conditional fraction of angles for which the linear term \(\delta t\) dominates is \((2/\pi)\arcsin(r_\delta(t))\) below \(t_\delta\), and is one above it. Differentiation under the integral therefore yields the formula for \(W'(\delta)\).

At \(t=t_\delta\), \(r_\delta(t)=1\), so the moving-endpoint contributions cancel when differentiating again. Direct differentiation gives
\[
\partial_\delta r_\delta(t)=\frac{2t[1+(1-\delta^2)t^2]}{(1-t^2)\sqrt{2+(2-\delta^2)t^2}},
\]
while
\[
1-r_\delta(t)^2=
\frac{[1-(\delta-1)^2t^2][1-(\delta+1)^2t^2]}{(1-t^2)^2}.
\]
Combining these identities yields the formula for \(W''(\delta)\). Its integrand is positive. If \(0<\delta\le1\), the numerator is immediate. If \(\delta>1\) and \(t<t_\delta\), then
\[
(\delta^2-1)t^2<\frac{\delta-1}{\delta+1}<1,
\]
so the numerator remains positive. The endpoint singularity is of square-root type and integrable. Hence \(W''(\delta)>0\).

The formula for \(W'(\delta)\) gives \(W'(0+)=0\), so strict convexity implies strict increase for positive \(\delta\). Finally, for almost every direction the derivative of \(\max\{|A-B|,\delta|b|\}\) tends to \(|b|\) as \(\delta\to\infty\), and is bounded by \(|b|\). Dominated convergence gives \(\lim W'(\delta)=\mathbb E|b|=1/2\).

## Verification
The identities were checked symbolically by direct expansion and independently sampled numerically. The bundled checker evaluates the one-dimensional second-derivative integral at several positive separations, checks positivity, and verifies the known closed mean width at the separated configuration \(\delta=2\) by direct spherical quadrature. These computations are diagnostic; the proof above is analytic.

## Relationship to prior work
Finch introduced three convex hulls of two orthogonal unit disks and, for the two-circle roller, stated that an exact mean-width expression remained open. His discrete configurations include distinguished separations but do not provide a separation-parameter derivative law. Bäsel later evaluated the mean width of the oloid, which is the member \(\delta=1\) of the present family. Nash, Pir, Sottile, and Ying studied the convex hull of two circles in three-space from algebraic and convex-geometric viewpoints, but their inspected treatment does not give this mean-width profile. Generic support-function theory already implies non-strict convexity of a mean width built from maxima of affine functions of the displacement parameter; the new statement here is the explicit switching reduction, the one-dimensional formulas for \(W'\) and \(W''\), and the proof of global strict convexity and limiting slope for this natural orthogonal-disk family.

## Limitations
No claim is made that every value \(W(\delta)\) has an elementary or classical-special-function closed form. The result is specific to equal disks in perpendicular planes with centers moving along their common line. A residual literature risk remains that an unindexed or differently phrased treatment of the full one-parameter mean-width profile predates this calculation.

## References
- Steven R. Finch, “Convex Hull of Two Orthogonal Disks,” arXiv:1211.4514, first public version 2012-11-19.
- Uwe Bäsel, “The mean width of the oloid and integral geometric applications of it,” arXiv:1604.07245.
- Michael Nash, Ata Fırat Pir, Frank Sottile, and Li Ying, “Convex Hull of Two Circles in R3,” arXiv:1612.09382.
