# Exact three-variable James constant of the regular octagonal Banach plane
## Finding
Let
\[
X_8=(\mathbb R^2,N_8),
\qquad
N_8(s,t)=\max\left\{|s|,|t|,\frac{|s|+|t|}{\sqrt2}\right\}.
\]
For the Ni--Liu--Zhou--Xia three-variable James type constant
\[
J_T(X)
=
\sup_{x,y,z\in S_X}
\min\{\|x-y\|,\|y-z\|,\|z-x\|\},
\]
one has
\[
\boxed{
J_T(X_8)=1+\frac1{\sqrt2}
}.
\]

Equality is attained by the unit vectors
\[
x=\left(\frac1{\sqrt2},\frac1{\sqrt2}\right),
\qquad
y=\left(\frac{\sqrt2-1}{2},-1\right),
\qquad
z=\left(-1,\frac{\sqrt2-1}{2}\right),
\]
for which all three pairwise distances equal
\[
1+\frac1{\sqrt2}.
\]

Consequently,
\[
J_T(X_8)<\sqrt3.
\]
Thus the stated universal lower bound \(J_T(X)\ge\sqrt3\) in the motivating preprint does not hold for arbitrary real Banach spaces. The proof of that lower bound there invokes a Dvoretzky-type almost-Euclidean two-dimensional subspace argument, which applies in the relevant infinite-dimensional regime but does not furnish such a subspace inside every fixed two-dimensional normed space.

## Assumptions and scope
All spaces and scalars are real. Put
\[
a=\sqrt2-1,
\qquad
L=1+\frac1{\sqrt2}.
\]
The unit ball of \(X_8\) is the regular octagon with vertices, in cyclic order,
\[
\begin{aligned}
v_0&=(1,a),&v_1&=(a,1),&v_2&=(-a,1),&v_3&=(-1,a),\\
v_4&=(-1,-a),&v_5&=(-a,-1),&v_6&=(a,-1),&v_7&=(1,-a).
\end{aligned}
\]
Parameterize the unit sphere by the piecewise-affine map
\[
\gamma(k+u)=(1-u)v_k+u v_{k+1},
\qquad
k\in\mathbb Z/8\mathbb Z,
\quad
0\le u\le1,
\]
and extend it with period \(8\).

For a cyclic gap \(g\ge0\), define
\[
D(s,g)=N_8\bigl(\gamma(s+g)-\gamma(s)\bigr).
\]
A quarter-turn of the octagon shifts the parameter by \(2\), so \(D(s,g)\) is periodic in \(s\) with period \(2\), and an edge-to-edge rotation reduces the phase analysis to \(s\bmod1\).

The result concerns the unrestricted three-point maximin distance on the unit sphere. It is different from centered-triple or equilateral-triangle constants, which impose additional algebraic constraints on the three points.

## Proof
We prove first that no three unit points can have all pairwise distances larger than \(L\).

### 1. Every cyclic gap at most \(5/2\) has distance at most \(L\)
By rotational symmetry take
\[
s=u,
\qquad
0\le u\le1.
\]
On the region where
\[
k\le u+g\le k+1,
\]
the vector
\[
\gamma(u+g)-\gamma(u)
\]
is affine in \((u,g)\). Since \(N_8\) is convex, the maximum of \(D(u,g)\) on each polygonal cell is attained at a cell vertex.

For
\[
0\le g\le\frac52,
\]
the four possible cells and their vertices are
\[
\begin{array}{c|l}
k&\text{cell vertices }(u,g)\\ \hline
0&(0,0),(0,1),(1,0),\\
1&(0,1),(0,2),(1,0),(1,1),\\
2&(0,2),(0,5/2),(1/2,5/2),(1,1),(1,2),\\
3&(1/2,5/2),(1,2),(1,5/2).
\end{array}
\]
Exact evaluation gives the respective cell maxima
\[
2(\sqrt2-1),
\qquad
\sqrt2,
\qquad
L,
\qquad
L.
\]
Therefore
\[
D(s,g)\le L
\qquad
\text{whenever }0\le g\le\frac52.
\tag{1}
\]

### 2. The strict branch for gaps between \(5/2\) and \(3\)
Write
\[
g=\frac52+h,
\qquad
0<h<\frac12,
\]
and let
\[
u=s\bmod1,
\qquad
0\le u<1.
\]
A direct edge calculation gives the following exact criterion:
\[
D(s,g)>L
\quad\Longleftrightarrow\quad
\begin{cases}
0\le u<1/2, &\text{always},\\
1/2<u<1, &u+h>1.
\end{cases}
\tag{2}
\]
At \(u=1/2\) one has \(D(s,g)\le L\).

For completeness, if
\[
u+h<\frac12,
\]
the second endpoint remains on the next diagonal edge and one coordinate of the difference equals
\[
L+(2-\sqrt2)h>L.
\]
If
\[
u+h\ge\frac12,
\]
the second endpoint is on the following vertical edge. Writing the positive coordinate magnitudes as
\[
p=2-(2-\sqrt2)u
\]
and
\[
q=2(\sqrt2-1)h+\sqrt2\,u-(\sqrt2-1),
\]
we obtain: for \(u<1/2\), \(p>L\); for \(u=1/2\), the norm is at most \(L\); and for \(u>1/2\), the coordinate branches are below \(L\), while
\[
(p+q)-\sqrt2 L
=
2(\sqrt2-1)(u+h-1).
\]
This proves (2).

