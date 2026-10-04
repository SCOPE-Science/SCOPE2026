# Order-2 Delaunay minimizes maximum enclosing-circle radius

## Finding

Let \(A\subset\mathbb{R}^2\) be a finite generic set with \(\#A\ge 4\), meaning that no three points are collinear and no four are cocircular. For a Euclidean triangle \(T\), let \(r(T)\) be the radius of its smallest enclosing circle. For an ordinary triangulation or a level-2 hypertriangulation \(Q\), define its enclosing-circle coarseness by
\[
c(Q)=\max_{T\in Q} r(T).
\]
Then the order-2 Delaunay hypertriangulation \(\operatorname{Del}_2(A)\) minimizes \(c\) among all complete level-2 hypertriangulations of \(A\):
\[
c(H)\ge c\!\left(\operatorname{Del}_2(A)\right)
\]
for every complete level-2 hypertriangulation \(H\) of \(A\).

The proof gives an exact reduction. Let \(P\) be the unique complete ordinary triangulation whose triangles age to the black triangles of \(H\). For each \(x\in A\), replace the star of \(x\) in \(P\) by the original-scale copies of the white triangles of \(H\) whose labels all contain \(x\); call the resulting triangulation of \(A\setminus\{x\}\) by \(P^{-x}\). Then
\[
2c(H)=\max\!\left(c(P),\max_{x\in A}c(P^{-x})\right).
\]
For the order-2 Delaunay hypertriangulation, the corresponding ordinary triangulations are exactly \(\operatorname{Del}(A)\) and \(\operatorname{Del}(A\setminus\{x\})\). Thus the higher-order minimization separates into \(\#A+1\) ordinary Delaunay minimax problems.

## Assumptions and scope

The competing objects are **complete** level-2 hypertriangulations of a finite generic planar point set. Completeness is the same competitor class used for the angle-vector optimality theorem of Edelsbrunner, Garber, and Saghafian. No assertion is made for incomplete or merely maximal competitors, and no assertion is made for levels \(k\ge 3\).

The functional is the direct geometric analogue of Rajan's min-containment functional: each hypertriangle is treated as an actual Euclidean triangle at its pair-average coordinates, and its smallest enclosing circle is measured there. The claim concerns the maximum such radius, not the list of all radii and not the circumradius when the smallest enclosing circle is supported by a longest edge.

## Proof

Write the vertices of level-2 hypertriangulations as pair averages \([ab]=(a+b)/2\). By the aging theorem for planar hypertriangulations, every level-2 hypertriangulation has a unique underlying level-1 triangulation \(P\). If \(H\) is complete, then \(P\) is a complete triangulation of \(A\). Its black hypertriangles have vertices
\[
[ab],\ [ac],\ [bc]
\]
for ordinary triangles \(abc\in P\). This is the medial triangle of \(abc\), hence it is similar to \(abc\) with linear scale \(1/2\). A white hypertriangle rooted at \(x\) has vertices
\[
[xa],\ [xb],\ [xc],
\]
so it is a translate of the triangle \(abc\) scaled by \(1/2\). Therefore the smallest-enclosing-circle radius of every hypertriangle is exactly one half the corresponding original-scale triangle radius.

Fix \(x\in A\). The white triangles rooted at \(x\), scaled back to the original points, triangulate the white region
\[
\operatorname{wh}(P,x)=\operatorname{st}(P,x)\cap\operatorname{conv}(A\setminus\{x\}).
\]
Together with the triangles of \(P\) not incident to \(x\), they form an edge-to-edge complete triangulation \(P^{-x}\) of \(A\setminus\{x\}\): outside the star nothing changes, while inside \(\operatorname{conv}(A\setminus\{x\})\) the portion of the deleted star is exactly \(\operatorname{wh}(P,x)\). This remains true when \(x\) is a convex-hull vertex because the intersection with \(\operatorname{conv}(A\setminus\{x\})\) removes precisely the corner cut off by deleting \(x\).

Every original-scale counterpart of a black hypertriangle lies in \(P\), and every original-scale counterpart of a white hypertriangle rooted at \(x\) lies in \(P^{-x}\). Conversely, every triangle newly filling \(P^{-x}\) is one of those white counterparts. Hence, after accounting for the common scale factor \(1/2\),
\[
2c(H)=\max\!\left(c(P),\max_{x\in A}c(P^{-x})\right). \tag{1}
\]

Now specialize to \(H=\operatorname{Del}_2(A)\). At level \(2\), a black triangle corresponding to \(abc\) has no point of \(A\) inside the circumcircle of \(abc\), so the black original-scale triangles are exactly \(\operatorname{Del}(A)\). A white triangle rooted at \(x\) corresponds to \(abc\) whose circumcircle contains exactly \(x\) from \(A\setminus\{a,b,c\}\). After deleting \(x\), that circle is empty. Conversely, if \(abc\) is a Delaunay triangle of \(A\setminus\{x\}\), genericity implies that \(x\) is strictly outside or strictly inside its circumcircle. In the first case \(abc\) is already a Delaunay triangle of \(A\); in the second it is exactly a white order-2 triangle rooted at \(x\). Therefore
\[
P=\operatorname{Del}(A),\qquad P^{-x}=\operatorname{Del}(A\setminus\{x\})
\]
for every \(x\in A\). Substituting into (1) gives
\[
2c\!\left(\operatorname{Del}_2(A)\right)=
\max\!\left(c(\operatorname{Del}(A)),\max_{x\in A}c(\operatorname{Del}(A\setminus\{x\}))\right). \tag{2}
\]

Rajan's theorem says that the ordinary Delaunay triangulation minimizes the maximum smallest-enclosing-circle radius among triangulations of the same point set. Apply it once to \(A\) and once to each \(A\setminus\{x\}\):
\[
c(P)\ge c(\operatorname{Del}(A)),\qquad
c(P^{-x})\ge c(\operatorname{Del}(A\setminus\{x\})).
\]
Taking the maximum over these \(\#A+1\) inequalities and using (1) and (2) proves
\[
c(H)\ge c\!\left(\operatorname{Del}_2(A)\right).
\]

## Verification

The proof has three independently checkable components. First, the aging structure and the white-region description are exactly the level-1-to-level-2 structure established in the hypertriangulation literature. Second, the pair-average coordinates give literal homotheties of ratio \(1/2\), so the radius scaling is exact and needs no numerical approximation. Third, the order-2 empty-circle condition decomposes into the ordinary empty-circle conditions on \(A\) and on each one-point deletion \(A\setminus\{x\}\), after which Rajan's minimax theorem applies separately.

Boundary cases were checked in the proof rather than suppressed: for a convex-hull vertex \(x\), the white region is the intersection of its star with \(\operatorname{conv}(A\setminus\{x\})\); genericity rules out the ambiguous case in which \(x\) lies on the circumcircle of a Delaunay triangle of \(A\setminus\{x\}\). The assumption \(\#A\ge 4\) ensures that every one-point deletion still admits an ordinary planar triangulation.

## Relationship to prior work

Edelsbrunner, Garber, and Saghafian prove angle-vector and local-angle optimality for order-2 Delaunay hypertriangulations. In their concluding remarks they explicitly ask whether other order-1 optimality properties generalize to higher levels and list the **smallest enclosing circle** property as an example. Their structural results also provide the aging and white-region facts used here, but they do not state the minimax theorem above.

Rajan proves the ordinary Delaunay theorem that minimizes the maximum min-containment radius. The present result is not a special case of Rajan's theorem because a level-2 hypertriangulation is a triangulation of pair averages subject to hypersimplicial label constraints. The new step is the exact deletion decomposition (1), which reduces every complete level-2 competitor to one triangulation of \(A\) and one triangulation of every one-point deletion, allowing Rajan's theorem to be applied componentwise.

Edelsbrunner and Osang define a radius function on the order-\(k\) Delaunay mosaic for higher-order alpha shapes. That radius is attached to rhomboids via constrained spheres and is not an extremal comparison over arbitrary complete level-2 hypertriangulations. The later flip-connectivity paper of Edelsbrunner, Garber, Ghafari, Heiss, and Saghafian likewise studies connectivity by flips and does not state an enclosing-circle minimization theorem.

## Limitations

The result does not show uniqueness of the minimizer; Rajan's ordinary minimax theorem itself can have ties in the objective. It does not compare incomplete level-2 hypertriangulations, whose underlying point usage can differ, and it does not extend automatically to \(k\ge 3\) because the level-2 deletion decomposition relies on the special form of black and white triangles and on the universal aging map from level \(1\) to level \(2\).

The originality assessment is based on targeted published-finding corpus searches, exact-phrase and semantic web searches, and inspection of the most directly relevant primary sources. Since the proof is short and structural, an equivalent observation could exist under different terminology; that residual risk is recorded rather than treated as a novelty proof.

## References

H. Edelsbrunner, A. Garber, and M. Saghafian, “Order-2 Delaunay Triangulations Optimize Angles,” arXiv:2310.18238, first submitted 2023-10-27; published in Advances in Mathematics 461 (2025), 110055.

V. T. Rajan, “Optimality of the Delaunay Triangulation in \(\mathbb{R}^d\),” Discrete & Computational Geometry 12 (1994), 189–202, DOI 10.1007/BF02574375.

H. Edelsbrunner and G. Osang, “A Simple Algorithm for Higher-Order Delaunay Mosaics and Alpha Shapes,” Algorithmica 85 (2023), 277–295, DOI 10.1007/s00453-022-01027-6.

H. Edelsbrunner, A. Garber, M. Ghafari, T. Heiss, and M. Saghafian, “Flips in Two-Dimensional Hypertriangulations,” arXiv:2212.11380, version dated 2025-09-25; published in European Journal of Combinatorics 132 (2026), 104248.
