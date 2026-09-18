# Exact triangle formula for Pach--Tardos roundness and sharp fatness calibration

## Statement

Pach and Tardos (2026) introduced, for a compact plane convex set \(S\) and distinct
\(p,q\in S\), the quantity
\[
C(S,p,q)=\frac{|S\cap \ell_{p,q}|}{|p-q|},
\]
where \(\ell_{p,q}\) is the perpendicular bisector of \(pq\), and defined the
**roundness**
\[
C(S)=\inf_{p\ne q} C(S,p,q).
\]
They proved the general comparison
\[
0.28\,C(S)\le \frac{r(S)}{R(S)}\le 2C(S),
\]
where \(r(S)\) and \(R(S)\) are the inradius and the radius of a smallest
containing disk, respectively.

For triangles this new invariant has an exact classical interpretation.

**Theorem 1 (exact triangle roundness).** Let \(T\) be a nondegenerate Euclidean
triangle and let \(\alpha\in(0,\pi/3]\) be its smallest interior angle. Then
\[
\boxed{C(T)=\tan\frac{\alpha}{2}}.
\]
If \(A\) is a vertex of angle \(\alpha\) and \(D\) is where the internal angle
bisector from \(A\) meets the opposite side, then the pair \(p=A,q=D\) attains
the minimum.

Thus, on triangles, Pach--Tardos roundness is exactly a monotone transform of
the standard minimum-angle mesh-quality parameter.

There is also a sharp comparison with classical inradius/circumradius fatness.
Put
\[
t=C(T)=\tan(\alpha/2),\qquad 0<t\le \frac1{\sqrt3},
\]
and
\[
\rho(T)=\frac{r(T)}{R(T)}.
\]
Define
\[
L(t)=
\begin{cases}
t,&0<t\le \sqrt2-1,\\[3pt]
\displaystyle\frac{4t^2(1-t^2)}{(1+t^2)^2},
   &\sqrt2-1\le t\le 1/\sqrt3,
\end{cases}
\]
and
\[
U(t)=\frac{2t(\sqrt{1+t^2}-t)}{1+t^2}.
\]

**Theorem 2 (sharp triangle fatness window).** Every nondegenerate triangle
satisfies
\[
\boxed{L(C(T))\le \rho(T)\le U(C(T))}.
\]
For every admissible \(t\), both endpoints are attained:

- \(L(t)\) is attained by the isosceles triangle whose two smallest angles are
  both \(2\arctan t\);
- \(U(t)\) is attained by the isosceles triangle whose unique smallest angle is
  \(2\arctan t\).

Consequently,
\[
\boxed{\frac{\sqrt3}{2}\,C(T)\le \frac{r(T)}{R(T)}<2C(T)}.
\]
The lower constant \(\sqrt3/2\) is sharp, with equality for the equilateral
triangle. The upper constant \(2\) is sharp as a supremum and is approached by
isosceles triangles whose unique smallest angle tends to zero.

## Proof of Theorem 1

Write \(\alpha\) for the smallest angle of \(T\).

### Universal lower bound

Fix arbitrary distinct \(p,q\in T\). After a similarity, take
\[
p=(-1,0),\qquad q=(1,0).
\]
The perpendicular bisector is the \(y\)-axis. Write
\[
T\cap\{x=0\}=[(0,-h_-),(0,h_+)]
\]
with \(h_-,h_+\ge0\). Hence
\[
C(T,p,q)=\frac{h_++h_-}{2}.
\]

Choose a side line of \(T\) supporting the upper endpoint \((0,h_+)\), and
write it as
\[
y=h_++ax,
\]
with \(T\) lying below this line. The line cannot be vertical, because it must
have both \(p\) and \(q\) in the same supporting half-plane. Since \(p,q\in T\),
\[
0\le h_+-a,\qquad 0\le h_++a,
\]
so
\[
h_+\ge |a|.
\]
Similarly, choose a side line supporting the lower endpoint and write it as
\[
y=-h_-+bx,
\]
with \(T\) above it. Again \(p,q\in T\) gives
\[
h_-\ge |b|.
\]

