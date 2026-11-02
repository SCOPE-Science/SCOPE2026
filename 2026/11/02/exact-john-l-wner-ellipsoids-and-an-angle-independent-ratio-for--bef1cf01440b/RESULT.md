# Exact John–Löwner ellipsoids and an angle-independent ratio for intersecting cylinders

## Finding

The intersection of two infinite solid right circular cylinders with different radii and nonparallel intersecting axes has explicit, unique maximal inscribed and minimal covering ellipsoids. The ellipsoids and explicit certifying contact points are given below for every radius ratio and every crossing angle. The **ratio of their Euclidean volumes is independent of the axis angle** and increases strictly from \(2\) to the unattained limit \(3\sqrt3/2\) as the ratio of larger to smaller cylinder radius increases from one to infinity.

## Assumptions and scope

Let the radii satisfy \(a\ge b>0\), and let the two cylinder axes be distinct, intersecting straight lines making an angle \(\beta\in(0,\pi)\). Let \(n_1,n_2\) be unit vectors in their axis plane perpendicular to the respective axes, and let \(e_3\) be a unit normal to their axis plane. The linear map

\[
T(v)=(n_1\cdot v,n_2\cdot v,e_3\cdot v)=(s_1,s_2,z)
\]

is invertible with \(|\det T|=|\sin\beta|\). It carries the cylinder intersection to the canonical compact convex body

\[
K_{a,b}=\{(s_1,s_2,z):s_1^2+z^2\le a^2,\quad s_2^2+z^2\le b^2\}.
\]

All formulas below are expressed in these affine coordinates; their inverse images under \(T\) are the Euclidean ellipsoids for the originally oriented cylinders. The result is for infinite circular cylinders; it does not assert the same formulas for finite-height cylinders, skew axes, or more than two cylinders.

Set
\[
t=\frac{a^2}{b^2},\qquad
u=\sqrt{t^2-t+1}-(t-1),\qquad \frac12<u\le1.
\]

The unique John ellipsoid and unique Löwner ellipsoid of \(K_{a,b}\) are respectively

\[
\boxed{J=\left\{\frac{s_1^2}{a^2}+\frac{s_2^2}{b^2}+\frac{z^2}{b^2}\le1\right\}},
\]

\[
\boxed{L=\left\{\frac{u s_1^2}{a^2(1+u)}+
\frac{s_2^2}{b^2(1+u)}+
\frac{z^2}{b^2(2-u)}\le1\right\}}.
\]

Their volume ratio satisfies
\[
\boxed{\frac{\operatorname{vol}(L)}{\operatorname{vol}(J)}=
(1+u)\sqrt{\frac{2-u}{u}}},\qquad
2\le\frac{\operatorname{vol}(L)}{\operatorname{vol}(J)}<\frac{3\sqrt3}{2}.
\]

Equality in the lower bound occurs exactly for \(a=b\). The upper bound is sharp in the limit \(a/b\to\infty\), but is not attained by a compact bicylinder.

## Proof

**Step 1: affine reduction.** Because both cylinders share an axis-intersection point and their transverse normals make an angle with sine \(|\sin\beta|\), \(T\) is invertible. Maximum-inscribed and minimum-containing volume ellipsoids are affine-equivariant, and both volumes acquire the common factor \(|\sin\beta|^{-1}\) under \(T^{-1}\). Thus it suffices to prove the canonical formulas.

**Step 2: the John ellipsoid and global certificate.** The proposed \(J\) is contained in \(K_{a,b}\): the inequalities \(s_1^2+z^2\le a^2\) and \(s_2^2+z^2\le b^2\) follow from its equation using \(a\ge b\). The six points \((\pm a,0,0)\), \((0,\pm b,0)\), \((0,0,\pm b)\) lie in \(K_{a,b}\cap\partial J\). After the linear normalization \((s_1/a,s_2/b,z/b)\), these become the six signed coordinate vectors. Giving each point weight \(1/2\), their weighted sum is zero and their weighted outer-product sum is the identity matrix. The John contact theorem consequently certifies that \(J\) is the unique maximal-volume inscribed ellipsoid, not just the best axis-aligned candidate.

**Step 3: algebra for the covering ellipsoid.** Put
\[
A=\frac{a^2(1+u)}u,\qquad B=b^2(1+u),\qquad C=b^2(2-u).
\]

The defining equation of \(u\) is equivalent to
\[
t(2u-1)=u(2-u).
\]

This gives two identities
\[
\frac{a^2}{A}+\frac{b^2}{B}=1,
\qquad
\frac{a^2-b^2}{A}+\frac{b^2}{C}=1.
\]

At a fixed \(z^2=w\in[0,b^2]\), a point of \(K_{a,b}\) satisfies \(s_1^2\le a^2-w\) and \(s_2^2\le b^2-w\). Thus its squared candidate ellipsoidal norm is at most
\[
F(w)=\frac{a^2-w}{A}+\frac{b^2-w}{B}+\frac{w}{C}.
\]

