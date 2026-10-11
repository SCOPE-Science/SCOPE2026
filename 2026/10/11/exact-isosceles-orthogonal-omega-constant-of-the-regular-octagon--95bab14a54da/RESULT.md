# Exact isosceles-orthogonal \(\Omega\)-constant of the regular octagonal Banach plane
## Finding
Let
\[
X_8=(\mathbb R^2,N_8),
\qquad
N_8(s,u)=
\max\left\{
|s|,\ |u|,\ \frac{|s|+|u|}{\sqrt2}
\right\}.
\]
The unit ball is a Euclidean regular octagon after the standard inradius normalization.

For the Liu--Yang--Fu--Li isosceles-orthogonal constant
\[
\Omega(X)
=
\sup\left\{
\frac{\|x+2y\|^2+\|2x+y\|^2}
{5\|x+y\|^2}:
x,y\in S_X,\ x\perp_I y
\right\},
\]
where
\[
x\perp_I y
\quad\Longleftrightarrow\quad
\|x+y\|=\|x-y\|,
\]
one has
\[
\boxed{
\Omega(X_8)=\frac{3+2\sqrt2}{5}
}.
\]

Moreover, in the one-parameter representation for symmetric Minkowski planes used in the defining source, the reduced objective has exactly two maximizing ratios,
\[
t=\sqrt2-1
\qquad\text{and}\qquad
t=\sqrt2+1.
\]
A concrete sharp isosceles-orthogonal unit pair is
\[
x=(1,\sqrt2-1),
\qquad
y=(1-\sqrt2,1).
\]

## Assumptions and scope
All scalars are real. Put
\[
e_1=(1,0),
\qquad
e_2=(0,1).
\]
The octagonal norm is invariant under coordinate interchange and independent sign changes, so
\[
\|e_1+t e_2\|
=
\|e_1-t e_2\|
=
\|e_2+t e_1\|
=
\|e_2-t e_1\|
\]
for every real \(t\). Thus \(X_8\) is a symmetric Minkowski plane with axes \(e_1,e_2\).

For such a plane, Proposition 4.2 of the defining paper gives
\[
\Omega(X)
=
\max_{t\ge0}
\Phi(t),
\qquad
\Phi(t)
=
\frac{f(t)^2+f(-t)^2}{5g(t)^2},
\]
where
\[
f(t)=\|(1+2t)e_1+(2-t)e_2\|,
\]
and
\[
g(t)=\|(1+t)e_1+(1-t)e_2\|.
\]
The full text of the source was inspected at Lemma 4.1 and Proposition 4.2; the reduction covers all unit isosceles-orthogonal pairs, not merely a sampled subclass.

## Proof
Write
\[
r=\sqrt2.
\]
For the regular-octagonal norm,
\[
N_8(a,b)=
\max\left\{
|a|,\ |b|,\ \frac{|a|+|b|}{r}
\right\}.
\]

First note that
\[
\Phi(t)=\Phi(1/t)
\qquad(t>0).
\tag{1}
\]
Indeed,
\[
g(1/t)=\frac{g(t)}{t}.
\]
Using invariance of \(N_8\) under interchange of coordinates and sign changes,
\[
f(1/t)=\frac{f(-t)}{t},
\qquad
f(-1/t)=\frac{f(t)}{t},
\]
which proves (1). Hence it is enough to maximize on
\[
0\le t\le1.
\]

Define
\[
d=5r-7,
\qquad
a=r-1,
\qquad
c=\frac{5r-1}{7}.
\]
These satisfy
\[
0<d<a<c<1.
\]

Direct comparison of the three affine branches of the octagonal norm gives, for \(0\le t\le1\),
\[
g(t)=
\begin{cases}
r,&0\le t\le a,\\
1+t,&a\le t\le1,
\end{cases}
\tag{2}
\]
\[
f(t)=
\begin{cases}
\dfrac{3+t}{r},&0\le t\le c,\\[5pt]
1+2t,&c\le t\le1,
\end{cases}
\tag{3}
\]
and
\[
f(-t)=
\begin{cases}
\dfrac{3-t}{r},&0\le t\le d,\\[5pt]
2+t,&d\le t\le1.
\end{cases}
\tag{4}
\]

Substituting (2)--(4) yields the complete reduced profile on \([0,1]\):
\[
\Phi(t)=
\begin{cases}
\dfrac{t^2+9}{10},
&0\le t\le d,
\\[8pt]
\dfrac{3t^2+14t+17}{20},
&d\le t\le a,
\\[8pt]
\dfrac{3t^2+14t+17}{10(1+t)^2},
&a\le t\le c,
\\[8pt]
\dfrac{5t^2+8t+5}{5(1+t)^2},
&c\le t\le1.
\end{cases}
\tag{5}
\]

