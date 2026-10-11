# Rigorous unique optimum for O'Hara's trapezoid cone
## Finding
Let
\[
\Omega
=
\{(\xi,\eta)\in\mathbb R^2:
0\le\xi\le2,\ |\eta|\le1+\xi/2\}.
\]
For \(h>0\) and an apex
\[
p=(x,y,h),
\]
let \(C_p\) be the convex hull of \(\Omega\times\{0\}\) and \(p\). Define
\[
F(p)
=
\frac{\operatorname{Area}(\partial C_p)^3}
{\operatorname{Vol}(C_p)^2}.
\tag{1}
\]

Then \(F\) has a unique global minimizer. It lies on the symmetry plane
\[
y=0.
\]
Writing it as
\[
p_*=(x_*,0,h_*),
\]
the pair \((x_*,h_*)\) is the unique solution in
\[
\mathbb R\times(0,\infty)
\]
of
\[
\frac{x}{s_1}
+
\frac{2(x-2)}{s_2}
+
\frac{x+2}{s_3}
=0,
\tag{2}
\]
\[
3h^2
\left(
\frac1{s_1}
+\frac2{s_2}
+\frac5{s_3}
\right)
-
2A(x,h)
=0,
\tag{3}
\]
where
\[
s_1=\sqrt{h^2+x^2},
\qquad
s_2=\sqrt{h^2+(2-x)^2},
\qquad
s_3=\sqrt{5h^2+(x+2)^2},
\tag{4}
\]
and
\[
A(x,h)=6+s_1+2s_2+s_3.
\tag{5}
\]

Numerically,
\[
x_*
=
0.90405068601394225129\ldots,
\]
\[
h_*
=
3.25028883901033616134\ldots,
\tag{6}
\]
and
\[
F(p_*)
=
329.6143694038955\ldots.
\tag{7}
\]

Thus the numerical optimum reported for this canonical trapezoid example is a genuine unique global optimum, not merely a local or sampled minimum.

## Assumptions and scope
The base is the trapezoid with vertices
\[
(0,-1),\quad
(0,1),\quad
(2,2),\quad
(2,-2).
\]
Its Euclidean area is
\[
6.
\]
The apex height satisfies
\[
h>0.
\]

The surface area in (1) is the complete boundary area: the base plus the four triangular lateral faces. The volume is the ordinary Euclidean volume.

The statement concerns exactly this trapezoid, which is the explicit nontriangular example used in the motivating source. No assertion is made here about a general polygonal base.

The characterization (2)--(3) is exact but implicit. No claim is made that \(x_*\) or \(h_*\) has a closed expression by radicals.

## Proof
The volume is independent of the horizontal apex coordinates:
\[
\operatorname{Vol}(C_p)
=
\frac{6h}{3}
=
2h.
\tag{8}
\]

For a base edge of length \(\ell\), if the horizontal projection \((x,y)\) is at Euclidean distance \(d\) from the supporting line of the edge, then the corresponding lateral triangular face has area
\[
\frac{\ell}{2}\sqrt{h^2+d^2}.
\tag{9}
\]
Applying (9) to the four edges gives
\[
\begin{aligned}
A(x,y,h)
={}&6
+\sqrt{h^2+x^2}
+2\sqrt{h^2+(2-x)^2}\\
&+\frac12
\sqrt{5h^2+(x+2-2y)^2}\\
&+\frac12
\sqrt{5h^2+(x+2+2y)^2}.
\end{aligned}
\tag{10}
\]

For fixed \(x,h\), the last two terms in (10) form an even strictly convex function of \(y\). Hence
\[
A(x,y,h)\ge A(x,0,h),
\]
with equality only at
\[
y=0.
\tag{11}
\]
Because the volume in (8) does not depend on \(x\) or \(y\), every global minimizer of (1) must satisfy (11).

On the symmetry plane, (10) becomes exactly (5). Thus
\[
F(x,0,h)
=
\frac{A(x,h)^3}{4h^2}.
\tag{12}
\]
Since the cube is increasing, minimizing (12) is equivalent to minimizing
\[
\Phi(x,h)
=
\frac{A(x,h)}{h^{2/3}}
\qquad
(x\in\mathbb R,\ h>0).
\tag{13}
\]

The function \(\Phi\) is coercive. Indeed,
\[
\Phi(x,h)\to\infty
\]
if \(h\to0^+\), if \(h\to\infty\), or if \(|x|\to\infty\). Hence it attains a global minimum.

We now prove uniqueness. For any \(c>0\), put
\[
G_c(x,h)
=
A(x,h)-c h^{2/3}.
\tag{14}
\]
Each radical in (5) is the Euclidean norm of an affine function of \((x,h)\), so \(A\) is convex. Also,
\[
-c h^{2/3}
\]
is strictly convex as a function of \(h>0\).

