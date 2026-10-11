# Exact Fu--Yang--Liu--Li skew James profile of the affine-regular hexagonal plane
## Finding
Let
\[
H=(\mathbb R^2,N),
\qquad
N(s,u)=\max\{|s|,|u|,|s-u|\}.
\]
For the Fu--Yang--Liu--Li skew James constant
\[
J[t,H]
=
\sup_{x,y\in S_H}
\min\{N(x+t y),N(t x-y)\},
\qquad
t>0,
\]
one has the exact formula
\[
\boxed{
J[t,H]
=
\frac{t^2+t+1}{t+1}
=
t+\frac1{t+1}
}.
\]

For \(0<t\le1\), equality is attained by
\[
x=(1,0),
\qquad
y=\left(\frac{t}{1+t},1\right).
\]
At \(t=1\), this gives the classical James value
\[
J(H)=\frac32.
\]

The source paper proves for an arbitrary Banach space the upper estimate
\[
J[t,X]
\le
\min\{1,t\}J(X)+|1-t|.
\]
For this hexagonal plane and \(0<t<1\), that estimate becomes
\[
J[t,H]\le1+\frac t2,
\]
while the exact value is
\[
1+\frac{t^2}{1+t}.
\]
The gap is
\[
\frac{t(1-t)}{2(1+t)}>0.
\]
Thus the general comparison with the ordinary James constant is strictly nonsharp at every unbalanced parameter on this canonical example.

## Assumptions and scope
All scalars are real and
\[
t>0.
\]
The unit ball of \(H\) is the affine-regular hexagon with vertices
\[
(1,0),\ (1,1),\ (0,1),\ (-1,0),\ (-1,-1),\ (0,-1).
\]

The six unit-sphere edges can be parametrized as
\[
\begin{aligned}
E_0&=\{(1,a):0\le a\le1\},\\
E_1&=\{(c,1):0\le c\le1\},\\
E_2&=\{(-b,1-b):0\le b\le1\},\\
E_3&=\{(-1,-b):0\le b\le1\},\\
E_4&=\{(-1+b,-1):0\le b\le1\},\\
E_5&=\{(b,-1+b):0\le b\le1\}.
\end{aligned}
\]

The linear maps
\[
Q(s,u)=(u,u-s)
\]
and
\[
R(s,u)=(s,s-u)
\]
are isometries of \(H\). The map \(Q\) acts transitively on the six edges, while \(R\) preserves \(E_0\) setwise and interchanges
\[
E_1\leftrightarrow E_5,
\qquad
E_2\leftrightarrow E_4.
\]
Hence, for an arbitrary pair of unit vectors, one may assume
\[
x=(1,a)\in E_0
\]
and reduce the second vector to
\[
E_0,\ E_1,\ E_2,\ \text{or }E_3.
\]

## Proof
First observe the reciprocal identity, valid in every Banach space:
\[
J[t,X]=tJ[1/t,X].
\tag{1}
\]
Indeed,
\[
tJ[1/t,X]
=
\sup_{x,y\in S_X}
\min\{\|t x+y\|,\|x-t y\|\}.
\]
After swapping \(x\) and \(y\) and using symmetry of the norm, this is exactly
\[
J[t,X].
\]
It therefore suffices to prove the formula for
\[
0<t\le1.
\]

Put
\[
L
=
\frac{t^2+t+1}{t+1}
=
1+\frac{t^2}{1+t}.
\tag{2}
\]
Fix
\[
x=(1,a),
\qquad
0\le a\le1.
\]

### Case \(E_0\)

Let
\[
y=(1,b),
\qquad
0\le b\le1.
\]
Then
\[
N(t x-y)
=
N(1-t,b-ta)
\le1.
\]
Indeed,
\[
|1-t|\le1,
\qquad
|b-ta|\le1,
\]
and
\[
|1-t-b+ta|\le1.
\]
Therefore
\[
\min\{N(x+t y),N(t x-y)\}
\le1
\le L.
\tag{3}
\]

### Case \(E_3\)

Let
\[
y=(-1,-b),
\qquad
0\le b\le1.
\]
Then
\[
N(x+t y)
=
N(1-t,a-tb)
\le1
\]
by the same endpoint bounds, and hence
\[
\min\{N(x+t y),N(t x-y)\}
\le1
\le L.
\tag{4}
\]

### Case \(E_1\)

Let
\[
y=(c,1),
\qquad
0\le c\le1.
\]
Set
\[
A=N(x+t y),
\qquad
B=N(t x-y).
\]
A direct evaluation of the polyhedral norm gives
\[
A=\max\{1+tc,a+t\}
\tag{5}
\]
and
\[
B=1-ta+\max\{0,t-c\}.
\tag{6}
\]

If
\[
c\ge t,
\]
then
\[
B=1-ta\le1\le L.
\]

Suppose instead that
\[
c<t.
\]
If both
\[
A>L
\quad\text{and}\quad
B>L
\]
held, then from (6),
\[
c+ta<1+t-L=\frac{t}{1+t}.
\tag{7}
\]
In particular,
\[
c<\frac{t}{1+t},
\]
so
\[
1+tc<L.
\]
Thus (5) would force
\[
a+t>L,
\]
or
\[
a>\frac1{1+t}.
\tag{8}
\]
But (7) also implies
\[
ta<\frac{t}{1+t},
\]
hence
\[
a<\frac1{1+t},
\]
contradicting (8). Therefore
\[
\min\{A,B\}\le L.
\tag{9}
\]

