# The exact random-brightness law and logarithmic saddle for a cubic constant-width body

## Finding
For \(0<|\varepsilon|\le 1/4\), let \(K_\varepsilon\subset\mathbb R^3\) have spherical support function
\[
h_\varepsilon(u)=1+\varepsilon u_1u_2u_3,\qquad u\in S^2.
\]
It is a smooth strictly convex body of width \(2\). Let \(U\) be Haar-uniform on \(S^2\), let \(b_\varepsilon(U)\) be the area of the orthogonal projection to \(U^\perp\), and put
\[
Y=\frac{4}{\pi\varepsilon^2}(\pi-b_\varepsilon(U))=\prod_{i=1}^3(1-U_i^2).
\]
Define, for \(0\le s\le1\),
\[
A(s)=s^2(1-s^2),\quad B(s)=\frac{(1-s^2)^3}{4},\quad T(s)=A(s)+B(s)=\frac{(1-s^2)(1+s^2)^2}{4},
\]
and the extended arcsine distribution function
\[
G(v)=\begin{cases}0&v\le0,\\\frac2\pi\arcsin\sqrt v&0<v<1,\\1&v\ge1.\end{cases}
\]
Then \(Y\) has support exactly \([0,8/27]\), and its **entire cumulative distribution function** is
\[
\boxed{F_Y(y)=\int_0^1 G\!\left(\frac{y-A(s)}{B(s)}\right)\,ds\quad(0\le y\le8/27).} \tag{1}
\]
Here the integrand at \(s=1\) may be assigned arbitrarily; it is a measure-zero point. Outside the support the CDF is \(0\) or \(1\), respectively. For \(0<y<8/27\) with \(y\ne1/4\), the density is
\[
\boxed{f_Y(y)=\frac1\pi\int_{\{0<s<1:A(s)<y<T(s)\}}\frac{ds}{\sqrt{(y-A(s))(T(s)-y)}}.} \tag{2}
\]
The unique interior critical value is \(y_*=1/4\). **The density has a two-sided logarithmic divergence with exact coefficient**
\[
\boxed{f_Y(y)=\frac6\pi\log\frac1{|y-1/4|}+O(1)\quad\text{as }y\to(1/4)^\pm.} \tag{3}
\]
Its endpoint laws are
\[
F_Y(y)=\frac32y+o(y)\quad(y\downarrow0),\qquad
1-F_Y(8/27-\delta)=\frac92\delta+o(\delta)\quad(\delta\downarrow0). \tag{4}
\]
Moreover,
\[
\boxed{\mathbb EY=\frac4{21},\quad\mathbb EY^2=\frac{128}{3003},\quad\operatorname{Var}(Y)=\frac{400}{63063}.} \tag{5}
\]
All these normalized expressions are independent of the nonzero admissible parameter \(\varepsilon\). In contrast, the previously evaluated axially symmetric cubic family has no interior logarithmic singularity in its random-brightness density.

## Assumptions and scope
The projection is orthogonal Euclidean projection, not a central plane section. Normals are sampled with the normalized rotation-invariant probability measure \(d\sigma/(4\pi)\). A convex body is identified by its support function. The amplitude range \(0<|\varepsilon|\le1/4\) is a convenient strictly convex subrange, not asserted to be the largest possible range. The distribution at \(\varepsilon=0\) is a point mass at \(\pi\) for unnormalized brightness and the division defining \(Y\) is intentionally omitted there. Equations (1)--(5) are exact for all nonzero parameters in the stated range, not small-amplitude asymptotics.

## Proof
**Convexity and brightness input.** Set \(P(u)=u_1u_2u_3\). For any unit tangent vector \(v\perp u\), homogeneity gives
\[
(\nabla_{S^2}^2P+PI)(v,v)=v^T(\nabla^2_{\mathbb R^3}P)(u)v-2P(u).
\]
The Euclidean Hessian has off-diagonal entries \(u_1,u_2,u_3\) and zero diagonal. Its Frobenius norm is \(\sqrt2\); also \(|P(u)|\le1/(3\sqrt3)\). Consequently the support-curvature tensor of \(1+\varepsilon P\) is uniformly positive definite when \(|\varepsilon|(\sqrt2+2/(3\sqrt3))<1\), which holds throughout the displayed range. The oddness of \(P\) gives constant width two.

