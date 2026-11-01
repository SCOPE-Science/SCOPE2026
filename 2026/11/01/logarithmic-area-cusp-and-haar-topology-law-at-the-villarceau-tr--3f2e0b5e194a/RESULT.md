# Logarithmic area cusp and Haar topology law at the Villarceau transition

## Finding
For a solid ring torus with major radius \(R>r>0\), let \(B_\beta\) be its central planar section by a plane inclined through \(\beta\in[0,\pi/2]\) to the equatorial plane, and write \(A(\beta)=\operatorname{area}(B_\beta)\). The critical Villarceau angle is \(\beta_*=\arcsin(r/R)\), and the critical area is
\[
A_* =4r\sqrt{R^2-r^2}+4R^2\arcsin(r/R).
\]
The function \(A\) is continuous and strictly decreasing from \(4\pi Rr\) to \(2\pi r^2\). At the critical angle it has the precise two-sided singular expansion
\[
A(\beta)=A_*+4(R^2-r^2)(\beta-\beta_*)\log|\beta-\beta_*|+O_{R,r}(|\beta-\beta_*|).
\]
In particular, its derivative tends to negative infinity on both sides of \(\beta_*\), with the same explicit logarithmic coefficient.

The generic section is an annulus for \(\beta<\beta_*\) and the disjoint union of two topological disks for \(\beta>\beta_*\). If \(\beta\) is the inclination of a Haar-uniform unoriented central plane, then
\[
\Pr(B_\beta\text{ is annular})=1-\sqrt{1-(r/R)^2},\qquad
\Pr(B_\beta\text{ has two components})=\sqrt{1-(r/R)^2}.
\]
For its area \(X=A(\beta)\), the probability density \(f_X\) vanishes at the interior critical area at the exact logarithmic rate
\[
\lim_{a\to A_*}f_X(a)\left|\log\left(\frac{|a-A_*|}{R^2}\right)\right|
=\frac{r/R}{4(R^2-r^2)}.
\]
The density limit is two-sided; the isolated critical plane has probability zero.

## Assumptions and scope
The solid torus is
\[
T_{R,r}=\left\{(x,y,z)\in\mathbb R^3:\left(\sqrt{x^2+y^2}-R\right)^2+z^2\le r^2\right\},\qquad 0<r<R.
\]
A central section means intersection of this *solid* with a plane through the origin, with ordinary Euclidean two-dimensional area intrinsic to that plane. All probabilities refer to the unique rotation-invariant law on *unoriented* central planes. The logarithms use dimensionless arguments when applied to lengths or areas. No statement is made for spindle or horn tori, offset planes, noncircular generating profiles, or arbitrary noncentral sections.

## Proof
**Radial normal form.** Rotational symmetry lets the plane be parametrized by
\[
(x,y,z)=(u\cos\beta,v,u\sin\beta),\qquad (u,v)=\rho(\cos\varphi,\sin\varphi).
\]
Put \(s=\sin\beta\) and \(h(\varphi)=\sqrt{1-s^2\cos^2\varphi}\). Substitution into the torus inequality yields
\[
\rho^2-2R h(\varphi)\rho+R^2-r^2\le0.
\]
The radial endpoints, whenever they exist, are
\[
\rho_\pm(\varphi)=Rh(\varphi)\pm\sqrt{r^2-R^2s^2\cos^2\varphi}.
\]
Both endpoints are strictly positive, since \((Rh)^2-(r^2-R^2s^2\cos^2\varphi)=R^2-r^2>0\). Thus every admissible angular ray intersects the section in a closed radial interval disjoint from the origin.

**Topology and Haar probability.** If \(Rs<r\), the radical is positive for every angle, and the radial intervals form a continuous annulus. If \(Rs>r\), the admissible angles consist of precisely two disconnected closed arcs around \(\pi/2\) and \(3\pi/2\); at their endpoints the radial intervals collapse to points. Each component is a topological disk. The transition \(Rs=r\) is the double-tangent Villarceau plane. Since \(|n_z|=\cos\beta\) is uniform on \([0,1]\) for a Haar-uniform unoriented plane normal \(n\), \(\beta\) has density \(\sin\beta\) on \([0,\pi/2]\); the stated topology probabilities follow by integrating at \(\beta_*\).

**Exact area integral and critical value.** Integrating the radial intervals gives
\[
A(\beta)=2R\int_0^{2\pi}\sqrt{1-s^2\cos^2\varphi}\,\sqrt{\bigl(r^2-R^2s^2\cos^2\varphi\bigr)_+}\,d\varphi.
\tag{1}
\]
The formula shows strict decrease in \(s\in[0,1]\): both nonnegative factors are pointwise nonincreasing, with strict decrease on a positive-measure set for distinct \(s\). At the two endpoints the sections are an annulus of area \(4\pi Rr\) and two disks of total area \(2\pi r^2\). At \(s=r/R\), the second factor becomes \(r|\sin\varphi|\). An elementary substitution \(t=\cos\varphi\) in each quadrant gives
\[
A_*=8Rr\int_0^1\sqrt{1-(r/R)^2t^2}\,dt
=4r\sqrt{R^2-r^2}+4R^2\arcsin(r/R).
\]

