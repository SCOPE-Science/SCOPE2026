# Sharp lower area profile and reverse stability for cyclic quadrilaterals

## Statement

Let \(Q\) be a nondegenerate convex **cyclic** Euclidean quadrilateral with side lengths
\[
a_1,a_2,a_3,a_4>0,
\]
perimeter \(P=\sum_i a_i\), area \(K\), and mean side length
\[
\mu=\frac P4.
\]
Write
\[
V=\sum_{i=1}^4(a_i-\mu)^2,
\qquad
q=\frac{V}{\mu^2}=\frac{16V}{P^2}.
\]
The strict quadrilateral inequalities imply \(0\le q<4\).

For \(0\le q<4/3\), put
\[
r=\frac{\sqrt{3q}}2\in[0,1)
\]
and define
\[
m(q)=(1-r)\left(1+\frac r3\right)^3.
\]
Then
\[
\boxed{
K\ge \mu^2\sqrt{m(q)}
=\frac{P^2}{16}
\sqrt{(1-r)\left(1+\frac r3\right)^3}.
}
\tag{1}
\]
This is sharp, and equality holds exactly when, up to permutation, the side multiset is
\[
\boxed{
\left\{
\mu(1+r),
\mu\left(1-\frac r3\right),
\mu\left(1-\frac r3\right),
\mu\left(1-\frac r3\right)
\right\}.
}
\tag{2}
\]
At \(q=0\) this is the square.

At the threshold
\[
\boxed{q=\frac43}
\tag{3}
\]
the behavior changes. For every \(4/3\le q<4\), the infimum of \(K\) among cyclic quadrilaterals with the prescribed \((P,q)\) is
\[
\boxed{\inf K=0.}
\tag{4}
\]
It is not attained by a nondegenerate quadrilateral. At \(q=4/3\) it is approached by the side ratio \(3:1:1:1\); for larger \(q\), it is approached by cyclic quadrilaterals tending to the ordinary degenerate boundary where one side equals the sum of the other three.

A global consequence is the sharp **reverse side-variance stability inequality**
\[
\boxed{
P^2-16K\le 12V
=12\sum_{i=1}^4\left(a_i-\frac P4\right)^2.
}
\tag{5}
\]
The constant \(12\) is best possible and is not attained in the nondegenerate class; it is approached along the equality family (2) as \(q\uparrow4/3\).

Equivalently, every nondegenerate cyclic quadrilateral satisfies
\[
\boxed{
4K\ge P^2-3\sum_{i=1}^4 a_i^2.
}
\tag{6}
\]

Together with the sharp inequality of Giugiuc--Oai--Altintas (2018), which supplies the opposite deficit estimate, (5) yields the sharp two-sided comparison
\[
\boxed{
\left(12-\frac{16}{\sqrt3}\right)V
\le P^2-16K\le 12V
}
\tag{7}
\]
for cyclic quadrilaterals. The left-hand inequality is prior work; the right-hand inequality and the exact lower profile (1)--(4) are the contribution claimed here, to the best of our knowledge.

## Context and prior boundary

Brahmagupta's formula gives the area of a cyclic quadrilateral in terms of its side lengths. Giugiuc, Oai and Altintas (2018) studied a sharp area inequality for convex quadrilaterals. Their proof includes exact upper bounds for a product of four numbers in \([0,2]\) with fixed sum and fixed quadratic moment, split at the same normalized threshold that corresponds here to \(q=4/3\). Applied to Brahmagupta's formula, that machinery controls the **maximum** area side of the fixed-variance problem and also yields the sharp left-hand inequality in (7).

The complementary question is the opposite one: at fixed perimeter and side variance, how small can the area of a cyclic quadrilateral be? The answer is not obtained from their product upper bound. The lower extremizer is a different \(1+3\) branch, and after \(q=4/3\) the lower envelope moves to the degenerate boundary and collapses to zero.

Quantitative polygonal isoperimetric results of Indrei--Nurbekyan (2015) and Indrei (2016) control several polygonal variances by the isoperimetric deficit, but do not give this exact cyclic lower profile or the sharp reverse constant in (5).

## Proof

### 1. Brahmagupta reduction

