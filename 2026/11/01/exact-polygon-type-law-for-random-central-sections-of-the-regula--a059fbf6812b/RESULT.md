# Exact polygon-type law for random central sections of the regular truncated tetrahedron

## Finding

Let \(T\subset\mathbb R^3\) be the regular truncated tetrahedron, and select an unoriented plane \(H\) through its centroid by Haar-uniform orientation. Outside a null set of normals, the section \(T\cap H\) is a convex polygon with \(N\in\{4,5,6\}\) sides. Its **complete exact probability law** is

\[
\begin{aligned}
\Pr(N=4)&=\frac{12}{\pi}\bigl[\Omega(A,B,C)+\Omega(D,F,C)\bigr],\\
\Pr(N=5)&=\frac{12}{\pi}\bigl[\Omega(B,D,C)+\Omega(E,G,F)+\Omega(E,F,D)\bigr],\\
\Pr(N=6)&=\frac{12}{\pi}\bigl[\Omega(B,E,D)+\Omega(G,H,F)\bigr].
\end{aligned}
\]

Here \(\Omega(P,Q,R)\) is the spherical area of the triangle determined by positive rays through \(P,Q,R\), explicitly given below. Its arguments are the following integer triples:

| Ray | Coordinates |
|:--|:--|
| \(A\) | \((1,0,0)\) |
| \(B\) | \((3,1,0)\) |
| \(C\) | \((4,1,1)\) |
| \(D\) | \((5,2,1)\) |
| \(E\) | \((1,1,0)\) |
| \(F\) | \((2,1,1)\) |
| \(G\) | \((3,3,2)\) |
| \(H\) | \((1,1,1)\) |

For positive-hemisphere rays \(P,Q,R\), set

\[
\Omega(P,Q,R)=2\arctan\frac{|\det(P,Q,R)|}{\|P\|\|Q\|\|R\|+(P\cdot Q)\|R\|+(Q\cdot R)\|P\|+(R\cdot P)\|Q\|}.
\]

All denominator terms are positive for the listed rays. The values are

| Sides | Probability (approximate) |
|:--|--:|
| \(4\) | \(0.2159360853126405\) |
| \(5\) | \(0.5202474652389365\) |
| \(6\) | \(0.2638164494484232\) |

An independent exact identity for the expectation is

\[
\boxed{\mathbb E N=\frac{18}{\pi}\arccos\left(\frac7{11}\right)=5.047880364135784\ldots .}
\]

## Assumptions and scope

Write \(t_0=(1,1,1)\), \(t_1=(1,-1,-1)\), \(t_2=(-1,1,-1)\), and \(t_3=(-1,-1,1)\). The solid \(T\) is the convex hull of the twelve points \(w_{ij}=2t_i+t_j\), for ordered distinct \(i,j\in\{0,1,2,3\}\). This is a uniform edge-truncation of the regular tetrahedron: all new edges have length \(2\sqrt2\). The volume centroid is the origin by tetrahedral symmetry.

The random plane is \(H=u^\perp\), where \(u\) is uniform on \(S^2\); normals \(u\) and \(-u\) describe the same plane. We count vertices/sides of the **intersection polygon**, not a projection silhouette. The exceptional orientations passing through an original polyhedron vertex, or producing a nongeneric edge incidence, form a finite union of great circles and have probability zero. The probabilities are unchanged by uniform scaling or rigid motion of \(T\).

## Proof

**1. Exactly eighteen intersectable edges.** For each \(i\), the three points \(w_{ij}\) with \(j\ne i\) are joined pairwise, forming the triangular truncation face. These supply twelve edges. For each unordered \(\{i,j\}\), the pair \(w_{ij},w_{ji}\) forms the surviving middle third of a tetrahedron edge, supplying six more edges. There are no others: the original four faces become hexagons and the four corner faces are triangles; these eight facets have \((4\cdot6+4\cdot3)/2=18\) distinct edges. An exact independent facet enumeration is reproduced by the verifier. Every vertex obeys \(\|w_{ij}\|^2=11\), and every edge has squared length \(8\).

