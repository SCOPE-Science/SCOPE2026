# Sharp regular-pentagon capacity of ellipses and a contact-phase transition

## Finding
Let \(E_{a,b}=\{(X,Y):X^2/a^2+Y^2/b^2\le1\}\), with \(a\ge b>0\), and let \(\rho_5(E_{a,b})\) be the maximum circumradius among **Euclidean regular pentagons** contained in the ellipse, allowing arbitrary rotations and translations. Write \(x=(b/a)^2\), \(h=\cos(\pi/5)=(1+\sqrt5)/4\), and
\[
U(x)=\tfrac14\sqrt{10+5x+x^{-1}},\qquad V(x)=\tfrac12\bigl(1+h+(1-h)x\bigr).
\]
Then the exact, globally sharp capacity is
\[
\boxed{\rho_5(E_{a,b})=\frac{b}{\min\{U(x),V(x)\}}},\qquad
\boxed{A_{5,\max}(E_{a,b})=\frac52\sin(2\pi/5)\,\rho_5(E_{a,b})^2}.
\]
There is one noncircular orientation transition, at
\[
\boxed{x_*=\frac{13+7\sqrt5-\sqrt{358+158\sqrt5}}4=0.4955728394635\ldots}.
\]
For \(x_*<x<1\), the only optimal orientations, modulo the dihedral symmetries of a regular pentagon and the reflections of the ellipse, place a vertex along the major axis; their minimal enclosing circles in affine unit-disk coordinates have four active vertices. For \(0<x<x_*\), the unique optimal orientation class places a vertex along the minor axis, with three active vertices. At \(x=x_*\), both classes are optimal, and at \(x=1\), every orientation is optimal. Every optimum is attained and its translation is uniquely fixed by the enclosing circle of the transformed vertices. The normalized area fraction \(A_{5,\max}(E_{a,b})/(\pi ab)\) is strictly increasing as \(b/a\) increases and therefore determines the aspect ratio uniquely.

## Assumptions and scope
“Regular” means Euclidean regular, not an affine image of a regular pentagon. The five vertices may have an arbitrary common translation, and containment of all vertices is equivalent to containment of the whole pentagon because the ellipse is convex. All axes are positive; \(a=b\) is treated separately as the circle endpoint. All statements concern exact Euclidean lengths and areas. The active-contact counts refer to the unique smallest enclosing Euclidean circle of the five vertices after the affine normalization \((X,Y)\mapsto(X/a,Y/b)\); they equivalently count boundary contacts in the original ellipse.

## Proof
**1. Reduction to a rotating five-point minimum-enclosing-circle problem.** Put \(t=b/a=\sqrt x\), and let \(q_j=(\cos(\phi+2\pi j/5),\sin(\phi+2\pi j/5))\), \(j=0,\ldots,4\). A regular pentagon of Euclidean circumradius \(\rho\) has vertices \(z+\rho q_j\). Under \((X,Y)\mapsto(X/a,Y/b)\), its vertices become a common translated copy of \((\rho/b)p_j\), where \(p_j=(t\cos(\phi+2\pi j/5),\sin(\phi+2\pi j/5))\). Thus such a pentagon fits inside the ellipse if and only if \((\rho/b)r_x(\phi)\le1\), where \(r_x(\phi)\) is the radius of the smallest disk covering all five \(p_j\). The optimization is exactly \(\rho_5/b=1/\min_\phi r_x(\phi)\). The rotation symmetry, antipodal symmetry of the ellipse, and reflection reduce \(\phi\) to \([0,\pi/10]\).

**2. A three-point certificate for every orientation.** Set \(\delta=\phi-\pi/10\in[-\pi/10,0]\), \(y=\cos(2\delta)\in[h,1]\), \(m=(1+x)/2\), and \(d=(1-x)/2\). Consider three transformed vertices \(p_1,p_3,p_4\). Let \(L^2=4\sin^2(2\pi/5)\), \(\ell^2=4\sin^2(\pi/5)\). Their three squared side lengths (with the two longer sides listed first) are
\[
L^2\{m+d\cos(2\delta+\pi/5)\},\quad
L^2\{m+d\cos(2\delta-\pi/5)\},\quad
\ell^2(m-dy).
\]
Their area is \(t\) times the fixed area of the corresponding untransformed triangle, hence independent of \(\delta\). By the standard circumradius formula (product of three side lengths divided by four times the area), the **squared circumradius** is a positive constant independent of \(\delta\) times
\[
P(y)=\bigl(m^2+2mdhy+d^2[y^2-(1-h^2)]\bigr)(m-dy).
\]
For \(0<x<1\) the second derivative satisfies
\[
P''(y)=2md^2(1-2h)-6d^3y<0\quad(h\le y\le1),
\]
since \(h>1/2\). Strict concavity therefore places the minimum circumradius of these triangles at an orientation endpoint. Direct substitution in the circumradius formula gives their endpoint circumradii as \(U(x)\) for \(\delta=-\pi/10\) and \(V(x)\) for \(\delta=0\).

There is a necessary distinction between a circumcircle and a *minimum enclosing circle*: a triangle with an obtuse angle has a minimum enclosing circle supported by its longest side. On our interval the longest side is the one with factor \(\cos(2\delta+\pi/5)\); its length strictly decreases as \(\delta\) increases. The triangle at \(\delta=0\) is acute and isosceles. Hence, if the triangle at a particular \(\delta\) is obtuse, moving right to its first right-angle orientation weakly decreases its minimum-enclosing-circle radius, at which orientation that radius equals the circumradius. The latter is at least \(\min\{U,V\}\) by strict concavity. For acute triangles the same bound holds directly by their circumcircles. Consequently, at **every** orientation, the smallest enclosing circle of these three vertices, and therefore that of all five, has radius at least \(\min\{U(x),V(x)\}\). At \(x=1\), all five vertices lie on the unit circle and the claimed radius is immediate.

