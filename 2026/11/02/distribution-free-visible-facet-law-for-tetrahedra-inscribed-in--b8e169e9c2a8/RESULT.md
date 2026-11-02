# Distribution-free visible-facet law for tetrahedra inscribed in centrally symmetric convex surfaces

## Finding

Let \(K\subset\mathbb R^3\) be any centrally symmetric convex body with \(0\in\operatorname{int}K\). Independently sample \(X_1,X_2,X_3,X_4\) from probability measures \(\mu_i\) supported on \(\partial K\). The four measures need not be equal or rotationally symmetric. Assume only that \(\mu_i(A)=\mu_i(-A)\) for every measurable \(A\), and that every affine plane has \(\mu_i\)-measure zero.

Almost surely the four points form a nondegenerate tetrahedron \(T=\operatorname{conv}\{X_1,X_2,X_3,X_4\}\). Let \(V\) be the number of triangular facets of \(T\) whose supporting planes strictly separate \(0\) from the interior of \(T\) (equivalently, the number of facets externally visible from \(0\)). Then

\[
\boxed{\Pr(V=0)=\tfrac18,\qquad \Pr(V=1)=\tfrac12,\qquad \Pr(V=2)=\tfrac38,\qquad \Pr(V\ge3)=0.}
\]

Consequently \(\mathbb E V=5/4\), \(\operatorname{Var}(V)=7/16\), and, conditional on \(0\notin T\), the probabilities of one and two visible facets are \(4/7\) and \(3/7\). These probabilities do not depend on \(K\) or on the four potentially different centrally symmetric sampling measures.

## Assumptions and scope

A convex body is compact, convex, and has nonempty interior. Central symmetry means \(K=-K\). Each \(\mu_i\) is a Borel probability measure on \(\partial K\) invariant under \(x\mapsto-x\). The no-affine-plane-mass condition guarantees all needed affine and linear general-position events with probability one; no smoothness or strictly convex boundary is required. Facets are viewed from the fixed origin, not from a direction at infinity. A facet is counted only when the origin lies in the strict opposite halfspace from the fourth vertex. Boundary or coplanar coincidences are excluded by the hypotheses.

## Proof

**1. Facets and barycentric signs.** For a nondegenerate configuration there are unique real \(\lambda_i\) with
\[
\sum_{i=1}^4\lambda_iX_i=0,\qquad \sum_{i=1}^4\lambda_i=1.
\]
The affine function \(\lambda_i(y)\) vanishes on the facet opposite \(X_i\) and equals one at \(X_i\). Hence that facet strictly separates \(0\) from \(T\) precisely when \(\lambda_i<0\), and \(V=\#\{i:\lambda_i<0\}\).

**2. A boundary restriction.** There cannot be three negative \(\lambda_i\). Otherwise the sole positive coordinate, say \(\lambda_j\), is greater than one, and
\[
X_j=\sum_{i\ne j}\frac{-\lambda_i}{\lambda_j}X_i+\frac1{\lambda_j}0.
\]
All coefficients on the right are strictly positive and sum to one. Because \(0\in\operatorname{int}K\) and each other \(X_i\in K\), this convex combination lies in \(\operatorname{int}K\), contrary to \(X_j\in\partial K\). Thus \(V\le2\). (Four negative coordinates are excluded already by their sum being one.)

**3. Sixteen equiprobable antipodal orientations.** Disintegrate each \(X_i\) into an unoriented line and an independent fair sign: \(X_i=\varepsilon_iU_i\), \(\varepsilon_i\in\{-1,1\}\). This is possible because \(K=-K\) and each \(\mu_i\) is antipodally invariant; conditional on all \(U_i\), the four signs remain independent and uniform. Since four vectors in \(\mathbb R^3\) have a one-dimensional linear-dependence space, let \(\sum_i b_iU_i=0\) with every \(b_i\ne0\). For the signed configuration put \(a_i=\varepsilon_ib_i\). The signs of \((a_1,a_2,a_3,a_4)\) run uniformly over all sixteen patterns. General position ensures \(S=\sum_i a_i\ne0\); the unique barycentric coordinates are \(\lambda_i=a_i/S\).

In the two sign patterns with all \(a_i\) of one sign, all \(\lambda_i>0\), giving \(V=0\). In each of the eight patterns with a \(1\)-versus-\(3\) sign split, the barycentric signs yield either one or three negative coordinates. Step 2 excludes three, so \(V=1\). In each of the six patterns with a \(2\)-versus-\(2\) split, multiplication by the common sign of \(1/S\) preserves two negative coordinates, so \(V=2\). The counts \(2,8,6\), divided by sixteen, give the asserted law. Summing the three masses gives one. The moment identities follow immediately.

The distribution holds conditionally on almost every collection of four unoriented lines, a stronger statement than unconditional shape or measure independence.

## Verification

The standalone `verify.py` uses exact rational arithmetic to enumerate all sixteen antipodal sign configurations of four rational unit vectors and independently tests outward facet halfspaces against barycentric signs. It repeats the exact test after two nonuniform invertible stretches, exhibits a rational interior-point configuration with three visible facets, and performs reproducible Monte Carlo diagnostics for the sphere, nonidentically distributed ellipsoidal samples, and nonidentically distributed \(\ell_4\)-boundary samples. Run `python3 verify.py` with the standard library. The analytic proof above, not the finite enumeration for one configuration or the simulations, establishes the universal statement.

## Relationship to prior work

Wendel's classical theorem yields the previously known \(\Pr(0\in T)=1/8\) for sphere-uniform tetrahedra, and, more generally, for symmetric sampling. Bonnet and O'Reilly study signed facet heights of spherical random polytopes and give exact formulas for **expected** numbers of facets by height in the rotationally uniform model; in conjunction with Wendel's law, these tools can recover the numerical one-sphere probabilities. The present statement is instead the full conditional sign-orbit classification for arbitrary centrally symmetric convex surfaces and four independent **nonidentical** antipodally invariant boundary laws. Neither the rotationally invariant facet-height formulas nor the scalar absorption probability alone state that joint distribution-free extension. Fodor, Montenegro Pinzón, and Vígh study the distinct spindle-convex analogue of Wendel's question.

## Limitations

The common-boundary hypothesis is substantive. If \(X_1=(1/10,1/10,1/10)\) lies in the interior of the unit ball and the other three points are the coordinate unit vectors, the origin has barycentric coordinates \((10/7,-1/7,-1/7,-1/7)\), and three facets are externally visible. Such configurations have positive probability under suitable absolutely continuous interior sampling. The result does not assert analogous universal laws for arbitrary interior laws, higher-dimensional simplices, or more than four sample points. No priority claim beyond the precisely stated distribution-free extension is made.

## References

1. G. Bonnet and E. O'Reilly, *Facets of spherical random polytopes*, arXiv:1908.04033 (first posted 2019-08-12); *Mathematische Nachrichten* 295 (2022), 1901–1933, DOI:10.1002/mana.202000314.
2. J. G. Wendel, *A problem in geometric probability*, *Mathematica Scandinavica* 11 (1962), 109–111, DOI:10.7146/math.scand.a-10655.
3. F. Fodor, N. A. Montenegro Pinzón, and V. Vígh, *On Wendel's equality for intersections of balls*, *Aequationes Mathematicae* 97 (2023), 439–451, first published 2022-09-10, DOI:10.1007/s00010-022-00912-3.
4. A. Akopyan, H. Edelsbrunner, and A. Nikitenko, *The Beauty of Random Polytopes Inscribed in the 2-Sphere*, arXiv:2007.07783 (2020-07-15), DOI:10.1080/10586458.2021.1980459.
