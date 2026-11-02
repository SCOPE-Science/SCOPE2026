# Extremal ellipsoids and a sharp volume ratio for rectangular-section Steinmetz bodies

## Finding

Fix an integer \(m\ge2\), write \(d=m+1\), and let \(a_1,\ldots,a_m>0\). Set \(b=\min_i a_i\) and consider the compact convex body
\[
K=\bigl\{(x_1,\ldots,x_m,z)\in\mathbb R^d:\ x_i^2+z^2\le a_i^2\text{ for every }1\le i\le m\bigr\}.
\]
Its horizontal sections are rectangular boxes; in three dimensions it is the intersection of two perpendicular circular cylinders, also called a (possibly unequal-radius) bicylinder or Steinmetz solid.

There is exactly one \(t\in[1,d/2)\) solving
\[
1=t\sum_{i=1}^m\frac{b^2}{d a_i^2-tb^2}.
\tag{1}
\]
The unique maximal-volume inscribed ellipsoid (John ellipsoid) and unique minimal-volume enclosing ellipsoid (Löwner ellipsoid) are, respectively,
\[
J=\left\{(x,z):\sum_{i=1}^m\frac{x_i^2}{a_i^2}+\frac{z^2}{b^2}\le1\right\},
\tag{2}
\]
\[
L=\left\{(x,z):\sum_{i=1}^m\frac{x_i^2}{d a_i^2-tb^2}+\frac{z^2}{tb^2}\le1\right\}.
\tag{3}
\]
Moreover, their *complete* common contact set with \(K\) on the Löwner side is the continuous ridge
\[
\partial K\cap\partial L=
\Gamma:=\{(x,z): |z|\le b,\ x_i^2+z^2=a_i^2\text{ for all }i\}.
\tag{4}
\]
Thus the enclosing ellipsoid touches the entire simultaneous cylinder-intersection curve, not merely finitely many isolated extremal points.

Write \(c_i=a_i^2/b^2\ge1\), so at least one \(c_i=1\). The exact ratio of the enclosing to inscribed ellipsoid volumes is
\[
\mathcal R_m(c_1,\ldots,c_m)
=\sqrt{t\prod_{i=1}^m\left(d-\frac{t}{c_i}\right)}.
\tag{5}
\]
It is strictly increasing in every coordinate \(c_i\) while the other parameters and the normalization \(\min c_i=1\) are retained. For all finite positive radii,
\[
m^{m/2}\le\mathcal R_m<\frac{d^{d/2}}2.
\tag{6}
\]
The lower equality holds exactly for equal radii. The upper constant is optimal but not attained: it is approached if one radius stays at \(b\) and all other radii tend to infinity relative to \(b\).

## Assumptions and scope

The ambient metric and volumes are Euclidean; all cylinder inequalities are simultaneous, and every radius is strictly positive. We require \(m\ge2\). The body is bounded because \(|z|\le b\) and \(|x_i|\le a_i\), convex as an intersection of second-order-cone-type quadratic cylinders, centrally symmetric, and full-dimensional. All claims are exact for every fixed dimension and every finite positive radius tuple. The boundary cases with some radii tending to infinity are limits, not members of the finite-radius family.

## Proof

**Unique scalar parameter.** The function \(H(t)=t\sum_i b^2/(d a_i^2-tb^2)\) is strictly increasing on \((0,d)\), since at least one \(a_i=b\) makes its smallest denominator vanish as \(t\uparrow d\). It satisfies \(H(0)=0\) and \(H(1)\le m/(d-1)=1\), with equality only for equal radii. At \(t=d/2\), the summand corresponding to \(a_i=b\) already contributes \(1\), and each of the other \(m-1\) summands is positive. Consequently (1) has a unique root \(1\le t<d/2\).

**John ellipsoid.** Uniqueness of a maximal-volume inscribed ellipsoid and invariance of \(K\) under every individual coordinate sign change imply that the John ellipsoid is centered and axis-aligned. If its semiaxes are \(u_1,\ldots,u_m,v\), containment in \(K\) requires \(u_i\le a_i\) and \(v\le b\), by considering its coordinate-axis extremities. Conversely, the ellipsoid (2) lies inside \(K\), because its points satisfy
\[
x_i^2+z^2\le \max(a_i^2,b^2)\left(\frac{x_i^2}{a_i^2}+\frac{z^2}{b^2}\right)\le a_i^2.
\]
It attains the product of all coordinate-width bounds, proving maximality and uniqueness.

