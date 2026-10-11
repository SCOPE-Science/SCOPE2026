# The Paley-29 Rips complex has 29 Klein-bottle links and integral two-torsion

## Finding

Let \(P_{29}\) be the Paley graph on \(\mathbb F_{29}\), with two distinct vertices adjacent precisely when their difference is a nonzero square. Give the vertices unit-edge shortest-path distance. At inclusive Vietoris–Rips scale \(1\), its clique complex \(K=\mathrm{VR}_{\le}(P_{29};1)\) is a connected, nonorientable, normal three-dimensional pseudomanifold with **exactly 29 singular vertices**. The link of every vertex is a triangulated Klein bottle; the link of every edge is a six-cycle; every triangle has precisely two tetrahedral cofaces. The integral homology groups are

\[
H_i(K;\mathbb Z)\cong\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z^{28}\oplus\mathbb Z/2,&i=2,\\
0,&\text{otherwise}.
\end{cases}
\]

In particular, over \(\mathbb F_2\), the Betti numbers in dimensions \(0,1,2,3\) are \((1,0,29,1)\), whereas over \(\mathbb Q\) they are \((1,0,28,0)\). Since the Paley graph has diameter \(2\), the inclusive graph-distance Rips filtration consists of 29 points for \(0\le r<1\), this pseudomanifold for \(1\le r<2\), and a full simplex for \(r\ge2\). These coefficient-dependent dimensions specify the entire positive-length ordinary field-valued barcode: over \(\mathbb F_2\), \(29\) degree-two bars and one degree-three bar \([1,2)\); over characteristic different from \(2\), \(28\) degree-two bars \([1,2)\). The degree-zero barcode has \(28\) bars \([0,1)\) and one infinite bar. No degree-one positive-length bars occur.

## Assumptions and scope

For the field \(\mathbb F_{29}\), write \(Q=\{x^2\bmod29:1\le x\le28\}\). Its 14 elements exclude zero and are closed under negation. Define \(G\) with vertex set \(\{0,\ldots,28\}\) and undirected edge \(\{a,b\}\) if and only if \((a-b)\bmod29\in Q\). The simplices of \(K\) are all nonempty vertex sets spanning complete subgraphs of \(G\), with the usual empty face. Orient simplices by increasing vertex order. All topology here is that of finite geometric realizations. The field-valued persistence assertions use conventional half-open barcode intervals for the inclusively filtered complexes.

## Proof

**Exact combinatorial structure.** Direct exhaustive enumeration using the finite-field adjacency test gives precisely \(29\) vertices, \(203\) edges, \(406\) triangles and \(203\) tetrahedra, and no clique of size at least five. Every triangle is incident to exactly two tetrahedra. The tetrahedron adjacency graph across triangles is connected. For each of the \(203\) edges, the simplicial link is a connected six-cycle. For each of the \(29\) vertices, the link is a connected closed triangulated surface with face vector \((14,42,28)\), hence Euler characteristic \(0\). The explicit orientation-propagation test on adjacent triangles fails on a closed loop in every vertex link, so by the classification of closed connected surfaces the link is a Klein bottle, not a torus. The same orientation test fails on the tetrahedral adjacency graph. Thus \(K\) is a connected nonorientable normal three-pseudomanifold with its vertex set precisely the singular locus. Each assertion is verified directly by the standalone `verify.py` enumerator; the checked finite sets and sign rules completely determine the computation.

**The top boundary and two-torsion.** The integral simplicial map \(\partial_3:C_3(K;\mathbb Z)\to C_2(K;\mathbb Z)\) is a \(406\)-by-\(203\) matrix. Every row has exactly two entries, each \(\pm1\), because every triangle meets two tetrahedra. Thus this is the signed incidence matrix of the connected dual graph. Choose a spanning tree on the \(203\) tetrahedra, reorient columns along this tree, and perform unimodular integer row and column operations on the \(202\) tree-edge rows. This gives \(202\) unit diagonal entries and a residual column whose nonzero entries are all \(\pm2\) whenever a dual non-tree edge gives an orientation contradiction; all other entries are zero. Nonorientability ensures at least one such contradiction. Hence the exact Smith factors of \(\partial_3\) are \(202\) units and a single \(2\); in particular \(\ker\partial_3=0\), and

\[
\operatorname{coker}(\partial_3)\cong \mathbb Z^{203}\oplus\mathbb Z/2.
\]