For a generic normal \(u\), a segment between distinct vertices \(v,w\) intersects the central plane \(u^\perp\) in its relative interior if and only if \((u\cdot v)(u\cdot w)<0\). The intersection is a nondegenerate convex polygon, and its vertices are precisely the intersections with crossing polyhedron edges. Therefore

\[
N(u)=\sum_{\{v,w\}\in E(T)}\mathbf1_{(u\cdot v)(u\cdot w)<0}.
\]

**2. Reduce to one spherical chamber.** Every symmetry of the tetrahedron permutes coordinates and performs an even number of coordinate sign changes. Since a normal and its negative represent one plane, almost every orientation can uniquely be transported, modulo chamber walls, into the chamber

\[
u=\frac{(1,y,z)}{\sqrt{1+y^2+z^2}},\qquad 0<z<y<1.
\]

The tetrahedral full symmetry group has order \(24\), and the total unoriented spherical measure is \(2\pi\); hence this chamber has spherical area exactly \(\pi/12\). Its gnomonic image in \((y,z)\) is the triangle with vertices \((0,0)\), \((1,0)\), and \((1,1)\).

**3. Exhaust the sign chambers.** The signs of all twelve linear functionals \(u\cdot w_{ij}\) can change only on their zero lines. Substituting the twelve explicit vertices and restricting to \(0<z<y<1\), only four zero lines meet the open triangular chamber:

\[
1-y-3z=0,\quad 1-3y-z=0,\quad 1-3y+z=0,\quad 1+y-3z=0.
\]

All remaining eight vertex functionals keep a strict fixed sign in the open chamber. Clipping this triangle successively by the four lines produces precisely the six closed polygonal cells below. Each cell is listed by its consecutive corner rays; the edge-crossing formula in step 1, evaluated at any interior direction, gives its side count.

| Cell | Consecutive corners | Number of section sides |
|:--|:--|--:|
| \(R_1\) | \(A,B,C\) | \(4\) |
| \(R_2\) | \(B,D,C\) | \(5\) |
| \(R_3\) | \(B,E,D\) | \(6\) |
| \(R_4\) | \(D,F,C\) | \(4\) |
| \(R_5\) | \(E,G,F,D\) | \(5\) |
| \(R_6\) | \(G,H,F\) | \(6\) |

The listed corners are exactly the pairwise intersections of the four displayed lines with each other and with the triangle boundary; all coordinates are rational. Adjacent cell interiors have disjoint sign patterns, and their union is the whole chamber. Thus this is an **exhaustive**, not sampled, classification. In particular, triangles, heptagons, or any other section side counts occur with probability zero.

**4. Evaluate spherical measures.** The well-known van Oosterom–Strackee spherical triangle formula displayed in the finding evaluates each triangular cell exactly. The sole quadrilateral \(E,G,F,D\) is partitioned into triangles \(E,G,F\) and \(E,F,D\). Add the cell areas with the same side count and divide by the total chamber area \(\pi/12\). This proves the three expressions, including normalization \(\Pr(N=4)+\Pr(N=5)+\Pr(N=6)=1\).

**5. A separate expectation identity.** The endpoints of any edge have Euclidean norm \(\sqrt{11}\) and mutual squared distance \(8\); hence their angle at the origin is \(\arccos(7/11)\). A uniformly oriented plane through the origin separates the endpoints with probability their angular separation divided by \(\pi\). Linearity of expectation over the eighteen edges gives the exact formula for \(\mathbb E N\), independently of the six-cell spherical-area calculation. Substitution of the three computed probabilities reproduces it.

## Verification

