# Sharp \(C\)-approximate Birkhoff symmetry of regular even polygonal planes
## Finding
Let \(N\ge6\) be even and let \(X_N\) be the real Banach plane whose unit ball is a Euclidean regular \(N\)-gon. For Chmieliński approximate Birkhoff--James orthogonality, define
\[
\chi_C(X_N)
=
\inf\left\{
\varepsilon\in[0,1):
x\perp_B y
\Longrightarrow
y\perp_B^\varepsilon x
\text{ for all }x,y\in X_N
\right\}.
\]
Then
\[
\boxed{
\chi_C(X_N)
=
\begin{cases}
0,&N\equiv2\pmod4,\\[3pt]
\tan(\pi/N),&4\mid N.
\end{cases}
}
\tag{1}
\]

Thus regular even polygons have an exact parity phase law. The \(N\equiv2\pmod4\) family has genuinely symmetric Birkhoff--James orthogonality, whereas every regular \(4m\)-gon has a positive sharp defect
\[
\chi_C(X_{4m})=\tan\frac{\pi}{4m}.
\]
In particular,
\[
\chi_C(X_8)=\sqrt2-1,
\qquad
\chi_C(X_{12})=2-\sqrt3.
\]
Moreover,
\[
\chi_C(X_N)\sim\frac{\pi}{N}
\]
along multiples of four.

## Assumptions and scope
All scalars are real.

Put
\[
\alpha=\frac{\pi}{N},
\qquad
c=\cos\alpha,
\qquad
s=\sin\alpha.
\]
Use the Euclidean-circle normalization
\[
v_k=
\left(
\cos((2k+1)\alpha),
\sin((2k+1)\alpha)
\right),
\qquad
0\le k<N.
\]
The regular polygon with vertices \(v_k\) is the unit ball of \(X_N\).

Its edge between
\[
(c,-s)
\quad\text{and}\quad
(c,s)
\]
has the norm-one supporting functional
\[
f_0(u,v)=\frac{u}{c}.
\tag{2}
\]
The next edge has supporting functional
\[
f_1(u,v)
=
\frac{u\cos(2\alpha)+v\sin(2\alpha)}{c}.
\tag{3}
\]

For a nonzero vector \(u\), let
\[
J(u)
=
\left\{
f\in S_{X_N^*}:f(u)=\|u\|
\right\}.
\]
The standard functional characterization of Chmieliński approximate Birkhoff--James orthogonality is
\[
u\perp_B^\varepsilon v
\quad\Longleftrightarrow\quad
\text{there is }f\in J(u)
\text{ with }
|f(v)|\le\varepsilon\|v\|.
\tag{4}
\]
Consequently, for unit vectors define the reverse residual
\[
\eta(y,x)
=
\min_{g\in J(y)}|g(x)|.
\tag{5}
\]
Then
\[
\chi_C(X_N)
=
\sup_{\substack{x,y\in S_{X_N}\\x\perp_B y}}
\eta(y,x).
\tag{6}
\]

## Proof
Write
\[
N=2n.
\]
The dihedral group of the regular polygon acts by norm isometries, so it is enough to analyze one edge and one adjacent vertex.

First let \(x\) be a smooth point of the reference edge:
\[
x=(c,t),
\qquad
-s<t<s.
\tag{7}
\]
By (2),
\[
J(x)=\{f_0\}.
\]
Hence
\[
x\perp_B y
\quad\Longleftrightarrow\quad
f_0(y)=0.
\tag{8}
\]
Thus \(y\) lies on the vertical diameter.

### Case 1: \(4\mid N\)

Now \(n\) is even. The vertical direction is normal to an edge of the regular polygon, so the two unit vectors satisfying (8) are
\[
y=\pm(0,c).
\]
For \(y=(0,c)\), the unique norming functional is
\[
g(u,v)=\frac{v}{c}.
\]
Therefore
\[
\eta(y,x)=|g(x)|=\frac{|t|}{c}<\frac{s}{c}=\tan\alpha.
\tag{9}
\]

It remains to consider a vertex. By symmetry take
\[
x=(c,s).
\tag{10}
\]
Then
\[
J(x)=\operatorname{conv}\{f_0,f_1\}.
\]
The condition \(x\perp_B y\) means that some functional in this line segment vanishes on \(y\). Up to replacing \(y\) by \(-y\), the direction of \(y\) therefore sweeps from angle
\[
\frac{\pi}{2}
\quad\text{to}\quad
\frac{\pi}{2}+2\alpha.
\tag{11}
\]

Because \(n\) is even, the two endpoint directions in (11) are edge-midpoint directions and the middle direction
\[
\frac{\pi}{2}+\alpha
\]
is a vertex direction. Thus the admissible boundary arc consists of two half-edges meeting at that vertex.

On the first open half-edge, the unique norming functional has Euclidean normal angle \(\pi/2\), hence its value at \(x\) is
\[
\frac{s}{c}=\tan\alpha.
\tag{12}
\]
On the second open half-edge, the unique norming functional has normal angle
\[
\frac{\pi}{2}+2\alpha,
\]
and its value at \(x\) is
\[
-\frac{s}{c}=-\tan\alpha.
\tag{13}
\]
At the central vertex, the norming set is the convex hull of these two functionals, so the values in (12)--(13) straddle zero and
\[
\eta(y,x)=0.
\]
At the two endpoint edge midpoints the norming functional is unique and
\[
\eta(y,x)=\tan\alpha.
\]
Together with (9), this proves
\[
\chi_C(X_N)\le\tan\alpha.
\]
The pair
\[
x=(c,s),
\qquad
y=(0,c)
\tag{14}
\]
has
\[
f_0(y)=0,
\]
so \(x\perp_B y\), while \(J(y)=\{g\}\) and
\[
|g(x)|=\tan\alpha.
\]
Thus equality holds:
\[
\chi_C(X_N)=\tan\alpha
\qquad
(4\mid N).
\tag{15}
\]

