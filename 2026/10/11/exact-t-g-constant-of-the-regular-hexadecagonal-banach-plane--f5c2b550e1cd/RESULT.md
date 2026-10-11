# Exact \(T_G\) constant of the regular hexadecagonal Banach plane
## Finding
Let \(X_{16}\) be the real Banach plane whose closed unit ball is the Euclidean regular hexadecagon with vertices
\[
v_k=
\left(
\cos\frac{k\pi}{8},
\sin\frac{k\pi}{8}
\right),
\qquad
0\le k<16.
\]
Put
\[
T_{16}
=
1-\sqrt2+2\sqrt{4-2\sqrt2}.
\]
Then every
\[
x,y\in S_{X_{16}},
\qquad
\|x-y\|=1,
\]
satisfies the simultaneous sharp bounds
\[
\boxed{
\|x+y\|\le T_{16},
\qquad
\|2x-y\|\le T_{16}.
}
\tag{1}
\]
Both inequalities can be equalities for the same pair. Therefore the Ahmad--Xie--Li constant
\[
T_G(X)
=
\sup_{\substack{x,y\in S_X\\\|x-y\|=1}}
\sqrt{\|x+y\|\,\|2x-y\|}
\]
has the exact value
\[
\boxed{
T_G(X_{16})
=
1-\sqrt2+2\sqrt{4-2\sqrt2}.
}
\tag{2}
\]

Numerically,
\[
T_G(X_{16})
=
1.750570838211692\ldots.
\]

## Assumptions and scope
All scalars are real. The norm is the Minkowski functional of the displayed regular hexadecagon. Equivalently,
\[
\|(s,t)\|
=
\max_{0\le j<8}
\frac{
\left|
s\cos\frac{(2j+1)\pi}{16}
+
t\sin\frac{(2j+1)\pi}{16}
\right|
}{
\cos(\pi/16)
}.
\tag{3}
\]

The dihedral symmetry of the unit ball is used only to reduce one boundary point to the reference edge
\[
[v_0,v_1].
\]
No Euclidean rotation is asserted to be a norm isometry unless it is a multiple of \(\pi/8\).

## Proof
Write
\[
z=x-y.
\]
The admissibility condition is exactly
\[
x,y,z\in S_{X_{16}},
\qquad
x=y+z.
\tag{4}
\]
The two factors in \(T_G\) are
\[
\|x+y\|
\quad\text{and}\quad
\|x+z\|.
\tag{5}
\]

By a dihedral isometry, write
\[
x=v_0+a(v_1-v_0),
\qquad
0\le a\le1.
\tag{6}
\]
Let
\[
s=\sqrt2,\qquad
b=\sqrt{2-\sqrt2},\qquad
c=\sqrt{2+\sqrt2},
\]
and define
\[
q
=
2-\sqrt2-\frac32\sqrt{2-\sqrt2}
+\frac12\sqrt{2+\sqrt2},
\tag{7}
\]
\[
\kappa_1
=
-2-2\sqrt{2-\sqrt2}
+2\sqrt{2+\sqrt2},
\tag{8}
\]
and
\[
\kappa_2
=
-\sqrt{2+\sqrt2}
-\sqrt{2-\sqrt2}
+2\sqrt2.
\tag{9}
\]
Direct squaring gives
\[
0<q<\frac12,
\qquad
\kappa_1>0,
\qquad
\kappa_2>0.
\tag{10}
\]

We now solve (4) edge by edge. Let \(E_j=[v_j,v_{j+1}]\), with indices modulo \(16\). For a nondegenerate interval of \(a\), solving
\[
y\in E_j,\qquad z\in E_k,\qquad y+z=x
\tag{11}
\]
over all \(16^2\) ordered edge pairs gives exactly the following six branches:
\[
(E_2,E_{13}),\ (E_3,E_{13}),\ (E_3,E_{14})
\]
and the three branches obtained by exchanging \(y\) and \(z\). Their \(a\)-ranges are respectively
\[
[0,q],\qquad
[q,1-q],\qquad
[1-q,1].
\tag{12}
\]
Parallel edge pairs produce only isolated endpoint configurations already contained in these branches.

