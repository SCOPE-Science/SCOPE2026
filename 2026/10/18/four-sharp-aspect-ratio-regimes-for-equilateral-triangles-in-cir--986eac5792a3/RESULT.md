# Four sharp aspect-ratio regimes for equilateral triangles in circular cylinders

## Finding

Let \(d\ge3\), \(r>0\), \(h\ge0\), and consider the closed Euclidean cylinder
\[
C_{d}(h,r)=[0,h]\times \overline B^{d-1}(0,r)\subset\mathbb R^d.
\]
Let \(L_d(h,r)\) be the maximum side length of any equilateral Euclidean triangle with all three vertices in \(C_d(h,r)\). Put \(\lambda=h/r\). Then \(L_d\) is independent of \(d\), and its **complete sharp profile** is
\[
\frac{L_d(h,r)}r=
\begin{cases}
\sqrt{\lambda^2+\frac32+\frac12\sqrt{9-4\lambda^2}},
  &0\le\lambda\le\sqrt2,\\[3pt]
\frac{\lambda^2}{\sqrt{\lambda^2-1}},
  &\sqrt2\le\lambda\le\sqrt{\frac73},\\[3pt]
\frac{\sqrt{\lambda^2+3}+\sqrt3}{2},
  &\sqrt{\frac73}\le\lambda\le\frac4{\sqrt3},\\[3pt]
\frac4{\sqrt3},&\lambda\ge\frac4{\sqrt3}.
\end{cases}
\]
The transitions occur at the three **exact** height-to-radius ratios \(\sqrt2\), \(\sqrt{7/3}\), and \(4/\sqrt3\). In particular, the maximum side length stabilizes exactly when \(h\ge4r/\sqrt3\), not before.

There is also a complete equality description. For a maximizing triangle of side \(s=L_d(h,r)\), order its vertices by axial coordinate \(t_1\le t_2\le t_3\), and write
\[
u=(t_2-t_1)/s,\qquad v=(t_3-t_2)/s,\qquad k=u+v.
\]
If \(0<h<4r/\sqrt3\), then \(t_1=0\), \(t_3=h\), \(k=h/s\), and, up to exchanging \(u\) and \(v\), exactly these cases occur:
\[
(u,v)=
\begin{cases}
(0,k),&0<k^2\le\frac12,\\
\left(\frac{k-\sqrt{4-7k^2}}2,\frac{k+\sqrt{4-7k^2}}2\right),
  &\frac12\le k^2\le\frac47,\\
(k/2,k/2),&\frac47\le k^2<1.
\end{cases}
\]
For every such axial triple, the orthogonal projections of the three vertices to the transverse hyperplane are the unique (up to transverse rigid motion) planar triangle with squared distances \(s^2(1-u^2)\), \(s^2(1-v^2)\), \(s^2(1-k^2)\), translated so that its circumcenter is the cylinder axis. In particular, each projected vertex is on the radius-\(r\) sphere. At \(h=0\), the extremizers are the equilateral triangles inscribed in the transverse radius-\(r\) ball, with side \(\sqrt3r\). At and beyond the final transition, \(s=4r/\sqrt3\), \(k=1\), \(u=v=1/2\): the two axial extreme vertices project to one transverse boundary point, and the third projects to its antipode. This configuration may be translated freely along the axial interval subject to its axial span \(s\). These, modulo cylinder symmetries and permitted axial translation, are **all** maximizers.

## Assumptions and scope

The cylinder is *solid* and includes both end caps. Its cross section is a Euclidean ball, not an arbitrary convex set or a hollow cylindrical surface. Equilateral means all three Euclidean side lengths are equal; the triangle may lie in any two-dimensional affine plane and need not be perpendicular or parallel to the cylinder axis. All statements hold in any finite Euclidean ambient dimension \(d\ge3\). We allow the flat limit \(h=0\). No claim is made for a two-dimensional rectangle, for noncircular cylinders, or for other regular polygons.

## Proof