### Case 2: \(N\equiv2\pmod4\)

Now \(n\) is odd. For the smooth point (7), the vertical direction is a vertex direction. Hence the two vectors in (8) are
\[
y=\pm(0,1).
\]
At \(y=(0,1)\), the two adjacent norming functionals have Euclidean normal angles
\[
\frac{\pi}{2}-\alpha
\quad\text{and}\quad
\frac{\pi}{2}+\alpha.
\]
Their values at \(x=(c,t)\) are respectively
\[
s+t
\quad\text{and}\quad
t-s.
\tag{16}
\]
Because
\[
-s<t<s,
\]
the two numbers in (16) have opposite signs. Their convex hull therefore contains zero, so
\[
y\perp_B x.
\tag{17}
\]

Now take the vertex (10). As before, the condition \(x\perp_B y\) restricts the direction of \(y\) to the sector (11). Since \(n\) is odd, both endpoint directions of that sector are vertex directions, and the entire boundary arc between them is one edge. The supporting normal to that edge has angle
\[
\frac{\pi}{2}+\alpha.
\]
Its value at \(x\), whose radial angle is \(\alpha\), is
\[
\frac{\cos(\pi/2)}{c}=0.
\tag{18}
\]
Thus every admissible \(y\) on this arc satisfies
\[
y\perp_B x.
\]
Central symmetry handles the opposite arc. Hence Birkhoff--James orthogonality is symmetric on \(X_N\), and
\[
\chi_C(X_N)=0
\qquad
(N\equiv2\pmod4).
\tag{19}
\]

Equations (15) and (19) prove (1).

Finally,
\[
\tan\frac{\pi}{N}
=
\frac{\pi}{N}
+
O(N^{-3}),
\]
which gives the stated asymptotic along \(4\mid N\).

## Verification
The bundled `verify.py` reconstructs regular \(N\)-gons for every even
\[
6\le N\le80
\]
in the displayed normalization.

For a dense rational sampling of every edge, it computes norming facets, detects Birkhoff--James orthogonality through sign changes of the norming functionals, and computes the reverse residual in (5). For every tested \(N\), the largest residual agrees with
\[
0
\]
when
\[
N\equiv2\pmod4,
\]
and with
\[
\tan(\pi/N)
\]
when
\[
4\mid N.
\]
The checker also verifies the sharp pair (14).

This numerical enumeration is only a reproducibility check. The continuum theorem follows from the exact support-functional classification in the proof.

## Relationship to prior work
Chmieliński, Khurana and Sain studied global and local approximate symmetry of Birkhoff--James orthogonality. Their primary paper identifies \(C\)-approximate symmetry as a natural problem and proves qualitative regular-polyhedral approximate-symmetry results. The inspected material states the functional framework, the polyhedral setting, and the regular-polygon examples, but does not give the sharp parity formula (1).

For the zero branch in (1), exact symmetry is consistent with the known classification that a regular \(2n\)-gonal norm has symmetric Birkhoff--James orthogonality when \(n\) is odd. The new quantitative content is therefore the non-Radon family
\[
N=4m,
\]
where the exact optimal defect is
\[
\tan(\pi/N).
\]

Chmieliński and Wójcik's earlier paper introduced global approximate symmetry and a related geometric constant. Only abstract-level material from that paper was accessible for this comparison, so it remains a bibliographic residual risk. Targeted searches for regular polygons, the exact tangent formula, the octagonal value \(\sqrt2-1\), and the dodecagonal value \(2-\sqrt3\) found no covering statement.

A separately indexed exact Dragomir-symmetry computation for the regular octagon concerns the other standard approximate-orthogonality relation. Its parameter is not the \(C\)-approximate parameter in (4), so it does not imply (1).

## Limitations
The result treats Euclidean regular even polygons in dimension two. It does not give the optimal \(C\)-approximate symmetry parameter for arbitrary centrally symmetric polygons.

The \(N\equiv2\pmod4\) zero branch is an exact-symmetry phenomenon already known at the qualitative level; the new contribution is the unified phase law and the sharp positive defect for every regular \(4m\)-gon.

The 2018 global-approximate-symmetry paper was available only through abstract and bibliographic material during the literature comparison. No exact regular-polygon formula was found, but this access limitation remains a residual originality risk.

## References
1. J. Chmieliński, D. Khurana and D. Sain, “Local Approximate Symmetry of Birkhoff--James Orthogonality in Normed Linear Spaces,” *Results in Mathematics* 76 (2021), 136, doi:10.1007/s00025-021-01437-y. First public preprint: arXiv:2012.08162v1, 15 December 2020. Primary Mathematics Subject Classification: 46B20.
2. J. Chmieliński and P. Wójcik, “Approximate symmetry of Birkhoff orthogonality,” *Journal of Mathematical Analysis and Applications* 461 (2018), 625--640, doi:10.1016/j.jmaa.2018.01.031.
3. D. Sain, S. Roy, S. Bagchi and V. Balestro, “A study of symmetric points in Banach spaces,” *Linear and Multilinear Algebra* 70 (2022), 888--898; first public preprint arXiv:1909.12683v1, 27 September 2019.
