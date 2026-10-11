# Mean-square widths of all five Platonic solids
## Finding
Let \(P\subset\mathbb R^3\) be a regular Platonic solid with edge length \(1\). For \(u\in S^2\), let
\[
w_P(u)=h_P(u)+h_P(-u)
\]
be its width in direction \(u\). If \(U\) is uniformly distributed on \(S^2\), then
\[
\begin{array}{c|c}
P & \mathbb E\,w_P(U)^2\\ \hline
\text{tetrahedron} &
\displaystyle \frac13\left(1+\frac{3+\sqrt3}{\pi}\right)\\[5pt]
\text{cube} &
\displaystyle 1+\frac4\pi\\[5pt]
\text{octahedron} &
\displaystyle \frac23+\frac{4}{\pi\sqrt3}\\[5pt]
\text{dodecahedron} &
\displaystyle \frac{3+\sqrt5}{2}
+\frac{10}{\pi}\sqrt{1+\frac{2}{\sqrt5}}\\[5pt]
\text{icosahedron} &
\displaystyle \frac{5+\sqrt5}{6}
+\frac{10}{\pi\sqrt3}.
\end{array}
\tag{1}
\]

Numerically, the five values in the same order are approximately
\[
0.835419517991,\quad
2.273239544735,\quad
1.401771860562,\quad
6.999193713256,\quad
3.043774314323.
\]

The tetrahedron and cube entries were evaluated previously. Formula (1) completes the exact Platonic-solid table; the dodecahedral entry is obtained below together with a single normal-fan derivation that simultaneously gives all four centrally symmetric cases.

## Assumptions and scope
All solids have Euclidean edge length \(1\). Spherical integration uses ordinary surface area measure \(d\sigma\) on \(S^2\), so uniform expectation is
\[
\mathbb E\,f(U)=\frac1{4\pi}\int_{S^2}f(u)\,d\sigma(u).
\]

The support function is
\[
h_P(u)=\max_{x\in P}x\cdot u.
\]
For a centrally symmetric solid centered at the origin,
\[
w_P(u)=2h_P(u).
\tag{2}
\]

The normal cell of a vertex \(v\) is the set of directions for which \(v\) maximizes the support function. For a regular polyhedron it is a regular spherical polygon centered at the radial direction \(v/\lVert v\rVert\).

No claim is made about the full width distributions or higher moments of the dodecahedron or icosahedron.

## Proof
We first derive a common formula for the four centrally symmetric Platonic solids.

Let \(P\) be a unit-edge, centrally symmetric regular polyhedron with \(N\) vertices, circumradius \(R\), and vertex valency \(q\). Fix a vertex \(v\), put
\[
n=\frac vR,
\]
and let \(C\) be the normal cell of \(v\). If \(\theta\) is spherical distance from \(n\), then on \(C\),
\[
h_P(u)=v\cdot u=R\cos\theta.
\tag{3}
\]

