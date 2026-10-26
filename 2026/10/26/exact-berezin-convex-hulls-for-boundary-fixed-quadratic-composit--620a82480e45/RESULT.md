# Exact Berezin convex hulls for boundary-fixed quadratic compositions

## Finding
For each real \(0<\mu<1\), let \(\varphi_\mu(z)=(1-\mu)z+\mu z^2\), and let \(C_{\varphi_\mu}f=f\circ\varphi_\mu\) on the classical Hardy space \(H^2(\mathbb D)\). Its Berezin range is \(B_\mu\). Define
\[
a_\mu=\frac1{2+\mu},\qquad K_\mu=\operatorname{conv}\bigl(\{1\}\cup\overline D(a_\mu,a_\mu)\bigr),
\]
where \(\overline D(c,R)=\{z\in\mathbb C:|z-c|\le R\}\). Then
\[
\boxed{\overline{\operatorname{conv}}B_\mu=K_\mu.}
\]
The two tangent points joining \(1\) to the limiting disk are
\[
T_\pm=\frac1{1+\mu}\ \pm\ i\frac{\sqrt{\mu(2+\mu)}}{(1+\mu)(2+\mu)}.
\]
Neither open tangent segment \((1,T_+)\) nor \((1,T_-)\) meets \(\overline{B_\mu}\); in particular \(B_\mu\) is nonconvex. Its convex-hull area is
\[
\boxed{\operatorname{Area}(K_\mu)=\frac{\pi+\sqrt{\mu(2+\mu)}-\arccos(1/(1+\mu))}{(2+\mu)^2}.}
\]
At the excluded endpoint \(\mu=0\), \(C_{\varphi_0}=I\) and \(B_0=\{1\}\). Nonetheless \(\varphi_\mu\to \varphi_0\) uniformly on \(\overline{\mathbb D}\) and, for every \(0<\mu<1\),
\[
\boxed{d_H(K_\mu,\{1\})=1,\qquad \lim_{\mu\downarrow0}\operatorname{Area}(K_\mu)=\pi/4.}
\]
Thus the convexified Berezin range has a macroscopic discontinuity at the identity despite uniform convergence of the symbols.

## Assumptions and scope
The Hardy space has inner product linear in the first argument and normalized Szegő kernel \(k_w(z)=(1-|w|^2)^{1/2}/(1-\overline wz)\). By definition \(B_\mu=\{\langle C_{\varphi_\mu}k_w,k_w\rangle: w\in\mathbb D\}\). Throughout the new theorem \(0<\mu<1\), and the operator acts on complex \(H^2(\mathbb D)\). Since \(|\varphi_\mu(z)|\le(1-\mu)|z|+\mu|z|^2<1\), the symbol is a holomorphic disk selfmap and induces a bounded composition operator. The result is about the closed **convex hull**, not an assertion that the range itself fills the hull. Area is planar Lebesgue measure; \(d_H\) is Euclidean Hausdorff distance of compact sets. The limit statement compares \(K_\mu\) with the actual \(\mu=0\) range.

## Proof
**1. Images of radius circles.** The reproducing-kernel calculation gives
\[
F_\mu(w):=\langle C_{\varphi_\mu}k_w,k_w\rangle
=\frac{1-|w|^2}{1-\overline w\varphi_\mu(w)}.
\]
Writing \(w=re^{i\theta}\), for \(0<r<1\), define
\[
A=1-(1-\mu)r^2,\quad B=\mu r^3,\quad \Delta=A^2-B^2.
\]
Here \(A-B=(1-r)(1+r+\mu r^2)>0\), so \(\Delta>0\). Consequently
\[
F_\mu(re^{i\theta})=\frac{1-r^2}{A-Be^{i\theta}}
\]
traces the *entire* circle of real center and radius
\[
c_r=\frac{(1-r^2)A}{\Delta},\qquad
\rho_r=\frac{(1-r^2)B}{\Delta}.
\]
At \(r=0\), \(F_\mu(0)=1\). Directly factoring \(A-B=(1-r)(1+r+\mu r^2)\), with \(A+B\to2\mu\), yields
\[
\lim_{r\uparrow1}c_r=\lim_{r\uparrow1}\rho_r=\frac1{2+\mu}=a_\mu.
\]
Hence \(\overline B_\mu\) contains the entire circle \(\partial\overline D(a_\mu,a_\mu)\), as well as \(1\).

**2. Exact global upper hull.** The identities
\[
(2+\mu)(1-r^2)A-\Delta=(1-r^2)^2(1+\mu+\mu^2r^2)>0
\]
and
\[
1-c_r=\frac{\mu r^2(1-r^2)(1+\mu r^2)}{\Delta}>0
\]
show that \(a_\mu<c_r<1\). More crucially,
\[
\frac{\rho_r}{1-c_r}=\frac r{1+\mu r^2}
<\frac1{1+\mu}=\frac{a_\mu}{1-a_\mu}.
\]
Strictness is equivalent to \((1-r)(1-\mu r)>0\). Set \(t_r=(1-c_r)/(1-a_\mu)\), which belongs to \((0,1)\). By convexity, \(K_\mu\) contains the homothetic disk
\[
(1-t_r)\{1\}+t_r\overline D(a_\mu,a_\mu)
=\overline D(c_r,t_r a_\mu).
\]
Because \(\rho_r<t_r a_\mu\), the circle traced at radius \(r\) lies strictly inside that disk, hence in the interior of \(K_\mu\). The value at \(r=0\) is \(1\in K_\mu\). This gives \(B_\mu\subset K_\mu\). Conversely, the origin value and the limiting entire circle from Step 1 generate \(K_\mu\) by closed convexification. Therefore \(\overline{\operatorname{conv}}B_\mu=K_\mu\).

