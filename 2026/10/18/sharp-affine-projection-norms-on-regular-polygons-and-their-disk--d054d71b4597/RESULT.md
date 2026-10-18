# Sharp affine projection norms on regular polygons and their disk-limit excess

## Finding
Let \(P_n\) be the regular \(n\)-gon inscribed in the Euclidean unit circle, \(n\ge 3\), with uniform area probability measure \(\mu_n\). Let \(\Pi_n\) be the \(L^2(\mu_n)\)-orthogonal projector onto the complex or real affine polynomials \(\operatorname{span}\{1,x,y\}\). Its two endpoint norms coincide, and for every \(n\ge3\) they admit the *exact finite polygon-cap formula*
\[
\|\Pi_n\|_{L^1\to L^1}=\|\Pi_n\|_{L^\infty\to L^\infty}
=1-\frac{2}{|P_n|}\left(|W_n|+\kappa_n\int_{W_n}y_1\,dy\right),
\qquad \kappa_n=\frac{12}{1+2\cos^2(\pi/n)},\quad
W_n=P_n\cap\{y:y_1<-1/\kappa_n\}.
\]
The cap's area and first moment are computable by finitely many explicitly specified line-segment intersections and shoelace sums (below); this is an exact closed finite algorithm for every dimension parameter, with no quadrature or limiting operation. In particular, the endpoint norms for the triangle, square and hexagon are \(19/8\), \(233/108\), and \(361/180\), respectively; these low-order evaluations are illustrations, not a priority claim.

The nontrivial disk-limit correction is sharp:
\[
\boxed{\displaystyle
\|\Pi_n\|_{L^\infty\to L^\infty}
=\frac{16\arcsin(1/4)+11\sqrt{15}}{8\pi}
+\frac{5\pi\sqrt{15}}{12n^2}+O(n^{-4}),\qquad n\longrightarrow\infty.}
\]
In particular, the regular polygonal affine least-squares projection is strictly less stable in the uniform norm than its disk counterpart for all sufficiently large finite side counts. The coefficient is unchanged for \(L^1\) by kernel symmetry. No statement of monotonicity for all side counts is asserted.

## Assumptions and scope
All polygons are convex, centered at the origin, use **area measure** (not boundary or vertex counting measure), and have unit circumradius. The affine projection is the linear orthogonal projector in \(L^2(\mu_n)\), not a nonlinear metric projection onto a polygon, a degree-growing polynomial interpolant, or a boundary Fourier projector. Operator norms refer to spaces of equivalence classes of real- or complex-valued measurable functions. Define \(v_j=(\cos(2\pi j/n),\sin(2\pi j/n))\) for \(j=0,\ldots,n-1\), listed counterclockwise. The disk \(D=\{y\in\mathbb R^2:|y|\le1\}\) carries uniform area probability measure, and \(\Pi_D\) denotes its degree-one \(L^2\) projector. All asymptotic constants are absolute.

## Proof
**1. Covariance and reproducing kernel.** Rotational and reflection symmetries give \(\mathbb E_{\mu_n}Y=0\) and \(\mathbb E_{\mu_n}(YY^{\mathsf T})=\sigma_n^2I_2\). Triangulate from the origin into congruent triangles with consecutive unit vertices \(a,b\), satisfying \(a\cdot b=\cos(2\pi/n)\). The uniform-triangle moment is \(\mathbb E|Y|^2=(|a|^2+|b|^2+a\cdot b)/6\); consequently
\[
\sigma_n^2=\frac{2+\cos(2\pi/n)}{12}=\frac{1+2\cos^2(\pi/n)}{12},
\qquad K_n(x,y)=1+\frac{x\cdot y}{\sigma_n^2}=1+\kappa_n x\cdot y.
\]
Thus \((\Pi_nf)(x)=\int_{P_n}K_n(x,y)f(y)\,d\mu_n(y)\).

