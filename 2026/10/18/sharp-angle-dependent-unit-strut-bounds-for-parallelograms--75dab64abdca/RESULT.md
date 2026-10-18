# Sharp angle-dependent unit-strut bounds for parallelograms

## Finding

A *unit strut* for a side with endpoints \(U,V\) of a convex polygon is a point \(W\) in the **closed** polygon, **not a vertex of the polygon**, satisfying \(\|W-U\|_2=\|W-V\|_2=1\). A polygon has the unit-strut property when every side has such a point.

**Theorem.** Let \(P\) be any nondegenerate Euclidean parallelogram with adjacent side lengths \(a,b>0\) and acute (or right) angle \(\varphi\in(0,\pi/2]\). Set \(c=\cos\varphi\in[0,1)\), \(s=\sin\varphi>0\), and \(L=2(a+b)\). Then \(P\) has the unit-strut property if and only if **all** the following hold:

\[
2c\le a,b\le2,\qquad a^2+4s^2b^2\ge4,\qquad b^2+4s^2a^2\ge4,
\]

and the single triple \(c=1/2,\ a=b=1\) is excluded. This one excluded boundary configuration is necessary because the only candidate strut on each side is a polygon vertex.

For every fixed \(\varphi\), the **sharp infimum** of the perimeter over unit-strut parallelograms is

\[
\boxed{\inf L=\begin{cases}
\dfrac{8}{\sqrt{5-4c^2}},&0\le c\le\tfrac12,\\[4pt]
8c,&\tfrac12\le c<1.
\end{cases}}
\]

At \(c\ne\tfrac12\) this infimum is attained, uniquely up to congruence, by a rhombus with side length \(2/\sqrt{5-4c^2}\) for \(c<1/2\), or \(2c\) for \(c>1/2\). At \(c=1/2\), corresponding to acute angle \(60^\circ\), the infimum is \(4\) but is **not attained**. It is approached by rhombi whose side lengths decrease to \(1\) from above. In particular every unit-strut parallelogram satisfies

\[
\boxed{L\ge\frac8{\sqrt5}},
\]

with equality if and only if it is a square of side \(2/\sqrt5\).

## Assumptions and scope

The Euclidean distance is used throughout, and a strut point is allowed on the polygon's boundary but may not be one of its vertices. The acute angle is the smaller angle between consecutive sides; treating an obtuse angle instead gives the same classification with \(|\cos\varphi|\). Side lengths are positive and angles exclude degeneracy. A length-\(\ell\) strut, for any \(\ell>0\), is covered by scaling every length in the theorem by \(\ell\). No assertion is made about arbitrary quadrilaterals or about consecutive struts on only part of a polygon.

## Proof

### Exact side-witness criterion

By a Euclidean congruence write the vertices in counterclockwise order as \(O=(0,0)\), \(U=(a,0)\), \(U+V=(a+bc,bs)\), and \(V=(bc,bs)\), where \(c\ge0\). Consider the side \([O,U]\). Its two circle intersections of unit radius about its endpoints exist precisely when \(a\le2\); for \(a<2\), the only intersection lying on the interior side of its supporting line is

\[
W_a=\left(\frac a2,\sqrt{1-\frac{a^2}4}\right).
\]

Put \(h_a=\sqrt{1-a^2/4}\), including \(h_a=0\) when \(a=2\). Expressing \(W_a=\lambda U+\mu V\) gives

\[
\mu=\frac{h_a}{bs},\qquad \lambda=\frac12-\frac{ch_a}{as}.
\]

This point is in the closed parallelogram exactly when \(0\le\lambda,\mu\le1\). Since \(h_a,c\ge0\), these conditions are equivalent to

\[
h_a\le bs,\qquad 2ch_a\le as.
\]

Squaring the second (all terms are nonnegative) and using \(s^2+c^2=1\) gives precisely \(a\ge2c\); squaring the first gives \(a^2+4b^2s^2\ge4\). Thus a geometric strut candidate exists if and only if \(2c\le a\le2\) and \(a^2+4s^2b^2\ge4\).

The point \(W_a\) is never \(O\) or \(U\). It equals another polygon vertex only if \((\lambda,\mu)=(0,1)\), which happens exactly when \(a=2c\) and \(b=1\): indeed \(\lambda=0\) forces \(a=2c\), in which case \(h_a=s\), and \(\mu=1\) forces \(b=1\). For \(a=2\) the midpoint of the side is a legitimate nonvertex strut. The congruent opposite side has the same criterion. Interchanging \(a,b\) gives the other side type and its potential vertex exception \((a,b)=(1,2c)\). Under both side types' feasibility inequalities, the first exception \((a,b)=(2c,1)\) can occur only when \(c=1/2\): the other side requires \(2c\le1\) and \(1+16c^2(1-c^2)\ge4\); for \(0\le c\le1/2\), the second inequality is possible only at \(c=1/2\). The transposed exception is identical. Thus the only globally feasible vertex-only case is \(c=1/2,\ a=b=1\), proving the exact if-and-only-if description.

