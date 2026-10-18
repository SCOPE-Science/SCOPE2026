# Complete tetrahedral-volume spectrum and maximizing families of the regular icosidodecahedron

## Finding
Let \(P\subset\mathbb R^3\) be a regular icosidodecahedron of edge length one, and put \(\varphi=(1+\sqrt5)/2\). The volumes of the \(\binom{30}{4}=27405\) unordered tetrahedra formed by four distinct vertices of \(P\), **including degenerate tetrahedra**, take exactly 27 values. They are \((a+b\varphi)/12\), with the exact multiplicities in the following table. No other volume occurs among vertex tetrahedra.

| \((a,b)\) | Multiplicity | \((a,b)\) | Multiplicity | \((a,b)\) | Multiplicity |
|---|---:|---|---:|---|---:|
| \((0,0)\) | 2235 | \((1,0)\) | 780 | \((0,1)\) | 1380 |
| \((1,1)\) | 2460 | \((0,2)\) | 240 | \((2,1)\) | 60 |
| \((1,2)\) | 3660 | \((2,2)\) | 1800 | \((1,3)\) | 840 |
| \((2,3)\) | 2460 | \((3,3)\) | 240 | \((2,4)\) | 3060 |
| \((3,4)\) | 1560 | \((2,5)\) | 120 | \((3,5)\) | 1380 |
| \((4,5)\) | 180 | \((3,6)\) | 420 | \((4,6)\) | 1800 |
| \((4,7)\) | 840 | \((5,7)\) | 180 | \((4,8)\) | 210 |
| \((5,8)\) | 780 | \((6,8)\) | 60 | \((5,9)\) | 120 |
| \((6,9)\) | 240 | \((6,10)\) | 240 | \((7,11)\) | 60 |

For **every** Euclidean tetrahedron \(T\subseteq P\), whether or not its vertices belong to the vertex set of \(P\), the sharp bound is
\[
\operatorname{vol}_3(T)\leq \frac{7+11\varphi}{12}=\frac{25+11\sqrt5}{24}.
\]
The containing polytope has volume \(\operatorname{vol}_3(P)=(45+17\sqrt5)/6\). Thus its maximal tetrahedral volume fraction is exactly
\[
\boxed{\frac{M(P)}{\operatorname{vol}_3(P)}=\frac{19+7\sqrt5}{232}.}
\]

Exactly 60 vertex quadruples attain equality. The **complete geometric equality locus**, including nonvertex choices, comprises 20 families: for each of the 20 triangular facets \(F\) of \(P\), there is a unique triple \(B_F\) of vertices forming an equilateral triangle of side \(\varphi^2\) such that
\[
T=\operatorname{conv}(B_F\cup\{x\}),\qquad x\in F,
\]
is a maximizing tetrahedron; every maximizing tetrahedron has this form. Each facet gives exactly three vertex-supported maximizers, obtained at its three vertices. No maximizing tetrahedron has two or more nonvertex vertices. This theorem is unchanged by a nondegenerate affine transformation, with the obvious volume scaling.

## Assumptions and scope
Choose the regular icosahedron
\[
V_0=\{(0,\pm1,\pm\varphi),(\pm1,\pm\varphi,0),(\pm\varphi,0,\pm1)\}
\]
(with independent signs within each displayed group). Its edges have length two. The icosidodecahedron \(P\) is the convex hull of the 30 edge midpoints \((u+v)/2\), where \(u,v\in V_0\) and \(\|u-v\|=2\). The polytope has 20 triangular and 12 pentagonal facets, and all its edges have length one. The formula for maximum tetrahedral volume concerns arbitrary four-point simplices contained in this closed convex body; a simplex is allowed to meet facets or edges, and a zero-volume vertex quadruple is included in the spectral census.

