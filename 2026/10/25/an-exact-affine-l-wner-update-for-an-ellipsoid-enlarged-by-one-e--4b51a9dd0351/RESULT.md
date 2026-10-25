# An exact affine Löwner update for an ellipsoid enlarged by one exterior point

## Finding

Let \(d\ge2\), let \(E_0\subset\mathbb R^d\) be a full-dimensional ellipsoid, and adjoin a single point \(p\) strictly outside it. The unique minimum-volume enclosing ellipsoid of \(K=\operatorname{conv}(E_0\cup\{p\})\) has an explicit center and shape matrix given below. Its contacts consist exactly of the external point and a full \((d-2)\)-dimensional latitude orbit on the original ellipsoid. In its own normalized coordinates, that orbit always has axial coordinate \(-1/d\), independently of the distance of the external point.

Write \(E_0=\{x:(x-m)^{\mathsf T}Q^{-1}(x-m)\le1\}\), where \(Q\) is real positive definite. Put \(v=p-m\) and \(H=\sqrt{v^{\mathsf T}Q^{-1}v}>1\). Define \(r\in(0,1/d)\) by
\[
d r^2+(d-1)Hr=1,\qquad r=\frac{2}{(d-1)H+\sqrt{(d-1)^2H^2+4d}}.\]
Set
\[
a=\frac{d(H+r)}{d+1},\quad c=\frac{H-dr}{d+1},\quad b^2=d a r=\frac{d^2(1-r^2)}{d^2-1}.\]
Then the unique enclosing ellipsoid is
\[
E_*=\{x:(x-m_*)^{\mathsf T}Q_*^{-1}(x-m_*)\le1\},
\]
where
\[
m_*=m+\frac cH v,\qquad Q_*=b^2 Q+\frac{a^2-b^2}{H^2}vv^{\mathsf T}.\]
The ratio of its volume to that of \(E_0\) is \(R_d(H)=a b^{d-1}\). If the added point lies in \(E_0\) instead, the unique Löwner ellipsoid remains \(E_0\).

For each fixed \(H>1\), the dimension-asymptotic refinement is
\[
R_d(H)=H-\frac{H-H^{-1}}{2d}+O_H(d^{-2})\qquad(d\to\infty).
\]
For each fixed integer \(d\ge2\), the large-distance limit is
\[
\lim_{H\to\infty}\frac{R_d(H)}H
=\frac d{d+1}\left(\frac d{\sqrt{d^2-1}}\right)^{d-1}.
\]

## Assumptions and scope

Euclidean volume is used in the full ambient dimension \(d\). The term Löwner ellipsoid always means the unique ellipsoid of **minimum volume containing** a body, not the maximum-volume contained John ellipsoid. The external point is genuinely outside \(E_0\), so \(H>1\); the case \(H\le1\) is the trivial unchanged-body boundary. The formula applies to every orientation and positive-definite \(Q\), with no axial symmetry assumption on \(E_0\) in original coordinates.

## Proof

**Affine reduction.** Apply the invertible map \(z=Q^{-1/2}(x-m)\) and rotate so that the image of \(p\) is \(H e_1\). The body becomes \(K_{d,H}=\operatorname{conv}(B_2^d\cup\{He_1\})\). Enclosing ellipsoids, their volumes up to a common determinant, and their contact conditions are preserved by this transformation.

**Feasibility with an exact certificate.** In normalized coordinates consider
\[
E=\left\{z:\frac{(z_1-c)^2}{a^2}+\frac{\|z_\perp\|^2}{b^2}\le1\right\}.
\]
The displayed quadratic for \(r\) has one positive root; its equation and \(H>1\) give \(0<r<1/d\). Direct substitution proves \(H-c=a\), \(c=a/d-r\), \(b^2=d a r=d^2(1-r^2)/(d^2-1)\), and \(a>b>1\). Thus the external apex is on \(E\). For any point \(z\in B_2^d\) with axial coordinate \(s=z_1\), we have \(\|z_\perp\|^2\le1-s^2\), and the *exact* factorization
\[
1-\left(\frac{(s-c)^2}{a^2}+\frac{1-s^2}{b^2}\right)
=\left(\frac1{b^2}-\frac1{a^2}\right)(s+r)^2\ge0.
\]
Hence the entire original ball and its convex hull with the apex lie in \(E\). On the ball the contact set is precisely \(s=-r\), \(\|z_\perp\|=\sqrt{1-r^2}\); the apex is the only additional contact, as a strict convex quadratic has strictly interior values on proper mixtures of distinct boundary points.

