# Sharp random-shadow variance and constant-width rigidity of right prisms

## Finding
Let \(Q\subset\mathbb R^2\) be any compact convex body with nonempty interior, area \(A>0\), and planar width \(w_Q(v)\) in unit direction \(v\in S^1\). Write
\[
\mu=\frac1{2\pi}\int_0^{2\pi}w_Q(e_\theta)\,d\theta=\frac{\operatorname{per}(Q)}\pi,\qquad
\nu=\frac1{2\pi}\int_0^{2\pi}w_Q(e_\theta)^2\,d\theta,
\qquad s=\frac{\nu}{\mu^2}-1\ge0.
\]
For every height \(h>0\), form the right prism \(K_h=Q\times[-h/2,h/2]\subset\mathbb R^3\), and let \(B_h(U)\) be its ordinary two-dimensional orthogonal projection area onto \(U^\perp\), with \(U\) uniform on \(S^2\). Put
\[
q=\frac\pi4-\frac23>0,\qquad g=\frac23-\frac{\pi^2}{16}>0.
\]
**The entire height-optimized random-shadow variance and its rigidity profile are exact:**
\[
\boxed{\operatorname{Var}(B_h)=\frac{A^2}{12}-A\mu qh+\mu^2\left(g+\frac{2s}{3}\right)h^2,}
\]
\[
\boxed{h_*(Q)=\frac{Aq}{2\mu(g+2s/3)},\qquad
\min_{h>0}\frac{\operatorname{Var}(B_h)}{A^2}
=\frac1{12}-\frac{q^2}{4(g+2s/3)}.}
\]
In particular, for **every** planar convex base and every positive height,
\[
\boxed{\operatorname{Var}(B_h)\ge C_*A^2,\qquad
C_*=\frac1{12}-\frac{(\pi/4-2/3)^2}{4(2/3-\pi^2/16)}
=0.0125877019078079\ldots.}
\]
This constant is sharp, and equality holds **if and only if** \(Q\) has constant planar width and \(h=Aq/(2\mu g)\). Thus disks and noncircular constant-width bodies are equally optimal under the area normalization, each at its own determined height.

More precisely, the excess over the sharp constant after optimizing height is the exact increasing function of the base's normalized width variance:
\[
\boxed{\min_{h>0}\frac{\operatorname{Var}(B_h)}{A^2}-C_*
=\frac{q^2s}{6g(g+2s/3)}.}
\]
**A stronger equality consequence concerns the entire random-shadow law.** At the minimizing height of any constant-width base, put \(t=q/(2g)=1.1916910571\ldots>1\). For one uniform random variable \(Z\) on \([0,1]\), every such optimized prism satisfies
\[
\boxed{\frac{B_{h_*}}{A}\ \overset{\mathrm d}=\ Z+t\sqrt{1-Z^2}.}
\]
Thus different constant-width bases, including nonsmooth ones, have exactly the same *entire normalized shadow-area distribution*, not just its variance. Its cumulative distribution function is, writing \(r=\sqrt{1+t^2}\),
\[
\Pr(B_{h_*}/A\le y)=
\begin{cases}
0,&y<1,\\
1-\dfrac{y+t\sqrt{r^2-y^2}}{r^2},&1\le y<t,\\[4pt]
1-\dfrac{2t\sqrt{r^2-y^2}}{r^2},&t\le y\le r,\\[4pt]
1,&y>r.
\end{cases}
\]

No polygonality or smoothness assumption on \(Q\) is required. For a disk of radius \(R\), the unique minimizing cylinder height satisfies \(h_*/R=\pi q/(2g)=1.87190393517865\ldots\).

## Assumptions and scope
Areas, perimeters, heights and widths use their ordinary Euclidean normalizations. The plane \(U^\perp\) is chosen using the rotation-invariant probability on unoriented planes, equivalently by choosing \(U\) uniformly on the entire sphere. Base \(Q\) may be a smooth convex region, a polygon, or a convex body with mixed boundary regularity. The random variable \(B_h\) is the **planar shadow area**, not the one-dimensional projected width nor the random-section area. The lower bound compares shadow-area variance to the square of the **base area**, rather than to the square of the mean shadow area. The height is free to vary but the base itself is fixed. The sharp equality statement quantifies jointly over all eligible bases and all heights \(h>0\).

