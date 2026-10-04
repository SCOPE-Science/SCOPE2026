# Twisted squares exhaust symmetric lattice-reduced-complete quadrilaterals

## Finding

Let \(\Lambda\subset\mathbb R^2\) be a full-rank lattice and let \(P\subset\mathbb R^2\) be an origin-symmetric convex quadrilateral. Then \(P\) is simultaneously lattice reduced and lattice complete with respect to \(\Lambda\) if and only if, after carrying \(\Lambda\) to \(\mathbb Z^2\), applying a positive homothety, and making a unimodular change of basis, it has the form
\[
Q_x=\operatorname{conv}\{\pm(1,x),\pm(x,-1)\},
\qquad 0<x<1.
\]
Thus the “twisted squares” introduced as examples by Codenotti and Freyer exhaust the entire origin-symmetric quadrilateral case of their question about bodies that are both lattice reduced and lattice complete.

In the canonical normalization \(\operatorname{width}_{\mathbb Z^2}(Q_x)=2\), the exact area and lattice diameter are
\[
\operatorname{area}(Q_x)=2(1+x^2),
\qquad
\operatorname{diam}_{\mathbb Z^2}(Q_x)=\frac{2(1+x^2)}{1+x}.
\]
The polar has the parameter law
\[
UQ_x^\circ
=
\frac{1+x}{1+x^2}Q_{\psi(x)},
\qquad
U=\operatorname{diag}(1,-1),
\qquad
\psi(x)=\frac{1-x}{1+x}.
\]
The map \(\psi\) is an involution of \((0,1)\) and has the unique fixed point
\[
x_*=\sqrt2-1.
\]
Consequently \(Q_{x_*}\) is the unique canonical member that is self-dual up to positive homothety and the displayed unimodular symmetry. Its lattice diameter is the unique minimum of the canonical diameter profile:
\[
\operatorname{diam}_{\mathbb Z^2}(Q_{x_*})
=4(\sqrt2-1).
\]

## Assumptions and scope

Lattice width, lattice diameter, reducedness, and completeness are those of Codenotti and Freyer. The classification is up to the natural equivalences that preserve these properties: translation, nonzero scalar homothety, and simultaneous linear transport of the body and lattice; after the lattice is identified with \(\mathbb Z^2\), unimodular transformations preserve the lattice.

Because \(P\) is origin-symmetric, its center is first translated to the origin. Scale so that
\[
\operatorname{width}_{\mathbb Z^2}(P)=2.
\]
Then for every nonzero \(z\in\mathbb Z^2\),
\[
h_P(z)\ge1,
\]
and equality is exactly the width condition in direction \(z\).

The source proves that every \(Q_x\) with \(0<x<1\) is simultaneously reduced and complete. The substantive direction below proves that no other origin-symmetric quadrilateral occurs.

## Proof

Let the vertices of the origin-symmetric quadrilateral be \(\pm u,\pm v\), with \(u\) and \(v\) adjacent. Since \(P\) is reduced, Proposition 3.1 of Codenotti–Freyer supplies a primitive width direction \(y_u\in\mathbb Z^2\) uniquely selecting \(u\), and a primitive width direction \(y_v\) uniquely selecting \(v\). These directions are linearly independent: a primitive direction and its negative uniquely select opposite vertices, not adjacent ones.

After the width normalization, both \(y_u\) and \(y_v\) lie on \(\partial P^\circ\), in the relative interiors of the two polar edges dual to \(u\) and \(v\). Those polar edges are adjacent. We claim that \(y_u,y_v\) form a lattice basis.

Indeed, if the sublattice they generate had index greater than one, its fundamental parallelogram would contain a nonzero lattice representative. Replacing that representative by its complement with respect to \(y_u+y_v\) if necessary produces a nonzero lattice point in the triangle
\[
\operatorname{conv}\{0,y_u,y_v\}
\]
other than its three vertices. The radial sides \([0,y_u]\) and \([0,y_v]\) contain no other lattice points because the two directions are primitive. Hence the extra point lies either in the open segment \((y_u,y_v)\) or in the interior of the triangle. Both sets lie in \(\operatorname{int}P^\circ\), contradicting \(h_P(z)\ge1\) for every nonzero lattice vector \(z\). Thus
\[
|\det(y_u,y_v)|=1.
\]

