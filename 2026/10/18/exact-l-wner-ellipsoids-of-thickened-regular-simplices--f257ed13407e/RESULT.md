# Exact Löwner ellipsoids of thickened regular simplices

## Finding

Let \(n\ge3\) and \(2\le k\le n-1\) be integers. Let \(U\subset\mathbb R^n\) be a \(k\)-dimensional linear subspace, and let \(v_0,\ldots,v_k\in U\) be the vertices of a centered regular \(k\)-simplex of circumradius one:
\[
\|v_i\|=1,\qquad \langle v_i,v_j\rangle=-1/k\quad(i\ne j),\qquad \sum_{i=0}^k v_i=0.
\]
For \(s\ge0\), define the rounded simplex, or ball parallel body,
\[
K_{n,k,s}=s\operatorname{conv}\{v_0,\ldots,v_k\}+B_2^n
=\operatorname{conv}\left(\bigcup_{i=0}^k(sv_i+B_2^n)\right).
\]
Set
\[
t=\frac{\sqrt{(n-k)^2s^2+4nk}-(n-k)s}{2n},\qquad
b^2=1+st,\qquad a^2=(1+st)(1+s/t).
\]
Then the **unique** ellipsoid of minimum \(n\)-volume containing \(K_{n,k,s}\) is
\[
\boxed{E_{n,k,s}=\{x:\|P_Ux\|^2/a^2+\|P_{U^\perp}x\|^2/b^2\le1\}.}
\]
Its exact volume is \(\kappa_n a^k b^{n-k}\), where \(\kappa_n=\pi^{n/2}/\Gamma(1+n/2)\). The parameter \(t\) is the unique positive solution of
\[
nt^2+(n-k)st=k.
\]
For every \(s>0\), the **complete** contact locus between \(K_{n,k,s}\) and \(E_{n,k,s}\) consists exactly of
\[
\boxed{\{(s+t)v_i+\sqrt{1-t^2}\,w:\ i=0,\ldots,k,\quad w\in U^\perp,\ \|w\|=1\}.}
\]
Every contact point obeys the separation-independent normalized law
\[
\boxed{\|P_Ux\|^2/a^2=k/n,\qquad \|P_{U^\perp}x\|^2/b^2=(n-k)/n.}
\]
The logarithm of the enclosing ellipsoid's volume is strictly concave as a function of \(s\ge0\):
\[
\boxed{\frac{d}{ds}\log\operatorname{vol}_n(E_{n,k,s})=\frac{k}{s+t}>0,\qquad
\frac{d^2}{ds^2}\log\operatorname{vol}_n(E_{n,k,s})<0.}
\]
At \(s=0\) the optimizer is the unit ball, and every point of its boundary is a contact point. As \(s\to\infty\), \(a/s\to\sqrt{n/k}\) and \(b\to\sqrt{n/(n-k)}\).

## Assumptions and scope

All sets and volumes are Euclidean. A containing ellipsoid may have an arbitrary center and arbitrary orientation; no rotational symmetry is imposed on a competing ellipsoid. The simplex is intrinsically \(k\)-dimensional and is embedded in dimension \(n>k\), ensuring that its unit-ball parallel body has nonempty \(n\)-dimensional interior. The center simplex is normalized to circumradius one, and the balls have radius one. Translation, common scaling, and orthogonal transformation give equivalent forms of the theorem. The restriction \(k\ge2\) concerns genuine simplex center configurations; two-center capsules are not asserted as a new case.

## Proof

**Step 1: the positive parameter and support-function containment.** For \(s>0\), the quadratic \(nt^2+(n-k)st-k\) has a unique positive zero, which belongs to \((0,\sqrt{k/n})\). At \(s=0\), take \(t=\sqrt{k/n}\). For a unit direction \(u\), put \(p=\|P_Uu\|\in[0,1]\). Then
\[
h_{K_{n,k,s}}(u)=1+s\max_i\langle v_i,P_Uu\rangle\le1+sp,
\]
with equality, for \(p>0\), precisely when \(P_Uu=pv_i\) for some index \(i\). The proposed ellipsoid's support function is \(h_E(u)=\sqrt{a^2p^2+b^2(1-p^2)}\). Direct substitution of the two semiaxis definitions gives the exact identity
\[
\boxed{a^2p^2+b^2(1-p^2)-(1+sp)^2=\frac{s}{t}(p-t)^2\ge0.}
\]
Therefore \(h_E\ge h_K\) in every direction, proving \(K_{n,k,s}\subseteq E_{n,k,s}\). For \(s=0\), both sets are the unit ball.

**Step 2: determine every contact.** For \(s>0\), equality of support functions forces \(p=t\) and \(P_Uu=t v_i\); hence the possible supporting normals are precisely
\[
u=t v_i+\sqrt{1-t^2}\,w,\qquad w\in U^\perp,\quad\|w\|=1.
\]
The convex body's unique support point for this normal is \(x=s v_i+u\). The ellipsoid support point is \(a^2t v_i/(1+st)+b^2\sqrt{1-t^2}w/(1+st)\), equal to the same \(x\) because \(a^2t/(1+st)=s+t\) and \(b^2=1+st\). Conversely every boundary intersection must share the unique supporting normal of the smooth ellipsoid and is therefore on this list. This proves the entire contact locus, without excluding any nongeneric points.

