# Exact John ellipsoids and contact latitudes of symmetric ball lenses in all dimensions

## Finding
For each integer \(n\ge2\) and real \(0\le s<1\), consider the symmetric lens
\[
L_{n,s}=\overline B_n(-s e_1,1)\cap\overline B_n(s e_1,1)\subset\mathbb R^n.
\]
Write
\[
D_{n,s}=\sqrt{4n+(n-1)^2s^2},\qquad
 a_{n,s}=\frac{D_{n,s}-(n+1)s}{2\sqrt n},\qquad
 b_{n,s}=\sqrt{a_{n,s}(a_{n,s}+\sqrt n\,s)}.
\]
The **unique** maximum-volume ellipsoid contained in \(L_{n,s}\), among all ellipsoids with arbitrary center and orientation, is
\[
E_{n,s}=\left\{(x_1,x_\perp):
 \frac{x_1^2}{a_{n,s}^2}+\frac{\|x_\perp\|_2^2}{b_{n,s}^2}\le1\right\}.
\]
Its volume is \(\kappa_n a_{n,s}b_{n,s}^{n-1}\), where \(\kappa_n=\pi^{n/2}/\Gamma(1+n/2)\). For \(0<s<1\), its exact boundary contact locus consists of the two \((n-2)\)-sphere orbits
\[
\left\{\left(\frac{\varepsilon a_{n,s}}{\sqrt n},
 b_{n,s}\sqrt{\frac{n-1}{n}}\,v\right):
 \varepsilon\in\{-1,1\},\ v\in S^{n-2}\right\}.
\]
After transforming the maximizing ellipsoid to the unit ball, the contact latitude is always \(\lvert u_1\rvert=1/\sqrt n\), independently of the center separation. For \(s=0\), the lens and its unique maximizing ellipsoid are both the unit ball, and their entire boundaries coincide.

There is also an exact nonzero thin-lens limit for the optimal occupied-volume fraction:
\[
\lim_{s\uparrow1}\frac{\operatorname{vol}_n(E_{n,s})}
 {\operatorname{vol}_n(L_{n,s})}
 =\frac{\kappa_n}{2\kappa_{n-1}}
 \frac{n^{n/2}}{(n+1)^{(n-1)/2}}.
\]

## Assumptions and scope
A closed Euclidean ball \(\overline B_n(y,r)\) has center \(y\in\mathbb R^n\) and radius \(r\ge0\). An ellipsoid means a nondegenerate affine image of \(\overline B_n(0,1)\). The lens has nonempty interior precisely for the stated range \(0\le s<1\); the degenerate endpoint \(s=1\) enters only as a limit. Coordinates are \(x=(x_1,x_\perp)\in\mathbb R\times\mathbb R^{n-1}\); \(S^{n-2}\) is the Euclidean unit sphere in the perpendicular space, also valid for \(n=2\) when it has two points. For balls of common radius \(R>0\) with center separation \(2d\), where \(0\le d<R\), multiply both semiaxes by \(R\) and set \(s=d/R\).

## Proof
**1. Algebraic normalization and containment.** The displayed formula for \(a=a_{n,s}\) is the positive root of
\[
a^2+\frac{n+1}{\sqrt n}\,sa+s^2=1.
\]
It is positive for \(s<1\), because \(D_{n,s}>(n+1)s\) is equivalent to \(s<1\). With \(b=b_{n,s}>0\), one also has
\[
b^2-a^2=\sqrt n\,sa.
\]
Put \(T=\operatorname{diag}(a,b,\dots,b)\), so that the proposed ellipsoid is \(T\overline B_n(0,1)\). For \(u=(u_1,u_\perp)\) of Euclidean norm at most one, let \(c=|u_1|\). The squared distance from \(Tu\) to the farther of the two sphere centers satisfies
\[
\begin{aligned}
\max_{\varepsilon=\pm1}\|Tu+\varepsilon se_1\|_2^2
&\le(a c+s)^2+b^2(1-c^2)\\
&=1-\sqrt n\,sa\left(c-\frac1{\sqrt n}\right)^2\le1.
\end{aligned}
\]
Thus \(E_{n,s}\subseteq L_{n,s}\) for all stated parameters. When \(s>0\), equality requires \(c=1/\sqrt n\) and \(\|u\|_2=1\), giving exactly the displayed contact orbits. At \(s=0\), \(a=b=1\).