**Enclosure and complete contact locus.** Put \(p_i=(d a_i^2-tb^2)^{-1}\) and \(r=(tb^2)^{-1}\). Equation (1) says \(\sum_i p_i=r\). Also
\[
\sum_i a_i^2p_i
=\frac1d\sum_i\left(1+tb^2p_i\right)
=\frac{m+1}{d}=1.
\tag{7}
\]
For every \((x,z)\in K\),
\[
\sum_i p_i x_i^2+r z^2
\le\sum_i p_i(a_i^2-z^2)+r z^2
=1.
\tag{8}
\]
This proves \(K\subseteq L\). Every \(p_i>0\), so equality in (8) holds if and only if each cylinder constraint is saturated. The right side of (4) is therefore exactly the complete contact locus, including its endpoints where some coordinates may vanish.

**Global optimality of the Löwner ellipsoid.** Set \(D=\operatorname{diag}(\sqrt{d a_1^2-tb^2},\ldots,\sqrt{d a_m^2-tb^2},b\sqrt t)\), so \(L=DB_2^d\). On \(\Gamma\) take two sign-symmetric probability orbits. Orbit \(\nu_0\) is uniform on \(z=0\), \(x_i=\pm a_i\) (independent signs). Orbit \(\nu_1\) is uniform on \(z=\pm b\), \(x_i=\pm\sqrt{a_i^2-b^2}\), with zero coordinates interpreted literally. Each orbit is supported on \(\partial K\cap\partial L\). Normalize by \(D^{-1}\) and form
\[
\nu=\frac{d-t}{d}\nu_0+\frac{t}{d}\nu_1.
\tag{9}
\]
The weights are positive and sum to one. The normalized mean is zero by sign symmetry. Off-diagonal second moments vanish. Each transverse diagonal second moment is
\[
\frac{(d-t)a_i^2+t(a_i^2-b^2)}{d(d a_i^2-tb^2)}=\frac1d,
\]
and the final-coordinate moment is \(\frac{t}{d}\frac{b^2}{tb^2}=1/d\). Hence
\[
\int yy^{\mathsf T}\,d\nu(y)=\frac1d I_d.
\tag{10}
\]
For completeness, the usual enclosing-ellipsoid contact criterion follows directly from (10): if an ellipsoid \(F=\{y:\|T(y-v)\|_2\le1\}\) contains all the normalized contacts, integrating the squared inequality gives
\[
\frac1d\operatorname{tr}(T^{\mathsf T}T)+\|Tv\|_2^2\le1.
\]
Arithmetic-geometric mean applied to the eigenvalues yields \(|\det T|\le1\), so \(\operatorname{vol}F\ge\operatorname{vol}B_2^d\). Equality requires \(v=0\) and \(T^{\mathsf T}T=I_d\). Applying this after the affine map \(D^{-1}\) proves that (3) is the unique minimum-volume ellipsoid containing \(K\), with no restriction to axis-aligned competitors.

**Volume ratio and sharpness.** Products of semiaxes in (2) and (3) give (5). The scalar root (1) is the unique stationary point and strict maximum, for \(0<s<d\), of
\[
G_c(s)=s\prod_{i=1}^m\left(d-\frac{s}{c_i}\right),
\quad
\frac{d}{ds}\log G_c(s)=\frac1s-\sum_i\frac1{d c_i-s}.
\tag{11}
\]
The second derivative of \(\log G_c\) is strictly negative, while the derivative tends to positive infinity at zero and is negative near \(d\) because some \(c_i=1\). Thus \(\mathcal R_m^2=\max_{0<s<d}G_c(s)\). Increasing any \(c_i\) strictly increases every corresponding factor for \(s>0\), hence strictly increases the maximum.

