# Two-point central-section law and sharp aspect-ratio transitions for square antiprisms

## Finding

Let \(h>0\) and let \(K_h\) be the right square antiprism with equatorial circumradius one, whose two square bases have heights \(+h\) and \(-h\) and relative azimuthal rotation \(\pi/4\). Choose an unoriented plane \(E\) through the origin according to normalized rotation-invariant measure on the Grassmannian of two-planes in \(\mathbb R^3\), and let \(N_h\) be the number of vertices of the polygon \(K_h\cap E\).

**Theorem.** For every \(h>0\), almost surely \(N_h\in\{6,8\}\), and both possibilities have positive probability. Set \(p_8(h)=\Pr(N_h=8)\). Its exact law is

\[
 p_8(h)=1-\frac8\pi\left[\arcsin\left(\frac{\cos(\pi/8)}{\sqrt{1+h^2}}\right)-\arcsin\left(\frac{1}{\sqrt{2(1+h^2)}}\right)\right].
\]

Equivalently,

\[
 p_8(h)=\frac4\pi\left[\arccos\left(\frac{h^2}{1+h^2}\right)+\arccos\left(\frac{1/\sqrt2-h^2}{1+h^2}\right)\right]-3.
\]

The complementary hexagon probability is \(p_6(h)=1-p_8(h)\). The function \(p_8\) is strictly increasing from zero to one as \(h\) runs from zero to infinity. More precisely,

\[
 p_8(h)=\frac{4\sqrt2}{\pi}h^2+O(h^4)\quad(h\downarrow0),
 \qquad
 p_6(h)=\frac8{\pi h}\left(\cos\frac\pi8-\frac1{\sqrt2}\right)+O(h^{-3})\quad(h\to\infty).
\]

For the *regular*, equal-edge square antiprism, the half-height is \(h=2^{-3/4}\). Its octagonal-section probability is

\[
 \boxed{p_8(2^{-3/4})=\frac8\pi\arccos\left(\frac{2\sqrt2-1}{7}\right)-3
 =0.32704409713846822257\ldots.}
\]

Thus the regular square antiprism has hexagonal central sections with probability \(0.67295590286153177743\ldots\). The two-point support is a geometric rigidity statement: central sections of the non-centrally symmetric square antiprism have neither four, five, seven, nine, nor ten sides in generic orientation, although its boundary has ten faces.

## Assumptions and scope

The eight vertices are

\[
 T_k=(\cos(k\pi/2),\sin(k\pi/2),h),\qquad
 B_k=(\cos(\pi/4+k\pi/2),\sin(\pi/4+k\pi/2),-h),\qquad k=0,1,2,3.
\]

The sixteen edges consist of the four top-square edges \(T_kT_{k+1}\), four bottom-square edges \(B_kB_{k+1}\), and eight oblique edges \(T_kB_k\) and \(T_kB_{k-1}\), where subscripts are interpreted modulo four. There are eight triangular lateral faces and two square bases. Positive \(h\) ensures a three-dimensional convex antiprism. A random plane has normal \(U\) Haar-uniform on the unit sphere, with \(U\) and \(-U\) representing the same unoriented plane. Exceptional normals perpendicular to one of the eight position vectors have spherical measure zero; all statements about section vertex counts are almost-sure statements off this explicitly excluded set.

No translated slicing planes, nonuniform orientations, unequal bases, or nonstandard azimuthal twists are included.

## Proof

**1. Every generic section vertex comes from one sign-changing edge.** For a full-dimensional convex polytope, a plane through an interior point that meets no polytope vertex cuts an edge precisely when its endpoints lie on opposite sides. The edge intersects the plane transversely, and the intersection lies at a genuine corner of the section. Conversely every section corner arises from such an original edge. Consequently, if \(s(V)=\operatorname{sign}(U\cdot V)\), then

\[
 N_h=\sum_{\{V,W\}\text{ an edge of }K_h}\boldsymbol1_{s(V)\ne s(W)}.
\]

The origin is interior because it lies strictly between the centers of two full-dimensional square bases.