Substituting the three branches into (3) gives the complete chord table:
\[
\begin{array}{c|c|c}
a\text{-range}&\|x+y\|&\|x+z\|\\
\hline
[0,q]&T_{16}&T_{16}-\kappa_1 a\\[2mm]
[q,1-q]&T_{16}-\kappa_2(a-q)&T_{16}-\kappa_2(1-q-a)\\[2mm]
[1-q,1]&T_{16}-\kappa_1(1-a)&T_{16}.
\end{array}
\tag{13}
\]
Exchanging \(y\) and \(z\) exchanges the last two columns. The endpoint compatibility identity is
\[
\kappa_1q
=
\kappa_2(1-2q).
\tag{14}
\]
Because both \(\kappa_1\) and \(\kappa_2\) are positive, every entry in the last two columns of (13) is at most \(T_{16}\). This proves (1).

It remains to show simultaneous equality. Let
\[
x=(1,0)
\]
and
\[
y=
\left(
\frac12,h
\right),
\qquad
h=
\frac{
\cos(\pi/16)-\tfrac12\sin(3\pi/16)
}{
\cos(3\pi/16)
}.
\tag{15}
\]
Then \(y\) lies on \(E_2\), while
\[
x-y=
\left(
\frac12,-h
\right)
\]
lies on \(E_{13}\). Thus
\[
\|x\|=\|y\|=\|x-y\|=1.
\]
This is the \(a=0\) endpoint of the first branch, so (13) gives
\[
\|x+y\|
=
\|2x-y\|
=
T_{16}.
\tag{16}
\]
Taking the geometric mean proves (2).

## Verification
The bundled `verify.py` reconstructs the sixteen vertices and eight facet functionals and replays the edge equations. It solves every ordered pair of edge equations for the reference edge, verifies that exactly the six nondegenerate branches in (12) occur, checks their endpoint values against the exact algebraic number \(q\), and verifies the three formulas in (13) together with the equality pair (15).

The finite edge enumeration is exhaustive because every point of the polygonal unit sphere lies on at least one of the sixteen closed edges. The branch calculation proves an identity on each feasible interval; no sampled grid is used as a substitute for the continuum argument.

## Relationship to prior work
Ahmad, Xie and Li introduced \(T_G\) and proved general bounds and relationships with other geometric constants. Their \(\ell_p\) example gives upper estimates rather than exact values, and their Hilbert-space theorem gives the value \(\sqrt3\). The inspected paper contains no regular-hexadecagon computation.

A published exact record computes \(T_G\) for the regular octagonal plane as \(2\sqrt2-1\). That result concerns a different unit ball and does not imply (1).

Another published record proves that every origin-containing inscribed equilateral triangle in every regular \(4n\)-gonal norm has one common perimeter. For a triple arising from (4), that theorem constrains the sum of all three pairwise side lengths. It does not bound each of the two particular factors in (5), and therefore does not imply the simultaneous envelope (1) or the geometric-mean optimum (2).

Targeted searches for \(T_G\), regular-hexadecagon aliases, the exact radical in (2), equilateral-triangle formulations, and the equivalent two-factor envelope found no covering statement.

## Limitations
The result is proved for the regular hexadecagonal plane only. No formula is asserted here for arbitrary regular \(4n\)-gons.

The proof classifies the feasible edge branches needed for the two chord factors but does not classify all equality pairs beyond dihedral symmetry, exchange of \(y\) and \(x-y\), and the displayed endpoint orbit.

Bibliographic and semantic searches cannot prove absolute novelty. An equivalent calculation could exist under a different affine normalization or only in the language of centered equilateral triangles.

## References
1. A. Ahmad, H. Xie and Y. Li, “Some new geometric constants in Banach spaces,” *Advances in Fixed Point Theory* 12 (2022), Article 9, doi:10.28919/afpt/7588. Published 25 August 2022.
