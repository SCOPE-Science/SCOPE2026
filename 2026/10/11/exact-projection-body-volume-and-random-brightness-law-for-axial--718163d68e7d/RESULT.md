# Exact projection-body volume and random-brightness law for axial cubic bodies

## Finding
Fix a unit vector \(e\in\mathbb R^3\). For each real \(t\), consider the spherical function
\[
h_t(u)=1+t\left((u\cdot e)^3-\frac35(u\cdot e)\right),\qquad u\in S^2.
\]
It is the support function of a three-dimensional convex body \(K_t\) **if and only if** \(|t|\le\tfrac12\). All these bodies have width two, and all their orthogonal planar projections admit threefold rotational symmetry after translation. For every unit projection normal \(v\), the **exact brightness** (orthogonal projection area) is
\[
 b_t(v):=\operatorname{area}_2(K_t\mid v^\perp)
 =\pi\left[1-\frac{t^2}{4}\bigl(1-(e\cdot v)^2\bigr)^3\right]. \tag{1}
\]
Consequently, for \(0<|t|\le\tfrac12\) the brightness has directional range
\[
 \pi(1-t^2/4)\le b_t(v)\le\pi,
\]
with equality on the left precisely at \(v\perp e\), and on the right precisely at \(v=\pm e\). The **sharp ratio of largest to smallest brightness within this axial family** is
\[
 \frac{\max_v b_t(v)}{\min_v b_t(v)}\le\frac{16}{15},
\]
and equality occurs exactly when \(|t|=\tfrac12\). No upper bound for a larger family of convex bodies is claimed.

For a uniform random direction \(V\in S^2\), when \(t\ne0\) define the normalized random brightness deficit
\[
Y_t:=\frac{4}{\pi t^2}\bigl(\pi-b_t(V)\bigr).
\]
Its complete distribution is **independent of both \(t\) and the axis \(e\)**:
\[
\mathbb P(Y_t\le y)=
\begin{cases}
0,&y<0,\\
1-\sqrt{1-y^{1/3}},&0\le y\le1,\\
1,&y>1,
\end{cases}
\qquad
 f_{Y_t}(y)=\frac{1}{6y^{2/3}\sqrt{1-y^{1/3}}}\quad(0<y<1). \tag{2}
\]
Thus the law of the unnormalized random brightness identifies \(|t|\) within this family when \(t\ne0\); it cannot distinguish \(t\) from \(-t\), since those bodies are reflections. The **projection body** \(\Pi K_t\) is the centrally symmetric convex body whose support function equals the brightness \(b_t(v)\). Its volume has the exact sharp profile
\[
\operatorname{vol}_3(\Pi K_t)=\frac{4\pi^4}{3}\left(1-\frac{12t^2}{35}-\frac{32t^4}{1001}+\frac{640t^6}{46189}\right). \tag{3}
\]
This volume is strictly decreasing with \(|t|\) over \(0<|t|\le\tfrac12\); its sharp ratio to the unit-ball projection-body volume is \(1475168/1616615\) at \(|t|=\tfrac12\). The accompanying exact intrinsic quantities are
\[
\operatorname{area}_2(\partial K_t)=4\pi-\frac{16\pi}{35}t^2,
\qquad
\operatorname{vol}_3(K_t)=\frac{4\pi}{3}-\frac{16\pi}{35}t^2. \tag{4}
\]
At \(t=0\), the body is the unit ball, brightness is identically \(\pi\), and \(Y_t\) is intentionally undefined; formulas (1), (3), and (4) still apply.

## Assumptions and scope
The parameter is real, the axis \(e\) is a Euclidean unit vector, and \(S^2\) is equipped with the normalized uniform distribution only in the probabilistic statement. Convex body means compact, convex, and with nonempty interior. All formulas include the curvature-degenerate endpoint \(|t|=\tfrac12\). The axis is arbitrary but fixed before the projection direction varies; the term \((u\cdot e)^3-3(u\cdot e)/5\) is the unique rotationally invariant real spherical harmonic of degree three about \(e\), up to scaling. Here \(K_t\mid v^\perp\) means Euclidean orthogonal projection, not a section.

This family lies in the exceptional threefold-projection setting singled out by Myroshnychenko, Ryabogin, and Saroglou (2026). Its fixed-width normalization makes brightness anisotropy and random projection-area fluctuations intrinsic geometric quantities rather than artifacts of scale.

