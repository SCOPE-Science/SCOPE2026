# Exact all-level area and conic boundary of the Ulam floating body of a triangle

## Finding
Let \(T\subset\mathbb R^2\) be any nondegenerate triangle, \(A=|T|\), and let \(M_{qA}(T)\) be its **Ulam floating body** at cap-area fraction \(0<q<1\): for every outward unit normal \(u\), the exposed point with normal \(u\) is the centroid of the unique cap \(\{x\in T:\langle u,x\rangle\ge c_u\}\) having area \(qA\). Put \(F(q)=|M_{qA}(T)|/A\). For \(0<q\le\tfrac12\), let \(p=1-q\). Then
\[
\boxed{F(q)=\frac23\left[p+q\log q+\frac{p^2}{q^2}\bigl(q+p\log p\bigr)\right].}
\tag{1}
\]
For \(\tfrac12\le q<1\), the exact complement identity gives
\[
\boxed{F(q)=\left(\frac{1-q}{q}\right)^2F(1-q).}
\tag{2}
\]
Thus the area ratio depends only on the cap fraction, not the triangle's shape. In particular,
\[
F\!\left(\frac12\right)=\frac23(1-\log2),
\quad
1-F(q)=\frac23q\log\frac1q+\frac{11}{9}q-\frac16q^2+O(q^3)
\quad(q\downarrow0).
\tag{3}
\]
The entire boundary is explicitly described: for \(q\le\tfrac12\), each of six barycentric-order sectors consists of two conic arcs, one satisfying a product-of-barycentric-coordinates equation and the other a product-of-affine-linear-functions equation. Their six affine-permuted copies constitute the whole strictly convex boundary. For \(q>\tfrac12\), the boundary follows by reflection and scaling about the triangle centroid.

## Assumptions and scope
An Ulam floating body is **not** the classical convex floating body obtained by retaining all points of prescribed minimum halfspace depth. The latter has a different triangle area profile. The cap-centroid/support-point characterization follows from the general Ulam floating body theorem of Huang, Slomka and Werner. Existence, uniqueness, and strict boundary parametrization hold for positive-area caps of a triangle and \(0<q<1\).

The construction is affine equivariant: if \(L\) is an invertible affine map, \(M_{q|LT|}(LT)=L(M_{q|T|}(T))\). Both numerator and denominator areas transform by the same absolute determinant. Hence it suffices to take the reference triangle with vertices \(v_0=(0,0)\), \(v_1=(1,0)\), \(v_2=(0,1)\), area \(1/2\), and centroid \(g=(1/3,1/3)\).

## Proof
**1. One normal sector and the cap switch.** In the reference triangle take the outward normal proportional to \(u=(1,t)\), \(0\le t\le1\); the three vertex heights are \(1,t,0\). As the cap fraction \(q\) is fixed, the cap changes from a small triangle at \(v_1\) to the complement of a small triangle at \(v_0\) precisely when \(t=p=1-q\).

For \(0\le t\le p\) write \(r=\sqrt{q/(1-t)}\). The cap is the triangle cut from \(v_1\) with edge fractions \(r\) and \(q/r\). As \(t\) grows, \(r\) ranges monotonically from \(\sqrt q\) to \(1\); the cap centroid is
\[
C_1(r)=\left(1-\frac{r+q/r}{3},\frac r3\right),\qquad \sqrt q\le r\le1.
\tag{4}
\]
Its barycentric coordinates \((\lambda_0,\lambda_1,\lambda_2)=(1-x-y,x,y)\) satisfy \(\lambda_0\lambda_2=q/9\), an arc of a rectangular hyperbola in affine coordinates.

For \(p\le t\le1\), the excluded lower-area triangle has area fraction \(p\). Put \(r=\sqrt{p/t}\); it decreases monotonically from \(1\) to \(\sqrt p\). Its intercept fractions are \(p/r\) and \(r\), and its centroid is \((p/(3r),r/3)\). Conservation of the full triangle first moment yields the upper-cap centroid
\[
C_2(r)=\left(\frac{1-p^2/r}{3q},\frac{1-pr}{3q}\right),\qquad 1\ge r\ge\sqrt p.
\tag{5}
\]
This lies on the conic \((1-3qx)(1-3qy)=p^3\). Formulas (4) and (5) agree at \(r=1\), with shared junction \(((2-q)/3,1/3)\). The endpoints at equal vertex-height directions meet the adjacent sectors by continuity. Permuting the three vertices produces the complete six-sector boundary, without omissions because the normal circle decomposes into those six sectors.

**2. Exact area by Green's theorem.** For a continuous positively oriented boundary and reference point \(g\), Green's formula gives \(\frac12\oint\det(C-g,dC)\). The six normal sectors are related by vertex-permuting affine maps with absolute determinant \(1\). Orientation induced by increasing normal is preserved on the boundary in each sector; therefore the contribution of one sector is sixfold in signed area.

