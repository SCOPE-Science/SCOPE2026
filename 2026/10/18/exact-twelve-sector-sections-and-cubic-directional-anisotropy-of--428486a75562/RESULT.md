# Exact twelve-sector sections and cubic directional anisotropy of the Steinmetz tricylinder

## Finding

Let \(R>0\), and let the **tricylinder** be the centrally symmetric convex body
\[
K_R=\{(x,y,z)\in\mathbb R^3:\ x^2+y^2\le R^2,\quad x^2+z^2\le R^2,\quad y^2+z^2\le R^2\}.
\]
For every unit normal \(n\in S^2\), put \(H_n=n^\perp\) and \(A_R(n)=\operatorname{area}(K_R\cap H_n)\). The following constitute one exact central-section area profile theorem.

**(i) Elementary all-direction law.** For normals outside a finite union of great circles, the formula below gives \(A_R(n)\) as a sum of exactly twelve explicitly constructed arctangent terms; all exceptional normals are determined by its unique continuous extension. To construct the sum, intersect \(H_n\) with the six planes
\[
u_i=\sigma u_j,\qquad 1\le i<j\le3,\quad\sigma\in\{-1,+1\}.
\]
This gives twelve distinct oriented unit boundary rays \(w_1,\ldots,w_{12}\), cyclically ordered so that \(n\cdot(w_j\times w_{j+1})>0\), with \(w_{13}=w_1\). For each successive pair, put
\[
m_j=\frac{w_j+w_{j+1}}{\|w_j+w_{j+1}\|},\quad
\ell_j=\operatorname*{argmin}_{1\le i\le3}|(m_j)_i|,
\]
\[
\Delta_j=n\cdot(w_j\times w_{j+1}),\quad
D_j=w_j\cdot w_{j+1}-(w_j)_{\ell_j}(w_{j+1})_{\ell_j},\quad
k_j=|n_{\ell_j}|.
\]
Then \(k_j>0\) and
\[
\boxed{A_R(n)=\frac{R^2}{2}\sum_{j=1}^{12}\frac{\operatorname{atan2}(k_j\Delta_j,D_j)}{k_j}.}
\]
The branch of \(\operatorname{atan2}\) here is the angle in \((0,\pi)\). This is a finite elementary evaluation, not a numerical integration prescription.

**(ii) Sharp minimum.** For every normal,
\[
\boxed{A_R(n)\ge\pi R^2,}
\]
with equality if and only if the plane is one of \(x=0\), \(y=0\), and \(z=0\). Three other exact symmetry-class section evaluations, including the minimum, are
\[
A_R(e_3)=\pi R^2,\qquad
A_R\left(\frac{(1,1,0)}{\sqrt2}\right)=\sqrt2\left(1+\frac\pi2\right)R^2,
\]
\[
A_R\left(\frac{(1,1,1)}{\sqrt3}\right)=6\sqrt3\arctan\left(\frac13\right)R^2.
\]
No assertion of the global maximum is made.

**(iii) Uniform cubic angular jet.** Fix any \((p,q)\in S^1\), and define
\[
n_\delta=(\delta p,\delta q,\sqrt{1-\delta^2}),\qquad \delta\downarrow0.
\]
Uniformly over \((p,q)\in S^1\),
\[
\boxed{\frac{A_R(n_\delta)}{R^2}=\pi+\frac\pi2\delta^2-\frac43\bigl(|p|^3+|q|^3\bigr)\delta^3+O(\delta^4).}
\]
Thus the quadratic section response is isotropic at a minimizing coordinate normal, whereas the third-order response varies with the azimuth. For unit \((p,q)\), the cubic coefficient has magnitude between \(4/(3\sqrt2)\) and \(4/3\), with the extremal magnitudes attained respectively at equal-magnitude horizontal components and at a coordinate horizontal component. In particular, the section-area function has an isotropic quadratic Taylor term at each coordinate normal, **but admits no third-order Taylor polynomial there**.

## Assumptions and scope

All intersections are *ordinary Euclidean* intersections of three **infinite** equal-radius cylinders with axes meeting orthogonally at the origin. Planar area is intrinsic two-dimensional Hausdorff measure, without projected-area normalization. A generic unit normal in (i) means that its three coordinates are nonzero and that the twelve rays produced by the six pair-equality planes are distinct; these conditions exclude only finitely many great circles. Formula (iii) describes a neighborhood of any of the six coordinate normals by symmetry, at fixed \(R>0\). The theorem makes no global-maximum assertion.

## Proof