**Logarithmic saddle coefficient.** Set \(\delta=r^2-R^2\sin^2\beta\), and write the integrand in (1) as
\[
2R\sqrt{1-\frac{r^2-\delta}{R^2}\cos^2\varphi}\;
\sqrt{\bigl(r^2\sin^2\varphi+\delta\cos^2\varphi\bigr)_+}.
\tag{2}
\]
Away from \(\varphi=0,\pi\) this is continuously differentiable in \(\delta\) near zero and contributes only \(O_{R,r}(\delta)\) to the area difference. Near either exceptional angle \(\varphi_0\), put \(t=\varphi-\varphi_0\). The first factor tends to \(c=\sqrt{1-(r/R)^2}\), and the singular model for the remaining integral is \(\sqrt{(r^2t^2+\delta)_+}\). With any fixed small cutoff \(\eta>0\), direct integration on \([-\eta,\eta]\) gives, on both sides of zero,
\[
J(\delta):=\int_{-\eta}^{\eta}\sqrt{(r^2t^2+\delta)_+}\,dt
=J(0)-\frac{\delta}{2r}\log\frac{|\delta|}{r^2}+O_{r,\eta}(\delta).
\tag{3}
\]
For \(\delta>0\) this follows from the antiderivative involving \(\operatorname{arsinh}(r\eta/\sqrt\delta)\); for \(\delta<0\) it follows from \(\operatorname{arcosh}(r\eta/\sqrt{-\delta})\), with the integral starting at \(|t|=\sqrt{-\delta}/r\). Replacing the smooth factor and the local trigonometric functions by their values and quadratic terms changes the area difference by \(O_{R,r}(\delta)\): the remainders have factors bounded by \(C(|\delta|+t^2)\) and their singular integrated changes are at worst \(O(\delta)\). Differentiating the same subtracted-integrand estimates for \(\delta\ne0\) bounds the derivative of this remainder by \(O_{R,r}(1)\). There are two exceptional angles. Combining (2) and (3) therefore yields
\[
A(\beta)-A_*=-\frac{2Rc}{r}\,\delta\log\frac{|\delta|}{r^2}+O_{R,r}(\delta),\qquad
\frac{dA}{d\delta}=-\frac{2Rc}{r}\log\frac{|\delta|}{r^2}+O_{R,r}(1).
\tag{4}
\]
Since \(\delta=-2Rrc(\beta-\beta_*)+O_{R,r}((\beta-\beta_*)^2)\), this gives
\[
A(\beta)-A_*=4(R^2-r^2)(\beta-\beta_*)\log|\beta-\beta_*|+O_{R,r}(|\beta-\beta_*|),
\]
and \(A'(\beta)=4(R^2-r^2)\log|\beta-\beta_*|+O_{R,r}(1)\). Thus the derivative tends to \(-\infty\) from both sides.

**Haar section-area density.** Strict monotonicity and the normal-density formula imply, for noncritical interior values,
\[
f_X(A(\beta))=\frac{\sin\beta}{|A'(\beta)|}.
\]
The previous asymptotics give \(|A'(\beta)|\sim4(R^2-r^2)|\log|\beta-\beta_*||\). Also \(|A(\beta)-A_*|\asymp|\beta-\beta_*||\log|\beta-\beta_*||\), so the logarithms of these distances have the same leading magnitude. Taking the limit yields the claimed vanishing-density coefficient. This also shows \(A_*\) lies strictly inside the support \([2\pi r^2,4\pi Rr]\).

## Verification
A standalone checker `check.py` evaluates (1) using high-precision quadrature and independently estimates the section area by a grid in orthonormal plane coordinates. For \((R,r)=(2,1),(3,2),(5,1)\) it checks the two endpoint identities and critical area, estimates the logarithmic coefficient by symmetric differences at two scales, and checks twelve noncritical areas against independent raster integration. Execution command: `python check.py` (requires `numpy`, `mpmath`). All checks passed at the packaged precision. These finite tests are not substituted for the universal analytic arguments above.

## Relationship to prior work
The Villarceau double-tangent plane, its two circular boundary components, and the classical geometry of toric sections predate this note. García Monera and Monterde (2011) give the exact double-tangent inclination and a planar geometric construction from the resulting circular arcs (particularly their Sections 2–4). Moroni's account provides equations of general toric sections and the classical classification of their special circles. These sources do not state a two-sided logarithmic *solid-section area* expansion or the associated Haar-area density limit. The new calculation is specifically the quantitative saddle coefficient and its induced probability law; the basic tangency and circular intersection are **not** claimed as new. It differs also from results on orthogonal *shadows* of solid tori: a projected silhouette and a central planar intersection have different sets, statistics, and singular mechanisms.

## Limitations
The result concerns a circular ring torus of fixed positive radii, and centered planes only. The criticality is a two-sided local asymptotic for each fixed \(0<r<R\); no uniformity as \(r/R\) approaches zero or one is asserted. The isolated singular plane and the ordinary endpoint cases are excluded from assertions about the density. The mathematical proof is not an independent external audit. Possible earlier area calculations in older stereological, geometric-design, or special-function literature remain a historical-priority risk.

## References
1. M. García Monera and J. Monterde, *Building a Torus with Villarceau Sections*, Journal for Geometry and Graphics **15** (2011), 93–99, especially Sections 2–4. https://www.heldermann-verlag.de/jgg/jgg15/j15h1mone.pdf
2. L. Moroni, *The toric section: intersection of a torus with a plane* (online mathematical exposition, 2017). https://www.lucamoroni.it/toric-sections/
3. C. Tomé, *Las circunferencias de Villarceau*, Cuaderno de Cultura Científica (27 May 2015), historical bibliography and elementary geometry. https://culturacientifica.com/2015/05/27/las-circunferencias-de-villarceau/
4. M. Macho Stadler, *El toro visto por Villarceau*, ZTFNews (26 November 2011), direct day-precise archived supporting source. https://ztfnews.wordpress.com/2011/11/26/el-toro-visto-por-villarceau/
5. A. Breda, A. Trocado and J. Dos Santos, *Topological Properties of the Intersection Curves Between a Torus and Families of Parabolic or Elliptical Cylinders*, Axioms **13** (2024), 852. This concerns quadric-cylinder intersections, not random central planar area. https://doi.org/10.3390/axioms13120852
