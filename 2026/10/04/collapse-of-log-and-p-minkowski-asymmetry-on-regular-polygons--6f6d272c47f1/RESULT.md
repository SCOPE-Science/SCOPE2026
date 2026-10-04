# Collapse of log and p-Minkowski asymmetry on regular polygons

## Finding

Let \(P_n\subset\mathbb R^2\) be a regular Euclidean \(n\)-gon, \(n\ge3\). For Jin's planar log-Minkowski measure of asymmetry \(\operatorname{as}_0\), and for Guo's standard \(p\)-Minkowski measures of asymmetry \(\operatorname{as}_p\) for every \(1\le p\le\infty\),
\[
\operatorname{as}_p(P_n)=
\begin{cases}
1,&n\ \text{even},\\[1mm]
\sec(\pi/n),&n\ \text{odd}.
\end{cases}
\]

Thus every standard \(p\)-measure, including the log endpoint, collapses to one value on each regular polygon. For odd \(n\), there is a sharp change in the critical-point set:
\[
C_1(P_n)=\operatorname{int}(P_n),
\]
whereas for every \(1<p\le\infty\) the unique \(p\)-critical point is the polygon center.

At the center, the normalized \(p\)-mixed-volume expression also equals \(\sec(\pi/n)\) for every \(0<p<1\). Consequently, Jin's Section 4 extension has this same value when its definition is read as the \(\overline V_p\) quantity used explicitly in the proof of that section.

For odd \(n\),
\[
\sec(\pi/n)
=
1+\frac{\pi^2}{2n^2}
+\frac{5\pi^4}{24n^4}
+O(n^{-6}).
\]
The triangle endpoint gives \(2\), agreeing with the extremal value in Jin's theorem.

## Assumptions and scope

The polygon may have any circumradius \(R>0\); all measures used here are affine, hence scale, invariant. The proof below fixes the center at the origin and writes
\[
r=R\cos(\pi/n)
\]
for the inradius.

For \(1\le p<\infty\), Guo's measure is
\[
\mu_p(P,x)^p
=
\int_{\mathbb S^1}
\left(\frac{h_x(P,-u)}{h_x(P,u)}\right)^p
\,dm_x(P,u),
\qquad
\operatorname{as}_p(P)=\inf_{x\in\operatorname{int}P}\mu_p(P,x),
\]
with the cone-volume probability measure \(m_x\). The \(p=\infty\) endpoint is the corresponding supremum ratio. Jin's \(\operatorname{as}_0\) is the normalized log-mixed volume at the unique \(\infty\)-critical point.

The statement about \(0<p<1\) concerns the normalized \(p\)-mixed-volume extension at that \(\infty\)-critical point, as used in Jin's Section 4 proof; it is separated from the unambiguous standard \(p\ge1\) definition because the accessible text has a typographical or extraction ambiguity in the displayed Section 4 definition.

## Proof

If \(n\) is even, \(P_n\) is centrally symmetric, so every measure in question equals \(1\).

Assume now that \(n\) is odd. Let \(u_0,\ldots,u_{n-1}\) be the outward unit normals of the sides. Every side has the same length \(s\), and
\[
\sum_{i=0}^{n-1}u_i=0.
\]
At the center,
\[
h(P_n,u_i)=r,
\qquad
h(P_n,-u_i)=R.
\]
The second identity holds because, for odd \(n\), the direction opposite a side normal points toward a vertex.

The ordinary Minkowski asymmetry at the center is therefore \(R/r\). It is also globally optimal: for every direction \(u\),
\[
h(P_n,-u)\le R,\qquad h(P_n,u)\ge r,
\]
so
\[
\frac{h(P_n,-u)}{h(P_n,u)}\le \frac Rr,
\]
with equality at the side normals. Hence
\[
\operatorname{as}_\infty(P_n)=\frac Rr=\sec(\pi/n).
\]
Rotational symmetry and uniqueness of the planar \(\infty\)-critical point place that point at the polygon center.

The cone-volume measure of the centered polygon gives mass \(1/n\) to every side normal, since
\[
A(P_n)=\frac{nsr}{2}.
\]
Therefore Jin's logarithmic definition gives
\[
\log \operatorname{as}_0(P_n)
=
\frac1n\sum_{i=0}^{n-1}\log\frac Rr
=
\log\frac Rr,
\]
and thus
\[
\operatorname{as}_0(P_n)=\frac Rr.
\]

It remains to treat Guo's standard \(p\)-measures. For \(x\in\operatorname{int}(P_n)\), put
\[
t_i=\langle x,u_i\rangle.
\]
Then
\[
h_x(P_n,u_i)=r-t_i,
\qquad
h_x(P_n,-u_i)=R+t_i,
\]
and the cone-volume mass of \(u_i\) is
\[
\frac{r-t_i}{nr}.
\]
Consequently, for \(1\le p<\infty\),
\[
\mu_p(P_n,x)^p
=
\frac1{nr}
\sum_{i=0}^{n-1}
(R+t_i)^p(r-t_i)^{1-p}.
\]

