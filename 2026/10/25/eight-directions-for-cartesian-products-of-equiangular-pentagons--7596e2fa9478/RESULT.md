# Eight directions for Cartesian products of equiangular pentagons

## Finding
Let \(P\) and \(Q\) be arbitrary convex equiangular pentagons with five genuine corners (all five interior angles equal to \(3\pi/5\)), and let \(K=P\times Q\subset\mathbb R^4\). Then the ordinary illumination number and finite fractional illumination number satisfy
\[
\boxed{I(K)=8,\qquad I^*(K)=\frac{25}{4}.}
\]
In particular, the ordinary illumination number is strictly submultiplicative on this natural family: each pentagon has \(I(P)=I(Q)=3\), whereas \(I(P\times Q)=8<9\). The ratio between ordinary and fractional illumination of the product is \(32/25\). These values are independent of the two polygons' side lengths and of their relative scale, orientation and translation.

An optimal ordinary certificate uses eight maximal directional vertex sets, indexed by their starting vertices in \((\mathbb Z/5\mathbb Z)^2\):
\[
(0,0),(0,2),(1,3),(2,0),(2,2),(3,1),(3,3),(4,4).
\]
An optimal fractional certificate assigns weight \(1/4\) to each of the 25 maximal directional vertex sets.

## Assumptions and scope
A nonzero vector \(u\) illuminates a boundary point \(x\) of a full-dimensional convex body \(K\) when \(x+\varepsilon u\in\operatorname{int}K\) for some \(\varepsilon>0\). The ordinary illumination number \(I(K)\) is the minimum number of such directions collectively illuminating every boundary point. The finite fractional illumination number \(I^*(K)\) is the minimum total nonnegative weight of finitely many directions such that the illuminating weight at each boundary point is at least one.

For \(P\) and \(Q\), label vertices \(p_i\) and \(q_j\) cyclically with indices in \(\mathbb Z/5\mathbb Z\). Every vertex of \(K\) is \((p_i,q_j)\). The factors are genuine full-dimensional convex equiangular pentagons; they need not be congruent or regular. The theorem concerns real directions in four dimensions, not merely a preselected finite set of candidate directions.

## Proof
**1. Exact maximal illumination sets of one factor.** At a vertex of an equiangular pentagon the interior tangent cone has opening angle \(3\pi/5\). Its arc of illuminating directions on the unit circle therefore has angular length \(3\pi/5\). As the five edge directions turn uniformly by \(2\pi/5\), the inward bisectors of the five vertex cones are equally spaced by \(2\pi/5\). For any fixed nonzero direction \(u\), the bisectors of the vertices illuminated by \(u\) must lie in an open angular arc of length \(3\pi/5\). Since \(2\pi/5<3\pi/5<4\pi/5\), at most two of the five equally spaced bisectors can fit, and if two fit their vertex indices are adjacent cyclically. Conversely, for every adjacent pair \(\{i,i+1\}\), choosing \(u\) with angle at the midpoint of their bisectors illuminates both: their angular separation is \(2\pi/5\), strictly smaller than the available arc length \(3\pi/5\). Thus the maximal illuminating vertex sets of either factor are exactly the five adjacent pairs.

Each pentagon consequently requires at least \(\lceil5/2\rceil=3\) directions. Three adjacent-pair directions plainly cover all five vertices, and hence all boundary points by the active-facet argument below. Therefore \(I(P)=I(Q)=3\).

**2. Reduction to cyclic \(2\times2\) tiles.** A product direction \((u,v)\in\mathbb R^2\times\mathbb R^2\) illuminates \((p_i,q_j)\) if and only if \(u\) illuminates \(p_i\) and \(v\) illuminates \(q_j\). Indeed, \(\operatorname{int}(P\times Q)=\operatorname{int}P\times\operatorname{int}Q\); if entry holds at possibly different positive step lengths in the factors, taking the smaller step yields entry in both by convexity. Conversely, product entry implies factor entry. The zero vector in either factor illuminates no vertex.

By step 1, each product direction illuminates at most four product vertices, belonging to a cyclic tile
\[
T_{a,b}=\{(a,b),(a+1,b),(a,b+1),(a+1,b+1)\},
\qquad (a,b)\in(\mathbb Z/5\mathbb Z)^2.
\]
Every such maximal tile is actually realized by a product direction, by independently choosing directions that illuminate the prescribed adjacent pairs of \(P\) and \(Q\). Every other direction's vertex set is contained in one of these tiles. Consequently both illumination optimizations may be performed over these 25 tiles without loss.

**3. Ordinary lower bound.** Fix the first-coordinate row \(i\). Its five product vertices must be covered. Any tile meeting this row covers exactly two of its five second-coordinate vertices. Therefore at least three chosen tiles meet each row. Summing over the five rows requires at least 15 row–tile incidences. Each tile meets exactly two rows. If \(N\) directions illuminate the entire product, extend each illuminated set to a containing tile and count these incidences: \(2N\ge15\), so \(N\ge8\). This argument covers arbitrary real directions, including nongeneric or critical directions.

