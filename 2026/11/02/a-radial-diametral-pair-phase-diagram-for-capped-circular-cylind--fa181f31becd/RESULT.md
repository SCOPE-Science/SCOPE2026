# A radial diametral-pair phase diagram for capped circular cylinders

## Finding

Let \(S_{R,h}=\partial\{(x,y,z):x^2+y^2\le R^2,\ 0\le z\le h\}\), for \(R,h>0\), carry its intrinsic path metric, including both planar caps and the curved lateral surface. Let \(p_r=(r,0,h)\), \(q_r=(-r,0,0)\), with \(0\le r\le R\). These are opposite points in the upper and lower disks. Put
\[
G_{R,r}(t)=\begin{cases}
2R\cos(t/2),&0\le t\le 2\arcsin(r/R),\\
2\sqrt{R^2+r^2-2Rr\sin(t/2)},&2\arcsin(r/R)<t\le\pi,
\end{cases}\qquad 0\le t\le\pi.
\]
At \(r=0\) use the second branch except at \(t=0\), where both give \(2R\). The **exact intrinsic distance law for this pair**, valid at every aspect ratio, is
\[
\boxed{d_{S_{R,h}}(p_r,q_r)=\min_{0\le t\le\pi}\left\{G_{R,r}(t)+\sqrt{h^2+R^2t^2}\right\}.}\tag{1}
\]
The already known surface diameter is \(D=h+2R\) [Cerdán--Schnell--Segura Gomis, Section 6]. Define
\[
h_0=\frac{\pi^2-4}{4}R,\quad T_h(t)=h+2R-\sqrt{h^2+R^2t^2},\quad
E_h=\{t\in(0,\pi]:T_h(t)>2R\cos(t/2)\}.
\]
Define a **critical radius** by the entirely explicit one-variable infimum
\[
\boxed{r_c(h)=\begin{cases}
R,&E_h=\varnothing,\\
\displaystyle\inf_{t\in E_h}\left[R\sin(t/2)-\sqrt{T_h(t)^2/4-R^2\cos^2(t/2)}\right],&E_h\ne\varnothing.
\end{cases}}\tag{2}
\]
The radicand in the second line is positive, and the bracket lies strictly between zero and \(R\sin(t/2)\) for every \(t\in E_h\). The exact three-regime phase diagram is
\[
\boxed{r_c(h)=R\ (0<h\le h_0),\quad 0<r_c(h)<R\ (h_0<h<2R),\quad r_c(h)=0\ (h\ge2R).}\tag{3}
\]
For every \(0\le r\le R\), the pair \((p_r,q_r)\) is diametral **if and only if** \(r\le r_c(h)\). Thus the entire continuum of opposite-cap antipodal pairs is diametral until \(h=h_0\). The antipodal rim pair ceases to be diametral immediately above that sharp threshold. For every \(h>h_0\), **all** diametral pairs on \(S_{R,h}\) are the rotational images of \((p_r,q_r)\) with \(0\le r\le r_c(h)\) (and their reversals). In particular, for \(h\ge2R\) the two cap centers constitute the unique unordered diametral pair.

## Assumptions and scope

Here \(R,h>0\) and all paths stay on the **entire boundary of the solid cylinder**; no path may pass through its interior. A cap is a closed Euclidean disk; a rim belongs to both cap and side. The parameter \(t\) in (1)--(2) is the smaller angular separation, in radians, of two lateral-surface contacts. All formulas include zero-radius, rim, and transition endpoints by continuity. The result classifies every diametral pair only in the regime \(h>h_0\); for shorter cylinders it classifies **all opposite-cap antipodal pairs**, without asserting these exhaust the diametral locus.

## Proof