Put
\[
\phi=\arctan a,\qquad \psi=\arctan b.
\]
The two supporting lines are distinct side lines of \(T\). If \(\theta\) is
the smaller angle between their unoriented lines, then \(\theta\ge\alpha\).
Indeed, if the corresponding interior triangle angle is at most \(\pi/2\),
then \(\theta\) is that angle; if it is larger than \(\pi/2\), then
\(\theta\) is its supplement, which equals the sum of the other two triangle
angles and is therefore at least \(2\alpha\).

Moreover,
\[
\theta\le |\phi|+|\psi|.
\]
Using the convexity and monotonicity of \(\tan\) on \([0,\pi/2)\),
\[
|a|+|b|
=\tan|\phi|+\tan|\psi|
\ge
2\tan\frac{|\phi|+|\psi|}{2}
\ge
2\tan\frac\alpha2.
\]
Therefore
\[
C(T,p,q)
=\frac{h_++h_-}{2}
\ge \frac{|a|+|b|}{2}
\ge \tan\frac\alpha2.
\]
Since \(p,q\) were arbitrary,
\[
C(T)\ge \tan(\alpha/2).
\]

### Equality from the smallest-angle bisector

Let \(A\) have angle \(\alpha\), let \(AB=c\), \(AC=b\), and let the internal
angle bisector \(AD\) meet \(BC\) at \(D\). Place \(A=(0,0)\) and \(AD\) on
the positive \(x\)-axis, so the two adjacent sides make angles
\(\pm\alpha/2\) with the \(x\)-axis.

The standard angle-bisector-length formula gives
\[
|AD|=\frac{2bc\cos(\alpha/2)}{b+c}=: \ell.
\]
The perpendicular bisector of \(AD\) is \(x=\ell/2\). It meets \(AB\) and
\(AC\) before their endpoints: the distance from \(A\) to either such
intersection, measured along the corresponding ray, is
\[
\frac{\ell}{2\cos(\alpha/2)}=\frac{bc}{b+c}\le \min\{b,c\}.
\]
Also the opposite side \(BC\) lies beyond \(x=\ell/2\) at those two rays.
Hence the whole intersection of \(T\) with the perpendicular bisector has
length
\[
\ell\tan(\alpha/2).
\]
Thus
\[
C(T,A,D)=\tan(\alpha/2),
\]
which matches the lower bound and proves Theorem 1.

## Proof of Theorem 2

Let the triangle angles be
\[
\alpha\le\beta\le\gamma,\qquad
x=\alpha/2,\quad y=\beta/2,\quad z=\gamma/2,
\]
so \(x+y+z=\pi/2\), and put
\[
t=\tan x,\qquad u=\tan y.
\]
By Theorem 1, \(t=C(T)\).

The radius \(R(T)\) of a smallest containing disk is half the longest side when
\(\gamma\ge\pi/2\), and is the usual circumcircle radius when
\(\gamma\le\pi/2\).

### Case 1: \(\gamma\ge\pi/2\)

Let \(R_\triangle\) be the usual circumcircle radius and let \(c\) be the
longest side. Then
\[
R(T)=c/2=R_\triangle\sin\gamma.
\]
Using
\[
r=4R_\triangle\sin x\sin y\sin z
\]
and \(\cos z=\sin(x+y)\),
\[
\rho(T)
=\frac{2\sin x\sin y}{\sin(x+y)}
=\frac{2tu}{t+u}.
\]
Here
\[
x\le y\le \frac\pi4-x,
\]
so this case exists exactly for \(x\le\pi/8\), equivalently
\(t\le\sqrt2-1\). For fixed \(t\), \(2tu/(t+u)\) is increasing in \(u\).
Thus its minimum is attained at \(y=x\) and equals \(t\); its maximum within
this case occurs at \(\gamma=\pi/2\).

