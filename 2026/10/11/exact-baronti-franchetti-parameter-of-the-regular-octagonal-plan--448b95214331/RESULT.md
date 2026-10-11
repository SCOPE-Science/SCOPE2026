# Exact Baronti--Franchetti parameter of the regular octagonal plane
## Finding
Let \(A=(\mathbb R^2,\|\cdot\|_A)\) be the real regular-octagonal plane
\[
\|(u,v)\|_A=\max\left\{|u|+(\sqrt2-1)|v|,\ |v|+(\sqrt2-1)|u|\right\}.
\]
For the Baronti--Franchetti parameter
\[
\Lambda(A)=\inf_{x,y\in S_A}\sup_{f\in S_{A^*}}\min\{|f(x)|,|f(y)|\},
\]
one has
\[
\Lambda(A)=\frac{\sqrt2}{1+\sqrt{\,4-2\sqrt2\,}}=0.679129302431368\ldots .
\]
If \(a=\sqrt2-1\), \(s=\sqrt{4-2\sqrt2}\), and \(r_0=a/(1+s)\), then equality is attained by the isosceles-orthogonal pair
\[
x_0=\left(\frac1s,\frac{r_0}{s}\right),\qquad
y_0=\left(-\frac{r_0}{s},\frac1s\right),
\]
and by its images under the norm symmetries.

## Assumptions and scope
All scalars are real. Put
\[
a=\sqrt2-1.
\]
The parameter is exactly the quantity introduced by Baronti and Franchetti:
\[
\Lambda(E)=\inf_{x,y\in S_E}\sup_{f\in S_{E^*}}\min\{|f(x)|,|f(y)|\}.
\]
Only their regular-octagonal plane \(A\) is treated.

## Proof
Write
\[
H(x,y)=\sup_{f\in S_{A^*}}\min\{|f(x)|,|f(y)|\}.
\]
For \(\sigma\in\{-1,1\}\), separation of the origin from the segment \([x,\sigma y]\) gives
\[
\operatorname{dist}_A(0,[x,\sigma y])
=\sup_{f\in S_{A^*}}\min\{f(x),f(\sigma y)\}.
\]
Choosing \(\sigma\) according to the relative signs of \(f(x)\) and \(f(y)\) yields
\[
H(x,y)=\max\{\operatorname{dist}_A(0,[x,y]),\operatorname{dist}_A(0,[x,-y])\}.
\]

In every symmetric Minkowski plane, the unit isosceles-orthogonal companion of \((u,v)\) is \((-v,u)\), up to sign. By the octagon symmetries it is enough to take
\[
x=(u,v),\qquad y=(-v,u),\qquad u\ge v\ge0,\qquad u+av=1.
\]
Set
\[
r=\frac vu\in[0,1],\qquad u=\frac1{1+ar}.
\]
A quarter-turn maps \([x,y]\) onto \([x,-y]\), so the two segment distances coincide.

For
\[
z_\lambda=\lambda x+(1-\lambda)y,\qquad 0\le\lambda\le1,
\]
the first coordinate vanishes at
\[
\lambda_0=\frac r{1+r},
\]
and the coordinates become equal at
\[
\lambda_e=\frac{1+r}{2}.
\]
On the three successive subintervals, the derivative of the active linear facet of the norm has signs determined by
\[
-(1-a)-(1+a)r<0,\qquad
(a-1)+(a+1)r,\qquad
(1-a)+(1+a)r>0.
\]
Therefore
\[
H(x,y)=h(r)=
\begin{cases}
\displaystyle\frac{1+r^2}{\sqrt2(1+ar)},&0\le r\le a,\\[3mm]
\displaystyle\frac{1+r^2}{(1+r)(1+ar)},&a\le r\le1.
\end{cases}
\]

