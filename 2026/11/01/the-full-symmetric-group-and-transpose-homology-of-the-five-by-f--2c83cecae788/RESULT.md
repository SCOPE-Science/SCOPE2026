# The full symmetric-group and transpose homology of the five-by-five diagonal-deleted chessboard

## Finding
Let \(B\) be the bipartite graph with left and right vertex sets both indexed by \(\{1,2,3,4,5\}\), and with an edge \((i,j)\) exactly when \(i\neq j\). Let \(X=\mathcal M(B)\) be its matching complex: a \(k\)-simplex is a placement of \(k+1\) pairwise nonattacking rooks on the twenty off-diagonal squares. All reduced homology here is simplicial homology.

The complete reduced integral homology is
\[
\widetilde H_d(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&d=2,\\
\mathbb Z^{13},&d=3,\\
0,&\text{otherwise}.
\end{cases}
\]
The group \(G=S_5\times C_2\) acts by simultaneously permuting both row and column labels and by transposition \(\tau:(i,j)\mapsto(j,i)\). With \(\varepsilon\) the nontrivial one-dimensional \(C_2\)-module, the complete rational representations are
\[
\widetilde H_2(X;\mathbb Q)\cong\mathbf1\boxtimes\varepsilon,
\qquad
\widetilde H_3(X;\mathbb Q)\cong
(S^{(4,1)}\boxtimes\mathbf1)\oplus
(S^{(2,1,1,1)}\boxtimes\varepsilon)\oplus
(S^{(3,2)}\boxtimes\mathbf1).
\]
Here \(S^\lambda\) denotes the irreducible characteristic-zero Specht representation indexed by the partition \(\lambda\) of five. Thus every simultaneous relabeling fixes the integral degree-two generator, transposition reverses it, and no nonzero rational degree-three class is invariant under all simultaneous relabelings.

For a permutation \(\sigma\in S_5\) let \(f\) denote the number of fixed labels, \(t\) its number of two-cycles, \(s=\operatorname{sgn}(\sigma)\), and \(e\in\{0,1\}\). The character is equivalently
\[
\operatorname{tr}(\sigma\tau^e\mid\widetilde H_2)=(-1)^e,\qquad
\operatorname{tr}(\sigma\tau^e\mid\widetilde H_3)
=(f-1)(1+(-1)^e s)+\binom f2+t-f.
\]

## Assumptions and scope
The board has **exactly** five rows and five columns, with precisely its five diagonal squares omitted. The group action is the full graph automorphism group: connectivity of the underlying bipartite graph forces any automorphism to preserve the two vertex classes or exchange them; preservation of the five absent diagonal edges then forces simultaneous, identical permutations in both classes. These two types exhaust \(G\). The representations are over \(\mathbb Q\); the underlying homology groups and the degree-two sign action are over \(\mathbb Z\). No statement is made about homotopy type or other board sizes.

## Proof
**Integral chain calculation.** Order the twenty allowed square vertices lexicographically; orient every nonempty face by this order, with the empty simplex in degree \(-1\). The exhaustive face counts by cardinality \(0,1,2,3,4,5\) are \((1,20,130,320,265,44)\). The augmented integral boundary matrices have entries \(0,\pm1\), and their compositions are identically zero, checked for every column.

The accompanying program performs exact, deterministic chain contraction. If the coefficient of a cell \(r\) in the boundary of a cell \(c\) is \(u\in\{1,-1\}\), choose the \((r,c)\) pair and eliminate it by unimodular row and column operations, replacing every other coefficient \(a_{r',c'}\) with \(a_{r',c'}-a_{r',c}\,u^{-1}a_{r,c'}\). Eliminate the corresponding row and column and the incident terms in adjacent differentials. This is the standard elementary cancellation of an integral contractible two-term summand, hence preserves the complete integral chain-homotopy type; it is not merely a field-rank computation. At each step the program chooses a unit entry by the stated deterministic sparsity and degree ordering. It makes \(1,19,111,208,44\) unit cancellations in boundary degrees \(0,1,2,3,4\), respectively, totalling \(383\). The remaining augmented chain complex consists of exactly one generator in degree two and thirteen in degree three, with **every residual differential entry zero** and no other generators. This gives exactly the asserted torsion-free reduced integral homology and proves there are no unlisted reduced homology groups.

**Integral action in degree two.** Independently form the original simplicial boundary matrices over \(\mathbb F_{101}\), compute \(\ker\partial_2/\operatorname{im}\partial_3\), and select a nonzero class. The original matrices have ranks \(\operatorname{rank}\partial_2=111\) and \(\operatorname{rank}\partial_3=208\), so this quotient is one-dimensional. For every one of the \(120\) simultaneous relabelings and their \(120\) transposed counterparts, transport the oriented cycle with the exact sign of the induced vertex ordering and reduce its difference from \((-1)^e\) times the original cycle against \(\operatorname{im}\partial_3\). Every difference vanishes. Since the degree-two **integral** homology is infinite cyclic, each automorphism can act on it only by \(+1\) or \(-1\), which are distinguished modulo \(101\). The action is therefore integrally \((-1)^e\).

**Degree-three characters and decomposition.** For each of the \(240\) group elements enumerate every simplex fixed setwise and weight its contribution by the sign of the induced ordering, obtaining the exact *reduced* simplicial Lefschetz number \(L=\sum_{d=-1}^{4}(-1)^d\operatorname{tr}(g\mid\widetilde C_d)\). The chain-level Hopf trace identity and the preceding integral homology calculation give \(L=\operatorname{tr}(g\mid\widetilde H_2)-\operatorname{tr}(g\mid\widetilde H_3)\). The values agree for all \(240\) elements with the stated closed character formula.

Finally the standard four-dimensional representation \(S^{(4,1)}\) has character \(f-1\), its sign twist \(S^{(2,1,1,1)}\) has character \(s(f-1)\), and the five-dimensional \(S^{(3,2)}\) has character \(\binom f2+t-f\): indeed the permutation module on unordered pairs decomposes as \(\mathbf1\oplus S^{(4,1)}\oplus S^{(3,2)}\). These three constituent characters, with the indicated transpose parities, sum to the verified trace. Equality of rational characters for the finite group \(G\) implies the asserted direct-sum isomorphism by characteristic-zero semisimplicity.

## Verification
Run `python3 verify_derangement5.py` with Python 3 and no third-party libraries. The executable enumerates all faces and checks all boundary compositions; executes every signed, exact-integer unit contraction; confirms all residual differentials vanish; tests the degree-two generator against all \(240\) automorphisms modulo \(101\); and independently checks all \(240\) alternating cellular traces against the formula. The bundled `verification_output.txt` records the complete conjugacy-class trace table and ends in `VERIFY_OK`. In this finite, explicitly specified complex, the enumeration is exhaustive. The integral proof depends on exact unit eliminations; modulo-\(101\) calculations are used only to distinguish the two possible automorphisms of a proven integral infinite cyclic group.

## Relationship to prior work
Shareshian and Wachs, *Torsion in the Matching Complex and Chessboard Complex*, §8 (arXiv:math/0409054, first public September 3, 2004), study this same diagonal-deleted board \(D_n\). Their Table 8.1 already records the degree-two integral group for \(n=5\); thus that value alone is **not** claimed to be new. Their §8 develops the connectivity/sharpness problem and does not state the complete degree-three homology or this full \(S_5\times C_2\) character. Friedman and Hanlon, *On the Betti Numbers of Chessboard Complexes* (1997), determine representation-theoretic data for **full rectangular** chessboards under independent row/column permutations, not the representation of the diagonal-deleted subcomplex. Passing to the diagonal-deleted subcomplex changes both the chain complex and its symmetry group; the full-board theorem does not supply the stated result without further connecting-map analysis.

## Limitations
The classification concerns a single canonical finite board, not a general formula for \(D_n\), and no homotopy wedge decomposition is inferred from these homology groups. Scientific originality is subject to unindexed or incompletely accessible literature on nonrectangular boards and to potential unstated consequences of prior exact-object computations. An independent mathematical audit has not been performed.

## References
1. John Shareshian and Michelle L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054 (first posted September 3, 2004), §8 and Table 8.1. https://arxiv.org/abs/math/0409054 . Full text: https://www.math.miami.edu/~wachs/papers/torsion.pdf .
2. Joel Friedman and Phil Hanlon, *On the Betti Numbers of Chessboard Complexes*, manuscript May 14, 1997. https://www.cs.ubc.ca/~jf/pubs/web_stuff/newchess.pdf .
3. Anders Björner and Volkmar Welker, *Complexes of Directed Graphs*, SIAM J. Discrete Math., DOI:10.1137/S0895480198338724 (relevant earlier nonrectangular-board connectivity result, cited by [1]).
