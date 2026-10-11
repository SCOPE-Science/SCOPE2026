# Orthogonal James–Schäffer collapse on regular \(8m\)-gonal Banach planes
## Finding
For every integer
\[
m\ge1,
\]
let \(X_{8m}\) be the real Banach plane whose unit ball is the Euclidean regular \(8m\)-gon. Define
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
\max\{\|x+y\|,\|x-y\|\}.
\]
Then
\[
\boxed{
J_{\perp}(X_{8m})
=
g_{\perp}(X_{8m})
=
\sqrt2
}.
\tag{1}
\]

In fact, every unit Birkhoff--James orthogonal pair satisfies the pointwise separation
\[
\boxed{
\min\{\|x+y\|,\|x-y\|\}
\le
\sqrt2
\le
\max\{\|x+y\|,\|x-y\|\}.
}
\tag{2}
\]
Both inequalities are simultaneous equalities for quarter-turn pairs at every edge midpoint and every vertex.

## Assumptions and scope
All scalars are real.

Put
\[
N=8m,
\qquad
\alpha=\frac{\pi}{N},
\qquad
c=\cos\alpha,
\qquad
s=\sin\alpha.
\]
Use the Euclidean-circle normalization in which the unit-ball vertices are
\[
v_k=
\left(
\cos((2k+1)\alpha),
\sin((2k+1)\alpha)
\right).
\]
The reference edge is
\[
E_0=[(c,-s),(c,s)].
\]
Its unique norming functional at interior points is
\[
f_0(u,v)=\frac{u}{c}.
\tag{3}
\]
The regular \(8m\)-gon is invariant under quarter-turn rotation
\[
R(u,v)=(-v,u).
\]

A unit vector \(x\) is Birkhoff--James orthogonal to \(y\) exactly when some norming functional of \(x\) vanishes on \(y\).

## Proof
By dihedral symmetry it suffices to place \(x\) on the closed reference edge.

First suppose that \(x\) is an interior edge point:
\[
x=(c,t),
\qquad
-s<t<s.
\tag{4}
\]
Then \(J(x)=\{f_0\}\), so \(x\perp_B y\) forces
\[
y=\pm(0,c),
\tag{5}
\]
because the vertical direction is a facet-normal direction when \(N=8m\).

Take \(y=(0,c)\). The vectors
\[
x+y=(c,t+c),
\qquad
x-y=(c,t-c)
\]
remain in the two facet cones centered at the directions
\[
\frac{\pi}{4}
\quad\text{and}\quad
-\frac{\pi}{4},
\]
respectively. These are facet-normal directions because
\[
\frac{\pi}{4}=2m\alpha.
\]
Hence the active norming functionals have normals \((1,1)/\sqrt2\) and \((1,-1)/\sqrt2\), and
\[
\|x+y\|
=
\sqrt2+\frac{t}{\sqrt2\,c},
\]
\[
\|x-y\|
=
\sqrt2-\frac{t}{\sqrt2\,c}.
\tag{6}
\]
Thus (2) holds for every smooth \(x\), with equality in both terms at the edge midpoint \(t=0\).

Now let \(x\) be the endpoint vertex
\[
x=(c,s).
\tag{7}
\]
The norming set is the segment joining the two adjacent facet functionals whose Euclidean normal angles are
\[
0
\quad\text{and}\quad
2\alpha.
\]
Therefore \(x\perp_B y\) exactly when, up to sign, the direction of \(y\) lies between
\[
\frac{\pi}{2}
\quad\text{and}\quad
\frac{\pi}{2}+2\alpha.
\tag{8}
\]
The corresponding unit-sphere arc consists of two half-edges meeting at
\[
Rx=(-s,c).
\]

On the first half-edge write
\[
y=(-r,c),
\qquad
0\le r\le s.
\tag{9}
\]
Then
\[
x+y=(c-r,c+s),
\qquad
x-y=(c+r,s-c).
\]
Their directions stay inside the facet cones centered at
\[
\frac{\pi}{4}
\quad\text{and}\quad
-\frac{\pi}{4},
\]
so
\[
\|x+y\|
=
\sqrt2+\frac{s-r}{\sqrt2\,c},
\]
\[
\|x-y\|
=
\sqrt2-\frac{s-r}{\sqrt2\,c}.
\tag{10}
\]
Hence (2) holds on this half-edge. At \(r=s\), one has \(y=Rx\) and both norms equal \(\sqrt2\).

The second half-edge in (8) is the reflection of the first across the line through \(Rx\). That reflection is a norm isometry fixing \(x\) up to the adjacent dihedral representative and merely interchanges the two chord formulas. Thus (2) holds there as well. Central symmetry handles the opposite Birkhoff sector.

This exhausts every unit Birkhoff--James orthogonal pair, proving (2).

Taking suprema of the left side of (2) gives
\[
J_{\perp}(X_{8m})\le\sqrt2,
\]
while a quarter-turn vertex pair gives equality. Taking infima of the right side gives
\[
g_{\perp}(X_{8m})\ge\sqrt2,
\]
while a quarter-turn edge-midpoint pair gives equality. Hence (1) follows.

## Verification
The bundled `verify.py` reconstructs every regular \(8m\)-gon for
\[
1\le m\le12,
\]
checks the reference-edge support geometry, samples every smooth branch and both vertex Birkhoff sectors, and verifies that the two chord norms straddle \(\sqrt2\). It also checks the quarter-turn equality pairs at edge midpoints and vertices.

The checker is supplementary. Exhaustiveness is provided by the analytic support-functional classification above: after dihedral reduction, a boundary point is either a smooth edge point or a vertex, and those two cases are completely resolved by (5) and (8).

## Relationship to prior work
Baronti and Papini introduced \(J_{\perp}\) and \(g_{\perp}\) as Birkhoff-orthogonal versions of the James and Schäffer constants. Their paper computes several examples, including the regular octagonal plane, for which they obtain
\[
J_{\perp}=g_{\perp}=\sqrt2.
\]
The inspected full text does not extend that octagonal observation to all regular polygons whose number of sides is divisible by eight.

The present result shows that the octagon is the first member of an infinite rigidity class:
\[
X_8,X_{16},X_{24},\ldots
\]
all have the same orthogonal James and Schäffer values as a Hilbert plane. The stronger pointwise statement (2) explains why: every Birkhoff-orthogonal chord pair crosses the common threshold \(\sqrt2\).

Previously recorded exact results for the regular decagon concern a different residue class and give a non-Hilbert common value. Exact ordinary James constants for regular \(8k+4\)-gons also concern the complementary fourfold residue class and do not imply the \(8m\)-gonal Birkhoff-orthogonal collapse proved here.

## Limitations
The theorem treats the residue class
\[
N\equiv0\pmod8.
\]
It does not claim a complete formula for \(J_{\perp}\) and \(g_{\perp}\) on every regular even polygon.

The Hilbert-valued equality in (1) does not imply that \(X_{8m}\) is Hilbert; these spaces are polyhedral for every finite \(m\).

Bibliographic and semantic-index searches cannot establish absolute novelty. An equivalent infinite-family statement could exist under different notation for orthogonal James and Schäffer constants.

## References
1. M. Baronti and P. L. Papini, “Parameters in Banach spaces and orthogonality,” *Constructive Mathematical Analysis* 5 (2022), 37--45, doi:10.33205/cma.1067323. Published online 9 March 2022. Mathematics Subject Classification: 46B20, 46B99, 46C15.