**1. Exact reduction to two rim contacts.** Every path from the upper disk to the lower disk contains a lateral subpath starting on the upper rim at some \(u\) and ending on the lower rim at some \(v\), with no intervening visit to either disk: choose the last upper-rim visit before the first lower-rim visit. Euclidean chord length bounds the prefix/suffix in their respective caps, while the unwrapped-cylinder inequality bounds that lateral subpath below by \(\sqrt{h^2+R^2t^2}\), where \(t\in[0,\pi]\) is the angular separation of \(u,v\). Conversely, a planar chord--shortest helical lateral segment--planar chord realizes any such candidate. Hence the distance equals the minimum over all rim contacts of \(|p_r-u|+\sqrt{h^2+R^2t^2}+|v-q_r|\).

**2. Exact angular minimization.** Rotate the lower rim back through angle \(t\) so that the two rim contacts coincide. Their cap-length sum becomes the sum of distances from one point on the radius-\(R\) circle to two foci of radius \(r\) whose angular separation is \(\pi-t\). In coordinates with the midpoint of the foci on the horizontal axis, the foci are \((m,\pm c)\), with \(m=r\sin(t/2)\), \(c=r\cos(t/2)\). For a prescribed focal sum \(2A\), the filled ellipse is centered at \((m,0)\) and has horizontal semiaxis \(B=\sqrt{A^2-c^2}\) and vertical semiaxis \(A\). Its largest squared distance from the origin is
\[
\max_{-1\le z\le1}\left(m^2+A^2+2mBz-c^2z^2\right).
\]
If the maximum occurs at an interior \(z=mB/c^2\), the first contact with the radius-\(R\) circle is at \(A=R\cos(t/2)\); its consistency condition is \(r\ge R\sin(t/2)\). Otherwise the maximum is at \(z=1\), and the first contact is at \(A=\sqrt{(R-m)^2+c^2}\), valid precisely when \(r\le R\sin(t/2)\). Degenerate focal configurations follow by direct limits. This proves \(G_{R,r}\) and (1). Notice that this minimization is not a heuristic symmetric-contact ansatz; both possible ellipse contacts are optimized.

**3. Diameter bound and its witnesses.** For two points on the side at levels \(z_1,z_2\), travel via the lower disk or the upper disk, taking whichever gives smaller total vertical travel. That vertical travel is at most \(h\), and the cap chord is at most \(2R\); hence the distance is at most \(h+2R\). For a side point and a cap point, a same-angle radial cap path followed by a generator similarly gives at most \(h+2R\). For points on opposite caps, choose a common-angle rim contact aligned with whichever point has greater radial coordinate, giving at most \(h+2R-|r_1-r_2|\); points on the same cap are at distance at most \(2R\). Conversely every path between the two cap centers necessarily travels at least \(R\) across each planar disk and at least \(h\) along the side, and a meridian achieves this lower bound. Hence \(D=h+2R\).

**4. Radius threshold.** In (1), the contact choice \(t=0\) gives exactly \(D\) for every \(r\). For a fixed positive \(t\), the competitor is strictly shorter exactly when \(G_{R,r}(t)<T_h(t)\). If \(T_h(t)\le2R\cos(t/2)\), no \(r\) works. Otherwise the second branch of \(G_{R,r}\) is strictly decreasing in \(r\) up to \(R\sin(t/2)\), where it meets the first branch. Solving \(G_{R,r}(t)=T_h(t)\) on that branch yields exactly the bracket in (2). Therefore, after intersection over all \(t\), the distance equals \(D\) precisely when \(0\le r\le r_c(h)\). At \(r=r_c(h)\), equality follows by continuity and the fact that all strict-shortcut sets are open in \(r\).

**5. Two sharp thresholds.** Put \(F_h(t)=2R\cos(t/2)+\sqrt{h^2+R^2t^2}\). Its derivative has the sign of \(Rt\cot(t/2)-h\) for \(0<t<\pi\). The function \(Rt\cot(t/2)\) strictly decreases from \(2R\) to zero. Thus \(F_h\) has at most one interior stationary point, which is a maximum. Therefore
\[
\min_{0\le t\le\pi}F_h(t)=\min\{h+2R,\sqrt{h^2+\pi^2R^2}\}.
\]
It follows that \(E_h\) is empty exactly when \(h\le h_0\). For \(h_0<h<2R\), \(E_h\) is nonempty but bounded away from \(t=0\), since \(F_h(t)-(h+2R)=\bigl(R^2/(2h)-R/4\bigr)t^2+O(t^4)>0\) near zero. The bracket in (2) then has positive infimum and is strictly smaller than \(R\). For \(h>2R\), this quadratic term is negative, and \(E_h\) includes arbitrarily small \(t\). At \(h=2R\), its leading term instead equals \(-Rt^4/96+O(t^6)<0\). Hence in both cases the bracket tends to zero along \(E_h\) as \(t\downarrow0\), proving \(r_c(h)=0\). This establishes (3).