Let \(v'\) be a neighbor of \(v\). The corresponding side of \(C\) lies on the great circle
\[
(v-v')\cdot u=0.
\]
If \(\delta\) is the spherical distance from \(n\) to that side, then the edge-length condition
\[
\lVert v-v'\rVert=1
\]
and
\[
v\cdot v'=R^2-\frac12
\]
give
\[
\sin\delta
=
\frac{n\cdot(v-v')}{\lVert v-v'\rVert}
=
\frac1{2R}.
\tag{4}
\]

The \(q\) side normals are equally spaced around \(n\). Put
\[
\alpha=\frac{\pi}{q}.
\]
One of the \(q\) equal sectors of \(C\) has spherical polar coordinates
\[
-\alpha\le\psi\le\alpha,
\qquad
0\le\theta\le\theta_b(\psi),
\]
where the bounding great circle satisfies
\[
\tan\theta_b(\psi)=\frac{\tan\delta}{\cos\psi}.
\tag{5}
\]
Consequently,
\[
I_q(\delta):=
\int_C\cos^2\theta\,d\sigma
=
\frac q3\left(2\alpha-J\right),
\tag{6}
\]
with
\[
J=
\int_{-\alpha}^{\alpha}
\frac{\cos^3\psi}
{\left(\cos^2\psi+\tan^2\delta\right)^{3/2}}
\,d\psi.
\tag{7}
\]

Set
\[
x=\sin\psi,
\qquad
A=\sec^2\delta.
\]
Then
\[
J=
\int_{-\sin\alpha}^{\sin\alpha}
\frac{1-x^2}{(A-x^2)^{3/2}}\,dx.
\]
An antiderivative is
\[
\arcsin\left(\frac{x}{\sqrt A}\right)
+
(1-A)\frac{x}{A\sqrt{A-x^2}},
\]
so
\[
J=
2\arcsin(\sin\alpha\cos\delta)
-
\frac{
2\sin^2\delta\sin\alpha\cos\delta
}{
\sqrt{1-\sin^2\alpha\cos^2\delta}
}.
\tag{8}
\]
Equations (6)--(8) therefore give
\[
I_q(\delta)
=
\frac q3\left[
\frac{2\pi}{q}
-2\arcsin\!\left(\sin\frac{\pi}{q}\cos\delta\right)
+\frac{
2\sin^2\delta\sin(\pi/q)\cos\delta
}{
\sqrt{1-\sin^2(\pi/q)\cos^2\delta}
}
\right].
\tag{9}
\]

Using (2), (3), and the \(N\) congruent normal cells,
\[
\mathbb E\,w_P(U)^2
=
\frac1{4\pi}\int_{S^2}4h_P(u)^2\,d\sigma(u)
=
\frac{NR^2}{\pi}I_q(\delta).
\tag{10}
\]

For the cube,
\[
N=8,\qquad q=3,\qquad R^2=\frac34,
\qquad
\sin^2\delta=\frac13.
\]
Here
\[
\sin\frac\pi3\cos\delta=\frac1{\sqrt2},
\]
and (9)--(10) give
\[
\mathbb E\,w_{\rm cube}(U)^2=1+\frac4\pi.
\]

For the octahedron,
\[
N=6,\qquad q=4,\qquad R^2=\frac12,
\qquad
\sin^2\delta=\frac12.
\]
Now
\[
\sin\frac\pi4\cos\delta=\frac12,
\]
so
\[
I_4(\delta)=\frac{2\pi}{9}+\frac4{3\sqrt3},
\]
and therefore
\[
\mathbb E\,w_{\rm oct}(U)^2
=
\frac23+\frac4{\pi\sqrt3}.
\]

For the icosahedron,
\[
N=12,\qquad q=5,\qquad
R^2=\frac{5+\sqrt5}{8},
\qquad
\sin^2\delta=\frac{5-\sqrt5}{10}.
\]
Again
\[
\sin\frac\pi5\cos\delta=\frac12,
\]
which gives
\[
I_5(\delta)
=
\frac\pi9+
\frac{10}{3\sqrt3}\sin^2\delta.
\]
Since
\[
4R^2\sin^2\delta=1,
\]
equation (10) yields
\[
\mathbb E\,w_{\rm ico}(U)^2
=
\frac{5+\sqrt5}{6}
+
\frac{10}{\pi\sqrt3}.
\]

For the dodecahedron,
\[
N=20,\qquad q=3,\qquad
R^2=\frac{3(3+\sqrt5)}8,
\qquad
\sin^2\delta=\frac{3-\sqrt5}{6}.
\]
This time
\[
\sin\frac\pi3\cos\delta
=
\frac{1+\sqrt5}{4}
=
\cos\frac\pi5,
\]
so
\[
\arcsin\!\left(\sin\frac\pi3\cos\delta\right)
=
\frac{3\pi}{10}.
\]
Also,
\[
\frac{
\sin(\pi/3)\cos\delta
}{
\sqrt{1-\sin^2(\pi/3)\cos^2\delta}
}
=
\cot\frac\pi5.
\]
Thus (9) becomes
\[
I_3(\delta)
=
\frac{\pi}{15}
+
2\sin^2\delta\cot\frac\pi5.
\]
Substitution in (10), together with
\[
4R^2\sin^2\delta=1,
\qquad
\cot^2\frac\pi5=1+\frac2{\sqrt5},
\]
gives
\[
\mathbb E\,w_{\rm dod}(U)^2
=
\frac{3+\sqrt5}{2}
+
\frac{10}{\pi}\sqrt{1+\frac2{\sqrt5}}.
\tag{11}
\]

Finally, the tetrahedron is not centrally symmetric, so (2) is unavailable. Finch's direct spherical integration gives
\[
\mathbb E\,w_{\rm tet}(U)^2
=
\frac13\left(1+\frac{3+\sqrt3}{\pi}\right).
\tag{12}
\]
Equations (10)--(12) establish the complete table (1).

## Verification
The supplied `verify.py` reconstructs standard unit-edge coordinates for all five Platonic solids, confirms their edge normalization and circumradii, and verifies the exact algebraic identities used in the four centrally symmetric normal-cell substitutions.

It independently evaluates the one-dimensional sector integral (7) by deterministic quadrature for the cube, octahedron, dodecahedron, and icosahedron and checks it against (9). It also performs deterministic spherical quadrature of the actual support functions of all five solids and compares the resulting second moments with (1).

These finite calculations are regression checks only. The four centrally symmetric formulas are proved by the exact normal-cell integral, while the tetrahedral value is the published exact evaluation reproduced in the cited source.

## Relationship to prior work
Finch introduced explicit mean-square-width calculations for regular polyhedra, obtaining the unit-edge tetrahedron and cube values and explicitly expressing the hope that analogous computations would be made for other convex bodies.

Kabluchko, Litvak, and Zaporozhets later proved a higher-moment form of Sudakov's formula for arbitrary compact convex sets and evaluated random-projection moments for regular cubes, simplices, and crosspolytopes. Their crosspolytope result includes the regular octahedron after scaling. Their full text contains no occurrence of the dodecahedron or icosahedron.

The present classification combines those established entries with an exact normal-cell evaluation for the centrally symmetric Platonic solids. The dodecahedral formula (11) is the missing entry needed to complete the five-solid table. Targeted searches for mean-square width, second width moment, random projection length, mean caliper diameter, and the exact dodecahedral constant did not locate a prior complete table or a prior dodecahedral evaluation.

## Limitations
Only the second moment of the directional width is classified. Full width distributions and higher moments are not supplied for the dodecahedron or icosahedron.

The normal-cell formula (9) is specialized here to regular three-dimensional polyhedra with regular vertex normal cells. No claim is made that it is the most general polyhedral second-moment formula.

The tetrahedral entry is prior work, and the cube and crosspolytope framework is also prior work. The new scientific content of the complete classification is the exact completion of the Platonic table, especially the dodecahedral evaluation and the unified normal-cell derivation for all four centrally symmetric solids.

A differently indexed classical stereological calculation under terms such as mean caliper diameter or Feret diameter remains a residual originality risk.

## References
1. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671v1, 4 October 2011.
2. Z. Kabluchko, A. E. Litvak, and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479v1, 26 November 2015.