**3. Endpoint realization and boundary contacts.** At \(\phi=0\), four of the five transformed vertices lie on the circle with center \((c_0,0)\), \(c_0=(1-x)/(4\sqrt x)\), and radius \(U(x)\). The fifth has squared inward slack \(5(1-x)/4\). When \(x\ge1/\sqrt5\), the center belongs to the convex hull of the four contacts, so the disk is the unique minimum enclosing circle. (For instance, its horizontal coordinate lies between the two horizontal contact coordinates, and vertical reflection gives convex containment.) Thus \(r_x(0)=U(x)\) throughout this range.

At \(\phi=\pi/10\), three vertices lie on the circle with center \((0,c_1)\), where \(c_1=(1-x)(1-h)/2\), and radius \(1-c_1=V(x)\). The other two vertices have positive squared inward slack \((1-x)5(\sqrt5-1)/8\) for \(x<1\). The circle center is within the convex hull of the three contact vertices (two lower symmetric contacts and one upper contact), so \(r_x(\pi/10)=V(x)\) for every \(0<x\le1\). Thus the preceding lower bound is attained at one of these orientations whenever the corresponding endpoint is smaller.

**4. Phase threshold and uniqueness.** Exact algebra factors the difference as
\[
16x\bigl(U(x)^2-V(x)^2\bigr)=\frac{3\sqrt5-7}{2}(x-1)
\left(x^2-\frac{13+7\sqrt5}{2}x+\frac{7+3\sqrt5}{2}\right).
\]
The quadratic has exactly one root in \((0,1)\), namely \(x_*\), with \(x_*>1/\sqrt5\); its other root exceeds one. Accordingly \(V(x)<U(x)\) for \(0<x<x_*\), and \(U(x)<V(x)\) for \(x_*<x<1\). Both lower-bound witnesses are therefore feasible in their stated regimes. Strict concavity in step 2, together with strict decrease of the longest-side half-length in the obtuse regime, excludes any other optimal orientation between endpoints. Uniqueness of the Euclidean smallest enclosing circle gives uniqueness of the translation for each chosen orientation. The contact descriptions and transition follow.

**5. Inverse shape statistic.** Put \(s=\sin(2\pi/5)\). The dimensionless optimal area fraction is
\[
Q(x)=\frac{5s}{2\pi}\frac{\sqrt x}{\min\{U(x),V(x)\}^2}.
\]
For \(0<x\le x_*\), the denominator is \(V(x)^2=(p+qx)^2\) with \(p=(1+h)/2\), \(q=(1-h)/2\). Its logarithmic derivative is positive because \(p>3qx\) for \(0<x\le1\). For \(x_*\le x\le1\), the variable factor is \(16x^{3/2}/(5x^2+10x+1)\), whose derivative has the sign of \(-5x^2+10x+3>0\) on \((0,1]\). The branches agree at the transition, proving strict increase and invertibility. The circle has the ordinary optimal disk-inscribed regular pentagon ratio \(Q(1)=5\sin(2\pi/5)/(2\pi)\); the thin-ellipse limit is zero.

## Verification
Run `python3 verify.py` in the same directory after installing `sympy` (see `requirements.txt`). The checker independently enumerates all pair- and triple-contact minimum enclosing circles for five transformed vertices, over 17 anisotropies and 181 orientations per anisotropy (3,077 cases), checking the predicted global lower bound and both endpoint formulas. It also symbolically tests the golden-ratio contact identities, the threshold factorization, strict-concavity derivative and contact slack identities. Its output terminates with `ALL_CHECKS_PASSED`. These finite numerical diagnostics do not substitute for the analytic minimization above.

## Relationship to prior work
Bogoşel [1] states that polygons of maximum area inside an ellipse, **without the Euclidean-regularity constraint**, are affine images of regular polygons inscribed in a disk. That affine-invariant maximum-area theorem does not imply the capacity of a **Euclidean** regular pentagon, because a general affine image of a regular pentagon is not Euclidean regular. A separately examined result [2] classifies ordinary Euclidean perimeters *within the family of maximum-area affine-regular inscribed polygons*. Its feasible set and objective differ from optimizing Euclidean-regular pentagon area over translations and rotations. No claim is made that these known results or elementary minimum-enclosing-circle facts are novel.

## Limitations
This is an exact theorem for planar ellipses and *regular pentagons* only; no assertion is made about other polygon orders, general convex hosts or noisy-measurement reconstruction. The normalized-area inverse assumes access to the exact optimal area, not an arbitrary inscribed area measurement. The search for historical priority did not establish that all earlier papers on regular-polygon fitting in ellipses have been examined; an earlier equivalent classification may exist. The discrete verification checks finite samples only and is not a proof of uniqueness for all orientations.

## References
1. B. Bogoşel, “Maximal perimeter polygons contained in disk/ellipse,” blog exposition dated 2023-09-22, https://mathproblems123.wordpress.com/2023/09/22/maximal-perimeter-polygons-contained-in-disk-ellipse/ (includes maximum-area inscribed polygon discussion).
2. “Exact perimeter selection among maximum-area polygons inscribed in ellipses,” research record, https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-exact-perimeter-selection-among-maximum-area-polygons-inscribed--9338777854e9/RESULT.md (full result examined and statements compared).