For \(p=1\), this becomes
\[
\mu_1(P_n,x)
=
\frac1{nr}
\sum_{i=0}^{n-1}(R+t_i)
=
\frac Rr,
\]
because \(\sum_i t_i=\langle x,\sum_i u_i\rangle=0\). Hence every interior point is \(1\)-critical.

For \(p>1\), define
\[
f_p(t)=(R+t)^p(r-t)^{1-p}.
\]
A direct differentiation gives
\[
f_p''(t)
=
p(p-1)(R+r)^2
(R+t)^{p-2}(r-t)^{-p-1}>0
\]
throughout the admissible interval. Since the average of the \(t_i\) is zero, Jensen's inequality yields
\[
\frac1n\sum_i f_p(t_i)\ge f_p(0)=R^pr^{1-p}.
\]
Thus
\[
\mu_p(P_n,x)\ge\frac Rr.
\]
Equality in strict Jensen occurs only when all \(t_i=0\). The side normals span \(\mathbb R^2\), so this forces \(x=0\). Therefore
\[
\operatorname{as}_p(P_n)=\frac Rr
\]
for every \(1<p<\infty\), with the center as unique critical point. The already established \(p=\infty\) case completes the standard spectrum.

Finally, for \(0<p<1\), the centered support ratio is constant on the cone-volume support, equal to \(R/r\). Hence every normalized \(p\)-mixed volume \(\overline V_p(P_n,-P_n)\) at the center is exactly \(R/r\). This is the quantity used in Jin's Section 4 comparison proof.

## Verification

The accompanying `verify.py` reconstructs regular polygons directly from their vertices. For every \(3\le n\le31\) it checks the side-normal support values. For odd \(n\), it checks the center formula for several \(p\)-values, verifies numerically on random interior points that the \(p=1\) expression is center-independent, and checks the strict-convexity lower-bound behavior for \(p>1\).

The script was replayed from its packaged path and prints:

`VERIFY_OK regular polygon p-asymmetry spectrum`

The finite computations are consistency checks only. The all-\(n\), all-\(p\) theorem is supplied by the support-function calculation and Jensen argument above.

## Relationship to prior work

Guo introduced the standard \(p\)-measures for \(1\le p\le\infty\). Guo, Guo, and Su later emphasized the structural question of when
\[
\operatorname{as}_1(C)=\operatorname{as}_\infty(C),
\]
which forces all intermediate standard \(p\)-measures to coincide, and supplied formulas and examples for coproducts.

Jin introduced the planar log-Minkowski measure and connected it to normalized \(p\)-mixed volumes, including a planar extension to \(0<p<1\). The accessible full text contains no occurrence of “polygon” and gives no regular-polygon evaluation.

The present result supplies a canonical infinite family of non-symmetric bodies for which the whole standard \(p\)-spectrum collapses, computes the log endpoint exactly, and identifies the critical-point-set transition at \(p=1\). Targeted searches for regular polygons together with \(p\)-measure, log-Minkowski asymmetry, mixed-volume asymmetry, and the secant value did not locate an equivalent statement or a stronger result implying it.

## Limitations

The exact formula uses the equal side-normal geometry of regular polygons. It does not classify arbitrary equiangular or cyclic polygons, nor does it classify all planar bodies for which \(\operatorname{as}_1=\operatorname{as}_\infty\).

The \(0<p<1\) clause is stated with an explicit interpretation because the accessible text of Jin's displayed Definition 4.1 is ambiguous, while the proof immediately uses \(\overline V_p\). The standard \(p\ge1\) result and the log endpoint are independent of that ambiguity.

The literature search was targeted rather than exhaustive. In particular, the ordinary Minkowski asymmetry \(\sec(\pi/n)\) for odd regular polygons is elementary enough that it may appear in older sources under different terminology. The originality claim concerns the combined log/\(p\) spectrum and critical-point structure after comparison with the located literature.

## References

Q. Guo, “On p-measures of asymmetry for convex bodies,” Advances in Geometry 12 (2012), 287–301, DOI 10.1515/advgeom.2011.052.

Q. Guo, J. Guo, and X. Su, “The measures of asymmetry for coproducts of convex bodies,” Pacific Journal of Mathematics 276 (2015), 401–418, DOI 10.2140/pjm.2015.276.401.

H. Jin, “The log-Minkowski measure of asymmetry for convex bodies,” Geometriae Dedicata 196 (2018), 27–34, DOI 10.1007/s10711-017-0302-5.
