# Supporting-face saturation of the weighted James envelope
## Finding
For a real Banach space \(X\), write
\[
J(X)=\sup_{x,y\in S_X}\min\{\|x+y\|,\|x-y\|\}
\]
for the classical James constant, and for \(0<\lambda<1\) write
\[
J(\lambda,X)
=
\sup_{x,y\in S_X}
\min\{
\|\lambda x+(1-\lambda)y\|,
\|\lambda x-(1-\lambda)y\|
\}
\]
for the weighted James constant introduced by Liu, Sarfraz and Li.

Suppose there are \(x,y\in S_X\) and \(f_+,f_-\in S_{X^*}\) such that
\[
f_+(y)=1,
\qquad
f_+(x+y)=J(X),
\]
and
\[
f_-(-y)=1,
\qquad
f_-(x-y)=J(X).
\tag{1}
\]
Then the source's general weighted-James upper envelope is attained for every weight:
\[
\boxed{
J(\lambda,X)
=
1-\bigl(2-J(X)\bigr)\min\{\lambda,1-\lambda\}
}
\qquad
(0<\lambda<1).
\tag{2}
\]

The condition (1) has a supporting-face interpretation: the two James-extremal chords \(x+y\) and \(x-y\) remain on supporting faces that also contain \(y\) and \(-y\), respectively.

As a canonical non-Hilbert application, let
\[
H=(\mathbb R^2,N),
\qquad
N(s,t)=\max\{|s|,|t|,|s-t|\}.
\]
Then
\[
J(H)=\frac32
\]
and (1) holds. Consequently
\[
\boxed{
J(\lambda,H)
=
1-\frac12\min\{\lambda,1-\lambda\}
}
\qquad
(0<\lambda<1).
\tag{3}
\]
Thus the general upper comparison from the defining paper can be sharp for an entire weight interval even in a uniformly non-square space.

## Assumptions and scope
All spaces and scalars are real. The theorem is a sufficient equality criterion; it does not claim that (1) is necessary.

For the affine-regular hexagon, the unit sphere has six edges
\[
\begin{aligned}
E_0&=\{(1,a):0\le a\le1\},\\
E_1&=\{(c,1):0\le c\le1\},\\
E_2&=\{(-b,1-b):0\le b\le1\},\\
E_3&=\{(-1,-b):0\le b\le1\},\\
E_4&=-E_1,\qquad E_5=-E_2.
\end{aligned}
\]
The maps
\[
Q(s,t)=(t,t-s)
\]
and
\[
R(s,t)=(s,s-t)
\]
are linear isometries because they permute the three quantities
\[
|s|,\qquad |t|,\qquad |s-t|.
\]
The map \(Q\) acts transitively on the six edges, and \(R\) stabilizes \(E_0\) while pairing the two edge classes on either side. Hence any unit pair can be reduced to
\[
x=(1,a)\in E_0
\]
with the second vector on \(E_0,E_1,E_2\), or \(E_3\).

## Proof
First note the exact symmetry
\[
J(\lambda,X)=J(1-\lambda,X).
\tag{4}
\]
Indeed, swapping \(x\) and \(y\) in the defining supremum and using \(\|z\|=\|-z\|\) changes the weight \(\lambda\) to \(1-\lambda\) without changing the two norm values.

It is therefore enough to take
\[
0<\lambda\le\frac12.
\]
Put
\[
j=J(X),
\qquad
d=1-2\lambda.
\]
For a pair satisfying (1),
\[
\lambda x+(1-\lambda)y
=
\lambda(x+y)+dy.
\]
Applying \(f_+\) gives
\[
\|\lambda x+(1-\lambda)y\|
\ge
f_+\bigl(\lambda(x+y)+dy\bigr)
=
\lambda j+d.
\tag{5}
\]
Likewise,
\[
\lambda x-(1-\lambda)y
=
\lambda(x-y)-dy,
\]
and \(f_-(-y)=1\) yields
\[
\|\lambda x-(1-\lambda)y\|
\ge
\lambda j+d.
\tag{6}
\]
Thus
\[
J(\lambda,X)\ge\lambda j+1-2\lambda.
\tag{7}
\]

The weighted-James comparison theorem of Liu, Sarfraz and Li gives, for \(0<\lambda\le1/2\),
\[
J(\lambda,X)
\le
\lambda J(X)+1-2\lambda.
\tag{8}
\]
Equations (7) and (8) coincide, so
\[
J(\lambda,X)
=
1-\bigl(2-j\bigr)\lambda
\qquad
\left(0<\lambda\le\frac12\right).
\]
Applying (4) gives (2) on the full interval.

