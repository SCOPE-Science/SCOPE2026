# Complete planar-section area profile of the Steinmetz bicylinder

## Finding
Let \(R>0\) and let the right-angle equal-radius bicylinder be
\[
K_R=\{(x,y,z)\in\mathbb R^3:x^2+z^2\le R^2,\ y^2+z^2\le R^2\}.
\]
For a nonzero normal \(n=(n_1,n_2,n_3)\), write \(a=\max(|n_1|,|n_2|)\), \(b=\min(|n_1|,|n_2|)\), \(c=|n_3|\), and \(\rho=(a^2+b^2+c^2)^{1/2}\). Let \(A_R(n)\) be the Euclidean area of the central planar section \(K_R\cap\{n\cdot x=0\}\). When \(a,b,c>0\), its complete directional profile is
\[
\boxed{A_R(n)=\frac{R^2\rho}{ab}\left[(a+b)\arctan\frac{a+b}{c}-(a-b)\arctan\frac{a-b}{c}\right].}
\]
This expression extends continuously to every nonzero normal. Explicitly, for \(a>0\), at \(c=0\), \(A_R(n)=\pi R^2\rho/a\); at \(b=0<c\),
\[
A_R(n)=\frac{2R^2\rho}{a}\left[\arctan\frac ac+\frac{ac}{a^2+c^2}\right];
\]
and at \(a=b=0\) it equals \(4R^2\).

The sharp central-section range is
\[
\boxed{\pi R^2\le A_R(n)\le\pi\sqrt2\,R^2.}
\]
The lower equality holds **exactly** for the two coordinate planes \(x=0\) and \(y=0\). The upper equality holds **exactly** for the two diagonal planes \(x+y=0\) and \(x-y=0\). Every affine (possibly noncentral) planar section has area at most \(\pi\sqrt2\,R^2\), with equality exactly for those two *central* diagonal planes. Every value of the central interval occurs.

There is also a strict directional-balancing principle: keeping \(a^2+b^2>0\) and \(c\ge0\) fixed, the central area increases strictly as the nonnegative pair \((a,b)\), \(a\ge b\), is balanced toward equality. Along the balanced meridian \(a=b>0\), put \(r=c/a\). The area divided by \(R^2\) is
\[
F(r)=2\sqrt{r^2+2}\arctan(2/r),\quad r>0,
\]
with endpoint values \(F(0)=\pi\sqrt2\) and \(F(\infty)=4\). It has exactly one interior critical point, a strict **minimum**, at the unique positive root of
\[
r(r^2+4)\arctan(2/r)=2(r^2+2),
\]
located at \(r\approx1.320136713377\), with \(F(r)\approx3.820396841389\).

## Assumptions and scope
Area is two-dimensional Euclidean Hausdorff measure within each affine plane. The cylinders are infinite in their axial directions but their intersection is compact. Normal coordinates may be rescaled by any common nonzero factor. All trigonometric inverse functions take their principal real values. Statements about the *minimum* concern central planes; arbitrary supporting affine planes can have zero section area. The radius factor \(R^2\) follows by homothety, so the proof sets \(R=1\).