**2. Supporting contacts and an exact isotropic frame.** Fix \(0<s<1\), and pass to the transformed lens \(K=T^{-1}L_{n,s}\), which contains the unit ball. Let \(v_1,\dots,v_n\in\mathbb R^{n-1}\) be the vertices of a centered regular \((n-1)\)-simplex on the unit sphere; they obey
\[
\sum_{j=1}^n v_j=0,\qquad
\sum_{j=1}^n v_jv_j^{\mathsf T}=\frac n{n-1}I_{n-1}.
\]
Define \(u_{j,\varepsilon}=(\varepsilon/\sqrt n,\sqrt{(n-1)/n}\,v_j)\) for each \(j\in\{1,\dots,n\}\) and \(\varepsilon\in\{-1,1\}\). These unit vectors belong to \(\partial K\). At \(u_{j,+}\), the active ball constraint is \(\|Tz+se_1\|_2^2\le1\); its outward gradient is
\[
2T^{\mathsf T}(Tu_{j,+}+se_1)=2b^2u_{j,+}.
\]
The analogous equation at \(u_{j,-}\) has the other sign of the center shift. By convexity, each \(\langle u_{j,\varepsilon},z\rangle\le1\) is a supporting halfspace for \(K\). The \(2n\) contacts, each given weight \(1/2\), satisfy exactly
\[
\frac12\sum_{j,\varepsilon}u_{j,\varepsilon}=0,
\qquad
\frac12\sum_{j,\varepsilon}
 u_{j,\varepsilon}u_{j,\varepsilon}^{\mathsf T}=I_n.
\]

**3. Global optimality and uniqueness without a symmetry restriction on competitors.** Every competing nondegenerate ellipsoid in \(K\) can be written \(F=y+A\overline B_n(0,1)\), where \(A\) is symmetric positive definite, by polar decomposition. Each contact halfspace above implies
\[
\langle u_{j,\varepsilon},y\rangle+\|A u_{j,\varepsilon}\|_2\le1.
\]
For any unit vector \(u\), \(\|Au\|_2\ge\langle u,Au\rangle\). Sum the halfspace inequalities with weights \(1/2\), use the two frame identities, and obtain
\[
\operatorname{tr}A
=\frac12\sum_{j,\varepsilon}
 \langle u_{j,\varepsilon},A u_{j,\varepsilon}\rangle
\le\frac12\sum_{j,\varepsilon}\|Au_{j,\varepsilon}\|_2\le n.
\]
The arithmetic–geometric mean inequality on the positive eigenvalues gives
\(\det A\le(\operatorname{tr}A/n)^n\le1\). Equality implies \(A=I_n\). For \(A=I_n\), each contact inequality says \(\langle u_{j,\varepsilon},y\rangle\le0\); its weighted sum vanishes, so each inner product is zero. As the contact vectors span \(\mathbb R^n\), \(y=0\). Consequently the unit ball is the **unique** largest ellipsoid in \(K\), and applying \(T\) proves the theorem. At \(s=0\), the same trace argument uses any centered isotropic finite set of unit-sphere contacts and proves uniqueness of the unit ball.

