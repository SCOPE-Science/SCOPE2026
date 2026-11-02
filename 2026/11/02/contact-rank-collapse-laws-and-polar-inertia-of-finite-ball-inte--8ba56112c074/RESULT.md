# Contact-rank collapse laws and polar inertia of finite ball intersections

## Finding

Let \(X\) be a finite collection of at least two distinct points in Euclidean \(\mathbb R^d\), \(d\ge2\), whose unique minimum enclosing ball has center \(c\) and radius \(R>0\). For \(\varepsilon>0\) consider the intersection of equal balls
\[
K_\varepsilon=\bigcap_{p\in X}\overline B(p,R+\varepsilon).
\]
Assume that all points \(p\in X\) satisfying \(\|p-c\|=R\) lie in a \(k\)-dimensional linear subspace \(L\) after translating by \(c\), and that \(0\) lies in the relative interior of their convex hull in \(L\), with \(1\le k\le d\). Put \(m=d-k\). With \(u=(p-c)/R\) ranging over these active points, form the bounded polytope
\[
P=\{z\in L: \langle u,z\rangle\ge-1\ \text{for every active }u\}.
\]
Write \(\kappa_j=\pi^{j/2}/\Gamma(1+j/2)\) for the volume of the Euclidean unit \(j\)-ball, including \(\kappa_0=1\).

**Contact-rank collapse theorem.** Under precisely these hypotheses,
\[
\boxed{\displaystyle
\lim_{\varepsilon\downarrow0}\frac{\operatorname{vol}_d(K_\varepsilon)}{\varepsilon^{(d+k)/2}}
=\operatorname{vol}_k(P)\,\kappa_m(2R)^{m/2}
\frac{\Gamma(1+m/2)\Gamma(k+1)}{\Gamma(k+1+m/2)}.}
\]
In particular, the collapse exponent is \((d+k)/2\), so the small-radius volume function determines the linear rank \(k\) of a positive-spanning active contact configuration. Each possible rank occurs in every ambient dimension \(d\).

**Full-rank polar-inertia correction.** When \(k=d\), let \(M_2(P)=\int_P\|z\|^2\,dz\). There is the sharper expansion
\[
\boxed{\displaystyle
\operatorname{vol}_d(K_\varepsilon)=\varepsilon^d\left[
\operatorname{vol}_d(P)+\frac{\varepsilon}{2R}
\big(d\operatorname{vol}_d(P)-(d+2)M_2(P)\big)
+O(\varepsilon^2)\right].}
\]
The coefficient of \(\varepsilon^{d+1}\) is strictly negative. When the active points are the vertices of a radius-\(R\) regular \(d\)-simplex,
\[
\operatorname{vol}_d(K_\varepsilon)
=\frac{d^{d/2}(d+1)^{(d+1)/2}}{d!}\,\varepsilon^d
\left(1-\frac{d(d-1)}{2R}\varepsilon+O(\varepsilon^2)\right).
\]

## Assumptions and scope

All intersections and volumes use Euclidean norms and Lebesgue measure. The set of active points consists of *every* center on the minimum enclosing sphere; all other centers are strictly interior to it. The assumption \(0\in\operatorname{relint}_L\operatorname{conv}\{p-c:\|p-c\|=R\}\) is essential; without it, the contact points might not positively span their linear hull and the stated rank law need not hold. The minimum enclosing ball of a non-singleton finite set has positive radius and is unique. No generic-position or affine-independence hypothesis is required among the active points.

The polar polytope may be written \(P=-\operatorname{conv}\{u\}^{\circ}\), where polarity is taken within \(L\). It contains the unit \(k\)-ball. The error constants in the full-rank expansion depend on the fixed point configuration and \(R\), not uniformly on configurations approaching a contact-rank transition.

## Proof