**2. Reduce the normal sphere to one fundamental wedge.** Replacing \(U\) by \(-U\) does not change the section, so choose \(U_z\ge0\). Rotations through integer multiples of \(\pi/2\) and reflections in vertical symmetry planes preserve the body; they reduce the azimuth to \(0\le\phi\le\pi/4\). Write \(\rho=\sqrt{U_x^2+U_y^2}\), \(c=hU_z/\rho\), \(C=\cos\phi\), \(S=\sin\phi\), \(D=(C-S)/\sqrt2=\cos(\phi+\pi/4)\), and \(F=(C+S)/\sqrt2\). The eight vertex-dot-product signs, in top-then-bottom cyclic order, are exactly the signs of

\[
 (c+C,\ c+S,\ c-C,\ c-S;\ F-c,\ -D-c,\ -F-c,\ D-c).
\]

For \(0<\phi<\pi/8\), the four positive thresholds satisfy \(S<D<F<C\); for \(\pi/8<\phi<\pi/4\), they satisfy \(D<S<C<F\). Directly counting sign-changing edges in the sixteen edges listed above gives this complete table (each row is an open interval, and equality cases are null):

| Azimuth | Ascending intervals for \(c\) | Section side counts, respectively |
|---|---|---|
| \(0<\phi<\pi/8\) | \((0,S),(S,D),(D,F),(F,C),(C,\infty)\) | \(6,6,8,8,8\) |
| \(\pi/8<\phi<\pi/4\) | \((0,D),(D,S),(S,C),(C,F),(F,\infty)\) | \(6,6,8,8,8\) |

This yields the exact orientation criterion

\[
 N_h=8\quad\Longleftrightarrow\quad c>\max\{\sin\phi,\cos(\phi+\pi/4)\}
\]

and \(N_h=6\) otherwise. Both events have positive spherical measure for every \(h>0\): choose \(c\) respectively sufficiently large or sufficiently small in any interior azimuth wedge.

**3. Integrate the spherical orientation probability.** On the upper unit hemisphere, \(Z=U_z\) is uniform on \([0,1]\) and independent of the uniform azimuth. For each nonnegative threshold \(t\),

\[
 \Pr(c>t\mid\phi)=\Pr\left(Z>\frac{t}{\sqrt{h^2+t^2}}\right)=1-\frac{t}{\sqrt{h^2+t^2}}.
\]

The fundamental azimuth wedge has length \(\pi/4\). Because \(D>S\) for \(\phi<\pi/8\), and \(S>D\) for \(\phi>\pi/8\),

\[
 p_8(h)=1-\frac4\pi\left[\int_0^{\pi/8}\frac{\cos(\phi+\pi/4)}{\sqrt{h^2+\cos^2(\phi+\pi/4)}}\,d\phi
 +\int_{\pi/8}^{\pi/4}\frac{\sin\phi}{\sqrt{h^2+\sin^2\phi}}\,d\phi\right].
\]

Each integral equals

\[
 \arcsin\frac{\cos(\pi/8)}{\sqrt{1+h^2}}-\arcsin\frac{1}{\sqrt{2(1+h^2)}}.
\]

This proves the first exact formula and normalization.

**4. Independent edge-angle expression.** For fixed nonzero vectors \(v,w\), a Haar-uniform plane normal places them in opposite open halfspaces with probability \(\arccos(v\cdot w/(|v||w|))/\pi\). All eight horizontal antiprism edges have endpoint angle

\[
 \alpha(h)=\arccos\frac{h^2}{1+h^2},
\]

and all eight lateral edges have endpoint angle

\[
 \beta(h)=\arccos\frac{1/\sqrt2-h^2}{1+h^2}.
\]

Linearity of expectation, followed by the proved \(N_h=6+2\boldsymbol1_{N_h=8}\), yields \(6+2p_8(h)=8(\alpha(h)+\beta(h))/\pi\). This gives the equivalent formula without relying on the spherical integral calculation.