**4. The thin-lens fraction.** Slicing perpendicular to the first coordinate yields
\[
\operatorname{vol}_n(L_{n,s})
=2\kappa_{n-1}\int_s^1(1-t^2)^{(n-1)/2}\,dt.
\]
As \(s\uparrow1\), put \(\eta=1-s\). The semiaxis formulas give
\[
a\sim\frac{2\sqrt n}{n+1}\eta,
\qquad b^2\sim\frac{2n}{n+1}\eta.
\]
The displayed integral is asymptotic to
\(\frac{2\kappa_{n-1}}{n+1}2^{(n+1)/2}\eta^{(n+1)/2}\).
Dividing \(\kappa_na b^{n-1}\) by this expression gives the claimed limit.

## Verification
The accompanying standalone `verify.py` checks the exact quadratic-radicand identity on 42 rational parameter pairs; evaluates 42,042 high-precision complete-containment inequalities; verifies 363 entries of finite isotropic contact-frame identities; and checks six thin-lens volume limits by independent quadrature. Running the program yields `VERIFY_OK exact_radicand_pairs= 42 support_grid_checks= 42042 contact_frame_entries= 363 thin_lens_limits= 6`. The proof of unrestricted optimality and uniqueness is the analytic supporting-frame and trace argument above; sampled parameters cannot establish a universal result.

For the three-dimensional lens whose unit-ball centers are one unit apart, \(s=1/2\), the semiaxes simplify to
\[
a=\frac{\sqrt{13}-2}{2\sqrt3},\qquad b^2=\frac{11-\sqrt{13}}{12}.
\]
Its known volume \(5\pi/12\) supplies an independent normalization check.

## Relationship to prior work
Finch (2013, §1) studies the same three-dimensional symmetric lens, its volume, surface area, and mean width, and records general-dimensional volume formulas. That work does not determine any maximum-volume inscribed ellipsoid. A separately published all-dimensional symmetric-lens mean-width formula determines a distinct intrinsic functional, not the ellipsoid semiaxes or contact locus. Güler and Gürtuna (2012, §6) determine extremal ellipsoids of a **ball truncated between parallel hyperplanes**. The latter has planar boundary pieces, whereas a proper lens consists of two spherical cap boundaries meeting along a ridge; their formulas do not specialize through affine equivalence to the lens. Ivanov, Lángi, Naszódi, and Sagmeister (2025, introduction and §5) develop general theory for ellipsoids of revolution and contact conditions but do not give the displayed exact solution for intersections of two balls. The proof above provides explicit contact positions and a finite frame certificate for this concrete body.

## Limitations
The conclusion concerns intersections of exactly two **congruent** Euclidean balls. It does not solve intersections of unequal balls, intersections of three or more balls, or all arbitrary convex bodies. The all-dimensional formula and uniqueness are proved analytically; the finite checks are supplemental. Historical priority beyond the inspected literature is not established, and an older equivalent formula under an alternative description of the lens remains possible. The nonempty-interior endpoint \(s=1\) is excluded from the ellipsoid statement because the lens degenerates to a singleton.

## References
1. Steven R. Finch, *Mutually Equidistant Spheres that Intersect*, arXiv:1301.5515v1 (first posted 2013-01-23), especially §1.
2. Osman Güler and Filiz Gürtuna, *Symmetry of convex sets and its applications to the extremal ellipsoids of convex bodies*, *Optimization Methods and Software* **27** (2012), 735–759, DOI:10.1080/10556788.2011.626037, especially §6.
3. Grigory Ivanov, Zsolt Lángi, Márton Naszódi, and Ádám Sagmeister, *John Ellipsoids of Revolution*, arXiv:2507.06947v2 (2025), especially introduction and §5.
4. *Mean width of a symmetric lens in every dimension*, published mathematical result, published-finding corpus record `2026/10/4/SCOPE-mean-width-of-a-symmetric-lens-in-every-dimension--80ec085cfff6`, `RESULT.md`.
5. Fritz John, *Extremum Problems with Inequalities as Subsidiary Conditions*, in *Studies and Essays Presented to R. Courant*, 1948, pp. 187–204 (general historical context; not needed for the elementary proof above).