For a unit projection normal \(n\), restrict the support function to the great circle \(n^\perp\). Its nontranslation Fourier component is a third harmonic of squared amplitude \(\varepsilon^2\prod_i(1-n_i^2)/16\). The planar support-area identity \(\tfrac12\int_0^{2\pi}(h^2-h'^2)\,d\theta\) therefore gives
\[
b_\varepsilon(n)=\pi-\frac{\pi\varepsilon^2}{4}\prod_{i=1}^3(1-n_i^2). \tag{6}
\]
This exact pointwise brightness formula is **previously published** and is used as input rather than claimed anew.

**Full distribution and density.** Write \(U=(\sqrt{1-Z^2}\cos\Phi,\sqrt{1-Z^2}\sin\Phi,Z)\), where \(Z\) is uniform on \([-1,1]\) and \(\Phi\) is independent and uniform on \([0,2\pi]\). Then \(S=|Z|\) is uniform on \([0,1]\) and direct multiplication yields
\[
Y=A(S)+B(S)\sin^2(2\Phi).
\]
The variable \(\sin^2(2\Phi)\) is beta-distributed with parameters \((1/2,1/2)\), hence has CDF \(G\) and density \(1/(\pi\sqrt{v(1-v)})\). Conditioning on \(S=s\) proves (1), and differentiating away from critical values gives (2). Since \(T'(s)=\tfrac{s}{2}(1+s^2)(1-3s^2)\), its maximum is \(T(1/\sqrt3)=8/27\). Every value between zero and this maximum is attained and has positive probability in every interior neighborhood.

**Critical-point census and the logarithm.** Set \(x_i=U_i^2\), so \(x_1+x_2+x_3=1\) and
\[
Y=x_1x_2+x_2x_3+x_3x_1-x_1x_2x_3.
\]
On the interior simplex, subtracting two partial derivatives gives \((x_j-x_i)(1-x_k)\), so the unique interior stationary point has all \(x_i=1/3\). This gives eight maxima on the sphere. The three simplex vertices correspond to six minima with \(Y=0\). On each open simplex edge, the only stationary point is its midpoint, producing four sign choices on each of three coordinate-zero great circles: exactly twelve nondegenerate saddle points, all with \(Y=1/4\). There are no other critical points.

At any such saddle, after sign and coordinate permutations, use local spherical coordinates \(U=(\sqrt{1-w^2}\cos(\pi/4+\alpha),\sqrt{1-w^2}\sin(\pi/4+\alpha),w)\). Expansion of the exact formula gives
\[
Y=\frac14+\frac{w^2}{4}-\alpha^2+O((|w|+|\alpha|)^3),
\]
while Haar area is \(d\alpha\,dw/(4\pi)\). The smooth Morse lemma reduces the local function exactly to \(1/4+p q\), with linear first-order coordinates \(p=w/2+\alpha\) and \(q=w/2-\alpha\). Their absolute Jacobian relative to \((w,\alpha)\) is one, so the leading normalized area measure is \(dp\,dq/(4\pi)\). Integrating \(\delta(t-pq)\) over a fixed small rectangle gives \(2\log(1/|t|)+O(1)\); the variation of the smooth measure contributes only \(O(1)\). Thus every saddle contributes \((2\pi)^{-1}\log(1/|t|)+O(1)\). Multiplying by twelve proves (3). The extrema cause no additional interior divergence.

**Endpoint coefficients.** In geodesic polar coordinates centered at each of the six axis minima, \(Y=r^2+O(r^4)\); each small cap of radius \(r\) has spherical area \(\pi r^2+o(r^2)\). Hence \(F_Y(y)=(6/(4\pi))\pi y+o(y)=3y/2+o(y)\). At each of the eight diagonal maxima, \(8/27-Y=(4/9)r^2+O(r^3)\). The eight small caps give the second assertion of (4).

**Moments.** The squared coordinate triple is Dirichlet with parameters \((1/2,1/2,1/2)\), whose monomial expectation is
\[
\mathbb E\prod_i x_i^{k_i}=\frac{\prod_i(1/2)_{k_i}}{(3/2)_{k_1+k_2+k_3}}.
\]
Expanding the polynomial \(x_1x_2+x_2x_3+x_3x_1-x_1x_2x_3\), and its square, yields \(4/21\) and \(128/3003\); subtraction gives the displayed variance. This completes the proof.

## Verification
The accompanying standalone Python file `verify.py` symbolically evaluates the Dirichlet moments, checks the factorization of the conditional law and both critical values, and numerically tests the singular coefficient from density differences on both sides. It independently samples uniform spherical directions and compares four bin frequencies against the conditional CDF. The program returned `VERIFY_OK` when executed from the delivered package. Numerical quadrature and finite sampling are supplementary diagnostics; the all-direction statements, endpoint laws, and logarithmic coefficient are proved analytically above.

## Relationship to prior work
Myroshnychenko, Ryabogin and Saroglou (2026) develop nonball constant-width examples whose planar projections admit threefold symmetry. A published exact-brightness calculation subsequently evaluates the complete directional function (6) and its extremal directions; **that entire pointwise formula is prior work**. The contribution here is the Haar pushforward law (1)--(2), its logarithmic interior singularity with coefficient (3), the endpoint mass laws and exact statistical moments. In particular, specifying the directional brightness function is not the same as explicitly evaluating its pushforward density and resolving the saddle singularity.

Another published calculation evaluates the entire random-brightness law of the different *zonal* cubic harmonic; it has a one-dimensional beta transform rather than twelve saddle points and lacks the interior logarithmic transition. Abas (2026) establishes general coarea and density methods for polyhedral brightness, including specific polytope examples. Its 92-page manuscript was inspected for the present smooth cubic model without finding an evaluated matching law. The original examples and general area/density methods are not claimed as new.

## Limitations
A complete pointwise brightness formula was known before this calculation, so the density is a nontrivial evaluation of the pushforward of known data, not a new directional-projection theorem. Historical priority of the special density and singular coefficient may be uncertain under alternate terminology. The formulas concern the specific tetrahedral cubic, not all threefold-projection exceptions or general smooth constant-width bodies. The CDF is an exact one-dimensional arcsine integral rather than an elementary piecewise closed form; the density is an exact quadrature away from the logarithmic critical value. No independent mathematical audit has been performed.

## References
1. S. Myroshnychenko, D. Ryabogin, C. Saroglou, *On convex bodies with rotationally symmetric planar projections*, arXiv:2609.27192v1 (first public 2026-09-23), https://arxiv.org/abs/2609.27192.
2. *Exact brightness profile of the cubic threefold-projection exception*, published mathematical record (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-brightness-profile-of-the-cubic-threefold-projection-excep--a6ac80c263be.
3. *Exact projection-body volume and random-brightness law for axial cubic bodies*, published mathematical record (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-projection-body-volume-and-random-brightness-law-for-axial--718163d68e7d.
4. O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202v1 (first public 2026-08-10), https://arxiv.org/pdf/2609.26202.
5. R. Schneider, *Convex Bodies: The Brunn--Minkowski Theory*, second edition, Cambridge University Press, for the classical support-function curvature and area identities.