**1. Uniform anisotropic localization.** Translate \(c\) to zero. Since the active unit vectors positively span \(L\), compactness of the unit sphere in \(L\) gives \(\gamma>0\) such that
\[
\min_{u\,\mathrm{active}}\langle u,z\rangle\le-\gamma\|z\|\qquad(z\in L).
\]
The active constraints for \(x\in K_\varepsilon\) are
\[
\|x\|^2-2R\langle u,x\rangle\le2R\varepsilon+\varepsilon^2.
\]
Taking an active \(u\) minimizing its inner product with the projection \(x_L\), we obtain
\[
\|x\|^2+2R\gamma\|x_L\|\le2R\varepsilon+\varepsilon^2.
\]
Therefore \(\|x_L\|=O(\varepsilon)\) and \(\|x_{L^\perp}\|=O(\sqrt\varepsilon)\), uniformly over the entire intersection. At \(x=0\), each inactive center has strict distance slack \(R-\|p\|>0\). Finiteness and the uniform localization show that all inactive constraints are automatically satisfied for sufficiently small \(\varepsilon\).

**2. Anisotropic limit.** Set \(x=\varepsilon z+\sqrt\varepsilon\,y\), with \(z\in L\) and \(y\in L^\perp\). After dividing the active ball inequalities by \(\varepsilon\), their exact form is
\[
\|y\|^2+\varepsilon\|z\|^2-2R\langle u,z\rangle\le2R+\varepsilon.
\]
By the uniform bounds from step 1, the rescaled intersections are contained in one fixed bounded set. Their indicator functions converge except on a null boundary to the indicator of
\[
D_0=\left\{(z,y):\|y\|^2\le2R,\quad
z\in\left(1-\frac{\|y\|^2}{2R}\right)P\right\}.
\]
This is also Hausdorff convergence: the defining inequalities vary uniformly on a common compact set and the limit has interior (strictly feasible at the origin). The Jacobian of the anisotropic map is \(\varepsilon^k\varepsilon^{m/2}=\varepsilon^{(d+k)/2}\). Dominated convergence gives the asserted limit after integrating the transverse sections:
\[
\begin{aligned}
\operatorname{vol}_d(D_0)
&=\operatorname{vol}_k(P)
\int_{\|y\|\le\sqrt{2R}}
\left(1-\frac{\|y\|^2}{2R}\right)^kdy\\
&=\operatorname{vol}_k(P)\,\kappa_m(2R)^{m/2}
\frac{\Gamma(1+m/2)\Gamma(k+1)}{\Gamma(k+1+m/2)}.
\end{aligned}
\]
The equality remains valid when \(m=0\), interpreting the integral on the zero-dimensional space as evaluation at its unique point. Choosing a regular \(k\)-simplex on a radius-\(R\) sphere inside \(L\subset\mathbb R^d\) realizes every rank \(k\).

**3. Full-rank radial expansion.** Now \(k=d\). For each unit vector \(v\), put
\[
a(v)=-\min_{u\,\mathrm{active}}\langle u,v\rangle\ge\gamma>0,
\qquad h=\varepsilon+\frac{\varepsilon^2}{2R}.
\]
The ray \(\{\rho v:\rho\ge0\}\) leaves the intersection at the smallest active-ball boundary, hence at the *exact* radial distance
\[
\rho_\varepsilon(v)=\sqrt{R^2a(v)^2+2Rh}-Ra(v).
\]
Uniformly in \(v\), Taylor expansion gives
\[
\rho_\varepsilon(v)=\frac{h}{a(v)}-\frac{h^2}{2R\,a(v)^3}+O(h^3).
\]
The polar radial function is \(\rho_P(v)=1/a(v)\). Radial integration and uniform remainders yield
\[
\operatorname{vol}_d(K_\varepsilon)
=h^d\operatorname{vol}_d(P)
-\frac{h^{d+1}}{2R}(d+2)M_2(P)+O(h^{d+2}),
\]
since \(\operatorname{vol}_d(P)=d^{-1}\int_{S^{d-1}}\rho_P^d\,d\sigma\) and \(M_2(P)=(d+2)^{-1}\int_{S^{d-1}}\rho_P^{d+2}\,d\sigma\). Substituting \(h\) gives the displayed formula. Because \(P\) contains the unit ball and is a bounded polytope, \(\rho_P\ge1\) everywhere and \(\rho_P>1\) on a set of positive spherical measure. Thus
\[
(d+2)M_2(P)-d\operatorname{vol}_d(P)
=\int_{S^{d-1}}(\rho_P^{d+2}-\rho_P^d)\,d\sigma>0.
\]

