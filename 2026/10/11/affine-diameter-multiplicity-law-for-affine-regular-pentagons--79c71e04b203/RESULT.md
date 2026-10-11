# Affine-diameter multiplicity law for affine-regular pentagons
## Finding
Let \(P\) be any nondegenerate affine image of a regular pentagon. For \(z\in\operatorname{int}P\), let \(N_a(P,z)\) denote the number of distinct affine diameters of \(P\) containing \(z\).

For Lebesgue-almost every \(z\in P\),
\[
N_a(P,z)\in\{1,3,5\}.
\]
Moreover, for a uniformly chosen point of \(P\),
\[
\Pr[N_a=1]=5-2\sqrt5,
\]
\[
\Pr[N_a=3]=\frac{7\sqrt5-15}{2},
\]
and
\[
\Pr[N_a=5]=\frac{7-3\sqrt5}{2}.
\]
Thus the complete almost-everywhere multiplicity distribution is explicit. Its first two moments are
\[
\mathbb E[N_a]=\sqrt5
\]
and
\[
\operatorname{Var}(N_a)=20-8\sqrt5.
\]

The fivefold locus is, up to its boundary, the central pentagon of the pentagram formed by the five diagonals. In a Euclidean regular model that central pentagon is rotated by \(\pi/5\) and has linear scale
\[
\frac{3-\sqrt5}{2}
\]
relative to the original pentagon.

## Assumptions and scope
An affine diameter of a planar convex body is a chord whose two endpoints lie in two distinct parallel supporting lines. Distinct affine diameters are counted as distinct geometric segments.

The statement is affine invariant. Therefore it is enough to prove it for one regular pentagon. Boundaries of the five relevant triangle families and all vertex--vertex exceptional chords form a finite union of line segments, hence a null set. The classification is deliberately stated almost everywhere so that these nongeneric points do not need a separate convention.

The result does not claim a corresponding closed distribution for arbitrary pentagons or for regular odd polygons with more than five sides.

## Proof
Label the vertices \(v_0,\ldots,v_4\) cyclically. For each edge
\[
E_j=[v_j,v_{j+1}],
\]
the unique vertex on the opposite supporting line parallel to \(E_j\) is
\[
v_{j+3},
\]
with indices taken modulo \(5\). Define
\[
T_j=\operatorname{conv}(v_j,v_{j+1},v_{j+3}).
\]

Away from the finite union of exceptional chords, every affine diameter has one endpoint in the relative interior of an edge and the other endpoint at the unique opposite vertex. Conversely, every segment joining \(v_{j+3}\) to a point of \(E_j\) is an affine diameter. A point in the interior of \(T_j\) lies on exactly one such segment. Hence, outside a null set,
\[
N_a(P,z)=\sum_{j=0}^{4}\mathbf 1_{T_j}(z).
\]
This is the planar edge--opposite-vertex specialization of the face-pair description in the published affine-diameter theory.

Each internal diagonal of the pentagon is a side of exactly two of the triangles \(T_j\). The indicator sum is locally constant off the five diagonals. Crossing one diagonal changes membership in exactly two triangles, so the count changes by an even integer. Near the relative interior of any boundary edge the count is \(1\). Any generic interior point can be joined to such a boundary-near point by a path avoiding diagonal-intersection points and crossing diagonals transversely. Therefore the generic count is odd. Since there are only five triangles,
\[
N_a(P,z)\in\{1,3,5\}
\]
almost everywhere.

We now compute the level-set areas. It is convenient to use the affine regular model
\[
\begin{aligned}
v_0&=(1,0),\\
v_1&=\left(\frac{\sqrt5-1}{4},1\right),\\
v_2&=\left(-\frac{\sqrt5+1}{4},\frac{\sqrt5-1}{2}\right),\\
v_3&=\left(-\frac{\sqrt5+1}{4},-\frac{\sqrt5-1}{2}\right),\\
v_4&=\left(\frac{\sqrt5-1}{4},-1\right).
\end{aligned}
\]
A shoelace calculation gives
\[
\operatorname{area}(P)=\frac52.
\]
Every triangle \(T_j\) has area
\[
\frac{\sqrt5}{2},
\]
so
\[
\frac{1}{\operatorname{area}(P)}
\int_P N_a(P,z)\,dz
=
\frac{\sum_{j=0}^{4}\operatorname{area}(T_j)}
{\operatorname{area}(P)}
=
\sqrt5.
\]

