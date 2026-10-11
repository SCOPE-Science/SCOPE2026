# Exact centered-triangle side interval of the regular decagonal Banach plane
## Finding
Let \(X_{10}\) be the real Banach plane whose unit ball is an affine regular decagon. For the Fu--Liu--Li constants
\[
J_L(X)=
\inf\left\{
\|u-v\|:
u,v,w\in S_X,\ u+v+w=0
\right\}
\]
and
\[
Y_J(X)=
\sup\left\{
\|u-v\|:
u,v,w\in S_X,\ u+v+w=0
\right\},
\]
the exact values are
\[
J_L(X_{10})=\frac{9-\sqrt5}{4},
\qquad
Y_J(X_{10})=4-\sqrt5.
\]
In the later notation used for variations of the James and Schäffer constants, these are
\[
g_1(X_{10})=\frac{9-\sqrt5}{4},
\qquad
J_1(X_{10})=4-\sqrt5.
\]

## Assumptions and scope
All scalars are real. Affine-regular decagons are linearly equivalent, so it is enough to use one convenient affine presentation.

Put
\[
\varphi=\frac{1+\sqrt5}{2},
\qquad
r=\frac{\sqrt5-1}{2}.
\]
Take the unit ball to be the convex hull of
\[
(1,0),\ (0,1),\ (-1,\varphi),\ (-\varphi,\varphi),\ (-\varphi,1),
\]
and their negatives. Its ten signed supporting functionals, in cyclic order, are
\[
\begin{aligned}
f_0(s,t)&=s+t,&
f_1(s,t)&=rs+t,&
f_2(s,t)&=rt,&
f_3(s,t)&=-rs,&
f_4(s,t)&=-s-rt,\\
f_5(s,t)&=-s-t,&
f_6(s,t)&=-rs-t,&
f_7(s,t)&=-rt,&
f_8(s,t)&=rs,&
f_9(s,t)&=s+rt.
\end{aligned}
\]
Thus
\[
N_{10}(z)=\max_{0\le j<10}f_j(z).
\]

If \(u,v,w\in S_{X_{10}}\) and \(u+v+w=0\), put
\[
x=u,\qquad y=-v.
\]
Then
\[
N_{10}(x)=N_{10}(y)=N_{10}(x-y)=1
\]
and
\[
\|u-v\|=N_{10}(x+y).
\]
Conversely every such pair \(x,y\) produces a centered unit triple. Hence the two constants are respectively the minimum and maximum of \(N_{10}(x+y)\) over
\[
N_{10}(x)=N_{10}(y)=N_{10}(x-y)=1.
\]

## Proof
Consider the compact polytope
\[
P=
\left\{
(x,y)\in\mathbb R^4:
f_i(x)\le1,\ f_i(y)\le1,\ f_i(x-y)\le1
\text{ for }0\le i<10
\right\}.
\]
Every admissible pair has at least one tight facet in each of the three unit-sphere conditions. It therefore belongs to at least one face
\[
F_{ijk}=
\left\{
(x,y)\in P:
f_i(x)=f_j(y)=f_k(x-y)=1
\right\},
\qquad
0\le i,j,k<10.
\]

The bundled exact calculation works in the quadratic field \(\mathbb Q(\sqrt5)\) and checks all
\[
10^3=1000
\]
facet triples. Exactly \(60\) produce nonempty faces. Every one of those faces is a line segment.

On a fixed segment, each quantity
\[
f_m(x+y)
\]
is affine in the segment parameter, while
\[
N_{10}(x+y)=\max_{0\le m<10} f_m(x+y)
\]
is the upper envelope of ten affine functions. Consequently its maximum on a segment occurs at an endpoint. Its minimum occurs at an endpoint or at an intersection of two of the ten affine functions. The checker evaluates every such candidate exactly, so this finite calculation is exhaustive for the full continuum of admissible pairs.

The global minimum is
\[
\frac{9-\sqrt5}{4}.
\]
It is attained, for example, at
\[
x=
\left(
\frac{1+\sqrt5}{4},
\frac{3-\sqrt5}{4}
\right),
\qquad
y=
\left(
-\frac{1+\sqrt5}{4},
\frac32
\right).
\]
Exact substitution gives
\[
N_{10}(x)=N_{10}(y)=N_{10}(x-y)=1
\]
and
\[
N_{10}(x+y)=\frac{9-\sqrt5}{4}.
\]

The global maximum is
\[
4-\sqrt5.
\]
It is attained at
\[
x=(1,0),
\qquad
y=
\left(
\frac{1-\sqrt5}{2},
\frac{5-\sqrt5}{2}
\right),
\]
for which
\[
N_{10}(x)=N_{10}(y)=N_{10}(x-y)=1
\]
and
\[
N_{10}(x+y)=4-\sqrt5.
\]
This proves both displayed constants.

## Verification
The bundled `verify.py` is a standalone exact-arithmetic certificate. It implements \(\mathbb Q(\sqrt5)\) using rational pairs, reconstructs all thirty inequalities of \(P\), solves every one of the \(1000\) tight-facet systems, and computes the exact feasible interval for each consistent affine line.

For each of the \(60\) nonempty faces, it evaluates all segment endpoints and all pairwise intersections of the ten affine output-facet functions. It verifies that the least and greatest values over all faces are exactly
\[
\frac{9-\sqrt5}{4}
\quad\text{and}\quad
4-\sqrt5,
\]
and separately checks both explicit attaining pairs. No floating-point sampling is used to certify either extremum.

## Relationship to prior work
Fu, Liu and Li introduced \(J_L(X)\) and \(Y_J(X)\) as centered unit-triangle side-length extrema, established their general bounds, and computed Hilbert and several standard sequence-space examples. Their publicly available full text contains no regular-decagon or regular-polygon computation.

Martini, Papini and Wu later studied the same pair under the notation \(g_1(X)\) and \(J_1(X)\), gave new characterizations, and related them to classical James and Schäffer constants. The accessible bibliographic record and abstract do not state a regular-decagon value; full text was not publicly retrievable in the present literature check, so an unlocated equivalent computation in that paper remains a residual risk.

The closest public exact result on the same regular decagon concerns its Banach--Mazur distance to a parallelogram, not centered-triangle side lengths. Results on true equilateral-triangle perimeters use a different constraint and do not imply these two extrema.

## Limitations
The result treats one canonical affine class, the regular decagonal plane. It does not give a formula for every regular \(2n\)-gonal norm or classify spaces with prescribed \(J_L\) or \(Y_J\).

Bibliographic and research-index searches cannot establish absolute uniqueness. In particular, the inaccessible full text of the 2024 Martini--Papini--Wu paper leaves a specific residual risk of an equivalent decagonal calculation under the \(g_1,J_1\) notation; no such statement appears in the accessible abstract, citation snippets, defining 2021 full text, targeted web searches, public research index, or the current local ledger.

## References
1. Y. Fu, Q. Liu and Y. Li, “New Geometric Constants in Banach Spaces Related to the Inscribed Equilateral Triangles of Unit Balls,” Symmetry 13 (2021), 951, doi:10.3390/sym13060951. Published 27 May 2021.
2. H. Martini, P. L. Papini and S. Wu, “Variations of the James and Schäffer constants in Banach spaces,” Annals of Functional Analysis 15 (2024), article 1, doi:10.1007/s43034-023-00308-7.
3. Q. Ni, Q. Liu, Y. Zhou and J. Xia, “3-variable James type constants in Banach spaces,” public preprint, March 2024; Mathematics Subject Classification 46B20, 46C15.