### Case 2: \(\gamma\le\pi/2\)

Now \(R(T)=R_\triangle\), hence
\[
\rho(T)
=4\sin x\sin y\sin z
=
\frac{4tu(1-tu)}{(1+t^2)(1+u^2)}.
\]
For fixed \(t\), the allowed interval ends at \(y=z\), namely
\[
y\le \frac\pi4-\frac x2,
\qquad
u\le u_*=\tan\left(\frac\pi4-\frac x2\right)
=\sqrt{1+t^2}-t.
\]
The \(u\)-dependent factor
\[
g(u)=\frac{u(1-tu)}{1+u^2}
\]
has derivative
\[
g'(u)=\frac{1-u^2-2tu}{(1+u^2)^2},
\]
which is nonnegative precisely for \(u\le u_*\). Thus \(\rho(T)\) is
increasing in \(y\) throughout the allowed interval.

The maximum therefore always occurs at \(y=z\). Since
\[
\sin^2 y
=\frac{1-\sin x}{2},
\]
we obtain
\[
\rho_{\max}(t)
=4\sin x\sin^2y
=2\sin x(1-\sin x)
=
\frac{2t(\sqrt{1+t^2}-t)}{1+t^2}
=U(t).
\]

For the minimum, if \(x\le\pi/8\), the obtuse/right case is available and
gives the smaller endpoint \(t\). If \(x\ge\pi/8\), every triangle with
smallest angle \(2x\) is acute or right, and the minimum occurs at \(y=x\).
Substitution gives
\[
\rho_{\min}(t)
=
\frac{4t^2(1-t^2)}{(1+t^2)^2}.
\]
This proves the sharp window and its equality cases.

Finally, on \(t\in[\sqrt2-1,1/\sqrt3]\),
\[
\frac{L(t)}t
=
\frac{4t(1-t^2)}{(1+t^2)^2}
\]
decreases to \(\sqrt3/2\), while for smaller \(t\), \(L(t)/t=1\).
Also \(U(t)<2t\) for every \(t>0\) and \(U(t)/t\to2\) as \(t\downarrow0\).
This proves the sharp linear corollary.

## Relation to prior work

Pach and Tardos introduced \(C(S)\) in arXiv:2609.20702 (submitted
17 September 2026). Their paper gives \(C=1\) for the disk and square and
proves the general inequalities
\[
D(S)\le C(S)\le 2D(S),
\qquad
0.28\,C(S)\le r(S)/R(S)\le2C(S),
\]
where \(D(S)=\operatorname{area}(S)/\operatorname{diam}(S)^2\). It does
not give an evaluation of \(C\) for arbitrary triangles or a sharp
triangle-specific comparison with \(r/R\).

The minimum angle and inradius/circumradius ratios are classical triangle and
mesh-quality parameters. The new point here is the exact identification of
the Pach--Tardos invariant with the half-angle tangent, together with the
sharp conversion interval between that newly introduced invariant and
smallest-enclosing-disk fatness.

Targeted searches using the defining perpendicular-bisector formulation,
"roundness", triangle/minimum-angle terminology, the source title and arXiv
identifier, and equivalent half-angle formulations did not locate this formula
or the sharp fatness window. Because the defining invariant was introduced in
a very recent preprint, unindexed or unpublished parallel work remains a
residual originality risk.

## Limitations

The exact formula and sharp conversion window are specific to Euclidean
triangles. They do not sharpen the Pach--Tardos comparison constants for
arbitrary convex bodies, nor do they improve the equal-area partition constant
in their Theorem 1. The result concerns the radius of a smallest disk
containing the triangle, as in convex-body fatness; for an obtuse triangle
this differs from the radius of the circle through all three vertices.

## Reference

J. Pach and G. Tardos, *Cutting a convex body into fat parts and approximating
Euclidean distance by graph distances*, arXiv:2609.20702 (2026),
https://arxiv.org/abs/2609.20702.
