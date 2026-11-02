# Closed bidegree formula for logarithmic discriminants of second hypersimplices

## Finding
For any integer \(n\ge4\), let \(A\) consist of the exponent vectors \(e_i+e_j\), where \(1\le i<j\le n\), modulo translation in the rank-\(n-1\) lattice \(\sum_i x_i=2\). Let \(\Lambda_A\) be the logarithmic discriminant of [1]. Its bidegree is
\[
\boxed{\bigl(\deg_z\Lambda_A,\deg_{s,\nu}\Lambda_A\bigr)=\bigl(n(n-1)(2^{n-2}-n+1),\ n(2^{n-2}-2)\bigr).}
\]
More precisely, the specialized Hurwitz form of the second-hypersimplex toric variety, after the universal exponent-only factor is divided out, is a nonzero scalar multiple of
\[
\Lambda_A\prod_{1\le i<j\le n}z_{ij}^{\,2(n-3)}.
\]

## Assumptions and scope
Work over \(\mathbb C\); \(n\) is any integer at least four. The toric variety \(X_A\subset\mathbb P^{\binom n2-1}\) is the closure of the monomial map with homogeneous coordinates \((t_it_j)_{i<j}\). The logarithmic discriminant and its normalization, including the universal factor \(s^{(d-1)h}\), are as in Theorem 5.2 of [1]. In the calculations below \(d=n-1\). The claimed bidegree concerns the irreducible residual factor, not the unnormalized specialized Hurwitz polynomial.

## Proof
**1. Degree, sectional genus and Hurwitz degree.** The normalized volume of the second hypersimplex is its Eulerian number \(v=2^{n-1}-n\). An independent Ehrhart calculation gives, for all nonnegative integers \(k\),
\[
L(k)=\#(k\Delta(2,n)\cap\mathbb Z^n)
=\binom{2k+n-1}{n-1}-n\binom{k+n-2}{n-1}.
\]
Indeed the first term counts weak compositions of \(2k\) into \(n\) parts, and at most one part can exceed \(k\). Taking \(n-2\) successive backward differences of this Hilbert polynomial computes the Hilbert polynomial of a general linear-section curve. Direct binomial expansion yields
\[
P_C(k)=(2^{n-1}-n)k-(n-4)2^{n-3}.
\]
Thus its sectional genus is \(g=1+(n-4)2^{n-3}\). The Hurwitz degree [1,2] is therefore
\[
h=2v+2g-2=n(2^{n-2}-2).
\]
The general curve misses the finite singular locus, so this Hurwitz formula applies.

**2. Isolated singularities and their chart.** Every face of \(\Delta(2,n)=\{(x_i):0\le x_i\le1,\sum x_i=2\}\) of positive dimension has independent active facet normals in the quotient normal lattice. Hence every positive-dimensional torus orbit of \(X_A\) is smooth. At a vertex \(e_1+e_2\), set its monomial coordinate to one and let \(U_j\), respectively \(V_j\), be the monomial coordinates indexed by \(\{1,j\}\), respectively \(\{2,j\}\), for \(3\le j\le n\). The local affine chart is the cone of \(2\times m\) matrices of rank at most one, where \(m=n-2\):
\[
R=\mathbb C[U_3,\ldots,U_n,V_3,\ldots,V_n]/(U_iV_j-U_jV_i).
\]
The Segre-cone Hilbert series is \((1+(m-1)t)/(1-t)^{m+1}\), so a general homogeneous linear system of parameters has Artinian quotient of length \(m\), with graded Hilbert series \(1+(m-1)t\). All \(\binom n2\) vertices have identical charts by permutation symmetry.

**3. Local transverse splitting.** Make the coefficient of the vertex monomial \(z_{12}=\varepsilon\), choose the other monomial coefficients generically, and take generic exponent parameters with \(s=1\). Locally the critical-point linear section has \(m+1\) equations of the shape
\[
\varepsilon+\sum_{j=3}^n\alpha_jU_j+\nu_1g+O(2)=0,\qquad
\alpha_jU_j+\beta_jV_j+\nu_jg+O(2)=0,
\]
where \(g=\varepsilon+\sum_j(\alpha_jU_j+\beta_jV_j)+O(2)\); the displayed quadratic terms come from coordinates at lattice points not adjacent to the chosen vertex. Summing the latter equations gives
\[
g=\frac{\varepsilon}{1+\sum_j\nu_j}+O(\varepsilon^2).
\]
For a completely explicit nonempty genericity witness, set \(\alpha_j=\nu_j=1\), take pairwise distinct nonzero \(\beta_j=b_j\), and choose \(\nu_1\) away from the finite exceptional set. The rank-one equations mean \(U_j=rV_j\); the first-order solutions are
\[
V_j=-\frac{\varepsilon}{(1+m)(r+b_j)}+O(\varepsilon^2),\qquad
\sum_{j=3}^n\frac{r}{r+b_j}=m+1+\nu_1.
\]
After clearing denominators the last equation has degree \(m\) and generically \(m\) distinct simple roots away from its poles: the rational function has a pole at each distinct \(-b_j\), hence its map to \(\mathbb P^1\) has degree \(m\) and is separable in characteristic zero. The Jacobian of the local transverse intersection is invertible at each leading solution. The analytic implicit-function theorem thus lifts them to \(m\) distinct branches for \(\varepsilon\ne0\), all tending to the vertex as \(\varepsilon\to0\).

