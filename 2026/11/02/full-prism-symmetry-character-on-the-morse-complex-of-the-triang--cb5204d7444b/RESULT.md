# Full prism-symmetry character on the Morse complex of the triangular prism

## Finding
Let \(P=C_3\mathbin{\square}K_2\) be the triangular-prism graph, let \(X=\mathfrak M(P)\) be the simplicial complex of acyclic vertex-edge matchings, and let \(G=\operatorname{Aut}(P)\cong S_3\times C_2\). Let \(\mathbf1\), \(\operatorname{sgn}\), and \(V\) denote respectively the trivial, sign, and two-dimensional standard rational representations of \(S_3\). Let \(\varepsilon\) be the nontrivial character of the layer-interchange factor \(C_2\). Then the complete rational fourth-homology representation is
\[
\widetilde H_4(X;\mathbb Q)\cong
(3\mathbf1\oplus7\operatorname{sgn}\oplus10V)\boxtimes\mathbf1
\;\oplus\;
(8\mathbf1\oplus4\operatorname{sgn}\oplus11V)\boxtimes\varepsilon.
\]
In particular, the two eigenspaces for layer interchange have dimensions \(30\) and \(34\), and the full symmetry quotient has precisely three independent positive-degree rational homology classes:
\[
\widetilde H_j(|X|/G;\mathbb Q)\cong
\begin{cases}\mathbb Q^3,&j=4,\\0,&j\ne4.\end{cases}
\]
This is an equivariant classification. The nonequivariant homotopy equivalence \(X\simeq\bigvee^{64}S^4\) was previously established and is not presented as new.

## Assumptions and scope
The graph \(P\) has vertices \(0,1,2,3,4,5\), triangle edges \(01,02,12,34,35,45\), and matching edges \(03,14,25\). A vertex of \(X\) is an incidence \((v,e)\) with \(v\in e\). A subset of these 18 incidences is a simplex if each graph vertex and graph edge is used at most once, and directing every chosen edge from its matched vertex to its other endpoint produces no directed cycle. This is the ordinary simplicial Morse complex of a graph, not its pure subcomplex or generalized matching complex. The graph has exactly two triangles, and its remaining three edges form a perfect matching between those triangles. Hence every graph automorphism either preserves or exchanges the two triangles, with a common arbitrary permutation of their three matched columns. This proves that its full automorphism group is \(S_3\times C_2\). All representation statements use rational coefficients and the natural induced simplicial action.

## Proof
**1. Exact finite model and homology concentration.** Order the nine graph edges lexicographically and the 18 vertex-edge incidences lexicographically. Represent every subset by its 18-bit mask. Exhaustively enforce distinct outgoing tails, distinct selected undirected edges, and absence of directed cycles. This produces \((1,18,126,428,705,450)\) simplices by cardinality \(0,1,2,3,4,5\), respectively, and none of greater cardinality. A second enumeration over all \(2^9=512\) undirected edge subsets retains spanning forests and selects one root for each component; orienting each tree towards its chosen root reproduces exactly the same 1,728 masks. The correspondence is exact: an undirected cycle in a selected orientation with outdegree at most one forces each of its vertices to have one outgoing cycle edge and hence forces a directed cycle. Conversely, a selected undirected forest with no repeated outgoing tail and no directed cycles has precisely one unmatched root in each tree component, and every edge points toward it.

A deterministic face-poset matching processes the incidence indices in the order
`1,9,2,13,14,8,16,17,15,12,4,0,3,7,10,5,6,11`.
At each index, pair each still-unmatched face missing the index with its one-vertex extension whenever both remain unmatched. This produces 831 matched pairs. Exactly one vertex and 64 four-dimensional simplices are unmatched. For all 6,606 codimension-one incidences among nonempty faces, orient unmatched incidences downward and matched incidences upward. The supplied finite checker topologically sorts the entire directed graph of 1,727 faces; all 1,727 are visited. Consequently the matching is acyclic. Forman's discrete Morse theorem gives a CW complex with one zero-cell and 64 four-cells and no other cells. All attaching maps are null because the lower skeleton is a point. Thus independently \(X\simeq\bigvee^{64}S^4\), confirming the previously published nonequivariant premise without claiming it as a new result.

**2. Exact signed Lefschetz traces.** For every \(g\in G\), permute the 18 incidence vertices via the graph automorphism. If a nonempty simplex \(\sigma\) is fixed setwise, its contribution to the simplicial Lefschetz number is \((-1)^{\dim\sigma}\) times the sign of the induced permutation of its vertices; otherwise the contribution is zero. Since only ordinary degree zero and reduced degree four homology remain, \(\chi_4(g)=L(g)-1\). Exhaustive calculation for all twelve elements gives this complete class table:

