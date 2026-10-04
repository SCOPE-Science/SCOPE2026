# Sharp minimal width of quadrilaterals inscribed in a disk
## Finding
Let \(D=\{x\in\mathbb R^2:\|x\|_2\le 1/2\}\), so the minimal width of \(D\) is \(w(D)=1\). For convex polygons \(P\subset D\) with at most four vertices, define
\[
\lambda_4(D)=\sup_P\frac{w(P)}{w(D)}.
\]
Then
\[
\lambda_4(D)=\frac{4\sqrt{3}}{9}.
\]
All nondegenerate equality cases can also be classified. Write the vertices of an equality quadrilateral as \(A,B,C,D\) in cyclic order and let \(x_1,x_2,x_3,x_4>0\) be half the four consecutive central arc angles. Up to cyclic relabeling and reversal, equality holds exactly when
\[
x_1=x_4=s_0:=\arcsin\sqrt{\frac23},\qquad x_2+x_3=\pi-2s_0,\qquad 0<x_2,x_3\le s_0.
\]
Thus the equality cases form a one-parameter family. It contains the symmetric deltoid displayed in the motivating paper and, at the two endpoints of the parameter interval, the corresponding limiting extreme trapezoids with three equal side lengths.

## Assumptions and scope
Minimal width means the minimum, over all unit directions, of the distance between the two parallel supporting lines orthogonal to that direction. The disk is normalized to radius \(1/2\), hence width \(1\). Polygons are allowed to have at most four vertices; degenerate repetitions do not improve the optimum.

A vertex of a polygon inside \(D\) can be moved radially outward from the segment joining its two neighbors until it reaches \(\partial D\), while the old polygon remains contained in the new one. Since width is monotone under inclusion, it is enough to consider polygons whose vertices lie on \(\partial D\).

Triangles are not extremal. If a triangle is inscribed in the diameter-one circle and its half-arc gaps are \(x,y,z>0\) with \(x+y+z=\pi\), its side lengths are \(\sin x,\sin y,\sin z\). Its three altitudes are the pairwise products of these side lengths, so if \(m\) is its minimal width then
\[
m^3\le (\sin x\sin y\sin z)^2\le\left(\frac{\sqrt3}{2}\right)^6,
\]
which gives \(m\le 3/4<4\sqrt3/9\). Hence an extremizer has four distinct boundary vertices.

## Proof
Let \(Q=ABCD\) be a cyclic quadrilateral in the diameter-one circle. Set
\[
a=|AB|,\quad b=|BC|,\quad c=|CD|,\quad d=|DA|,
\]
and let
\[
p=|AC|,\qquad q=|BD|.
\]
Because the circumradius is \(1/2\), the altitude of any inscribed triangle to one side equals the product of its other two side lengths. Therefore the widths of \(Q\) perpendicular to its four sides are
\[
W_a=\max\{bp,dq\},\quad
W_b=\max\{cq,ap\},\quad
W_c=\max\{dp,bq\},\quad
W_d=\max\{aq,cp\}.
\]
For a polygon, a minimum of the width function is attained at a direction perpendicular to an edge, so
\[
w(Q)=\min\{W_a,W_b,W_c,W_d\}.
\]

The cyclic cosine law gives
\[
p^2=\frac{(ac+bd)(ad+bc)}{ab+cd},\qquad
q^2=\frac{(ac+bd)(ab+cd)}{ad+bc},
\]
and hence
\[
\frac pq=\frac{ad+bc}{ab+cd}.
\]
Relabel cyclically so that \(p\ge q\). Then \((a-c)(d-b)\ge0\); after rotating by two vertices if necessary, assume \(a\ge c\) and \(d\ge b\), and after reversing orientation if necessary, assume \(a\le d\). The ratio formula implies
\[
dq\ge bp,\qquad aq\ge cp,
\]
while \(ap\ge cq\) and \(dp\ge bq\) are immediate. Thus
\[
W_a=dq,\quad W_b=ap,\quad W_c=dp,\quad W_d=aq,
\]
and the ordering \(p\ge q\), \(a\le d\) yields
\[
w(Q)=aq.
\]