**1. Reduction to the minimum transverse enclosing ball.** Write a candidate triangle as \(P_i=(t_i,y_i)\), with \(t_i\in[0,h]\) and \(y_i\in\mathbb R^{d-1}\), and let its side length be \(s>0\). After relabelling \(t_1\le t_2\le t_3\), define \(u,v,k\) as above. The axial difference between any two vertices is at most their Euclidean separation, so \(0\le k\le1\). Orthogonal projection onto the transverse hyperplane yields a triangle with side squares
\[
a^2=s^2(1-u^2),\qquad b^2=s^2(1-v^2),\qquad c^2=s^2(1-k^2).
\]
The three projected points lie in an affine plane of dimension at most two, so their minimum enclosing ball has the same radius as their minimum enclosing circle in that plane. The cylinder's transverse-ball condition is equivalent to the radius of this unique minimum circle being at most \(r\), after a transverse translation. Conversely, if these three projected lengths form a triangle whose minimum-circle radius is at most \(r\), such an equilateral triangle is realizable in \(C_d(h,r)\) whenever \(sk\le h\): the Euclidean Pythagorean identity reconstructs all three spatial side lengths \(s\).

**2. The complete sharp transverse-radius envelope.** Put \(z=k^2\) and \(p=uv\). By Heron's identity, the squared projected triangle area is
\[
\mathcal A_\perp^2=\frac{s^4}{16}(3-4z+4p).
\]
We need only consider feasible \(0\le u\le v\), whence \(0\le p\le z/4\), with the projected area nonnegative. The largest projected side is \(a\). For an acute projected triangle, its minimum enclosing circle is its circumcircle; for a right or obtuse projected triangle, it is the circle with the longest side as diameter. In the acute case the normalized squared radius is
\[
\frac{R_{\rm circ}^2}{s^2}
=(1-z)\frac{(1+p)^2-z}{3-4z+4p}=F_z(p).
\]
The key exact derivative is
\[
\frac{\partial F_z}{\partial p}
=\frac{2(1-z)(2p+1)(p+1-2z)}{(3-4z+4p)^2}.
\]
Thus the acute-branch minimum moves from \(p=0\), to \(p=2z-1\), and finally to \(p=z/4\), with the transitions at \(z=1/2\) and \(z=4/7\). For completeness, when \(z>1/2\) there is an obtuse projected branch at \(u\le k-1/(2k)\). Its minimum-circle radius \(s\sqrt{1-u^2}/2\) decreases toward the right-triangle boundary. At that boundary the circumradius agrees continuously with the diameter radius, while the acute derivative is still negative: its boundary product \(p_b=1/2-1/(4z)\) satisfies
\[
(2z-1)-p_b=\frac{(2z-1)(4z-1)}{4z}>0.
\]
Hence the obtuse branch cannot beat the subsequent acute minimum. In the limiting collinear case \(k=1\), continuity and the direct diameter-circle rule give the same value. It follows that the **minimum possible enclosing-circle radius of the transverse projection of a unit-side equilateral triangle with normalized axial span \(k\)** is
\[
f(k)=
\begin{cases}
\displaystyle\frac{1-k^2}{\sqrt{3-4k^2}},&0\le k\le1/\sqrt2,\\[3pt]
\displaystyle k\sqrt{1-k^2},&1/\sqrt2\le k\le2/\sqrt7,\\[3pt]
\displaystyle\frac{4-k^2}{4\sqrt3},&2/\sqrt7\le k\le1.
\end{cases}
\]
All three minima are attained by the axial splits listed in the Finding. The displayed formulas agree at their interfaces. Differentiating each branch shows that \(f\) is continuous and strictly decreasing on \([0,1]\), from \(f(0)=1/\sqrt3\) to \(f(1)=\sqrt3/4\).

