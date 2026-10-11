# Exact vertex-anchored equilateral-hexagon constant of the regular pentagon
## Finding
Let \(C\) be a regular Euclidean pentagon. Write
\[
D=\frac{C-C}{2},
\]
and use the Minkowski norm with unit ball \(D\) as the relative distance of \(C\). Fix any vertex \(v\) of \(C\).

Every relatively equilateral hexagon inscribed in \(C\) and containing \(v\) has common relative side length
\[
d_v=\frac{3(\sqrt5-1)}4.
\]
In particular, the value is not merely numerical. Under the homothetic-packing correspondence used by Lassak,
\[
r=\frac{d}{2+d},
\]
the corresponding six-copy positive-homothety ratio is
\[
r_v=3-\frac{6\sqrt5}{5}=0.316718427\ldots .
\]

This theorem concerns the invariant attached to a prescribed pentagon vertex. It does not assert that the vertex is globally optimal among all possible first boundary points.

## Assumptions and scope
The polygon \(C\) is any affine image of a regular pentagon; relative distance is affine invariant, so it is enough to work with one convenient affine model.

Parametrize \(\partial C\) cyclically by \(s\in[0,5]\), using unit parameter length on each of the five sides. The source theorem proves existence of a relatively equilateral \(k\)-gon through every prescribed boundary point, and its accompanying observation states that for \(k\ge4\), all relatively equilateral \(k\)-gons sharing the same boundary vertex have the same common relative side length. Thus it is enough to construct one exact hexagon through a chosen vertex.

The value \(d_v\) is a vertex-anchored quantity. The global invariant \(d_C(6)\) allows the first boundary point to vary, and its equality with \(d_v\) is not proved here.

## Proof
Put \(q=\sqrt5\) and use the affine regular-pentagon model
\[
\begin{aligned}
V_0&=(1,0),\\
V_1&=\left(\frac{q-1}{4},1\right),\\
V_2&=\left(-\frac{q+1}{4},\frac{q-1}{2}\right),\\
V_3&=\left(-\frac{q+1}{4},-\frac{q-1}{2}\right),\\
V_4&=\left(\frac{q-1}{4},-1\right).
\end{aligned}
\]
Let \(P(s)\) linearly traverse \(V_jV_{j+1}\) when \(j\le s\le j+1\), with indices modulo \(5\). Define
\[
s_0=0,\quad
s_1=\frac34,\quad
s_2=\frac{15-q}{8},\quad
s_3=\frac52,\quad
s_4=\frac{25+q}{8},\quad
s_5=\frac{17}{4}.
\]
These parameters are strictly increasing in \([0,5)\), so the points \(P_i=P(s_i)\) occur in convex cyclic order.

The difference body \(D=(C-C)/2\) is the centrally symmetric decagon with counterclockwise vertices
\[
\begin{aligned}
D_0&=\left(-\frac q4,-\frac{q+1}{4}\right),&
D_1&=(0,-1),\\
D_2&=\left(\frac q4,-\frac{q+1}{4}\right),&
D_3&=\left(\frac{q+5}{8},\frac{1-q}{4}\right),\\
D_4&=\left(\frac{q+5}{8},\frac{q-1}{4}\right),&
D_5&=\left(\frac q4,\frac{q+1}{4}\right),\\
D_6&=(0,1),&
D_7&=\left(-\frac q4,\frac{q+1}{4}\right),\\
D_8&=\left(-\frac{q+5}{8},\frac{q-1}{4}\right),&
D_9&=\left(-\frac{q+5}{8},\frac{1-q}{4}\right).
\end{aligned}
\]
Set
\[
d_0=\frac{3(q-1)}4.
\]
For \(i=0,\ldots,5\), let \(Z_i=P_{i+1}-P_i\), where \(P_6=P_0\). Direct exact substitution gives the following boundary representations for \(Z_i/d_0\):
\[
\begin{array}{c|c}
i & Z_i/d_0\\ \hline
0 & D_7\\
1 & (1-t_1)D_8+t_1D_9,\quad t_1=\frac{5-q}{6}\\
2 & (1-t_2)D_0+t_2D_1,\quad t_2=\frac12-\frac q6\\
3 & (1-t_3)D_1+t_3D_2,\quad t_3=\frac12+\frac q6\\
4 & (1-t_4)D_3+t_4D_4,\quad t_4=\frac{1+q}{6}\\
5 & D_5 .
\end{array}
\]
Since \(2<q<3\), every displayed \(t_i\) lies in \([0,1]\). Hence \(Z_i/d_0\in\partial D\) for every \(i\). By the definition of the Minkowski gauge of \(D\),
\[
\lVert Z_i\rVert_D=d_0
\]
for all six sides. Therefore \(P_0,\ldots,P_5\) is a relatively equilateral hexagon through the vertex \(V_0\) with common relative side length \(d_0\).

