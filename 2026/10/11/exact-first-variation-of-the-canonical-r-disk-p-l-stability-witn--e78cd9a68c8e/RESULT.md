# Exact first variation of the canonical \(r\)-disk Pál stability witness
## Finding
For \(r\ge w>0\), let \(T_{w,r}\subset\mathbb R^2\) be the regular \(r\)-disk triangle of minimal width \(w\). Consider the canonical deformation from the sharpness argument for the ball-convex Pál stability theorem: one vertex is continued along an adjacent boundary circle of radius \(r\) by chord distance \(x>0\), while the other two vertices are fixed. Write the resulting \(r\)-disk triangle as \(T_x\).

Set
\[
s=\frac12\left(\sqrt{4r^2-(r-w)^2}-\sqrt3\,(r-w)\right),\qquad
u=\frac{s}{2r},\qquad c=\sqrt{1-u^2}.
\]
Then \(0<u\le 1/2\). For sufficiently small \(x>0\), put
\[
z=\frac{x}{2r},\qquad d=\sqrt{1-z^2},
\]
and define
\[
a(x)=sd+cx,
\]
\[
b(x)^2=s^2+x^2+sx\left((c-\sqrt3u)d-(u+\sqrt3c)z\right),
\]
\[
D(x)=\frac{sx}{4}\left((\sqrt3c-u)d-(\sqrt3u+c)z\right).
\]
For \(0\le t\le 2r\), let
\[
J_r(t)=r^2\arcsin\!\left(\frac{t}{2r}\right)-\frac{t}{4}\sqrt{4r^2-t^2}
\]
be the area of the minor circular segment of radius \(r\) and chord length \(t\). Then the deformation has the exact area-deficit formula
\[
\operatorname{area}(T_x)-\operatorname{area}(T_{w,r})
=D(x)+J_r(a(x))+J_r(b(x))-2J_r(s).
\]
In particular,
\[
\operatorname{area}(T_x)-\operatorname{area}(T_{w,r})=L(r,w)x+O(x^2),
\]
where
\[
L(r,w)=\frac r2\left(2u^2+\frac{\sqrt3u(1-2u^2)}{c}\right)
=\frac{s}{2c}\sin\!\left(2\arcsin u+\frac{\pi}{3}\right)>0.
\]
The same family has \(\operatorname{diam}T_x=a(x)\), hence
\[
\operatorname{diam}T_x-\operatorname{diam}T_{w,r}=cx+O(x^2).
\]
Therefore every constant \(C\) valid in a local Hausdorff stability estimate
\[
\inf_{\phi}d_H(K,\phi T_{w,r})\le C\left(\operatorname{area}(K)-\operatorname{area}(T_{w,r})\right)
\]
for all sufficiently close \(r\)-ball convex bodies \(K\) of minimal width \(w\) must satisfy
\[
C\ge C_{\mathrm{can}}(r,w):=\frac{c}{2L(r,w)}
=\frac{c^2}{s\sin(2\arcsin u+\pi/3)}.
\]
At the Reuleaux endpoint \(r=w\), this gives \(C_{\mathrm{can}}=\sqrt3/(2w)\); in the classical Pál limit \(r\to\infty\) with \(w\) fixed, it tends to \(1/w\).

## Assumptions and scope
The ambient plane is Euclidean. The parameters satisfy \(r\ge w>0\). The deformation is exactly the one used in Section 5 of arXiv:2606.02882v1: if the original vertices are \(v_1,v_2,v_3\), then \(v_3\) lies on the shorter radius-\(r\) arc from \(v_2\) to the new vertex \(v(x)\), and \(|v_3-v(x)|=x\). For sufficiently small \(x>0\), the source proves that \(T_x\) still has minimal width \(w\) and observes that its diameter is \(|v_2-v(x)|\).

The claim is path-wise. It gives the exact area law and first-order efficiency of this canonical sharpness family, and therefore an explicit necessary lower bound for any local Hausdorff stability constant. It does not identify the globally best finite-\(r\) stability constant.

## Proof
Place the unperturbed vertices at
\[
v_2=(-s/2,0),\qquad v_3=(s/2,0),\qquad v_1=(0,\sqrt3s/2).
\]
The center of the radius-\(r\) circle carrying the side from \(v_2\) to \(v_3\) is \(O=(0,rc)\). Its lower arc midpoint is \((0,r(c-1))\), so the height that realizes the minimal width is
\[
w=\frac{\sqrt3s}{2}+r(1-c)=r(1+\sqrt3u-c).
\]
Solving this relation with \(c^2+u^2=1\) and \(0<u\le1/2\) yields
\[
s=\frac12\left(\sqrt{4r^2-(r-w)^2}-\sqrt3(r-w)\right).
\]

Let the central angular increment from \(v_3\) to \(v(x)\) be \(\beta\). Since \(|v_3-v(x)|=x\), one has \(\sin(\beta/2)=z\), so \(\cos(\beta/2)=d\). Rotating the radius vector \(v_3-O\) through \(\beta\) gives the exact displacement
\[
v(x)-v_3=x(cd-uz,\,ud+cz).
\]
Direct distance calculations now give the two changed chord lengths
\[
|v_2-v(x)|=a(x)=sd+cx
\]
and
\[
|v_1-v(x)|^2=b(x)^2=s^2+x^2+sx\left((c-\sqrt3u)d-(u+\sqrt3c)z\right).
\]
The signed determinant of the new vertex triangle gives its Euclidean area increment
\[
D(x)=\frac{sx}{4}\left((\sqrt3c-u)d-(\sqrt3u+c)z\right).
\]

