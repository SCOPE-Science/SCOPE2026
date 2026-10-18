# Sharp tetrahedral rigidity and complete vertex-volume spectrum of the rhombic triacontahedron

## Finding

Put \(\varphi=(1+\sqrt5)/2\). Define the twelve-point set \(I\) by cyclic coordinate permutations of \((0,\pm1,\pm\varphi)\), and the twenty-point set \(D\) by the eight independent sign choices of \((1,1,1)\) together with cyclic permutations of \((0,\pm\varphi,\pm\varphi^{-1})\). The convex hull \(P=\operatorname{conv}(I\cup D)\) is the regular rhombic triacontahedron, normalized so its outer regular icosahedron has edge length \(2\). Its Euclidean volume is \(20\).

**Sharp maximum and complete equality classification.** For every four points \(x_1,x_2,x_3,x_4\in P\),

\[
\operatorname{Vol}_3\bigl(\operatorname{conv}\{x_1,x_2,x_3,x_4\}\bigr)
\le \frac{5+2\sqrt5}{3}.
\]

Exactly twenty unordered tetrahedra attain equality, and **every maximizing tetrahedron has all four vertices at vertices of \(P\)**. Each consists of three points \(u,v,w\in I\) forming an equilateral triangle of side \(2\varphi\), and the uniquely associated point \(-\varphi(u+v+w)\in D\). There are exactly twenty such long equilateral triangles. The sharp volume fraction is \((5+2\sqrt5)/60\).

**Complete discrete spectrum.** Among all \(\binom{32}{4}=35\,960\) unordered four-element subsets of the vertex set, the tetrahedral volumes take exactly **39 distinct values**, including zero. Exactly **2,340** subsets are affinely dependent. The exact multiplicity table appears below; its \(a,b\) columns mean that six times the tetrahedron volume equals \(a+b\varphi\).

| \(a\) | \(b\) | Multiplicity |
|---:|---:|---:|
| 0 | 0 | 2340 |
| -6 | 4 | 360 |
| 4 | -2 | 1460 |
| -2 | 2 | 1920 |
| 8 | -4 | 440 |
| 2 | 0 | 3180 |
| -4 | 4 | 1620 |
| 6 | -2 | 360 |
| 0 | 2 | 3600 |
| -6 | 6 | 60 |
| 4 | 0 | 3450 |
| -2 | 4 | 1680 |
| 8 | -2 | 120 |
| -8 | 8 | 120 |
| 2 | 2 | 2220 |
| -4 | 6 | 300 |
| 6 | 0 | 300 |
| 0 | 4 | 3660 |
| 4 | 2 | 1680 |
| -2 | 6 | 180 |
| 8 | 0 | 670 |
| 2 | 4 | 1440 |
| -4 | 8 | 150 |
| 6 | 2 | 180 |
| 0 | 6 | 420 |
| 4 | 4 | 1640 |
| -2 | 8 | 60 |
| 8 | 2 | 20 |
| 2 | 6 | 720 |
| -4 | 10 | 60 |
| 6 | 4 | 200 |
| 0 | 8 | 240 |
| 4 | 6 | 660 |
| 8 | 4 | 120 |
| 2 | 8 | 120 |
| 6 | 6 | 120 |
| 16 | 0 | 10 |
| 4 | 8 | 60 |
| 6 | 8 | 20 |

## Assumptions and scope

All convex hulls, sections, lengths, and volumes are Euclidean. Signs attached to the two displayed coordinate patterns vary independently, and only **cyclic** permutations of the displayed triples are used. The theorem optimizes over arbitrary four points of the fixed three-dimensional body \(P\), not over convex bodies with freely varying shape. The discrete spectrum concerns distinct vertices only, with the zero-volume case retained. Overall homothetic rescaling multiplies all displayed tetrahedron volumes by the third power of the scale factor.

## Proof

**1. Exact realization and vertices.** Let \(g_1,\ldots,g_6\) be
\[
(0,1,\varphi),\ (0,-1,\varphi),\ (1,\varphi,0),\ (-1,\varphi,0),\ (\varphi,0,1),\ (\varphi,0,-1).
\]
The zonotope \(Z=\sum_{j=1}^6[-g_j,g_j]\) satisfies \(Z=2\varphi P\). Indeed, direct arithmetic in \(\mathbb Z[\varphi]\) shows that its sixty-four signed generator sums are distinct, exactly thirty-two of these are the stretched points of \(I\cup D\), and those thirty-two, but no others, have at least three linearly independent active facet normals. Each of the fifteen unordered generator pairs gives a nonzero distinct normal \(g_i\times g_j\) perpendicular to exactly those two generators. Each corresponding positive and negative supporting face has exactly four of the displayed vertices. A face of a three-dimensional zonotope is two-dimensional only if its normal annihilates at least two independent generators; hence these fifteen normal pairs exhaust the thirty rhombic facets. The vertex-incidence signature is twenty vertices on three facets and twelve vertices on five facets. All assertions in this paragraph are checked with exact equality and determinant tests in the standalone checker.

**2. Volume normalization.** The three-dimensional zonotope volume identity gives
\[
\operatorname{Vol}_3(Z)=8\sum_{1\le i<j<k\le6}\left|\det(g_i,g_j,g_k)\right|.
\]
Its direct twenty-term evaluation in \(\mathbb Z[\varphi]\) equals \(20(2\varphi)^3\). Since \(Z=2\varphi P\), this proves \(\operatorname{Vol}_3(P)=20\). The identity follows from the mixed-volume multilinearity of Minkowski sums of segments, or by partitioning a generic three-zonotope into parallelotopes indexed by independent generator triples.