## Proof
**1. Chord integration.** At height \(z\in[-1,1]\), the body is the square \(|x|,|y|\le w(z)=\sqrt{1-z^2}\). By reflection and coordinate interchange assume \(a\ge b\ge0\), \(c\ge0\), and write the section-plane equation \(ax+by+cz=0\). For \(a>b>0,c>0\), the length of the line segment cut from this square at height \(z\), measured in the horizontal plane, is
\[
L(z)=\sqrt{a^2+b^2}\begin{cases}
2w(z)/a,&|cz|\le(a-b)w(z),\\
((a+b)w(z)-|cz|)/(ab),&(a-b)w(z)<|cz|\le(a+b)w(z),\\
0,&|cz|>(a+b)w(z).
\end{cases}
\]
The first regime meets two opposite sides of the square; the second meets adjacent sides. In the section plane, a change of height \(dz\) contributes area \(\rho\,L(z)\,dz/\sqrt{a^2+b^2}\). Put \(z_\pm=(a\pm b)/\sqrt{c^2+(a\pm b)^2}\) and \(I(s)=\int_0^s\sqrt{1-z^2}\,dz=(s\sqrt{1-s^2}+\arcsin s)/2\). Symmetry gives
\[
A_1(n)=2\rho\left[\frac2a I(z_-)+\frac1{ab}\left((a+b)(I(z_+)-I(z_-))-\frac c2(z_+^2-z_-^2)\right)\right].
\]
The noninverse-trigonometric terms cancel upon substituting \(z_\pm\). Since \(\arcsin(t/\sqrt{t^2+c^2})=\arctan(t/c)\) for \(t\ge0,c>0\), the displayed boxed formula follows. Taking limits yields all stated boundary formulas, including the horizontal square section of area \(4\). Continuity also follows from the continuous radial function of a compact convex body with the origin in its interior.

**2. Strict balancing.** For fixed \(c>0\) define \(g(X)=\sqrt X\arctan(\sqrt X/c)\), continuously at \(X=0\). Set \(X=(a+b)^2\), \(Y=(a-b)^2\). The formula becomes \(A_1(n)=4\rho\,[g(X)-g(Y)]/(X-Y)\), interpreted by continuity when \(X=Y\). The exact identity
\[
\frac{g(X)-g(Y)}{X-Y}=\int_0^1\frac{c^3\,dt}{(c^2+t^2X)(c^2+t^2Y)}
\]
follows from \(g(X)=\int_0^1 cX/(c^2+t^2X)\,dt\). For fixed \(a^2+b^2\), the sum \(X+Y=2(a^2+b^2)\) is fixed, while \(XY=(a^2-b^2)^2\) strictly decreases on balancing toward \(a=b\). The denominator in the integral equals \(c^4+c^2t^2(X+Y)+t^4XY\), so the integrand, and therefore the area, strictly increases. When \(c=0\), the boundary profile \(\pi\rho/a\) gives the same strict conclusion directly.