**Radial parametrization.** If \(u\in S^2\), the three cylinder inequalities for a point \(r u\) are \(r^2(1-u_i^2)\le R^2\), \(i=1,2,3\). Hence the allowed radial length is
\[
\rho_{K_R}(u)=\frac{R}{\sqrt{1-\min_i u_i^2}}.
\]
Every plane through the origin meets \(S^2\) in a unit great circle, so polar area integration yields
\[
A_R(n)=\frac{R^2}{2}\int_{S^2\cap H_n}\frac{d\theta}{1-\min_i u_i^2}.
\tag{1}
\]
The denominator is bounded below by \(2/3\), because the smallest of three squared unit coordinates is at most \(1/3\).

**Twelve elementary sectors.** The minimum \(\min_i |u_i|\) is attained by a fixed index on each open arc separated by the six pair-equality planes. A generic \(H_n\) meets their lines in exactly twelve oriented rays, which cut the entire great circle into twelve arcs. On arc \(j\), the index \(\ell_j\) defined at its midpoint is the active index throughout its interior. The pertinent cylinder bound is \(\sum_{i\ne\ell_j}x_i^2\le R^2\). Under the linear coordinate projection
\[
T_{\ell_j}:H_n\longrightarrow\mathbb R^2,\qquad
(x_1,x_2,x_3)\longmapsto(x_i)_{i\ne\ell_j},
\]
the Euclidean area Jacobian is \(|n_{\ell_j}|=k_j\). This linear isomorphism takes the radial sector into a planar circular sector of radius \(R\) bounded by \(T_{\ell_j}w_j\) and \(T_{\ell_j}w_{j+1}\). Its opening angle \(\alpha_j\in(0,\pi)\) satisfies
\[
\sin\alpha_j=\frac{k_j\Delta_j}{\|T_{\ell_j}w_j\|\|T_{\ell_j}w_{j+1}\|},\qquad
\cos\alpha_j=\frac{D_j}{\|T_{\ell_j}w_j\|\|T_{\ell_j}w_{j+1}\|}.
\]
The projected wedge's orientation can be chosen consistently; its *unoriented* area uses the positive numerator \(k_j\Delta_j\). Consequently \(\alpha_j=\operatorname{atan2}(k_j\Delta_j,D_j)\), and the area of the original wedge equals \(R^2\alpha_j/(2k_j)\). Summing proves (i).

For exceptional normals, the planar sections vary continuously in Hausdorff metric, or equivalently the integrand in (1) converges pointwise under a continuously moving orthonormal frame and stays bounded by \(3/2\). Their area is therefore the unique continuous limit of the generic formula.

**Sharp minimum and symmetry values.** Since \(\min_i u_i^2\ge0\), equation (1) gives \(A_R(n)\ge\pi R^2\). Equality requires \(\min_i u_i^2=0\) almost everywhere on the great circle, and therefore everywhere by continuity. The great circle is connected and is covered by the three coordinate great circles \(\{u_i=0\}\). If none of the three coordinates vanished identically on the plane, each intersection of the plane with \(\{u_i=0\}\) would be a pair of antipodal points, and six points could not cover a great circle. Thus one coordinate vanishes identically, so \(H_n\) is a coordinate plane. Conversely each such section is the radius-\(R\) disk.

For the face-diagonal normal, write \((x,y,z)=(t/\sqrt2,-t/\sqrt2,s)\). Its domain is \(|t|\le R\) and \(s^2+t^2/2\le R^2\), and integration gives
\[
4\int_0^R\sqrt{R^2-t^2/2}\,dt=\sqrt2\left(1+\frac\pi2\right)R^2.
\]
For the body-diagonal normal, the pair-equality rays divide the great circle into twelve congruent arcs, and on each such wedge the surviving coordinate-projection disk sector has angle \(\arctan(1/3)\) and area Jacobian \(1/\sqrt3\). Therefore the twelve equal wedge areas sum to \(6\sqrt3\arctan(1/3)R^2\).

