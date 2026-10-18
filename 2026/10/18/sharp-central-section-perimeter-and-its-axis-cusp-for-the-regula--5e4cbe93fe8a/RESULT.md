# Sharp central-section perimeter and its axis cusp for the regular rhombic dodecahedron

## Finding

Let
\[
K=\{x\in\mathbb R^3:|x_i|+|x_j|\le2\text{ for }1\le i<j\le3\}
\]
be the regular rhombic dodecahedron. For every unit normal \(n\in S^2\), let \(P(n)\) be the intrinsic Euclidean perimeter of the central section \(K\cap n^\perp\), counted along its planar polygon boundary. Then
\[
\boxed{P(n)\le 8\sqrt2,}
\]
with equality **exactly** for the six coordinate-axis normals. More strongly, the global directional deficit obeys the explicit strict-away-from-axes estimate
\[
\boxed{8\sqrt2-P(n)\ge \frac4{3\sqrt3}\bigl(n_1^2n_2^2+n_1^2n_3^2+n_2^2n_3^2\bigr).}
\]

The maximum has a first-order, direction-dependent cusp. For every \(p^2+q^2=1\) and every sufficiently small \(\delta\ge0\), uniformly in \((p,q)\), put \(n_\delta=(\sqrt{1-\delta^2},\delta p,\delta q)\). Then
\[
\boxed{P(n_\delta)=8\sqrt2-8(\sqrt2-1)(|p|+|q|)\delta+O(\delta^2).}
\]
In particular \(P\), as a function on the sphere, is not differentiable at any maximizing coordinate normal.

The complete directional perimeter function is also elementary. Let \(a\ge b\ge c\ge0\) be the decreasing rearrangement of \((|n_1|,|n_2|,|n_3|)\), without requiring unit normalization, and \(S=a+b+c\). In the six-sided chamber \(a\le b+c\),
\[
\boxed{P_6(a,b,c)=\frac4S\!\left[\sqrt{2a^2+(b+c)^2}+\sqrt{2b^2+(a+c)^2}+\sqrt{2c^2+(a+b)^2}\right].}
\]
In the eight-sided chamber \(a>b+c\),
\[
\begin{aligned}
P_8(a,b,c)={}&\frac{4\sqrt{2a^2+(b+c)^2}}S
+\frac{8b\sqrt{(a+b)^2+2c^2}}{(a+b-c)S}\\
&+\frac{4(a-b-c)\sqrt{2a^2+(b-c)^2}}{(a+b-c)(a-b+c)}
+\frac{8c\sqrt{(a+c)^2+2b^2}}{(a-b+c)S}.
\end{aligned}
\]
The functions agree continuously along \(a=b+c\). Within the closed six-sided chamber the sharp range is
\[
\boxed{4\sqrt6\le P(n)\le 4(1+\sqrt3).}
\]
Equality on the left occurs exactly for body-diagonal normals, and equality on the right exactly for face-diagonal normals, up to signs and permutations. This last interval is asserted **only for the six-sided chamber**; the global maximum above applies to both chambers.

## Assumptions and scope

All perimeter measurements are intrinsic to a plane through the center; this is not the perimeter of an orthogonal shadow and not the area of a section. Every nonzero normal is allowed in the two explicit directional formulas, and the extremal assertions use unit normals. The eight-sided chamber allows zeros in the smaller coordinates; at coordinate normals the polygon has four sides and the displayed expression is understood by its direct, nonsingular value. Additional boundary degeneracies follow by continuity. Multiplication of the body by a positive scalar multiplies all perimeters by that scalar. A large-sample numerical test is not part of the logical continuum proof.

## Proof

**1. A tetrahedral-generator description.** Put
\[
 u_1=(1,1,1),\quad u_2=(1,-1,-1),\quad u_3=(-1,1,-1),\quad u_4=(-1,-1,1).
\]
The body has exactly the fourteen vertices \(\{(\pm1,\pm1,\pm1)\}\cup\{\pm2e_1,\pm2e_2,\pm2e_3\}\). The support function evaluated on this vertex set is
\[
 h_K(z)=\max\{|z_1|+|z_2|+|z_3|,\ 2\max_i|z_i|\}.
\]
Sorting the absolute coordinates of \(z\) and checking the signs of the four dot products gives
\[
 h_K(z)=\frac12\sum_{j=1}^{4}|u_j\cdot z|.
\]
By uniqueness of support functions, \(K=\sum_{j=1}^{4}[-u_j/2,u_j/2]\), a Minkowski sum of four segments.