We now verify the hexagonal application independently.

Fix
\[
x=(1,a),
\qquad 0\le a\le1.
\]
If
\[
y=(1,b)\in E_0,
\]
then
\[
N(x-y)=|a-b|\le1.
\]
If
\[
y=(-1,-b)\in E_3,
\]
then
\[
N(x+y)=|a-b|\le1.
\]
Neither class can force the James minimum above \(3/2\).

For
\[
y=(c,1)\in E_1,
\]
direct evaluation gives
\[
N(x+y)=1+\max\{a,c\},
\qquad
N(x-y)=2-a-c.
\tag{9}
\]
If both quantities in (9) were greater than \(3/2\), then
\[
\max\{a,c\}>\frac12
\]
and simultaneously
\[
a+c<\frac12,
\]
which is impossible.

For
\[
y=(-b,1-b)\in E_2,
\]
one obtains
\[
N(x+y)=1+a-b,
\qquad
N(x-y)=\max\{1+b,2-a\}.
\tag{10}
\]
If the first quantity in (10) were greater than \(3/2\), then
\[
a-b>\frac12,
\]
hence
\[
a>\frac12,\qquad b<\frac12.
\]
Both entries of the maximum in (10) would then be strictly less than \(3/2\). Therefore every unit pair satisfies
\[
\min\{N(x+y),N(x-y)\}\le\frac32.
\]
The pair
\[
x=\left(1,\frac12\right),
\qquad
y=(0,1)
\tag{11}
\]
has
\[
N(x+y)=N(x-y)=\frac32,
\]
so
\[
J(H)=\frac32.
\tag{12}
\]

Finally define
\[
f_+(s,t)=t,
\qquad
f_-(s,t)=s-t.
\]
Both have dual norm \(1\), because their absolute values are bounded by \(N(s,t)\) and each bound is attained on the unit sphere. For the pair (11),
\[
f_+(y)=1,
\qquad
f_+(x+y)=\frac32,
\]
and
\[
f_-(-y)=1,
\qquad
f_-(x-y)=\frac32.
\]
Thus (1) holds with \(j=3/2\), and (2) gives (3).

## Verification
The proof of the saturation criterion is symbolic and uses only the defining source's weighted-James upper estimate plus two norm-one supporting functionals.

The hexagonal value \(J(H)=3/2\) is proved by an exhaustive dihedral edge reduction. No numerical search is used for that upper bound.

The bundled `verify.py` uses exact rational arithmetic. It checks that \(Q\) and \(R\) preserve the hexagonal norm, verifies the four reduced edge formulas on rational grids, confirms the classical James witness, and checks the weighted witness
\[
x=\left(1,\frac12\right),
\qquad
y=(0,1)
\]
for every reduced rational weight with denominator at most \(80\). The finite grid is supplementary only; equations (5)--(10) prove the continuous statements.

## Relationship to prior work
Liu, Sarfraz and Li introduced the weighted James constant in 2021. Their Section 5 proves general lower and upper comparisons with the classical James constant. On the half interval \(0<\lambda\le1/2\), their upper estimate is exactly
\[
J(\lambda,X)
\le
\lambda J(X)+1-2\lambda.
\]
The inspected defining article does not give a supporting-face equality criterion for this bound and does not compute the weighted profile of the affine-regular hexagonal plane.

The literature already contains exact weighted-James calculations for other spaces, notably classical sequence spaces. Those results use the geometry of their own unit spheres and do not imply (1) or the hexagonal formula (3).

The criterion isolates a reusable geometric mechanism behind equality: a single James-extremal pair and two support functionals simultaneously certify the source upper estimate for every weight. The affine-regular hexagon shows that this mechanism is not confined to the square endpoint \(J(X)=2\); here
\[
J(H)=\frac32<2.
\]

## Limitations
Condition (1) is sufficient, not proved necessary. A space could saturate the weighted-James upper envelope through different maximizing pairs at different weights.

The explicit application is restricted to the affine-regular hexagonal plane. No claim is made here about all regular polygons or all Radon planes.

Bibliographic and semantic searches cannot prove absolute novelty. An equivalent equality observation may occur under supporting-face or exposed-face terminology without using the phrase “weighted James constant.”

## References
1. Q. Liu, M. Sarfraz and Y. Li, “Some aspects of generalized Zbăganu and James constant in Banach spaces,” *Demonstratio Mathematica* 54 (2021), 299–310, doi:10.1515/dema-2021-0033. Published online 16 August 2021. Primary MSC 46B20.