The source observation for \(k\ge4\) now shows that every relatively equilateral hexagon through \(V_0\) has the same common relative side length. Dihedral symmetry gives the same value for every pentagon vertex. Thus
\[
d_v=\frac{3(\sqrt5-1)}4.
\]

Finally,
\[
\frac{d_v}{2+d_v}
=
\frac{3(\sqrt5-1)}{5+3\sqrt5}
=
3-\frac{6\sqrt5}{5}.
\]
This is the claimed homothetic-copy ratio.

## Verification
The supplied `verify.py` performs the calculation symbolically in \(\mathbb Q(\sqrt5)\). It reconstructs the six boundary points, the ten vertices of \(D\), verifies each of the six boundary representations exactly, checks the four interpolation parameters lie in \([0,1]\), and verifies the packing-ratio simplification. The script returns `VERIFY_OK`.

The checker verifies the explicit construction. The statement that all relatively equilateral hexagons with the same prescribed boundary vertex have the same side length is a published structural fact and was checked in the primary source.

## Relationship to prior work
Lángi's 2003 paper develops relative distance for convex bodies and exact side-length questions for inscribed polygons. Lassak's 2004 paper proves existence of relatively equilateral polygons through prescribed boundary points and records the common-vertex equal-length property for \(k\ge4\). In its discussion of six-point homothetic packing, the same paper identifies the regular pentagon as the likely worst body and depicts a six-copy pentagonal packing with ratio only approximately \(0.32\), corresponding to an equilateral-hexagon side length only approximately \(0.94\).

The result above extracts an exact algebraic value for the canonical vertex-anchored configuration behind that benchmark. Searches using relative-distance, equilateral-hexagon, regular-pentagon, six-homothet, numerical-value, and radical-form aliases did not locate this exact constant in the inspected literature.

A later six-point result allowing arbitrary points of the pentagon, including an interior point, has a different domain and does not imply this boundary-inscribed, prescribed-vertex equilateral-hexagon statement.

## Limitations
No global optimization over the first boundary point is claimed. In particular, the theorem does not prove that
\[
d_C(6)=\frac{3(\sqrt5-1)}4
\]
for the regular pentagon, nor does it prove the broader conjectural extremality of the regular pentagon among all convex bodies.

The originality conclusion is limited by historical indexing: the 2004 figure may have been generated from an unpublished exact calculation, and an unindexed note could contain the same radical value.

## References
1. Z. Lángi, *On the relative lengths of sides of convex polygons*, Studia Scientiarum Mathematicarum Hungarica 40 (2003). DOI: 10.1556/SSCMATH.40.2003.1-2.9. Public date verified as 2003-07-01.
2. M. Lassak, *On relatively equilateral polygons inscribed in a convex body*, Publicationes Mathematicae Debrecen 65 (2004), 133--148. DOI: 10.5486/PMD.2004.2953. Relevant items are Theorem 1, the common-vertex equal-length observation, Claim 3, and Figure 6.