**Step 3: an explicit isotropic contact certificate.** The parameter equation is equivalent to \(nt(s+t)=k(1+st)\). It implies
\[
\frac{(s+t)^2}{a^2}=\frac{k}{n},\qquad
\frac{1-t^2}{b^2}=\frac{n-k}{n}.
\]
Scale \(E_{n,k,s}\) to the unit ball by \(T_0= a^{-1}P_U+b^{-1}P_{U^\perp}\). Its normalized contact points are
\[
y_{i,w}=\frac{s+t}{a}v_i+\frac{\sqrt{1-t^2}}{b}w.
\]
Choose an orthonormal basis \(e_1,\ldots,e_{n-k}\) of \(U^\perp\). Give equal weights to the \(2(k+1)(n-k)\) points \(y_{i,\varepsilon e_j}\), where \(i=0,\ldots,k\), \(j=1,\ldots,n-k\), and \(\varepsilon=\pm1\). The regular-simplex identity \((k+1)^{-1}\sum_i v_iv_i^{\mathsf T}=P_U/k\), together with the signed orthogonal-basis identity, gives
\[
\boxed{\operatorname{mean}y=0,\qquad
\operatorname{mean}(yy^{\mathsf T})=I_n/n.}
\]
Each of these contact points has unit Euclidean norm.

**Step 4: global optimality and uniqueness without symmetry assumptions.** Let any ellipsoid \(F=c+T(B_2^n)\), with invertible \(T\), contain the normalized body \(T_0 K_{n,k,s}\). Every chosen contact point \(y\) lies in \(F\), so averaging \(\|T^{-1}(y-c)\|^2\le1\) yields
\[
\frac1n\operatorname{tr}((TT^{\mathsf T})^{-1})+\|T^{-1}c\|^2\le1.
\]
The arithmetic-geometric mean inequality on the eigenvalues of \((TT^{\mathsf T})^{-1}\) gives \(|\det T|\ge1\), so \(F\) has at least unit-ball volume. If equality holds, both the center term and the eigenvalue inequality are equalities, forcing \(c=0\) and \(TT^{\mathsf T}=I_n\). Thus \(F\) is the unit ball itself. Undoing the normalization proves that \(E_{n,k,s}\) is the unique minimum-volume containing ellipsoid. The same argument with contact points of the unit sphere handles \(s=0\).

**Step 5: growth and strict logarithmic concavity.** Put \(V(s)=\kappa_n a^k b^{n-k}\). Using the expressions for \(a,b\),
\[
\log\frac{V(s)}{\kappa_n}=\frac n2\log(1+st)+\frac k2\log(1+s/t).
\]
Its partial derivative with respect to \(t\), holding \(s\) fixed, equals \(ns/[2(1+st)]-ks/[2t(s+t)]\), which vanishes by \(nt(s+t)=k(1+st)\). Differentiation along \(t=t(s)\) therefore gives
\[
(\log V)'=\frac{nt}{2(1+st)}+\frac{k}{2(s+t)}=\frac{k}{s+t}.
\]
Implicit differentiation yields
\[
t'(s)=-\frac{(n-k)t}{2nt+(n-k)s},\qquad 1+t'(s)=\frac{(n+k)t+(n-k)s}{2nt+(n-k)s}>0.
\]
Consequently \((\log V)''=-k(1+t')/(s+t)^2<0\). The formulas extend continuously and differentiably to \(s=0\). Finally the quadratic equation yields \(st\to k/(n-k)\); the asserted large-\(s\) semiaxis limits follow.

## Verification

The standalone Python 3 file `verify.py` uses only standard-library exact rational arithmetic. It checks the support-function factorization, parameter identity, both normalized-contact projection identities, the covariance scalar identities, and the growth derivative identities for 510 rational parameter configurations with \(3\le n\le16\), \(2\le k<n\). It also checks 3,060 exact rational support differences. Run it with `python3 verify.py`. These finite tests are supplementary and do not prove the all-parameter theorem; the preceding exact arguments prove it.

## Relationship to prior work

Yıldırım's 2005 preprint, subsequently published in 2006, treats approximation algorithms for minimum-volume ellipsoids covering convex hulls of arbitrary full-dimensional ellipsoids. The present rounded-simplex family is included in that broad input class, but the available abstract supplies neither the stated exact semiaxes nor the complete contact locus or logarithmic concavity. The full text could not be examined, so this comparison retains a historical-priority risk.

Güler and Gürtuna's September 2007 preprint supplies general Löwner ellipsoid and contact theory and exact solutions for slabs, truncated second-order cones, and cylinders obtained as convex hulls of parallel ellipsoidal slices. Its fully inspected class definitions and exact formulas do not cover the unit-ball parallel body of a regular simplex of affine dimension at least two. The general contact theory is classical; the asserted contribution is this explicit family-wide evaluation, complete contact description, and growth law. Two-center capsule configurations and related lens dualities do not imply the \(k\ge2\) geometry: the affine dimension of the centers' convex hull and its regular-simplex covariance structure change.

## Limitations

The theorem concerns Euclidean balls of equal radius placed at vertices of a regular simplex. It does not cover arbitrary arrangements of ball centers, nonregular simplices, unequal radii, or anisotropic offset bodies. The parameter \(s\) scales the simplex circumradius while the ball radius is fixed; the case \(s=0\) is degenerate only in the center configuration, not in the body. No independent audit has been performed. Historical priority, particularly relative to unavailable full-text algorithmic literature, remains subject to further checking.

## References

1. E. Alper Yıldırım, *On the Minimum Volume Covering Ellipsoid of Ellipsoids*, publicly posted January 14, 2005, Optimization Online, https://optimization-online.org/2005/01/1043/; SIAM Journal on Optimization 17 (2006), 621–641, doi:10.1137/050622560.
2. O. Güler and F. Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707, September 5, 2007, https://arxiv.org/abs/0709.0707.
3. F. John, *Extremum problems with inequalities as subsidiary conditions*, Studies and Essays Presented to R. Courant (1948), 187–204; standard circumscribed-ellipsoid contact conditions are recounted and proved in reference 2.