**2. Sharp maximum from a projection envelope.** Fix \(n\in S^2\), let \(H=n^\perp\), and denote by \(\pi_H\) orthogonal projection onto \(H\). Cauchy's planar perimeter formula \(\operatorname{Per}(C)=\int_0^\pi w_C(\theta)\,d\theta\) shows that perimeter is monotone under planar convex-set inclusion. Thus
\[
 P(n)=\operatorname{Per}(K\cap H)\le\operatorname{Per}(\pi_HK).
\]
The perimeter of a planar zonogon is twice the sum of its (full) segment-generator lengths, hence
\[
 \operatorname{Per}(\pi_HK)=2\sum_{j=1}^{4}\|\pi_Hu_j\|_2
 =2\sum_{j=1}^{4}\sqrt{3-(u_j\cdot n)^2}.
\]
Write \(q_j=(u_j\cdot n)^2\). The tight-frame identities \(\sum_j u_ju_j^\mathsf T=4I_3\) and \(\sum_j q_j=4\) give, by strict concavity of the square root,
\[
 \operatorname{Per}(\pi_HK)\le 2\cdot4\sqrt{3-\tfrac14\sum_jq_j}=8\sqrt2.
\]
For the strengthened deficit use \(f(t)=\sqrt{3-t}\), which has \(f''(t)=-1/[4(3-t)^{3/2}]\le-1/(12\sqrt3)\) for \(0\le t<3\), and extend its strong-concavity inequality by continuity at \(t=3\). Taylor's inequality about the mean \(\overline q=1\), summed over four terms, yields
\[
 8\sqrt2-\operatorname{Per}(\pi_HK)
 \ge\frac1{12\sqrt3}\sum_{j=1}^{4}(q_j-1)^2.
\]
Directly expanding the four tetrahedral forms gives the exact identities
\[
 \sum_j(u_j\cdot n)^4
 =4+16\sum_{i<j}n_i^2n_j^2,\qquad
 \sum_j(q_j-1)^2=16\sum_{i<j}n_i^2n_j^2.
\]
Combining these equations proves the stated \(4/(3\sqrt3)\) deficit bound. Equality in the upper bound forces all \(q_j=1\), hence \(n_i n_j=0\) for all unequal \(i,j\). Thus \(n\) is a signed coordinate vector. Conversely, when \(n=e_1\), the projected body and the central section coincide and are the diamond with vertices \((0,\pm2,0)\), \((0,0,\pm2)\), of perimeter \(8\sqrt2\). Symmetry covers all six coordinate normals. This completes the sharp maximum and equality classification.

**3. Exact section edge lengths.** The twenty-four edges of \(K\) join each cube vertex \(v=(s_1,s_2,s_3)\), where \(s_i\in\{-1,1\}\), to the three axis vertices \(w=2s_ie_i\). A generic central plane cuts this edge precisely when \((n\cdot v)(n\cdot w)<0\). For \(s=n\cdot v\), \(t=n\cdot w\), the intersection point is
\[
 p(v,w)=\frac{t v-s w}{t-s}.
\]
The following exhaustive cyclic edge lists use notation `v -> w` for that unique crossing point. They apply after signed-permutation symmetry puts the normal in the generic region \(a>b>c>0\); list positions are cyclic in the section plane. Each list is repeated by central symmetry after halfway round.

When \(a>b+c\), the eight points in cyclic order are

```
( 1, 1,-1) -> ( 0, 0,-2)
(-1, 1,-1) -> ( 0, 2, 0)
(-1, 1, 1) -> ( 0, 2, 0)
(-1, 1, 1) -> ( 0, 0, 2)
(-1,-1, 1) -> ( 0, 0, 2)
( 1,-1, 1) -> ( 0,-2, 0)
( 1,-1,-1) -> ( 0,-2, 0)
( 1,-1,-1) -> ( 0, 0,-2)
```

When \(a<b+c\), the six points in cyclic order are

```
( 1, 1,-1) -> ( 0, 0,-2)
(-1, 1,-1) -> ( 0, 2, 0)
(-1, 1, 1) -> (-2, 0, 0)
(-1,-1, 1) -> ( 0, 0, 2)
( 1,-1, 1) -> ( 0,-2, 0)
( 1,-1,-1) -> ( 2, 0, 0)
```

Substituting each pair into \(p(v,w)\), subtracting consecutive vectors and summing their Euclidean lengths gives exactly the two displayed expressions \(P_8\) and \(P_6\). The cyclic descriptions also verify that all faces are accounted for; no unexamined section edges remain. Both expressions are invariant under common rescaling of \((a,b,c)\); degeneracies follow from continuity of perimeter for convergent planar convex sections.