Run `python3 verify.py` with Python 3 and the standard library; no external packages or downloads are required. The program independently constructs all eight facets from integer supporting-plane tests, derives eighteen edges by pairs of shared facets, checks each squared edge length and vertex norm, clips the ordered-direction chamber by all twelve vertex zero planes using exact rational arithmetic, checks the **complete prescribed six-cell list and side counts**, evaluates the closed spherical triangle areas, verifies their sum is \(\pi/12\), and checks the independent edge-angle formula for the mean. An isotropic-normal Monte Carlo check with a fixed seed is included as an optional finite consistency diagnostic. The deterministic rational chamber checks and the analytic proof, not Monte Carlo, establish exhaustiveness.

Observed verifier output:

```
Exact polyhedron: 12 vertices, 18 equal edges, 4 triangles, 4 hexagons.
Exact spherical-area evaluation: sides=4, probability=0.215936085312640
Exact spherical-area evaluation: sides=5, probability=0.520247465238937
Exact spherical-area evaluation: sides=6, probability=0.263816449448423
Mean sides from spherical areas=5.047880364135784; from 18 edge angles=5.047880364135783.
Independent isotropic Monte Carlo (35000 orientations): {4: 0.214514, 5: 0.520886, 6: 0.2646}.
PASS: exact combinatorics, all 6 spherical chambers, normalization,
independent mean identity, and finite numerical consistency.
```

## Relationship to prior work

The general decomposition of section parameters into arrangements and chambers is established by Brandenburg, De Loera, and Meroni, *The Best Ways to Slice a Polytope* (2023 preprint, 2025 publication). Brandenburg, De Loera, Luo, and Meroni (first public March 26, 2026) further develop exact algorithms for slice-volume moments, prominently for cubes and other polyhedral norm balls. Birkemeyer, Brose, Brandenburg, and Prün (first public September 14, 2026) investigate which combinatorial section data reconstruct a polytope; their central-section vertex-count theorem is a reconstruction statement under generic hypotheses. These general algorithms and structural principles are prior work and not claimed new.

The contribution here is the **evaluated exact Haar probability law** for the specified noncentrally symmetric Archimedean polyhedron, including its six-rational-cell arrangement and independent expectation check. The inspected primary papers do not state this particular distribution. Related exact central-section laws for the icosahedron and rectangular boxes concern other polytopes; projections are also distinct from central sections. Broad prior frameworks make such computations possible in principle but do not alone imply the displayed evaluated coefficients.

## Limitations

The theorem applies to a specific regular truncated tetrahedron and central planes selected by uniform orientation. It does not describe off-center random planes, orientation-biased distributions, areas or perimeters of the sections, or other truncated regular polytopes. The closed forms involve standard arctangent spherical areas, not elementary rational probabilities. The work has received no independent mathematical audit, and an equivalent older evaluated law could exist in stereology or crystallography despite the targeted literature comparisons. The general sign-arrangement principle and the edge-angle expectation trick are classical rather than independent novelty claims.

## References

1. M.-C. Brandenburg, J. A. De Loera, C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239 (first public April 27, 2023), *Mathematics of Computation* 94 (2025), 1003–1042. https://arxiv.org/abs/2304.14239
2. M.-C. Brandenburg, J. A. De Loera, Y. Luo, C. Meroni, *Critical moments of slices and slabs of the cube (and other polyhedral norms)*, arXiv:2603.25643 (first public March 26, 2026). https://arxiv.org/abs/2603.25643
3. A. Birkemeyer, A. E. Brose, M.-C. Brandenburg, N. Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195 (first public September 14, 2026). https://arxiv.org/abs/2609.16195
4. J. A. De Loera, L. López-Campos, D. Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope*, arXiv:2412.12419 (first public December 17, 2024). https://arxiv.org/abs/2412.12419
5. J. E. van Oosterom, J. Strackee, *The Solid Angle of a Plane Triangle*, IEEE Transactions on Biomedical Engineering 30 (1983), 125–126. The spherical-triangle identity is used as a standard analytic formula, not claimed new.
