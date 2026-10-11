# Exact M-curvature of the two exceptional regular-polygon families
## Finding
Let \(P_N\subset\mathbb R^2\) be a regular centrally symmetric \(N\)-gon of circumradius \(1\). For a centrally symmetric convex body \(C\), write \(m(C)\) for the M-curvature introduced by Dalla, Larman, Mani-Levitska, and Zong.

For every integer \(r\ge1\),
\[
\boxed{
m(P_{12r-2})
=
1-\sec\!\left(\frac{\pi}{6}+\frac{\pi}{3(12r-2)}\right)
+
\frac{\tan\!\left(\frac{\pi}{6}+\frac{\pi}{3(12r-2)}\right)}
{2\cos\!\left(\frac{\pi}{12r-2}\right)}
}
\tag{1}
\]
and
\[
\boxed{
m(P_{12r+2})
=
1-\sec\!\left(\frac{\pi}{6}-\frac{\pi}{3(12r+2)}\right)
+
\frac{\tan\!\left(\frac{\pi}{6}-\frac{\pi}{3(12r+2)}\right)}
{2\cos\!\left(\frac{\pi}{12r+2}\right)}
}.
\tag{2}
\]

These are precisely the two infinite regular-polygon families that Sezgin identified computationally in the M-curvature discussion:
\[
N=2(6r+1)
\quad\text{or}\quad
N=2(6r+5).
\]

Both sequences satisfy
\[
m(P_N)\longrightarrow 1-\frac{\sqrt3}{2}.
\tag{3}
\]
Among all polygons in the two families, \(P_{10}\) is the unique maximizer. Formula (1) gives
\[
m(P_{10})=\frac{7-3\sqrt5}{2}.
\tag{4}
\]
The decagon value (4) is a consistency check with an already known special case; the contribution here is the closed all-family evaluation and analytic proof.

## Assumptions and scope
For a centrally symmetric convex body \(C\), Dalla--Larman--Mani-Levitska--Zong define
\[
m(C)
=
\min_{\substack{x,y\in\partial C\\ \lVert x-y\rVert_C=1}}
\left(
1-\frac{d(0,L(x,y))}{d(0,T(x,y))}
\right),
\tag{5}
\]
where \(L(x,y)\) is the line through \(x,y\), and \(T(x,y)\) is the parallel supporting line on the same side of the origin.

Equivalently, if a boundary vector \(d\in\partial C\) is fixed and
\[
Q_d=C\cap(C-d),
\]
then
\[
m(C)
=
1-
\max_{d\in\partial C}
\max_{x\in Q_d}
\frac{n_d\cdot x}{h_C(n_d)},
\tag{6}
\]
where \(n_d\) is either perpendicular rotation of \(d\), oriented so that the numerator is nonnegative. Formula (6) is independent of the normalization of \(n_d\).

The result concerns only the two residue classes
\[
N\equiv10,2\pmod{12}.
\]
No formula is asserted here for the remaining even regular polygons.

## Proof
Put
\[
a=\frac{\pi}{N},
\qquad
v_j=(\cos 2ja,\sin 2ja),
\]
so
\[
P_N=\operatorname{conv}\{v_0,\ldots,v_{N-1}\}.
\]
Its edge normals are
\[
u_j=(\cos(2j+1)a,\sin(2j+1)a),
\]
and every edge has support value
\[
c=\cos a.
\tag{7}
\]

By the dihedral symmetries, every boundary difference direction can be represented by
\[
d(t)=(1-t)v_0+t v_1,
\qquad
0\le t\le\frac12.
\tag{8}
\]
Set
\[
n(t)=(-d_2(t),d_1(t)).
\]
Because both families have
\[
N\equiv2\pmod4,
\]
a direct dot-product calculation with the perpendicular vertex gives the useful identity
\[
h_{P_N}(n(t))=\cos a
\qquad
\left(0\le t\le\frac12\right).
\tag{9}
\]
Thus the denominator in (6) is constant throughout the chamber.