Since all \(c_i\ge1\), \(G_c(1)\ge 1(d-1)^m=m^m\), with strict inequality if any \(c_i>1\); equality holds when all radii are equal. Conversely, retaining an index \(j\) with \(c_j=1\),
\[
G_c(s)=s(d-s)\prod_{i\ne j}(d-s/c_i)
\le d^{m-1}s(d-s)\le \frac{d^{m+1}}4.
\tag{12}
\]
The first inequality is strict for finite radii because \(m\ge2\). When all \(c_i\) other than \(c_j\) tend to infinity, \(G_c\) converges uniformly on compact subsets of \((0,d)\) to \(d^{m-1}s(d-s)\); the maximizing root tends to \(d/2\). This proves the sharp bounds (6).

For the classical three-dimensional bicylinder, with \(a_1=a\ge a_2=b\), put \(c=(a/b)^2\). Equation (1) reduces to
\[
t=1+c-\sqrt{c^2-c+1},
\]
so the enclosing semiaxes are \(\sqrt{3a^2-tb^2}\), \(b\sqrt{3-t}\), and \(b\sqrt t\). The volume ratio increases from \(2\) at equal radii to the sharp limit \(3\sqrt3/2\) as \(a/b\to\infty\).

## Verification

The standalone file `verify.py` implements a bisection of (1), directly evaluates the contact moments (9)--(10), tests the ridge and random interior points, checks the sharp volume bounds, and independently minimizes a concave-determinant program via SciPy SLSQP when SciPy is installed. With Python 3 and SciPy installed, run `python verify.py`. In the reported execution, 330 deterministic parameter cases passed all elementary identities and geometric tests, with largest normalized numerical residual \(6.66\times10^{-16}\); 84 independent constrained solves passed with maximum relative precision-coordinate discrepancy \(8.66\times10^{-7}\). These finite tests support reproducibility, not the infinite quantifiers, which follow from the proof above.

## Relationship to prior work

The classical Steinmetz solid and its unequal-radius variants have a substantial literature on their volume, boundary curves and surface area; see MathWorld's account and references to Hubbell and Moore. The two-cylinder special case here concerns extremal ellipsoids and their full continuous contact locus rather than those known integrals.

Güler and Gürtuna (2007), especially their Theorem 2.2 and Section 8, develop Löwner-contact optimality and solve enclosing ellipsoids for truncated cones and single ellipsoidal cylinders. Their special-case domains are not the simultaneous intersection of \(m\) cylindrical quadratic constraints above, and their general contact criterion alone does not supply the root (1), the ridge contact identity (4), or the sharp ratio (6). The general criterion motivates the certificate (9)--(10), which is also proved directly here.

Nearby mathematical records treat central-section areas of intersections of cylinders, ellipsoidal approximations of other convex bodies, and projection statistics. Those are different invariants or different bodies. An unrestricted theorem about enclosing ellipsoids implies existence and the possibility of optimality certificates, but not these numerical formulae without solving the present geometry. This comparison is about mathematical implication rather than title overlap.

## Limitations

This is an all-dimensional exact result for the stated *rectangular-section* family; it does not claim an analogous formula for arbitrary tilted cylinder axes, noncircular cross sections or translations of the axes. The sharp upper ratio belongs only to a divergent-radius limit, not to a finite convex body. Historical originality remains subject to independent review, especially older geometric-design literature and potentially inaccessible pre-digital publications. Numerical checks are not a proof, and no independent audit has been performed.

## References

- O. Güler and F. Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707v1, publicly posted 2007-09-05. Full text: https://arxiv.org/pdf/0709.0707.
- E. W. Weisstein, *Steinmetz Solid*, MathWorld, https://mathworld.wolfram.com/SteinmetzSolid.html (historical bibliography and unequal-radius bicylinder volume).
- J. H. Hubbell, *Common Volume of Two Intersecting Cylinders*, J. Res. NBS C 69C (1965), 139–143 (volume predecessor, cited by MathWorld; full text not assessed).
- M. Moore, *Symmetrical Intersections of Right Circular Cylinders*, Mathematical Gazette 58 (1974), 181–185 (classical solid geometry; full text not assessed).
