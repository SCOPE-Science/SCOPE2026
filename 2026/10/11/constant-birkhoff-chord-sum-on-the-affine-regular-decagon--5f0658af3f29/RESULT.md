# Constant Birkhoff chord-sum on the affine-regular decagon
## Finding
Put
\[
r=\frac{\sqrt5-1}{2},
\qquad
\phi=\frac{1+\sqrt5}{2},
\]
so that
\[
r\phi=1,
\qquad
r^2=1-r.
\]
Let
\[
X_{10}=(\mathbb R^2,N_{10}),
\]
where
\[
N_{10}(s,t)
=
\max\{
|s+t|,
|rs+t|,
r|t|,
r|s|,
|s+rt|
\}.
\]
For every
\[
x,y\in S_{X_{10}},
\qquad
x\perp_B y,
\]
one has the exact chord-sum identity
\[
\boxed{
N_{10}(x+y)+N_{10}(x-y)
=
\frac{3\sqrt5-1}{2}
}.
\tag{1}
\]

Therefore the orthogonal James and orthogonal Schäffer constants
\[
J_{\perp}(X)
=
\sup_{\substack{x,y\in S_X\\x\perp_B y}}
\min\{\|x+y\|,\|x-y\|\},
\]
and
\[
g_{\perp}(X)
=
\inf_{\substack{x,y\in S_X\\x\perp_B y}}
\max\{\|x+y\|,\|x-y\|\}
\]
coincide on this plane:
\[
\boxed{
J_{\perp}(X_{10})
=
g_{\perp}(X_{10})
=
\frac{3\sqrt5-1}{4}
}.
\tag{2}
\]

## Assumptions and scope
All scalars are real. Birkhoff--James orthogonality means
\[
x\perp_B y
\quad\Longleftrightarrow\quad
\|x\|\le\|x+\lambda y\|
\ \text{for every }\lambda\in\mathbb R.
\]

The unit ball of \(N_{10}\) is the affine-regular decagon with consecutive vertices
\[
(1,0),\ (0,1),\ (-1,\phi),\ (-\phi,\phi),\ (-\phi,1),
\]
and their negatives.

Two linear isometries are
\[
R(s,t)=(-t,s+\phi t)
\]
and
\[
S(s,t)=(t,s).
\]
Indeed, \(R\) cyclically permutes the ten listed vertices and \(S\) reflects them. Hence the generated dihedral group is transitive on edges and on vertices.

For a polyhedral norm, \(x\perp_B y\) exactly when some norming functional at \(x\) annihilates \(y\). Equivalently, if the active norming functionals at \(x\) are \(f_1,\ldots,f_k\), then
\[
0\in\operatorname{conv}\{f_1(y),\ldots,f_k(y)\}.
\tag{3}
\]
This follows directly by applying the one-variable convex minimum condition to
\[
\lambda\longmapsto N_{10}(x+\lambda y).
\]

## Proof
By the dihedral symmetry, a unit vector \(x\) is reduced to one of two cases: an interior point of the edge joining \((1,0)\) to \((0,1)\), or the vertex \((1,0)\).

First suppose
\[
x=(a,1-a),
\qquad
0<a<1.
\]
The unique norming functional is
\[
f_0(s,t)=s+t.
\]
Condition (3) therefore gives
\[
f_0(y)=0.
\]
On the line \(s+t=0\),
\[
N_{10}(s,-s)=r|s|,
\]
so, after replacing \(y\) by \(-y\) if necessary,
\[
y=(\phi,-\phi).
\tag{4}
\]

A direct substitution into the five defining functionals gives
\[
N_{10}(x+y)=2r+r^2a.
\tag{5}
\]
For completeness, the five absolute values at \(x+y=(a+\phi,-a-r)\) are
\[
1,\quad
r^2(1-a),\quad
ra+r^2,\quad
1+ra,\quad
2r+r^2a.
\]
The last is largest because
\[
(2r+r^2a)-(1+ra)
=
(2r-1)(1-a)\ge0,
\]
and the remaining comparisons are immediate from
\[
0\le a\le1
\quad\text{and}\quad
r^2=1-r.
\]

Reflection by \(S\) gives
\[
N_{10}(x-y)
=
2r+r^2(1-a)
=
\phi-r^2a.
\tag{6}
\]
Hence
\[
N_{10}(x+y)+N_{10}(x-y)
=
2r+\phi.
\tag{7}
\]