## Proof
**1. An exact pointwise brightness identity.** Let \(u=(\sqrt{1-z^2}\cos\phi,\sqrt{1-z^2}\sin\phi,z)\in S^2\). Project \(K_h\) onto \(u^\perp\). The projected prism is the Minkowski sum of the projected base and the projection of its vertical segment. The area of the projected base equals \(A|z|\), since orthogonal projection from the horizontal plane onto \(u^\perp\) scales planar area by \(|z|\). The projected vertical segment has length \(h\sqrt{1-z^2}\). By the elementary planar mixed-area identity, adding a segment of length \(\ell\) to a planar convex set increases area by \(\ell\) times the set's width perpendicular to the segment. The unit direction perpendicular to both \(u\) and the projected vertical segment is horizontal, and the corresponding width of the projected base equals that of the original \(Q\). Consequently
\[
B_h(u)=A|z|+h\sqrt{1-z^2}\,w_Q(v_\phi),
\]
where \(v_\phi\) is a horizontal unit vector obtained from the azimuth by a quarter-turn. This identity extends by continuity to polar directions; no limit case affects the Haar law.

**2. Spherical integration.** For Haar-uniform \(U\), \(Z=|U_3|\) is uniform on \([0,1]\), while \(v_\phi\) is independently uniform on \(S^1\). The elementary integrals are
\[
\mathbb EZ=\frac12,\quad \mathbb EZ^2=\frac13,\quad
\mathbb E\sqrt{1-Z^2}=\frac\pi4,\quad
\mathbb E(1-Z^2)=\frac23,\quad
\mathbb E\bigl[Z\sqrt{1-Z^2}\bigr]=\frac13.
\]
Expanding the pointwise brightness identity and using the definitions of \(\mu\) and \(\nu\) gives
\[
\mathbb EB_h=\frac A2+\frac{\pi\mu h}{4},\qquad
\mathbb EB_h^2=\frac{A^2}{3}+\frac{2A\mu h}{3}+\frac{2\nu h^2}{3}.
\]
Subtracting the squared mean proves
\[
\operatorname{Var}(B_h)=\frac{A^2}{12}-A\mu\left(\frac\pi4-\frac23\right)h+
\left(\frac{2\nu}{3}-\frac{\pi^2\mu^2}{16}\right)h^2.
\]

**3. Exact minimization and equality.** Since \(Q\) has positive area, its widths are continuous and positive. The identity
\[
\nu-\mu^2=\frac1{2\pi}\int_0^{2\pi}(w_Q(e_\theta)-\mu)^2\,d\theta\ge0
\]
shows \(s\ge0\), and the quadratic coefficient equals \(\mu^2(g+2s/3)>0\). Positivity of \(g\) follows from \(\pi^2<32/3\); positivity of \(q\) follows from \(\pi>8/3\). Hence the quadratic is strictly convex in \(h\), its unique minimizing height is positive, and completion of the square gives the first two boxed formulas. Because \(g+2s/3\ge g\), the minimum is at least \(C_*\). Equality requires \(s=0\), equivalent by continuity of the width function to \(w_Q\) being constant in every direction; conversely every body of constant width attains equality at the stated positive height. Subtracting \(C_*\) from the minimum gives the exact stability profile. Its derivative with respect to \(s\) is \(q^2/[6(g+2s/3)^2]>0\), proving strict growth away from constant width.

**4. Full-law universality.** If \(w_Q\equiv\mu\), the pointwise identity in step 1 reads \(B_h/A=Z+(h\mu/A)\sqrt{1-Z^2}\). At the unique optimal height, \(h\mu/A=q/(2g)=t\), independent of the particular base. For \(t>1\), the function \(f(z)=z+t\sqrt{1-z^2}\) increases from \(t\) to \(r=\sqrt{1+t^2}\) at \(z=1/r\) and then decreases to \(1\). Solving \(f(z)=y\) gives \(z_\pm=(y\pm t\sqrt{r^2-y^2})/r^2\). Counting the lengths of the sublevel intervals in uniform \(Z\) proves the displayed exact distribution function, including the regime switch at \(y=t\). That \(t>1\) follows from the elementary lower bound \(\pi>3.14\).

