# Rigidity of separable inradius objectives for Delaunay triangulations

**Same-model review: passed. Independent audit: not yet performed.**

## Result

Let \(P\subset\mathbb R^2\) be a finite point set in general position (no three collinear and no four cocircular), and let \(T\) be a triangulation of \(P\). For a continuous function \(\varphi:(0,\infty)\to\mathbb R\), define the separable inradius functional
\[
F_\varphi(T)=\sum_{\Delta\in T}\varphi(r_\Delta),
\]
where \(r_\Delta\) is the inradius of the triangle \(\Delta\).

Then the following classification holds:

\[
\boxed{\text{The Delaunay triangulation maximizes }F_\varphi\text{ for every }P}
\]
if and only if
\[
\boxed{\varphi(t)=at+b\quad\text{for some }a\ge 0.}
\]
Likewise, the Delaunay triangulation minimizes \(F_\varphi\) for every such \(P\) if and only if \(\varphi(t)=at+b\) with \(a\le0\).

Thus Lambert's 1994 linear inradius criterion is rigid inside the whole class of continuous separable transforms of the inradius: apart from an additive constant and a nonnegative rescaling, there is no other universal Delaunay-maximized objective of the form \(\sum\varphi(r_\Delta)\).

### Cyclic rigidity

A related characterization strengthens the classical Japanese theorem. For a convex cyclic quadrilateral \(ABCD\), write
\[
r_{ABC},\ r_{ACD},\ r_{ABD},\ r_{BCD}
\]
for the four triangle inradii determined by its two diagonals. A continuous \(\varphi:(0,\infty)\to\mathbb R\) satisfies
\[
\varphi(r_{ABC})+\varphi(r_{ACD})
=
\varphi(r_{ABD})+\varphi(r_{BCD})
\tag{1}
\]
for every convex cyclic quadrilateral if and only if \(\varphi\) is affine.

### Power sums

For every \(p>0\), the functional
\[
\sum_{\Delta\in T} r_\Delta^p
\]
is universally maximized by the Delaunay triangulation if and only if \(p=1\). For every \(p\ne1\), counterexamples may be chosen arbitrarily close to a cyclic quadrilateral and with a unique Delaunay diagonal.

This is in sharp contrast with the circumradius criterion: known Delaunay optimality results allow arbitrary increasing transforms of the circumradius in the corresponding minimizing functional.

## Proof

### 1. Universal Delaunay extremality forces cyclic invariance

Assume first that the Delaunay triangulation maximizes \(F_\varphi\) for every finite planar point set in general position. Apply the assertion to a set consisting of the four vertices of a strictly convex noncyclic quadrilateral. There are only two triangulations, so the unique Delaunay diagonal must give at least as large a value of the two-triangle functional.

Now let \(ABCD\) be a convex cyclic quadrilateral. Perturb \(D\) slightly to one side of its circumcircle while preserving convexity. On one side, diagonal \(AC\) is uniquely Delaunay; on the other side, diagonal \(BD\) is uniquely Delaunay. The two corresponding inequalities have opposite directions. Letting the perturbation tend to zero and using continuity of triangle inradii and of \(\varphi\) gives the equality (1) on the original cyclic quadrilateral.

The same argument applies if universal Delaunay *minimization* is assumed: the two one-sided inequalities again collapse to equality on the cyclic limit.

### 2. A cyclic kite realizes every midpoint relation

Fix \(\lambda>0\) and \(0<\alpha<\pi/2\). Put
\[
A=(\lambda,0),\qquad C=(-\lambda,0),
\]
\[
B=\lambda(\cos2\alpha,\sin2\alpha),\qquad
D=\lambda(\cos2\alpha,-\sin2\alpha).
\]
These four points form a convex cyclic kite. Write \(s=\sin\alpha\) and \(c=\cos\alpha\).

