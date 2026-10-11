# Sharp James envelope for the Takahashi minimum von Neumann--Jordan constant
## Finding
Let \(X\) be a real Banach space with \(\dim X\ge2\). For the classical Takahashi minimum von Neumann--Jordan constant
\[
C_{-\infty}(X)
=
\sup_{(x,y)\ne(0,0)}
\frac{\min\{\|x+y\|^2,\|x-y\|^2\}}
{\|x\|^2+\|y\|^2},
\]
and the James constant
\[
J(X)
=
\sup_{u,v\in S_X}
\min\{\|u+v\|,\|u-v\|\},
\]
one has the sharp universal envelope
\[
\boxed{
C_{-\infty}(X)
\le
1+\bigl(J(X)-1\bigr)^2
}.
\tag{1}
\]

The envelope is attained by the affine-regular hexagonal Day--James plane
\[
H=(\mathbb R^2,N),
\qquad
N(s,t)=\max\{|s|,|t|,|s-t|\}.
\]
Indeed,
\[
J(H)=\frac32
\]
and
\[
\boxed{
C_{-\infty}(H)=\frac54
=
1+\left(\frac32-1\right)^2
}.
\tag{2}
\]

Thus (1) is best possible as a function of \(J(X)\): no smaller universal function can replace its right-hand side at the James value \(3/2\).

## Assumptions and scope
All spaces and scalars are real. The dimension assumption excludes the one-dimensional degenerate setting and matches the standard geometric-constant framework.

The norm on \(H\) is equivalently the Day--James \(\ell_\infty-\ell_1\) norm:
\[
N(s,t)
=
\begin{cases}
\max\{|s|,|t|\},&st\ge0,\\
|s|+|t|,&st\le0.
\end{cases}
\]
Its unit sphere is the affine-regular hexagon with vertices
\[
(1,0),\ (1,1),\ (0,1),\ (-1,0),\ (-1,-1),\ (0,-1).
\]

## Proof
Take arbitrary nonzero \(x,y\in X\). By homogeneity and interchange of the two vectors, assume
\[
\|x\|=1,
\qquad
\|y\|=r,
\qquad
0\le r\le1.
\]
If \(r=0\), the quotient defining \(C_{-\infty}(X)\) equals \(1\), so suppose \(r>0\) and put
\[
u=\frac{y}{r}\in S_X.
\]

Write
\[
J=J(X).
\]
By the definition of the James constant, for the unit pair \(x,u\) at least one sign
\[
\sigma\in\{-1,1\}
\]
satisfies
\[
\|x+\sigma u\|\le J.
\]
Using
\[
x+\sigma y
=
(1-r)x+r(x+\sigma u),
\]
convexity of the norm gives
\[
\min\{\|x+y\|,\|x-y\|\}
\le
1-r+rJ
=
1+r(J-1).
\tag{3}
\]
Therefore
\[
\frac{\min\{\|x+y\|^2,\|x-y\|^2\}}
{\|x\|^2+\|y\|^2}
\le
\frac{\bigl(1+r(J-1)\bigr)^2}{1+r^2}.
\tag{4}
\]
Set
\[
c=J-1.
\]
The elementary identity
\[
(1+c^2)(1+r^2)-(1+cr)^2=(c-r)^2
\]
implies
\[
\frac{(1+cr)^2}{1+r^2}\le1+c^2.
\tag{5}
\]
Combining (4) and (5), then taking the supremum, proves (1).

It remains to verify sharpness.

First we compute \(J(H)\). The isometries
\[
Q(s,t)=(t,t-s),
\qquad
R(s,t)=(s,s-t)
\]
act dihedrally on the six edges of the unit hexagon. Hence it suffices to take
\[
x=(1,a),
\qquad
0\le a\le1,
\]
and reduce \(y\) to four edge classes.

If
\[
y=(1,b)
\]
or
\[
y=(-1,-b),
\qquad
0\le b\le1,
\]
one of \(N(x-y)\) and \(N(x+y)\) is at most \(1\).

If
\[
y=(c,1),
\qquad
0\le c\le1,
\]
then
\[
N(x+y)=\max\{1+c,1+a\},
\qquad
N(x-y)=2-a-c.
\]
If both exceeded \(3/2\), the first inequality would force
\[
\max\{a,c\}>\frac12,
\]
whereas the second would force
\[
a+c<\frac12,
\]
a contradiction.

