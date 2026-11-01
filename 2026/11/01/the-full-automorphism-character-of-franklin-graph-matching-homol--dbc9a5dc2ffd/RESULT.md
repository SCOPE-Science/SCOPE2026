# The full automorphism character of Franklin-graph matching homology

## Finding
Let \(F\) be the twelve-vertex Franklin graph, and let \(X=\mathcal M(F)\) be its **ordinary matching complex**: vertices of \(X\) are graph edges, and faces are sets of pairwise vertex-disjoint graph edges. Put \(G=\operatorname{Aut}(F)\). Define \(\eta:G\to\{+1,-1\}\) as the sign of the permutation induced on the eighteen **unoriented graph edges**. There are four distinguished Hamiltonian cycles permuted by \(G\); their induced permutation representation identifies \(G/\langle z\rangle\cong S_4\), where \(z(i)=i+6\pmod {12}\). Moreover \(\eta(z)=-1\), giving a canonical splitting \(G\cong S_4\times C_2\) with \(S_4=\ker\eta\).

Write \(S^{\lambda}\) for the rational irreducible representation of \(S_4\) indexed by a partition \(\lambda\) of four, inflated to \(G\) through its four-Hamiltonian-cycle action. The complete nonzero reduced rational homology is
\[
\boxed{\widetilde H_3(X;\mathbb Q)\cong\eta\oplus S^{(3,1)}\oplus(\eta\otimes S^{(3,1)})\oplus S^{(2,2)}\oplus S^{(2,1,1)},}
\]
with all other reduced rational homology groups zero. The integral ordinary homotopy type, already known separately, is \(X\simeq\bigvee^{12}S^3\); the novelty asserted here is the **complete symmetry action**, not this homotopy type.

In particular the full-group invariant subspace is zero, the \(\ker\eta\)-invariant subspace has dimension one, and the central half-turn \(z\) has trace four, splitting rational third homology into eigenspaces of dimensions eight and four. Thus the **ordinary geometric quotients** satisfy
\[
\widetilde H_*(|X|/G;\mathbb Q)=0,\qquad
\widetilde H_3(|X|/\ker\eta;\mathbb Q)\cong\mathbb Q,
\]
and all other reduced rational homology of the latter quotient vanishes. These are rational statements, not claims of integral representation-lattice decomposition or quotient homotopy equivalence.

## Assumptions and scope
Number vertices by \(0,1,\ldots,11\), interpreting indices cyclically. Include the twelve edges \(\{i,i+1\}\), together with the six distinct edges \(\{i,i+5\}\) for even \(i\), or equivalently \(\{i,i-5\}\) for odd \(i\), with repeated unordered edges identified. This is the LCF presentation `[5,-5]^6`. The 18 graph edges are ordered lexicographically; all oriented simplicial signs refer to this order. A matching containing \(k\) graph edges has simplicial dimension \(k-1\). The graph is distinct from the six-vertex octahedral graph, even though both have a 48-element automorphism group abstractly isomorphic to \(S_4\times C_2\).

The distinguished Hamiltonian cycle is the vertex sequence
`(0,1,2,3,10,11,6,7,8,9,4,5)` (closed to its initial vertex). Its four-element orbit consists of four **edge sets** of Hamiltonian cycles, not the four vertices of a chosen drawing. The induced action on that orbit is the \(S_4\) action in the theorem.

## Proof
**Independent determination of the homology premise.** Exhaustively list all subsets of the eighteen edges that form matchings. Their numbers in sizes one through six are exactly \((18,117,336,417,186,17)\), totaling 1,091 nonempty simplices. Process the edges in lexicographic order. For each edge label, pair each still-unpaired nonempty matching that omits this label with its still-unpaired coface obtained by inserting it, when that coface is a matching. There are exactly 539 pairs, leaving one critical vertex and twelve critical three-simplices. To verify the matching is acyclic, direct every nonmatched proper codimension-one incidence downward and each matched incidence upward. The associated directed Hasse graph has exactly 3,942 incidences; an exhaustive topological sort processes all 1,091 faces. Hence Forman's discrete Morse theorem gives a CW model with one zero-cell, twelve three-cells and no other cells. It follows over the integers that \(X\simeq\bigvee^{12}S^3\). The concrete exhaustive certificate is reproducible by the embedded standard-library programs; this is **not** an inference from sampled cases or field ranks.