The diagonal \(AC\) gives two congruent right triangles. Their common inradius is
\[
u=\lambda(s+c-1).
\tag{2}
\]
The two triangles produced by diagonal \(BD\) have inradii
\[
v=2\lambda c(1-c),\qquad
w=2\lambda s(1-s).
\tag{3}
\]
Since \(s^2+c^2=1\),
\[
v+w=2u.
\tag{4}
\]
Moreover, with
\[
\delta=s-c\in(-1,1),
\]
one has
\[
v=u(1+\delta),\qquad w=u(1-\delta).
\tag{5}
\]
As \(\alpha\) ranges over \((0,\pi/2)\), \(\delta\) ranges over all of \((-1,1)\); for each fixed \(\alpha\), scaling \(\lambda\) makes \(u\) arbitrary in \((0,\infty)\).

Applying (1) to this kite therefore yields
\[
\varphi((1+\delta)t)+\varphi((1-\delta)t)=2\varphi(t)
\tag{6}
\]
for every \(t>0\) and every \(-1<\delta<1\). Given arbitrary \(x,y>0\), choose
\[
t=\frac{x+y}{2},\qquad \delta=\frac{x-y}{x+y}.
\]
Then (6) becomes the midpoint Jensen equation
\[
\varphi(x)+\varphi(y)=2\varphi\!\left(\frac{x+y}{2}\right).
\]
Continuity implies
\[
\varphi(t)=at+b.
\tag{7}
\]
This proves both the cyclic-rigidity statement and the necessity of affinity for universal Delaunay extremality.

### 3. The slope has the required sign

It remains to determine the sign of \(a\). Consider the convex quadrilateral
\[
A=(-1,0),\quad B=(0,1),\quad C=(1,0),\quad D=(0,-2).
\]
The circumcircle of \(ABC\) is the unit circle and \(D\) lies outside it, so \(AC\) is the unique Delaunay diagonal.

The sum of the two inradii for diagonal \(AC\) is
\[
S_{AC}=(\sqrt2-1)+\frac{\sqrt5-1}{2},
\]
while the two triangles for diagonal \(BD\) are congruent and give
\[
S_{BD}=\frac{6}{3+\sqrt2+\sqrt5}.
\]
Their difference is
\[
S_{AC}-S_{BD}
=
\frac{3(\sqrt2+\sqrt{10}-4)}{2(3+\sqrt2+\sqrt5)}>0.
\tag{8}
\]
For an affine \(\varphi(t)=at+b\), the constant term contributes the same amount to both triangulations, so (8) forces \(a\ge0\) under universal maximization and \(a\le0\) under universal minimization.

### 4. Converse

All triangulations of a fixed planar point set have the same number of triangles, so the additive term \(b\) contributes the same constant to every triangulation. Lambert proved that the Delaunay triangulation maximizes the arithmetic mean, equivalently the sum, of the triangle inradii. Therefore every \(\varphi(t)=at+b\) with \(a\ge0\) is universally Delaunay-maximized, and every such affine function with \(a\le0\) is universally Delaunay-minimized.

## Explicit power counterexamples

Take the cyclic kite above with \(\lambda=1\) and \(\alpha=\pi/6\). Then
\[
u=\frac{\sqrt3-1}{2},\qquad
v=\frac{2\sqrt3-3}{2},\qquad
w=\frac12,
\]
with \(v+w=2u\) and \(v\ne w\).

If \(p>1\), strict convexity gives
\[
v^p+w^p>2u^p.
\]
Move \(D\) an arbitrarily small distance radially outward. Then \(AC\) becomes the unique Delaunay diagonal, while by continuity the \(BD\) triangulation still has the larger \(p\)-power sum. Hence the Delaunay triangulation fails to maximize \(\sum r^p\).

If \(0<p<1\), strict concavity reverses the cyclic inequality. Moving \(D\) an arbitrarily small distance radially inward makes \(BD\) uniquely Delaunay, while the \(AC\) triangulation retains the larger \(p\)-power sum. This proves the power-sum statement.

## Relation to prior work