For angles \(\alpha,\beta\), let \(X_{\alpha,\beta}(t)\) be the intersection of the two lines
\[
u_\alpha\cdot x=c,
\qquad
u_\beta\cdot(x+d(t))=c,
\tag{10}
\]
where
\[
u_\theta=(\cos\theta,\sin\theta),
\]
and put
\[
F_{\alpha,\beta}(t)
=
\frac{n(t)\cdot X_{\alpha,\beta}(t)}{c}.
\tag{11}
\]
Since \(d(t)\) and \(n(t)\) are affine in \(t\), every \(F_{\alpha,\beta}\) is a quadratic polynomial.

Consider first
\[
N=12r-2.
\]
The cyclic order of the defining half-planes of
\[
P_N\cap(P_N-d(t))
\]
shows that the maximizing vertex in direction \(n(t)\) is
\[
X_{A,B}(t)
\]
until one shifted supporting line changes, and then
\[
X_{A,B_2}(t),
\]
where
\[
A=\frac{2\pi}{3}+\frac a3,
\qquad
B=\frac{\pi}{3}-\frac a3,
\qquad
B_2=\frac{\pi}{3}+\frac{5a}{3}.
\tag{12}
\]
The switch occurs at
\[
t_-=
\frac{\cos a-2\sin(\pi/6+a/3)}
{\cos(\pi/3+5a/3)-\sin(\pi/6+a/3)}.
\tag{13}
\]
For
\[
0<a\le\frac{\pi}{10},
\]
one has
\[
0<t_-<\frac12.
\]

Direct simplification gives
\[
F_{A,B}(0)
=
F_{A,B}(t_-)
=
F_{A,B_2}(t_-)
=
R_-(a),
\tag{14}
\]
where
\[
R_-(a)
=
\sec\!\left(\frac{\pi}{6}+\frac a3\right)
-
\frac{\tan(\pi/6+a/3)}{2\cos a}.
\tag{15}
\]
The quadratic coefficient of \(F_{A,B}\) is
\[
\frac{
\bigl(\sqrt3\cos(4a/3)-\sin(4a/3)\bigr)
\sin^2a\,
\sin(\pi/3+2a/3)
}{
\sin(\pi/6+a/3)\cos a\cos(\pi/6+a/3)
},
\tag{16}
\]
which is positive on the stated range. The quadratic coefficient of \(F_{A,B_2}\) is
\[
\frac{
\bigl(\cos(\pi/3+5a/3)-\sin(\pi/6+a/3)\bigr)^2
}{
\cos a\cos(\pi/6+4a/3)
},
\tag{17}
\]
also positive, and
\[
F'_{A,B_2}\!\left(\frac12\right)=0.
\tag{18}
\]
Hence the first branch is convex with equal endpoint values \(R_-(a)\), while the second branch decreases from \(R_-(a)\) to its vertex at \(t=1/2\). Therefore
\[
\max_{0\le t\le1/2}
\max_{x\in P_N\cap(P_N-d(t))}
\frac{n(t)\cdot x}{h_{P_N}(n(t))}
=
R_-(a).
\tag{19}
\]
Combining (6), (15), and \(a=\pi/N\) gives (1).

Now let
\[
N=12r+2.
\]
The same half-plane walk has one symmetric change:
\[
A=\frac{2\pi}{3}-\frac a3,
\qquad
A_2=\frac{2\pi}{3}+\frac{5a}{3},
\qquad
B=\frac{\pi}{3}+\frac a3.
\tag{20}
\]
The maximizing vertex is \(X_{A,B}(t)\) first and \(X_{A_2,B}(t)\) after the switch
\[
t_+
=
\frac{\cos a-2\cos(\pi/3+a/3)}
{\sin(\pi/6+5a/3)-\cos(\pi/3+a/3)}.
\tag{21}
\]
For
\[
0<a\le\frac{\pi}{14},
\]
one has
\[
0<t_+<\frac12.
\]
At the switch,
\[
F_{A,B}(0)
=
F_{A,B}(t_+)
=
F_{A_2,B}(t_+)
=
R_+(a),
\tag{22}
\]
where
\[
R_+(a)
=
\sec\!\left(\frac{\pi}{6}-\frac a3\right)
-
\frac{\tan(\pi/6-a/3)}{2\cos a}.
\tag{23}
\]
The two branch quadratic coefficients are respectively
\[
\frac{
\bigl(\sin(\pi/6+5a/3)-\cos(\pi/3+a/3)\bigr)
\bigl(\cos(\pi/3+a/3)-\cos(\pi/3+7a/3)\bigr)
}{
2\sin(\pi/3+a/3)\cos a\cos(\pi/3+a/3)
}
\tag{24}
\]
and
\[
\frac{
\bigl(\cos(\pi/3+a/3)-\sin(\pi/6+5a/3)\bigr)^2
}{
\sin(\pi/3+4a/3)\cos a
},
\tag{25}
\]
both positive, while
\[
F'_{A_2,B}\!\left(\frac12\right)=0.
\tag{26}
\]
The same convex-endpoint argument therefore gives the maximum \(R_+(a)\), proving (2).