Equality is attained in this case by
\[
a=0,
\qquad
c=\frac{t}{1+t},
\]
because then
\[
A=B=L.
\tag{10}
\]

### Case \(E_2\)

Let
\[
y=(-b,1-b),
\qquad
0\le b\le1.
\]
Again write
\[
A=N(x+t y),
\qquad
B=N(t x-y).
\]
Directly,
\[
A=-tb+\max\{1,a+t\}
\tag{11}
\]
and
\[
B=\max\{t+b,1+t-ta\}.
\tag{12}
\]

If
\[
a+t\le1,
\]
then
\[
A\le1\le L.
\]
Assume
\[
a+t>1
\]
and suppose both
\[
A>L
\quad\text{and}\quad
B>L.
\]
From (11),
\[
a>\frac1{1+t}+tb.
\tag{13}
\]
Since (12) is larger than \(L\), at least one of its two entries is larger than \(L\).

If
\[
t+b>L,
\]
then
\[
b>\frac1{1+t},
\]
and (13) gives
\[
a>1,
\]
a contradiction.

If instead
\[
1+t-ta>L,
\]
then
\[
a<\frac1{1+t},
\]
which also contradicts (13). Hence
\[
\min\{A,B\}\le L.
\tag{14}
\]

There is a second equality family:
\[
b=0,
\qquad
a=\frac1{1+t},
\]
for which again
\[
A=B=L.
\tag{15}
\]

The reflection \(R\) reduces \(E_4\) and \(E_5\) to the already treated \(E_2\) and \(E_1\). Together with edge transitivity, (3), (4), (9), and (14) prove
\[
J[t,H]\le L
\qquad
(0<t\le1).
\]
Equation (10) gives equality, so
\[
J[t,H]=L
\qquad
(0<t\le1).
\tag{16}
\]

Finally, for
\[
t\ge1,
\]
apply (1) to \(1/t\):
\[
J[t,H]
=
t\,\frac{t^{-2}+t^{-1}+1}{t^{-1}+1}
=
\frac{t^2+t+1}{t+1}.
\]
This proves the full profile.

## Verification
The bundled `verify.py` uses only exact rational arithmetic.

It verifies that \(Q\) and \(R\) preserve
\[
N(s,u)=\max\{|s|,|u|,|s-u|\},
\]
checks the six edge parametrizations, and tests the exact formulas (5), (6), (11), and (12) on rational grids.

For every reduced rational
\[
0<t\le1
\]
with denominator at most \(10\), it exhaustively checks rational edge parameters with denominator at most \(10\), confirms
\[
\min\{N(x+t y),N(t x-y)\}\le\frac{t^2+t+1}{t+1}
\]
on all four canonical edge classes, and verifies both equality families exactly.

These finite checks are reproducibility aids, not the proof of the continuum statement. The infinite parameter range is covered by the analytic edge inequalities above and the exact reciprocal identity.

## Relationship to prior work
Fu, Yang, Liu and Li introduced \(J[t,X]\) in 2023 as the skew version of Milman's moduli. Their Section 5 proves the Hilbert value
\[
J[t,H_{\mathrm{Hilbert}}]=\sqrt{1+t^2},
\]
establishes duality estimates, and derives
\[
\max\{1,t\}J(X)-|1-t|
\le
J[t,X]
\le
\min\{1,t\}J(X)+|1-t|.
\]
The same paper uses the affine-regular hexagonal plane considered here as Example 3.1.4 for the different squared-sum invariant \(E[t,X]\), and later computes its skew von Neumann--Jordan constant. The inspected Section 5 gives no \(J[t,X]\) computation for that plane.

Rao, Liu, Wu, Yin and Ni introduced a later generalized-mean skew James type constant. Their definition contains Fu--Yang--Liu--Li's \(J[t,X]\) as the negative-infinity mean endpoint. They also treat the same hexagonal norm, but the displayed extreme-point formula and its proof are explicitly restricted to generalized-mean exponent at least \(1\). Thus that example does not determine the negative-infinity endpoint used here.

The present formula therefore supplies the missing minimum-type endpoint on the same canonical test plane. It also shows that the 2023 source's general upper comparison with the ordinary James constant is strictly nonsharp whenever
\[
t\ne1.
\]

## Limitations
The result is specific to the affine-regular hexagonal plane. It does not determine the skew James profile of arbitrary regular polygons, arbitrary Radon planes, or general polyhedral Banach planes.

The edge proof gives explicit sharp families but does not attempt to classify every maximizing pair.

The later generalized-mean paper is highly relevant because it contains \(J[t,X]\) as a limiting member of a larger family. Its regular-hexagon calculation is proved only for mean exponent at least \(1\); no assertion is made here about what additional endpoint information might be obtainable from other arguments in that framework.

Bibliographic and semantic searches cannot establish absolute novelty. An equivalent minimum-type hexagonal computation under a different affine normalization remains a residual literature risk.

## References
1. Y. Fu, Z. Yang, Q. Liu and Y. Li, “On Some Skew Constants in Banach Spaces,” Kyungpook Mathematical Journal 63 (2023), 199–223, doi:10.5666/KMJ.2023.63.2.199. Public date: 27 September 2023.
2. Z. Rao, Q. Liu, Q. Wu, Z. Yin and Q. Ni, “The skew James type constant in Banach spaces,” arXiv:2504.00827, first posted 31 March 2025; later published in Analysis Mathematica 52 (2026), 619–636.