The common intersection of the five triangles is exactly the central pentagon of the pentagram. In the model above its cyclic vertices are
\[
\begin{aligned}
w_0&=\left(\frac{\sqrt5-1}{4},\sqrt5-2\right),\\
w_1&=\left(\frac{2-\sqrt5}{2},\frac{3-\sqrt5}{2}\right),\\
w_2&=\left(\frac{\sqrt5-3}{2},0\right),\\
w_3&=\left(\frac{2-\sqrt5}{2},-\frac{3-\sqrt5}{2}\right),\\
w_4&=\left(\frac{\sqrt5-1}{4},-(\sqrt5-2)\right).
\end{aligned}
\]
Each \(w_j\) is the intersection of two pentagram diagonals, and all five points satisfy the half-plane inequalities defining every \(T_j\). The central cell is therefore the fivefold region. Its area is
\[
\frac{35-15\sqrt5}{4},
\]
so its normalized area is
\[
p_5=
\frac{7-3\sqrt5}{2}.
\]

Let \(p_1,p_3,p_5\) be the normalized areas of the three generic multiplicity levels. Since the diagonal arrangement has area zero,
\[
p_1+p_3+p_5=1.
\]
The integral identity above gives
\[
p_1+3p_3+5p_5=\sqrt5.
\]
Substituting the exact value of \(p_5\) yields
\[
p_3=\frac{7\sqrt5-15}{2}
\]
and
\[
p_1=5-2\sqrt5.
\]
These are all positive and sum to \(1\).

Finally,
\[
\mathbb E[N_a^2]
=
p_1+9p_3+25p_5
=
25-8\sqrt5,
\]
hence
\[
\operatorname{Var}(N_a)
=
25-8\sqrt5-5
=
20-8\sqrt5.
\]

## Verification
The supplied `verify.py` uses exact arithmetic in \(\mathbb Q(\sqrt5)\). It reconstructs the affine-regular model, verifies that each edge has the stated opposite vertex, checks the five triangle orientations and equal areas, verifies the pentagram incidence of the five central vertices, checks that every central vertex satisfies all triangle half-plane inequalities, and computes the outer and central areas exactly.

It then verifies the three probability formulas, their positivity, normalization, mean, second moment, and variance. The checker returns `VERIFY_OK`.

The checker is not being used to infer a continuum statement from finite sampling. The almost-everywhere correspondence between affine diameters and the five edge--opposite-vertex triangle families, and the parity argument across the diagonal arrangement, are proved above.

## Relationship to prior work
Bárány, Hug, and Schneider introduced the mean number \(N_a(K)\) of affine diameters through a point and proved exact integral formulas and sharp bounds. Their planar polytope proof gives the edge--opposite-face decomposition used here, and in dimension two it determines the mean through mixed-area data. It does not state a pointwise multiplicity distribution for regular or affine-regular pentagons.

Soltan's survey organizes classical results on affine diameters, including intersection and characterization questions, but the indexed material does not give the three-level pentagon distribution above.

Berele and Catoiu later use a regular pentagon as an example in their study of Fermat--Ceder points for affine diameters. Their published preview explicitly depicts affine diameters of a regular pentagon and proves nonuniqueness of certain equiangular concurrency points, but it does not state the areas of the \(1\)-, \(3\)-, or \(5\)-fold affine-diameter loci, nor their probability law or variance.

Searches using “regular pentagon affine diameters,” “affine-diameter multiplicity,” “mean number of affine diameters pentagon,” “pentagram affine diameters,” and the three exact radical area fractions did not locate a covering theorem or table.

## Limitations
The result is an almost-everywhere classification. Points on the five diagonals and on the finite collection of exceptional vertex--vertex chords are excluded; their exact pointwise multiplicities are not classified here.

The proof is specific to affine-regular pentagons. It does not provide a multiplicity law for arbitrary pentagons, and it does not claim that the same three-level pattern persists for larger odd regular polygons.

The 2020 regular-pentagon figure is highly relevant geometric prior art. Its inspected preview does not state the new measure-theoretic distribution, but an unindexed discussion or exercise based on the same pentagram arrangement remains a residual originality risk.

## References
1. I. Bárány, D. Hug, and R. Schneider, *Affine diameters of convex bodies*, arXiv:1403.7158v1, 2014-03-27; Proceedings of the American Mathematical Society 144 (2016), 797--812. DOI: 10.1090/PROC12746.
2. V. Soltan, *Affine diameters of convex bodies -- a survey*, Expositiones Mathematicae 23 (2005), 47--63. DOI: 10.1016/j.exmath.2005.01.019.
3. A. Berele and S. Catoiu, *The Fermat--Torricelli theorem in convex geometry*, Journal of Geometry 111 (2020), article 22. DOI: 10.1007/s00022-020-00535-6.
