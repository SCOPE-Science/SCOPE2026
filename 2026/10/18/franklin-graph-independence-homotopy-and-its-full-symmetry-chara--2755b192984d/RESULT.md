# Franklin-graph independence homotopy and its full symmetry character

## Finding
Let \(F\) be the twelve-vertex Franklin graph, with the explicit labeling below, and let \(K=\operatorname{Ind}(F)\) be its ordinary independence complex. Then
\[
K\simeq\bigvee^{4}S^{2}.
\]
The full graph-automorphism group \(G=\operatorname{Aut}(F)\) has order \(48\). Its action on the unique nonzero reduced rational homology group decomposes as
\[
\widetilde H_2(K;\mathbb Q)\cong \mathbf1_G\oplus W,
\]
where \(W\) is an absolutely irreducible rational \(G\)-representation of dimension three. The central involution \(z(i)=i+6\pmod {12}\) acts trivially on \(\mathbf1_G\) and by minus the identity on \(W\). Consequently, the full symmetry-fixed homology is one-dimensional, even though \(\widetilde H_2(K;\mathbb Z)\cong\mathbb Z^4\).

## Assumptions and scope
Label vertices \(0,1,\ldots,11\) modulo twelve. Include each cycle edge \(\{i,i+1\}\), and include \(\{i,i+5\}\) for even \(i\) and \(\{i,i-5\}\) for odd \(i\), removing repetitions. This is the LCF presentation `[5,-5]^6` of the Franklin graph (also called the six-crossed prism). The resulting simple graph has twelve vertices, eighteen edges, and degree three at every vertex. A simplex of \(K\) is a set of graph vertices containing no graph edge. The automorphism action permutes graph vertices and hence acts simplicially on \(K\). Rational coefficients are used only for the representation decomposition; the homotopy assertion is integral.

## Proof
**1. Exact face domain.** Encode a subset of graph vertices by the integer \(m\) whose set bits are precisely its vertices. Test each of the \(2^{12}\) subsets against the eighteen explicit graph edges. The numbers of nonempty simplices in dimensions \(0,1,2,3,4,5\) are respectively \(12,48,76,45,12,2\). There are therefore \(195\) nonempty faces.

**2. A complete acyclic matching.** On the remaining nonempty face poset, call a face free when it has exactly one remaining immediate coface. If any free face exists, choose one of largest dimension, breaking ties by smallest bitmask, and remove it together with its unique immediate coface as a matched pair. Otherwise remove a remaining maximal face of largest dimension, again breaking ties by smallest bitmask, and declare it critical. The removal process leaves a simplicial subcomplex after every step. Indeed, a face with exactly one immediate coface has no higher-dimensional coface, while a critical face is maximal. This construction is specified without discretionary choices.

The exhaustive calculation in `verify_franklin.py` produces \(95\) matched pairs and five critical cells: the single critical vertex has mask `2048`, and the four critical two-simplices have masks `328`, `577`, `578`, and `1168`. Independently, form the directed Hasse graph of all \(195\) nonempty faces, orienting each matched incidence from lower to higher dimension and all unmatched incidences from higher to lower dimension. Topological sorting visits every vertex, so there is no directed cycle. Thus the matching is acyclic in the sense of discrete Morse theory. The resulting Morse CW complex has one zero-cell and four two-cells, with no one-cells or other cells. Each two-cell has the constant attaching map into the sole zero-cell, yielding exactly \(\bigvee^4S^2\). In particular all integral reduced homology is torsion-free and concentrated in degree two.

**3. Complete symmetry character.** Enumerate all permutations of the twelve vertices that preserve adjacency and nonadjacency, by injective recursive backtracking. This enumerates exactly \(48\) automorphisms; the only central elements are the identity and \(z\) specified above. For any \(g\in G\), the simplicial action on the augmented chain complex has reduced Lefschetz number
\[
\chi(g)=-\sum_{\substack{S\in K\\gS=S}}(-1)^{|S|}\operatorname{sgn}(g|_S),
\]
where the empty simplex is included with sign \(+1\), and \(\operatorname{sgn}(g|_S)\) is the sign of the induced permutation of the fixed subset \(S\). Since the only nonzero reduced homology is in even degree two, this Lefschetz number is exactly the trace of \(g\) on \(\widetilde H_2(K;\mathbb Q)\).

