# Exact sparse-direction covariograms and two symmetry-axis overlap reversals for cross-polytopes

## Finding
For an integer \(d\ge3\), write
\[C_d=\bigl\{x\in\mathbb R^d:\sum_{i=1}^d|x_i|\le1\bigr\},\qquad V_d=\operatorname{vol}_d(C_d)=\frac{2^d}{d!}.\]
For \(k\in\{1,2,3\}\), put \(v_k=e_1+\cdots+e_k\) and \(G_{d,k}(t)=\operatorname{vol}_d(C_d\cap(C_d+t v_k))\). The exact fractional overlap for \(0\le t\le2/k\) is
\[
\frac{G_{d,k}(t)}{V_d}=\begin{cases}
(1-t/2)^d,&k=1,\\
(1-t)^{d-1}\bigl(1+(d-2)t/2\bigr),&k=2,\\
A^{d-2}\bigl(A^2+(d/2)aA+d(d-1)a^2/12\bigr),&k=3,
\end{cases}
\qquad a=3t/2,\quad A=1-a.
\]
For \(t>2/k\), the intersection has zero \(d\)-volume. Signed coordinate permutations of the translation vector give the same law.

In three dimensions these are the three kinds of rotational-symmetry axes of the regular octahedron. At equal *Euclidean* translation distance \(s\), set \(H_k(s)=G_{3,k}(s/\sqrt{k})\); the profiles, within their positive supports, are
\[
H_1(s)=\frac43\bigl(1-s/2\bigr)^3,\qquad
H_2(s)=\frac23\bigl(1-s/\sqrt2\bigr)^2\bigl(2+s/\sqrt2\bigr),\qquad
H_3(s)=\frac43-\sqrt3\,s+\frac12 s^2.
\]
There are exactly two strict-order reversals within the common interval \(0<s<2/\sqrt3\), at
\[
s_{13}=\frac{3-\sqrt{24\sqrt3-39}}2=0.698560766237849\ldots,\qquad
s_{12}=\frac{3-\sqrt{9-6\sqrt2}}{1+\sqrt2}=0.945467749979010\ldots.
\]
The rankings on the three consecutive open intervals are, respectively,
\[
H_2>H_3>H_1,\qquad H_2>H_1>H_3,\qquad H_1>H_2>H_3.
\]
Thus the vertex axis first overtakes the face-normal axis, and then overtakes the edge-midpoint axis. These are comparisons of *three symmetry-axis profiles*, not a global extremality theorem over arbitrary directions.

## Assumptions and scope
All volumes are ordinary Euclidean Lebesgue volumes, with \(C_d\) having vertices \(\pm e_i\) (edge length \(\sqrt2\)). The separation parameter \(t\) is a coordinate displacement, while \(s=\sqrt k\,t\) is the Euclidean distance between the two centers. The formulas cover every real \(t\ge0\), all integers \(d\ge3\), and \(k=1,2,3\). By central symmetry they extend to negative \(t\) after replacing \(t\) by \(|t|\). Endpoints are included by continuity.

## Proof
**Support.** By central symmetry, the difference body of \(C_d\) is \(2C_d\). Hence \(C_d\cap(C_d+t v_k)\) is empty if \(k t>2\), and at \(k t=2\) it is lower-dimensional. The \(d\)-volume of \(C_d\) is \(2^d/d!\) from its \(2^d\) congruent simplicial orthants.

**One displaced coordinate.** For every \(x\),
\[
\max\{\|x\|_1,\|x-te_1\|_1\}=|x_1-t/2|+t/2+\sum_{i=2}^d|x_i|.
\]
Therefore the intersection is the \(\ell_1\) ball of radius \(1-t/2\) centered at \(te_1/2\). Its volume proves the first formula.

**Two equally displaced coordinates.** Write \(u=x_1+x_2\), \(v=x_1-x_2\), and \(r=\sum_{i=3}^d|x_i|\). The identity \(|x_1|+|x_2|=\max\{|u|,|v|\}\), together with the Jacobian \(dx_1\,dx_2=du\,dv/2\), transforms the two \(\ell_1\)-ball inequalities into the intersection of squares \(|u|,|v|\le1-r\) and \(|u-2t|,|v|\le1-r\). The first-two-coordinate intersection area is exactly \(2(1-r)(1-r-t)\) if \(0\le r\le1-t\), and zero otherwise. In dimension \(d\ge3\), integration over \(d-2\) remaining coordinates uses the radial \(\ell_1\) shell density \(2^{d-2}r^{d-3}/(d-3)!\). Thus
\[
G_{d,2}(t)=\frac{2^{d-1}}{(d-3)!}\int_0^{1-t}r^{d-3}(1-r)(1-r-t)\,dr
=\frac{2^d}{d!}(1-t)^{d-1}\left(1+\frac{d-2}{2}t\right).
\]