**3. Upper bound and exact maximizing directions.** By Step 2, for each fixed horizontal norm and vertical component the largest section has \(a=b>0\). Write \(r=c/a\). Direct substitution gives \(F(r)\) above. Its derivative has the sign of
\[
T(r)=r(r^2+4)\arctan(2/r)-2(r^2+2)=\int_0^2\frac{r^2(2-t^2)-2t^2}{r^2+t^2}\,dt.
\]
Indeed \(F'(r)=2T(r)/(\sqrt{r^2+2}(r^2+4))\). Differentiating the integrand with respect to \(r^2\) yields \(t^2(4-t^2)/(r^2+t^2)^2>0\) for \(0<t<2\). Hence \(T\) is strictly increasing, with limits \(-4\) at zero and \(4/3\) at infinity. It has exactly one positive zero, at which \(F\) has its unique strict interior minimum. The endpoint limits are \(\pi\sqrt2\) and \(4\); because \(\pi\sqrt2>4\), the unique global maximum of the meridian is at \(r=0\). The purely vertical normal has area \(4\), so it cannot maximize. Equality in balancing and in the meridional maximum forces \(a=b>0,c=0\), exactly the two asserted undirected diagonal normal directions.

**4. Lower bound and its equality cases.** Every point in the Euclidean unit ball satisfies both cylinder inequalities, so every central section contains its unit disk and has area at least \(\pi\). If the section plane is neither \(x=0\) nor \(y=0\), it contains a unit direction \(v\) with \(v_xv_y\ne0\). Along that direction the radial function of the bicylinder equals \(1/\sqrt{\max(v_x^2,v_y^2)+v_z^2}>1\). By continuity this strict radial excess holds on a nonempty open arc; thus the section area strictly exceeds \(\pi\). The two coordinate sections are unit disks, proving both equality cases. Continuity of the area on the connected sphere of normal directions gives the entire interval.

**5. Affine planes.** The Brunn concavity theorem for parallel sections of a convex body, together with central symmetry, shows that no affine section exceeds the central parallel section. Equality in the universal upper bound therefore requires the diagonal normal directions from Step 3. In orthonormal coordinates \(p=(x+y)/\sqrt2\), \(q=(x-y)/\sqrt2\), \(z\), the body satisfies \((|p|+|q|)^2/2+z^2\le1\). At the shifted diagonal plane \(p=t\), with \(0<|t|<\sqrt2\), the allowed width in \(q\) is \(2(\sqrt{2(1-z^2)}-|t|)\) for \(|z|\le\sqrt{1-t^2/2}\), and zero otherwise. This is pointwise strictly smaller than its central counterpart on a set of positive height measure. Thus every noncentral parallel section has strictly smaller area. The other diagonal family follows by symmetry; supporting planes and disjoint planes plainly cannot attain the maximum.

## Verification
The accompanying `check_sections.py` tests the inverse-tangent formula against two independent representations: (i) direct polar integration of the radial function in the section plane, and (ii) numerical integration of the horizontal-square chord lengths. It covers 159 nonzero normals, including symmetry axes, diagonal normals and pseudorandom directions. It also verifies the exact algebraic secant-kernel identity symbolically, tests directional balancing along seven meridians, and checks the scalar critical-point equation by an independent integral representation. The analytic proof above, not finite numerical tests, establishes the universal quantifiers and strict inequalities.

## Relationship to prior work
The bicylinder is classical, with horizontal square slices and its volume and surface area widely known. Weisstein's *Steinmetz Solid* and Ngô Quốc Anh's dated exposition supply the geometry and volume calculations, not the all-direction central-area profile. Moore's 1974 paper and Angell–Moore's 1987 paper concern symmetric intersections of cylinders; their full texts were not available for a conclusive content comparison, so priority relative to those works remains provisional. The accessible 2019 paper by Zhang, Chu and Li, *Application and Implementation of Steinmetz Solid*, presents an axis-aligned slicing/animation procedure and total surface area, not the stated all-normal inverse-tangent formula or its extrema. Aschmoneit and Cockx (2025) vary intersection depth and calculate three-dimensional volume and boundary surface area, different invariants from the planar-section area considered here. This theorem supplies an explicit sharp all-orientation classification, rather than a claim about novelty of any one axial section.

## Limitations
The radius-equal and orthogonal-axis assumptions are essential to the stated closed formula and maximizing directions. No unequal-radius or nonorthogonal-cylinder analogue, general affine area profile, or uniqueness claim for differently shaped sections is proved. Historical priority is not certified because older symmetric-intersection papers could not be inspected in full. The verification is self-review; independent audit and external mathematical validation have not been performed.

## References
1. E. W. Weisstein, *Steinmetz Solid*, MathWorld, https://mathworld.wolfram.com/SteinmetzSolid.html .
2. Ngô Quốc Anh, *Steinmetz Solid*, 19 January 2008, https://anhngq.wordpress.com/2008/01/19/steinmetz-solid/ .
3. Moreton Moore, *Symmetrical intersections of right circular cylinders*, The Mathematical Gazette **58** (1974), 181–185, https://doi.org/10.2307/3615957 .
4. I. O. Angell and M. Moore, *Symmetrical intersections of cylinders*, Acta Crystallographica A **43** (1987), 244–250, https://doi.org/10.1107/S0108767387099501 .
5. L. Zhang, J. Chu and N. Li, *Application and Implementation of Steinmetz Solid*, Journal of Physics: Conference Series **1345** (2019), 042093, https://doi.org/10.1088/1742-6596/1345/4/042093 .
6. F. J. Aschmoneit and B. Cockx, *Volume and Surface Area of two Orthogonal, Partially Intersecting Cylinders: A Generalization of the Steinmetz Solid*, arXiv:2512.22555v1 (2025), https://arxiv.org/html/2512.22555v1 .
