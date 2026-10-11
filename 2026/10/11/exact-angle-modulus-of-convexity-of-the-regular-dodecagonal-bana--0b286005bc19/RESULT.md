# Exact angle modulus of convexity of the regular dodecagonal Banach plane
## Finding
Let \(X_{12}=(\mathbb R^2,N_{12})\), where
\[
N_{12}(s,t)=
\max\left\{
|s|,\ |t|,\
\left|\frac{\sqrt3s+t}{2}\right|,\
\left|\frac{s+\sqrt3t}{2}\right|,\
\left|\frac{-s+\sqrt3t}{2}\right|,\
\left|\frac{-\sqrt3s+t}{2}\right|
\right\}.
\]
Its unit ball is the regular dodecagon circumscribed about the Euclidean unit disk.

For \(0\le\epsilon\le2\), the Du--Ahmad--Din--Li angle modulus of convexity is
\[
\delta^a_{X_{12}}(\epsilon)
=
\begin{cases}
-1,
&0\le\epsilon\le4-2\sqrt3,
\\[4pt]
1-\dfrac{(4-\epsilon)^2}{6},
&4-2\sqrt3\le\epsilon\le2(\sqrt3-1),
\\[8pt]
1-\dfrac{(4-\sqrt3\,\epsilon)^2}{2},
&2(\sqrt3-1)\le\epsilon\le2.
\end{cases}
\]

Equivalently, if
\[
M(\epsilon)
=
\sup\left\{
N_{12}(x+y):
N_{12}(x)=N_{12}(y)=1,\ 
N_{12}(x-y)=\epsilon
\right\},
\]
then
\[
M(\epsilon)
=
\begin{cases}
2,
&0\le\epsilon\le4-2\sqrt3,
\\[4pt]
\dfrac{4-\epsilon}{\sqrt3},
&4-2\sqrt3\le\epsilon\le2(\sqrt3-1),
\\[8pt]
4-\sqrt3\,\epsilon,
&2(\sqrt3-1)\le\epsilon\le2.
\end{cases}
\]

## Assumptions and scope
All scalars are real. Put
\[
r_0=2-\sqrt3,
\qquad
a=4-2\sqrt3=2r_0,
\qquad
b=2(\sqrt3-1).
\]
The twelve signed supporting functionals of the unit ball are
\[
f_j(s,t)
=
s\cos\frac{j\pi}{6}
+
t\sin\frac{j\pi}{6},
\qquad
0\le j<12,
\]
so
\[
N_{12}(z)=\max_{0\le j<12}f_j(z).
\]

The angle modulus of convexity is
\[
\delta_X^a(\epsilon)
=
\inf\left\{
1-\frac12\|x+y\|^2:
x,y\in S_X,\ \|x-y\|=\epsilon
\right\}.
\]
Hence
\[
\delta_{X_{12}}^a(\epsilon)
=
1-\frac12M(\epsilon)^2.
\]
It is therefore enough to determine \(M(\epsilon)\).

## Proof
Let
\[
A=N_{12}(x+y),
\qquad
B=N_{12}(x-y)
\]
for arbitrary \(x,y\in S_{X_{12}}\). Choose signed facet functionals \(p,q\) with
\[
A=p(x+y),
\qquad
B=q(x-y).
\]
The triangle inequality gives
\[
A\le2.
\tag{1}
\]

The dual unit ball is the convex hull of the twelve facet functionals. For any two signed facet functionals \(p,q\), exact evaluation on the twelve primal vertices gives
\[
\|p+\sqrt3\,q\|_*+\|p-\sqrt3\,q\|_*\le4
\tag{2}
\]
and
\[
\|\sqrt3\,p+q\|_*+\|\sqrt3\,p-q\|_*\le4.
\tag{3}
\]
These finite inequalities can also be read from one cyclic-separation table. If the separation of \(p\) and \(q\) is \(k\pi/6\), with \(0\le k\le6\), then the left side of either (2) or (3) is respectively
\[
2\sqrt3,\quad
2+\sqrt3,\quad
4,\quad
4,\quad
4,\quad
2+\sqrt3,\quad
2\sqrt3.
\]

Using (2),
\[
\begin{aligned}
A+\sqrt3 B
&=(p+\sqrt3 q)(x)+(p-\sqrt3 q)(y)\\
&\le
\|p+\sqrt3 q\|_*+\|p-\sqrt3 q\|_*\\
&\le4.
\end{aligned}
\]
Similarly, (3) gives
\[
\sqrt3 A+B\le4.
\]
Therefore, if \(B=\epsilon\),
\[
A
\le
\min\left\{
2,\ 
4-\sqrt3\,\epsilon,\ 
\frac{4-\epsilon}{\sqrt3}
\right\}.
\tag{4}
\]