**Optimality and uniqueness.** Map \(E\) to \(B_2^d\) by \(y_1=(z_1-c)/a\), \(y_\perp=z_\perp/b\). The apex maps to \(e_1\), and every latitude contact maps to
\[
y=-\frac1d e_1+\sqrt{1-\frac1{d^2}}\,\omega,\qquad \omega\in S^{d-2}\subset e_1^\perp.
\]
Place mass \(1/(d+1)\) at \(e_1\) and mass \(d/(d+1)\) uniformly on that latitude. Its mean is zero and its second-moment matrix is \(I_d/d\): the axial second moment is \((1+d/d^2)/(d+1)=1/d\), while each transverse second moment equals \((d/(d+1))(1-d^{-2})/(d-1)=1/d\). For any other ellipsoid \(F=\{y:(y-w)^{\mathsf T}M^{-1}(y-w)\le1\}\) containing the transformed body, integrate its quadratic inequality against this contact probability measure. One obtains
\[
\frac1d\operatorname{tr}(M^{-1})+w^{\mathsf T}M^{-1}w\le1.
\]
Therefore \(\operatorname{tr}(M^{-1})\le d\), and the arithmetic-geometric mean inequality applied to the eigenvalues of \(M^{-1}\) gives \(\det M\ge1\). Equality requires \(w=0\), \(M=I_d\). Thus the unit ball is the unique minimum-volume enclosing ellipsoid in these coordinates. Undoing the affine map proves both optimality and uniqueness of the stated \(m_*\) and \(Q_*\).

**Volume and asymptotics.** In normalized coordinates the semiaxes are \(a,b,\ldots,b\), so \(R_d(H)=ab^{d-1}\). At fixed \(H>1\), expanding the positive quadratic root gives \(r=(dH)^{-1}+O_H(d^{-2})\). More precisely, using \(b^2=d^2(1-r^2)/(d^2-1)\), we obtain \(a=H+(H^{-1}-H)/d+O_H(d^{-2})\), and \(b^{d-1}=1+(1-H^{-2})/(2d)+O_H(d^{-2})\). Multiplication gives the claimed expansion. At fixed \(d\) and \(H\to\infty\), we have \(Hr\to1/(d-1)\), \(a/H\to d/(d+1)\), and \(b^2\to d^2/(d^2-1)\), yielding the second limit. No uniformity in simultaneous dimension and spike-distance growth is asserted.

## Verification

Run \(\texttt{python verify_cap.py}\) using only the Python standard library. The independent numerical diagnostics verify the quadratic and contact identities, sphere containment, affine shape matrix, and selected asymptotic regimes in dimensions from \(2\) to \(1200\). The script reported \(\texttt{PASS 18700 deterministic numerical diagnostics}\). Finite checks are supporting consistency tests, **not** a proof of the universal statements; the proof is above.

## Relationship to prior work

The general isotropic-contact characterization and uniqueness of extremal ellipsoids were established earlier; the present contact certificate uses that geometric structure but includes an explicit global minimizing ellipsoid. Todd's 1982 paper determines minimum-volume ellipsoids containing **cuts of an ellipsoid**, rather than the convex hull obtained by adjoining an exterior point. Güler–Gürtuna provide extremal-ellipsoid theory and examples for truncated cones, cylinders and slabs, but the inspected formulas do not specialize to the present spherical-patch-plus-apex body. Yıldırım studies outer ellipsoidal approximation of convex hulls of full-dimensional ellipsoids; his algorithms do not state this exact rank-one ball-plus-point formula or its contact geometry. Bezdek–Ivanov–Strachan discuss cap bodies and illumination, not optimal circumscribing ellipsoids. This is an evidence-limited comparison, not an assertion that all historical literature has been exhausted.

## Limitations

An exhaustive historical novelty guarantee is unavailable, particularly for equivalent statements in optimal experimental design or special-case updates to minimum-volume ellipsoids. The theorem assumes Euclidean volume and a single adjoined point; it is not a claim about multiple arbitrary points, minimum enclosing spheres, or maximum-volume contained ellipsoids. The large-dimension formula holds for fixed \(H>1\) and the long-spike formula for fixed \(d\).

## References

1. M. J. Todd, *On Minimum Volume Ellipsoids Containing Part of a Given Ellipsoid*, Mathematics of Operations Research **7** (1982), 253–261, doi:10.1287/moor.7.2.253.
2. O. Güler and F. Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707 (first posted 2007-09-05).
3. E. A. Yıldırım, *On the Minimum Volume Covering Ellipsoid of Ellipsoids*, SIAM Journal on Optimization, doi:10.1137/050622560 (2006).
4. K. Bezdek, R. Ivanov, C. Strachan, *Illuminating Spiky Balls and Cap Bodies*, arXiv:2204.04561 (2022).