## Proof
**1. Exact finite vertex reduction and spectrum.** Put \(W=\{u+v:u,v\in V_0,\ \|u-v\|=2\}\). This is the doubled vertex set of \(P\), with exactly 30 distinct points. Every coordinate of \(W\) belongs to \(\mathbb Z[\varphi]\), and \(\varphi^2=\varphi+1\). For each ordered four-tuple of distinct points \(w_0,w_1,w_2,w_3\in W\), define
\[
D(w_0,w_1,w_2,w_3)=\det(w_1-w_0,w_2-w_0,w_3-w_0).
\]
The actual tetrahedron vertices are \(w_i/2\), so their unsigned volume is \(|D|/48\). The attached exact-arithmetic `verify.py` enumerates all \(\binom{30}{4}=27405\) unordered index sets, computing both a three-by-three difference determinant and, independently, the four-by-four homogeneous-coordinate determinant. It checks their equality for every case. Each unsigned determinant is a multiple of four in \(\mathbb Z[\varphi]\), and the complete distribution of \(|D|/4\) is precisely the 27-value table displayed above, with \((a,b)\) representing \(a+b\varphi\). The largest is \(7+11\varphi\), attained 60 times. The calculation uses integer arithmetic only: for exact order comparisons it writes \(a+b\varphi=(2a+b+b\sqrt5)/2\) and compares the appropriate integer squares. The included program is a finite exhaustive proof for this *fixed finite vertex set*; it does not purport to certify a general class of polytopes.

For a direct equality witness, the four points
\[
(0,0,\varphi),\quad (0,\varphi,0),\quad
\tfrac12(-1-\varphi,-\varphi,-1),\quad
\tfrac12(1+\varphi,-\varphi,-1)
\]
belong to \(P\), and their absolute difference determinant equals \((7+11\varphi)/2\). Their tetrahedral volume is \((7+11\varphi)/12\). This proves sharpness against the finite enumeration.

**2. From vertex tetrahedra to arbitrary tetrahedra.** Fix four points \(p_0,\ldots,p_3\in P\) and write each as a convex combination of vertices of \(P\). Their **oriented** homogeneous-coordinate determinant is separately affine in each \(p_i\), hence a convex combination of the oriented determinants of all vertex four-tuples supported by the four decompositions. Therefore its absolute value cannot exceed the largest absolute vertex determinant. This proves the unrestricted bound, not merely a vertex-restricted bound.

**3. All equality configurations.** The same complete finite check finds that a pair of fixed vertices occurs in at most three of the 60 maximizing vertex quadruples. If an unrestricted maximizing tetrahedron had two nonvertex vertices, express these two vertices as nontrivial convex combinations of polytope vertices and choose particular positive-weight vertices for the other two positions. Equality in the multilinear determinant bound would force all four combinations obtained by choosing two distinct positively weighted vertices in each of the first two positions to be maximizing vertex quadruples, with the other two vertices fixed. They are four distinct quadruples sharing a fixed pair, contradicting the maximum pair co-degree three. Hence at most one tetrahedron vertex is nonvertex.

The complete certificate further shows that among the triples of polytope vertices occurring in the 60 maximizing vertex tetrahedra, exactly 20 triples admit three different maximizing completions; the other 180 triples have just one completion. In every three-completion case, the fixed triple is an equilateral triangle of side \(\varphi^2\), and the three admissible completion vertices form an edge-one equilateral triangular **facet** of \(P\). The certificate verifies its supporting-plane property against all 30 polytope vertices, not just its three side lengths. These 20 facets are distinct and all 60 vertex-supported maximizers are partitioned into their three-element completion sets.

For each such fixed triple, the determinant is affine in the variable fourth point and takes the same maximum signed value at all three facet vertices, so every fourth point in their triangular convex hull is optimal. Conversely, if a maximizing tetrahedron has one nonvertex fourth point, every vertex with positive coefficient in any vertex expansion of that point must be a maximizing completion of the fixed other three points; there must be at least two such completions. The finite three-completion classification confines the point to exactly one of the 20 indicated facets. Finally, if all four points are vertices, the preceding partition places the tetrahedron in exactly one family. This proves the asserted complete equality locus.