Suppose two distinct points had the same minimal value
\[
\Phi=c.
\]
If their heights differ, strict convexity of the second term in (14), together with convexity of \(A\), gives
\[
G_c<0
\]
at every nontrivial point of the segment joining them, contradicting minimality of \(c\).

If the two points have the same height but different \(x\)-coordinates, then for fixed \(h>0\) each term
\[
\sqrt{h^2+(x-a)^2}
\]
is strictly convex in \(x\), and so is
\[
\sqrt{5h^2+(x+2)^2}.
\]
Thus again the midpoint has
\[
G_c<0,
\]
a contradiction. Therefore the global minimizer of \(\Phi\), hence of \(F\), is unique.

There is also a useful global characterization of critical points. Let \((x,h)\) be stationary for \(\Phi\) and put
\[
c=\Phi(x,h).
\]
Differentiating (13) shows
\[
A_x(x,h)=0,
\qquad
3hA_h(x,h)=2A(x,h).
\tag{15}
\]
At the same point,
\[
G_c(x,h)=0
\]
and
\[
\nabla G_c(x,h)=0.
\tag{16}
\]
Since \(G_c\) is convex, (16) implies
\[
G_c(\widetilde x,\widetilde h)\ge0
\]
for every \(\widetilde h>0\). Equivalently,
\[
\Phi(\widetilde x,\widetilde h)\ge c.
\]
Thus every stationary point of \(\Phi\) is automatically a global minimizer. Since the global minimizer is unique and exists, \(\Phi\) has exactly one stationary point.

Finally, differentiating (5) gives
\[
A_x
=
\frac{x}{s_1}
+
\frac{2(x-2)}{s_2}
+
\frac{x+2}{s_3},
\]
and
\[
A_h
=
h
\left(
\frac1{s_1}
+\frac2{s_2}
+\frac5{s_3}
\right).
\]
Therefore (15) is precisely the system (2)--(3). Its unique solution is the global optimum.

## Verification
The supplied `verify.py` reconstructs (2)--(5) from the surface-area formula and solves the unique stationary system at high precision. It obtains
\[
x_*
=
0.90405068601394225129\ldots,
\qquad
h_*
=
3.25028883901033616134\ldots.
\]

As an independent regression against the motivating source, the checker minimizes the surface area at the four fixed heights
\[
h=1,2,3,4
\]
and obtains the horizontal coordinates
\[
0.91690678\ldots,\quad
0.90792913\ldots,\quad
0.90452827\ldots,\quad
0.90306106\ldots,
\]
matching the reported values \(0.9169,0.9079,0.9045,0.9031\).

The numerical solve is not used to prove existence, globality, or uniqueness. Those facts follow from coercivity, symmetry, convexity, and the argument (14)--(16). Computation is used only to evaluate the uniquely characterized optimizer numerically.

## Relationship to prior work
The motivating paper defines cone isoperimetric centers and proves that, for a triangular base, the incenter is optimal for every prescribed height and the globally optimal cone has an explicit height.

The same paper then emphasizes that this behavior does not extend unchanged to general convex planar bases and singles out the trapezoid used here. For this trapezoid it reports only numerical experiments: fixed-height center coordinates near
\[
0.9169,\ 0.9079,\ 0.9045,\ 0.9031
\]
for heights \(1,2,3,4\), and a numerically observed global minimum near
\[
h=3.250,
\qquad
x=0.90405.
\]
No proof of global uniqueness or exact stationary characterization is supplied there.

The present result turns that numerical example into a theorem. It gives the complete surface-area formula, proves that symmetry is forced, proves existence and uniqueness globally rather than on a sampled parameter window, and characterizes the optimum as the unique solution of the explicit radical system (2)--(3).

Searches under the terms “cone isoperimetric center,” “isoperimetrically optimal cone,” the distinctive trapezoid, and the numerical fingerprints \(0.90405\) and \(3.250\) did not locate a later published theorem that supplies this global uniqueness statement.

## Limitations
Only the canonical trapezoid from the motivating paper is treated. The proof does not classify cone isoperimetric centers for all trapezoids or all convex polygons.

The exact answer is an implicit two-equation characterization, not a radical closed form.

The short convexity argument may have appeared in unindexed notes or informal discussion of the example; this remains the principal historical originality risk.

The result concerns optimization of the surface-area-to-volume ratio of a cone with fixed planar base. It is distinct from the classical isoperimetric problem for sets contained inside an already fixed cone.

## References
1. J. O'Hara, *The incenter of a triangle as a cone isoperimetric center*, arXiv:1012.5918v1, 29 December 2010.
2. J. O'Hara, *Isoperimetric characterization of the incenter of a triangle*, *Elemente der Mathematik* 68 (2013), 77--85. DOI: 10.4171/EM/223.
