# The 336-automorphism homology character of the Heawood two-point configuration space

## Finding
Let \(H\) be the incidence graph of the Fano plane, and let \(X=\operatorname{UConf}_2(|H|)\) be the space of unordered pairs of distinct points on its geometric realization. The full graph automorphism group \(G=\operatorname{Aut}(H)\) has order \(336\). The complete nonzero rational homology is \(H_0(X;\mathbb Q)\cong\mathbb Q\), \(H_1(X;\mathbb Q)\cong\mathbb Q^8\), and \(H_2(X;\mathbb Q)\cong\mathbb Q^{14}\). The integral top homology is \(H_2(X;\mathbb Z)\cong\mathbb Z^{14}\); all higher homology is zero.

The **new classification** is the full rational \(G\)-character on second homology, including automorphisms exchanging points and lines of the Fano plane:

| Automorphism type | Order | Number of elements | Trace on \(H_1(X;\mathbb Q)\) | Trace on \(H_2(X;\mathbb Q)\) |
|---|---:|---:|---:|---:|
| Point/line preserving | 1 | 1 | 8 | 14 |
| Point/line preserving | 2 | 21 | 0 | -2 |
| Point/line preserving | 3 | 56 | -1 | -1 |
| Point/line preserving | 4 | 42 | 0 | 2 |
| Point/line preserving | 7 | 48 | 1 | 0 |
| Point/line exchanging | 2 | 28 | -2 | -2 |
| Point/line exchanging | 6 | 56 | 1 | 1 |
| Point/line exchanging | 8 | 84 | 0 | 0 |

All elements of a displayed type and order have the displayed traces; the two order-seven classes each contain 24 elements and have equal traces. This table determines the entire characteristic-zero representation up to isomorphism. The second-homology character has inner product \(2\) with itself, so its complexification is a direct sum of two **distinct irreducible constituents**, each occurring once. No positive-degree rational homology is invariant under all automorphisms. Consequently the quotient \(X/G\) is rationally acyclic: \(\widetilde H_i(X/G;\mathbb Q)=0\) for all \(i\ge0\).

## Assumptions and scope
Let \(P=\mathbb F_2^3\setminus\{0\}\). Label points by \(P\) and lines by a second copy of \(P\), interpreted as the seven nonzero linear functionals. Join a point \(p\) to a line \(\ell\) exactly when \(p\cdot\ell=0\) over \(\mathbb F_2\). This is the connected, 14-vertex, 21-edge, cubic Heawood graph. Its 336 automorphisms consist of the 168 collineations \((p,\ell)\mapsto(Ap,A^{-T}\ell)\) and the 168 dualities \((p,\ell)\mapsto(A^{-T}\ell,Ap)\), with \(A\in\mathrm{GL}_3(\mathbb F_2)\). The action on \(X\) sends unordered configurations forward vertexwise and edgewise. All homology here is ordinary singular homology, not homology of the graph's matching complex, independence complex, or ordered configuration space.

The graph is simple and has no loops. For two particles, the unordered Abrams cubical subcomplex \(D\) formed by configurations on vertex-disjoint closed graph cells includes into \(X\) as an equivariant homotopy equivalence on homology. A subdivision condition sufficient for the ordinary configuration-to-discrete equivalence is satisfied without subdivision: paths between essential vertices have at least one edge, and simple cycles have at least three edges. The graph's girth is six. The inclusion is natural under every graph automorphism, so the rational homology representations coincide.

## Proof
**1. The exact cubical model.** Orient every graph edge from its point endpoint to its line endpoint. The zero-cells of \(D\) are unordered pairs of distinct vertices, the one-cells are a graph edge and a vertex not incident to it, and the two-cells are unordered pairs of vertex-disjoint edges. Thus \((|C_0|,|C_1|,|C_2|)=(91,252,168)\). The one-cell boundary is \(\partial[e,v]=[b,v]-[a,v]\) for oriented edge \(e:a\to b\). For the ordered edge indices \(i<j\), the square boundary is \(\partial[e_i,e_j]=[e_j,b_i]-[e_j,a_i]+[e_i,a_j]-[e_i,b_j]\). Direct cancellation proves \(\partial_1\partial_2=0\).