**Group identification.** An exhaustive adjacency-preserving bijection search lists all 48 graph automorphisms. Their action on the orbit of the Hamiltonian cycle specified above produces **all 24** permutations of four elements. The kernel is precisely the identity and the half-turn \(z(i)=i+6\). This half-turn permutes the eighteen graph edges as nine transpositions, so \(\eta(z)=-1\). Therefore every coset of \(\langle z\rangle\) has a unique representative in \(\ker\eta\); the latter group maps isomorphically to \(S_4\), establishing \(G=\ker\eta\times\langle z\rangle\).

**The character from fixed matchings.** For \(g\in G\), let \(C_d\) be the oriented rational simplicial chain group. The reduced equivariant Euler–Poincaré identity and the preceding Morse determination give
\[
\chi_3(g)=1-\sum_{d=0}^{5}(-1)^d\operatorname{tr}(g\mid C_d).
\]
Each chain trace is an exact signed count of invariant matchings, with the sign of the induced permutation of the graph edges within the matching. Alternatively, decompose the action of \(g\) on the eighteen graph edges into disjoint permutation cycles. Discard cycles whose edges are not pairwise vertex-disjoint. A \(g\)-invariant graph matching is exactly a union of admissible remaining edge cycles with pairwise disjoint endpoint sets. For an invariant matching using \(r\) edge cycles of lengths \(\ell_1,\ldots,\ell_r\), its chain-orientation sign is \((-1)^{\sum(\ell_i-1)}\). Its alternating chain contribution is therefore \((-1)^{r-1}\). Including the empty selection yields the independent identity
\[
\chi_3(g)=\sum_{\substack{\mathcal A\text{ a compatible set}\\\text{of admissible edge cycles}}}(-1)^{|\mathcal A|}.
\]
The embedded verifier independently computes the two expressions for **every** automorphism and checks equality.

Let \(\mu(g)\) denote the cycle type of its permutation of the four Hamiltonian cycles. Direct exhaustive enumeration gives the following **entire ten-class character table**. Every row identifies one conjugacy class.

| \(\mu(g)\) | \(\eta(g)\) | Class size | \(\chi_3(g)\) |
| --- | ---: | ---: | ---: |
| \((1,1,1,1)\) | \(+1\) | 1 | 12 |
| \((1,1,1,1)\) | \(-1\) | 1 | 4 |
| \((2,1,1)\) | \(+1\) | 6 | 2 |
| \((2,1,1)\) | \(-1\) | 6 | -2 |
| \((2,2)\) | \(+1\) | 3 | 0 |
| \((2,2)\) | \(-1\) | 3 | 0 |
| \((3,1)\) | \(+1\) | 8 | 0 |
| \((3,1)\) | \(-1\) | 8 | -2 |
| \((4)\) | \(+1\) | 6 | 0 |
| \((4)\) | \(-1\) | 6 | 0 |

The identity gives dimension twelve. The half-turn has trace four, giving the stated \(8+4\) eigenspace dimensions. Taking exact scalar products of the listed values with the ten characters \(\chi^{\lambda}(\mu)\eta^j\), where \(\lambda\vdash4\) and \(j=0,1\), gives multiplicity one only for \((\lambda,j)=((4),1),((3,1),0),((3,1),1),((2,2),0),((2,1,1),0)\), with zero in the other five cases. Their dimensions add to twelve. This proves the representation statement.

