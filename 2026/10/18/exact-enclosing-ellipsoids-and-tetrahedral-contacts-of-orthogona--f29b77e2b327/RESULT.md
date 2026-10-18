# Exact enclosing ellipsoids and tetrahedral contacts of orthogonal-disk hulls

## Finding

Let \(t\ge0\). In Euclidean \(\mathbb R^3\), consider two unit disks in perpendicular planes with centers separated by \(t\) along the common line of those planes:
\[
D_-(t)=\{(u-t/2,y,0):u^2+y^2\le1\},\qquad
D_+(t)=\{(u+t/2,0,z):u^2+z^2\le1\},
\]
and \(K_t=\operatorname{conv}(D_-(t)\cup D_+(t))\). Put
\[
r=\sqrt{t^2+12},\quad
 a^2=\frac{(2t+r)^2}{12},\quad
 b^2=\frac{12-t^2+tr}{12}.
\]
**The unique minimum-volume ellipsoid containing \(K_t\), among all translated and arbitrarily oriented ellipsoids, is**
\[
E_t=\left\{(x,y,z):\frac{x^2}{a^2}+\frac{y^2+z^2}{b^2}\le1\right\},\qquad
\operatorname{vol}_3(E_t)=\frac{4\pi}{3}ab^2.
\]

For every \(t>0\), the entire contact set \(K_t\cap\partial E_t\) consists of **exactly four points**. Writing
\[
p=\frac{t-r}{6}=\frac{-2}{t+r},\qquad
c=\frac t2-p,\qquad d=\sqrt{1-p^2},
\]
these are \((-c,d,0)\), \((-c,-d,0)\), \((c,0,d)\), and \((c,0,-d)\). Under the linear normalization \((x,y,z)\mapsto(x/a,y/b,z/b)\), the four contacts become the vertices of a regular tetrahedron on the unit sphere, independent of \(t\):
\[
\left(-\frac1{\sqrt3},\pm\sqrt{\frac23},0\right),\qquad
\left(\frac1{\sqrt3},0,\pm\sqrt{\frac23}\right).
\]
For \(t=0\), \(E_0\) is the unit ball and the contact locus is the union of the two generating unit circles. The distinguished separation \(t=1\) is the classical oloid. A simultaneous change of the disk radius from \(1\) to \(\rho>0\) scales the semiaxes by \(\rho\), with \(t\) replaced by center separation divided by \(\rho\).

## Assumptions and scope

The disks are *filled* Euclidean disks, have equal radius, and lie in two perpendicular planes meeting along the line of their centers. Their separation is arbitrary and nonnegative, including disjoint disks. The ambient dimension is three. Ellipsoid centers, principal axes and axis ratios are unrestricted in the optimization. The result is about the minimum-volume **containing** ellipsoid (Löwner ellipsoid), not the maximum-volume inscribed (John) ellipsoid. At \(t=0\) the body is still full-dimensional.

## Proof

**1. Algebraic parameter and containing candidate.** Set \(p=(t-\sqrt{t^2+12})/6\). Then
\[
3p^2-tp-1=0,\qquad t=3p-\frac1p,\qquad
-\frac1{\sqrt3}\le p<0.
\]
Equality in the left inequality holds exactly at \(t=0\). Define \(c=t/2-p\). Elementary rearrangement gives
\[
c=\frac{1-p^2}{-2p}>0,\quad
a^2=3c^2,\quad b^2=\frac32(1-p^2),\quad
\frac{a^2}{b^2}=\frac{1-p^2}{2p^2}\ge1.
\]
These are equivalent to the two closed radical expressions in the finding.

