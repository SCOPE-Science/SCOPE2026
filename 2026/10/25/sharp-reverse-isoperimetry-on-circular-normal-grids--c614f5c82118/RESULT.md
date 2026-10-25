# Sharp reverse isoperimetry on circular normal grids

## Finding
Fix an integer \(N\ge3\), a perimeter \(P>0\), and the outward-normal grid
\[
U_N=\{(\cos(2\pi j/N),\sin(2\pi j/N)):j=0,\ldots,N-1\}.
\]
Let \(\mathcal G_N(P)\) be the full-dimensional convex polygons of perimeter \(P\) whose outward edge normals belong to \(U_N\); not every grid normal has to occur.

If \(N\) is odd, the complete sharp area interval is
\[
\boxed{\frac{P^2}{4\bigl(2\cot(\pi/(2N))+\tan(\pi/N)\bigr)}
\ \le\ \operatorname{area}(K)\ \le\ \frac{P^2}{4N\tan(\pi/N)}.}
\]
The lower-bound equality cases are precisely the \(N\) rotated (and freely translated) isosceles triangles with angles \(\pi/N,\pi/N,\pi-2\pi/N\); their outward-normal gaps are \((1,(N-1)/2,(N-1)/2)\) grid steps, cyclically ordered. The upper-bound equality case is the regular \(N\)-gon with outward normals \(U_N\), up to translation. Every area between the bounds occurs.

For even \(N\ge4\), the sharp area set is
\[
0<\operatorname{area}(K)\le \frac{P^2}{4N\tan(\pi/N)}.
\]
Its lower infimum zero is not attained by a full-dimensional polygon, but is approached by flattening a parallelogram using two antipodal pairs from \(U_N\). All intermediate areas occur. For odd \(N\to\infty\), with \(P\) held fixed, the sharp lower endpoint has the expansion
\[
\frac{P^2\pi}{16N}-\frac{P^2\pi^3}{96N^3}+O(P^2N^{-5}).
\]

## Assumptions and scope
Polygons are compact, convex, and full-dimensional in the Euclidean plane; translation does not change the questions. Their edges are allowed to have zero length in an auxiliary surface-area-measure parametrization, in which case that facet is absent from the resulting polygon. The fixed outward-normal grid is as displayed, without arbitrary rotations between different polygons. The theorem is not an assertion about arbitrary \(N\)-gons or about polygons with prescribed edge *lengths*.

## Proof
**1. The surface-area-measure polytope.** For a polygon \(K\) set \(\ell_j\ge0\) equal to its edge length at normal \(u_j\), or zero if absent. Closedness of the polygonal edge vector sequence gives \(\sum_j\ell_j u_j=0\), and perimeter gives \(\sum_j\ell_j=P\). Hence the admissible length vector lies in the compact polytope
\[
C_N(P)=\{\ell\in\mathbb R_{\ge0}^N:\sum_j\ell_j=P,\ \sum_j\ell_j u_j=0\}.
\]
Conversely, when \(N\) is odd, any such vector has normals not confined to a closed semicircle: otherwise the balancing vector would require a pair of antipodal positive-mass normals, impossible on an odd grid. Minkowski's planar polygon theorem therefore produces a unique full-dimensional polygon up to translation, of perimeter \(P\), with precisely this surface-area measure. For even \(N\), all interior vectors and the nondegenerate boundary vectors also yield polygons, while vectors supported on one antipodal pair describe limiting collapsed configurations.

**2. Reduction to triangles for odd \(N\).** In the plane, the surface-area measure is additive under Minkowski addition. Thus if \(\ell=t\ell^{(1)}+(1-t)\ell^{(2)}\), its polygon is, up to translation, \(tK_1+(1-t)K_2\). Brunn--Minkowski makes \(\sqrt{\operatorname{area}}\) concave on \(C_N(P)\). Consequently its minimum occurs at a vertex of that polytope. Every vertex has at most three positive coordinates, since \(C_N(P)\) is cut out by three independent affine constraints. At least three are necessary because an odd grid contains no antipodal pair. Such a vertex is therefore a triangle; its three normals must surround the origin and every successive normal gap is strictly below \(\pi\).

Moreover the Brunn--Minkowski equality condition shows that a nontrivial mixture of different such vertices has *strictly greater* area than the common minimum: equality would require the constituent polygons to be homothetic, and fixed perimeter would make them translates with identical length vectors. This proves that all minimizers themselves must be vertices.

**3. Discrete angle classification.** Order the three outward normals cyclically. Their successive angular gaps are \(2\pi k_i/N\), with positive integers \(k_i<N/2\) and \(k_1+k_2+k_3=N\). The interior triangle angles are \(A_i=\pi-2\pi k_i/N\). When \(N\) is odd, write \(a_i=N-2k_i\); these are positive odd integers with \(a_1+a_2+a_3=N\), and \(A_i=\pi a_i/N\).