**4. The six-sided sharp interval.** In this chamber put \(x_i=|n_i|/S\). Then \(x_i\ge0\), \(\sum_i x_i=1\) and \(\max_i x_i\le1/2\). The formula simplifies to
\[
 P_6=4\sum_{i=1}^3 f(x_i),\qquad f(x)=\sqrt{3x^2-2x+1}.
\]
Since \(f''(x)=2/(3x^2-2x+1)^{3/2}>0\), strict Jensen yields the minimum at \((1/3,1/3,1/3)\), equal to \(4\sqrt6\). A convex function attains its maximum on the clipped simplex \(\{x_i\ge0,\sum x_i=1,\max x_i\le1/2\}\) at a vertex, and its only vertices are the permutations of \((1/2,1/2,0)\). The maximum is therefore \(4(1+\sqrt3)\). Strict convexity excludes any other equality cases.

**5. Local cusp at each maximizer.** In the eight-sided formula set \(a=1\), \(b=\delta|p|/\sqrt{1-\delta^2}\), \(c=\delta|q|/\sqrt{1-\delta^2}\), interchanging \(b,c\) if needed. Direct differentiation of the displayed rational-square-root expression at \((b,c)=(0,0)\) gives
\[
 P_8(1,b,c)=8\sqrt2-8(\sqrt2-1)(b+c)+O((b+c)^2).
\]
The denominators stay bounded away from zero on a fixed neighborhood, so the remainder is uniform in tangent direction. The stated expansion follows. The one-sided directional derivative in the tangent direction \((p,q)\) is \(-8(\sqrt2-1)(|p|+|q|)\), which cannot arise from a linear tangent differential; hence \(P\) is not differentiable at a maximizing axis normal.

## Verification

The accompanying standalone Python 3 checker reconstructs each section from the full twenty-four-edge list, projects the intersection points to an orthonormal planar basis, and computes the independent convex-hull perimeter using the monotone-chain algorithm. For 3,200 deterministic generic directions, it compares this geometric calculation to the closed formulas, checks the six/eight edge count, the global upper inequality, the projection envelope and the explicit quantitative deficit. It also tests exact special orientations and the local first-order coefficient at several tangent directions and scales. The maximum observed absolute difference between the independently constructed perimeter and the closed formula is approximately \(5.33\times10^{-15}\). The algebraic identities, tight-frame Jensen proof and exhaustive geometric edge construction—not finite tests—prove the all-direction theorem. Run `python verify_rhombic_perimeter.py` from the directory containing the extracted artifact.

## Relationship to prior work

The rhombic dodecahedron is the face-centered-cubic lattice Voronoi cell. Hausel, Makai and Szűcs (1999) prove inscribed-cube existence and a universal-cover property involving this body, rather than sharp intrinsic section perimeters. König and Koldobsky (2018) prove a sharp perimeter inequality for central sections of **cubes**, a different polytope whose maximizing normal is face-diagonal rather than coordinate-axis. Leppmeier (2019) compares lattice-cell and tessellation-tetrahedron volumes, not planar boundary lengths. Standard Cauchy perimeter and zonotope formulas are explicitly treated as known tools, not claimed as new. A separate directional *section-area* treatment of the rhombic dodecahedron gives polygon crossing data; area itself does not imply the present sharp perimeter inequality, tetrahedral-frame deficit or coordinate-axis nonsmooth response. The edge-length formulas can be computed from known crossing data and are not independently claimed as an invention of a new polygon-construction method.

## Limitations

The body must be the specified regular rhombic dodecahedron and the plane central. The sharp \(4\sqrt6\) lower and \(4(1+\sqrt3)\) upper bounds stated within the six-sided chamber are not presented as a global lower classification over the eight-sided chamber. No arbitrary affine deformation, translated section, or higher-dimensional generalization is asserted. The quantitative global deficit is valid but is not claimed to have the best possible coefficient. Earlier general geometric tools and possible uncatalogued precise special-case formulas pose historical-priority risk. Independent mathematical validation has not been performed.

## References

1. T. Hausel, E. Makai Jr., A. Szűcs, *Inscribing cubes and covering by rhombic dodecahedra via equivariant topology*, arXiv:math/9906066, first public 1999-06-10, https://arxiv.org/abs/math/9906066.
2. H. König and A. Koldobsky, *On the maximal perimeter of sections of the cube*, arXiv:1806.08659, first public 2018-06-22, https://arxiv.org/html/1806.08659v1.
3. M. Leppmeier, *The Dodecahedron as a Voronoi Cell and its (minor) importance for the Kepler conjecture*, 2019, https://epub.uni-bayreuth.de/id/eprint/4313/1/Paper_Dodekaeder_Entwurf_B8.pdf.