The three quantities in (4) switch order exactly at
\[
a=4-2\sqrt3
\]
and
\[
b=2(\sqrt3-1).
\]
Thus (4) is precisely the asserted three-branch upper bound for \(M(\epsilon)\).

It remains to attain every branch. The following five explicit unit-pair families cover the whole interval. Each displayed pair satisfies
\[
N_{12}(x)=N_{12}(y)=1,
\qquad
N_{12}(x-y)=\epsilon.
\]

For
\[
0\le\epsilon\le a,
\]
take
\[
x=(1,-r_0),
\qquad
y=(1,-r_0+\epsilon).
\]
Then
\[
N_{12}(x+y)=2.
\]

For
\[
a\le\epsilon\le1,
\]
take
\[
x=(1,-r_0),
\qquad
y=
\left(
\frac{4-\epsilon}{\sqrt3}-1,\ 
\epsilon-r_0
\right).
\]
Then
\[
N_{12}(x+y)=\frac{4-\epsilon}{\sqrt3}.
\]

For
\[
1\le\epsilon\le b,
\]
take
\[
x=(1,-r_0),
\qquad
y=
\left(
\sqrt3-\epsilon,\ 
\frac{\epsilon+r_0}{\sqrt3}
\right).
\]
Again,
\[
N_{12}(x+y)=\frac{4-\epsilon}{\sqrt3}.
\]

For
\[
b\le\epsilon\le\sqrt3,
\]
take
\[
x=(1,-r_0),
\qquad
y=(-2+3\sqrt3-2\epsilon,1).
\]
Then
\[
N_{12}(x+y)=4-\sqrt3\,\epsilon.
\]

Finally, for
\[
\sqrt3\le\epsilon\le2,
\]
take
\[
x=(1,2+\sqrt3-2\epsilon),
\qquad
y=(1-\sqrt3,\sqrt3-1).
\]
Then
\[
N_{12}(x+y)=4-\sqrt3\,\epsilon.
\]

These families meet the upper envelope throughout \(0\le\epsilon\le2\), so the formula for \(M(\epsilon)\) is exact. Substitution into
\[
\delta_{X_{12}}^a(\epsilon)
=
1-\frac12M(\epsilon)^2
\]
gives the three displayed branches.

## Verification
The bundled `verify.py` uses exact symbolic arithmetic.

It reconstructs the twelve facet functionals and twelve unit-ball vertices and checks all cyclic separations in the dual inequalities
\[
\|p+\sqrt3q\|_*+\|p-\sqrt3q\|_*\le4
\]
and
\[
\|\sqrt3p+q\|_*+\|\sqrt3p-q\|_*\le4.
\]
The exact seven-entry separation table is
\[
2\sqrt3,\ 
2+\sqrt3,\ 
4,\ 
4,\ 
4,\ 
2+\sqrt3,\ 
2\sqrt3.
\]

For each of the five explicit witness families, every signed facet evaluation is affine in \(\epsilon\). The checker verifies the required norm upper bounds at both endpoints of each parameter interval; affinity then proves them on the entire interval. It also verifies an identically active facet for each claimed norm, establishing equality rather than only an upper estimate.

No numerical sampling is used to establish the continuum statement.

## Relationship to prior work
Du, Ahmad, Din and Li introduced the angle modulus of convexity and proved its exact relation to the classical Clarkson modulus:
\[
\delta_X^a(\epsilon)
=
1-2(1-\delta_X(\epsilon))^2.
\]
Their paper gives general structural properties and computations on selected concrete spaces. The inspected open full text contains no occurrence of a regular polygon or dodecagon.

The closest public indexed angle-modulus result located for a regular polygon concerns the angle modulus of smoothness at one separation in the regular octagonal plane. It changes both the polygon and the extremal direction: smoothness minimizes the sum norm at fixed separation, whereas the present convexity profile maximizes it for every separation.

Other public exact dodecagonal results located in the comparison search concern unrelated affine, P-angle, James, or polygonal invariants and do not imply the full fixed-separation profile above.

## Limitations
The theorem is specific to the regular dodecagonal plane. It does not give a formula for every regular polygon or classify all unit pairs attaining the supremum.

The proof determines the full modulus through exact support geometry, but it does not address stability of near-extremizing pairs. Bibliographic and semantic searches cannot establish absolute novelty, and an equivalent computation under another normalization of the regular dodecagon remains a residual literature risk.

## References
1. D. Du, A. Ahmad, A. Din and Y. Li, “Some Moduli of Angles in Banach Spaces,” Mathematics 10 (2022), 2965, doi:10.3390/math10162965. Published 17 August 2022. MSC: 46B20.