Make a unimodular change of basis sending these two width directions to \(e_1,e_2\). Since they uniquely select adjacent vertices, we may write
\[
u=(1,a),
\qquad
v=(b,1),
\qquad
|a|<1,
\qquad
|b|<1.
\]
The diagonal lattice directions give
\[
h_P(e_1+e_2)=\max(1+a,1+b)\ge1
\]
and
\[
h_P(e_1-e_2)=\max(1-a,1-b)\ge1.
\]
Therefore \(a,b\) cannot both be negative and cannot both be positive. After coordinate reflections and interchange if necessary, write
\[
a=r\ge0,
\qquad
b=-s\le0,
\qquad
0\le r,s<1.
\]
Thus
\[
P=\operatorname{conv}\{\pm(1,r),\pm(-s,1)\}.
\]

Let
\[
A=\begin{pmatrix}1&-s\\ r&1\end{pmatrix},
\qquad
\Delta=1+rs.
\]
Since \(P=A B_1^2\), where \(B_1^2\) is the planar \(\ell_1\)-unit ball, its gauge on a lattice vector \((p,q)\) is
\[
\|(p,q)\|_P
=
\frac{|p+sq|+|q-rp|}{1+rs}.
\]
Suppose first that \(r<s\). The two coordinate values are
\[
\|e_1\|_P=\frac{1+r}{1+rs}
<
\frac{1+s}{1+rs}=\|e_2\|_P.
\]
We show that every lattice vector not parallel to \(e_1\) has strictly larger gauge. By central symmetry assume \(p>0\).

If \(q>0\) and \(q\ge rp\), then
\[
|p+sq|+|q-rp|
=(1-r)p+(1+s)q
\ge2+s-r
>1+r.
\]
If \(q>0\) and \(q<rp\), then \(q\le p-1\), so
\[
|p+sq|+|q-rp|
=(1+r)p-(1-s)q
\ge(r+s)p+1-s
>1+r.
\]
If \(q=-k<0\) and \(p\ge sk\), then
\[
|p-sk|+k+rp
=(1+r)p+(1-s)k
>1+r.
\]
Finally, if \(q=-k<0\) and \(p<sk\), then \(p\le k-1\) and necessarily \(k\ge2\); hence
\[
|p-sk|+k+rp
=(1+s)k-(1-r)p
\ge(r+s)k+1-r
>1+r.
\]
Thus \(\pm e_1\) are the only shortest nonzero lattice vectors in the gauge of \(P\). By Lemma 2.1 of Codenotti–Freyer, these are exactly the lattice diameter directions of \(P\). A complete quadrilateral cannot have only one parallel pair of diameter directions: Proposition 3.7 requires a diameter segment ending in the relative interior of every edge, while segments in one fixed direction pass between only one opposite pair of edges. Hence \(r<s\) is impossible. By symmetry, \(s<r\) is impossible as well. Therefore
\[
r=s=x.
\]

If \(x=0\), then \(P=\operatorname{conv}\{\pm e_1,\pm e_2\}\), which Codenotti–Freyer explicitly note is reduced but not complete. Hence \(0<x<1\), and
\[
P
=
\operatorname{conv}\{\pm(1,x),\pm(-x,1)\}
=
Q_x.
\]
Conversely, Example 3.10 of Codenotti–Freyer proves that every \(Q_x\), \(0<x<1\), is simultaneously lattice reduced and complete. This proves the classification.

For the exact invariants, the determinant of
\[
\begin{pmatrix}1&x\\x&-1\end{pmatrix}
\]
has absolute value \(1+x^2\), while the \(\ell_1\)-unit ball has area \(2\), giving
\[
\operatorname{area}(Q_x)=2(1+x^2).
\]
The gauge formula with \(r=s=x\) shows that its shortest nonzero lattice vectors are \(\pm e_1,\pm e_2\), each of gauge
\[
\lambda_1(Q_x;\mathbb Z^2)=\frac{1+x}{1+x^2}.
\]
Since \(Q_x-Q_x=2Q_x\), Lemma 2.1 gives
\[
\operatorname{diam}_{\mathbb Z^2}(Q_x)
=
\frac{2}{\lambda_1(Q_x;\mathbb Z^2)}
=
\frac{2(1+x^2)}{1+x}.
\]