The classical Japanese theorem says that for a cyclic polygon the sum of the inradii of the triangles is independent of the triangulation. Its converse is also classical: triangulation-independent inradius sum characterizes cyclicity. Lambert's 1994 result proves that among all triangulations of a planar point set, the Delaunay triangulation maximizes the arithmetic mean (equivalently, because the triangle count is fixed, the sum) of the inradii.

Minculete, Barbu and Szöllősy (2012) derived additional nonlinear identities for the four inradii of a cyclic quadrilateral. Their relations include reciprocal and squared inradii, but with factors involving the two diagonal lengths; they do not give unweighted separable invariance of the form (1).

Klyachin and Grigorieva (2017) developed sufficient conditions for simplex functionals minimized by generalized \(\Phi\)-triangulations. In the ordinary Delaunay case they obtain, in particular, minimization of \(\sum \mu(R_\Delta)\) for arbitrary increasing \(\mu\), where \(R_\Delta\) is circumradius. This makes the inradius rigidity above structurally different: continuous unweighted separable transforms of inradius collapse to the affine family.

Dolbilin, Edelsbrunner and Musin (2012), and subsequent work on functionals over Delaunay sets, address how finite-set optimality of a functional transfers to density optimality for infinite Delaunay sets. They do not provide the separable-inradius classification above.

Searches under combinations of “Delaunay inradius functional”, “convex function of inradius”, “sum of powers of inradii”, “Japanese theorem functional equation”, and synonymous separable-objective language did not locate the affine-rigidity theorem, the cyclic functional classification, or the power-sum counterexamples. The originality claim is therefore only to the best of our knowledge.

## Limitations

- The classification assumes \(\varphi\) is continuous. Standard weaker regularity assumptions for the midpoint Jensen equation could replace continuity, but no maximal regularity statement is claimed.
- The result is for ordinary Euclidean planar triangulations of finite point sets. No claim is made for constrained or weighted Delaunay triangulations, surface Delaunay triangulations, or higher dimensions.
- The full text of Lambert's 1994 proceedings paper was not directly inspectable in this check. Its abstract, proceedings entry, later computational-geometry references, and later summaries were inspected; they state the linear arithmetic-mean/sum criterion. Because Lambert is the closest source and apparently also discusses the converse Japanese theorem, it remains the main residual originality risk.
- Equivalent folklore in classical Japanese-theorem or mesh-quality literature remains possible because the rigidity proof is short once the cyclic kite is identified.

## Reproducibility

The coordinate calculation in the cyclic-kite proof and two near-cyclic power examples can be checked with `artifacts/verify_kite.py`. The proof itself is symbolic and does not depend on numerical computation.

## References

1. R. A. Johnson, *Modern Geometry: An Elementary Treatise on the Geometry of the Triangle and the Circle*, 1929, p. 193. Modern reference summary: https://mathworld.wolfram.com/JapaneseTheorem.html
2. T. Lambert, *The Delaunay Triangulation Maximizes the Mean Inradius*, Proceedings of the Sixth Canadian Conference on Computational Geometry, 1994, pp. 201–206. Bibliographic record: https://dblp.org/rec/conf/cccg/Lambert94
3. N. Minculete, C. Barbu, G. Szöllősy, *About the Japanese Theorem*, Crux Mathematicorum 38(5) (2012), 188–193. https://cms.math.ca/wp-content/uploads/crux-pdfs/CRUXv38n5.pdf
4. V. A. Klyachin, E. G. Grigorieva, *Description of functionals that are minimized by Φ-triangulations*, Itogi Nauki i Tekhniki. Sovrem. Mat. Pril. Temat. Obz. 139 (2017), 9–14. https://www.mathnet.ru/eng/into220
5. N. P. Dolbilin, H. Edelsbrunner, O. R. Musin, *On the Optimality of Functionals over Triangulations of Delaunay Sets*, Russian Mathematical Surveys 67(4) (2012), 781–783. https://arxiv.org/abs/1209.3541