**6. All diametral pairs above \(h_0\).** The side-only shortcut between any two side points is at most \(\sqrt{h^2+\pi^2R^2}<D\), so such a pair is not diametral. A side--cap pair is strictly closer than \(D\) by the same-angle rim construction, except possibly when both endpoints are opposite rims, already excluded. Same-cap pairs are at most \(2R<D\). Two opposite-cap points of radii \(r_1\ne r_2\) are strictly closer by the estimate in step 3. If their radii agree and are nonzero, but their angles differ by less than \(\pi\), choose the common rim contact in the direction of one endpoint: the chord to the other is strictly shorter than \(R+r\), so the distance is strictly below \(D\). The only remaining candidates are precisely the opposite-cap antipodal pairs in (1), completing the classification.

## Verification

The accompanying `verify.py` independently minimizes the original two-angle rim-contact functional and compares it with (1) for multiple aspect ratios/radii, tests the ellipse contact formula by angular minimization, checks the analytical endpoint threshold \(h_0\), and tests the three-phase structure by high-resolution one-dimensional searches. These finite tests are illustrative numerical cross-checks: the argument above, especially the focal-ellipse lemma and the lower-bound reduction, proves the all-parameter claims.

## Relationship to prior work

Cerdán, Schnell and Segura Gomis study exactly the same capped cylinder and **already prove its diameter \(h+2R\)**, as well as constant antipodal distance for \(h\le(\pi-2)R\). Their Section 6 also proves a closely related two-branch minimization for equatorial antipodes passing through one cap. Those statements are explicitly prior and are **not claimed as new**. The finding here is instead the complete radial classification of which **opposite-cap pairs** achieve that known diameter, its exact one-dimensional distance reduction, its distinct sharp thresholds \(h_0\) and \(2R\), and the full diametral-pair classification for \(h>h_0\). The published analysis of Bae--Korman--Okamoto concerns geodesic diameter and path multiplicity in planar polygonal domains; Mohar's later capped-cylinder construction concerns pursuit games, not extremal rim-contact profiles. This is a best-knowledge originality comparison, not a proof of historical priority.

## Limitations

The result concerns circular, not arbitrary convex, caps; equal-radius caps; the Euclidean product lateral metric; and **intrinsic** surface paths. The formula (2) is a one-dimensional explicit infimum, not an elementary closed form for \(r_c\) inside the middle regime. For \(h\le h_0\), the full diametral locus away from the two caps is not classified. No statement about independence from previously unindexed treatments, arbitrary cylinders, or external peer certification is made.

## References

1. A. Cerdán, U. Schnell and S. Segura Gomis, *On a Relative Isodiametric Inequality for Centrally Symmetric, Compact, Convex Surfaces*, Beiträge zur Algebra und Geometrie 54 (2013), 277--289, DOI:10.1007/s13366-012-0123-5. Author-preprint Section 6: https://f-n.hszg.de/fileadmin/Redakteure/Fakultaeten/Mathematik-und-Naturwissenschaften/hochschullehrer_innen/schnell/rel_isodiam.pdf .
2. S. W. Bae, M. Korman and Y. Okamoto, *The Geodesic Diameter of Polygonal Domains*, initial arXiv posting 2010-01-05, arXiv:1001.0695, https://arxiv.org/abs/1001.0695 .
3. B. Mohar, *The game of Cops and Robber on geodesic spaces*, Canadian Journal of Mathematics, DOI:10.4153/S0008414X24000543, Section 8 (capped-cylinder metric construction).