This is affine in \(w\) and equals one at both endpoints \(w=0\) and \(w=b^2\). Therefore \(F(w)=1\) throughout, proving \(K_{a,b}\subseteq L\). Indeed the outer ellipsoid's quadratic form equals the positive convex combination \(\frac{u}{1+u}\frac{s_1^2+z^2}{a^2}+\frac{1}{1+u}\frac{s_2^2+z^2}{b^2}\); therefore **the entire common boundary ridge of the two cylinders lies on \(\partial L\)**. For \(a>b\), two finite sign orbits of this continuous contact locus suffice to certify optimality:
\[
\mathcal O_0=\{(\pm a,\pm b,0)\},\qquad
\mathcal O_1=\{(\pm\sqrt{a^2-b^2},0,\pm b)\}.
\]

Here signs on each orbit are independent. For \(a=b\), the second orbit contains only the two distinct axial poles.

**Step 4: the Löwner global certificate.** Normalize \(L\) to the unit ball by \((s_1,s_2,z)\mapsto(s_1/\sqrt A,s_2/\sqrt B,z/\sqrt C)\). Distribute probability mass
\[
p_0=\frac{1+u}{3}
\]

uniformly on \(\mathcal O_0\), and mass
\[
p_1=\frac{2-u}{3}
\]

uniformly on \(\mathcal O_1\). These are positive and sum to one. Sign symmetry makes the mean zero and off-diagonal covariances vanish. The three diagonal covariances are
\[
\frac{p_0a^2+p_1(a^2-b^2)}{A}
=\frac{p_0 b^2}{B}=
\frac{p_1 b^2}{C}=\frac13.
\]

Hence the weighted outer-product sum is \(I_3/3\). Multiplying the contact weights by three yields the normalized Löwner contact identity \(\sum c_i v_iv_i^{\mathsf T}=I_3\), with \(\sum c_i v_i=0\). The convex-body Löwner contact theorem proves global optimality and uniqueness of \(L\), including among nonsymmetric and rotated ellipsoids.

**Step 5: ratio and rigidity.** Ellipsoid volumes are \((4\pi/3)\) times the product of the semiaxes, so
\[
\frac{\operatorname{vol}(L)}{\operatorname{vol}(J)}
=\frac{\sqrt{ABC}}{ab^2}=(1+u)\sqrt{\frac{2-u}{u}}.
\]

For \(t>1\) the inverse relation is \(t=u(2-u)/(2u-1)\). Its derivative is negative, as is
\[
\frac{d}{du}\log\frac{\operatorname{vol}(L)^2}{\operatorname{vol}(J)^2}
=\frac{-2(u^2-u+1)}{u(1+u)(2-u)}<0.
\]

Consequently the ratio strictly increases with \(t\), starting at \(2\) when \(u=1\), and tending to \(3\sqrt3/2\) as \(u\downarrow1/2\). No step depends on \(\beta\) except the common affine volume factor, proving angle independence.

## Verification

The standalone standard-library Python file `check_bicylinders.py` checks the two endpoint contact equalities, normalized contact covariance, exact volume-ratio reduction, and a reproducible finite numerical sweep of radii, including the equal-radius case and strongly unequal radii. It also samples points of the canonical body and of the proposed inscribed ellipsoid. Execute with `python3 check_bicylinders.py`. These finite checks corroborate, but do not replace, the universal analytic containment and contact-certification arguments above.

## Relationship to prior work

Hubbell (1965) gives the complete intersection **volume** of nonparallel cylinders of arbitrary radii and angle, including elliptic-integral and hypergeometric evaluations. That is a different invariant from the two extremal ellipsoids studied here. Classical John–Löwner theory supplies the contact-moment optimality criteria used in the proof; no novelty is claimed for those criteria or their affine invariance. Freund–Sun (2002) treats algorithms for covering finite point sets, Klartag (2003) studies general symmetric-body ellipsoid maps and contact characterizations, and Weber–Schröcker (2009) studies uniqueness for extremal ellipsoids. The claim here is the explicit pair of formulas, their contact-orbit structure, and the sharp angle-independent ratio for **this entire two-cylinder family**. Searches for equivalences and stronger covering results did not locate a statement containing these formulas; this is not a proof of historical uniqueness.

## Limitations

The result assumes two infinite solid right circular cylinders whose axes intersect and are nonparallel. Degenerate parallel axes lead to noncompact intersections and are excluded. The affine-coordinate ellipsoids must be transformed back for the original Euclidean coordinates. Historical priority is provisional: obscure engineering bounds or earlier convex-geometry treatments may have established equivalent ellipsoids, and the cited general references were not all inspected page-by-page. No independent external audit has been performed. The 1965 source has year and issue-period evidence but no verified exact first-public day; the day-stamped 2002 source is used as conservative exact-day archival provenance, not as the first historical study of the cylinders.

## References

1. J. H. Hubbell, “Common Volume of Two Intersecting Cylinders,” *Journal of Research of the National Bureau of Standards C* **69C** (1965), 139–143. https://nvlpubs.nist.gov/nistpubs/jres/69C/jresv69Cn2p139_A1b.pdf.
2. R. M. Freund and P. Sun, “Computation of Minimum Volume Covering Ellipsoids,” Optimization Online, publicly posted 2002-07-31. https://optimization-online.org/2002/07/516/.
3. B. Klartag, “On John-Type Ellipsoids,” arXiv:math/0312065 (2003-12-02). https://arxiv.org/abs/math/0312065.
4. M. J. Weber and H.-P. Schröcker, “Davis’ Convexity Theorem and Extremal Ellipsoids,” arXiv:0907.1158 (2009-07-07). https://arxiv.org/abs/0907.1158.
