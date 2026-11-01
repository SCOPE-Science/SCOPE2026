# Full \(S_4\times C_2\) symmetry of the cuboctahedral matching complex

## Finding
Let \(Q_3\) be the cube graph, \(C=L(Q_3)\) the cuboctahedral graph, and \(K=\operatorname{Match}(C)=\operatorname{Ind}(L(C))\) its ordinary edge-matching complex. The full automorphism group is \(G\cong S_4\times C_2\), where \(S_4\) is the rotation group and the central involution is geometric inversion. Denote the rational Specht module of shape \(\lambda\vdash4\) by \(V_{\lambda}\), and use superscript \(+\) or \(-\) for the action of central inversion. Then the complete positive-degree rational homology representation is
\[
\begin{aligned}
\widetilde H_3(K;\mathbb Q)\cong{}&V_{(4)}^+\oplus2V_{(4)}^-\oplus5V_{(3,1)}^+\oplus2V_{(3,1)}^-\\
&\oplus5V_{(2,2)}^+\oplus4V_{(2,2)}^-\oplus2V_{(2,1,1)}^+\oplus2V_{(2,1,1)}^-\\
&\oplus2V_{(1,1,1,1)}^+\oplus V_{(1,1,1,1)}^-.
\end{aligned}
\]
All other reduced rational homology vanishes. Consequently central inversion has eigenspace dimensions \(34\) and \(23\), the invariant dimensions under \(G\) and its rotation subgroup are respectively \(1\) and \(3\), and the ordinary orbit spaces have \(\widetilde H_3(K/G;\mathbb Q)\cong\mathbb Q\) and \(\widetilde H_3(K/S_4;\mathbb Q)\cong\mathbb Q^3\), with no other reduced rational homology.

## Assumptions and scope
The cube has vertex set \(\{0,\ldots,7\}\), with an edge \(\{u,v\}\) precisely when the three-bit exclusive-or \(u\oplus v\) is one of \(1,2,4\). Index the twelve cube edges lexicographically. The cuboctahedron \(C=L(Q_3)\) has these twelve cube edges as vertices, adjacent when they share a cube endpoint. Index its twenty-four edges lexicographically as \(e_0,\ldots,e_{23}\). A \(q\)-simplex of \(K\) is a set of \(q+1\) pairwise vertex-disjoint edges of \(C\); its orientation is increasing edge-index order. This is **not** the matching complex of the cube, the perfect-matching-only subcomplex, or a two-particle configuration space.

Every cube symmetry is a signed coordinate permutation \(g=(\sigma,b)\), with \(\sigma\in S_3\), \(b\in(\mathbb Z/2)^3\), acting by coordinate permutation followed by bit flips. These forty-eight transformations exhaust \(\operatorname{Aut}(C)\). Indeed, the eight maximal triangles of \(C\) are precisely the three-edge stars at the eight cube vertices: the cube has no triangles, and every three pairwise incident cube edges have a common endpoint. Their intersections recover the cube graph, so every cuboctahedral automorphism arises from a cube automorphism. The orientation-preserving subgroup acts faithfully on the four antipodal cube body-diagonal pairs and is \(S_4\); the central inversion \(z\) flips all three coordinates. This determines the group-product and the \(\pm\) convention uniquely.

## Proof
**Exact integral homology premise.** The nonempty simplex counts in dimensions \(0,1,2,3,4,5\) are, respectively,
\[(24,204,744,1116,528,32).\]
A standalone finite certificate is supplied. Starting with all nonempty simplices, for pivots \(j=0,\ldots,23\) pair each still-unmatched face not containing \(e_j\) to its union with \(e_j\), whenever both are still unmatched, and remove both. This produces exactly \(1287\) pairs. Reversing the corresponding matched edges of the complete Hasse diagram produces a directed graph on \(2648\) vertices with \(9936\) arrows; an exhaustive topological sort visits every vertex, proving acyclicity. There remain one critical zero-cell, sixty-five critical three-cells, and eight critical four-cells, with no other critical cells.

