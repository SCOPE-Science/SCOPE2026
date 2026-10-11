# Exact area spectrum of affine-regular hexagons in the regular octagon
## Finding
Let \(O_8\subset\mathbb R^2\) be the regular octagon of circumradius \(1\), centered at the origin. If \(H\) ranges over all affine-regular hexagons inscribed in \(O_8\), then
\[
\boxed{
\operatorname{area}(H)\in
\left[
\frac{3(2+3\sqrt2)}8,
\frac{3(3-\sqrt2)}2
\right]
}
\tag{1}
\]
and every value in this interval occurs.

Since
\[
\operatorname{area}(O_8)=2\sqrt2,
\]
the normalized spectrum is
\[
\boxed{
\frac{\operatorname{area}(H)}{\operatorname{area}(O_8)}
\in
\left[
\frac{9+3\sqrt2}{16},
\frac{9\sqrt2-6}{8}
\right].
}
\tag{2}
\]

Thus the regular octagon has a nontrivial but very narrow affine-regular-hexagon area band: approximately
\[
0.827665\le
\frac{\operatorname{area}(H)}{\operatorname{area}(O_8)}
\le0.840990.
\]

## Assumptions and scope
An affine-regular hexagon is a nonsingular affine image of a Euclidean regular hexagon. A centered affine-regular hexagon can be represented as
\[
H(u,v)=\operatorname{conv}\{\pm u,\pm v,\pm(v-u)\},
\tag{3}
\]
with \(u\) and \(v\) linearly independent. Its area is
\[
\operatorname{area}(H(u,v))=3\lvert\det(u,v)\rvert.
\tag{4}
\]

For an inscribed hexagon, all six points in (3) lie on \(\partial O_8\). Central symmetry of \(O_8\) makes it enough to require
\[
u,\ v,\ v-u\in\partial O_8.
\tag{5}
\]

The result is specific to the regular octagon. It does not claim universal sharp constants for arbitrary centrally symmetric convex bodies.

## Proof
Write
\[
q=\frac{\sqrt2}{2}.
\]
The octagon vertices, in counterclockwise order, are
\[
p_0=(1,0),\quad
p_1=(q,q),\quad
p_2=(0,1),\quad
p_3=(-q,q),
\]
followed by their negatives. Its eight supporting inequalities can be written without nested radicals as
\[
n_j\cdot x\le1,
\qquad j=0,\ldots,7,
\tag{6}
\]
where, putting \(r=\sqrt2-1\),
\[
\begin{aligned}
n_0&=(1,r),& n_1&=(r,1),& n_2&=(-r,1),& n_3&=(-1,r),\\
n_4&=(-1,-r),& n_5&=(-r,-1),& n_6&=(r,-1),& n_7&=(1,-r).
\end{aligned}
\tag{7}
\]

By a dihedral symmetry, place
\[
u=p_0+s(p_1-p_0),
\qquad0\le s\le1.
\tag{8}
\]
Choose the orientation so that
\[
D=\det(u,v)>0.
\]
Solving the boundary conditions
\[
v\in\partial O_8,
\qquad
v-u\in\partial O_8
\tag{9}
\]
against the eight inequalities (6) leaves exactly three feasible edge chambers. Negative orientation gives their reflected copies. The three positive chambers are as follows.

| chamber | range of \(s\) | \(D(s)=\det(u,v)\) |
| --- | --- | --- |
| I | \(0\le s\le1-q\) | \((2-\sqrt2)s^2+(2\sqrt2-3)s+(3-\sqrt2)/2\) |
| II | \(1-q\le s\le q\) | \((1-\sqrt2/2)s^2+(\sqrt2/2-1)s+(2+\sqrt2)/4\) |
| III | \(q\le s\le1\) | \((2-\sqrt2)s^2-s+(1+\sqrt2)/2\) |

For completeness, chamber I corresponds to \(v\) on edge \(p_1p_2\) and \(v-u\) on edge \(p_2p_3\); chamber II keeps \(v\) on \(p_1p_2\) while \(v-u\) lies on \(p_3p_4\); chamber III has \(v\) on \(p_2p_3\) and \(v-u\) on \(p_3p_4\). Direct substitution into (6) proves that these are the only feasible positive-orientation cases.

Each displayed quadratic has positive leading coefficient. Its endpoint value is the same in every chamber:
\[
D_{\max}=\frac{3-\sqrt2}{2}.
\tag{10}
\]
The critical points are respectively
\[
\frac12-\frac{\sqrt2}{4},
\qquad
\frac12,
\qquad
\frac12+\frac{\sqrt2}{4},
\tag{11}
\]
and substitution gives the common minimum
\[
D_{\min}=\frac14+\frac{3\sqrt2}{8}
=
\frac{2+3\sqrt2}{8}.
\tag{12}
\]
Therefore every inscribed affine-regular hexagon satisfies
\[
D_{\min}\le\lvert\det(u,v)\rvert\le D_{\max}.
\]
Using (4) proves the endpoint values in (1).

Finally, in chamber II the continuous quadratic takes the value \(D_{\max}\) at both endpoints and \(D_{\min}\) at \(s=1/2\). Hence it assumes every value in
\[
[D_{\min},D_{\max}],
\]
so the entire interval in (1), not merely its endpoints, is realized.

## Verification
The bundled `verify.py` performs an exact symbolic facet enumeration over the quadratic field \(\mathbb Q(\sqrt2)\). It fixes \(u\) on one octagon edge, places \(v\) on each of the eight possible edges, and forces \(v-u\) onto each possible active supporting line. It then checks all eight inequalities exactly.

The enumeration returns precisely six oriented feasible cases: the three chambers in the proof and their reflected negative-determinant copies. It symbolically differentiates each determinant quadratic and verifies the common exact extrema (10)--(12), as well as the area normalization.

The computation is a finite exact replay of the chamber proof, not a sampling argument.

## Relationship to prior work
Lassak studied affine-regular hexagons of smallest and largest area in an arbitrary planar centrally symmetric convex body. His theorem gives structural conditions involving additional vertices of the associated affine-regular dodecagon, and his paper explicitly treats the minimum- and maximum-area positions as its basic objects.

The same paper notes special bodies for which all inscribed affine-regular hexagons have equal area, including ellipses and parallelograms, and asks whether other such bodies exist. The regular octagon is therefore a natural canonical test body where the area is not constant.

The inspected primary paper does not evaluate the extreme areas for the regular octagon, and later related work on relatively equilateral polygons uses affine-regular hexagons as canonical inscribed objects without supplying this octagonal area spectrum.

Targeted searches for the regular octagon together with affine-regular hexagons, minimum or maximum area, and exact area-spectrum language did not locate an implication-equivalent published evaluation.

## Limitations
The theorem concerns one canonical centrally symmetric body, the regular octagon. It does not classify the area spectrum for general regular \(2m\)-gons or arbitrary centrally symmetric polygons.

The finite chamber reduction uses the octagon's dihedral symmetry and its eight linear supporting inequalities; the same three-quadratic proof does not automatically generalize to higher side counts.

Because the final optimization is elementary once the three feasible edge chambers are known, an unindexed classical computation remains the principal historical originality risk.

## References
1. M. Lassak, *Affine-regular hexagons of extreme areas inscribed in a centrally symmetric convex body*, *Advances in Geometry* 3 (2003), 45--51. DOI: 10.1515/advg.2003.004.
2. M. Lassak, *On relatively equilateral polygons inscribed in a convex body*, *Publicationes Mathematicae Debrecen* 65 (2004), 133--148. DOI: 10.5486/PMD.2004.2953.