**4. Simplex specialization.** The polar of the normalized regular \(d\)-simplex with unit circumradius is another regular simplex with vertices \(d u_i\). Its volume is \(d^{d/2}(d+1)^{(d+1)/2}/d!\). For a uniform point \(Z\) in this simplex, the elementary Dirichlet barycentric moment identity gives \(\mathbb E\|Z\|^2=d^2/(d+2)\), so inserting \(M_2(P)=\operatorname{vol}_d(P)d^2/(d+2)\) finishes the specialization.

## Verification

The accompanying `VERIFY.py` evaluates direct radial integrals for regular and nonregular planar active triangles, compares an exact three-dimensional two-ball lens with the rank-one coefficient, and independently integrates a three-dimensional rank-two case using a deterministic-seed low-discrepancy sample. The tests check convergence of the leading and second-order coefficients; they do not replace the uniform analytic proof. Execute with `python VERIFY.py` in an environment with NumPy and SciPy.

For a diameter pair at distance \(2R\) in \(\mathbb R^3\), the exact intersection volume is \(2\pi R\varepsilon^2+(4\pi/3)\varepsilon^3\), matching the rank-one coefficient. For an active equilateral triangle in \(\mathbb R^2\), the polar volume is \(3\sqrt3\) and the relative first correction is \(-\varepsilon/R\). These also independently check both predicted powers.

## Relationship to prior work

Intersections of congruent balls, also called ball bodies, are classical in convex geometry. Bezdek's 2019 study establishes global volumetric bounds and uses enclosing-sphere contact arguments, including a finite contact simplex; it does not state a general local collapse exponent indexed by the positive-spanning contact rank or the full-rank second-order polar-inertia identity. Bezdek's 2018 work treats intrinsic volumes and related comparison problems. The 2024 survey by Bezdek, Lángi and Naszódi discusses lens comparisons and intrinsic volumes, without the local rank-indexed asymptotic claimed here. The distinction is between estimates at a fixed radius and the geometry of collapse *as the common radius decreases to the minimum enclosing radius*. The local deformation and its second-order inertia law are the asserted contribution; the ordinary enclosing-ball and convex-polarity facts are not new.

## Limitations

The result is conditional on all active contacts lying in a subspace that they positively span about the enclosing-ball center. Contacts forming a more degenerate configuration, unequal ball radii, infinitely many moving centers, and uniform stability under rank transitions are not classified. The asymptotics concern exact Euclidean volumes rather than finite-sample measurements. The literature comparisons support provisional originality but do not establish historical priority; an earlier equivalent formula might exist. Independent review has not been performed.

## References

1. Károly Bezdek, *Volumetric bounds for intersections of congruent balls*, arXiv:1912.05118 (first posted 2019-12-11), https://arxiv.org/abs/1912.05118.
2. Károly Bezdek, *On intrinsic volumes of intersections of congruent balls*, arXiv:1810.11886 (2018), https://arxiv.org/abs/1810.11886.
3. Károly Bezdek, Zsolt Lángi, and Márton Naszódi, *Selected topics from the theory of intersections of balls*, arXiv:2411.10302 (first posted 2024-11-15), https://arxiv.org/abs/2411.10302. This later survey supplies context, not the historical eligibility date.