The complete resulting character distribution, organized by group-element order and trace, is:

| Order | Trace | Number of automorphisms |
| ---: | ---: | ---: |
| 1 | 4 | 1 |
| 2 | -2 | 1 |
| 2 | 0 | 9 |
| 2 | 2 | 9 |
| 3 | 1 | 8 |
| 4 | 0 | 6 |
| 4 | 2 | 6 |
| 6 | 1 | 8 |

In particular \(\chi(1)=4\), \(\chi(z)=-2\), \(\sum_{g\in G}\chi(g)=48\), and \(\sum_{g\in G}\chi(g)^2=96\). The multiplicity of the trivial representation is therefore \(48/48=1\). Over characteristic zero its invariant line splits, giving a rational three-dimensional complementary representation with character \(\psi=\chi-1\). Since
\[
\langle\psi,\psi\rangle_G=\frac1{48}\sum_{g\in G}(\chi(g)-1)^2=1,
\]
\(W\) is absolutely irreducible. Finally, \(\psi(z)=-3\). Because \(z\) is central of order two, its action on this irreducible three-dimensional space is scalar, necessarily \(-1\). This proves the full representation statement.

## Verification
The included standard-library program `verify_franklin.py` enumerates all \(4096\) vertex subsets, constructs the complete matching and its directed Hasse graph, checks every incidence by topological sorting, enumerates all \(48\) automorphisms without a group-order oracle, and evaluates each signed fixed-face Lefschetz sum exactly. Separate cellular boundary calculations over both \(\mathbb F_2\) and \(\mathbb F_{1009}\) give ranks \((11,37,35,10,2)\) in degrees one through five, consistent with the integral Morse calculation. Running `python3 verify_franklin.py` prints `PASS` when all assertions succeed. The discrete-Morse proof, not agreement of finite-field ranks, establishes the full integral homotopy type.

## Relationship to prior work
Barmak's 2010 study *Star clusters in independence complexes of graphs*, particularly Theorem 3.4, proves that the independence complex of every triangle-free graph is homotopy equivalent to a suspension. This theorem applies to the Franklin graph, but does not determine the four-sphere multiplicity, the explicit perfect acyclic matching, or the automorphism character. The published *Edge-orbit matching-complex splitting for the Franklin graph* concerns matchings of **graph edges**, rather than independent sets of **graph vertices**. Its \(\bigvee^{12}S^3\) calculation neither implies nor is implied by the present theorem. The usual Franklin graph identifiers and LCF representation are recorded by MathWorld. Searches under the aliases *six-crossed prism* and *Knödel graph* did not reveal the same homotopy and representation statement; absence from indexed results is not proof of universal priority.

## Limitations
This is an exact theorem about one naturally distinguished finite graph, not a classification of all cubic or bipartite graphs. The wedge-of-spheres equivalence is nonequivariant; no equivariant CW wedge decomposition and no integral decomposition of the full automorphism lattice are asserted. The character decomposition is rational, although the homology groups themselves are integral and torsion-free. A previously unindexed or inaccessible publication could already contain equivalent calculations. The finite proof is reproducible from the included complete enumerator; it has not received independent external verification.

## References
1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418, first publicly posted 2010-07-02, especially Sections 1, 3, and 7.
2. *Franklin Graph*, Wolfram MathWorld, graph aliases, LCF notation, and graph identification.
3. *Edge-orbit matching-complex splitting for the Franklin graph*, published-finding corpus publication identifier `be4888fadcca`, 2026; direct RESULT text inspected for the distinct matching-complex domain.