**2. Sharp finite norm.** The endpoint Lebesgue function \(H_n(x)=\int_{P_n}|1+\kappa_nx\cdot y|\,d\mu_n(y)\) is convex and continuous as a function of \(x\), and a convex function on a polygon is bounded above by its maximum at the vertices. Rotational symmetry makes \(H_n(v_j)\) independent of \(j\); use \(v_0=(1,0)\). Equality of the operator norm and maximum Lebesgue function follows by choosing an essentially bounded input of the appropriate sign/phase of the kernel. The integral kernel is symmetric, hence the adjoint calculation gives the same exact \(L^1\) norm. Because \(\int K_n(v_0,y)\,d\mu_n(y)=1\), separating the negative cap \(W_n\) gives the asserted exact formula.

To specify the finite cap calculation, clip the cyclic list \(v_0,\ldots,v_{n-1}\) against the vertical half-plane \(y_1\le -1/\kappa_n\), adding each interior original vertex and each transversal intersection \(v_j+t(v_{j+1}-v_j)\) with \(t=(-1/\kappa_n-(v_j)_1)/((v_{j+1})_1-(v_j)_1)\). Write the resulting cyclic clipped vertices as \(w_i=(a_i,b_i)\) and \(\Delta_i=a_ib_{i+1}-a_{i+1}b_i\), with indices cyclic. Then
\[
|W_n|=\frac12\sum_i\Delta_i,\qquad
\int_{W_n}y_1\,dy=\frac16\sum_i(a_i+a_{i+1})\Delta_i,
\qquad |P_n|=\frac n2\sin(2\pi/n).
\]
All quantities are exact expressions in elementary trigonometric numbers for every integer \(n\ge3\). Degenerate cap-boundary vertices may be retained or suppressed without changing the shoelace sums.

**3. A second-order polygon-to-disk cancellation lemma.** Write \(h=\pi/n\) and \(s_h=1-h^2/3\). In the angular cell centered at the outward side normal \(\beta_j=(2j+1)h\), put \(\phi=\beta_j+\delta\), \(|\delta|\le h\). The polygon radial boundary is \(R_n(\phi)=\cos h/\cos\delta\). Taylor's formula, uniformly in the cell, yields
\[
R_n(\phi)-s_h=\frac12\left(\delta^2-\frac{h^2}{3}\right)+O(h^4).
\]
The leading displayed term has zero cell average and zero first angular moment, because it is even with mean zero on \([-h,h]\). Hence if a family \(G_h\) on the circle has uniformly bounded sup norm and uniform piecewise \(C^2\) bounds away from a bounded number of corners, while remaining globally Lipschitz, then
\[
\int_0^{2\pi}\bigl(R_n(\phi)-s_h\bigr)G_h(\phi)\,d\phi=O(h^4).
\]
Indeed, in ordinary cells, subtract the linear Taylor polynomial of \(G_h\) at \(\beta_j\), leaving \(O(\delta^2)\); multiplying the \(O(h^2)\) zero-moment factor and integrating gives \(O(h^5)\) per cell and \(O(h^4)\) altogether. At each of the boundedly many exceptional cells, subtract only the center value, use the Lipschitz bound \(O(h)\), and obtain \(O(h^4)\) per exceptional cell. The uniform \(O(h^4)\) remainder in the radial formula also integrates to \(O(h^4)\). This calculation holds for all sufficiently large \(n\).

**4. Apply the cancellation to the absolute affine kernel.** The integral function \(F_h(y)=|1+\kappa_n y_1|\) is uniformly Lipschitz. Its restriction to the circle is continuous and piecewise smooth with at most two corners, uniformly bounded derivatives between corners. Polar integration and the previous lemma therefore imply
\[
\int_{P_n}F_h(y)\,dy=\int_{s_hD}F_h(y)\,dy+O(h^4).
\]
For rigor, subtract the two radial primitives: the difference is \((R_n-s_h)F_h(e^{i\phi})+O(h^4)\) uniformly, since \(R_n,s_h=1+O(h^2)\) and \(F_h\) is uniformly Lipschitz. The same argument for the constant function gives \(|P_n|=\pi s_h^2+O(h^4)\). Moreover
\[
\kappa_n=4+\frac83h^2+O(h^4)
=\frac4{s_h^2}+O(h^4).
\]
Consequently, if \(L_D(r)=\pi^{-1}\int_D|1+4r z_1|\,dz\), then
\[
\|\Pi_n\|=L_D(1/s_h)+O(h^4).
\]
The disk marginal of its first coordinate is \(\frac2\pi\sqrt{1-x^2}\) on \([-1,1]\). Direct integration (splitting at \(-1/4\)) yields
\[
L_D(1)=\frac{16\arcsin(1/4)+11\sqrt{15}}{8\pi},
\qquad L_D'(1)=\frac{5\sqrt{15}}{4\pi}.
\]
As \(1/s_h=1+h^2/3+O(h^4)\), Taylor expansion gives
\[
L_D(1/s_h)=L_D(1)+\frac{5\sqrt{15}}{12\pi}h^2+O(h^4)
=L_D(1)+\frac{5\pi\sqrt{15}}{12n^2}+O(n^{-4}).
\]
The strictly positive correction establishes the claimed eventual strict norm excess, completing the proof.

