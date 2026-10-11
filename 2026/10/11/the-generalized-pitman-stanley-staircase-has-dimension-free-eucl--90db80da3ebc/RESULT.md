# The generalized Pitman–Stanley staircase has dimension-free Euclidean inradius
## Finding
For integers
\[
n\ge1,
\qquad
m\ge2,
\]
consider the generalized Pitman–Stanley polytope
\[
\mathcal P_{n,m}
=
\operatorname{PS}_n^m(\mathbf1,\mathbf0)
\subset
\mathbb R^{n\times m}.
\]
Write
\[
s_{ij}(x)=\sum_{p=1}^i x_{pj}.
\]
The defining inequalities specialize to
\[
x_{ij}\ge0,
\]
and, for every \(1\le i\le n\),
\[
0\le s_{im}(x)\le s_{i,m-1}(x)\le\cdots\le s_{i1}(x)\le i.
\]

With the standard Euclidean metric on \(\mathbb R^{nm}\),
\[
\boxed{
r_{\mathrm{in}}(\mathcal P_{n,m})
=
r_m
=
\frac{1}{2+(m-1)\sqrt2}.
}
\]
In particular, the inradius is completely independent of the row parameter \(n\).

Define
\[
y_j=r_m\bigl(1+(m-j)\sqrt2\bigr)
\qquad
(1\le j\le m).
\]
Then
\[
y_m=r_m,\qquad
y_1=1-r_m,\qquad
y_j-y_{j+1}=r_m\sqrt2.
\]
The matrix
\[
c^{(0)}_{ij}=y_j
\]
is an incenter.

The complete incenter set is the polytope of matrices \(c=(c_{ij})\) satisfying
\[
c_{ij}\ge r_m,
\]
\[
s_{im}(c)\ge r_m\sqrt i,
\]
\[
s_{ij}(c)-s_{i,j+1}(c)\ge r_m\sqrt{2i},
\]
and
\[
s_{i1}(c)\le i-r_m\sqrt i,
\]
for every admissible \(i,j\).

Every incenter has the same first row:
\[
\boxed{
c_{1j}=y_j
\qquad
(1\le j\le m).
}
\]
Consequently,
\[
\boxed{
\dim \mathcal I_{n,m}
=
\begin{cases}
0,&n=1,\\
m(n-1),&n\ge2.
\end{cases}
}
\]

Thus the new \(m\)-column extension has a metric bottleneck entirely controlled by its first row: increasing \(n\) adds \(m\) ambient dimensions at a time without changing the largest inscribed-ball radius.

## Assumptions and scope
The polytope is the Dugan--Hegarty--Morales--Raymond generalized Pitman–Stanley polytope with top vector \(\mathbf1\), bottom vector \(\mathbf0\), and \(m\ge2\).

The metric is the ordinary Euclidean metric in the source coordinates \(x_{ij}\). The theorem is not invariant under the integral equivalence with the associated grid-flow polytope, because a general integral equivalence need not be orthogonal.

The source permits more general vectors \(\mathbf a,\mathbf b\). No radius formula is claimed here for arbitrary \(\mathbf a,\mathbf b\).

## Proof
The source defines \(\operatorname{PS}_n^m(\mathbf a,\mathbf b)\) as the nonnegative matrices whose column prefix sums form a multichain in dominance order between \(\mathbf a\) and \(\mathbf b\). Specializing to \(\mathbf a=\mathbf1\), \(\mathbf b=\mathbf0\) gives the displayed system.

For the coordinate halfspace \(x_{ij}\ge0\), the inward normal has norm \(1\), so a radius-\(r\) ball centered at \(c\) requires
\[
c_{ij}\ge r.
\]
For the upper prefix wall \(s_{i1}(x)\le i\), the normal has norm \(\sqrt i\), giving
\[
s_{i1}(c)\le i-r\sqrt i.
\]
For the lower prefix wall \(s_{im}(x)\ge0\), the same norm gives
\[
s_{im}(c)\ge r\sqrt i.
\]
Finally,
\[
s_{ij}(x)-s_{i,j+1}(x)\ge0
\]
has \(i\) coefficients \(+1\) and \(i\) coefficients \(-1\), hence normal norm \(\sqrt{2i}\), so
\[
s_{ij}(c)-s_{i,j+1}(c)\ge r\sqrt{2i}.
\]
These conditions are necessary and sufficient because they are exactly the Euclidean distance conditions for the ball to lie in every defining halfspace.

