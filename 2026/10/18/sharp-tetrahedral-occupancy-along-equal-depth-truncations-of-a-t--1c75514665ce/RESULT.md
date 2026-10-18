# Sharp tetrahedral occupancy along equal-depth truncations of a tetrahedron

## Finding

Let \(\Delta=\operatorname{conv}\{v_0,v_1,v_2,v_3\}\subset\mathbb R^3\) be any nondegenerate tetrahedron. For \(0\le t\le 1/2\), cut all four vertices at the same affine fraction of the incident edges, retaining the convex polytope
\[
P_t=\operatorname{conv}\{(1-t)v_i+t v_j:0\le i,j\le3,\ i\ne j\}.
\]
If \(M(P_t)\) is the maximum volume of **any** tetrahedron contained in \(P_t\), then
\[
\boxed{\frac{M(P_t)}{\operatorname{vol}_3(\Delta)}=(1-t)(1-3t+3t^2),\qquad
\frac{M(P_t)}{\operatorname{vol}_3(P_t)}=\frac{(1-t)(1-3t+3t^2)}{1-4t^3}.}
\]
The occupancy fraction is strictly decreasing and then strictly increasing: its unique minimum over \([0,1/2]\) occurs at the unique \(\tau\in(0,1/2)\) satisfying
\[
24\tau^4-32\tau^3+3\tau^2+12\tau-4=0.
\]
Numerically, \(\tau\approx0.432030293634991\), with sharp minimal occupancy \(\approx0.221219566210031\). In particular, the regular Archimedean truncated tetrahedron, obtained when \(t=1/3\) and \(\Delta\) is regular, has occupancy \(6/23\); its rectified-octahedron endpoint at \(t=1/2\) has occupancy \(1/4\).

For each interior \(0<t<1/2\), precisely \(24\) unordered quadruples of the \(12\) polytope vertices attain the sharp tetrahedral volume. This is a vertex-supported count, **not** a classification of all possibly nonvertex-supported maximizers.

## Assumptions and scope

The tetrahedron \(\Delta\) is arbitrary and nondegenerate; its Euclidean shape is immaterial, because both the numerator and denominator transform by the same affine volume factor. The truncation fraction \(t\) is measured from each original tetrahedron vertex toward adjacent vertices, simultaneously on all six edges. The range \(0\le t\le1/2\) goes continuously from the untruncated tetrahedron to the edge-midpoint octahedron. At either endpoint, nominally distinct directed-edge points can coincide; the \(24\)-quadruple count is asserted only for the open interval.

No condition is placed on the locations of the four vertices of the optimized contained tetrahedron: they may lie anywhere within the solid. The formula does not extend by assertion to independently chosen truncation fractions or to dimensions other than three.

## Proof

**1. Affine reduction and volume of the truncated body.** An invertible affine map sends \((v_0,v_1,v_2,v_3)\) to \((0,e_1,e_2,e_3)\). Thus the vertices to consider are the \(12\) directed-edge points
\[
w_{ij}(t)=(1-t)v_i+t v_j,\qquad i\ne j.
\]
For \(0\le t\le1/2\), the removed pieces are four interior-disjoint corner tetrahedra, each homothetic to \(\Delta\) by factor \(t\). Consequently
\[
\operatorname{vol}_3(P_t)=(1-4t^3)\operatorname{vol}_3(\Delta).
\]
The inclusion and equality of the stated vertex and halfspace constructions follow from the barycentric constraints \(0\le\lambda_i\le1-t\) and \(\sum_i\lambda_i=1\): their three-dimensional extreme points have exactly two nonzero coordinates, \(1-t\) and \(t\), except for the indicated endpoint identifications.

**2. Exact exhaustive determinant bound.** For any four chosen points \(a,b,c,d\) of the polytope, their normalized tetrahedral volume is \(|\det(b-a,c-a,d-a)|\), measured relative to the normalized simplex \((0,e_1,e_2,e_3)\). The signed determinant is affine in each of its four vector arguments; fixing three arguments, the maximum of its absolute value on \(P_t\) occurs at a vertex. Repeating for all arguments reduces the unrestricted maximum exactly to \(\binom{12}{4}=495\) unordered quadruples of directed-edge vertices.

The following exhaustive exact polynomial census lists each possible absolute normalized determinant \(Q(t)\) together with its number of unordered quadruples (the forms can coincide numerically at isolated truncation fractions):

| \(Q(t)\) | Multiplicity |
|---|---:|
| \(0\) | 78 |
| \(t^2(1-2t)\) | 48 |
| \(t^2(1-t)\) | 72 |
| \(t(1-t)(1-2t)\) | 120 |
| \(t(1-t)^2\) | 72 |
| \(t(3t^2-3t+1)\) | 24 |
| \((1-t)^2(1-2t)\) | 48 |
| \((1-2t)^2\) | 3 |
| \((1-t)(3t^2-3t+1)\) | 24 |
| \((1-2t)(2t^2-2t+1)\) | 6 |

These multiplicities sum to \(495\). This enumeration is a finite proof step: `verify.py` constructs all \(12\) vertices as degree-one integer polynomials, expands **every** four-point determinant by exact polynomial arithmetic, and checks the ten forms and multiplicities, with no randomness or symbolic-algebra dependencies. A signed nonzero determinant has no sign reversal on \(0<t<1/2\), because all nine nonzero forms displayed have positive factors there.