**The first boundary and remaining homology.** A breadth-first spanning tree of the connected primal graph has \(28\) edges, so the integral one-cycle lattice \(\ker\partial_1\) is freely coordinatized by its \(175\) non-tree edges. Projecting the boundaries of all \(406\) triangles onto these coordinates gives an integer presentation for \(H_1(K;\mathbb Z)\). The supplied verifier performs \(175\) successive pivots of magnitude \(1\), updating the full sparse integer matrix with unimodular operations and exhausting every cycle coordinate. Hence \(H_1(K;\mathbb Z)=0\) and \(\operatorname{im}\partial_2\) is a free abelian group of rank \(175\). There is a short exact sequence

\[
0\to H_2(K;\mathbb Z)\to \operatorname{coker}(\partial_3)\xrightarrow{\overline{\partial_2}}\operatorname{im}\partial_2\to0.
\]

Since the rightmost group is free, this sequence splits as abelian groups. Therefore the torsion of \(H_2\) is precisely \(\mathbb Z/2\), and its free rank is \(203-175=28\). Connectivity supplies \(H_0=\mathbb Z\); the absence of higher simplices and injectivity of \(\partial_3\) give all other vanishing statements.

**Persistence.** Directly checking the common-neighbor counts gives strongly regular parameters \((29,14,6,7)\), hence graph diameter \(2\). The only nontrivial positive-dimensional filtration value is \(1\); the complexes before and after are a discrete set and a full simplex. Thus each homology class in dimensions at least one is born at \(1\) and dies at \(2\). Universal coefficients give the stated characteristic-dependent Betti numbers: the \(\mathbb Z/2\) in degree two contributes one extra degree-two \(\mathbb F_2\) class and one degree-three \(\mathbb F_2\) class via the Tor term. In degree zero, all vertices merge at \(1\).

## Verification

Run `python3 verify.py` with Python 3 and no nonstandard dependencies. The verifier constructs adjacency from quadratic residues, enumerates every possible clique through size five (and excludes larger cliques), computes primal and dual connectivity, checks all vertex and edge links and local orientation contradictions, executes the integer unit-pivot elimination for the one-cycle lattice, and independently computes all three nonzero mod-two boundary ranks. Its expected output begins with `VERIFY_OK` and reports `vertices=29 edges=203 triangles=406 tetrahedra=203`, `unit_d2_pivots=175`, and `mod2_ranks=(28,175,202)`. The proof of the signed-incidence Smith factors is supplied above and depends on the verified global dual connectivity, two-coface condition, and nonorientable sign obstruction; the program checks these hypotheses rather than trusting precomputed Smith-normal-form logs.

## Relationship to prior work

Adamaszek and Adams [1] furnish early Vietoris–Rips homotopy methodology for circular metrics, but neither the Paley graph nor its integral torsion is covered by their circle classification. Cioabă, Guo, Ji and Mim [2], especially Theorem 5.21 and its Paley-29 example, previously establish a vanishing result for first cohomology in a strongly regular graph setting; **vanishing first cohomology is not claimed as new here**. Their inspected example and results do not determine the integral second homology or the Klein-bottle vertex links. Rinaldo and Romeo [3] study Paley-17 in a different, two-dimensional vertex-decomposability setting. The metric graph data [4] confirm the Paley-29 graph parameters and diameter, not the integral clique-complex classification.

## Limitations

The result is for the unique explicitly defined 29-vertex quadratic-residue graph and its inclusive graph-distance filtration only; it does not classify all strongly regular graphs of parameters \((29,14,6,7)\), all Paley graphs, the integral cohomology ring, or the full homotopy type. The signs and unit pivots are exact finite computations, not evidence of an all-parameter theorem. A search of accessible publications and indexed results cannot exclude equivalent statements in unindexed sources. The paper [2] already establishes related first-cohomology vanishing; this finding's distinctive content is the 29 Klein links and exact integral two-torsion.

## References

[1] M. Adamaszek and H. Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669 (first version 2015-03-12); *Pacific Journal of Mathematics* 290 (2017), 1–40; DOI 10.2140/pjm.2017.290.1. https://arxiv.org/abs/1503.03669

[2] S. M. Cioabă, K. Guo, C. Ji and M. Mim, *Clique complexes of strongly regular graphs, their eigenvalues, and cohomology groups*, *Linear Algebra and its Applications* 730 (2026), 152–197, DOI 10.1016/j.laa.2025.10.013. Full text: https://pure.uva.nl/ws/files/302796852/Clique_complexes_of_strongly_regular_graphs_their_eigenvalues_and_cohomology_groups.pdf

[3] G. Rinaldo and F. Romeo, *2-Dimensional vertex decomposable circulant graphs*, 2020, accessible full text https://ssmr.ro/bulletin/pdf/63-3/articol_7.pdf

[4] DistanceRegular.org, *Paley graph P29*, https://www.math.mun.ca/distanceregular/graphs/paley29.html
