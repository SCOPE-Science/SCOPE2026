# Toroidal grid neighborhood complexes collapse to one or two tori

## Finding

Let \(L\subseteq\mathbb Z^2\) be a finite-index rank-two sublattice such that
\[
\lambda_1(L):=\min_{(a,b)\in L\setminus\{(0,0)\}}(|a|+|b|)\geq5.
\]
Put \(A=\mathbb Z^2/L\), \(N=|A|\), and let \(G_L\) be the simple undirected Cayley graph with vertex set \(A\) and neighbors \(v\pm e_1,v\pm e_2\), with \(e_1=(1,0)\) and \(e_2=(0,1)\) interpreted in \(A\). The **open-neighborhood complex** \(\mathcal N(G_L)\) is the abstract simplicial complex consisting of vertex subsets with a common graph neighbor.

**Theorem.** There is a sequence of exactly \(2N\) elementary simplicial collapses
\[
\mathcal N(G_L)\searrow T_L,
\qquad f(T_L)=(N,3N,2N),
\]
where \(T_L\) is a finite triangulated closed orientable surface, possibly disconnected. More precisely,
\[
|T_L|\cong_{\mathrm{PL}}\bigsqcup_{j=1}^{c(L)}(S^1\times S^1),
\quad c(L)=
\begin{cases}
1,&\text{if some }(a,b)\in L\text{ has }a+b\text{ odd},\\
2,&\text{if every }(a,b)\in L\text{ has }a+b\text{ even}.
\end{cases}
\]
Consequently its integral homology is torsion-free, with ranks \(c(L),2c(L),c(L)\) in dimensions \(0,1,2\), respectively, and zero in dimensions above \(2\).

For the standard **twisted toroidal grids**, set
\[
L_{m,n,k}=\langle(m,0),(k,n)\rangle,
\quad m,n\geq5,\quad 0\leq k<m.
\]
Here \(N=mn\) and \(c(L_{m,n,k})=1\) precisely when \(m\) is odd or \(k+n\) is odd. This includes ordinary Cartesian grids \(G_{L_{m,n,0}}=C_m\square C_n\). Twisting can change the answer at fixed size: at \(m=n=6\), twist \(k=2\) gives two tori, whereas twist \(k=3\) gives one.

## Assumptions and scope

All vertices are residue classes in \(A=\mathbb Z^2/L\); there are no loops or multiple edges. The lower bound on the \(\ell^1\)-length of a nonzero period excludes short identifications and makes every vertex neighborhood a genuine four-vertex set. It holds automatically for \(L_{m,n,k}\) when \(m,n\geq5\), because a nonzero multiple of \((k,n)\) has vertical displacement at least \(n\), and a vector of vertical displacement zero is a nonzero multiple of \((m,0)\). The theorem is about the **open** Lovász neighborhood complex, not the closed-neighborhood complex and not a Vietoris–Rips complex. Its original tetrahedral complex generally is not PL homeomorphic to a surface; the conclusion is an elementary **collapse to** a PL surface.

## Proof

**1. Distinct neighborhoods and free local faces.** Write \(E=v+e_1\), \(W=v-e_1\), \(U=v+e_2\), and \(D=v-e_2\), in the quotient \(A\). Every maximal simplex of \(\mathcal N(G_L)\) is the tetrahedron \(Q_v=\{W,E,U,D\}\). No distinct centers have three common neighbors: choose common-neighbor lifts in the infinite square grid; if two choices of the relative period differ, their difference has \(\ell^1\)-length at most \(4\), contradicting \(\lambda_1(L)\geq5\). For a fixed relative period, distinct infinite-grid centers have at most two common neighbors. Thus every triangle of \(Q_v\) belongs to no other tetrahedron. The opposite horizontal pair \(\{W,E\}\) has the unique common neighbor \(v\), by the same short-period argument.

**2. Exactly two elementary collapses per center.** For each \(v\in A\), first delete the free pair
\[
(\{W,E,U\},\ Q_v),
\]
which removes one triangle and its tetrahedron. Then delete
\[
(\{W,E\},\ \{W,E,D\}),
\]
which removes the opposite horizontal edge and its remaining triangle. These are genuine elementary simplicial collapses: the triangle in the first pair has only the displayed tetrahedron as coface; after that tetrahedron and triangle are removed, the horizontal opposite edge is contained in exactly the remaining indicated triangle, because only \(v\) is a common neighbor of \(W\) and \(E\). All these pairs are disjoint as simplices for different centers, so the \(2N\) operations may be made in any fixed center order.

The surviving two triangles per center are
\[
\{W,U,D\},\qquad\{E,U,D\}.
\]
In the universal cover \(\mathbb Z^2\), they triangulate the diamond with corners \(v\pm e_1,v\pm e_2\), along the vertical diagonal \(\{U,D\}\). Counting their face incidences gives \(f_2=2N\), \(f_1=3N\), \(f_0=N\). The resulting complex is precisely the quotient by \(L\) of those triangles on the infinite grid.

