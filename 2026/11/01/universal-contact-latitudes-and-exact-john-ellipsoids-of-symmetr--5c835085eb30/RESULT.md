# Universal contact latitudes and exact John ellipsoids of symmetric two-ball lenses

## Finding
Let \(d\ge2\) be an integer and \(0<c<1\). Define the unit-radius, center-separation-\(2c\) lens
\[
K_{d,c}=\overline B_d(ce_1,1)\cap\overline B_d(-ce_1,1)\subset\mathbb R^d.
\]
Put
\[
k=\frac{c(d+1)}{\sqrt d},\qquad
 a=\frac{2(1-c^2)}{\sqrt{k^2+4(1-c^2)}+k},\qquad
 b=\sqrt{a^2+ca\sqrt d}.
\]
The **unique maximum-volume inscribed ellipsoid** (John ellipsoid) of this lens, with no restriction on its center or orientation, is
\[
E_{d,c}=\left\{(x,z)\in\mathbb R\times\mathbb R^{d-1}:
\frac{x^2}{a^2}+\frac{\|z\|^2}{b^2}\le1\right\}.
\]
Its volume is exactly \(\kappa_d a b^{d-1}\), where \(\kappa_d=\pi^{d/2}/\Gamma(1+d/2)\).

Under the affine map \((x,z)=(a u_1,b u_\perp)\), **the entire contact set** between the unit ball and the transformed lens is the pair of spherical latitudes
\[
\left\{u\in S^{d-1}:|u_1|=\frac1{\sqrt d}\right\}.
\]
In particular, the normalized contact latitudes are independent of \(c\). The semiaxes satisfy \(0<a<1-c\) and \(a<b<\sqrt{1-c^2}\). At fixed \(0<c<1\), their dimension-asymptotic behavior is
\[
\lim_{d\to\infty}a\sqrt d=\frac{1-c^2}{c},
\qquad \lim_{d\to\infty}b=\sqrt{1-c^2}.
\]
Scaling both original balls to radius \(R>0\) multiplies both semiaxes by \(R\) when their centers lie at \(\pm Rc e_1\).

## Assumptions and scope
Balls are closed Euclidean balls. The lens has nonempty interior because \(0<c<1\). An ellipsoid is any full-dimensional affine image of the Euclidean unit ball; its center and principal axes are **not** constrained in the optimization. The theorem excludes \(c=1\), where the intersection degenerates to one point. The contact-set claim concerns the stated affine normalization, not every possible normalization of an arbitrary ellipsoid.

## Proof
**1. Algebraic identities and feasibility.** The positive number \(a\) is the unique positive root of
\[
a^2+\frac{c(d+1)}{\sqrt d}a+c^2=1.
\]
Consequently,
\[
b^2-a^2=ca\sqrt d>0,\qquad
b^2+c^2=1-\frac{ca}{\sqrt d}.
\]
If \((t,v)\in S^{d-1}\), the larger of the squared distances from \((at,bv)\) to the centers \(\pm ce_1\) equals
\[
\begin{aligned}
& a^2t^2+b^2(1-t^2)+c^2+2ca|t|\\
&\quad=1-(b^2-a^2)\left(|t|-\frac1{\sqrt d}\right)^2\le1.
\end{aligned}
\]
Thus the boundary of \(E_{d,c}\) lies in both balls. By convexity and because the origin lies in both balls, the entire ellipsoid lies in their intersection. Equality occurs exactly at the two asserted latitudes. From the root equation and \((d+1)/\sqrt d>2\) it also follows that \(0<a<1-c\); the identities above give \(a<b<\sqrt{1-c^2}\).

**2. A finite contact certificate.** Let \(T=\operatorname{diag}(a,b,\ldots,b)\) and \(L=T^{-1}K_{d,c}\). We already know \(B_d\subset L\). For each \(j\in\{2,\ldots,d\}\) and each \(\sigma,\tau\in\{-1,+1\}\), define
\[
u_{j,\sigma,\tau}
=\frac{\sigma}{\sqrt d}e_1
+\tau\sqrt{\frac{d-1}{d}}e_j.
\]
Each is a common boundary point of \(B_d\) and \(L\). At a positive-longitude contact, the active ball inequality in transformed coordinates has gradient
\[
2(a^2u_1+ca,\ b^2u_\perp)=2b^2u,
\]
where the equality uses \(b^2-a^2=ca\sqrt d\) and \(u_1=1/\sqrt d\). The negative-longitude case uses the other defining ball and gives the same gradient. Hence \(u\) is also a shared outer unit normal: the hyperplane \(u\cdot y=1\) supports \(L\) at every listed contact.