Finally, the defining matrix is symmetric and squares to \((1+x^2)I\). Taking the polar of the image of the \(\ell_1\)-unit ball therefore gives directly
\[
Q_x^\circ
=
\frac{1+x}{1+x^2}Q_{(x-1)/(x+1)}.
\]
The reflection \(U=\operatorname{diag}(1,-1)\) changes the parameter sign, producing the stated involution \(\psi(x)=(1-x)/(1+x)\). Solving \(\psi(x)=x\) gives \(x=\sqrt2-1\). Differentiating the diameter profile gives the same unique interior minimizer.

## Verification

The accompanying `verify.py` uses exact rational arithmetic. It checks the normal-form gauge on a grid of rational \((r,s)\): when \(r<s\), the only shortest lattice directions are \(\pm e_1\); when \(s<r\), they are \(\pm e_2\); and when \(r=s\), the two coordinate direction pairs tie.

For rational \(x\in(0,1)\), it also verifies the diameter formula, area range, polar-vertex formula, the involution identity \(\psi(\psi(x))=x\), and invariance of the canonical diameter profile under \(\psi\). The script was replayed from its packaged path and returned:

`VERIFY_OK symmetric lattice quadrilateral classification profile`

The finite grid is a consistency check only. The classification for arbitrary real parameters is established by the inequalities in the proof.

## Relationship to prior work

Codenotti and Freyer introduced the lattice-complete notion used here and developed the parallel theory of lattice reduced and lattice complete bodies. Their Example 3.10 exhibits the twisted squares \(Q_x\) as simultaneously reduced and complete. Their Section 4.2 gives a complete classification only for triangles, while Question 5.3 asks more generally what can be said about bodies that are simultaneously reduced and complete and lists the \(Q_x\) quadrangles among the known examples. The inspected full text does not state that these exhaust the origin-symmetric quadrilateral case.

Cools and Lemmens classify inclusion-minimal *lattice polygons* of fixed lattice width. Their objects have lattice vertices and their classification addresses width-minimality, not simultaneous completeness for arbitrary real quadrilaterals. Their full text contains a five-type classification, including a quadrangular type, but it does not imply the theorem above.

Bárány and Füredi study lattice diameter of convex polygons under an earlier, slightly different completeness framework. The accessible material establishes their diameter/width focus but did not provide full text for a decisive theorem-by-theorem comparison. Codenotti–Freyer explicitly cite that work as using a slightly different notion and nevertheless present the twisted squares only as examples and pose the simultaneous reduced/complete question. This older source remains a stated residual originality risk rather than being treated as absent.

Targeted searches using “twisted square,” the coordinate model, origin-symmetric or centrally symmetric quadrilateral, lattice reduced, lattice complete, polar, and the parameter \(\sqrt2-1\) did not locate an equivalent classification.

## Limitations

The theorem classifies only origin-symmetric quadrilaterals. It does not classify non-symmetric quadrilaterals, pentagons, or hexagons that are simultaneously lattice reduced and complete, and it does not address the higher-dimensional existence question in Question 5.3.

The polar involution and the exact area/diameter formulas are consequences of the classification and the canonical coordinates; the central originality claim is the exhaustion of the symmetric quadrilateral class by twisted squares.

The literature comparison is strong for the defining 2024 theory and the accessible 2017 width-minimal classification, but the full 2001 Bárány–Füredi paper was not accessible in this run. Its different notion and the later paper's explicit framing reduce, but do not eliminate, historical alias risk.

## References

G. Codenotti and A. Freyer, “Lattice reduced and complete convex bodies,” Journal of the London Mathematical Society 110 (2024), e12982, DOI 10.1112/jlms.12982; arXiv:2307.09429, first submitted 2023-07-18.

F. Cools and A. Lemmens, “Minimal polygons with fixed lattice width,” Annals of Combinatorics 23 (2019), 285–293, DOI 10.1007/s00026-019-00431-0; arXiv:1702.01131, first submitted 2017-02-03.

I. Bárány and Z. Füredi, “On the lattice diameter of a convex polygon,” Discrete Mathematics 241 (2001), 41–50, DOI 10.1016/S0012-365X(01)00145-5.