The oriented integral Morse boundary from the eight critical four-cells to the sixty-five critical three-cells is reconstructed by exact signed gradient-path reduction. In lexicographic order of the critical face tuples, its rows \(6,41,4,5,52,15,36,37\), against the eight critical four-cell columns, form the diagonal matrix \(\operatorname{diag}(1,-1,-1,-1,-1,-1,-1,-1)\). Their twenty-four-bit face masks are `0x404802`, `0x140048`, `0x22802`, `0x402802`, `0x800908`, `0x402044`, `0x80148`, `0x800148`. This is a unimodular maximal minor, so the attaching map is a primitive injection of free integral groups. The three-skeleton of the Morse CW model is a wedge of sixty-five three-spheres; each four-cell attachment is determined by its integral degree vector because \(\pi_3\) of this simply-connected wedge equals \(H_3\). Changing the three-sphere basis and canceling the eight primitive attachments gives
\[K\simeq\bigvee^{57}S^3.\]
Thus \(\widetilde H_3(K;\mathbb Z)\cong\mathbb Z^{57}\), with no other reduced integral homology. This same-object nonequivariant conclusion has been obtained in an earlier published computation; it is verified here as the prerequisite, **not** claimed as the new representation finding.

**Character reconstruction.** For \(g\in G\), let \(t_q(g)\) be the signed trace of its action on oriented simplicial \(q\)-chains, obtained by summing the induced orientation sign over the \(g\)-invariant matchings of size \(q+1\). As the only nonzero unreduced homology groups are the trivial \(H_0\) and degree-three homology, Euler–Poincaré gives
\[\chi_3(g)=1-\sum_{q=0}^5(-1)^q t_q(g).\]
The forty-eight group elements fall into ten classes. Write \(g=r z^\epsilon\), where \(r\) is a proper cube rotation, \(\epsilon\in\{0,1\}\), and \(\mu\) is the cycle type of \(r\) on the four body diagonals. The exhaustive signed fixed-face calculation gives:

| \(\mu\) | \(\epsilon\) | Class size | \(\chi_3\) |
|---|---:|---:|---:|
| \((1,1,1,1)\) | 0 | 1 | 57 |
| \((1,1,1,1)\) | 1 | 1 | 11 |
| \((2,1,1)\) | 0 | 6 | 3 |
| \((2,1,1)\) | 1 | 6 | 1 |
| \((2,2)\) | 0 | 3 | 13 |
| \((2,2)\) | 1 | 3 | -1 |
| \((3,1)\) | 0 | 8 | -3 |
| \((3,1)\) | 1 | 8 | -1 |
| \((4)\) | 0 | 6 | -3 |
| \((4)\) | 1 | 6 | -5 |

A separate algorithm checks the entire table without summing traces dimension by dimension. Partition the twenty-four cuboctahedral edges into cycles under \(g\); discard any cycle containing incident edges; retain sets of cycles whose edge unions are matchings. A union of \(k\) cycles on \(m\) edge-vertices has orientation sign \((-1)^{m-k}\). Substitution into the alternating chain trace, including the empty matching, gives the exact identity
\[\chi_3(g)=\sum_{T\text{ admissible orbit-cycle sets}}(-1)^{|T|}.\]
The independent orbit-cycle enumeration reproduces all ten entries.

**Irreducible decomposition and quotient consequence.** For the five standard rational characters of \(S_4\), indexed by partitions \((4),(3,1),(2,2),(2,1,1),(1,1,1,1)\), take the inner product with \(\chi_3\) after multiplying by the trivial or sign character of \(\langle z\rangle\). The resulting \((+,-)\) multiplicity pairs in that order are
\[(1,2),\qquad(5,2),\qquad(5,4),\qquad(2,2),\qquad(2,1).\]
Their weighted dimensions sum to \(57\). The inversion character value \(11\) yields eigenspace dimensions \((57+11)/2=34\) and \((57-11)/2=23\). The trivial \(S_4\)-representation occurs once with even and twice with odd inversion sign: hence \(\dim\widetilde H_3(K;\mathbb Q)^G=1\) and \(\dim\widetilde H_3(K;\mathbb Q)^{S_4}=3\). Finally, for a finite group acting simplicially on a finite complex, barycentric subdivision and rational averaging identify ordinary quotient homology with the invariant rational homology. This proves the quotient assertions.