Assign each of the \(4(d-1)\) contact points the positive weight
\[
\omega=\frac{d}{4(d-1)}.
\]
Symmetry and direct calculation give
\[
\sum_{j,\sigma,\tau}\omega u_{j,\sigma,\tau}=0,
\qquad
\sum_{j,\sigma,\tau}\omega\,u_{j,\sigma,\tau}u_{j,\sigma,\tau}^{\mathsf T}=I_d.
\]
The sufficiency direction of the classical John contact theorem now states that the unit ball is the unique maximum-volume ellipsoid in \(L\). Applying \(T\) proves that \(E_{d,c}\) is the unique John ellipsoid of \(K_{d,c}\). This certificate excludes *all* shifted, tilted, and nonsymmetric ellipsoid competitors, rather than merely optimizing a two-parameter subclass.

**3. Dimension limit.** Since \(a\) is the positive solution of
\[
a^2+\frac{c(d+1)}{\sqrt d}a=1-c^2,
\]
one first obtains \(a=O(d^{-1/2})\), then \(a\sqrt d\to(1-c^2)/c\). Finally, \(b^2=a^2+ca\sqrt d\to1-c^2\). This proves both limits.

## Verification
The supplied `verify.py` reproduces the defining quadratic equation, verifies the exact squared-distance identity over sampled latitudes, constructs and checks the finite John moment certificate and common contact normals, and compares the analytic semiaxes with independent continuous constrained optimization for an explicit parameter grid. It also tests the dimension limit numerically. These finite tests supplement, but do not replace, the exact identities and contact-theorem proof above. Run `python3 verify.py` with NumPy and SciPy.

## Relationship to prior work
The classical John theorem gives a necessary-and-sufficient contact decomposition for the maximally inscribed ellipsoid of **any** convex body; it does not by itself evaluate the semiaxes or contact latitudes of this two-ball lens. Ivanov and Naszódi (2022) develop considerably more general functional John and Löwner contact conditions, with the convex-body case discussed explicitly in Sections 1 and 12.1; no lens-specific semiaxis or latitude formula appears in that treatment.

Bezdek (2019) studies the same lens class within intersections of congruent balls but establishes inradius, circumradius, and intrinsic-volume inequalities, not the maximally inscribed ellipsoid. A later survey by Bezdek, Lángi, and Naszódi (2024) develops those lens extremal problems but does not discuss John ellipsoids. The publicly indexed result *Mean width of a symmetric lens in every dimension* computes a support-function average for exactly the same body; this is an independent invariant and does not determine the John ellipsoid. Other indexed John-ellipsoid formulas concern different bodies, such as the Khachiyan half-cone. A recent exact Euclidean projector for two-ball intersections likewise concerns a different geometric optimization problem.

## Limitations
The result covers exactly two congruent overlapping Euclidean balls and does not determine John ellipsoids for unequal radii or intersections of three or more balls. It does not claim novelty of the John contact criterion. Although searches and comparisons did not identify an equivalent explicit lens formula, historical priority is not exhaustively established: older convex-optimization sources might contain this special-case calculation. The high-dimensional limit is at fixed positive \(c\), not uniform as \(c\) tends to zero or one.

## References
1. Grigory Ivanov and Márton Naszódi, *Functional John and Löwner conditions for pairs of log-concave functions*, arXiv:2212.11781v1 (first public 2022-12-22), especially Sections 1 and 12.1 of v2 (2023).
2. Károly Bezdek, *Volumetric bounds for intersections of congruent balls*, arXiv:1912.05118v1 (first public 2019-12-11).
3. Károly Bezdek, Zsolt Lángi and Márton Naszódi, *Selected topics from the theory of intersections of balls*, arXiv:2411.10302v1 (first public 2024-11-15), especially Section 3 of v2.
4. *Mean width of a symmetric lens in every dimension*, publicly indexed geometric result, 2026, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-mean-width-of-a-symmetric-lens-in-every-dimension--80ec085cfff6.
5. *Exact John ellipsoid of the Khachiyan half-cone*, publicly indexed geometric result, 2026, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-john-ellipsoid-of-the-khachiyan-half-cone--12746f7a27eb.
6. Fritz John, *Extremum problems with inequalities as subsidiary conditions*, 1948, classical contact criterion.