Restrict to \(i=1\). Then
\[
c_{1m}\ge r,
\qquad
c_{1j}-c_{1,j+1}\ge r\sqrt2,
\qquad
c_{11}\le1-r.
\]
Telescoping gives
\[
1-r\ge c_{11}\ge c_{1m}+(m-1)r\sqrt2\ge r+(m-1)r\sqrt2,
\]
hence
\[
r\le\frac1{2+(m-1)\sqrt2}=r_m.
\]

Now use the repeated-row center \(c^{(0)}_{ij}=y_j\). Coordinate inequalities hold because \(y_j\ge r_m\). Also
\[
s_{im}(c^{(0)})=ir_m\ge r_m\sqrt i,
\]
\[
s_{ij}(c^{(0)})-s_{i,j+1}(c^{(0)})=ir_m\sqrt2\ge r_m\sqrt{2i},
\]
and
\[
s_{i1}(c^{(0)})=i(1-r_m)\le i-r_m\sqrt i,
\]
because \(i\ge\sqrt i\). Therefore the bound is attained.

At \(r=r_m\), equality holds in the first-row telescope, so every inequality used there is itself equality. Thus
\[
c_{1m}=r_m,
\qquad
c_{1j}-c_{1,j+1}=r_m\sqrt2,
\qquad
c_{11}=1-r_m,
\]
which uniquely gives \(c_{1j}=y_j\).

For \(n=1\), the incenter is unique. For \(n\ge2\), all incenters lie in the affine subspace defined by the fixed first row, whose dimension is \(m(n-1)\). To show this upper bound is attained, choose
\[
0<\varepsilon<
\min_{2\le i\le n}
\frac{r_m(i-\sqrt i)}{i-1},
\]
set the first row equal to \(y\), and set every later row equal to \(y+\varepsilon\mathbf1\). Then every non-first-row coordinate inequality is strict, and for \(i\ge2\),
\[
ir_m+(i-1)\varepsilon>r_m\sqrt i,
\]
\[
ir_m\sqrt2>r_m\sqrt{2i},
\]
and
\[
i(1-r_m)+(i-1)\varepsilon<i-r_m\sqrt i.
\]
Hence this point is in the relative interior of the incenter set inside the fixed-first-row affine subspace. The dimension is exactly \(m(n-1)\).

## Verification
The proof is symbolic and applies to all \(n\ge1\), \(m\ge2\).

The critical source premise was checked directly in the full text: the generalized Pitman–Stanley polytope is the set of nonnegative matrices whose column prefix sums form the displayed dominance multichain.

The accompanying `verify.py` checks the radius and center construction for \(1\le n\le100\) and \(2\le m\le50\). It verifies every normalized halfspace-distance inequality, the exact first-row telescoping equality, and the positive-slack witness used for the dimension formula. These finite calculations are corroborative only.

## Relationship to prior work
Dugan, Hegarty, Morales, and Raymond introduce the generalized \(m\)-column Pitman–Stanley polytope, realize it as a grid-flow polytope, and study its vertices and faces. Their full text also highlights the all-ones top vector as a distinguished case in their enumeration results.

The same authors subsequently study volumes and lattice points of the generalized family. Those works develop enumerative and flow-polytope structure rather than Euclidean largest-inscribed-ball geometry.

The classical \(m=1\) Pitman–Stanley polytope predates this generalization. The present claim is deliberately for \(m\ge2\), so its object is the generalized family rather than the 1999 classical case.

Targeted searches used “generalized Pitman–Stanley polytope”, “\(m\)th Pitman–Stanley polytope”, “inradius”, “Chebyshev center”, “largest inscribed ball”, “flow polytope”, and “plane partition polytope”. No inspected source or published-result record supplied the radius formula, the forced first row, or the incenter-dimension formula.

## Limitations
The formula is proved only for \(\operatorname{PS}_n^m(\mathbf1,\mathbf0)\). Arbitrary top and bottom vectors introduce competing prefix scales, and the same one-row bottleneck need not control.

The result is coordinate-metric rather than invariant under the source's integral equivalence to a flow polytope.

The exact radius follows from a short first-row obstruction once the correct normalized chain distances are written down. Accordingly, an unindexed folklore observation or a general Chebyshev-center theorem for dominance-chain polytopes remains a residual originality risk.

## References
1. William T. Dugan, Maura Hegarty, Alejandro H. Morales, and Annie Raymond, *The Pitman-Stanley Polytope and Flow Polytopes*, Joint Mathematics Meetings 2022 abstract, public meeting date 2022-04-08.
2. William T. Dugan, Maura Hegarty, Alejandro H. Morales, and Annie Raymond, *Generalized Pitman-Stanley polytope: vertices and faces*, arXiv:2307.09925, first arXiv version 2023-07-19; Discrete & Computational Geometry, DOI 10.1007/s00454-024-00704-3.