Let
\[
s=\frac P2=2\mu
\]
be the semiperimeter and put
\[
y_i=\frac{s-a_i}{\mu}=2-\frac{a_i}{\mu}.
\tag{8}
\]
For a nondegenerate convex quadrilateral, every side is smaller than the sum of the other three, so
\[
0<y_i<2.
\]
Moreover,
\[
\sum_i y_i=4,
\qquad
\sum_i(y_i-1)^2=q.
\tag{9}
\]
Because \(Q\) is cyclic, Brahmagupta's formula becomes
\[
K^2
=\prod_{i=1}^4(s-a_i)
=\mu^4\prod_{i=1}^4y_i.
\tag{10}
\]
Thus the lower-area problem is exactly the minimum-product problem for four variables in the open box \((0,2)^4\) under (9).

Conversely, any positive side vector satisfying the strict quadrilateral inequalities admits a convex cyclic realization, so the algebraic equality and limiting families below are geometrically realizable.

### 2. Exact minimum for \(0\le q<4/3\)

Inside the hyperplane \(\sum_i y_i=4\), the squared Euclidean distance from \((1,1,1,1)\) to any face \(y_i=0\) or \(y_i=2\) is \(4/3\). Hence for \(q<4/3\) the constraint sphere in (9) lies entirely inside the open box. The product therefore has an attained positive minimum.

At an interior critical point of \(\log(y_1y_2y_3y_4)\), Lagrange multipliers give
\[
\frac1{y_i}=\lambda+\nu y_i,
\tag{11}
\]
so every coordinate is a root of one quadratic. Therefore a critical point has at most two distinct coordinate values. Up to permutation, the only multiplicity types are \(1+3\) and \(2+2\).

Set
\[
r=\frac{\sqrt{3q}}2.
\]
The two \(1+3\) products are
\[
\Pi_+=(1+r)\left(1-\frac r3\right)^3,
\qquad
\Pi_-=(1-r)\left(1+\frac r3\right)^3,
\tag{12}
\]
and the \(2+2\) product is
\[
\Pi_{22}=
\left(1-\frac q4\right)^2
=\left(1-\frac{r^2}{3}\right)^2.
\tag{13}
\]
The exact differences are
\[
\Pi_+-\Pi_{22}
=\frac{4r^3(2-r)}{27},
\qquad
\Pi_{22}-\Pi_-
=\frac{4r^3(r+2)}{27}.
\tag{14}
\]
For \(0<r<1\), both are positive, so the minimum is \(\Pi_-\). Translating the corresponding \(y\)-coordinates through (8) gives precisely the side multiset (2). Equations (1) and (2) follow from (10).

### 3. Collapse of the lower envelope at \(q=4/3\)

Once \(q\ge4/3\), the constraint sphere meets the boundary \(y_i=0\), where the product vanishes. More explicitly, for
\[
u=\sqrt{6q-8}\in[0,4)
\]
the boundary point
\[
\left(
0,
\frac{4-u}{3},
\frac{8+u}{6},
\frac{8+u}{6}
\right)
\tag{15}
\]
has sum \(4\), lies in \([0,2]^4\), and satisfies
\[
\sum_i(y_i-1)^2=q.
\]
It is a limit of positive feasible points with the same two constraints. Hence the infimum of the product, and therefore of the cyclic area, is zero.

The condition \(y_1=0\) is \(a_1=s=P/2\), exactly the degenerate-quadrilateral boundary. At \(q=4/3\), (15) is \((0,4/3,4/3,4/3)\), which translates to side ratio \(3:1:1:1\). This proves (3)--(4).

### 4. Sharp reverse stability

For \(q<4/3\), use the exact lower envelope. Since \(q=4r^2/3\),
\[
1-\frac{3q}{4}=1-r^2.
\]
A direct factorization gives
\[
(1-r)\left(1+\frac r3\right)^3-(1-r^2)^2
=
\frac{4r^2(1-r)(7r+9)}{27}
\ge0.
\tag{16}
\]
Both sides being nonnegative,
\[
\sqrt{m(q)}\ge1-\frac{3q}{4}.
\]
By (1),
\[
K\ge\mu^2\left(1-\frac{3q}{4}\right)
=\frac{P^2}{16}-\frac34V.
\tag{17}
\]
This is exactly (5).