The accompanying code reconstructs every cell and verifies the chain identity for all 168 squares. Gaussian elimination modulo three yields \(\operatorname{rank}_{\mathbb F_3}\partial_1=90\) and \(\operatorname{rank}_{\mathbb F_3}\partial_2=154\); therefore their rational ranks are **at least** these values, not merely inferred from floating-point computations. The 14 explicitly listed signed integral vectors in `heawood_cycles.json` each have zero two-boundary, and their reductions modulo three are independent. Since \(C_2\) has dimension 168, these certificates force \(\operatorname{rank}_{\mathbb Q}\partial_2\le154\); the modular lower bound proves equality. The zero-boundary rank cannot exceed 90 because every one-cell boundary has coefficient sum zero; hence \(\operatorname{rank}_{\mathbb Q}\partial_1=90\). We obtain \(\dim H_2=168-154=14\) and \(\dim H_1=252-90-154=8\). The second homology is the kernel of an integer matrix with no incoming differential, and hence is a free abelian group of rank 14. Connectedness follows also from \(\operatorname{rank}\partial_1=90\). There are no cells of dimension greater than two.

**2. The natural first-homology representation.** There is an automorphism-equivariant cellular chain map \(p:C_*(D;\mathbb Q)\to C_*(H;\mathbb Q)\) given by \(p([u,v])=u+v\), \(p([e,v])=e\), and \(p([e_i,e_j])=0\). The prescribed boundary identities show that \(p\) is a chain map. Choose a breadth-first spanning tree of \(H\) rooted at any vertex. Every vertex has tree depth at most three; the eight fundamental cycles have length at most seven and hence each avoids some graph vertex. Place one particle at such an omitted vertex while the other traverses the fundamental cycle. This realizes a one-cycle of \(D\) mapping to the fundamental graph cycle. Thus \(p_*:H_1(D;\mathbb Q)\twoheadrightarrow H_1(H;\mathbb Q)\) is surjective. Both spaces have first Betti number eight, so this map is an isomorphism of rational \(G\)-representations. The eight-dimensional *nonequivariant* rank is also consistent with Ko and Park's previously established graph-braid homology formula and is not claimed as new.

For any graph automorphism \(g\), let \(t_V(g)\) be its trace on the fourteen-dimensional vertex permutation chain group, and \(t_E(g)\) its **signed** trace on the oriented 21-edge chain group. Because \(H\) is connected, \(\operatorname{tr}(g|H_1(H;\mathbb Q))=1-t_V(g)+t_E(g)\).

**3. Character calculation.** Each graph automorphism acts by a signed permutation on each cubical chain group. Write \(t_i(g)=\operatorname{tr}(g|C_i(D;\mathbb Q))\). The cellular Lefschetz identity and the first-homology isomorphism give the **exact** formula
\[
\operatorname{tr}(g|H_2(X;\mathbb Q))
=t_0(g)-t_1(g)+t_2(g)-t_V(g)+t_E(g).
\]
A fixed zero-cell is an unordered two-vertex set stabilized by \(g\). A fixed one-cell is an edge–vertex pair fixed with its orientation sign. A fixed two-cell is an unordered pair of disjoint edges stabilized by \(g\), counted with the product of edge-orientation signs and an additional minus sign if the two edges are exchanged. These are exhaustive, finite signed-permutation rules, not approximations.

