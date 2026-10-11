# Optimized annulus protection scale for regular even polygons
## Finding
Let \(N\ge6\) be even, and let \(P_N\) be a regular \(N\)-gon normalized so that its minimal width is \(1\). Set
\[
a=\frac{\pi}{N},
\qquad
s=\sin^2 a,
\]
and define
\[
\boxed{
\delta_N=
\frac{s\bigl(3-2s-2\sqrt2(1-s)\bigr)}
{1+4s-4s^2}
}.
\tag{1}
\]

If \(H\subset\operatorname{int}P_N\) is any set whose width in every direction perpendicular to a side of \(P_N\) is at most \(\delta_N\), then every finite collection of strips covering
\[
P_N\setminus H
\]
has total width at least \(1\).

In particular, if \(0<\delta\le\delta_N\), then the conclusion holds when \(H\) is any translate, contained in the interior, of the same-orientation homothetic copy
\[
\delta P_N.
\]

The constant in (1) is the largest width threshold certified by optimizing the free parameter in the explicit quantitative inequalities appearing in White--Wisewell's proof for this regular family. It is not asserted to be the true optimal hole size in Bezdek's problem.

The first values are approximately
\[
\delta_6=0.0540971,\quad
\delta_8=0.0285955,\quad
\delta_{10}=0.0177912,\quad
\delta_{12}=0.0121685.
\]
Moreover,
\[
\delta_N\sim
(3-2\sqrt2)\frac{\pi^2}{N^2}.
\tag{2}
\]

## Assumptions and scope
A strip is the closed region between two parallel lines, and its width is the distance between those lines.

White and Wisewell prove that for a polygon satisfying their positive angle criterion, one may choose a number \(\varepsilon>0\) so that a hole whose side-normal widths are all at most \(\varepsilon\) cannot lower the total strip width needed to cover the remainder. Their proof gives four explicit sufficient inequalities for \(\varepsilon\). The present argument specializes and optimizes those inequalities for regular even polygons.

For a regular even \(N\)-gon of minimal width \(1\), every side is one of White--Wisewell's special sides. Its inradius is \(1/2\), its circumradius is
\[
R=\frac1{2\cos a},
\]
and its side length is
\[
c=2R\sin a=\tan a.
\tag{3}
\]
The projection overlap \(c\) used in their proof is therefore exactly \(\tan a\).

A same-orientation homothetic copy \(\delta P_N\) has width \(\delta\) in every side-normal direction, so the side-normal-width formulation immediately implies the homothetic-annulus statement.

## Proof
White--Wisewell's first explicit condition is
\[
\varepsilon\le
\frac{1-\lambda}{2}\,
c\min\sin\theta,
\qquad 0<\lambda<1,
\tag{4}
\]
where \(\theta\) runs over the internal angles adjacent to special edges.

For \(P_N\), every internal angle is
\[
\pi-2a.
\]
Using (3),
\[
\frac{1-\lambda}{2}\tan a\sin(2a)
=
(1-\lambda)\sin^2a.
\]
Thus (4) becomes
\[
\varepsilon\le A(\lambda):=(1-\lambda)s.
\tag{5}
\]

There are no non-special edges, so White--Wisewell's second condition is vacuous.

Their third condition becomes
\[
\varepsilon\le
B(\lambda):=
\frac12\left(
1-\sqrt{1-\lambda^2\tan^2a}
\right).
\tag{6}
\]
Here \(A\) is strictly decreasing and \(B\) is strictly increasing on \((0,1)\). Hence
\[
\max_{0<\lambda<1}\min\{A(\lambda),B(\lambda)\}
\]
is attained at their unique intersection.

Put
\[
u=1-\lambda.
\]
The equation \(A=B\) is equivalent, after one squaring with both sides nonnegative, to
\[
(1+4s-4s^2)u^2+(4s-6)u+1=0.
\tag{7}
\]
Its discriminant is
\[
32(1-s)^2.
\]
The root in \((0,1)\) is
\[
u=
\frac{3-2s-2\sqrt2(1-s)}
{1+4s-4s^2}.
\tag{8}
\]
Since the optimized value is \(su\), equations (1) and (8) follow.

It remains to check that White--Wisewell's fourth inequality does not lower this value. That condition has right-hand side
\[
\frac c2
\min_\theta\frac{\sin\theta}{1-\cos\theta}.
\tag{9}
\]
For sides of a regular \(N\)-gon, any nonparallel side angle in \((0,\pi)\) is an integral multiple of \(2a\). Consequently
\[
\frac{\sin\theta}{1-\cos\theta}
=
\cot\frac\theta2
\ge \tan a
\]
for every angle occurring in (9). Therefore (9) is at least
\[
\frac12\tan^2a.
\tag{10}
\]

