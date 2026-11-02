# A sharp triangle-area dispersion law for every trapezoid

## Finding

Let \(K\) be a nondegenerate convex Euclidean trapezoid, meaning a quadrilateral with at least one pair of parallel opposite sides. Denote its longer and shorter parallel bases by \(B\ge b>0\) and set \(t=b/B\in(0,1]\). Take three points independently, each uniformly distributed with respect to area in \(K\), and let \(T\) be the unsigned area of their triangle. Define the dimensionless quantity
\[
C(K)=\frac{\operatorname{Var}(T)}{(\mathbb ET)^2}.
\]
Then \(C(K)=C(t)\), where, writing
\[
P(t)=3t^4+12t^3+14t^2+12t+3,
\]
one has the exact rational profile
\[
\boxed{C(t)=\frac{9t^8+72t^7+204t^6+312t^5+326t^4+312t^3+204t^2+72t+9}{P(t)^2}.}
\]
It is strictly decreasing for \(0<t<1\), with exact range
\[
\boxed{\frac{95}{121}\le C(K)<1.}
\]
The lower bound is attained exactly by parallelograms; the upper bound is approached as the short base shrinks to zero and is not attained by a nondegenerate trapezoid. Consequently, a single exact value of \(C(K)\) uniquely determines \(b/B\), independent of height or shear.

The inverse has sharp endpoint behavior:
\[
1-C(t)=\frac83t^2+O(t^3)\quad(t\downarrow0),\qquad
C(t)-\frac{95}{121}=\frac{180}{1331}(1-t)^2+O((1-t)^3)\quad(t\uparrow1).
\]
Hence the inverse shape parameter is locally Lipschitz at every interior value of \(C\), but has optimal Hölder exponent \(1/2\) at both endpoint values. It is also globally Hölder with exponent \(1/2\) on its attainable range.

## Assumptions and scope

All sampling is from the two-dimensional interior **by normalized Lebesgue area**, independently for each point. A trapezoid here includes parallelograms as the equal-base endpoint. The triangular object with \(b=0\) is used only as a limit, not as a nondegenerate quadrilateral. Boundary coincidences or collinear sampled triples have probability zero. Population moments, rather than finite-sample estimators, are considered.

The ratio \(C\) is invariant under invertible affine maps: every triangle area changes by the same positive determinant magnitude, so the ratio of variance to squared mean is unchanged. Shearing and scaling normalize any such trapezoid to
\[
K_t=\{(x,y):0\le y\le1,\ |x|\le r(y)\},\qquad r(y)=1-(1-t)y.
\]
Its total area is \(1+t\), and conditional on a sampled height \(Y=y\), the horizontal coordinate is uniform on \([-r(y),r(y)]\), while \(Y\) has density \(2r(y)/(1+t)\).

## Proof

**1. The first area moment.** Order the heights of three sampled points as \(y_1<y_2<y_3\). Put \(r_i=r(y_i)\), \(\Delta=y_3-y_1\), \(A=(y_3-y_2)r_1\), \(B=(y_2-y_1)r_3\), and \(D=\Delta r_2=A+B\). Conditional horizontal coordinates can be written as \(r_iU_i\), where the \(U_i\) are independent uniform variables on \([-1,1]\). The triangle area is
\[
T=\frac12|AU_1+BU_3-DU_2|.
\]
Because \(|AU_1+BU_3|\le D\), integration first over \(U_2\), followed by \(U_1,U_3\), yields
\[
\mathbb E[T\mid y_1,y_2,y_3]
=\frac D4+\frac{A^2+B^2}{12D}
=\frac D3-\frac{AB}{6D}.
\]
The ordered-height density is \(6\prod_i[2r_i/(1+t)]\). Integrating the middle height using
\[
\int_{y_1}^{y_3}r(y_2)^2\,dy_2=\frac\Delta3(r_1^2+r_1r_3+r_3^2),\qquad
\int_{y_1}^{y_3}(y_3-y_2)(y_2-y_1)\,dy_2=\frac{\Delta^3}{6}
\]
gives the polynomial double integral
\[
\mathbb ET=\frac{4}{3(1+t)^3}\int_0^1\!\int_{y_1}^1
(y_3-y_1)^2(4r_1^3r_3+3r_1^2r_3^2+4r_1r_3^3)\,dy_3\,dy_1.
\]
Direct polynomial integration produces
\[
\boxed{\mathbb ET=\frac{P(t)}{36(1+t)^3}.}
\]
This first-moment calculation is included for completeness; general polygonal expected-hull-area results precede the present result.

