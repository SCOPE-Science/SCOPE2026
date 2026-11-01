# Exact recursive self-volume of the regular four-cross-polytope

## Finding

The centered four-dimensional cross-polytope
\[
B=\{x\in\mathbb R^4:\ |x_1|+|x_2|+|x_3|+|x_4|\le 1\}
\]
has **recursive self-volume** (in the sense of Wolansky's 2026 boundary-section definition)
\[
\boxed{\mathcal W_4(B)=\frac{128}{15}.}
\]
Its polar is the four-cube \(B^\circ=[-1,1]^4\), which has recursive self-volume \(16\). Hence for this polar pair the exact ratio is
\[
\boxed{\frac{\mathcal W_4(B)}{\mathcal W_4(B^\circ)}=\frac8{15}\ne1.}
\]
The essential intermediate invariant is the three-dimensional **cuboctahedral** central section \(C=B\cap\{x_1+x_2+x_3+x_4=0\}\), for which the calculation below gives \(\mathcal W_3(C)=16/3\). These evaluations are of the *new recursive functional*, not ordinary Euclidean volume or the classical intrinsic volumes.

## Assumptions and scope

For any origin-symmetric convex polytope \(K\) of intrinsic dimension \(d\), use the Euclidean measure intrinsic to its affine span. Define \(\mathcal W_1(I)=2\) for a centered interval. In dimension \(d\ge2\), with \(\mathscr F(K)\) the set of facets and \(u_F\) a Euclidean unit normal of facet \(F\), set
\[
\mathcal W_d(K)=\frac1d\sum_{F\in\mathscr F(K)}
\frac{\mathcal H^{d-1}(F)}
{\mathcal H^{d-1}(K\cap u_F^\perp)}
\mathcal W_{d-1}(K\cap u_F^\perp).
\tag{1}
\]
This is precisely the facet form of the boundary-section recurrence (Wolansky, Section 4, equation (5)), evaluated at the origin. Every section below has positive intrinsic volume; the formula is not applied to degenerate sections. All volumes, normals, and areas are Euclidean, prior to taking the dimensionless ratios in (1).

## Proof

**Planar base cases.** A centered parallelogram has \(\mathcal W_2=4\). Indeed, after an invertible linear change of coordinates it is a square, and each of its four directed boundary edges has Minkowski length \(2\); its self-perimeter is \(8\), half of which is the planar self-volume. An affine-regular hexagon has \(\mathcal W_2=3\): the six boundary-edge displacement vectors lie on the boundary of its unit hexagonal norm ball (after common scaling), so each has Minkowski length \(1\); its self-perimeter is \(6\). These statements can also be checked directly from (1) with \(\mathcal W_1=2\).

**Cuboctahedron as a canonical section.** Let \(e_1,\ldots,e_4\) be the coordinate basis and let
\[
E=\left\{x\in\mathbb R^4:\sum_{i=1}^4x_i=0\right\},\qquad
C=B\cap E=\operatorname{conv}\left\{\frac{e_i-e_j}{2}:i\ne j\right\}.
\]
The twelve displayed vertices are precisely the intersections of \(E\) with the sign-changing edges of \(B\). They make \(C\) a regular cuboctahedron in the Euclidean three-space \(E\).

It has eight equilateral triangular facets, given by \(x_i=\pm\tfrac12\), and six square facets, given by \(x_i+x_j=\tfrac12\) with unordered \(\{i,j\}\). Direct Euclidean geometry of their displayed vertices gives:

| Facet orbit | Number | Facet area | Distance from origin | Orthogonal central section | Section area | Section \(\mathcal W_2\) |
| --- | ---: | ---: | ---: | --- | ---: | ---: |
| Triangles | 8 | \(\sqrt3/8\) | \(1/\sqrt3\) | Regular hexagon | \(3\sqrt3/4\) | \(3\) |
| Squares | 6 | \(1/2\) | \(1/2\) | Square | \(1\) | \(4\) |

For a triangular facet normal, its central plane inside \(E\) is \(x_i=0\); its six vertices are \(\pm(e_j-e_k)/2\) for distinct \(j,k\ne i\), forming the claimed regular hexagon. For a square facet normal, the central plane is \(x_i+x_j=0\) (and therefore the complementary pair also sums to zero), whose vertices are \(\pm(e_i-e_j)/2\) and \(\pm(e_k-e_l)/2\), giving a square with perpendicular diagonals of length \(\sqrt2\). The facet areas and distances follow from the same coordinates: a triangle has side length \(1/\sqrt2\), and a square also has side length \(1/\sqrt2\).

The ordinary three-volume is recovered independently by pyramids from the origin:
\[
\operatorname{vol}_3(C)
=\frac13\left(8\frac{\sqrt3}{8}\frac1{\sqrt3}
+6\frac12\frac12\right)=\frac56.
\]
Applying recurrence (1) to its two facet orbits yields the exact non-Euclidean recursive invariant
\[
\mathcal W_3(C)=\frac13\left(
8\frac{\sqrt3}{8}\frac{3}{3\sqrt3/4}
+6\frac12\frac4{1}\right)
=\frac13(4+12)=\boxed{\frac{16}{3}}.
\tag{2}
\]

**The four-dimensional step.** The regular four-cross-polytope \(B\) has sixteen congruent tetrahedral facets, one for each sign pattern. The facet \(\operatorname{conv}\{e_1,e_2,e_3,e_4\}\) has ordinary three-volume \(1/3\), obtained by dividing the square root of the Gram determinant of its three edge differences by \(3!\). Its unit normal is \((1,1,1,1)/2\), so its orthogonal central section is exactly \(C\). Signed coordinate reflections identify the section and the facet area for every other facet. Thus (1) and (2) give
\[
\mathcal W_4(B)
=\frac14\cdot16\cdot\frac13\cdot
\frac{16/3}{5/6}
=\boxed{\frac{128}{15}}.
\]
Finally, for the polar cube \([-1,1]^4\), all eight facets are Euclidean three-cubes parallel to a central congruent three-cube; the ratio of their ordinary three-volumes is one. Repeated application of (1) starting from \(\mathcal W_1=2\) gives \(\mathcal W_d([-1,1]^d)=2^d\). Therefore \(\mathcal W_4(B^\circ)=16\), proving the stated exact polar ratio \(8/15\).

## Verification

The accompanying standalone `verify.py` constructs both polytopes directly from their Euclidean vertices, groups the fourteen three-dimensional facets of \(C\), computes facet areas and orthogonal central-section polygons, evaluates planar Minkowski perimeters from polygon half-space inequalities, checks \(\operatorname{vol}_3(C)=5/6\), and independently forms the four-dimensional recursion from all sixteen tetrahedral facets. The program checks the two exact targets \(16/3\) and \(128/15\) numerically to strict tolerances. Run it as `python verify.py` with NumPy and SciPy installed. This is numerical corroboration, not a proof for an infinite class; the proof above is exact and finite by symmetry.

## Relationship to prior work

Wolansky (2026, arXiv:2604.01950, first publicly submitted April 2, 2026) defines the recursive functional and calculates cube and Euclidean-ball examples; his Section 4 gives its facet-normal integration. His paper's general prose mentions polar duality. The exact cross-polytope calculation here is not present in the inspected source, and its distinct value from the polar cube demonstrates that the *stated recurrence itself* cannot satisfy a universal equality \(\mathcal W_d(K)=\mathcal W_d(K^\circ)\) in four dimensions. This mathematical comparison uses the recursive definition directly; it is not an assertion about unrelated volume conventions.

Classical planar self-circumference results, including those surveyed by Ghandehari and Martini (2019), supply the known hexagon/parallelogram base values. Geometric records on cube–cross-polytope intersections concern Mahler products, regular-section laws, and other functionals, not the recursive self-volume in (1). No identical published evaluation was identified in the searched records; that failure to find one is not a proof of priority.

## Limitations

The conclusion is an exact evaluation for one natural four-dimensional body, its polar comparison, and the cuboctahedral section used in its proof. It is not a general formula for all cross-polytopes or a universal extremal bound. The existence and values of global self-volume extrema remain open in higher dimensions. The literature comparison is provisional, and no independent human mathematical audit has been performed. Numerical checks are not a substitute for the exact geometric reasoning.

## References

1. G. Wolansky, *Self perimeter of convex sets*, arXiv:2604.01950 (v1 posted 2026-04-02), especially Sections 3–4 and the higher-dimensional recursion.
2. M. Ghandehari and H. Martini, *On self-circumferences in Minkowski planes*, Extracta Mathematicae 34(1) (2019), 73–89. Referenced for the classical planar normalization.