It remains to treat a vertex. Let
\[
x=(1,0).
\]
The active norming functionals are
\[
f_0(s,t)=s+t,
\qquad
f_4(s,t)=s+rt.
\]
Thus (3) is equivalent to
\[
(u+v)(u+rv)\le0
\tag{8}
\]
for \(y=(u,v)\in S_{X_{10}}\).

After replacing \(y\) by \(-y\), condition (8) selects exactly the boundary edge
\[
y=(1+r\theta,-\phi),
\qquad
0\le\theta\le1.
\tag{9}
\]
Indeed, the two boundary rays of the cone in (8) meet the unit sphere at
\[
(1,-\phi)
\quad\text{and}\quad
(\phi,-\phi),
\]
which are adjacent vertices of the decagon.

Direct evaluation now gives
\[
N_{10}(x+y)=2r+r^2\theta
\tag{10}
\]
and
\[
N_{10}(x-y)=\phi-r^2\theta.
\tag{11}
\]
Thus the sum is again
\[
2r+\phi.
\]
Since
\[
2r+\phi
=
\frac{3\sqrt5-1}{2},
\]
equation (1) follows for every unit Birkhoff--James pair.

Set
\[
c=\frac{3\sqrt5-1}{4}.
\]
Equation (1) implies, for every admissible pair,
\[
\min\{N_{10}(x+y),N_{10}(x-y)\}\le c
\]
and
\[
\max\{N_{10}(x+y),N_{10}(x-y)\}\ge c.
\]
Therefore
\[
J_{\perp}(X_{10})\le c
\quad\text{and}\quad
g_{\perp}(X_{10})\ge c.
\]

Finally take
\[
x=\left(\frac12,\frac12\right),
\qquad
y=(\phi,-\phi).
\]
Both are unit vectors, the unique norming functional of \(x\) is \(s+t\), and it annihilates \(y\). Hence
\[
x\perp_B y.
\]
Equations (5) and (6), with \(a=1/2\), give
\[
N_{10}(x+y)
=
N_{10}(x-y)
=
c.
\]
This proves both equalities in (2).

## Verification
The bundled `verify.py` works in the exact quadratic field
\[
\mathbb Q(\sqrt5).
\]
It verifies the identities
\[
r\phi=1,
\qquad
r^2=1-r,
\]
checks the ten vertices and the two dihedral generators, verifies the two exact Birkhoff branches, and confirms the chord formulas (5), (6), (10), and (11) on exact rational parameter grids.

The finite grid is a reproducibility check only. Exhaustiveness comes from the analytic dichotomy between edge-interior and vertex points and the exact norming-functional criterion (3).

## Relationship to prior work
Baronti and Papini introduced \(J_{\perp}\) and \(g_{\perp}\) for Birkhoff--James orthogonal unit pairs. Their 2022 paper proves general inequalities and computes several two-dimensional examples, including two hexagonal norms, the regular octagon, and a mixed Euclidean--taxicab plane. The inspected examples section contains no decagonal computation and no constant-chord-sum theorem.

A public exact record for the affine-regular decagon gives the same number
\[
\frac{3\sqrt5-1}{4}
\]
as a Banach--Mazur distance from a parallelogram. That is a different affine-containment invariant and does not imply (1) or (2).

Other checked decagonal records concern a Birkhoff geometric-mean objective, a Birkhoff cosine objective, a Massera--Schäffer Birkhoff quantity, and a generalized James profile over all unit pairs. None of those statements fixes the sum
\[
N_{10}(x+y)+N_{10}(x-y)
\]
for every Birkhoff--James pair, and none implies both extremal identities in (2).

## Limitations
The constant chord-sum identity is proved here only for the affine-regular decagon. It is not asserted for arbitrary regular polygons or arbitrary Radon planes.

The result classifies the two chord norms through two one-parameter Birkhoff branches, but it does not classify all ordered maximizing pairs beyond dihedral symmetry and sign.

The literature search cannot prove absolute novelty. An equivalent decagonal identity could exist under a different affine normalization or without the \(J_{\perp},g_{\perp}\) notation.

## References
1. M. Baronti and P. L. Papini, “Parameters in Banach spaces and orthogonality,” *Constructive Mathematical Analysis* 5 (2022), 37--45, doi:10.33205/cma.1067323. Published online 9 March 2022.