**2. The second area moment.** If \(Z_1,Z_2,Z_3\) are independent copies of a centered planar random vector with covariance matrix \(\Sigma\), then the squared signed-area determinant expands into the sum of three pair determinants. Their mixed expectations vanish by centering and independence, and each squared pair determinant has expectation \(2\det\Sigma\). Thus, for the unsigned triangle area,
\[
\mathbb E[T^2]=\frac14\cdot6\det\Sigma=\frac32\det\Sigma.
\]
For the uniform distribution on \(K_t\), horizontal reflection symmetry makes the covariance diagonal. Elementary slice integration gives
\[
\operatorname{Var}(X)=\frac{1+t^2}{6},\qquad
\operatorname{Var}(Y)=\frac{1+4t+t^2}{18(1+t)^2}.
\]
Consequently,
\[
\boxed{\mathbb E[T^2]=\frac{(1+t^2)(1+4t+t^2)}{72(1+t)^2}.}
\]
This determinant identity is a general elementary moment identity and is not claimed as a new general lemma.

**3. The normalized profile and its strict shape ordering.** Substitution into \(C=\mathbb E[T^2]/(\mathbb ET)^2-1\) gives the displayed polynomial ratio. Exact differentiation factors as
\[
\boxed{C'(t)=\frac{144t(t-1)(1+t)^3(t^4+4t^3+10t^2+4t+1)}{P(t)^3}.}
\]
Every factor other than \(t-1\) is positive on \((0,1)\), proving strict decrease. Exact endpoints are \(C(0)=1\) (limiting triangle) and \(C(1)=95/121\) (parallelogram), giving the full range, rigidity and uniqueness of inverse reconstruction.

**4. Sharp inverse stability.** Expanding the rational function gives the two displayed quadratic endpoint laws. No Hölder inverse exponent exceeding \(1/2\) is possible at either endpoint, since the changes in \(C\) are quadratic in the base-ratio changes. In the interior \(C'(t)\ne0\), so the inverse function theorem gives local Lipschitz regularity. For the global bound, \(-C'(t)/(t(1-t))\) extends to a strictly positive continuous function on \([0,1]\), hence has a positive minimum \(m\). For \(0\le a<b\le1\),
\[
C(a)-C(b)\ge m\int_a^b u(1-u)\,du\ge\frac{m}{6}(b-a)^2.
\]
Thus \(|b-a|\le\sqrt{6/m}\sqrt{|C(a)-C(b)|}\), establishing the optimal global Hölder exponent.

## Verification

Run `python verify.py` after installing the package in `requirements.txt`. The checker performs exact symbolic integrations of the first and second area moments, confirms the rational derivative factorization, endpoints and quadratic coefficients, and independently simulates area-uniform random triangles in several trapezoids including a sheared example. The exact proof establishes the theorem for all admissible base ratios; Monte Carlo checks are corroborative only and do not serve as universal proof.

## Relationship to prior work

The Sylvester four-point identity relates the probability of four uniform interior points being in convex position to the first area moment of three random points; it is classical and appears, for example, in the 2015 account of Marckert and the 2021 exposition of Sharpe. Buchta (1984) gives general expected convex-hull-area formulas in polygonal domains, including the first-moment setting used here. Neither that prior first-moment evaluation nor the elementary covariance determinant formula is presented as original.

The contribution here is the exact **shape ordering of the normalized triangle-area dispersion**, its complete attainable range, inverse reconstruction of the trapezoid's affine base ratio, and the two sharp endpoint inverse stability laws. The inspected 2024 Gaussian Sylvester work instead concerns Gaussian samples and Gale duality, not uniform interior sampling from trapezoids. An inaccessible earlier general polygon formula and older specialty literature remain historical-priority risks; independent external priority assessment has not been undertaken.

## Limitations

The result requires independent uniform area sampling, exact population moments, and a nondegenerate planar convex trapezoid. It reconstructs only the affine base-length ratio, not Euclidean side lengths or height. It does not supply statistical error bars or a similar ordering theorem for arbitrary convex quadrilaterals. At the two endpoints the inverse is only Hölder, not Lipschitz. Historical priority is provisional.

## References

1. Sheree T. Sharpe, *Random Hyperplanes of a Convex Body, Sylvester's Problem and Crofton's Formula*, arXiv:2109.05961v1 (first public 2021-09-10), https://arxiv.org/abs/2109.05961.
2. Jean-François Marckert, *Around Sylvester's Question in the Plane*, arXiv:1511.03658v1 (first public 2015-11-11), https://arxiv.org/abs/1511.03658.
3. Christian Buchta, *Zufallspolygone in konvexen Vielecken*, J. Reine Angew. Math. 347 (1984), 212–220 (full text not inspected).
4. Florian Frick, Andrew Newman and Wesley Pegden, *Youden's Demon Is Sylvester's Problem*, arXiv:2407.02589v1 (first public 2024-07-02), https://arxiv.org/abs/2407.02589.
5. Eric W. Weisstein, *Polygon Triangle Picking*, MathWorld, https://mathworld.wolfram.com/PolygonTrianglePicking.html (regular-polygon first-moment benchmarks).