**5. Monotonicity, endpoint exponents, and the regular case.** For each interior azimuth, the conditional octagon probability \(1-t/\sqrt{h^2+t^2}\) is strictly increasing in \(h>0\), as the threshold \(t\) is positive except at a zero-measure boundary. Dominated convergence gives the endpoints zero and one. Expanding \(\alpha(h)\) and \(\beta(h)\) at \(h=0\) gives \(\alpha=\pi/2-h^2+O(h^4)\) and \(\beta=\pi/4+(1+\sqrt2)h^2+O(h^4)\); the quadratic constant follows. Expanding the two inverse sines at argument zero gives the inverse-height constant and \(O(h^{-3})\) remainder.

The base-square edges have squared length \(2\), while each lateral edge has squared length \(2-\sqrt2+4h^2\). Equating them gives \(h^2=1/(2\sqrt2)\). Then both \(\alpha\) and \(\beta\) equal \(\arccos((2\sqrt2-1)/7)\); substitution proves the equal-edge formula.

## Verification

The included standalone `verify.py` uses only Python's standard library. Running `python verify.py` checks the true sixteen-edge hull structure independently through supporting planes, constructs planar intersection polygons through an independent two-dimensional convex-hull algorithm for 3,600 sampled normals, compares independent edge-angle and spherical-integration formulas at seven positive heights, checks the regular-solid constant and endpoint asymptotics, and performs 420,000 total seeded Haar-orientation trials at three heights. All checks succeeded. The exhaustive proof of the two-point support is the symbolic threshold table above, not the finite samples. Numerical comparisons are corroborative and not proofs for the continuum of normals or heights.

## Relationship to prior work

Lonke, *On random sections of the cube* (arXiv:math/9812123v1, submitted 21 December 1998), studies the expected face counts of Haar-random central sections of a cube, including higher-dimensional cases. Its full text gives no square-antiprism section distribution. Grünbaum, *Are prisms and antiprisms really boring? (Part 2)* (Geombinatorics 14, 2004, 10–17), develops structural definitions and combinatorial facts for antiprisms, including the traditional regular configuration and isosceles lateral variants; no central-section probability or aspect-ratio distribution appears in that inspected paper. Both sources supply a natural geometric-probability and antiprism context but neither statement implies the present two-point support classification or the all-height law.

Broadie, *A theorem about antiprisms* (Linear Algebra and Its Applications 66, 1985, 99–111), addresses conditions for antiprism realizability under polarity; the accessible abstract does not state a random-section law. Aravind, *Two families of antiprisms* (The Mathematical Gazette 80, 1996, 462–465), examines geometric families of antiprisms; a complete accessible version was not established. Those scope comparisons are limited by the material available. Previously indexed exact central-section distributions of cubes, orthotopes, icosahedra, truncated polyhedra, and polygonal prisms concern different solids or different invariants; a distribution for the square antiprism is not a corollary of their individual formulas merely because the number of possible polygon types is small.

## Limitations

The model requires congruent square bases in antiprismatic relative position and a common axial half-height \(h>0\), with a uniformly oriented central plane. The proof says nothing about other twists, offset bases, translated planes, section area, section perimeter, or antiprisms with more than four vertices in each base. The computational verification is finite, and historical priority is provisional: failure to locate a matching published formula is not proof of novelty, and some older geometric literature is not fully accessible. The proof is supplied in full, but independent mathematical validation and absolute historical-priority certification have not been performed.

## References

1. Y. Lonke, *On random sections of the cube*, arXiv:math/9812123v1 (first public version: 1998-12-21), https://arxiv.org/html/math/9812123v1.
2. B. Grünbaum, *Are prisms and antiprisms really boring? (Part 2)*, Geombinatorics **14** (2004), 10–17, https://faculty.washington.edu/moishe/branko/BG254.Prisms%20and%20antiprisms.%20Part%202.pdf.
3. M. N. Broadie, *A theorem about antiprisms*, Linear Algebra and Its Applications **66** (1985), 99–111, doi:10.1016/0024-3795(85)90127-2.
4. P. K. Aravind, *Two families of antiprisms*, The Mathematical Gazette **80** (1996), 462–465, doi:10.2307/3618508.