**3. Optimization over the axial span.** Every contained triangle satisfies the simultaneous sharp constraints
\[
s k\le h,\qquad s f(k)\le r,
\]
and, conversely, each permissible \(k\) admits a spatial triangle attaining its minimal transverse radius. Therefore
\[
L_d(h,r)=\max_{0\le k\le1}\min\left\{\frac h k,\frac r{f(k)}\right\},
\]
with the natural convention at \(k=0\) (and taking the flat case separately). Because \(r/f(k)\) strictly increases and \(h/k\) strictly decreases on \(k>0\), for \(0<h<4r/\sqrt3\) there is a unique maximizing crossing \(h/k=r/f(k)\). The crossing traverses the three branches of \(f\) at the aspect ratios
\[
\frac{h}{r}=\frac{k}{f(k)}\in
\left\{\sqrt2,\sqrt{\frac73},\frac4{\sqrt3}\right\}
\]
at the stated values of \(k\). Solving the elementary crossing equations gives, successively,
\[
\begin{aligned}
&s^2=h^2+\tfrac32r^2+\tfrac r2\sqrt{9r^2-4h^2},\\
&s=\frac{h^2}{\sqrt{h^2-r^2}},\\
&s=\frac{\sqrt{h^2+3r^2}+\sqrt3r}{2}.
\end{aligned}
\]
For \(h\ge4r/\sqrt3\), the endpoint \(k=1\) attains \(s=r/f(1)=4r/\sqrt3\), and no other \(k\) can do better. This proves the complete formula and the exact onset of saturation.

**4. Sharpness and equality.** The minimizing splitting product \(p\) is unique on each regime, except only for the harmless interchange of the two consecutive gaps \(u,v\). At the optimum before saturation, both span and circle constraints are tight. The projected triangle is acute (right at the first threshold), with a unique minimum circle; hence its projected circumcenter is forced to the cylinder axis and the three projected vertices lie on the lateral boundary. The axial projections and transverse shape are thereby fixed up to the cylinder's rigid symmetries. At saturation, equality in the transverse bound forces \(k=1\) and \(u=v=1/2\), yielding precisely the antipodal projection described in the Finding. The construction explicitly realizes every equality case. Dimension independence follows since a two-dimensional transverse affine plane is available for all \(d\ge3\).

## Verification

The standalone, standard-library-only program `verify.py` reconstructs maximizing triangles directly from their axial coordinates and transverse distance data; it checks all three spatial side lengths, axial containment, and transverse disk containment. It also independently computes minimum covering circles of projected triangles, samples spatial orientations, and checks exact rational algebra identities from the three envelope branches. Run using `python3 verify.py` beside this file. Expected output begins `VERIFY_OK` and includes 2,000 constructed witnesses, 77,088 admissible projected-grid checks, and 132,000 random spatial-orientation checks. These finite diagnostics are **not** a substitute for the all-parameter analytical proof above.

## Relationship to prior work

Horváth's *Triangle in a brick* (arXiv:1010.1607, first posted October 8, 2010) concerns equilateral triangles in **rectangular boxes of volume one**, with each box edge at least \(1/\sqrt2\), and studies particular sharp length bounds and equality cases. The present theorem concerns an arbitrary-height **circular cylinder** and produces a full three-transition aspect-ratio law, including unrestricted triangle orientation and all equality configurations. Neither the shape restrictions nor the quantitative conclusions imply one another. The classical minimum-enclosing-circle theorem for three planar points supplies the acute/obtuse dichotomy used here; by itself it does not optimize the three possible axial-gap configurations or determine the cylinder phase transitions. The corresponding extremal tetrahedron-volume problem for a cylinder also has a different objective.

## Limitations

No claim is made of an absolute priority determination: older literature could conceivably contain an equivalent cylinder-specific profile under different terminology. The random and finite checks establish neither infinite-dimensional claims nor universal uniqueness; those claims follow solely from the analytic proof. The theorem is restricted to finite Euclidean dimensions \(d\ge3\) with a circular transverse ball and does not address noncircular cylinders or general simplices.

## References

1. Á. G. Horváth, *Triangle in a brick*, arXiv:1010.1607v1, public preprint dated 2010-10-08, https://arxiv.org/pdf/1010.1607 (full six-page manuscript inspected).
2. G. Chrystal, *On the problem to construct the minimum circle enclosing n given points in a plane*, Proceedings of the Edinburgh Mathematical Society 3 (1884), 30–33, DOI 10.1017/S0013091500037238 (historical minimum-circle method; publisher's online extract inspected).
3. IMO 1984 shortlist, problem 13, concerning inscribed tetrahedron volume in a right circular cylinder, https://tamnd.github.io/brain/practice/maths/shortlist/1984/13/ (distinct extremal problem; public solution inspected).
