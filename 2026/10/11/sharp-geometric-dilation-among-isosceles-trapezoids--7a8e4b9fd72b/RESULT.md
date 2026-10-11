# Sharp geometric dilation among isosceles trapezoids
## Finding
Let \(C\) be the boundary of a nondegenerate Euclidean isosceles trapezoid. Then
\[
\boxed{
\delta(C)\ge
\delta_*=
\frac{2S_*}{\sqrt{(S_*-1)(3S_*+1)}}
=
1.89615765267304\ldots
}
\tag{1}
\]
where \(S_*\) is the unique root in \((1,2)\) of
\[
11S^5-17S^4+6S^3-2S^2-5S-1=0.
\tag{2}
\]

Equality in (1) is unique up to similarity and reflection. Normalize the average base length to \(1\). Then the extremal trapezoid has bases
\[
1-x_*,
\qquad
1+x_*,
\]
leg length \(S_*\), and height
\[
H_*=\sqrt{S_*^2-x_*^2},
\]
where
\[
x_*=\frac{2S_*+1-S_*^2}{2S_*}.
\tag{3}
\]
Numerically,
\[
S_*=1.43009102057699\ldots,
\]
\[
x_*=0.634582585270256\ldots,
\]
\[
H_*=1.28158701210907\ldots.
\]

In particular, allowing the mild asymmetry of an isosceles trapezoid lowers the best dilation below the centrally symmetric value \(2\) forced for parallelograms.

## Assumptions and scope
For a closed curve \(C\), its geometric dilation is the supremum, over distinct points \(p,q\in C\), of the shorter boundary distance from \(p\) to \(q\) divided by the Euclidean distance \(\lvert p-q\rvert\).

Dumitrescu, Ebbers-Baumann, Grüne, Klein, and Rote prove that for every closed convex curve,
\[
\delta(C)=\frac{|C|}{2h},
\tag{4}
\]
where \(h\) is the minimum Euclidean length of a halving chord, namely a chord whose endpoints divide the perimeter into two equal arcs.

Write the two bases of an isosceles trapezoid as
\[
1-x,\qquad 1+x,
\qquad 0\le x<1,
\]
after a similarity normalization. Let its height be \(H>0\) and its equal leg length be
\[
S=\sqrt{x^2+H^2}.
\tag{5}
\]
The perimeter is \(2(1+S)\), so a halving arc has length \(1+S\).

## Proof
Place the vertices, in counterclockwise order, at
\[
A=(0,0),\quad
B=(1-x,0),\quad
C=(1,H),\quad
D=(-x,H).
\tag{6}
\]
The side lengths are
\[
1-x,\quad S,\quad 1+x,\quad S.
\]

Parameterize the boundary by arc length \(u\), starting at \(A\), and pair the point at \(u\) with the point at \(u+1+S\). By reflection symmetry it suffices to examine three regimes.

For
\[
0\le u\le1-x,
\]
the endpoints lie on the two bases and the squared chord length is
\[
d_1(u)^2=(1-x-2u)^2+H^2.
\]
Hence this regime contributes
\[
h_1=H.
\tag{7}
\]

For
\[
1-x\le u\le1,
\]
put
\[
t=u-(1-x),
\qquad 0\le t\le x.
\]
The squared chord length is
\[
d_2(t)^2=
\left(1-x+t\left(1+\frac{x}{S}\right)\right)^2
+
H^2\left(1-\frac{t}{S}\right)^2.
\tag{8}
\]
Differentiation gives
\[
\frac{d}{dt}d_2(t)^2
=
\frac{2(S+x)}{S}(2t+1-S).
\]
Thus the unconstrained minimum occurs at
\[
t=\frac{S-1}{2}.
\]
It lies in the interval exactly when
\[
1\le S\le1+2x,
\]
and then
\[
h_2^2=
\frac{(S-x)(S+1)^2}{2S}.
\tag{9}
\]
If the critical point lies outside the interval, the endpoint value is dominated by one of the other two regimes and creates no additional branch.

For
\[
1\le u\le1-x+S,
\]
put
\[
t=u-1,
\qquad
0\le t\le S-x.
\]
The paired points lie on the two legs and
\[
d_3(t)^2=
\left(1+\frac{x^2}{S}\right)^2
+
H^2
\left(
1-\frac{x+2t}{S}
\right)^2.
\tag{10}
\]
The minimum occurs at
\[
t=\frac{S-x}{2},
\]
so
\[
h_3=1+\frac{x^2}{S}.
\tag{11}
\]

Equations (7), (9), and (11) give the complete halving-distance formula
\[
h=
\min\left\{
H,\,
1+\frac{x^2}{S},\,
\sqrt{\frac{(S-x)(S+1)^2}{2S}}
\right\},
\tag{12}
\]
with the third entry included only when \(1\le S\le1+2x\).

Divide (12) by the half-perimeter \(1+S\). In the active three-branch region define
\[
A=
\frac{\sqrt{S^2-x^2}}{1+S},
\quad
B=
\sqrt{\frac{S-x}{2S}},
\quad
C=
\frac{S+x^2}{S(1+S)}.
\tag{13}
\]
Then
\[
\frac1{\delta(C)}=\min\{A,B,C\}.
\tag{14}
\]