**Quotients.** Character averaging over 48 elements gives zero invariants for \(G\), and averaging over the 24 elements with \(\eta=+1\) gives one invariant. A finite simplicial group action can be made simplicially admissible by barycentric subdivision; over \(\mathbb Q\), taking invariants is exact, so rational homology of the ordinary geometric quotient equals invariant rational homology of the original complex. This proves both quotient statements.

## Verification
With standard Python 3, in the directory containing the accompanying files run `python3 verify_franklin_character.py` and `python3 verify_chain_independent.py`. The first regenerates all graph edges, all 48 automorphisms, all 1,091 nonempty faces, the 539-pair discrete-Morse matching and complete directed Hasse incidence graph. It tests acyclicity by topological sorting and constructs the four-Hamiltonian-cycle quotient action, confirming its image and kernel. It computes chain traces and, by a separate fixed-edge-orbit method, the same character at every one of the 48 automorphisms; it explicitly checks the proposed irreducible decomposition and ten conjugacy classes. It writes `franklin_character_certificate.json` from newly computed data and prints `FRANKLIN_CHARACTER_VERIFIED` upon success.

The second uses a separate face enumeration and binary boundary elimination. It gives boundary ranks \((1,17,100,236,169,17)\) over \(\mathbb F_2\), with reduced Betti sequence \((0,0,0,12,0,0)\), and prints `FRANKLIN_INDEPENDENT_CHAIN_VERIFIED`. The binary calculation is a corroboration; the integral Morse construction, not finite-field ranks alone, proves the characteristic-zero homology premise. The certificate records class representatives, signed chain traces, the four Hamiltonian cycles and all multiplicities.

## Relationship to prior work
Engström's 2005 study of independence complexes of claw-free graphs supplies an early, directly relevant topological framework; matching complexes are independence complexes of line graphs. It proves connectivity tools, not the present 48-element character. The separately published *Edge-orbit matching-complex splitting for the Franklin graph* already proves the **same** ordinary homotopy type \(\bigvee^{12}S^3\) and classifies its two edge-deletion orbits. That prior result is expressly acknowledged and supplies no character table, no rational irreducible decomposition, and no ordinary quotient rational homology calculation. The published *Full octahedral symmetry representation of the matching complex* uses a group abstractly isomorphic to \(G\), but its graph and matching complex are different (six graph vertices and first homology of dimension eleven); neither its module nor its computation implies this result. Prior studies of Knödel/crossed-prism graphs address graph parameters rather than this topological representation. A general signed-fixed-simplex Lefschetz method alone supplies a computational identity, not the graph-specific character values; the latter are the contribution here.

## Limitations
The decomposition is over \(\mathbb Q\), without asserting an integral direct-sum splitting. Quotient claims identify rational homology, not homeomorphism or homotopy type. The theorem concerns only the Franklin graph, not every crossed prism. The finite checks are complete for this graph and are reproducible, but they do not constitute an independent external audit. Publication-priority verification cannot rule out unindexed equivalent calculations.

## References
1. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420v1, first public December 17, 2005; full original HTML text consulted: https://arxiv.org/html/math/0512420v1.
2. *Edge-orbit matching-complex splitting for the Franklin graph*, public mathematical record dated October 11, 2026, identifier `be4888fadcca`; full mathematical result inspected in the published-finding corpus public repository.
3. *The full octahedral symmetry representation of the matching complex*, public mathematical record dated October 11, 2026, identifier `c700eceb52bb`; full mathematical result inspected in the published-finding corpus public repository.
4. G. Fertin and A. Raspaud, *A survey on Knödel graphs*, Discrete Applied Mathematics 137 (2004), 173–195, DOI:10.1016/S0166-218X(03)00260-9; graph-family background, abstract and introduction consulted.
5. R. Forman, *A user's guide to discrete Morse theory*, Sém. Lothar. Combin. 48 (2002), Article B48c; standard acyclic-matching theorem.
