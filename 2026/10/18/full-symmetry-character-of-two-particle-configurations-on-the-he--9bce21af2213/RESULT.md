# Full symmetry character of two-particle configurations on the Heawood graph

## Finding
Let \(H\) be the Heawood graph, the point-line incidence graph of the Fano plane, and let \(B_2(H)\) denote its space of unordered pairs of distinct points. Write \(G=\operatorname{Aut}(H)\), of order \(336\). The integral homology groups are
\[
H_0(B_2(H);\mathbb Z)\cong\mathbb Z,\quad
H_1(B_2(H);\mathbb Z)\cong\mathbb Z^8\oplus\mathbb Z/2,\quad
H_2(B_2(H);\mathbb Z)\cong\mathbb Z^{14},
\]
with no homology in higher degrees. The first-homology statement follows from the known triconnected-graph formula; the new result is the complete character of the natural \(G\)-action on rational homology, especially in degree two.

An automorphism either preserves or exchanges the two bipartition classes. In the table, an order together with this exchange flag specifies an entire character-constant subset of \(G\); the cardinalities sum to \(336\). The last two columns are the traces on \(H_1(B_2(H);\mathbb Q)\) and \(H_2(B_2(H);\mathbb Q)\), respectively.

| Element order | Exchanges point/line classes? | Elements | Degree-one trace | Degree-two trace |
| ---: | :---: | ---: | ---: | ---: |
| 1 | No | 1 | 8 | 14 |
| 2 | No | 21 | 0 | -2 |
| 2 | Yes | 28 | -2 | -2 |
| 3 | No | 56 | -1 | -1 |
| 4 | No | 42 | 0 | 2 |
| 6 | Yes | 56 | 1 | 1 |
| 7 | No | 48 | 1 | 0 |
| 8 | Yes | 84 | 0 | 0 |

In particular, both nontrivial rational homology representations have no invariants under either the full automorphism group or its index-two bipartition-preserving subgroup. The reduced rational homology of the corresponding orbit spaces therefore vanishes in every degree.

## Assumptions and scope
Use vertices \(p_i\) and \(\ell_j\), with indices in \(\mathbb Z/7\), and join \(p_i\) to \(\ell_j\) precisely when \(i-j\in\{0,1,3\}\). This is a copy of the Heawood graph. The underlying graph has \(14\) vertices, \(21\) edges and girth \(6\), and is trivalent and three-vertex-connected. The graph is nonplanar: the planar girth-six bound would require \(21\le3(14-2)/2=18\). The graph cycle rank is \(8\).

For the two-particle case, the unordered Abrams cubical model \(D_2(H)\) is a deformation retract of the actual configuration space: the graph meets the standard subdivision conditions (cycles have at least three edges and paths between essential vertices at least one edge). Its cells are unordered pairs of disjoint closed graph cells, with \(91\) zero-cells, \(252\) oriented one-cells and \(168\) oriented two-cells.

## Proof
**First homology and the two-dimensional rank.** Ko and Park's formula for a three-vertex-connected nonplanar graph gives \(H_1(B_2(H);\mathbb Z)\cong\mathbb Z^8\oplus\mathbb Z/2\). The required connectivity is checked exhaustively for all deleted vertex sets of sizes zero, one and two in `verify_cycles.py`, and the nonplanarity argument above is elementary. Since \(D_2(H)\) is connected, has no cells above degree two and has Euler characteristic \(91-252+168=7\), its second rational Betti number is \(14\). The integral second homology is the kernel of a homomorphism between free abelian cellular groups and hence free, giving rank \(14\).

**Canonical identification in degree one.** Define a cellular chain map \(F:C_*(D_2(H))\longrightarrow C_*(H)\) by sending a zero-cell \(\{v,w\}\) to \(v+w\), a one-cell \(\{v,e\}\) (with \(e\) oriented) to \(e\), and every two-cell to zero. The two opposite edges in each square cancel after applying \(F\), so this is a chain map. It commutes with every graph automorphism. Each of the \(28\) six-cycles in \(H\) can be lifted to a one-cycle in \(D_2(H)\): keep one particle at a vertex outside the cycle, and move the other around the cycle. These six-cycles span the eight-dimensional graph cycle space over \(\mathbb Q\). Indeed, `verify_cycles.py` enumerates all \(28\) and checks that their oriented edge vectors have rank \(8\) modulo \(3\), hence also over \(\mathbb Q\). Thus \(F_*:H_1(B_2(H);\mathbb Q)\to H_1(H;\mathbb Q)\) is surjective, and the known equality of dimensions makes it an equivariant isomorphism.