If
\[
y=(-b,1-b),
\qquad
0\le b\le1,
\]
then
\[
N(x+y)=1+a-b,
\qquad
N(x-y)=\max\{1+b,2-a\}.
\]
If both exceeded \(3/2\), the first would give
\[
a-b>\frac12.
\]
Hence
\[
a>\frac12,
\qquad
b<\frac12,
\]
which makes both entries in the second maximum strictly smaller than \(3/2\), again a contradiction.

Reflection by \(R\) covers the remaining two edges. Consequently
\[
J(H)\le\frac32.
\]
For
\[
x_0=\left(1,\frac12\right),
\qquad
u_0=(0,1),
\]
one has
\[
N(x_0+u_0)=N(x_0-u_0)=\frac32,
\]
so
\[
J(H)=\frac32.
\tag{6}
\]

Now choose
\[
p=(1,0),
\qquad
q=\left(-\frac14,-\frac12\right).
\]
Then
\[
N(p)=1,
\qquad
N(q)=\frac12,
\]
and
\[
N(p+q)=N(p-q)=\frac54.
\]
Thus
\[
\frac{\min\{N(p+q)^2,N(p-q)^2\}}
{N(p)^2+N(q)^2}
=
\frac{25/16}{5/4}
=
\frac54.
\tag{7}
\]
Equations (1), (6), and (7) give (2).

## Verification
The proof of the universal inequality is exact. Its final scalar step is the identity
\[
(1+c^2)(1+r^2)-(1+cr)^2=(c-r)^2.
\]

The bundled `verify.py` uses exact rational arithmetic. It verifies the two hexagonal isometries on an integer grid, checks the four reduced edge formulas and the James upper bound on a dense rational grid, verifies the sharp James pair, verifies the \(C_{-\infty}\) witness exactly, and checks the scalar envelope identity on rational samples.

The finite grids are reproducibility checks only. The universal theorem and the complete hexagonal edge argument above are analytic and cover all admissible vectors.

## Relationship to prior work
Liu, Din and Li's 2021 paper recalls Takahashi's classical \(C_{-\infty}(X)\), introduces the parameterized quantity \(C_{-\infty}(a,X)\), and proves estimates relating that parameterized construction to a generalized James constant. The inspected defining section does not state (1), and its Day--James examples concern saturation of the parameterized quantity in specified parameter ranges rather than the classical James envelope proved here.

A 2026 paper on the direct isosceles-orthogonal Takahashi scale proves the formally similar bound
\[
C_t^I(X)\le1+\bigl(J(X)-1\bigr)^2
\]
for a different invariant whose admissible pairs are required to be unit and isosceles orthogonal before deformation. The same paper explicitly distinguishes this direct restriction from Takahashi's unrestricted scale and gives an exact diagonal isosceles reparametrization of the unrestricted profile. The present result concerns that unrestricted minimum endpoint and therefore is not implied by the restricted theorem.

The 2026 paper also identifies affine-regular hexagons as extremal for its restricted Radon-plane estimate. Here the independent edge argument computes \(J(H)=3/2\), while (7) and the universal unrestricted upper bound prove
\[
C_{-\infty}(H)=\frac54.
\]
Thus the same numerical envelope is sharp in both constructions, for different reasons.

Targeted searches used the exact invariant name, the formula \(1+(J(X)-1)^2\), Takahashi/unrestricted aliases, the affine-regular-hexagon alias, and the value \(5/4\). No public record located states the unrestricted theorem (1) or the exact classical hexagonal value as a consequence of that theorem.

## Limitations
The theorem is an upper envelope in terms of the James constant; it does not classify all spaces or all James values at which equality is possible.

The affine-regular hexagon proves sharpness at
\[
J=\frac32.
\]
No assertion is made that every admissible James value admits an equality example.

The direct isosceles-restricted Takahashi constants introduced later are different objects. Equality of the numerical bound on the hexagon does not identify the two theories in general.

Bibliographic and semantic searches cannot prove absolute novelty. An equivalent unrestricted inequality may have appeared under a different Takahashi-profile notation or as an unstated consequence of a general power-mean estimate.

## References
1. Q. Liu, A. Din and Y. Li, “Some aspects of generalized von Neumann-Jordan type constant,” *AIMS Mathematics* 6 (2021), 6309--6321, doi:10.3934/math.2021370. Published 12 April 2021. MSC 46B20.
2. “Isosceles-Orthogonal Takahashi--von Neumann--Jordan-Type Constants in Banach Spaces,” *Axioms* 15 (2026), article 684, public full text at the publisher website.
