# Sharp intrinsic eccentricity interval of the regular tetrahedral surface

## Finding
Let \(S_a\) denote the **boundary surface**, not the solid body, of a regular tetrahedron with Euclidean edge length \(a>0\). Use the intrinsic shortest-path length metric, including paths through edges and at vertices. Define the source eccentricity
\[
e_a(p)=\max_{q\in S_a}d_{S_a}(p,q).
\]
Then the exact full eccentricity range is
\[
\boxed{\{e_a(p):p\in S_a\}=[a,2a/\sqrt3].}
\]
In particular the intrinsic Chebyshev radius is \(\boxed{a}\). All six edge midpoints attain that minimum, and all four vertices attain the upper endpoint \(2a/\sqrt3\). Neither exclusivity assertion is made.

A structural ingredient valid in all dimensions at least two is the following: for any full-rank Euclidean lattice \(\Lambda\subset\mathbb R^d\), \(d\ge2\), and its inversion quotient \(P_\Lambda=(\mathbb R^d/\Lambda)/(u\sim-u)\),
\[
\operatorname{rad}(P_\Lambda)\ge \frac12\min_{\lambda\in\Lambda\setminus\{0\}}\|\lambda\|_2.
\]
The regular tetrahedron is the first nontrivial sharp realization here, by an explicit two-coset covering of its torus double cover. The minimax result is intrinsic and does not concern the Euclidean inradius or circumradius of the solid tetrahedron.

## Assumptions and scope
The surfaces and quotients are compact **length metric spaces**; distances are infima of lengths of surface curves. Torus quotients have the usual quotient metric under a finite group of isometries. A lattice \(\Lambda\) is full rank, and its shortest nonzero vector length is \(\lambda_1(\Lambda)>0\). Geodesic closed balls are closed in the torus. The tetrahedral statement is stated for all \(a>0\), reduced to \(a=1\) by similarity. No claim is made for irregular tetrahedra or arbitrary intrinsic metrics on spheres.

For the unit case set
\[
e_1=(1,0),\qquad e_2=(1/2,\sqrt3/2),\qquad
\Lambda=\mathbb Z(2e_1)+\mathbb Z(2e_2).
\]
Its flat torus is \(T=\mathbb R^2/\Lambda\), and the half-turn involution is \(j([u])=[-u]\). The quotient \(T/\langle j\rangle\) is isometric to \(S_1\), as justified below. Sources in the tetrahedron are represented by \([u]_{\pm}\), and targets by \([v]_{\pm}\).

## Proof
**1. Triangular-torus realization.** Triangulate the plane into unit equilateral triangles with vertex lattice \(\mathbb Ze_1+\mathbb Ze_2\). The period lattice \(\Lambda\) identifies eight triangles in one fundamental parallelogram, and inversion pairs them into four triangular faces. Its only fixed points modulo \(\Lambda\) are the four order-two points, all triangular-lattice vertices, and each has total angle \(\pi\) in the quotient. The quotient has four vertices, six edges, and four equilateral triangular faces, with three faces at each vertex. The parity labels on lattice vertices ensure that every edge joins distinct vertices and every face has three distinct vertices. This is exactly the face gluing and intrinsic metric of the unit regular tetrahedron. Alternatively, checking the pairwise edge labels in \((\mathbb Z/2)^2\) gives its tetrahedral adjacency directly. In particular the quotient metric formula is
\[
 d_{S_1}([u]_{\pm},[v]_{\pm})
 =\min_{\lambda\in\Lambda}\min\{\|u-v-\lambda\|_2,\|u+v-\lambda\|_2\}.
\]
The equality follows from lifting paths in the finite isometric quotient, including branch points, or by triangulated developments; the quotient length metric agrees with the orbital minimum formula.

**2. Two-center covering identity.** For a fixed source \([u]_{\pm}\), translate the target variable \(v\) over the torus and rearrange the preceding minimum. Its eccentricity equals
\[
 e_1([u]_{\pm})
 = \sup_{x\in\mathbb R^2}\operatorname{dist}\bigl(x,\Lambda\cup(\Lambda+2u)\bigr).
\]
Thus the source's farthest-point distance is the periodic Euclidean covering radius of a pair of lattice cosets. The same identity works for any dimension and any flat torus inversion quotient. It is a **minimax covering problem**, not a mean-pair-distance identity.

**3. Universal lower bound, with a proof of the topological obstruction.** Let \(T=\mathbb R^d/\Lambda\) with \(d\ge2\), and let \(s=\lambda_1(\Lambda)\). Every open torus ball of radius strictly below \(s/2\) is a homeomorphic image of a Euclidean open ball and is contractible in \(T\): no two different lifts in that ball can differ by a lattice vector of length at least \(s\). Suppose two torus centers had covering radius \(r<s/2\). Choose \(r<r'<s/2\); the two open \(r'\)-balls cover \(T\) and each is contractible. This is impossible: the degree-one integral cohomology of \(T\) has classes \(\alpha\) and \(\beta\) with \(\alpha\smile\beta\ne0\) in degree two. For an open cover \(T=U\cup V\) by sets each contractible in \(T\), both classes restrict to zero on both \(U\) and \(V\). They therefore lift to relative classes in \(H^1(T,U;\mathbb Z)\) and \(H^1(T,V;\mathbb Z)\), whose relative cup product lands in \(H^2(T,U\cup V;\mathbb Z)=H^2(T,T;\mathbb Z)=0\). That contradicts \(\alpha\smile\beta\ne0\). Therefore any two-point covering radius on \(T\) is at least \(s/2\). The identity of Step 2 gives \(\operatorname{rad}(P_\Lambda)\ge s/2\). This is an explicit cup-product proof; no appeal to a bare covering-count assertion is needed.