Along the first arc,
\[
\det(C_1(r)-g,C_1'(r))
=\frac19\left(1-\frac{2q}{r}+\frac q{r^2}\right).
\]
Its integral in the induced direction is
\[
J_1=\frac19\int_{\sqrt q}^{1}\left(1-\frac{2q}{r}+\frac q{r^2}\right)dr
=\frac19\bigl(p+q\log q\bigr).
\tag{6}
\]
Along the second arc,
\[
\det(C_2(r)-g,C_2'(r))
=-\frac{p^2}{9q^2}\left(1-\frac{2p}{r}+\frac p{r^2}\right).
\]
As \(r\) decreases from \(1\) to \(\sqrt p\), the positively oriented integral is
\[
J_2=\frac{p^2}{9q^2}\int_{\sqrt p}^{1}\left(1-\frac{2p}{r}+\frac p{r^2}\right)dr
=\frac{p^2}{9q^2}\bigl(q+p\log p\bigr).
\tag{7}
\]
The body's physical area is \(6(J_1+J_2)/2=3(J_1+J_2)\). Dividing by the reference triangle area \(1/2\) yields \(F(q)=6(J_1+J_2)\), exactly (1).

**3. Complement symmetry at every level.** For an arbitrary triangle of centroid \(G\), the top \(qA\)-cap of normal \(u\) and its complementary bottom \(pA\)-cap of normal \(-u\) partition \(T\). Calling their centroids \(C_q(u)\) and \(C_p(-u)\), the moment identity is
\[
q(C_q(u)-G)+p(C_p(-u)-G)=0.
\]
These are the unique exposed points of the respective Ulam bodies with the indicated normals. The equality of exposed-point maps in all directions yields
\[
M_{qA}(T)-G=-\frac pq\bigl(M_{pA}(T)-G\bigr).
\tag{8}
\]
The area scales by \((p/q)^2\), establishing (2) for \(q\ge1/2\). At \(q=p=1/2\), (8) shows that the body is centrally symmetric about \(G\).

**4. Endpoints.** At \(q=1/2\), substitution in (1) gives \(\frac23(1-\log2)\); expansion using \(\log(1-q)\) at zero gives (3). The area approaches \(1\) as \(q\downarrow0\) and \(0\) as \(q\uparrow1\), as required by cap-centroid geometry.

## Verification
`verify.py` is a standalone, standard-library-only numerical cross-check. It clips the reference triangle by arbitrary oriented halfplanes, obtains the target cap-area threshold by bisection, evaluates centroids using the polygon shoelace moment formula, and computes the area of the resulting ordered cap-centroid boundary. It compares those independently constructed areas against (1)–(2) for twelve cap parameters, including three parameters under an invertible affine change of triangle. It also checks 156 analytic conic-arc identities and 99 complement-law values. The tolerances are explicit in the code. These finite tests corroborate, rather than replace, the exact Green-integral proof above.

## Relationship to prior work
Huang, Slomka and Werner introduced the Ulam floating body and proved the cap-centroid support characterization and general regularity results; the new calculation specializes that construction to the triangle and integrates its boundary exactly. Huang and Slomka introduced the underlying metronoid formalism, but do not derive the triangle Ulam area profile. Molchanov and Turin treat Ulam bodies as average-quantile regions within a more general framework, without this all-level triangle computation.

A published exact area profile for the **classical convex floating body** of every triangle concerns halfspace-depth contours, not cap-centroid supports, and does not imply (1). A published exact Ulam area formula for the **square** concerns a non-affinely-equivalent body with parabolic and hyperbolic boundary pieces; it does not imply (1). Targeted searches using metronoid, zonoid trimming, uniform-simplex average-quantile regions, and Ulam triangle area terminology did not locate an implication-equivalent formula.

## Limitations
This is a planar-triangle result for uniform area measure and does not assert an analogue for arbitrary polygons or higher-dimensional simplices. The cap-centroid characterization is a prior theorem used as a premise; the exact conic decomposition and Green-integrated triangle area are the asserted contribution. Full scholarly priority remains uncertain, particularly under statistical zonoid-trimming or metronoid terminology. No independent mathematical audit has been performed.

## References
1. H. Huang, B. A. Slomka and E. M. Werner, *Ulam Floating Body*, arXiv:1803.08224, initially submitted 2018-03-22; *Journal of the London Mathematical Society* 100 (2019), 425–446.
2. H. Huang and B. A. Slomka, *Approximations of convex bodies by measure-generated sets*, arXiv:1706.07112, initially submitted 2017-06-21; *Geometriae Dedicata* 192 (2018), 173–196.
3. I. Molchanov and R. Turin, *Convex bodies generated by sublinear expectations of random vectors*, arXiv:2006.02186, initially submitted 2020-06-03; *Advances in Applied Mathematics* 131 (2021), 102251.
4. *Exact area profile of the convex floating body of every triangle*, publicly available result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-area-profile-of-the-convex-floating-body-of-every-triangle--34558385f85d .
5. *Exact Ulam floating body of the square*, publicly available result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-ulam-floating-body-of-the-square--acefdad229b3 .