The same values are attained explicitly on the dual sphere. Baronti and Franchetti give
\[
\|(p,q)\|_{A^*}=
\begin{cases}
\max\{|p|,|q|\},&
\min\{|p|,|q|\}\le a\max\{|p|,|q|\},\\
(|p|+|q|)/\sqrt2,&
\min\{|p|,|q|\}\ge a\max\{|p|,|q|\}.
\end{cases}
\]
For \(0\le r\le a\),
\[
f_r=\left(\frac{1-r}{\sqrt2},\frac{1+r}{\sqrt2}\right)
\]
has dual norm one and satisfies \(f_r(x)=f_r(y)=h(r)\). For \(a\le r\le1\),
\[
f_r=\left(\frac{1-r}{1+r},1\right)
\]
has dual norm one and again satisfies \(f_r(x)=f_r(y)=h(r)\).

For the first branch the derivative has the sign of
\[
ar^2+2r-a,
\]
whose unique zero in \([0,a]\) is
\[
r_0=\frac{a}{1+\sqrt{1+a^2}}.
\]
For the second branch the derivative has the sign of
\[
r^2+2ar-1,
\]
whose unique zero in \([a,1]\) is
\[
r_1=\sqrt{1+a^2}-a.
\]
At both critical points the value is
\[
L=\frac{\sqrt2}{1+\sqrt{1+a^2}}
=\frac{\sqrt2}{1+\sqrt{4-2\sqrt2}}.
\]

It remains to pass from isosceles pairs to arbitrary unit pairs. Let \(w,z\in S_A\), and let \(k\) be the quarter-turn of \(w\). The four rays through \(w,k,-w,-k\) partition the plane. Thus for suitable signs \(\epsilon,\sigma\in\{-1,1\}\),
\[
z=\alpha\,\epsilon k+\beta\,\sigma w
\]
with \(\alpha,\beta\ge0\). Since all three vectors are unit,
\[
1=\|z\|_A\le\alpha+\beta,
\]
so \(\alpha+\beta\ge1\).

The pair \((\epsilon k,\sigma w)\) is isosceles orthogonal. By the explicit functionals above, after applying the corresponding norm symmetry there is \(f\in S_{A^*}\) with
\[
f(\epsilon k)=f(\sigma w)\ge L.
\]
Hence
\[
|f(w)|\ge L,\qquad
f(z)\ge L(\alpha+\beta)\ge L.
\]
Thus \(H(w,z)\ge L\) for every unit pair, proving \(\Lambda(A)\ge L\). The isosceles pair with \(r=r_0\) satisfies \(H(x_0,y_0)=L\), so \(\Lambda(A)\le L\). Equality follows.

## Verification
The isosceles-pair value is checked in two exact ways: by minimizing the octagonal norm along a segment and by exhibiting a dual unit functional that attains the same value. The global reduction uses all four cones determined by a unit vector and its quarter-turn, so no sphere stratum is omitted.

The included `algebra_check.py` verifies the derivative roots, equality of the two branch minima, endpoint values, and the nested-radical identity by exact symbolic simplification. No finite sampling or numerical optimization is used as proof.

## Relationship to prior work
Baronti and Franchetti introduced \(\Lambda(E)\), proved
\[
\frac12\le\Lambda(E)\le\frac1{\sqrt2},
\]
computed the affine-regular hexagon and all \(\ell_p^2\) planes, and then devoted their final section to the regular octagonal plane \(A\) and its dual. Their complete article gives several orthogonality properties of this octagon but does not state \(\Lambda(A)\).

The value found here lies strictly between the universal lower endpoint and the Hilbert value. Targeted searches using the authors, the notation \(\Lambda\), the regular-octagon description, and the exact nested radical did not locate an equivalent evaluation. Exact indexed results for the same octagon found in the comparison search concern different invariants.

## Limitations
The theorem computes only the Baronti--Franchetti parameter of this regular octagon. It does not give a formula for arbitrary regular polygons or for broader octagonal families.

A later source may restate the value under different notation; this remains the principal bibliographic residual risk. Search absence is not used by itself as a novelty proof.

## References
1. M. Baronti and C. Franchetti, “The isosceles orthogonality and a new 2-dimensional parameter in real normed spaces,” *Aequationes Mathematicae* 89 (2015), 673--683, DOI 10.1007/s00010-014-0255-9; published online 2014-03-14.