### Sharp fixed-angle perimeter

First suppose \(c\ge1/2\). Every admissible pair satisfies \(a,b\ge2c\), so \(L=2(a+b)\ge8c\). The candidate \(a=b=2c\) satisfies the remaining quadratic inequalities, because

\[
c^2(5-4c^2)-1=(1-c^2)(4c^2-1)\ge0.
\]

For \(1/2<c<1\), its strut point for \([O,U]\) lies on the adjacent side \([O,V]\) at fraction \(1/(2c)\in(0,1)\), so it is not a vertex; symmetry handles the remaining sides. Equality in the perimeter estimate forces this rhombus. At \(c=1/2\), equality would force \(a=b=1\), but each purported strut is a polygon vertex and is forbidden. Rhombi with \(a=b>1\), sufficiently close to \(1\), satisfy all strict inequalities and are admissible, giving the unattained infimum \(4\).

Now suppose \(0\le c\le1/2\). Write \(k=4s^2=4(1-c^2)\ge3\). For an admissible parallelogram, swap the names of the side types if necessary so that \(0<a\le b\). Its quadratic constraints include

\[
4\le b^2+ka^2.
\]

Set \(S=a+b\) and \(x=a/S\in(0,1/2]\). Then

\[
4\le S^2\bigl((1-x)^2+kx^2\bigr).
\]

The quadratic \(f(x)=(1-x)^2+kx^2\) is strictly convex on \([0,1/2]\); its endpoint values are \(f(0)=1\) and \(f(1/2)=(1+k)/4\ge1\). Therefore \(f(x)\le(1+k)/4\), with equality for \(x>0\) only at \(x=1/2\). Hence

\[
L=2S\ge \frac8{\sqrt{1+k}}=\frac8{\sqrt{5-4c^2}},
\]

and equality forces \(a=b=2/\sqrt{5-4c^2}\). This length is at least \(2c\), because

\[
1-c^2(5-4c^2)=(1-c^2)(1-4c^2)\ge0.
\]

For \(c<1/2\) its strut point for \([O,U]\) lies in the relative interior of the opposite side \([V,U+V]\), with affine coordinates \(\mu=1\) and \(\lambda=1/2-c\in(0,1)\). Thus the equality rhombus is admissible. The boundary case \(c=1/2\) has already been analyzed. The same calculation establishes uniqueness up to congruence.

Finally, the fixed-angle lower bound is strictly increasing as a function of \(c\in[0,1)\): each displayed branch is strictly increasing away from \(c=0\), and the branches match at \(c=1/2\). Its global minimum is therefore \(8/\sqrt5\) at \(c=0\), with only the square equality case. This completes the proof.

## Verification

A standalone `checker.py` checks the polynomial factorization symbolically, compares the exact rational feasibility conditions with direct geometric point containment and vertex exclusions for 720 cases, tests four forbidden-vertex boundaries, checks three admitted sharp rhombi, and checks the perimeter lower bound on 222 feasible rational cases. Running `python checker.py` prints a single `PASS` line. The proof above establishes the universal quantifiers independently of these finite experiments.

## Relationship to prior work

Nikonorov and Nikonorova introduced the side-strut condition in *Some extremal problems for polygons in the Euclidean plane* (first arXiv version September 13, 2022), proving a universal perimeter bound \(L\ge3\) for polygons with a unit strut at every side, and posing related questions for only some consecutive sides. Their result does not give the exact angle-resolved feasible region or the sharp parallelogram perimeter bound obtained here. The relative self-Chebyshev radius problem studied by Balestro, Martini, Nikonorov and Nikonorova (2020) has a different quantifier structure: it minimizes a maximum farthest-point distance on a boundary rather than requiring an equidistant nonvertex witness for each edge.

## Limitations

The result concerns Euclidean parallelograms only; the published general polygon theorem is not improved outside this subclass. The nonvertex restriction matters at precisely stated boundary points. The numerical checker is corroborative and cannot establish originality or extend the result to arbitrary polygons. An unindexed prior treatment of this elementary-looking specialized case cannot be excluded without broader bibliographic checking.

## References

1. Yu. G. Nikonorov and O. Yu. Nikonorova, *Some extremal problems for polygons in the Euclidean plane*, arXiv:2209.05940v1, publicly posted 2022-09-13; revised v2 2022-10-01. https://arxiv.org/abs/2209.05940 . In particular, Definition of a strut and Theorems 1–3.
2. V. Balestro, H. Martini, Yu. Nikonorov and Yu. Nikonorova, *Extremal problems for convex curves with given relative Chebyshev radius*, arXiv:2010.06315v1, publicly posted 2020-10-13. https://arxiv.org/abs/2010.06315 .