## Verification
The accompanying standalone standard-library Python program `verify.py` reproduces all scalar coefficients and the exact stability identity; it also tests the circular-base equality and the strict square-base inequality. Independently, for a unit-square base, the formula for the second shadow-area moment agrees identically at five heights with the three-dimensional orthotope identity, which is calculated by a different facet/minor decomposition. A deterministic two-dimensional midpoint quadrature over the actual square-prism brightness function independently tests the first and second spherical moments (with stated numerical tolerances). The program prints `VERIFY_OK`. The quadrature is diagnostic only; the continuous theorem follows from the explicit projection identity, elementary Haar integrals, and strict quadratic minimization above.

## Relationship to prior work
Finch's 2011 work [1] explicitly develops first and second **one-dimensional width** moments of the regular tetrahedron and cube, and motivates extending such calculations to other convex bodies. The full mathematical sections on planar squares, planar triangles, and three-dimensional polyhedra were inspected. That work does not optimize the variance of **two-dimensional shadow areas** for right prisms or characterize all constant-width equality bases.

Finch's 2012 treatment of planar projections [6] already gives mean-square shadow area for the regular cube (and other regular three-dimensional polytopes); its geometric examples do not yield the arbitrary-base sharp constant-width equality class. The 2015 study of Kabluchko–Litvak–Zaporozhets [2] develops higher moments of random one-dimensional projection lengths, not the right-prism shadow-area variance profile. The mathematical record [3] provides exact **two-dimensional shadow-area moments for all orthotopes**, thereby already covering the special case when \(Q\) is a rectangle: this case is a check, not a novelty claim. Its all-orthotope theorem does not quantify over arbitrary nonrectangular planar convex bases, including noncircular constant-width shapes, and therefore does not imply the sharp equality classification or the exact monotone width-variance profile stated here. The distinct record [4] computes second moments of one-dimensional widths of uniform regular prisms, not the two-dimensional shadow-area statistic. A further investigation [5] studies the area–perimeter **covariance** of circular-cylinder shadows, rather than optimized variance of area alone. No covering published statement was identified in the inspected mathematical sources or targeted topic searches, although the present proof relies on standard projection and mixed-area facts.

## Limitations
The theorem does not address tilted (oblique) prisms, nonuniform viewing directions, partial occlusions, surface-brightness effects, random sections, or full area-distribution laws. The sharp constant is normalized by fixed base area; other normalizations lead to different optimization questions. Elementary projection geometry makes the claim short to prove; no claim of a novel projection formula itself is made. There remains bibliographic uncertainty that an older stereological result under the terms 'caliper', 'brightness moment' or 'generalized cylinder' may contain an equivalent height-optimized inequality. 

## References
[1] S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, first public 4 October 2011, arXiv:1110.0671, https://arxiv.org/html/1110.0671v2.

[2] Z. Kabluchko, A. E. Litvak, D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, first public 26 November 2015, arXiv:1511.08479, https://arxiv.org/html/1511.08479v3.

[3] *Exact planar shadow-area moments for all orthotopes*, publicly available mathematical result, 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-planar-shadow-area-moments-for-all-orthotopes--0d2368f94d4d.

[4] *Exact mean-square width of every uniform regular prism*, publicly available mathematical result, 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-mean-square-width-of-every-uniform-regular-prism--eb371b3be549.

[5] *Exact cylinder shadow mixed moment and sharp positive covariance*, publicly available mathematical result, 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-cylinder-shadow-mixed-moment-and-sharp-positive-covariance--1feeb231b707.

[6] S. R. Finch, *Planar Projections and Second Intrinsic Volume*, first public 12 March 2012, arXiv:1203.2464, https://arxiv.org/html/1203.2464v1.