**3. Two planar triangulations and their deck-group action.** Partition the infinite-grid centers by parity of coordinate sum. The diamonds centered at centers of a fixed parity form a translation-invariant, edge-to-edge tiling of \(\mathbb R^2\): adjacent centers differ by \(e_1+e_2\) or \(e_1-e_2\); the diamond has area \(2\), equal to the covolume of this center lattice. Triangulating all diamonds by their vertical diagonals produces a simplicial triangulation of the plane. The centers of the opposite parity produce another, disjoint simplicial plane; the two vertex sets are disjoint because every diamond's vertices have parity opposite to the center. The minimum-period hypothesis guarantees that their quotients are still honest simplicial triangulations, with no triangles or edges identified internally.

Each \(\ell\in L\) acts on the disjoint union of these two planes by an orientation-preserving translation and swaps them exactly when its coordinate sum is odd. Let \(L_{\mathrm{even}}=\{(a,b)\in L:a+b\text{ is even}\}\). If all periods have even sum, the two components quotient separately to \(\mathbb R^2/L\), each a torus. If an odd-sum period exists, the action is transitive on the two planes; the quotient is one copy of \(\mathbb R^2/L_{\mathrm{even}}\), also a torus. Translation quotients inherit PL orientation and the stated triangulations. This proves the component and orientability assertions.

**4. Homology and twisted-grid criterion.** Elementary collapses preserve homotopy type, and the orientable torus has integral homology \(\mathbb Z,\mathbb Z^2,\mathbb Z\) in degrees \(0,1,2\). For \(L_{m,n,k}\), parity of every period is controlled by the generators \((m,0)\) and \((k,n)\), yielding the criterion \(m\) even and \(k+n\) even for the two-torus case. This also agrees with the elementary bipartiteness criterion for the graph.

## Verification

Run `python3 verify_toroidal_neighborhoods.py` with Python 3 and no third-party dependencies. The verifier constructs all tetrahedral neighborhood facets, checks triangle uniqueness and **each individual free-face collapse**, counts the surviving simplices, confirms every vertex link is a six-cycle, checks component counts and Euler characteristic, and performs independent mod-two boundary-rank calculations on five sample parameter choices. Its exhaustive parameter region is \(5\leq m,n\leq8\), \(0\leq k<m\). The recorded run reports:

`VERIFY_OK cases=104 links=4524 local_collapses=9048 triangulated_surfaces=all mod2_homology=5_samples`

The all-lattice theorem is proved by the universal-cover argument above, not by this finite test. The checker does not establish new universal assertions outside its explicitly enumerated domain.

## Relationship to prior work

Matsushita [1] defines these open-neighborhood complexes and relates their fundamental groups to graph-theoretic even fundamental groups. That theorem does not determine the PL types, two-dimensional homology, or explicit simplicial collapses of general lattice-quotient grids. Shukla [2, Theorems 2.5–2.6, Lemma 4.2] already gives **similar two-dimensional neighborhood-complex collapses** for many 4-regular **circulant graphs**, including special cyclic-grid cases homotopy equivalent to a torus. Those covered cyclic instances and the local collapse method are not claimed as new. The statement here covers arbitrary finite-index square-lattice quotients, including noncyclic translation groups, gives the exact number and topology of components by lattice parity, and provides an explicit all-parameter collapse and PL core. Morris [3, Definitions 1.2 and Remark 1.8] independently describes twisted toroidal grids and their **graph bipartiteness** criterion; that bipartiteness fact is not claimed as new, and the inspected work concerns graph-cover automorphisms rather than the topology of open-neighborhood complexes.

## Limitations

The period-length lower bound is essential to the presented local uniqueness argument; smaller periods are not classified here. The theorem proves an elementary collapse and hence a homotopy equivalence of the original three-dimensional complex, not a PL homeomorphism of the original complex to a torus. Existing circulant subfamilies overlap Shukla's earlier work. Published-literature comparisons do not exclude an unindexed equivalent statement for general lattice quotients.

## References

[1] T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803 (first posted 2012-10-10), *J. Math. Sci. Univ. Tokyo* 24 (2017), 321–353, https://arxiv.org/abs/1210.2803 .

[2] S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526 (first posted 2018-02-13), *Electron. J. Combin.* 26 (2019), P2.4, https://arxiv.org/html/1802.04526v2 .

[3] D. W. Morris, *Automorphisms of the canonical double cover of a toroidal grid*, arXiv:2301.05396 (first posted 2023-01-13), *Art Discrete Appl. Math.* 6 (2023), P3.07, https://arxiv.org/html/2301.05396v1 .
