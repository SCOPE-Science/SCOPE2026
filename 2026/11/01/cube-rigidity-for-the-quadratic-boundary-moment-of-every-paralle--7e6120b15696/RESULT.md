# Cube rigidity for the quadratic boundary moment of every parallelepiped

## Finding

**Theorem.** Every full-dimensional Euclidean parallelepiped \(K\subset\mathbb R^3\) with surface area \(S=\mathcal H^2(\partial K)\) and center of symmetry \(c\) satisfies
\[
\int_{\partial K}|x-c|^2\,d\mathcal H^2(x)\ \ge\ \frac{5}{72} S^2.
\]
Equality holds **if and only if** \(K\) is a Euclidean cube, up to translation and rigid motion. Both the geometric center and the surface-area centroid coincide at \(c\), so this is an exact scale-free bound for the usual centered quadratic surface moment of inertia. The result includes every oblique or sheared parallelepiped, not just rectangular prisms. The coefficient is sharp: a cube of edge length \(a\) has area \(6a^2\) and moment \(5a^4/2\).

## Assumptions and scope

We use ordinary Euclidean length and surface-area measure. A full-dimensional parallelepiped is a translate of
\[
K_0=\left\{t_1u+t_2v+t_3w:-\frac12\le t_i\le\frac12\right\}
\]
for linearly independent vectors \(u,v,w\in\mathbb R^3\). Let \(a=|u|\), \(b=|v|\), \(d=|w|\) and denote the three individual facet areas by
\[
F_1=|v\times w|,\qquad F_2=|u\times w|,\qquad F_3=|u\times v|.
\]
Thus \(0<F_1\le bd\), \(0<F_2\le ad\), \(0<F_3\le ab\), with equality in all three area bounds precisely when all edge vectors are mutually perpendicular. Put \(T=F_1+F_2+F_3\), so \(S=2T\). The center of symmetry is the centroid for both uniform volume and uniform boundary area, by antipodal symmetry.

## Proof

**1. Exact facet moment.** A point on either facet corresponding to \(u\) has the form \(\pm u/2+tv+sw\), where \(t,s\in[-1/2,1/2]\). Averaging the squared norm over both facets gives \(|u|^2/4+(|v|^2+|w|^2)/12\), since the mixed terms integrate to zero. Summing the three pairs gives
\[
I:=\int_{\partial K}|x-c|^2d\mathcal H^2(x)
=\frac16\sum_{i=1}^3(T+2F_i)a_i^2,
\qquad (a_1,a_2,a_3)=(a,b,d).
\]
Consequently \(I\ge (5/72)S^2\) is equivalent to
\[
N:=\sum_{i=1}^3(T+2F_i)a_i^2\ \ge\ \frac53T^2.
\tag{1}
\]

**2. Convex relaxation over independent facet areas.** Fix arbitrary positive lengths \(a,b,d\). In the larger closed box
\[
0\le F_1\le bd,\quad0\le F_2\le ad,\quad0\le F_3\le ab,
\tag{2}
\]
consider the quadratic polynomial
\[
H(F_1,F_2,F_3)=\frac53(F_1+F_2+F_3)^2-
\sum_{i=1}^3 F_i\bigl(a^2+b^2+d^2+2a_i^2\bigr).
\]
It is convex (its Hessian equals \((10/3)\mathbf1\mathbf1^{\mathsf T}\)). Every point of the box is a convex combination of its eight vertices, so it suffices to prove \(H\le0\) there. This relaxation is legitimate even though not every triple of face areas within the box is realized by an actual parallelepiped.

**3. All eight vertices.** Write \(D=-H=N-5T^2/3\). At the zero vertex, \(D=0\). At a single-face vertex such as \((bd,0,0)\),
\[
D=bd\left(3a^2+b^2+d^2-\frac53bd\right)>0,
\]
by \(b^2+d^2\ge2bd\). The other two single-face vertices are symmetric. At a two-face vertex such as \((bd,ad,0)\),
\[
D=d(a+b)\left((a+b)^2+d^2-\frac53d(a+b)\right)
=d(a+b)\left(\left(a+b-\frac56d\right)^2+\frac{11}{36}d^2\right)>0.
\]
Again the other two follow by permutation.