Enumerate the 168 nonsingular binary three-by-three matrices and their 168 point–line dualities. The verifier enumerates and validates all 336 vertex permutations, reconstructs each signed edge permutation, and evaluates the preceding traces for **every** element, obtaining exactly the eight rows in the table. The type/order classes contain respectively \(1,21,56,42,48,28,56,84\) elements, summing to 336. There are no omitted group elements. The character-square sum equals \(672\), and division by 336 gives inner product \(2\), proving the assertion about two inequivalent complex irreducible constituents. The weighted sums of both positive-degree characters over the 336 elements are zero. Averaging over a finite group over \(\mathbb Q\) identifies quotient homology with invariants, so \(X/G\) has only rational \(H_0\).

## Verification
Run `python heawood_verify.py` in a directory containing `heawood_cycles.json`. No packages beyond the Python standard library are required. The script regenerates the 14 points/lines, all graph edges and all unordered discrete configuration cells, checks all chain identities, verifies the rank-154 nonzero minor modulo three, checks the 14 independent integral two-cycles, verifies a breadth-first fundamental cycle bound, and enumerates all 336 automorphisms and signed traces. It also checks the distinct mod-two rank 153, consistent with the previously known two-primary first-homology phenomenon. Output from executing the bundled source is in `heawood_verify_output.txt`; its final line reports the character self inner product as two. The verifier's first line is `HEAWOOD_VERIFY_OK`.

The finite computations are exhaustive for **this finite graph**, not a claim about an infinite family. Independence of the integral cycles and modular rank bounds together establish the rational rank exactly; the mod-two rank comparison by itself is not used as a complete Smith normal form.

## Relationship to prior work
Barnett and Farber (2009) supply foundational ordered two-point graph-configuration topology and the deleted-product model. Ko and Park (2011), Theorem 3.16, determines the first-homology rank and torsion of unordered graph braid groups for broad graph classes, including nonplanar 3-connected graphs such as \(H\). Its first-rank consequence, together with the Euler characteristic of the two-particle cubical complex, also gives the ordinary top Betti number fourteen. These nonequivariant quantities are acknowledged antecedents, not presented as new. Kurlin (2009 preprint, subsequently 2012) explains graph-braid discrete models and presentations. The additional contribution here is the **complete, full-order-336 rational homology character**, including dualities, exact multiplicity-free decomposition criterion, and rational quotient consequence; these are not stated by the cited rank or presentation theorems.

An indexed calculation of the **ordered**, mod-two, two-point Heawood space describes a different space and coefficient field; it does not imply the full rational action on this **unordered** space. Published equivariant calculations for matching/independence complexes of the Heawood graph likewise concern different complexes. Published symmetry calculations for unordered two-point spaces on Petersen, cuboctahedral and dodecahedral graphs use a related method but different graph actions. Search failure alone does not establish publication priority.

## Limitations
This is the rational representation and integral top-homology classification for **two unordered particles on this one graph**, not a classification of more particles, arbitrary incidence graphs or all graph braid groups. The result does not determine integral \(G\)-lattices, cup products, or torsion in the quotient. The first-homology rank, the two-primary torsion in unordered graph braid abelianization, and the top-homology rank are already consequences of earlier general work; only the explicit full symmetry character and deductions using it are advanced as original. Unindexed equivalent computations or general character formulas not located remain publication-priority risks.

## References
1. K. Barnett and M. Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, first public arXiv version 2009-03-12, https://arxiv.org/abs/0903.2180 (general ordered-configuration results; not this character).
2. K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, first public arXiv version 2011-01-13, https://arxiv.org/abs/1101.2648 (Theorem 3.16; pre-existing nonequivariant first-homology information).
3. V. Kurlin, *Computing braid groups of graphs with applications to robot motion planning*, arXiv 2009-08-07, https://arxiv.org/abs/0908.1067 (discrete graph-configuration models).
4. T. Maciążek and A. Sawicki, *Non-abelian quantum statistics on graphs*, Communications in Mathematical Physics (2019), https://doi.org/10.1007/s00220-019-03583-5 (higher-particle graph homology methods and wheel-graph examples, not a Heawood automorphism character).
