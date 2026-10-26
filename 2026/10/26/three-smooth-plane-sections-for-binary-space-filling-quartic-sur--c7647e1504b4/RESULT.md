# Three smooth plane sections for binary space-filling quartic surfaces

## Finding
Every geometrically smooth quartic surface \(S\subset\mathbf P^3_{\mathbf F_2}\) containing all fifteen \(\mathbf F_2\)-rational points has **at least three** rational planes whose intersections with \(S\) are geometrically smooth plane quartic curves. This lower bound is sharp. Equivalently, each such surface has at most twelve distinct rational tangent planes, and that upper bound is achieved.

A stronger exhaustive statement holds even without geometric smoothness: among the quartic forms vanishing at all fifteen rational points and nonsingular at those points, the numbers having respectively \(10\), \(11\), or \(12\) distinct rational tangent planes are exactly \(24,192\), \(80,640\), and \(20,160\). There are no other values.

## Assumptions and scope
All forms, derivatives, projective points, and planes are over \(\mathbf F_2\), except geometric smoothness, which is tested over an algebraic closure. A rational plane is a hyperplane with a nonzero binary linear equation, modulo scalars (so one of fifteen). A transverse plane means that its scheme-theoretic quartic intersection with the surface is geometrically smooth. Forms are counted with coordinates fixed: no quotient by projective transformations is taken. The bound applies to every geometrically smooth quartic vanishing at all rational points, whether or not it has any prescribed symmetry.

## Proof
**Step 1: all defining quartics.** The 35 degree-four monomials in four variables evaluate on the 15 nonzero binary vectors with evaluation-map rank 15. Hence the vector space of space-filling quartic equations has dimension \(20\) and contains exactly \(2^{20}=1,048,576\) forms. One independent basis is obtained by binary elimination of the full evaluation matrix. Another is obtained from the 24 forms \(x_k(x_i^2x_j+x_ix_j^2)\), where \(0\leq i<j\leq3\) and \(0\leq k\leq3\). Gaussian elimination verifies that these generators span a rank-20 subspace, hence exactly the same kernel.

**Step 2: exhaustive Gauss-image bound.** At each nonzero binary point \(P\), let \(g_F(P)\) be the four-component gradient. For a pointwise nonsingular form this is a nonzero vector and thus a rational tangent-plane equation. Both complete independent enumerations of the \(2^{20}\) linear combinations yield \(124,992\) forms with gradients nonzero at all fifteen rational points. Among those, precisely \(24,192\) have ten distinct gradient values, \(80,640\) have eleven, and \(20,160\) have twelve. As each gradient determines a unique rational tangent plane, at least three rational planes are absent from the Gauss image.

**Step 3: absence from the image means transverse.** Let \(H\) be a rational plane that is not tangent to \(S\) at a rational point. The quartic restriction \(S\cap H\) vanishes on all seven points of \(\mathbf P^2(\mathbf F_2)\). A standalone exhaustive lemma shows that a binary plane quartic containing all seven points is geometrically singular if and only if it is singular at one of those seven points: the relevant vector space has dimension eight (256 forms), and exactly 24 forms are rationally nonsingular, all verified geometrically smooth by Jacobian-ideal Gröbner bases in each affine chart. Since \(S\) is geometrically smooth, a singular rational point of \(S\cap H\) is exactly a point where \(H=T_PS\). This does not happen, so \(S\cap H\) is geometrically smooth. There are at least three such planes.

**Step 4: sharpness and geometric smoothness.** With variables \(a,b,c,d\), take the explicit polynomial

\[\begin{aligned}F={}&a^3(c+d)+a^2(b^2+bc+d^2)\\&+a(b^3+b^2c+c^3+c^2d+cd^2)\\&+b^3(c+d)+b(c^3+c^2d+cd^2+d^3)+c^3d+cd^3.\end{aligned}\]

Exact binary Gröbner calculations of the hypersurface Jacobian ideal in all four standard projective charts establish smoothness over \(\overline{\mathbf F_2}\); direct evaluation confirms vanishing at all fifteen rational points. Its rational gradient values, in bit-mask coordinates, are \([12,13,3,11,8,9,8,6,15,5,14,1,7,13,9]\), with twelve distinct entries. The missing planes have masks \(2,4,10\), meaning \(b=0\), \(c=0\), and \(b+d=0\). Direct Gröbner checks of all fifteen plane-section restrictions confirm that **exactly those three** are geometrically smooth. Thus the lower bound is attained.

## Verification
Run `python census_monomials.py` (standard-library-only exhaustive kernel enumeration), compile `census_generators.cpp` with `g++ -std=c++17 -O2 -o census_generators census_generators.cpp` and run `./census_generators` (independent generators of the same 20-dimensional space), and run `python geometry_checks.py` (SymPy exact arithmetic for the finite plane lemma, witness smoothness, and all fifteen plane sections). The packaged `.stdout` files record the actual successful output of these programs. All counts are exhaustive for the stated finite domains; no statistical extrapolation is used.

## Relationship to prior work
Bruggemann, Choi, Freidin, and Whyte (2024), Theorem 3.11, rule out plane-transverse-free degree-\(q+2\) smooth space-filling surfaces over odd finite fields. Their statement restricts to odd characteristic and does not imply this even-characteristic \(q=2\) sharp count. Their Lemma 3.9 discusses the relationship between tangencies and rational singularities of plane sections. Asgarli, Duan, and Lai study transverse **lines** and general field-size hypotheses; those results do not imply the exact three-plane guarantee here. The present argument computes the complete binary Gauss-image distribution and supplies a smooth extremal surface.

## Limitations
This theorem is limited to the smallest even field and degree four; it does not assert an analogous bound for larger even fields or for higher-degree hypersurfaces. The exhaustive count is for coordinate-fixed forms, not isomorphism classes. No independent external audit of this result has occurred. Published and unpublished finite-geometry tables may contain overlapping data not identified in the consulted sources.

## References
1. C. Bruggemann, V. Choi, B. Freidin, J. Whyte, *Transverse-freeness in finite geometries*, arXiv:2409.05248 (initial public version 2024-09-08), especially Lemma 3.9 and Theorem 3.11.
2. S. Asgarli, L. Duan, K.-W. Lai, *Transverse lines to surfaces over finite fields*, arXiv:1903.08845 (initial public version 2019-03-21).
3. S. Asgarli, L. Duan, K.-W. Lai, *Transverse linear subspaces to hypersurfaces over finite fields*, arXiv:2008.11306.
4. M. Homma, S. J. Kim, *Filling curves for the projective plane over a finite field*, arXiv:0903.1918 (supporting plane-curve literature; full text not used to establish novelty).