## Verification
The package includes `verify_cubocta_equiv.py` and `verify_orbit_cycles.py`, each standalone and using only Python's standard library. Run `python3 verify_cubocta_equiv.py` and `python3 verify_orbit_cycles.py`. The first checks the simplex census, all \(1287\) discrete-Morse pairs, acyclicity of all \(9936\) Hasse arrows, the exact integral unit minor, all \(48\) signed chain traces, class sizes, character inner products, and quotient invariant dimensions. It terminates with `VERIFY_OK`. The second performs an independent edge-orbit-cycle enumeration for all \(48\) symmetries, ending with `ORBIT_VERIFY_OK`. Recorded outputs accompany the code. Neither verification rests on floating-point arithmetic or a random sample.

## Relationship to prior work
Engström's foundational work on independence complexes of claw-free graphs (2005) includes line graphs as the relevant general setting but proves connectivity properties, not this finite homology character. Freij's general equivariant discrete Morse theory does not state cuboctahedral matching-complex irreducibles. Bate–Everitt–Ford–Ramos determine homology representations of matching complexes of **complete hypergraphs**, not matchings in the twenty-four-edge cuboctahedral graph. Li studies graded **permutation representations on matchings**, rather than this third-homology representation; no explicit cuboctahedral character is given.

The closest exact-object published calculation, *The cuboctahedral matching complex is a wedge of \(57\) three-spheres*, determines its full integral nonequivariant homotopy type but does not compute the action of any nonidentity graph automorphism. An independently published computation of the ordinary matching complex of the **octahedral** graph has the same automorphism-group abstract type but concerns a different six-vertex graph and a degree-one homology module of rank eleven. The full homology modules of two-particle configuration spaces **on** the cuboctahedral graph concern a different topological space, with nonzero homology in degrees one and two; their formulas do not imply this matching-complex representation. These distinctions concern the objects and implication relations, not merely differences in titles.

## Limitations
The theorem concerns the rational irreducible \(G\)-module in degree three. Although the integral homology is free of rank \(57\), this does not classify its integral representation lattice or integral homology of the symmetry quotients. Rational homology of a quotient does not prove it is homotopy equivalent or homeomorphic to a three-sphere. The search cannot exclude an equivalent unindexed calculation. No independent mathematical audit has been performed.

## References
1. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420v1, first public 2005-12-17, especially Section 2. https://arxiv.org/html/math/0512420v1
2. R. Freij, *Equivariant discrete Morse theory*, Discrete Mathematics 309 (2009), 3821–3829. https://doi.org/10.1016/j.disc.2008.10.029
3. M. Bate, B. Everitt, S. Ford, E. Ramos, *Homology of matching complexes and representations of symmetric groups*, arXiv:2312.13750v3, especially Theorems 1.1 and 2.1. https://arxiv.org/html/2312.13750v3
4. S. Li, *Equivariant log-concavity of graph matchings*, arXiv:2202.08828v2. https://arxiv.org/html/2202.08828v2
5. *The cuboctahedral matching complex is a wedge of \(57\) three-spheres*, published research record (full result examined). https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-the-cuboctahedral-matching-complex-is-a-wedge-of-57-three-sphere--42f20681b118/RESULT.md
6. *The full octahedral symmetry representation of the matching complex*, published research record (full result examined). https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-the-full-octahedral-symmetry-representation-of-the-matching-comp--c700eceb52bb/RESULT.md
7. *Full symmetry modules of the cuboctahedral two-particle configuration space*, published research record (full result examined). https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-full-symmetry-modules-of-the-cuboctahedral-two-particle-configur--5d6ece5c784b/RESULT.md