At the all-three-face vertex \((bd,ad,ab)\), put \(t=ab+ad+bd\) and \(s=a+b+d\). Direct expansion gives
\[
3D=3ts^2+6abd\,s-11t^2
=\frac12\Bigl[
(a-b)^2\bigl(5ab+d(a+b)\bigr)
+(a-d)^2\bigl(5ad+b(a+d)\bigr)
+(b-d)^2\bigl(5bd+a(b+d)\bigr)
\Bigr]\ge0.
\tag{3}
\]
Every coefficient of a squared difference is strictly positive, hence equality here requires \(a=b=d\). This proves \(H\le0\) throughout (2), and therefore (1) for every actual parallelepiped.

**4. Rigidity.** Because the actual \(F_i\) are all positive, equality cannot occur at the zero vertex. If any \(F_i\) is strictly smaller than its upper bound, write \(F\) in the standard multilinear convex decomposition into the eight box vertices. At least one strictly negative vertex of \(H\) receives positive weight: if any coordinate is below its upper bound and another is positive, a one- or two-face vertex occurs with positive weight. Thus equality forces all \(F_i\) to equal their upper bounds. Equation (3) then forces \(a=b=d\). Pairwise maximal cross products force mutual orthogonality, so \(K\) is a Euclidean cube. Conversely the cube attains equality by the explicit facet integral above.

## Verification

The standalone program `verify.py` checks the exact algebraic identity (3), all eight box vertices, and three rational interior points for each of 1,000 integer length triples. It then checks 698 nondegenerate pseudorandom oblique triples by two independent methods: the closed facet formula and Gaussian polynomial-exact quadrature directly over the six facets, including the sharp inequality. It checks the unit cube equality separately. The observed counts in the supplied execution were 11,000 exact rational checks and 699 geometric checks. The proof above, not the finite checks, establishes the assertion for arbitrary real independent edge vectors.

Run the verifier with `python verify.py` using only the Python standard library.

## Relationship to prior work

Freitas, Laugesen and Liddell (2007), Theorem 5 and Section 5.4, prove precisely the constant \(5/72\) for **cuboids/rectangular prisms**; their theorem assumes mutually orthogonal edges and does not cover a general sheared parallelepiped. Their other results include existence and comparisons with triangular prisms, ellipsoids and other polyhedra. The present theorem extends that known exact constant and unique cube equality to the full six-parameter affine family of nondegenerate parallelepipeds, using an independent-area convex relaxation and an explicit three-variable sum-of-squares identity.

Csató, Giovagnoli and Roy (2026) study fixed-surface-area weighted perimeter optimization in arbitrary dimensions and record the three-dimensional unrestricted minimization problem as open. Their published results on existence and two-dimensional extremizers do not imply the present sharp parallelepiped subclass theorem. The full primary papers were inspected in the mathematical comparisons; no claim of universal convex-body optimality is made here.

## Limitations

This theorem is restricted to three-dimensional parallelepipeds. It does not prove the cube minimizes the moment among all convex bodies, nor among arbitrary prisms or polytopes; indeed published examples have smaller dimensionless moment ratios. The bound uses Euclidean surface area, not affine surface area, and the center is the central-symmetry point. Historical priority is provisional, especially for an equivalent result in older affine-polytope literature; the directly motivating and nearest primary sources were examined, but no search establishes exhaustive worldwide uniqueness. Independent mathematical audit has not been performed.

## References

1. P. Freitas, R. S. Laugesen, G. F. Liddell, *On convex surfaces with minimal moment of inertia*, Journal of Mathematical Physics **48** (2007), 122902, DOI: 10.1063/1.2823888. Theorem 5, Section 5.4, publicly readable author-provided full text at https://www.researchgate.net/publication/228883213_On_convex_surfaces_with_minimal_moment_of_inertia .
2. G. Csató, D. Giovagnoli, P. Roy, *Weighted Perimeters and pth Moments of Inertia of Convex Curves and Surfaces*, arXiv:2608.19851v1, originally public 2026-08-20, https://arxiv.org/pdf/2608.19851 . See Introduction pp. 1–4 and Theorem 1.2.
