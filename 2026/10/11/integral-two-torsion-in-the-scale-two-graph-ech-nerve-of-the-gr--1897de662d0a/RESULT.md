# Integral two-torsion in the scale-two graph Čech nerve of the Grötzsch graph

## Finding
Let \(G\) denote the eleven-vertex Grötzsch graph, the Mycielski construction applied to the five-cycle. Let \(\mathcal N(G,2)\) be the nerve of the closed radius-one balls centered at the vertices in the unit-edge geometric realization of \(G\), equipped with its intrinsic shortest-path metric. Its reduced **integral** homology is
\[
\widetilde H_j(\mathcal N(G,2);\mathbb Z)\cong
\begin{cases}
\mathbb Z/2,&j=1,\\
\mathbb Z^{10},&j=2,\\
0,&j\notin\{1,2\}.
\end{cases}
\]
In particular, the complex has nonzero integral torsion; it is not homotopy equivalent to any wedge of spheres. A 55-step elementary collapse reduces its dimension from five to two.

## Assumptions and scope
All calculations concern **only** the graph defined here, and closed balls in the *geometric realization* with its intrinsic path metric. Number the vertices \(v_i=i\), \(u_i=5+i\) for \(0\le i<5\), and \(w=10\), with subscripts interpreted modulo five. The undirected edges are \(v_iv_{i+1}\), \(u_iv_{i-1}\), \(u_iv_{i+1}\), and \(wu_i\), for every \(i\in\{0,1,2,3,4\}\). Thus \(G\) has 11 vertices and 20 edges. The coefficient ring in the theorem is \(\mathbb Z\); this is not solely a mod-two or rational calculation.

At scale two, a collection of vertex-centered closed radius-one graph balls intersects if and only if its vertex centers have a common graph vertex at distance at most one. Consequently the maximal simplices are contained in the eleven closed graph neighborhoods \(N_G[v]\). This also follows from the even-scale nerve formula of Adams–Shukla–Singh [1]. These eleven neighborhoods are distinct inclusion-maximal faces: five have five vertices, five have four vertices, and one has six vertices.

## Proof
**Step 1 (finite complete face enumeration).** Construct all nonempty subsets of the eleven sets \(N_G[v]\), identify repeated subsets, and order the resulting faces by their increasing vertex tuples. Their dimension-indexed face vector is exactly
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(11,55,90,45,11,1).
\]
This means 213 nonempty faces. The complete construction is implemented in `verify.py` without external libraries.

**Step 2 (homotopy-preserving collapse).** The accompanying `certificate.json` records 55 ordered pairs \((\sigma,\tau)\). The verifier reconstructs the **current** face set at every step and checks that \(\sigma\) is a codimension-one face of \(\tau\), with \(\tau\) its *unique* strict coface. It then deletes that elementary free pair. This provides an explicit simple-homotopy equivalence onto a two-dimensional simplicial complex \(L\), whose face vector is
\[
(f_0(L),f_1(L),f_2(L))=(11,46,46).
\]
All remaining faces are verified downward-closed.

**Step 3 (integral cellular boundary).** The edges of \(L\) joining vertex 0 to each of the other ten vertices form a spanning tree. Contracting that tree gives a homotopy-equivalent CW complex with one vertex, 36 oriented one-cells, and 46 oriented two-cells. Orient edges from the smaller to the greater vertex; orient every triangle by its increasing vertex ordering. For a triangle \([a,b,c]\) with \(a<b<c\), its cellular boundary is \([b,c]-[a,c]+[a,b]\). Discard tree-edge coordinates after contracting the tree to obtain an integer matrix \(A\) with 36 rows and 46 columns. Rows are ordered lexicographically by non-tree edge and columns lexicographically by triangle; both are rebuilt by the verifier.

**Step 4 (exact torsion certificate).** The 36 triangle-column indices recorded as `pivot_triangle_indices` in `certificate.json` select a 36-by-36 submatrix \(B\) of \(A\) having **exact signed determinant \(+2\)**, as verified by fraction-free integer elimination. Moreover \(\operatorname{rank}_{\mathbb F_2}(A\bmod2)=35\), whereas \(\operatorname{rank}_{\mathbb F_3}(A\bmod3)=36\). The determinant first proves \(A\) has full row rank 36 over \(\mathbb Q\), and that the product of all positive Smith invariant factors of \(A\) divides two. The mod-two rank shows that precisely one invariant factor is even. It follows that the Smith invariant factors are 35 copies of 1 and one copy of 2. Thus the cokernel of \(A\) is \(\mathbb Z/2\), and the kernel is a free abelian group of rank \(46-36=10\). These are respectively \(H_1(L;\mathbb Z)\) and \(H_2(L;\mathbb Z)\); the connectedness of the spanning tree gives \(\widetilde H_0(L;\mathbb Z)=0\), while the collapse makes all higher homology vanish. Homotopy invariance now proves the finding for \(\mathcal N(G,2)\).

## Verification
Run `python3 verify.py certificate.json` in the directory containing both attached files. No third-party packages, downloaded papers, or external files are required. The script reconstructs every vertex, edge, Čech facet, and simplex rather than trusting a claimed count; verifies each of the 55 elementary collapses as a genuine free-face deletion; checks the spanning tree and signed boundary construction; calculates the exact determinant \(+2\), and both modular ranks. Its successful final line begins `VERIFY_OK` and includes `faces: 213`, `collapse_pairs: 55`, `spine: [11, 46, 46]`, `boundary_shape: [36, 46]`, `minor_determinant: 2`, and `rank_mod_2: 35`. These operations provide exact finite arithmetic certificates; they do not require extrapolation from experimental examples.

## Relationship to prior work
Adams, Shukla and Singh [1] introduce intrinsic graph Čech nerves and derive their closed-neighborhood description at even integer scale; their scale-two homotopy classification is for binary hypercubes, not the Grötzsch graph. Previte [2] studies the equivalent distance-neighborhood construction for various graph families. Matsushita [3] studies exactly the general closed-neighborhood construction and connects it to other graph complexes, but the inspected results do not give this graph's integral chain calculation or the order-two invariant. The result here is not a statement about the Lovász **open** neighborhood complex, the independence complex, or a Vietoris–Rips clique complex. In particular, general equivalences between constructions do not independently specify the Smith invariant factors for this particular graph.

## Limitations
This is an exact, isolated graph computation, not a homotopy-type classification and not an infinite-family theorem. In particular, no identification of the fundamental group or of an integral wedge decomposition is asserted. The symbolic calculation gives only the stated integral homology groups and a two-dimensional deformation spine. Literature checks may miss unindexed calculations or a corollary hidden in an equivalent graph-complex formulation. No independent external audit has been performed.

## References
[1] H. Adams, S. Shukla, A. Singh, “Čech complexes of hypercube graphs,” first public 12 December 2022, arXiv:2212.05871, https://arxiv.org/abs/2212.05871.

[2] C. Previte, “The D-neighborhood complex of a graph,” thesis, 2014, https://doi.org/10.25675/3.018305.

[3] T. Matsushita, “Closed neighborhood complexes of graphs,” arXiv:2511.12608, first public 16 November 2025, https://arxiv.org/abs/2511.12608.