If \(S\le1\), then \(A\le1/2\). If \(S\ge2\), then \(C\le1/2\). If \(1<S<2\) but
\[
x<\frac{S-1}{2},
\]
the middle branch is inactive and
\[
C<
\frac{S+1}{4S}<\frac12.
\]
Therefore every trapezoid with dilation below \(2\) lies in
\[
1<S<2,
\qquad
x\ge\frac{S-1}{2}.
\tag{15}
\]

For fixed \(S\) in (15), both \(A\) and \(B\) decrease strictly with \(x\), while \(C\) increases strictly. The switch between the two decreasing branches occurs at
\[
A=B
\quad\Longleftrightarrow\quad
x=x_0(S):=
\frac{2S+1-S^2}{2S}.
\tag{16}
\]
At this switch,
\[
\operatorname{sgn}\!\left(A^2-C^2\right)
=
\operatorname{sgn} P(S),
\]
where
\[
P(S)=11S^5-17S^4+6S^3-2S^2-5S-1.
\tag{17}
\]
Now
\[
P(1)=-8,\qquad P(2)=109,
\]
and, after writing \(S=1+y\),
\[
P(1+y)
=
11y^5+38y^4+48y^3+24y^2-4y-8.
\]
This polynomial has exactly one sign change, so Descartes' rule of signs gives exactly one positive root. Thus (17) has a unique root \(S_*\in(1,2)\).

For \(1<S<S_*\), the maximizing crossing is \(A=C\). Its value is
\[
m_A(S)=
\frac{\sqrt{S(5S+4)}-S}{2(S+1)},
\tag{18}
\]
and
\[
m_A'(S)=
\frac{
3S+2-\sqrt{S(5S+4)}
}{
2\sqrt S\,(S+1)^2\sqrt{5S+4}
}>0,
\tag{19}
\]
because
\[
(3S+2)^2-S(5S+4)=4(S+1)^2.
\]

For \(S>S_*\), the maximizing crossing is \(B=C\). If its common value is \(r\), eliminating \(x\) gives
\[
S=
\frac{1-r}{
r-(1-2r^2)^2
}.
\tag{20}
\]
Along this branch,
\[
\frac{dS}{dr}
=
-\frac{4r(3r+2)}
{(4r^3+4r^2-1)^2}<0,
\tag{21}
\]
so its optimum decreases with \(S\).

Consequently the global maximum of \(1/\delta(C)\) occurs uniquely where
\[
A=B=C.
\]
Equations (16)--(17) yield \(S=S_*\) and (3). Finally,
\[
\frac1{\delta_*^2}
=
\frac{S_*-x_*}{2S_*}
=
\frac{(S_*-1)(3S_*+1)}{4S_*^2},
\]
which is equivalent to (1).

## Verification
The bundled `verify.py` verifies the algebraic reductions symbolically.

It checks the derivative and minimum in each halving-chord regime, factors the switch equation \(A=B\), derives polynomial (17), verifies the monotonicity formulas (19) and (21), and isolates the unique real root \(S_*\in(1,2)\).

As a separate numerical regression test, it samples many admissible trapezoids, directly parameterizes their boundaries, computes thousands of halving chords, and compares the sampled minimum with formula (12). It also checks that the claimed extremal value agrees with a dense two-parameter search.

The numerical sweep is diagnostic only. The quantified theorem follows from the exact piecewise halving-distance formula and one-variable monotonicity proof above.

## Relationship to prior work
Dumitrescu, Ebbers-Baumann, Grüne, Klein, and Rote establish the halving-pair formula (4), prove the sharp lower bound
\[
\delta(C)\ge\frac n2\tan\frac{\pi}{n}
\]
for centrally symmetric convex \(n\)-gons, and derive a weaker general bound for arbitrary convex \(n\)-gons. Their paper explicitly ends by asking for a tight lower bound on the geometric dilation of arbitrary, not only centrally symmetric, convex polygons.

The present theorem gives a complete sharp answer on the natural first nonsymmetric quadrilateral family. It is not a corollary of the centrally symmetric theorem: the unique extremizer is a genuine trapezoid with unequal bases and has dilation strictly below \(2\).

Targeted searches using “geometric dilation,” “detour,” “halving distance,” “halving chord,” and “isosceles trapezoid” located the general halving-chord literature but no statement of the sharp isosceles-trapezoid constant or its algebraic extremizer.

## Limitations
The theorem treats isosceles trapezoids, not all convex quadrilaterals or all convex polygons.

It does not resolve the source paper's open problem of the sharp lower bound for arbitrary convex \(n\)-gons.

The argument depends on reflection symmetry to reduce the halving-chord geometry to three elementary regimes; general trapezoids require additional branches.

Because the optimization is elementary after the halving-pair reduction, an unindexed specialized calculation remains the principal originality risk.

## References
1. A. Dumitrescu, A. Ebbers-Baumann, A. Grüne, R. Klein, and G. Rote, *On the geometric dilation of closed curves, graphs, and point sets*, arXiv:math/0407135v1, 8 July 2004; *Computational Geometry* 36 (2006), 16--38. DOI: 10.1016/j.comgeo.2005.07.004.
2. A. Ebbers-Baumann, A. Grüne, and R. Klein, *Geometric dilation of closed planar curves: New lower bounds*, *Computational Geometry* 37 (2007), 188--208. DOI: 10.1016/j.comgeo.2004.12.009.