### 3. Three strict gaps are impossible
Suppose, for contradiction, that three points on the unit sphere have all pairwise distances greater than \(L\). Choose cyclic parameter lifts
\[
s_1<s_2<s_3<s_1+8
\]
and define the three cyclic gaps
\[
g_1=s_2-s_1,
\qquad
g_2=s_3-s_2,
\qquad
g_3=s_1+8-s_3.
\]
Then
\[
g_1+g_2+g_3=8.
\]
By (1), every \(g_i\) must exceed \(5/2\). Hence
\[
g_i=\frac52+h_i,
\qquad
0<h_i<\frac12,
\qquad
h_1+h_2+h_3=\frac12.
\tag{3}
\]
Let
\[
u_i=s_i\bmod1.
\]
The phase update is
\[
u_{i+1}\equiv u_i+\frac12+h_i\pmod1.
\tag{4}
\]
By (2), none of the \(u_i\) can equal \(1/2\).

If some \(u_i>1/2\), condition (2) forces
\[
u_i+h_i>1,
\]
so the wrapped value in (4) satisfies
\[
u_{i+1}=u_i+h_i-\frac12>\frac12.
\]
Thus all three phases are above \(1/2\), and all three updates use
\[
u_{i+1}=u_i+h_i-\frac12.
\]
Summing cyclically gives
\[
0=h_1+h_2+h_3-\frac32=-1,
\]
a contradiction.

If no \(u_i>1/2\), then all three lie below \(1/2\). To keep the next phase below \(1/2\), (4) must again wrap at every step, so the same summation gives the same contradiction. Therefore at least one pairwise distance is at most \(L\), proving
\[
J_T(X_8)\le L.
\tag{5}
\]

### 4. Sharpness
Take
\[
x=\left(\frac1{\sqrt2},\frac1{\sqrt2}\right),
\qquad
y=\left(\frac a2,-1\right),
\qquad
z=\left(-1,\frac a2\right).
\]
Each vector has \(N_8\)-norm \(1\). Their differences are
\[
x-y=\left(\frac12,L\right),
\qquad
x-z=\left(L,\frac12\right),
\]
and
\[
y-z=\left(1+\frac a2,-1-\frac a2\right).
\]
Consequently,
\[
N_8(x-y)=N_8(x-z)=N_8(y-z)=L.
\]
Together with (5),
\[
J_T(X_8)=1+\frac1{\sqrt2}.
\]
Finally,
\[
\left(1+\frac1{\sqrt2}\right)^2
=
\frac32+\sqrt2
<3,
\]
so \(J_T(X_8)<\sqrt3\).

## Verification
The proof is analytic and finite. Its upper bound uses only a four-cell convexity check, the explicit strict-gap criterion (2), and the cyclic phase contradiction.

The bundled `verify.py` works in the exact quadratic field \(\mathbb Q(\sqrt2)\). It verifies the eight vertices, the sharp equilateral triple, every vertex evaluation in the four convexity cells, and the algebraic values of the cell maxima. It also tests the strict-gap criterion on an exact rational grid of phases and gap parameters and checks a dense rational family of gaps up to \(5/2\).

The grid checks are reproducibility aids only. The continuum upper bound follows from convexity on the four cells and the symbolic phase calculation in the proof.

## Relationship to prior work
Ni, Liu, Zhou and Xia introduced the three-variable James type constant \(J_T(X)\) as the largest possible minimum pairwise distance among three unit vectors. Their motivating preprint states
\[
\sqrt3\le J_T(X)\le2
\]
for a Banach space and derives the lower estimate through a Dvoretzky-type almost-Euclidean two-dimensional subspace argument. That mechanism is available in infinite-dimensional settings but not in an arbitrary fixed Banach plane. The regular octagon above gives an explicit two-dimensional obstruction.

The same source proves
\[
J_T(H)=\sqrt3
\]
for Hilbert spaces and computes an affine hexagonal example with value \(2\). Targeted full-text inspection found no regular-octagon computation.

Public research-index searches were made for the exact invariant, three-point packing aliases, the regular octagon, the radical value \(1+1/\sqrt2\), and the claimed \(\sqrt3\) lower bound. The closest indexed exact result computes \(J_T\) on real \(\ell_4\) in dimension at least three; it does not imply a two-dimensional regular-polygon value. Other close octagonal records concern different invariants such as \(T_G\), \(G_L\), the Ptolemy constant, and parameterized von Neumann--Jordan constants.

The result is also not implied by equilateral-triangle perimeter formulas for regular polygons. Those impose an equilateral and often origin-containing configuration, whereas \(J_T\) is a maximin problem over all triples on the unit sphere; proving the upper bound requires excluding every nonequilateral triple with larger minimum separation.

## Limitations
The theorem is specific to the regular octagonal Banach plane. It does not compute \(J_T\) for every regular polygon or classify all maximizing triples.

The source comparison concerns the public March 2024 preprint version inspected here. A later revision could alter the scope of its lower-bound statement.

Bibliographic and semantic searches cannot establish absolute novelty. Equivalent results may be phrased as a three-point packing radius on a Minkowski unit circle rather than under the notation \(J_T\).

## References
1. Q. Ni, Q. Liu, Y. Zhou and J. Xia, “3-variable James type constants in Banach spaces,” public full-text preprint, uploaded 24 March 2024, ResearchGate record 379237890. Mathematics Subject Classification: 46B20, 46C15.