**3. Missing exposed segments.** Since \(a_\mu<1/2\), the point \(1\) lies strictly outside the disk. Elementary right-triangle geometry gives the displayed tangent points \(T_\pm\). Each closed segment \([1,T_\pm]\) is an exposed face of \(K_\mu\): the supporting line is tangent to the disk and passes through \(1\). In Step 2, every point with \(0<r<1\) lies in the interior of \(K_\mu\); hence none is on either supporting line. To analyze accumulation, suppose \(F_\mu(r_j e^{i\theta_j})\) tends to a point on a tangent segment. A subsequence of \(r_j\) converges in \([0,1]\). An interior limit \(r\in(0,1)\) is impossible because all points on its image circle are strictly interior to \(K_\mu\). If \(r=0\), the only possible limit is \(1\); if \(r=1\), it lies on the limit circle, whose intersection with the corresponding tangent line is the sole point \(T_\pm\). Thus the relative interior \((1,T_\pm)\) is disjoint from \(\overline B_\mu\). If \(B_\mu\) were convex then its closure would be convex and equal \(K_\mu\), a contradiction.

**4. Area and the identity endpoint.** Let \(a=a_\mu\), center-to-exterior-point distance \(d=1-a\), and tangent length \(\ell=\sqrt{d^2-a^2}\). The region \(K_\mu\) is a disk with the external tangent wedge adjoined. Subtracting the circular cap from the triangle gives
\[
\operatorname{Area}(K_\mu)=\pi a^2+a\ell-a^2\arccos(a/d).
\]
Since \(a=1/(2+\mu)\), \(a/d=1/(1+\mu)\), and \(a\ell=\sqrt{\mu(2+\mu)}/(2+\mu)^2\), this is exactly the boxed formula. For \(\mu=0\), the symbol is \(z\), so \(C_{\varphi_0}=I\), giving \(B_0=\{1\}\). For positive \(\mu\), \(0\in\overline D(a_\mu,a_\mu)\subset K_\mu\), and the farthest point in that disk from \(1\) has distance \((1-a_\mu)+a_\mu=1\). By convexity, every point of \(K_\mu\) is within distance \(1\) of \(1\), so \(d_H(K_\mu,\{1\})=1\). Finally, \(|\varphi_\mu(z)-z|=\mu|z^2-z|\le2\mu\) for \(|z|\le1\), while the area formula tends to \(\pi/4\) as \(\mu\downarrow0\). This proves the claimed discontinuity.

## Verification
All inequalities are exact symbolic identities for \(0<\mu<1\) and \(0<r<1\). The indispensable strict inequality is \((1-r)(1-\mu r)>0\). The supplementary standalone checker verifies the center, radius, two algebraic factorizations, tangency, area, and supporting containment on a finite rational grid; this does not replace the analytic argument for continuum parameters. Reproduce with `python3 checker.py`. No computer-assisted infinite certification is asserted.

## Relationship to prior work
Bourdon, Le, and Thompson (2026, arXiv:2610.17634v1) give the general Berezin-transform formula and, in their Proposition 3.7, show that certain families \(\varphi(z)=z\psi(z^n)\) have circular fixed-radius images and contain their interiors. Our quadratic symbol fits that proposition with \(n=1\) and \(\psi(z)=1-\mu+\mu z\). That prior circle description is used and credited; it does not determine the **global** closed convex hull, its tangent contact points, its exact area, or the macroscopic jump at the identity. Cowen and Felder (2021) studied convexity and ranges for rotational and Blaschke-factor composition symbols; Augustine, Garayev, and Shankar (2023) studied other composition-operator Berezin convexity phenomena. The present nonmonomial boundary-fixed quadratic family is distinct from those explicitly classified there. Related exact calculations for monomial composition symbols cannot imply this continuum family because \(0<\mu<1\) yields two nonzero Taylor coefficients. No general assertion of first-ever priority is made.

## Limitations
The positive formula is established for the real convex coefficient segment \(0<\mu<1\), not arbitrary complex quadratic coefficients, arbitrary boundary-fixed disk maps, or higher-degree polynomials. It describes the closed convex hull, not the exact full nonconvex boundary of \(B_\mu\). The limiting area is not the actual area at \(\mu=0\). Publication priority against literature not indexed in the inspected sources is unresolved; there is no independent external audit.

## References
1. P. Bourdon, T. Le, and D. Thompson, *Berezin ranges of composition operators on* \(H^2\), arXiv:2610.17634v1 (first publicly posted October 13, 2026), especially introductory Berezin-transform formula and Proposition 3.7. https://arxiv.org/html/2610.17634v1
2. C. C. Cowen and C. Felder, *Convexity of the Berezin range*, arXiv:2109.12095, especially §4 on composition symbols. https://arxiv.org/pdf/2109.12095
3. M. Augustine, M. T. Garayev, and K. Shankar, *Composition operators, convexity of their Berezin range and related questions*, arXiv:2302.12547v2. https://arxiv.org/pdf/2302.12547