**4. Exact local discriminant order.** A general transverse Artinian section of the Segre cone has local basis consisting of \(1\) and \(m-1\) degree-one classes. In the present witness, use \(1,V_3,\ldots,V_{n-1}\). Their evaluation matrix on the \(m\) split branches has first column \(1\) and remaining columns proportional to \(\varepsilon/(r_i+b_j)\). Its determinant is a nonzero scalar times \(\varepsilon^{m-1}\) to leading order. For the nonzero scalar, suppose a combination of \(1,1/(r+b_3),\ldots,1/(r+b_{n-1})\) vanishes at all \(m\) distinct \(r_i\). Multiplication by the \(m-1\) denominators yields a polynomial of degree at most \(m-1\) with \(m\) roots. It is identically zero, and evaluating residues at the distinct poles forces every coefficient to vanish. Thus the evaluation determinant is invertible at leading order. At \(\varepsilon=0\), the local linear equations give \(g=0\), \(U_j=-b_jV_j\), and \(\sum_j b_jV_j=0\). The rank-one minors then force \(V_iV_j=0\) for distinct indices, while multiplication of the linear relation gives \(V_i^2=0\); thus \(1,V_3,\ldots,V_{n-1}\) indeed forms a basis of the length-\(m\) special fiber. The finite rank-\(m\) intersection algebra is generically étale away from \(\varepsilon=0\), and its trace pairing is the Gram matrix of this evaluation matrix. Consequently its discriminant vanishes to order exactly \(2(m-1)=2(n-3)\) along the vertex coefficient divisor. Other intersection points contribute units. Because this order is attained at a generic point of the divisor, it is the global extraneous exponent.

**5. Final degree subtraction.** Theorems 4.1 and 5.2 of [1] show that only singular torus orbits produce coefficient-only factors, and that the universal-exponent-normalized Hurwitz form has coefficient degree \(dh\). By Step 2, the singular orbits are exactly the \(\binom n2\) vertices, and by Step 4 each contributes \(2(n-3)\). Therefore
\[
\deg_z\Lambda_A=(n-1)n(2^{n-2}-2)-\binom n2\,2(n-3)
=n(n-1)(2^{n-2}-n+1).
\]
The exponent degree stays \(h=n(2^{n-2}-2)\), proving the claim.

## Verification
An independent arithmetic checker `verify.py` recomputes the Ehrhart difference and derived \((b,h)\) for integers \(4\le n\le12\), and compares the first four pairs to Example 8.3, Table 3 of [1]. The proof of the local discriminant order is the trace-determinant argument in Steps 3--4; the finite arithmetic tests alone are not an infinite proof.

## Relationship to prior work
Goertz--Sturmfels--Telen [1], Theorems 4.1 and 5.2, establish the factorization framework and Hurwitz-degree formula for singular toric varieties. Their Example 8.3 records the pairs \((12,8),(80,30),(330,84),(1092,210)\) numerically for \(n=4,5,6,7\) and explicitly asks for degree formulas in the singular case; it does not establish the all-\(n\) formula or the uniform local multiplicity computed here. Sturmfels [2] gives the foundational Hurwitz degree formula, not the specialized logarithmic-discriminant correction.

## Limitations
The formula is for second hypersimplices only, over characteristic zero, with the logarithmic-discriminant convention of [1]. No assertion about general hypersimplices \(\Delta(r,n)\), positive-characteristic branch collisions, or independent external validation is made. Priority outside the inspected literature remains an uncertainty.

## References
[1] M. Goertz, B. Sturmfels, S. Telen, *The Logarithmic A-Discriminant*, arXiv:2610.29204v1 (first public 2026-10-21), Sections 4--5 and Example 8.3. https://arxiv.org/html/2610.29204v1

[2] B. Sturmfels, *The Hurwitz Form of a Projective Variety*, arXiv:1410.6703v2, Theorem 1.1. https://arxiv.org/abs/1410.6703