## Proof
**1. Exact convexity interval.** Rotate coordinates to take \(e=(0,0,1)\), and set \(z=u\cdot e\in[-1,1]\). The cubic \(P(x)=x_3^3-\tfrac35 x_3|x|^2\) is homogeneous and harmonic in \(\mathbb R^3\); its restriction to \(S^2\) is therefore a degree-three spherical harmonic. A smooth spherical function \(h\) is a convex support function if and only if its spherical curvature-radius form \(Q_h=\nabla^2_{S^2}h+hI\) is positive semidefinite everywhere. For a rotationally symmetric function \(h(z)\), the two eigenvalues of \(Q_h\), in the azimuthal and meridional directions, are respectively
\[
\rho_{\mathrm{az}}=h-zh',\qquad
\rho_{\mathrm{mer}}=h-zh'+(1-z^2)h''.
\]
The formulas extend continuously to both poles. Substituting \(h_t\) yields
\[
 \rho_{\mathrm{az}}(z)=1-2tz^3,
 \qquad \rho_{\mathrm{mer}}(z)=1+t(6z-8z^3). \tag{5}
\]
On \([-1,1]\), the absolute maximum of \(2z^3\) is \(2\). The polynomial \(6z-8z^3\) has derivative \(6-24z^2\), so its extreme values on \([-1,1]\) are among \(z=\pm1,\pm\tfrac12\), where its absolute value is exactly \(2\). Therefore both principal radii are nonnegative everywhere for \(|t|\le\tfrac12\). Conversely, at \(z=\operatorname{sgn}(t)\), the first radius equals \(1-2|t|\), so \(|t|>\tfrac12\) cannot be a support function. At \(t=\tfrac12\), the factorizations
\[
 \rho_{\mathrm{az}}=(1-z)(z^2+z+1),
 \qquad \rho_{\mathrm{mer}}=(1-z)(2z+1)^2
\]
show precisely how the support form becomes semidefinite; the case \(t=-\tfrac12\) is antipodal. The constant term ensures positive width, and the support function has a full-dimensional body throughout this interval. Because the degree-three term is odd, \(h_t(u)+h_t(-u)=2\) for all \(u\).