Let \(x_1,x_2,x_3,x_4>0\) be half the four consecutive central arc angles, so \(x_1+x_2+x_3+x_4=\pi\), and let \(a=\sin x_1\), \(d=\sin x_4\). If one \(x_i>\pi/2\), the remaining three half-arcs have total \(r<\pi/2\), and a side-normal width adjacent to that large gap is at most
\[
\max_{0\le u\le r}\sin u\sin(r-u)=\sin^2(r/2)<\frac12,
\]
so such a quadrilateral is strictly suboptimal. Hence for an extremizer every \(x_i\le\pi/2\). Under the relabeling above, write
\[
s=x_1,\qquad t=x_4,
\]
so \(s\le t\). The diagonal \(q=|BD|\) is the chord subtending the complementary pair of arcs, hence
\[
q=\sin(s+t),
\]
and therefore
\[
w(Q)=\sin s\,\sin(s+t).
\]

If \(s\le\pi/4\), then
\[
w(Q)\le\sin s\le\frac{\sqrt2}{2}<\frac{4\sqrt3}{9}.
\]
If \(s\ge\pi/4\), then \(t\ge s\) gives \(s+t\ge\pi/2\), where the sine decreases as \(t\) increases. Hence
\[
w(Q)\le \sin s\sin(2s)=2\sin^2s\cos s.
\]
Put \(z=\sin^2s\). On \(1/2\le z\le1\), this upper bound is
\[
2z\sqrt{1-z},
\]
whose unique maximum occurs at \(z=2/3\). Its value is
\[
2\cdot\frac23\cdot\frac1{\sqrt3}=\frac{4\sqrt3}{9}.
\]
Equality forces \(t=s=s_0:=\arcsin\sqrt{2/3}\). The other two half-arcs then have sum \(\pi-2s_0\), and the relabeling inequalities are equivalent to requiring each of them to be at most \(s_0\). Conversely, every positive split with those bounds gives all four side-normal widths at least \(4\sqrt3/9\), with two of them equal to that value. This proves both the sharp constant and the complete equality classification.

## Verification
A standalone standard-library checker is included as `artifacts/verify_widest_quadrilateral.py`. It independently evaluates polygon support widths and the closed side/diagonal formulas for \(30000\) random cyclic quadrilaterals, checks that none exceeds \(4\sqrt3/9\), verifies eleven samples across the equality family, and verifies the coordinates
\[
(1/2,0),\quad(-1/6,\sqrt2/3),\quad(-1/2,0),\quad(-1/6,-\sqrt2/3).
\]
The replay command is `python3 artifacts/verify_widest_quadrilateral.py`; its success marker is `VERIFY_OK widest inscribed quadrilateral`. The computation is a consistency check only; the proof above is analytic and does not depend on finite sampling.

## Relationship to prior work
Lassak's 2017 paper defines the same minimal-width approximation problem and treats the unit-width disk. It proves the exact value for odd numbers of vertices and, for four vertices, exhibits a one-parameter family of quadrilaterals with decimal width approximately \(0.7698\), then conjectures that this is optimal. In the radius-\(1/2\) normalization used here, direct evaluation of the displayed coordinates gives \(4\sqrt3/9\), agreeing with that decimal value. The symbolic coefficient printed in the displayed lower bound of the arXiv version is twice this normalized value. The result here supplies the missing global upper bound and characterizes every equality case.

The 2023 paper by González-Arreola, Jerónimo-Castro, and Sánchez-Ortiz studies a different approximation direction: wide triangles contained in an arbitrary quadrilateral. Its theorem does not determine the largest minimal width of a quadrilateral contained in a disk.

## Limitations
The theorem concerns the Euclidean disk and quadrilaterals only. It does not settle the corresponding even-\(n\) disk problem for larger \(n\), nor the analogous extremal problem for general centrally symmetric convex bodies. The originality search found no covering exact theorem, but an obscure older result under different terminology remains a residual bibliographic risk.

## References
1. M. Lassak, *Approximation of convex bodies by polytopes with respect to minimal width and diameter*, arXiv:1703.10110, first submitted 2017-03-29.
2. E. González-Arreola, J. Jerónimo-Castro, and D. Sánchez-Ortiz, *Approximation of Quadrilaterals by Triangles with Respect to Minimal Width*, Results in Mathematics 78 (2023), DOI 10.1007/s00025-023-01898-3.