**4. Exact triangular area.** Every triangle with perimeter \(P\) and interior angles \(A_1,A_2,A_3\) has inradius \(r=P/(2\sum_i\cot(A_i/2))\): each vertex contributes tangent length \(r\cot(A_i/2)\) to each incident edge. Since area is \(Pr/2\),
\[
\operatorname{area}(T)=\frac{P^2}{4\sum_{i=1}^3\cot(A_i/2)}.
\]
The function \(z\mapsto\cot z\) is strictly convex for \(0<z<\pi/2\), because its second derivative is \(2\cot z\csc^2z>0\). Therefore on positive odd triples \(a_1+a_2+a_3=N\), the denominator is uniquely maximized, up to permutation, by \((a_1,a_2,a_3)=(1,1,N-2)\): transferring two units from a smaller coordinate to a larger one strictly raises the sum until two coordinates are one. This gives the lower endpoint and exactly the stated normal-gap triples. When \(N=3\), this is the single possible triple, consistently yielding the equilateral triangle.

**5. Sharp maximum.** The classical polygonal isoperimetric inequality gives \(\operatorname{area}(K)\le P^2/(4m\tan(\pi/m))\) for a convex \(m\)-gon, with equality exactly for a regular \(m\)-gon. This bound increases strictly with \(m\ge3\), and \(m\le N\). Thus it gives the displayed upper bound; the regular grid polygon realizes equality.

**6. Even grids and the full ranges.** For even \(N\ge4\), choose any two distinct antipodal normal pairs from the grid. Parallelograms with the corresponding four outward normals and positive opposite side lengths have perimeter \(P\). One side-length pair may tend to zero while the other remains positive, so their areas tend to zero. All full-dimensional polygons have strictly positive area. The upper bound from Step 5 remains sharp. Finally, Minkowski interpolation between any two polygons of equal perimeter and grid normals remains in the same family and changes area continuously. This proves that every intermediate area in either stated interval is realized.

**7. Expansion.** Put \(u=\pi/(2N)\). A trigonometric simplification gives the odd-grid minimum as
\[
A_{\min}=\frac{P^2}{8}\frac{\sin u\cos(2u)}{\cos^3u}.
\]
Expanding the analytic factor gives \(\sin u\cos(2u)/\cos^3u=u-2u^3/3+O(u^5)\), and hence the claimed two-term asymptotic.

## Verification
Run `python3 verify_grid_area.py` using Python 3 and its standard library. The standalone script enumerates all admissible three-normal supports for odd grids from \(N=3\) to \(43\), reconstructs each polygon independently from its directed edges, compares shoelace area with the inradius formula, and verifies the complete equality orbit. It additionally tests random Minkowski mixtures, the polygonal maximum, even-grid flattening examples, and the asymptotic expansion. In the checked run, 19,481 triangular supports and 1,260 nonvertex mixtures passed; maximum observed discrepancy of the independent triangular area evaluations was \(2.01\times10^{-16}\). These finite tests are not the proof of any universal assertion; Steps 1--7 are.

## Relationship to prior work
Congpei An, *Gauss--Chebyshev Quadrature, S1-Designs, and the Planar Minkowski Inverse Problem* (arXiv:2610.11814, first posted 2026-10-08), motivates the fixed circular facet-normal grid and develops reconstruction, mixed-area quadrature, and Hausdorff approximation. The present optimization keeps perimeter and the normal grid fixed but lets facet masses vary, determining the previously unidentified sharp **minimum** area and all equality shapes. The maximum-area side follows the classical polygonal isoperimetric theorem, represented here by Bogosel's geometric proof (arXiv:2309.05802), and is not claimed new. Khimshiashvili--Panina--Siersma (arXiv:1805.07521) study area critical points without the finite-normal restriction. Bogosel (arXiv:2402.05648) studies reverse isoperimetry with a containing-disk constraint, not a prescribed normal set. None of the inspected statements implies the odd-grid minimum formula or its parity transition. This is a priority assessment, not a proof of uniqueness in the literature.

## Limitations
Only finite equally spaced normal grids are covered. The claimed lower minimizer for odd grids omits all but three normals; if each grid direction is required to occur with **strictly positive** side length, the same lower bound is an infimum but is not attained unless \(N=3\). For even grids the infimum is zero. No quantitative stability away from extremizers is proved. Possible unindexed classical inequalities for polygons with direction restrictions remain an originality risk. The entire arXiv manuscript of the 2026 motivating source was not accessible during the final literature comparison; its retrieved HTML introduction and initial mathematical sections were read.

## References
1. Congpei An, *Gauss--Chebyshev Quadrature, S1-Designs, and the Planar Minkowski Inverse Problem: A One-Dimensional Model for Design-Induced Convex Geometry*, arXiv:2610.11814, posted 2026-10-08. https://arxiv.org/abs/2610.11814
2. Beniamin Bogosel, *A Geometric proof for the Polygonal Isoperimetric Inequality*, arXiv:2309.05802 (2023). https://arxiv.org/abs/2309.05802
3. Giorgi Khimshiashvili, Gaiane Panina and Dirk Siersma, *Extremal areas of polygons with fixed perimeter*, arXiv:1805.07521 (2018; v2 2019). https://arxiv.org/html/1805.07521v2
4. Beniamin Bogosel, *A reverse isoperimetric inequality for convex shapes with inclusion constraint*, arXiv:2402.05648 (2024). https://arxiv.org/abs/2402.05648
5. Rolf Schneider, *Convex Bodies: The Brunn--Minkowski Theory*, 2nd expanded ed., Cambridge University Press, 2014 (planar Minkowski existence and area concavity).