**Characters and the automorphism group.** For each graph automorphism \(g\), let \(t_i(g)\) be the trace on the oriented cellular chain group \(C_i(D_2(H);\mathbb Q)\); let \(u_i(g)\) be its trace on \(C_i(H;\mathbb Q)\). The Hopf trace formula and the preceding equivariant isomorphism yield
\[
\operatorname{tr}(g\mid H_1(B_2(H);\mathbb Q))=u_1(g)-u_0(g)+1,
\]
\[
\operatorname{tr}(g\mid H_2(B_2(H);\mathbb Q))=t_0(g)-t_1(g)+t_2(g)+u_1(g)-u_0(g).
\]
A zero-cell contributes \(1\) precisely when its unordered vertex pair is fixed. A one-cell contributes its oriented-edge sign precisely when both its stationary vertex and its moving edge are fixed. For a square formed by two disjoint oriented edges, a fixed square contributes the product of their orientation signs, multiplied by \(-1\) if the two factors are exchanged. These rules specify every trace without solving for a homology basis.

The seven Fano lines are \(\{j,j+1,j+3\}\) modulo seven. Precisely \(168\) point permutations preserve this collection; each determines the permutation of lines. Composing these collineations with a point-line duality gives the other \(168\) automorphisms. The executable exhaustive computation `verify_configuration.py` checks adjacency preservation and evaluates the preceding signed-cell formulas for all \(336\) automorphisms. Grouping by element order and bipartition exchange gives exactly the table in the Finding. This exhausts \(G\), whose order \(336\) is independently established for the Heawood graph.

**Orbit-space consequence.** For a finite group acting on a finite CW complex, rational homology of the orbit space is the invariant part of rational homology of the original space (after an equivariant subdivision if required). Averaging the character values over either \(G\) or its \(168\)-element color-preserving subgroup yields zero in degrees one and two. Since the space is connected and has no higher-dimensional homology, the reduced rational homology of both quotients is zero.

## Verification
Run `python3 verify_configuration.py` and `python3 verify_cycles.py` with Python 3 and no third-party dependencies. Their expected complete outputs are `CONFIGURATION_CHECK.txt` and `CYCLE_CHECK.txt`. The first reconstructs all \(91\), \(252\), and \(168\) cells and both integral boundary matrices, verifies the composition of boundaries vanishes, computes ranks over five finite fields, enumerates \(336\) edge-preserving automorphisms, and evaluates all signed traces. The second independently checks vertex connectivity, all six-cycles, girth and cycle-span rank. The finite-field calculations are cross-checks; the integer conclusions about first homology use Ko–Park's theorem, and the character identities use the exact chain formulas above.

## Relationship to prior work
Ko and Park, *Characteristics of graph braid groups* (arXiv:1101.2648), Theorem 3.16, provide the known first-homology calculation used here, not an equivariant second-homology character. An and Knudsen, *On the second homology of planar graph braid groups* (arXiv:2008.10371, publicly available August 24, 2020), develop second-homology generators for planar graphs; their Example 6.8 shows limitations in the nonplanar case. That planar classification does not cover the Heawood graph. Lawrence and Wilson, *The Structure of the Heawood Graph* (arXiv:1907.11978), describe its graph automorphisms and cycle structure, not the two-particle configuration homology representation. Prior calculations of mod-two homology for *ordered* Heawood two-point configurations do not specify the rational characters of the *unordered* configuration space. The result here isolates precisely this additional representation-theoretic information.

## Limitations
The result does not determine the integral module structure on second homology, rational cup products, nontrivial fundamental-group presentations, or higher-particle configuration spaces. The degree-two free rank and degree-one abelian group are not claimed as original. A finite literature search cannot exclude an unindexed equivalent symmetry-character calculation; a separate independent mathematical audit has not been performed.

## References
1. K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, arXiv:1101.2648 (January 13, 2011), especially the Abrams model and Theorem 3.16. https://arxiv.org/abs/1101.2648
2. B. H. An and B. Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371 (first public August 24, 2020), especially Sections 1 and 6. https://arxiv.org/abs/2008.10371
3. E. D. Lawrence and R. T. Wilson, *The Structure of the Heawood Graph*, arXiv:1907.11978 (July 27, 2019), Proposition 1 and the cycle computations. https://arxiv.org/abs/1907.11978