The four derivatives are respectively
\[
\frac{t}{5},
\qquad
\frac{3t+7}{10},
\qquad
-\frac{2(2t+5)}{5(1+t)^3},
\qquad
\frac{2(t-1)}{5(1+t)^3}.
\]
Therefore \(\Phi\) is strictly increasing up to
\[
t=a=\sqrt2-1
\]
and nonincreasing afterwards on \([0,1]\), with strict decrease away from the endpoint \(t=1\) in the last two pieces. Consequently
\[
\max_{0\le t\le1}\Phi(t)=\Phi(\sqrt2-1).
\]
At this point,
\[
\Phi(\sqrt2-1)
=
\frac{3+2\sqrt2}{5}.
\]
By the reciprocal symmetry (1), the only second maximizing ratio is
\[
\frac1{\sqrt2-1}=\sqrt2+1.
\]

For the explicit extremizer, take
\[
x=(1,\sqrt2-1),
\qquad
y=(1-\sqrt2,1).
\]
Both vectors have octagonal norm \(1\), and \(y\) is the quarter-turn of \(x\). Directly,
\[
N_8(x+y)=N_8(x-y)=\sqrt2,
\]
so \(x\perp_I y\). Also,
\[
N_8(x+2y)=N_8(2x+y)=1+\sqrt2.
\]
Hence
\[
\frac{N_8(x+2y)^2+N_8(2x+y)^2}
{5N_8(x+y)^2}
=
\frac{2(1+\sqrt2)^2}{10}
=
\frac{3+2\sqrt2}{5}.
\]
This matches the global upper value from (5).

## Verification
The bundled `verify.py` uses exact arithmetic in \(\mathbb Q(\sqrt2)\).

It checks the breakpoint order
\[
0<5\sqrt2-7<\sqrt2-1<\frac{5\sqrt2-1}{7}<1,
\]
verifies the norm formulas (2)--(4) on every branch by exact comparison of the active octagonal facets, checks continuity at each breakpoint, verifies the derivative signs used in the monotonicity argument, and evaluates the maximum exactly as
\[
\frac{3+2\sqrt2}{5}.
\]

It separately verifies the sharp pair
\[
x=(1,\sqrt2-1),
\qquad
y=(1-\sqrt2,1)
\]
and confirms
\[
N_8(x)=N_8(y)=1,
\quad
N_8(x+y)=N_8(x-y)=\sqrt2,
\quad
N_8(x+2y)=N_8(2x+y)=1+\sqrt2.
\]

A rational-grid reconstruction of the reduced objective is included only as a consistency check. The continuum maximum is proved analytically by the exact piecewise formulas and derivative signs.

## Relationship to prior work
Liu, Yang, Fu and Li introduced \(\Omega(X)\) from the parallelogram law under isosceles orthogonality. Their paper proves the general upper value \(8/5\) in the infinite-dimensional setting, characterizes the finite-dimensional non-uniformly-non-square endpoint, relates \(\Omega\) to the James constant, and derives the one-parameter representation for symmetric Minkowski planes used above.

The same source computes
\[
\Omega(\ell_\infty^2)=\frac85
\]
and computes
\[
\Omega=\frac{49}{40}
\]
for a classical \(\ell_\infty-\ell_1\) hexagonal plane. The inspected full text contains no occurrence of “octagon”, “octagonal”, or “regular”, and it gives no value for the regular octagonal norm.

A 2022 paper with a closely similar title introduces a different parameterized invariant denoted \(\Omega_X(\alpha)\) and identifies it with another parameterized quantity \(\gamma_X(\alpha)\). Its public abstract and bibliographic metadata were checked because of the notation collision; it is not the fixed constant \(\Omega(X)\) defined by the \(\|x+2y\|\), \(\|2x+y\|\) quotient above.

Later work on isosceles-orthogonal constants and generalized power-mean constructions was also checked at the level of statements relevant to regular polygons. No inspected source or public research record gives the value
\[
\frac{3+2\sqrt2}{5}
\]
for the regular-octagonal \(\Omega\)-constant.

## Limitations
The result computes \(\Omega\) only for the regular octagonal plane. It does not give a closed formula for every regular \(4n\)-gonal norm; numerical exploration indicates that the active branch can depend on the polygonal arithmetic, so a uniform extrapolation is not asserted.

The proof relies on the published symmetric-Minkowski reduction to one parameter; that theorem was inspected in the full defining source. The octagonal piecewise maximization after the reduction is self-contained.

Bibliographic and semantic searches cannot prove absolute novelty. An equivalent calculation may exist under a linearly equivalent octagonal normalization or without the \(\Omega\) notation.

## References
1. Q. Liu, Z. Yang, Y. Fu and Y. Li, “New geometric constants of isosceles orthogonal type,” arXiv:2111.08392, first publicly posted 16 November 2021. Mathematics Subject Classification: 46B20, 46C15.
2. Z. Yang and Y. Li, “A New Geometric Constant in Banach Spaces Related to the Isosceles Orthogonality,” Kyungpook Mathematical Journal 62 (2022), 271–287, doi:10.5666/KMJ.2022.62.2.271.