**Uniform third-order term.** By scaling let \(R=1\). Choose an orthonormal basis of \(H_{n_\delta}\) depending smoothly on \(\delta\) and reducing to \(e_1,e_2\) at \(\delta=0\). The unit great-circle coordinate \(u(\theta,\delta)\) then has expansions uniform in \(p,q,\theta\):
\[
u_1=\cos\theta+O(\delta^2),\quad
u_2=\sin\theta+O(\delta^2),\quad
u_3=-\delta(p\cos\theta+q\sin\theta)+O(\delta^3).
\tag{2}
\]
Write \(m(\theta,\delta)=\min_i u_i^2\). Uniformly \(0\le m\le C\delta^2\), and from (1)
\[
A_1(n_\delta)=\pi+\frac12\int_0^{2\pi}m(\theta,\delta)\,d\theta+O(\delta^4).
\tag{3}
\]
The integral of \(u_3^2\) is \(\pi\delta^2+O(\delta^4)\). Away from the four angles where \(\sin\theta=0\) or \(\cos\theta=0\), the minimum \(m\) equals \(u_3^2\) for small \(\delta\). Near each of the two zeros of \(\cos\theta\), write \(s=\theta-\theta_0\); the loss \(u_3^2-m\) has local positive part
\[
\bigl(\delta^2q^2-s^2\bigr)_++O_{L^1}(\delta^4),
\]
whose integral is \(\tfrac43\delta^3|q|^3+O(\delta^4)\). The two zeros of \(\sin\theta\) similarly contribute \(\tfrac43\delta^3|p|^3\) each. In particular,
\[
\int_0^{2\pi}m\,d\theta=\pi\delta^2-\frac83\bigl(|p|^3+|q|^3\bigr)\delta^3+O(\delta^4).
\]
The remainder is uniform, since the coordinate expansions in (2), the local zero crossings, and the \(L^1\) estimates have uniformly bounded coefficients on the compact parameter circle. Inserting this into (3) proves (iii). Finally, \(|p|^3+|q|^3\) ranges over \([1/\sqrt2,1]\) on \(p^2+q^2=1\), with the stated equality cases. To see the final regularity assertion, use the local tangent coordinates \(a=\delta p,b=\delta q\). The degree-three directional term becomes \(-\tfrac43(|a|^3+|b|^3)\); it is even under sign reversal in each coordinate, nonzero, and is not a homogeneous cubic polynomial. The uniform remainder therefore rules out any degree-three Taylor polynomial. It does not claim a stronger neighborhood-regularity classification.

## Verification

Run `python check_tricylinder.py` with NumPy and SciPy. The checker independently evaluates (1) by midpoint polar quadrature for 240 deterministic generic normals and by direct radial-boundary polygon reconstruction for 24 of them. It cross-checks all three symmetry-class constants and tests the predicted cubic coefficients along four tangent directions at three shrinking angular radii. The measured maximum absolute deviations between the twelve-sector expression and the independent polar or polygon methods were below \(10^{-8}\) in the recorded run. These are finite computational checks; exact validity for all directions and the asymptotic remainder are proved above, not inferred from sampling.

## Relationship to prior work

The tricylinder is classical; its volume and surface area are not claimed as new. Moore (1974) and Angell–Moore (1987) study intersections of equal cylinders; the accessible 1987 full article derives volume and surface area and illustrates orthographic *views*, not the intrinsic area of the central plane-section for arbitrary normal, nor the cubic angular jet. A later Illinois Geometry Lab report treats multidimensional volumes of intersections of cylinders. The arctangent section law, strict minimizer classification and anisotropic cubic expansion are assessed here against these actual statements, and are not deductions of the inspected volume and surface-area formulas.

## Limitations

The result is restricted to three congruent perpendicular cylinders with concurrent axes and their central plane sections. The exact twelve-sector construction requires a generic normal, with exceptional directions defined by a proven continuous limit; it is not a single non-branching closed expression for all normals. The *maximum* section area and the full distribution under uniformly random normals are not determined. The complete 1974 article and 2013 report were not materially available for full-text comparison, leaving a historical-priority risk.

## References

1. Moreton Moore, “Symmetrical Intersections of Right Circular Cylinders,” *The Mathematical Gazette* 58 (1974), 181–185. DOI: `10.2307/3615957` (accessible abstract; full text unavailable).
2. I. O. Angell and Moreton Moore, “Symmetrical Intersections of Cylinders,” *Acta Crystallographica A* 43 (1987), 244–250. DOI: `10.1107/S0108767387099501` (full text inspected; illustrations and volume calculations).
3. Lingyi Kong, Luvsandondov Lkhamsuren, Abigail Turner, Ananya Uppal, and A. J. Hildebrand, “Intersecting Cylinders: From Archimedes and Zu Chongzhi to Steinmetz and Beyond,” Illinois Geometry Lab Project Report, dated 2013-04-25 (bibliographic entry inspected; full text unavailable).
4. Eric W. Weisstein, “Steinmetz Solid,” *MathWorld*, `https://mathworld.wolfram.com/SteinmetzSolid.html` (tricylinder definition and classical volume/surface data).
