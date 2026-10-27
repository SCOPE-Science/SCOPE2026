# Sharp contrast profile for four-knot periodic linear-spline projection

## Finding
On a circle with four consecutive arcs of lengths \(r,1,r,1\), the \(L^2\)-orthogonal projector \(P_r\) onto continuous piecewise-affine functions has the exact \(L^\infty\)- and \(L^1\)-norm
\[
\|P_r\|=F(r)=\frac{90r^6+913r^5+3154r^4+4742r^3+3154r^2+913r+90}{3(r+2)(r+3)^2(2r+1)(3r+1)^2}.
\]
The profile is inversion-symmetric, \(F(r)=F(1/r)\), and is strictly increasing on \((0,1)\) and strictly decreasing on \((1,\infty)\). Its unique sharp maximum is \(F(1)=17/9\), while \(F(r)>5/3\) for every finite positive contrast and \(\lim_{r\to0^+}F(r)=\lim_{r\to\infty}F(r)=5/3\).

## Assumptions and scope
Fix any real \(r>0\). Form a metric circle from four ordered edges of positive arclengths \(r,1,r,1\), with four distinct vertices numbered cyclically \(0,1,2,3\). Let \(V_r\) be the four-dimensional space of real or complex continuous periodic functions that restrict to affine functions on each edge. The operator \(P_r:L^2\to V_r\) is orthogonal for unweighted arclength measure. The stated norms concern the corresponding extensions on \(L^\infty\) and \(L^1\), and also the restriction \(C\to C\) with supremum norm. The normalization of total circle length is immaterial: scaling all edge lengths by a positive factor preserves the norm. No infinite-grid or larger-knot-count assertion is made.

## Proof
Let \(\phi_i\) be the nodal hat with value one at vertex \(i\) and zero at the other vertices. The Gram matrix \(G=(\int\phi_i\phi_j)_{i,j=0}^3\) is
\[
G=\begin{pmatrix}
(r+1)/3&r/6&0&1/6\\
r/6&(r+1)/3&1/6&0\\
0&1/6&(r+1)/3&r/6\\
1/6&0&r/6&(r+1)/3
\end{pmatrix}.
\]
The matrix is positive definite, since for any nonzero nodal coefficient vector its associated spline is nonzero in \(L^2\). Setting \(Q=(r+1)(r+3)(3r+1)\), multiplication verifies that the first row of \(G^{-1}\) equals
\[
Q^{-1}\bigl(4(3r^2+8r+3),\;-2r(3r+5),\;8r,\;-2(5r+3)\bigr).
\]
Denote its positive magnitudes by \(A,B,C,D\), in that order. The reproducing kernel for evaluation at vertex zero is \(K_0(y)=A\phi_0(y)-B\phi_1(y)+C\phi_2(y)-D\phi_3(y)\). The \(L^\infty\)-norm of this evaluation functional is exactly \(\int|K_0(y)|\,dy\), by choosing the measurable sign of \(K_0\) as input. On an edge of length \(\ell>0\), any affine function joining opposite-sign endpoint values \(u\) and \(-v\), for \(u,v>0\), has absolute integral \(\ell(u^2+v^2)/(2(u+v))\). Every pair of adjacent coefficients above has opposite signs; therefore
\[
F(r)=\frac{r(A^2+B^2)}{2(A+B)}+\frac{B^2+C^2}{2(B+C)}+\frac{r(C^2+D^2)}{2(C+D)}+\frac{D^2+A^2}{2(D+A)}.
\]
Substituting the four explicit magnitudes, clearing positive denominators and collecting coefficients gives the displayed degree-six rational function. This proves equality at vertex zero. Alternating arc lengths yield a dihedral subgroup acting transitively on the four vertices, hence every vertex has the same evaluation norm.

For any point \(x\) in an edge with vertices \(i,j\), the function \((P_rf)(x)\) is a convex combination of \((P_rf)(i)\) and \((P_rf)(j)\). Thus its operator norm is no larger than the larger of the two vertex evaluation norms. Consequently \(\|P_r\|_{\infty\to\infty}=F(r)\), and the kernel symmetry implies the same \(L^1\)-norm. Bounded measurable sign functions give equality; continuous sign approximations achieve arbitrarily close values, proving equality of the \(C\to C\) norm as well.

The exact algebraic comparisons are
\[
F(r)-\frac53=\frac{8r(r+1)^2(11r^2+26r+11)}{3(r+2)(r+3)^2(2r+1)(3r+1)^2}>0,
\]
\[
\frac{17}{9}-F(r)=\frac{2(r-1)^2(18r^4+69r^3+98r^2+69r+18)}{9(r+2)(r+3)^2(2r+1)(3r+1)^2}\ge0.
\]
Differentiation yields
\[
F'(r)=-\frac{16(r-1)(r+1)(33r^6+178r^5+377r^4+456r^3+377r^2+178r+33)}{3(r+2)^2(r+3)^3(2r+1)^2(3r+1)^3}.
\]
All denominators and coefficient-positive factors are strictly positive when \(r>0\). Thus the derivative has the sign of \(1-r\), proving strict monotonicity and uniqueness of the maximum. The inversion symmetry follows either by exchanging the two edge lengths (and scaling arclength) or directly from the palindromic rational expression; the endpoint limits follow from the leading and constant coefficients.

## Verification
The companion standalone file `check_periodic4.py` uses Python standard-library rational arithmetic. It reconstructs the Gram matrix, inverses and vertex kernel, computes signed-piece absolute integrals exactly, compares the resulting norm with the claimed rational expression, and checks the two difference identities for 221 rational edge contrasts. It also checks inverse-contrast symmetry and six independent derivative evaluations. The displayed explicit factorizations, rather than finite samples, establish their universal inequalities.

## Relationship to prior work
Ciesielski and Kamont [1], including their equations (2.2) and (2.10)–(2.15), study the norm of interval-based linear-spline projections and the Franklin system. Their explicit sign-integral mechanism is analogous, but an interval Gram matrix has endpoints rather than the cyclic corner entries here. Passenbrunner [2], Theorem 1.4 and Section 3, proves knot-independent boundedness of arbitrary periodic spline orthoprojectors. That theorem does not determine the exact four-vertex two-periodic contrast profile, the upper value \(17/9\), or uniqueness of the uniform maximizing shape. Thus the statement refines the available general bounds in the smallest alternating periodic mesh.

## Limitations
The result applies to exactly four distinct vertices, two repeated positive arc lengths, order-two splines, and unweighted arclength orthogonality. It does not classify all non-alternating four-arc meshes or larger circles. No claim of an independent audit is made. The kernel signs attaining the \(L^\infty\)-norm generally cannot be realized exactly by a continuous input, although continuous inputs approximate the norm. Prior unindexed explicit finite-cycle computations could coincide with this special case.

## References
[1] Z. Ciesielski and A. Kamont, *The Lebesgue constants for the Franklin orthogonal system*, Studia Mathematica 164 (2004), 55–73, DOI: 10.4064/sm164-1-4. https://www.impan.pl/shop/en/publication/transaction/download/product/90654

[2] M. Passenbrunner, *Orthogonal projectors onto spaces of periodic splines*, arXiv:1608.06720, first public version 2016-08-24; later Journal of Complexity 42 (2017), 85–93. https://arxiv.org/abs/1608.06720
