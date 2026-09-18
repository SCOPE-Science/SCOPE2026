# Exact triangle formula for Pach--Tardos roundness and sharp fatness calibration

## Main result

For a compact planar convex set \(S\), Pach and Tardos define
\[
C(S,p,q)=\frac{|S\cap \ell_{p,q}|}{|p-q|},\qquad
C(S)=\inf_{p\ne q}C(S,p,q),
\]
where \(\ell_{p,q}\) is the perpendicular bisector of \(pq\). They call
\(C(S)\) the roundness of \(S\).

Let \(T\) be a nondegenerate triangle and let \(\alpha\in(0,\pi/3]\) be its
smallest interior angle.

**Theorem 1.**
\[
\boxed{C(T)=\tan\frac{\alpha}{2}}.
\]
If \(A\) is a vertex of angle \(\alpha\) and \(D\) is where the internal
angle bisector from \(A\) meets the opposite side, then \(C(T,A,D)=C(T)\).

Thus the new Pach--Tardos invariant is, on triangles, exactly a monotone
transform of the classical minimum-angle mesh-quality parameter.

There is also a sharp conversion to convex-body fatness. Let \(r(T)\) be the
inradius, \(R(T)\) the radius of a smallest containing disk, and put
\[
t=C(T),\qquad \rho(T)=\frac{r(T)}{R(T)}.
\]
Then \(0<t\le1/\sqrt3\). Define
\[
L(t)=
\begin{cases}
t,&0<t\le\sqrt2-1,\\[3pt]
\displaystyle\frac{4t^2(1-t^2)}{(1+t^2)^2},
&\sqrt2-1\le t\le1/\sqrt3,
\end{cases}
\]
and
\[
U(t)=\frac{2t(\sqrt{1+t^2}-t)}{1+t^2}.
\]

**Theorem 2.**
\[
\boxed{L(C(T))\le \rho(T)\le U(C(T))}.
\]
Both endpoints are sharp for every admissible \(t\). The lower endpoint is
attained by the isosceles triangle whose two smallest angles are both
\(2\arctan t\); the upper endpoint is attained by the isosceles triangle
whose unique smallest angle is \(2\arctan t\).

In particular,
\[
\boxed{\frac{\sqrt3}{2}\,C(T)\le\frac{r(T)}{R(T)}<2C(T)}.
\]
The lower constant is optimal and is attained by the equilateral triangle.
The upper constant \(2\) is optimal as a supremum.

## Proof of Theorem 1

Fix distinct \(p,q\in T\). After a similarity, write
\[
p=(-1,0),\qquad q=(1,0).
\]
The perpendicular bisector is the \(y\)-axis. Write
\[
T\cap\{x=0\}=[(0,-h_-),(0,h_+)].
\]
Choose a side line supporting the upper endpoint and write it as
\[
y=h_++ax
\]
with \(T\) below it. Since both \((\pm1,0)\) lie in \(T\),
\[
h_+\ge |a|.
\]
Likewise, a side line supporting the lower endpoint can be written
\[
y=-h_-+bx
\]
with \(T\) above it, and
\[
h_-\ge |b|.
\]

Let \(\phi=\arctan a\) and \(\psi=\arctan b\). The two supporting lines are
distinct side lines of \(T\). If \(\theta\) is their smaller unoriented angle,
then \(\theta\ge\alpha\). Indeed, if their triangle vertex angle is acute or
right, \(\theta\) is that angle; if it is obtuse, \(\theta\) is its supplement,
the sum of the other two triangle angles, hence at least \(2\alpha\).
Also
\[
\theta\le|\phi|+|\psi|.
\]
By convexity and monotonicity of \(\tan\) on \([0,\pi/2)\),
\[
|a|+|b|
=\tan|\phi|+\tan|\psi|
\ge2\tan\frac{|\phi|+|\psi|}{2}
\ge2\tan\frac{\alpha}{2}.
\]
Therefore
\[
C(T,p,q)=\frac{h_++h_-}{2}
\ge\tan\frac{\alpha}{2}.
\]

For equality, take a minimum-angle vertex \(A\) and let its internal angle
bisector meet the opposite side at \(D\). If \(AB=c\), \(AC=b\), then
\[
|AD|=\frac{2bc\cos(\alpha/2)}{b+c}=:\ell.
\]
Place \(AD\) on the positive \(x\)-axis and the adjacent sides at angles
\(\pm\alpha/2\). The perpendicular bisector \(x=\ell/2\) meets both adjacent
sides before their endpoints because the corresponding ray distance is
\[
\frac{\ell}{2\cos(\alpha/2)}=\frac{bc}{b+c}\le\min\{b,c\}.
\]
Its intersection with \(T\) therefore has length
\[
\ell\tan(\alpha/2),
\]
so \(C(T,A,D)=\tan(\alpha/2)\).