**4. Ordinary upper bound.** Choose one realizing direction for each of the eight tiles
\[
T_{0,0},\ T_{0,2},\ T_{1,3},\ T_{2,0},\ T_{2,2},\ T_{3,1},\ T_{3,3},\ T_{4,4}.
\]
Direct modular incidence counting gives the following exact coverage multiplicities, row by row, in second-coordinate order \(0,1,2,3,4\):
\[
(2,1,1,1,1),\quad (1,1,1,2,1),\quad (1,1,1,2,1),\quad
(1,2,2,2,1),\quad (1,1,1,1,2).
\]
Every vertex is covered. For completeness, let \(x\) be any point in the relative interior of a face \(F\) of the product polytope, and choose a vertex \(z\in F\). Every facet inequality active at \(x\) is also active at \(z\). A direction that points strictly inward at every active facet through \(z\) also does so at \(x\), so any direction illuminating \(z\) illuminates \(x\). Thus covering the vertices covers the whole boundary. Combining with step 3 yields \(I(K)=8\).

**5. Sharp fractional value.** For any finite weighted collection of directions, sum its illumination constraints over all 25 vertices. Each direction illuminates at most four vertices, so its total weight \(W\) satisfies \(25\le4W\), whence \(I^*(K)\ge25/4\). Conversely, assign weight \(1/4\) to one realizing direction for each of the 25 tiles \(T_{a,b}\). Every product vertex \((i,j)\) belongs to exactly four of these tiles (choices \(a=i\) or \(i-1\), independently \(b=j\) or \(j-1\)), so every vertex receives illuminating weight exactly one. The active-facet observation in step 4 extends this inequality to all boundary points. Total weight is \(25/4\), proving \(I^*(K)=25/4\).

All choices of realizing directions use strict inequalities, so neither boundary degeneracies nor arbitrary side lengths affect the argument.

## Verification
Run `python3 verify.py`. This standalone exact-integer/fraction checker defines all 25 cyclic tiles, confirms the eight specified tiles cover all 25 vertices with the five multiplicity rows above, derives the row-count bound eight, and checks the full 25-tile fractional coverage at exact weight \(1/4\) per tile. It also verifies that the 25 maximal incidence patterns are distinct. Output:

`EXACT_OK: cells=25 tiles=25 selected=8 row_bound=8 fractional=25/4 rows=[(2, 1, 1, 1, 1), (1, 1, 1, 2, 1), (1, 1, 1, 2, 1), (1, 2, 2, 2, 1), (1, 1, 1, 1, 2)]`

The checker certifies a finite combinatorial subproblem, not the continuous normal-fan reduction. That reduction and the validity for all equiangular pentagons are proved analytically in steps 1–2. The lower bounds in steps 3 and 5 quantify over all possible directions, not only the finite witness set.

## Relationship to prior work
Naszódi introduced fractional illumination and supplied the original weighted-direction framework, including a regular-pentagon lower bound. Sriamorn computed multiple illumination numbers of regular polygons, giving the ordinary pentagon value three as a specialization. Gorodzha's September 20, 2026 preprint proves the universal fractional illumination upper bound \(2^d\) and motivates exact finite-dimensional values; it gives no Cartesian-product pentagon evaluation.

Recent exact evaluations for equiangular polygons establish the planar fractional value \(5/2\), while the result on Cartesian products of simplices establishes an exact formula for simplex factors. Neither covers a four-dimensional product of two pentagons, and neither implies the eight-tile construction or exact product fractional value. The latter paper explicitly limits its theorem to products of simplices. A separate multiple-illumination study concerns planar polygons with antipodally paired normals, which cannot describe a pentagon. The present result concerns a non-simplex product in four dimensions and shows that ordinary illumination need not multiply with the factors' ordinary illumination numbers.

## Limitations
The exact product result is proved for two equiangular pentagons; no formula is asserted for arbitrary polygon pairs or for three or more polygon factors. The fractional number of the product happens to equal the product of its factors' known fractional values, but no general fractional-product theorem is claimed. The eight specified 2-by-2 tiles provide one optimum, not a classification of every optimum ordinary cover. Neither historical uniqueness nor independent mathematical validation is asserted; an older result on covering finite cyclic grids or illumination products under different terminology remains a priority risk.

## References
1. Y. Gorodzha, *Fractional illumination and the optimal exponential rate in Hadwiger's covering conjecture*, arXiv:2609.23913v1, submitted September 20, 2026, https://arxiv.org/abs/2609.23913.
2. K. Sriamorn, *On the multiple illumination numbers of convex bodies*, arXiv:2306.13517v1, June 23, 2023, https://arxiv.org/abs/2306.13517.
3. M. Naszódi, *Fractional illumination of convex bodies*, *Contributions to Discrete Mathematics* **4** (2009), 83–88, https://doi.org/10.55016/ojs/cdm.v4i2.62022.
4. *Exact fractional illumination of every equiangular polygon*, publicly available proof, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-fractional-illumination-of-every-equiangular-polygon--035cb636082a.
5. *Exact ordinary and fractional illumination of every product of simplices*, publicly available proof, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-ordinary-and-fractional-illumination-of-every-product-of-s--24a86928f4ea.
6. *Exact multiple illumination and parity rigidity for polygons with antipodal edge-normal fans*, publicly available proof, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-multiple-illumination-and-parity-rigidity-for-polygons-wit--f4e6962728dc.