## Verification
The accompanying standalone `verify.py` uses only Python's standard library. Its shoelace cap computation follows Step 2, while an independent Simpson-rule polar integral follows the radial boundary formula from Step 3 without polygon clipping. It compares sixteen separate polygon cases, checks the exact triangle/square/hexagon rational values and numerically tests the coefficient at seven larger side counts. These are finite regression checks; the all-\(n\) assertions and the error term follow analytically from the preceding arguments.

## Relationship to prior work
Dunkl's 1987 study constructs orthogonal polynomial families with *area measure on the regular hexagon*, but its accessible abstract and bibliographic record do not state this arbitrary-\(n\) sharp endpoint norm family or the disk-limit excess coefficient; the full text could not be examined. Li, Sun and Xu (2007) study discrete Fourier analysis, trigonometric interpolation and cubature on a hexagon and triangle, including a Lebesgue estimate as **polynomial degree** grows; this is a different projection and asymptotic parameter. Hangelbroek, Narcowich, Sun and Ward (2010) prove uniform bounds for \(L^2\) projectors onto kernel spaces on manifolds, not this planar volume projector's sharp constant. Dai and Xu (2010) and Li and Xu (2013) study sphere/ball Sobolev and spectral polynomial approximation, rather than the regular-polygon all-\(n\) endpoint constants. A previously known disk affine-projector norm supplies the leading baseline, and earlier simplex/cube/cross-polytope evaluations address different domains. Neither these earlier exact values nor the elementary kernel formula alone specifies the sharp coefficient of the polygonal approximation error without the angular cancellation argument above.

## Limitations
The claims concern only *degree-one* area-orthogonal projection on *regular inscribed planar polygons*, with the disk as the limit; they do not address higher polynomial degree, arbitrary irregular polygons, nonuniform weights, or interior \(L^p\) norms. The error term is asymptotic and no universal finite-\(n\) monotonicity is claimed. The finite-shoelace formula gives an algorithm rather than a single simple closed expression free of the side count. An older hexagonal least-squares source was available only as an abstract, and an equivalent historical treatment under other terminology remains possible; independent historical-priority review is outstanding.

## References
1. C. F. Dunkl, *Orthogonal Polynomials on the Hexagon*, SIAM Journal on Applied Mathematics **47** (1987), 343–351, DOI: 10.1137/0147022. Accessible abstract; full text not inspected.
2. H. Li, J. Sun and Y. Xu, *Discrete Fourier Analysis, Cubature and Interpolation on a Hexagon and a Triangle*, arXiv:0712.3093, first publicly posted 2007-12-19.
3. T. Hangelbroek, F. J. Narcowich, X. Sun and J. D. Ward, *Kernel Approximation on Manifolds II: The \(L_\infty\)-norm of the \(L_2\)-projector*, arXiv:1005.2424, posted 2010-05-13.
4. F. Dai and Y. Xu, *Polynomial Approximation in Sobolev Spaces on the Unit Sphere and the Unit Ball*, arXiv:1011.2819, posted 2010-11-12.
5. H. Li and Y. Xu, *Spectral Approximation on the Unit Ball*, arXiv:1310.2283, posted 2013-10-08.