**4. Normalizing by the containing volume.** The original edge-two icosahedron has 20 equilateral triangular facets and volume \(20\varphi^2/3\); equivalently, its facet-origin determinants all have absolute value \(2\varphi^2\), giving \(20(2\varphi^2)/6\). Passing to the edge-midpoint hull removes 12 congruent pentagonal pyramids, one at each original vertex. Each pyramid has height \(1/\sqrt{\varphi+2}\) and a regular pentagon base of side one and area \((\varphi+2)^{3/2}/4\), so its volume is \((\varphi+2)/12\). Consequently,
\[
\operatorname{vol}_3(P)=\frac{20\varphi^2}{3}-(\varphi+2)
=\frac{14+17\varphi}{3}=\frac{45+17\sqrt5}{6}.
\]
Dividing \((7+11\varphi)/12\) by this value and simplifying \(\varphi^2=\varphi+1\) yields \((19+7\sqrt5)/232\), as claimed.

## Verification
Run `python3 verify.py` in a directory containing the embedded standalone `verify.py`. The verifier regenerates the original 12 vertices, all 30 edges and their 30 midpoints, independently calculates every tetrahedral determinant by two exact formulas in \(\mathbb Z[\varphi]\), compares the 27-entry count histogram, and verifies the count 60 of maximizers, maximum fixed-pair co-degree three, the 20 repeating triples and supporting facet planes, and their exhaustive coverage of all 60 maximizers. It additionally checks the icosahedron's 20 face determinants. The expected final output begins `VERIFY_OK` and reports the sizes and exact invariants. None of the arguments uses floating-point tolerances or random sampling.

## Relationship to prior work
The maximum-volume simplex problem in a prescribed polytope is developed generally by Gritzmann, Klee and Larman [1], and approximation algorithms are analyzed by Nikolov [2]. Their general frameworks do not themselves provide the displayed 27-level *instance-specific* determinant census or the full equality families. Horváth and Lángi [3] optimize whole polytopes with prescribed numbers of vertices on a sphere, a different variational problem. Lassak [4] establishes general containment properties of maximum-volume inscribed simplices, not the sharp value for this fixed Archimedean polyhedron. Standard descriptions of the icosidodecahedron as the rectification of the icosahedron, including its 30 vertices and 20 triangular facets, are available in classical regular-polytope geometry [5]. Exact enumeration of the 12-vertex icosahedral configuration would not determine the spectrum of edge-midpoint four-tuples: the latter involve additional mixed determinant terms and 30 possible vertices rather than 12.

## Limitations
The statement applies only to the regular icosidodecahedron and its nondegenerate affine images, not to arbitrary realizations with the same face lattice. The certificate exhausts a finite configuration; the unrestricted and continuous equality conclusions require, and are supplied by, the separate determinant-affinity and pair-codegree arguments above. The results have not undergone an independent external audit. A plausibly relevant historical source, Gritzmann, Klee and Larman [1], was accessible here only through its published abstract and references, leaving a residual possibility of an equivalent older evaluation. No priority claim is inferred solely from unsuccessful searches.

## References
1. P. Gritzmann, V. Klee and D. Larman, “Largest \(j\)-simplices in \(n\)-polytopes,” *Discrete & Computational Geometry* **13** (1995), 477–515, DOI: 10.1007/BF02574058. Full article not inspected.
2. A. Nikolov, “Randomized Rounding for the Largest Simplex Problem,” arXiv:1412.0036, first submitted 28 November 2014; §1 and §2.1 inspected in the HTML full text.
3. Á. G. Horváth and Z. Lángi, “Maximum volume polytopes inscribed in the unit sphere,” arXiv:1402.6496, first submitted 26 February 2014; substantial portions of the HTML full text inspected.
4. M. Lassak, “Approximation of convex bodies by inscribed simplices of maximum volume,” *Beiträge zur Algebra und Geometrie* **52** (2011), 389–394, DOI: 10.1007/s13366-011-0026-x; the open-access PDF and its principal theorem inspected.
5. H. S. M. Coxeter, *Regular Polytopes*, third edition, 1973, geometry of rectified regular polyhedra; descriptive geometric background only, not inspected in full.
