# Review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

The defining source was inspected at Definition 1 and Lemma 7. Its roundness
is the length cut out by the perpendicular bisector of \(pq\), divided by
\(|pq|\), followed by an infimum over distinct \(p,q\in S\).

The lower bound in Theorem 1 was rederived directly for an arbitrary pair.
After normalizing \(p=(-1,0)\), \(q=(1,0)\), supporting side lines at the two
ends of the perpendicular-bisector chord have equations
\(y=h_++ax\) and \(y=-h_-+bx\). Containment of both \(p\) and \(q\) forces
\(h_+\ge|a|\) and \(h_-\ge|b|\). The smaller angle between any two side
lines of a triangle is at least its minimum interior angle \(\alpha\): at an
obtuse vertex that smaller line angle is the supplement of the interior
angle, hence the sum of the other two angles and at least \(2\alpha\).
Convexity of tangent on \([0,\pi/2)\) then gives
\[
(h_++h_-)/2\ge \tan(\alpha/2).
\]
The possible vertical-support degeneracy was checked: a vertical supporting
line through the perpendicular bisector cannot contain the two normalized
points \(x=\pm1\) in one supporting half-plane.

For equality, the pair consisting of a minimum-angle vertex and the opposite
angle-bisector foot was checked explicitly. The angle-bisector length is
\(2bc\cos(\alpha/2)/(b+c)\); the perpendicular bisector at its midpoint
meets both adjacent sides before their endpoints, and its chord length is
exactly the angle-bisector length times \(\tan(\alpha/2)\).

The sharp fatness window was checked with the two correct branches of the
smallest enclosing disk of a triangle. If the largest angle is at least
\(\pi/2\), the containing radius is half the longest side and
\[
\rho=2tu/(t+u).
\]
If the largest angle is at most \(\pi/2\), the containing radius is the
ordinary triangle circumradius and
\[
\rho=\frac{4tu(1-tu)}{(1+t^2)(1+u^2)}.
\]
For fixed \(t=\tan(\alpha/2)\), both expressions are monotone increasing in
the permitted \(u=\tan(\beta/2)\) range; the derivative in the acute branch
is proportional to \(1-u^2-2tu\) and vanishes exactly at the isosceles
upper endpoint. This gives the displayed piecewise lower envelope and
isosceles upper envelope. The two lower formulas coincide at
\(t=\sqrt2-1\), and both envelopes coincide at the equilateral endpoint
\(t=1/\sqrt3\).

The linear corollary was also checked at the endpoints. On the second lower
branch \(L(t)/t=4t(1-t^2)/(1+t^2)^2\) is decreasing on
\([\sqrt2-1,1/\sqrt3]\) and equals \(\sqrt3/2\) at the right endpoint.
The upper ratio tends to \(2\) as \(t\downarrow0\), so both constants are
sharp in the stated senses.

## Originality

The complete Pach--Tardos preprint was inspected around the definition of
roundness, its comparison with area/diameter and inradius/circumradius
fatness, and the equal-area partition theorem. It records \(C=1\) for the
disk and square and the general inequalities \(D\le C\le2D\) and
\(0.28C\le r/R\le2C\), but does not state or derive the triangle formula
\(C(T)=\tan(\alpha_{\min}/2)\), its minimizing angle-bisector pair, or the
sharp triangle-specific \(r/R\) window.

Searches covered the source title and arXiv identifier, the exact
perpendicular-bisector definition, "roundness" combined with triangle and
minimum-angle terminology, half-angle formulations, and standard mesh-quality
language. They found standard literature relating minimum angle to other
triangle quality measures, but no source using the newly introduced
Pach--Tardos invariant or implying the exact formula above. Searches of the
current SCOPE archive by the source identifier, authors, roundness, and the
claim family found no overlap.

No inaccessible paper was identified whose metadata specifically suggests
prior coverage of this invariant. The source preprint is dated
17 September 2026, so unindexed or unpublished parallel work remains a
non-negligible residual risk.

## Value

The result gives the first exact calibration, beyond the disk and square
examples in the source, of a newly introduced convex-geometric invariant on a
major model class. For triangles it identifies the invariant with the
minimum-angle condition used throughout mesh generation and finite-element
geometry. The second theorem is stronger than a qualitative equivalence: it
determines the full sharp range of classical inradius/smallest-containing-disk
fatness at each fixed roundness and improves the general lower conversion
constant \(0.28\) to the optimal triangle constant \(\sqrt3/2\).

## Limitations

The formulas are triangle-specific. No improvement is claimed for arbitrary
convex bodies or for the partition constant in the source paper. The
circumradius in the fatness statement is the convex-body circumradius (smallest
containing disk), not necessarily the radius of the three-point circumcircle.
Very recent parallel work may not yet be indexed.