For \(q\ge4/3\), the right-hand side of (17) is nonpositive, so (17) remains true trivially because \(K>0\). Thus (5) holds on the full range \(0\le q<4\).

Along the lower-envelope equality family (2), let \(q\uparrow4/3\), equivalently \(r\uparrow1\). Then \(K\to0\) and \(V/P^2=q/16\to1/12\), so
\[
\frac{P^2-16K}{V}\longrightarrow12.
\]
No smaller universal constant can replace \(12\). This proves sharpness.

Finally, substituting \(V=\sum_i a_i^2-P^2/4\) into (5) gives (6).

## Reproducibility

The result is exact and symbolic. The lower envelope is certified by the critical-point classification (11) and the factorizations (14); the reverse inequality is reduced to the single factorization (16). The boundary family (15) can be checked by direct substitution.

## Literature comparison and originality boundary

Giugiuc--Oai--Altintas (2018) is the closest located prior result and materially limits the novelty claim. Their Theorem 1.1 gives a sharp convex-quadrilateral area inequality with square equality. Their Lemmas 1.2 and 1.3 solve the corresponding **maximum-product** problem under normalized first- and second-moment constraints, with a split at the same threshold. That prior work covers the upper-product side and, after algebraic rewriting, the left-hand inequality in (7). None of those statements is claimed as new here.

The present claim is the complementary **minimum-product/cyclic minimum-area** side: the exact lower envelope (1), its equality family (2), the zero-infimum transition (3)--(4), and the resulting sharp reverse deficit inequality (5). Targeted searches through September 2026 using combinations of cyclic quadrilateral, side variance, sum of squared sides, fixed perimeter, minimum area, reverse stability, Brahmagupta formula, and the equivalent form (6) did not locate these statements.

Indrei--Nurbekyan (2015) establishes polygonal isoperimetric stability with side and radius variances, while Indrei (2016) gives a different sharp quantitative polygonal deficit involving radius and barycentric-angle variances. These results are broader in polygon count but do not provide the exact fixed-second-moment cyclic minimum treated here.

Originality remains to the best of our knowledge. The proof becomes elementary after the Brahmagupta substitution, so an equivalent inequality may occur in older geometric-inequality collections or in abstract symmetric-polynomial literature under different notation. No located source provided concrete evidence of such coverage.

## Limitations

- Only nondegenerate convex cyclic Euclidean quadrilaterals are covered.
- For \(q\ge4/3\), the lower value is an infimum attained only on the degenerate boundary of the side-length cone.
- The lower envelope is not a lower bound for arbitrary flexible noncyclic quadrilaterals.
- The known upper-product/upper-area counterpart and the left-hand inequality in (7) are prior work and are not part of the novelty claim.
- Equivalent older symmetric-polynomial or geometric-inequality formulations remain a residual originality risk.

## References

1. Leonard Mihai Giugiuc, Dao Thanh Oai, and Kadir Altintas, “An inequality related to the lengths and area of a convex quadrilateral,” *International Journal of Geometry* 7 (2018), no. 1, 81–86. https://ijgeometry.com/product/leonard-m-giugiuc-dao-t-oai-and-kadir-altintas-an-inequality-related-to-the-lengths-and-area-of-a-convex-quadrilateral/
2. Carl Anton Bretschneider, “Untersuchung der trigonometrischen Relationen des geradlinigen Viereckes,” *Archiv der Mathematik und Physik* 2 (1842), 225–261.
3. Eisso J. Atzema, “From Brahmagupta to Euler: on the formula for the area of a cyclic quadrilateral,” *BSHM Bulletin* 30 (2015), 20–34. DOI: https://doi.org/10.1080/17498430.2014.942818
4. Emanuel Indrei and Levon Nurbekyan, “On the stability of the polygonal isoperimetric inequality,” *Advances in Mathematics* 276 (2015), 62–86. DOI: https://doi.org/10.1016/j.aim.2015.02.013
5. Emanuel Indrei, “A sharp lower bound on the polygonal isoperimetric deficit,” *Proceedings of the American Mathematical Society* 144 (2016), 3115–3122. DOI: https://doi.org/10.1090/proc/12947