**Three displaced coordinates: the base lens.** First work in \(\mathbb R^3\). Fix the third coordinate \(z\). The two cross-sectional \(\ell_1\) disks have radii \(R_1=1-|z|\) and \(R_2=1-|z-t|\), with centers displaced by \((t,t)\). The preceding \((u,v)\)-square transformation gives the area of their overlap. For \(0\le z\le t\) it is \((2-3t)(1-\max\{z,t-z\})\). On the two exterior intervals, which are related by reflection about \(z=t/2\), it is \((2R-3t)(R-t)\), with \(R\) varying from \(3t/2\) to \(1\). These are all positive cross-sections when \(0\le t\le2/3\). Consequently
\[
\begin{aligned}
G_{3,3}(t)&=2\int_{3t/2}^1(2R-3t)(R-t)\,dR
+(2-3t)\int_0^t(1-\max\{z,t-z\})\,dz\\
&=\frac43-3t+\frac32t^2
=\frac23(1-3t/2)(2-3t/2).
\end{aligned}
\]
The last product uses radii in the unit ball; equivalently the radius-\(R\) lens has volume \(\frac23 R(R-a)(2R-a)\), where \(a=3t/2\), whenever \(R\ge a\).

**Three displaced coordinates: general dimension.** For \(d>3\), fix the other \(d-3\) coordinates with \(\ell_1\) norm \(r\). The remaining three-dimensional lens has radius \(R=1-r\) and nonempty interior precisely for \(0\le r<A\), \(A=1-a\). Integrating its exact volume against the shell density \(2^{d-3}r^{d-4}/(d-4)!\) yields
\[
G_{d,3}(t)=\frac{2^{d-2}}{3(d-4)!}
\int_0^A r^{d-4}(1-r)(A-r)(2(1-r)-a)\,dr.
\]
Put \(w=A-r\), so the last three factors become \(a^2w+3aw^2+2w^3\). The beta integral \(\int_0^A r^mw^j\,dr=m!j!A^{m+j+1}/(m+j+1)!\) gives
\[
G_{d,3}(t)=\frac{2^d}{d!}A^{d-2}\left(A^2+\frac d2aA+\frac{d(d-1)}{12}a^2\right).
\]
The same expression reproduces the directly proved \(d=3\) case.

**Sharp symmetry-axis ranking.** Expanding the three cubic or quadratic profiles gives
\[
H_1-H_2=-\frac s6\bigl((1+\sqrt2)s^2-6s+12-6\sqrt2\bigr),
\]
\[
H_1-H_3=-\frac s6\bigl(s^2-3s+12-6\sqrt3\bigr),
\]
\[
H_2-H_3=\frac s6\bigl(\sqrt2 s^2-3s+6(\sqrt3-\sqrt2)\bigr).
\]
The quadratic in the last expression has positive leading coefficient and discriminant \(57-24\sqrt6<0\); therefore \(H_2>H_3\) throughout their common positive support. Each of the first two quadratic factors has exactly one root in \((0,2/\sqrt3)\), namely \(s_{12}\) and \(s_{13}\). At \(s=s_{13}\) the strict inequality \(H_2>H_3=H_1\) shows \(s_{13}<s_{12}\). Their signs at small \(s\) and at the support boundary give precisely the three asserted ranking regimes; no other crossings are possible.

## Verification
The standalone `verify_octahedral.py` uses symbolic rational identities to reconstruct the one-parameter three-dimensional lens integral, checks the all-dimensional shell integral identities in dimensions \(3\) through \(12\), verifies the exact comparison polynomials, and independently reconstructs three-dimensional intersection volumes from eight facet inequalities using SciPy convex hulls at 18 interior parameter values. The observed output is `OCTAHEDRAL_COVARIOGRAM_OK` with both crossing constants. Finite-dimensional symbolic checks and sampled convex hulls independently corroborate, but do not replace, the integral proof for every \(d\ge3\).

## Relationship to prior work
Bianchi's 2008 covariogram theorem establishes that the full covariogram determines any three-dimensional convex polytope, up to its inherent ambiguities. This is a uniqueness result, not an explicit evaluation of the three symmetry-axis overlap profiles. Ciccariello's 2014 regular-octahedron autocorrelation formulas are *orientation-averaged functions of translation length*; averaging directions does not determine any single fixed-axis overlap profile or the two ranking reversals. Work on optimal translations of arbitrary polytope pairs treats a broader optimization task but does not state these exact all-dimensional sparse-axis polynomials. The present result concerns an explicitly defined continuous geometric covariogram, not discrete lattice overlap counts or the polar cube's distinct covariogram. The novelty assessment is limited to inspected sources and does not establish historical priority.

## Limitations
Only signed-permutation images of displacements with one, two, or three equally sized nonzero coordinates are treated. The axis-ranking result concerns the three octahedral symmetry classes, **not the global maximizer among arbitrary directions**. No general formula for other translation patterns, complete directional anisotropy order, or independent mathematical audit is claimed. Unindexed geometric-scattering formulas may predate these identities.

## References
- G. Bianchi, *The covariogram determines three-dimensional convex polytopes*, arXiv:0805.1605v1, first posted 12 May 2008. https://arxiv.org/abs/0805.1605
- S. Ciccariello, *The correlation functions of the regular tetrahedron and octahedron*, arXiv:1407.2788v1, first posted 10 July 2014. https://arxiv.org/abs/1407.2788
- H.-K. Ahn, S.-W. Cheng and I. Reinbacher, *Maximum overlap of convex polytopes under translation*, Computational Geometry 46 (2013), 552–565, DOI 10.1016/j.comgeo.2011.11.003.