Write \(D(t)=(1-t)(3t^2-3t+1)\) for the proposed maximum. Direct polynomial subtraction shows \(D(t)-Q(t)>0\) for \(0<t<1/2\) for every other listed form. In the table order, omitting \(Q=0\) and \(Q=D\), the eight relevant differences are
\[
\begin{aligned}
& (1-2t)^2+t^2(1-t), && (1-t)^2(1-2t),\\
& (1-t)(5t^2-4t+1), && (1-t)(1-2t)^2,\\
& (1-2t)(3t^2-3t+1), && t^2(1-t),\\
& t^2(2-3t), && t^3.
\end{aligned}
\]
All are strictly positive: \(5t^2-4t+1=5(t-2/5)^2+1/5\), \(3t^2-3t+1>0\), and every remaining factor is positive on the open interval. The zero form has gap \(D(t)>0\) as well. The endpoints follow by direct substitution and continuity.

**3. Sharp witness.** In normalized coordinates the four feasible directed-edge vertices
\[
(t,0,0),\quad(1-t,t,0),\quad(0,1-t,0),\quad(0,0,1-t)
\]
have absolute determinant exactly \(D(t)=(1-t)(1-3t+3t^2)\). Thus the upper bound is attained throughout the full parameter interval. The census identifies \(24\) vertex quadruples with that polynomial on the open interval, with all other classes strictly smaller.

**4. The unique minimum.** The unnormalized maximum itself decreases strictly, since \(D'(t)=-(2-3t)^2<0\) throughout this interval. Differentiating the exact occupancy ratio gives
\[
\frac{d}{dt}\frac{D(t)}{1-4t^3}
=\frac{F(t)}{(1-4t^3)^2},\qquad
F(t)=24t^4-32t^3+3t^2+12t-4.
\]
On \(0<t\le1/2\),
\[
F'(t)=12+6t-96t^2(1-t)>0,
\]
since \(t^2(1-t)\le1/8\) there. Since \(F(0)=-4\) and \(F(1/2)=1/4\), there is exactly one critical point, a strict global minimum, as stated. The denominator is strictly positive on \([0,1/2]\). The special values \(6/23\) and \(1/4\) follow by exact substitution. In particular, \(R(2/5)=7/31<1/4\), giving a simple rational witness that the interior occupancy fraction falls below the octahedral endpoint.

## Verification

Run `python3 verify.py` with Python 3. The standalone certificate uses integer-coefficient polynomial operations and `fractions.Fraction`; it enumerates each of the \(495\) four-point subsets once, checks the exact ten-class symbolic histogram, counts the \(24\) interior vertex-supported maximizers, verifies rational special values and the derivative polynomial, and encloses the unique positive root with rational bisection. Its expected output begins with `VERIFY_OK vertex_sets=495 distinct_symbolic_volume_forms=10`.

The exhaustive finite step is logically sufficient only in combination with the multilinear vertex reduction and the displayed positive gap factorizations. Rational bisection supplies a numerical approximation, not the proof of uniqueness of the root.

## Relationship to prior work

Jiao and Torquato [1] study dense *packings* of the regular truncated tetrahedron (the equal-edge case \(t=1/3\)). The present internal approximation quantity asks instead for the *largest single tetrahedron contained within one truncated body*, over a continuous affine truncation parameter. Packing density is not an upper bound or formula for that optimization problem.

Di Summa, Eisenbrand, Faenza, and Moldenhauer [2] treat maximum-volume simplices in finitely generated polytopes, including approximation algorithms and computational hardness. Their generic vertex/determinant viewpoint motivates a finite reduction but provides neither the ten determinant classes nor this family-specific sharp occupancy and quartic minimum.

Beck [3] studies expected volumes of *random* inscribed simplices; these moments are mathematically different from an attained maximum and cannot determine the present sharp profile. The complete text of [3] was not available for comparison, so it is not used as whole-document evidence of noncoverage.

## Limitations

The maximum-volume formula and unique occupancy minimum are proved for exactly the one-parameter equal-depth affine truncation of a tetrahedron. The listed \(24\) optimizers count **vertex-supported** tetrahedra, not the entire equality set of continuously varying contained tetrahedra. The theorem does not address asymmetric truncations, higher-dimensional truncated simplices, or packings of multiple solids. The literature comparison supports a new explicit formulation relative to the inspected works, but does not certify historical priority against all possible sources.

## References

1. Y. Jiao and S. Torquato, *Analytical Construction of A Dense Packing of Truncated Tetrahedra*, arXiv:1107.2300, first submitted 2011-07-12, revised title *A Packing of Truncated Tetrahedra that Nearly Fills All of Space*, https://arxiv.org/abs/1107.2300 .
2. M. Di Summa, F. Eisenbrand, Y. Faenza, and C. Moldenhauer, *On largest volume simplices and sub-determinants*, arXiv:1406.3512, first submitted 2014-06-13, https://arxiv.org/abs/1406.3512 .
3. D. Beck, *On Random Simplex Picking Beyond the Blashke Problem*, arXiv:2412.07952, first submitted 2024-12-10, https://arxiv.org/abs/2412.07952 .