For even \(N\ge6\),
\[
0<s\le\frac14.
\]
The expression in (8) satisfies \(u<1/2\) throughout this interval. One direct check is that the denominator minus twice the numerator equals
\[
(4\sqrt2-5)+(8-4\sqrt2)s-4s^2,
\]
which is positive on \([0,1/4]\). Hence
\[
\delta_N=su<\frac s2
\le
\frac{s}{2(1-s)}
=
\frac12\tan^2a.
\]
Thus (10) is never active at the optimizer.

White--Wisewell's proof of their positive theorem then applies with
\[
\varepsilon=\delta_N.
\]
They explicitly observe that their diameter restriction may be replaced by the requirement that the hole have width at most \(\varepsilon\) in every direction perpendicular to a side. This proves the stated strip-covering conclusion.

Finally, as \(N\to\infty\),
\[
s=\sin^2\frac{\pi}{N}
\sim\frac{\pi^2}{N^2},
\]
while the factor \(u\) in (8) tends to
\[
3-2\sqrt2.
\]
This proves (2).

## Verification
The bundled `verify.py` performs two independent checks of the algebra used above.

First, symbolic simplification verifies that the expression (8) is an exact root of (7), that the discriminant is \(32(1-s)^2\), and that the asymptotic coefficient is \(3-2\sqrt2\).

Second, for every even \(N\) from \(6\) through \(400\), it checks numerically that:
\[
0<u<\frac12,
\]
the two active White--Wisewell bounds agree at the displayed optimizer, the fourth bound is strictly larger, and a dense grid in \(\lambda\) never exceeds the claimed optimized minimum.

The finite sweep is diagnostic only. The quantified theorem follows from the exact specialization and monotonicity argument in the proof.

## Relationship to prior work
Bezdek asked whether removing a sufficiently small homothetic copy from a convex body preserves Bang's lower bound on the total width of a strip cover.

White and Wisewell characterize the polygons for which such a positive statement holds. They state explicitly that every regular even polygon belongs to the positive class. Their proof introduces four quantitative restrictions on the translation scale. They also say that actual bounds are unnecessary for their theorem except for obtaining an explicit estimate for the square, and they optimize that square case to recover the known factor
\[
1-\frac1{\sqrt2}.
\]
They do not give an explicit all-\(N\) threshold for regular even polygons.

Zhang and Ding subsequently restate the positive result for polygons having an incircle tangent to two parallel sides, again including regular even polygons. Their paper records the same square estimate but does not provide a regular-even-\(N\) formula.

Formula (1) is obtained by carrying the quantitative part of White--Wisewell's proof through the full regular even family and optimizing its only free parameter. It therefore quantifies a previously qualitative infinite family, while remaining deliberately weaker than a claim of optimality for the original annulus problem.

Targeted searches under polygonal annuli, regular even polygons, regular hexagons, strip/plank coverings, explicit \(\varepsilon\), and the radical/trigonometric fingerprint in (1) did not locate an implication-equivalent published formula.

## Limitations
The constant \(\delta_N\) is a certified threshold furnished by the White--Wisewell method. It is not proved to be the largest possible homothetic hole for which the annulus theorem is true.

The theorem is stated for even regular polygons with \(N\ge6\). The square is exceptional in the proof because its translation step doubles the raw \(\varepsilon\); its sharper factor \(1-1/\sqrt2\) is prior work.

The homothetic corollary uses a same-orientation copy. The stronger side-normal-width statement applies to arbitrary holes satisfying the indicated directional width bounds.

The exact specialization is elementary once the source inequalities are known, so an unindexed calculation in older notes remains a historical originality risk.

## References
1. S. A. White and L. Wisewell, *Covering polygonal annuli by strips*, *Discrete & Computational Geometry* 37 (2007), 577--585. DOI: 10.1007/s00454-007-1305-z.
2. Y. Zhang and R. Ding, *A Note about Bezdek's Conjecture on Covering an Annulus by Strips*, *Electronic Journal of Combinatorics* 15 (2008), #N19. DOI: 10.37236/894.
3. A. Bezdek, *Covering an annulus by strips*, *Discrete & Computational Geometry* 30 (2003), 177--180. DOI: 10.1007/s00454-003-0002-y.