On the first generating *circle*, write a point as \((v-t/2,\pm\sqrt{1-v^2},0)\), with \(-1\le v\le1\). Its squared ellipsoidal gauge is
\[
q_t(v)=\frac{(v-t/2)^2}{a^2}+\frac{1-v^2}{b^2}.
\]
The identities just derived imply \(q_t(p)=1\) and \(q_t'(p)=0\). Since \(q_t\) is quadratic with leading coefficient \(1/a^2-1/b^2\), the **exact global identity** is
\[
1-q_t(v)=\left(\frac1{b^2}-\frac1{a^2}\right)(v-p)^2\ge0
\qquad(-1\le v\le1).
\]
Thus the entire first generating circle lies in \(E_t\); the second follows by the isometry \((x,y,z)\mapsto(-x,z,y)\). Convexity of the ellipsoid then gives \(K_t\subseteq E_t\). For \(t>0\), we have \(p^2<1/3\) and therefore \(a>b\), so the circle-gauge inequality is strict unless \(v=p\). For \(t=0\), \(a=b=1\) and every point of either generating circle is a contact.

**2. Sharp unrestricted lower bound for every competitor.** For \(t>0\), the four circle contacts are
\[
w_1=(-c,d,0),\quad w_2=(-c,-d,0),\quad
w_3=(c,0,d),\quad w_4=(c,0,-d).
\]
Because \(c^2/a^2=1/3\) and \(d^2/b^2=2/3\), their images \(u_i=\operatorname{diag}(a^{-1},b^{-1},b^{-1})w_i\) obey the exact matrix identities
\[
\frac14\sum_{i=1}^4 u_i=0,\qquad
\frac14\sum_{i=1}^4 u_i u_i^{\mathsf T}=\frac13 I_3.
\]
In particular, the \(u_i\) are four points of the unit sphere with pairwise inner product \(-1/3\), hence a regular tetrahedron. The same four points can be selected from the two generating circles at \(t=0\) by taking \(p=-1/\sqrt3\).

Let \(F\) be **any** ellipsoid containing the normalized body \(\operatorname{diag}(a^{-1},b^{-1},b^{-1})K_t\). Write \(F=m+T B_2^3\), with \(m\in\mathbb R^3\) and \(T\) invertible. All four \(u_i\) belong to \(F\); consequently
\[
1\ge\frac14\sum_{i=1}^4\|T^{-1}(u_i-m)\|^2
=\frac13\operatorname{tr}((TT^{\mathsf T})^{-1})+\|T^{-1}m\|^2.
\]
The arithmetic–geometric mean inequality on the three positive eigenvalues of \((TT^{\mathsf T})^{-1}\) gives \(\det((TT^{\mathsf T})^{-1})\le1\), or \(|\det T|\ge1\). Therefore \(\operatorname{vol}_3(F)\ge \operatorname{vol}_3(B_2^3)\), proving that \(E_t\) is a global minimum-volume enclosing ellipsoid without any a priori symmetry assumption. Equality requires \(m=0\) and \(TT^{\mathsf T}=I_3\), so the optimal ellipsoid is unique.

**3. Exhaustive contact classification.** For \(t>0\), the strict square factorization in Step 1 leaves precisely two contact points on each generating circle, namely \(w_1,w_2\) and \(w_3,w_4\). The ellipsoid is strictly convex. A nontrivial segment joining two distinct points of \(E_t\) lies in its interior, so no point added by taking the convex hull of the two disks can create an additional contact. The four listed points are therefore the complete contact locus. For \(t=0\) the circle gauge is identically one and exactly the two full generating circles touch the optimal unit ball.

## Verification

The standard-library script `verify.py` tests the rational-parameter form \(t=3p-1/p\) with exact `Fraction` arithmetic at 1,074 distinct admissible rational choices of \(p\). At each it checks the semiaxis ratios, tangency identities, and the global squared-gap factorization at 41 rational circle parameters. It also checks the constant regular-tetrahedron covariance identities and 2,200 floating-point circle evaluations for widely spaced real separations. The recorded command is `python3 verify.py`; its expected summary begins `VERIFY_OK`. These finite diagnostics are corroboration; universal validity follows from the displayed algebra and determinant inequality.

## Relationship to prior work

Dirnböck and Stachel's 1997 full-text treatment of the oloid develops its boundary, rolling motion, area and volume. In §3 it also describes a distinguished ellipsoid **inscribed** in the oloid (their equation (26)); that is the opposite containment direction and does not provide its minimum-volume enclosing ellipsoid. Finch's 2012 arXiv paper (initial submission November 19, 2012) studies convex hulls of pairs of orthogonal unit disks and computes or asks about volume, surface area and mean width in special configurations; it does not give the present unrestricted enclosing-ellipsoid formula. Bäsel's 2016 full-text paper evaluates mean width and related integral-geometric quantities of the oloid. Nash, Pir, Sottile and Ying's 2016 preprint (later 2017 publication) classifies geometric and algebraic features of two-circle convex hulls rather than their minimum-volume enclosing ellipsoids. The published derivative law for orthogonal-disk mean width studies precisely the same moving-center family but a different invariant; a width derivative formula does not imply these semiaxes or the tetrahedral optimality certificate. Generic minimal-volume-ellipsoid existence and algorithms likewise do not supply this closed formula or its complete contact locus.

## Limitations

This is an exact mathematical statement for equal disks in perpendicular planes with centers on their common line. It does not establish analogous formulas for unequal radii, oblique planes, or general ellipsoid unions. The search of named sources and related public results does not establish absolute historical priority: an earlier calculation could be indexed under a different phrase or embedded in a general computational treatment. The regular tetrahedron is obtained **after normalizing by the optimal ellipsoid**; the unnormalized four contacts need not be equidistant. No independent scientific audit has been performed.

## References

1. H. Dirnböck and H. Stachel, “The Development of the Oloid,” *Journal for Geometry and Graphics* **1** (1997), 105–118, especially §3, equation (26). Full text: https://www.heldermann-verlag.de/jgg/jgg01_05/jgg0113.pdf.
2. S. R. Finch, “Convex Hull of Two Orthogonal Disks,” arXiv:1211.4514 (first public submission 2012-11-19), https://arxiv.org/abs/1211.4514.
3. U. Bäsel, “The mean width of the oloid and integral geometric applications of it,” arXiv:1604.07245 (2016), https://arxiv.org/abs/1604.07245.
4. E. Nash, A. F. Pir, F. Sottile, and L. Ying, “Convex Hull of Two Circles in R3,” arXiv:1612.09382 (2016), https://arxiv.org/abs/1612.09382.
5. “A one-dimensional derivative law for orthogonal-disk mean width,” published public record: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-one-dimensional-derivative-law-for-orthogonal-disk-mean-width--6e52fbc79bdf.