For a sufficiently small deformation all three boundary arcs remain minor arcs. The area of an \(r\)-disk triangle is the area of its Euclidean vertex triangle plus the three minor circular-segment areas. One chord remains \(s\); the other two become \(a(x)\) and \(b(x)\). Since the minor segment with chord \(t\) has area
\[
J_r(t)=r^2\arcsin\!\left(\frac{t}{2r}\right)-\frac{t}{4}\sqrt{4r^2-t^2},
\]
the displayed exact deficit formula follows immediately.

Differentiate at \(x=0\). The elementary formulas give
\[
a'(0)=c,\qquad b'(0)=\frac{c-\sqrt3u}{2},\qquad D'(0)=\frac{s}{4}(\sqrt3c-u),
\]
and
\[
J_r'(s)=\frac{s^2}{2\sqrt{4r^2-s^2}}=\frac{ru^2}{c}.
\]
Therefore
\[
L(r,w)=D'(0)+J_r'(s)\bigl(a'(0)+b'(0)\bigr)
=\frac r2\left(2u^2+\frac{\sqrt3u(1-2u^2)}{c}\right).
\]
If \(\alpha=\arcsin u\), then \(0<\alpha\le\pi/6\), and the same expression is
\[
L(r,w)=\frac{s}{2c}\sin\!\left(2\alpha+\frac\pi3\right)>0.
\]
This proves the first-order expansion.

The source's canonical-family geometry gives \(\operatorname{diam}T_x=a(x)\). For any compact sets \(A,B\),
\[
|\operatorname{diam}A-\operatorname{diam}B|\le2d_H(A,B).
\]
Since isometries preserve diameter,
\[
\inf_\phi d_H(T_x,\phi T_{w,r})\ge\frac{a(x)-s}{2}=\frac c2x+O(x^2).
\]
Dividing by the area deficit and letting \(x\downarrow0\) proves \(C\ge c/(2L)\). Substituting \(u=1/2\), \(c=\sqrt3/2\), and \(s=w\) gives the endpoint \(\sqrt3/(2w)\). From the width relation, as \(r\to\infty\) with \(w\) fixed one has \(u\sim w/(\sqrt3r)\), \(c\to1\), and \(s\to2w/\sqrt3\), yielding the limit \(1/w\).

## Verification
The proof is analytic and does not rely on finite sampling. The included `verify.py` uses only the Python standard library to check the coordinate identities numerically at several admissible parameter pairs, compare the exact deficit quotient with \(L(r,w)\), verify the equivalent trigonometric expression for \(L(r,w)\), and check the two endpoint limits. Its successful output is `VERIFY_OK`.

The finite checks are consistency tests only. The universal quantifiers, the exact segment decomposition, positivity of \(L(r,w)\), and the stability-constant implication are established by the formulas above.

## Relationship to prior work
Fodor and Sagmeister, arXiv:2606.02882v1, introduce exactly this one-vertex \(r\)-disk-triangle deformation to prove that their linear Hausdorff stability order is optimal. Their Section 5 proves only the existence of a constant \(c_5>0\) with area deficit less than \(c_5x\), using an upper bound by a radius-\(r\) sector and a circular-segment difference. The paper records first-order upper expansions for those bounding terms, but it does not give the exact area-deficit formula above, the exact derivative \(L(r,w)\), or the resulting explicit finite-\(r\) canonical lower bound on a Hausdorff stability constant.

Fodor, Robock, and Sagmeister, arXiv:2602.19300, establish the underlying \(r\)-ball-convex isominwidth theorem and the geometry of \(T_{w,r}\), including the width-realizing height; they do not analyze this stability deformation. Lucardesi and Zucco, arXiv:2405.18294 and Journal of Geometric Analysis 35 (2025), treat the ordinary convex Pál problem, corresponding to the limiting regime \(r\to\infty\), not finite \(r\)-disk triangles.

Targeted searches for exact finite-\(r\) canonical area laws, first variations, and explicit lower bounds for the ball-convex Pál Hausdorff constant found no statement implying the formula or coefficient here. The closest indexed results concern other width-stability problems and do not specialize to this deformation.

## Limitations
The bound \(C_{\mathrm{can}}(r,w)\) is a necessary lower bound generated by one canonical path. No claim is made that it is the optimal global Hausdorff stability constant for finite \(r\). The exact formula is Euclidean; hyperbolic and spherical analogues are not derived here. The originality search cannot exclude an unindexed calculation of the same elementary first variation.

## References
1. F. Fodor and Á. Sagmeister, *Optimal stability of Pál's isominwidth inequality for ball convex bodies in planes of constant curvature*, arXiv:2606.02882v1, first public 1 June 2026.
2. F. Fodor, N. Robock, and Á. Sagmeister, *Pál's isominwidth inequality for ball convex bodies in planes of constant curvature*, arXiv:2602.19300.
3. I. Lucardesi and D. Zucco, *Three quantitative versions of the Pál inequality*, arXiv:2405.18294; Journal of Geometric Analysis 35 (2025).