## Proof of Theorem 2

Order the angles as
\[
\alpha\le\beta\le\gamma,
\]
and set
\[
x=\alpha/2,\qquad y=\beta/2,\qquad z=\gamma/2,\qquad
t=\tan x,\qquad u=\tan y.
\]
Then \(x+y+z=\pi/2\) and, by Theorem 1, \(t=C(T)\).

If \(\gamma\ge\pi/2\), the smallest containing disk has radius half the
longest side. Writing \(R_\triangle\) for the ordinary three-point
circumradius,
\[
R(T)=R_\triangle\sin\gamma.
\]
Using \(r=4R_\triangle\sin x\sin y\sin z\),
\[
\rho(T)
=\frac{2\sin x\sin y}{\sin(x+y)}
=\frac{2tu}{t+u}.
\]
Here \(x\le y\le\pi/4-x\), so this branch exists exactly when
\(t\le\sqrt2-1\). For fixed \(t\), the last expression is increasing in \(u\),
and its minimum is \(t\), attained at \(y=x\).

If \(\gamma\le\pi/2\), the smallest containing disk is the ordinary
circumcircle. Hence
\[
\rho(T)
=4\sin x\sin y\sin z
=\frac{4tu(1-tu)}{(1+t^2)(1+u^2)}.
\]
For fixed \(t\), the allowed interval ends at \(y=z\), equivalently
\[
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
which is nonnegative exactly for \(u\le u_*\). Thus \(\rho(T)\) increases with
\(y\) throughout the allowed interval.

The maximum always occurs at \(y=z\). Since
\[
\sin^2y=\frac{1-\sin x}{2},
\]
this gives
\[
\rho_{\max}(t)
=2\sin x(1-\sin x)
=\frac{2t(\sqrt{1+t^2}-t)}{1+t^2}
=U(t).
\]
For the minimum, the obtuse branch gives \(t\) when
\(t\le\sqrt2-1\). Once \(t\ge\sqrt2-1\), the minimum is in the acute branch
at \(y=x\), giving
\[
\rho_{\min}(t)=\frac{4t^2(1-t^2)}{(1+t^2)^2}=L(t).
\]
The stated isosceles equality cases follow from \(y=x\) and \(y=z\).

Finally, \(L(t)/t=1\) on the first branch. On the second branch,
\[
\frac{L(t)}{t}=\frac{4t(1-t^2)}{(1+t^2)^2}
\]
decreases from \(1\) to \(\sqrt3/2\), while \(U(t)<2t\) and
\(U(t)/t\to2\) as \(t\downarrow0\). This proves the sharp linear corollary.

## Relation to prior work

Pach and Tardos introduced \(C(S)\) in arXiv:2609.20702, submitted
17 September 2026. Their paper records \(C=1\) for the disk and square and
proves the general comparisons
\[
D(S)\le C(S)\le2D(S),\qquad
0.28\,C(S)\le\frac{r(S)}{R(S)}\le2C(S),
\]
where \(D(S)=\operatorname{area}(S)/\operatorname{diam}(S)^2\). It does not
evaluate \(C\) for arbitrary triangles or give a sharp triangle-specific
conversion to \(r/R\).

Targeted searches covered the defining perpendicular-bisector formulation,
the source title and arXiv identifier, roundness combined with triangle and
minimum-angle terminology, equivalent half-angle formulations, and standard
mesh-quality terminology. No prior occurrence of the exact triangle formula
or the sharp fatness window was located. Because the invariant itself is
extremely recent, unindexed or unpublished parallel work remains a residual
originality risk.

## Limitations

The exact formula and sharp conversion window are triangle-specific. They do
not improve the Pach--Tardos constants for arbitrary convex bodies or their
equal-area partition constant. The \(R(T)\) used here is the convex-body
circumradius, i.e. the radius of a smallest disk containing the triangle; for
an obtuse triangle this is not the radius of the circle through its vertices.

## Reference

J. Pach and G. Tardos, *Cutting a convex body into fat parts and approximating
Euclidean distance by graph distances*, arXiv:2609.20702 (2026),
https://arxiv.org/abs/2609.20702.