**2. Planar projections and their areas.** Let \(v\) be a unit normal to a projection plane \(E=v^\perp\), and put
\[
\tau=\|\operatorname{proj}_E e\|=\sqrt{1-(e\cdot v)^2}.
\]
When \(\tau>0\), choose the angle \(\theta\) in \(E\) so that \(e\cdot u=\tau\cos\theta\). The restriction of \(h_t\) to its unit circle is
\[
h_t|_E(\theta)=1+t\left(\frac{\tau^3}{4}\cos3\theta+\left(\frac{3\tau^3}{4}-\frac{3\tau}{5}\right)\cos\theta\right). \tag{6}
\]
The first Fourier harmonic is exactly a planar translation and does not affect area. Removing it gives the centered support function \(p(\theta)=1+a\cos3\theta\), where \(a=t\tau^3/4\). It is invariant under rotation by \(2\pi/3\). At \(\tau=0\), the projection is a disk and the same conclusion holds. For any planar convex body with a smooth support function \(p\), Minkowski's support-function area identity is
\[
\operatorname{area}_2=\frac12\int_0^{2\pi}\bigl(p(\theta)^2-p'(\theta)^2\bigr)\,d\theta.
\]
Using orthogonality of the first and third harmonics gives
\[
\operatorname{area}_2=\pi(1-4a^2)
=\pi\left(1-\frac{t^2\tau^6}{4}\right),
\]
which proves (1), including \(\tau=0\), and its sharp extrema and ratio. Since \(0\le\tau\le1\) and \(|t|\le\tfrac12\), the smallest admissible area is \(15\pi/16\).

**3. Distribution of random projection areas.** If \(V\) is uniformly distributed on \(S^2\), then \(Z=e\cdot V\) is uniformly distributed on \([-1,1]\). By (1), for \(t\ne0\),
\[
Y_t=(1-Z^2)^3.
\]
For \(0\le y\le1\), the event \(Y_t\le y\) is equivalent to \(|Z|\ge\sqrt{1-y^{1/3}}\). Uniformity of \(Z\) gives (2) immediately. Differentiation yields the density, which has integrable endpoint singularities and integrates to one. The endpoints of the unnormalized brightness distribution are \(\pi(1-t^2/4)\) and \(\pi\), so its support determines \(|t|\), whereas \(t\mapsto-t\) is reflection through the origin in this odd-harmonic family.

**4. Intrinsic volumes.** With \(h=h_t\), the surface area is \(\int_{S^2}\det Q_h\,d\sigma\) and volume is \(\tfrac13\int_{S^2} h\det Q_h\,d\sigma\). The curvature formula from Step 1 yields
\[
\det Q_h=(1-2tz^3)(1+t(6z-8z^3)),
\]
and all odd powers of \(z\) integrate to zero. Evaluating even moments \(\tfrac12\int_{-1}^1 z^{2j}\,dz=1/(2j+1)\) gives (4). Independently, the mean of (1) over the sphere equals \(\pi(1-4t^2/35)\) because \(\mathbb E(1-Z^2)^3=16/35\); Cauchy's projection formula then gives the same surface area. Both routes apply to the endpoint bodies by the smooth-support integral identities or approximation from the interior.

**5. Exact projection-body volume and its sharp endpoint.** The Cauchy projection-body construction gives a centrally symmetric convex body \(\Pi K_t\) whose support function on \(S^2\) is \(b_t\). For \(z=e\cdot v\), put \(k=t^2/4\) and \(q(z)=1-k(1-z^2)^3\), so \(b_t(v)=\pi q(z)\). Its azimuthal and meridional curvature radii are \(\pi(q-zq')\) and \(\pi(q-zq'+(1-z^2)q'')\), respectively. Applying the support-function volume identity gives
\[
\frac{3\operatorname{vol}_3(\Pi K_t)}{2\pi^4}
=\int_{-1}^1 q(z)\bigl(q(z)-zq'(z)\bigr)\bigl(q(z)-zq'(z)+(1-z^2)q''(z)\bigr)\,dz
=2-\frac{96k}{35}-\frac{1024k^2}{1001}+\frac{81920k^3}{46189}.
\]
Substituting \(k=t^2/4\) proves (3). Writing the parenthesized factor in (3) as \(W(t)\), direct differentiation yields
\[
W'(t)=\frac{8t}{1616615}\left(16800t^4-25840t^2-138567\right),
\]
which is strictly negative for \(0<t\le1/2\) since \(16800t^4\le1050<138567\). Evenness extends this to strict decrease with \(|t|\). Evaluating (3) at \(|t|=1/2\) gives \(W=1475168/1616615\), the claimed sharp endpoint ratio.


## Verification
The standalone `verify.py` checks symbolically that the defining homogeneous cubic is harmonic, derives both curvature-radius polynomials and their endpoint factorizations, checks all stationary-point values used in the sharp convexity bound, verifies the planar trigonometric decomposition and support-function area integral, and independently integrates the volume and surface-area identities. It computes the exact volume of the projection body and checks its sharp endpoint and derivative sign. It also differentiates the probability distribution and checks the expected normalized deficit \(16/35\) against the Cauchy formula. The symbolic program returned `VERIFY_OK` when run against the exact embedded file. These checks validate stated algebra; all-direction convexity and random-direction distribution are established by the analytic arguments above, not by a finite sample.

## Relationship to prior work
Myroshnychenko, Ryabogin, and Saroglou (arXiv:2609.27192v1, first public 2026-09-23) prove rigidity for fourfold or higher rotational symmetry of every planar projection and produce cubic counterexamples for threefold symmetry. Their complete fourteen-page source analyzes Fourier restrictions and the existence of such bodies but does not compute this axial family's curvature threshold, complete brightness profile, random-brightness law, or projection-body volume. A separately published threefold-projection classification covers the entire degree-three harmonic support space; it supplies a structural umbrella, not an area or probability formula. A separate published calculation obtains a sharp support-function threshold for the non-axial cubic \(u_1u_2u_3\); that different harmonic and parameter are not algebraically equivalent to the rotationally symmetric zonal cubic considered here.

Abas (arXiv:2609.26202v1, first public 2026-08-10) develops random width and brightness densities for polytopes and an inverse theory. Its public abstract advertises explicit tetrahedral and truncated-octahedral, rather than smooth axially cubic, laws. The full text was not available for substantive comparison, so the possibility of an unindexed general formula or worked example remains a bibliographic risk. The present result does not claim a general distribution theorem for all smooth constant-width bodies.

## Limitations
This is a complete result for the unique zonal **degree-three harmonic** family at width two, not a classification of all bodies with threefold-symmetric projections. The exact bound \(16/15\) and the projection-body volume endpoint are sharp only within this axial family; it is not a universal brightness anisotropy bound. The density formula is for uniform random projection directions; changing the angular sampling measure changes the law. The normalized random deficit is not defined at \(t=0\). The finite symbolic checks do not by themselves prove infinite-dimensional geometric assertions, and absolute novelty cannot be established by bibliographic searches alone.

## References
1. S. Myroshnychenko, D. Ryabogin, C. Saroglou, *On convex bodies with rotationally symmetric planar projections*, arXiv:2609.27192v1, first publicly available 2026-09-23, https://arxiv.org/abs/2609.27192.
2. O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202v1, first publicly available 2026-08-10, https://arxiv.org/abs/2609.26202.
3. R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, second edition, for classical support-function, curvature-area and projection identities.
4. *Classification of the threefold planar-projection exception in three dimensions*, published mathematical record (2026); used only for statement-level comparison.
5. *Sharp convexity threshold for the cubic constant-width support family*, published mathematical record (2026); concerns the distinct tetrahedrally symmetric cubic.