**3. Exhaustive exact determinant lemma.** For vertices \(a,b,c,d\), write \(\Delta(a,b,c,d)=|\det(b-a,c-a,d-a)|\), so the tetrahedral volume is \(\Delta/6\). The accompanying standalone code constructs the exact thirty-two-point set from the displayed formulas and enumerates all \(\binom{32}{4}=35\,960\) unordered quadruples **without sampling**. It works in \(\mathbb Z[\varphi]\) as pairs of integers \((r,s)\) representing \(r+s\varphi\), uses only the relation \(\varphi^2=\varphi+1\), and compares signs exactly by squaring rational integers against five. The resulting histogram is the complete table above; its entries sum to \(35\,960\), there are exactly thirty-nine levels, the zero level occurs \(2\,340\) times, and the unique largest determinant level is \(6+8\varphi=10+4\sqrt5\), of multiplicity twenty. This is a finite exhaustive calculation supplying an exact, reproducible proof of the finite lemma; floating-point experiments play no role.

**4. Geometric form and rigidity of maximizers.** Direct exact tests on the twenty quadruples at that largest level show that each has precisely three vertices in \(I\), one in \(D\), the three pairwise squared lengths in \(I\) are all \(4\varphi^2\), and the fourth vertex is exactly \(-\varphi\) times their vector sum. Conversely the checker exhausts all triples of \(I\) and finds precisely twenty with these squared lengths, all represented among the largest-level quadruples. None of the twenty maximizing four-element subsets shares three vertices with another.

For arbitrary \(x_j\in P\), expand each point as a convex combination of vertices. The **oriented** tetrahedral determinant is affine in each of its four point arguments, so its value is a convex combination of oriented vertex-quadruple determinants. Its absolute value is therefore at most the largest vertex-supported absolute determinant, proving the global bound. Equality forces every positively weighted vertex quadruple to have the same oriented extreme determinant. If even one \(x_j\) were not a vertex, two different choices of a vertex in its convex decomposition, with all other choices fixed, would give two extremal vertex quadruples sharing three vertices. This contradicts the exact non-sharing check. Hence every maximizing tetrahedron is vertex-supported, and the twenty quadruples above exhaust *all* equality cases. Dividing the maximal determinant \(10+4\sqrt5\) by six gives the stated volume.

## Verification

Run `python3 check_exact.py` using Python 3 and no third-party packages. The script independently checks the scaled six-generator realization, all thirty supporting rhombi, the twenty-plus-twelve vertex valences, the exact volume \(20\), each of the \(35\,960\) determinant values, every histogram multiplicity, the maximum, the twenty long-triangle/opposite-apex configurations, and the absence of any pair of maximizers sharing three vertices. The machine-readable histogram is `volume_spectrum.json`. Successful execution ends with `VERIFY_OK 32 vertices, 30 rhombic facets, 39 exact levels, 20 isolated maximizers`. Exact comparisons use integer arithmetic, so the certificate involves no numerical tolerance, finite search truncation, or external dependency.

## Relationship to prior work

The rhombic triacontahedron and its realization as a three-dimensional projection of the six-dimensional cube were studied by Koca, Koca and Koc (2014). Their preprint explicitly decomposes its vertex set into the twelve-vertex icosahedral and twenty-vertex dodecahedral shells. That construction establishes the object, but neither the maximal contained tetrahedron nor the complete four-vertex determinant distribution. Horváth and Lángi (2014) study a different extremal problem: optimizing the shapes of polytopes of prescribed vertex count **on a sphere**, rather than finding a simplex inside this fixed rhombic triacontahedron. The known regular-icosahedron tetrahedral maximum is likewise not a bound for the larger hull \(P\): the sharp maximizers here necessarily use a dodecahedral-shell vertex and all are isolated.

## Limitations

The **thirty-nine** exact volume levels describe only four-element subsets of the vertex set, not a discretization of the continuously many tetrahedra with arbitrary points of \(P\). Only the *maximum* and its complete equality locus are proved for arbitrary contained tetrahedra. The theorem concerns this fixed regular Catalan solid, not arbitrary deformations or all three-zonotopes. The proof of the finite determinant lemma is an explicit exhaustive integer-algebra computation, not an independent closed-form grouping of the thirty-nine levels. Historical priority beyond the checked literature is not certified, and external independent mathematical validation has not been conducted.

## References

1. M. Koca, N. O. Koca, R. Koc, “Group Theoretical Analysis of Quasicrystallography from Projections of Higher Dimensional Lattices \(B_n\),” arXiv:1403.2847, first submitted 12 March 2014. Section 3.3, especially the vertex-orbit construction and Figure 8.
2. Á. G. Horváth and Z. Lángi, “Maximum volume polytopes inscribed in the unit sphere,” arXiv:1402.6496, submitted 26 February 2014. A different, variable-container extremal problem.
3. P. Bourke, “Rhombic Triacontahedron,” August 2002, updated November 2021, coordinate and combinatorial reference: https://paulbourke.org/geometry/Rhombic_triacontahedron/index.html.