| Action on columns | Layer interchange | Number of elements | \(L(g)\) | \(\chi_4(g)\) |
| --- | --- | ---: | ---: | ---: |
| Identity | No | 1 | 65 | 64 |
| Transposition | No | 3 | 1 | 0 |
| Three-cycle | No | 2 | 2 | 1 |
| Identity | Yes | 1 | -3 | -4 |
| Transposition | Yes | 3 | -7 | -8 |
| Three-cycle | Yes | 2 | 0 | -1 |

**3. Exact decomposition.** Apply the character inner-product formula to the six rational irreducibles of \(S_3\times C_2\), using \(S_3\) characters \((1,1,1)\), \((1,-1,1)\), and \((2,0,-1)\) on identity, transpositions, and three-cycles. The multiplicities are \((3,7,10)\) for even layer parity and \((8,4,11)\) for odd layer parity. Their dimension is \(3+7+20+8+4+22=64\), confirming the stated decomposition.

**4. Quotient consequence.** Over \(\mathbb Q\), the cellular chains of an equivariant barycentric subdivision of the finite orbit space compute the \(G\)-coinvariants of the chains of \(X\). Averaging is exact in characteristic zero; hence quotient rational homology is the invariant part of \(H_*(X;\mathbb Q)\). The trivial \(G\)-representation has multiplicity three in degree four, and there are no other positive-degree rational groups. This proves the quotient formula.

## Verification
Run `python3 verify.py` with Python's standard library. The checker independently enumerates all simplices from directed partial matchings and from rooted undirected forests. It verifies the deterministic 831-pair acyclic matching, the 6,606-incidence topological sort, all twelve graph-automorphism actions, the signed simplex traces, all six rational multiplicities, and the dimension and invariant-subspace checks. The expected final line is `TRIANGULAR_PRISM_MORSE_64S4_FULL12_CHARACTER_OK`. The reported full character is independently reproducible from the explicit six class representatives and signed Lefschetz formula above; no floating-point arithmetic is required.

## Relationship to prior work
Donovan, Lin, and Scoville (2019) define Morse complexes and determine their topology for several classes of graphs, without providing the prism's full rational character. Scoville and Zaremsky (2020) prove general connectivity bounds that do not determine this representation. Two published, directly overlapping calculations already settle (i) the triangular-prism Morse complex's mod-two Betti vector and (ii) its entire nonequivariant integral homotopy type, including the identification with the second Morse iterate of the three-cycle. Those earlier facts are expressly excluded from the new claim. Their homotopy equivalence determines the dimension \(64\) and the identity trace, but cannot determine the five nonidentity traces, six irreducible multiplicities, or quotient invariants; the exact signed action computation is additional information. Other published equivariant Morse results found concern different graphs, such as complete bipartite graphs and triangular books, with no implication establishing the displayed prism character.

## Limitations
The classification is a rational representation of the full twelve-element graph automorphism group. It does not identify an integral \(\mathbb Z[G]\)-lattice, give equivariant attaching maps or fixed-point-set homotopy types, or extend to longer prisms. The historical wedge-of-spheres claim is already known, not a second finding. An inaccessible 2020 thesis on directed forest complexes of Cayley graphs remains a bibliographic uncertainty; its available abstract is insufficient for a definitive whole-document non-coverage conclusion. This finite result has not received independent external mathematical review.

## References
1. Connor Donovan, Maxwell Lin, Nicholas A. Scoville, *On the homotopy and strong homotopy type of complexes of discrete Morse functions*, arXiv:1909.11440, first submitted 2019-09-25, https://arxiv.org/abs/1909.11440.
2. Nicholas A. Scoville and Matthew C. B. Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481, first submitted 2020-04-22, https://arxiv.org/abs/2004.10481.
3. *The second discrete-Morse iterate of a triangle is a wedge of sixty-four four-spheres*, published result, public identifier `2026/10/11/SCOPE-the-second-discrete-morse-iterate-of-a-triangle-is-bigvee-64-s-4--5138f6290b59`.
4. *Mod-2 homology of the triangular-prism Morse complex*, published result, public identifier `2026/10/4/SCOPE-mod-2-homology-of-the-triangular-prism-morse-complex--4af8059de6d1`.
5. Kennedy Courtney, *The Directed Forest Complex of Cayley Graphs*, M.S. thesis, Boise State University, 2020, https://scholarworks.boisestate.edu/td/1684/.