Taking
\[
a\downarrow0
\]
in either (15) or (23) gives
\[
R_\pm(a)\to\frac{\sqrt3}{2},
\]
which proves (3).

Finally, direct differentiation shows that both \(R_-(a)\) on
\[
0<a\le\frac{\pi}{10}
\]
and \(R_+(a)\) on
\[
0<a\le\frac{\pi}{14}
\]
are strictly decreasing. Since
\[
m=1-R,
\]
the M-curvature strictly increases with \(a\) inside each residue family. The largest available \(a\) is
\[
a=\frac{\pi}{10},
\]
so \(P_{10}\) is the unique maximizer over the union of the two families.

## Verification
The bundled `verify.py` reconstructs the definition directly from half-planes.

For each tested regular polygon it:
1. parametrizes a half-edge of possible boundary difference vectors;
2. constructs
\[
P_N\cap(P_N-d);
\]
3. enumerates all pairwise intersections of its supporting lines;
4. discards infeasible candidates;
5. maximizes the normalized line-height ratio from (6); and
6. compares the result to (1) or (2).

The script tests both residue families through several hundred sides, checks the switch formulas and active pairs, and verifies the decagon specialization
\[
m(P_{10})=\frac{7-3\sqrt5}{2}.
\]

This finite computation is diagnostic only. The all-\(N\) conclusion follows from the exact chamber analysis (9)--(26).

## Relationship to prior work
Dalla, Larman, Mani-Levitska, and Zong introduced M-curvature in their study of blocking numbers and posed the problem of maximizing it over centrally symmetric convex domains. They conjectured that the regular decagon is extremal.

Sezgin's thesis later discusses the same M-curvature problem and states that the regular polygons
\[
2(6r+1)
\quad\text{and}\quad
2(6r+5)
\]
form exceptional infinite families, that this had been proved “by aid of computer,” and that the regular decagon is extremal among those regular polygons. No closed formula or analytic all-family proof is supplied there.

Formulae (1)--(2) replace that computer-only family statement by an exact analytic evaluation. The decagon specialization (4) is not claimed as new: it is a previously established endpoint and is used here as a consistency check.

Targeted searches under M-curvature, regular polygons, the two residue families, blocking numbers, and the exact trigonometric forms did not locate a published all-family formula implying (1)--(2).

## Limitations
The result evaluates M-curvature only on the two regular-polygon residue families highlighted in the earlier computational observation.

It does not prove that the regular decagon globally maximizes M-curvature over all centrally symmetric convex domains, which is the original broader problem.

The chamber proof depends on the regular-polygon half-plane order. It does not automatically extend to arbitrary centrally symmetric polygons with the same number of sides.

Because the final formula follows from elementary trigonometry once the active half-plane pattern is known, an unindexed calculation in older blocking-number notes remains the principal historical originality risk.

## References
1. L. Dalla, D. G. Larman, P. Mani-Levitska, and C. Zong, *The Blocking Numbers of Convex Bodies*, *Discrete & Computational Geometry* 24 (2000), 267--278. DOI: 10.1007/s004540010032. Online publication: 3 May 2000.
2. S. Sezgin, *The Unrestricted Blocking Number in Convex Geometry*, doctoral thesis, University College London, February 2010, UCL Discovery eprint 19509.