For the tetrahedral lattice,
\[
\|2me_1+2ne_2\|_2^2=4(m^2+mn+n^2),\qquad (m,n)\in\mathbb Z^2.
\]
The minimum for \((m,n)\ne(0,0)\) is four. Hence \(e_1(p)\ge1\) for every tetrahedral source \(p\).

**4. Sharpness at edge midpoints.** Consider the midpoint \(p\) of the tetrahedral edge joining the vertices represented by \(0\) and \(e_1\). It is represented by \(u=e_1/2\). Then \(2u=e_1\), and the two-coset union is precisely the rectangular lattice
\[
\Lambda\cup(\Lambda+e_1)
 =\mathbb Ze_1+\mathbb Z(2e_2-e_1)
 =\mathbb Z(1,0)+\mathbb Z(0,\sqrt3).
\]
Its Voronoi cell is a rectangle with half-sides \(1/2\) and \(\sqrt3/2\); its covering radius is therefore
\[
\sqrt{(1/2)^2+(\sqrt3/2)^2}=1.
\]
The identity in Step 2 gives \(e_1(p)=1\), establishing the global minimum. Tetrahedral edge transitivity gives all six midpoints as minimizers. In particular, the midpoint of the opposite edge is a target at distance one from \(p\) (corresponding to a Voronoi corner), so equality is genuinely attained.

**5. Maximum and full interval.** For any source, adding the second coset cannot increase the covering radius, so \(e_1(p)\le\operatorname{covrad}(\Lambda)\). The six shortest nonzero vectors in \(\Lambda\) form an equilateral hexagonal neighbor arrangement with nearest-neighbor distance two. The Voronoi cell is a regular hexagon of inradius one and circumradius \(1/\cos(\pi/6)=2/\sqrt3\). Thus all sources satisfy \(e_1(p)\le2/\sqrt3\). At each tetrahedral vertex, \(2u\in\Lambda\), so the cosets coincide and equality holds. Finally, \(e_1\) is 1-Lipschitz as a function of source by the triangle inequality, and \(S_1\) is connected. Its continuous image is a connected compact interval containing both proved extrema. It must be exactly \([1,2/\sqrt3]\). Scaling by \(a\) gives the stated theorem.

## Verification
The proof is exhaustive over every source and target; it does not rely on sampling. For independent numerical corroboration, run `python tetra_radius_verify.py` with Python 3, NumPy, and SciPy. It reconstructs the periodic two-coset Voronoi diagrams in a finite surrounding supercell, checks the exact vertex and three nonzero half-period source cases, and tests 250 reproducible generic source configurations against both proved global bounds. The checker reported vertex radius \(1.1547005383792515\), radius \(1\) for all three nontrivial half-period shifts, and 250 generic covering radii between \(1.000031628761\) and \(1.149742494086\). These finite checks only corroborate the analytical proof. The package includes the actual executed checker script.

## Relationship to prior work
Davis, Dods, Traub and Yang (arXiv:1508.03546, first version 12 August 2015) develop the equilateral triangular-lattice unfolding of tetrahedral geodesics and classify vertex-directed geodesic trajectories. We use that standard geometry but do not claim the lattice description is new. D. M. Davis (arXiv:2306.11059, 2023) analyzes source cut loci and geodesic complexity, notably the meeting of cut-locus branches near opposite edge midpoints; its stated claims do not give a lower bound for eccentricity over **all** sources or the exact intrinsic Chebyshev radius. Earlier vertex-source distance distributions also supply the value \(2/\sqrt3\) at tetrahedral vertices; the upper endpoint alone is not new. The distinct contribution here is the sharp **global minimax bound** and six optimal edge-midpoint witnesses derived from a topological obstruction to covering a torus by two small balls.

General torus cup-length and periodic circle-covering methods are classical and not presented as new individually. A previously published treatment of the same tetrahedral minimax problem under alternate terminology could exist; the statement is not a claim of independent historical certification.

## Limitations
This does not prove that edge midpoints are the **only** minimizing sources, or vertices the only maximizing sources. No pointwise formula for eccentricity away from the cited extremizers is asserted beyond the exact two-coset variational identity. The numerical checker samples only finitely many configurations and requires SciPy. The result concerns the intrinsic **surface** metric rather than the Euclidean metric in the tetrahedron's ambient space. The proof does not extend automatically to general polyhedra. Historical priority remains uncertain pending independent examination of older sources.

## References
1. D. Davis, V. Dods, C. Traub, J. Yang, *Geodesic trajectories on regular polyhedra*, arXiv:1508.03546v1 (12 August 2015), https://arxiv.org/pdf/1508.03546 . Material inspected: Sections 1–3 and triangular-lattice vertex labels.
2. D. M. Davis, *Geodesic complexity of a tetrahedron*, arXiv:2306.11059 (19 June 2023), https://arxiv.org/pdf/2306.11059 . Material inspected: Section 2, Figures 2.1–2.8, and Section 3 including the midpoint discussion.
3. The standard integral cohomology cup product of a flat torus and its use in Lusternik–Schnirelmann category theory; an account is H. Singh, *Lusternik-Schnirelmann Category and Cobordism*, Proceedings of the AMS **102** (1988), 183–190, https://doi.org/10.2307/2046056 . The needed special case is proved explicitly above.
