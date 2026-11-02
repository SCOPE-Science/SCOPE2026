# Five simultaneous queen changes are necessary and sufficient for eight-queen solution mobility

## Finding

Let \(\mathcal Q_8\) be the family of placements of eight pairwise nonattacking queens on the standard \(8\times8\) board. For placements \(P,Q\), put \(\delta(P,Q)=8-|P\cap Q|\), the number of queens whose occupied squares change. For an integer \(k\), let \(G_k\) have vertex set \(\mathcal Q_8\), with two *distinct* placements adjacent when \(\delta(P,Q)\le k\). The simultaneous replacement need only preserve nonattack at its endpoints; intermediate partially rearranged boards are not required to be valid.

**The sharp connectivity threshold is \(k=5\).** Specifically, \(G_4\) has five connected components, of orders \(84,2,2,2,2\), while \(G_5\) is connected, with radius \(3\) and diameter \(4\). Its unordered-pair shortest-path enumerator is
\[
464t+2002t^2+1704t^3+16t^4.
\]
There are \(68\) configurations of eccentricity \(3\) and \(24\) of eccentricity \(4\).

Moreover, the eight configurations outside the order-\(84\) component of \(G_4\) constitute one orbit under the eight symmetries of the square board. If instead an exchange is required to change **exactly five** queens, the resulting graph is still connected; it has \(296\) edges, radius \(4\), and diameter \(5\). Its unordered-pair distance enumerator is
\[
296t+1178t^2+1968t^3+720t^4+24t^5.
\]
These are exact finite statements, not claims for arbitrary board sizes.

## Assumptions and scope

Rows and columns are indexed by \(\{0,1,\ldots,7\}\). Every solution is represented by a permutation \(p=(p_0,\ldots,p_7)\), with a queen at \((i,p_i)\) in row \(i\). This is a valid placement exactly when the eight integers \(i+p_i\) are pairwise distinct and the eight integers \(i-p_i\) are pairwise distinct. The positions of the queens are unlabelled; changing queens means changing occupied squares. For two valid permutations, \(\delta\) equals their Hamming distance. Thus \(\delta=1\) is impossible for distinct states, and the exchange threshold is unambiguous.

The graph \(G_k\) uses unrestricted simultaneous exchanges of at most \(k\) occupied squares. It is **not** the graph of chess-legal individual queen moves, nor a Markov chain that permits attacking intermediate arrangements. Every vertex along a reconfiguration path is a fully valid eight-queen placement.

## Proof

There are exactly \(8!=40320\) candidate permutations. The code `verify_permutations.py` checks the two diagonal-distinctness conditions for each candidate and retains the \(92\) solutions, in lexicographic order. For each unordered pair of the \(92\) resulting configurations it counts unequal permutation positions; all \(\binom{92}{2}=4186\) pairs are exhausted. Their Hamming-distance frequencies for distances \(2,3,4,5,6,7,8\) respectively are
\[
8,\quad32,\quad128,\quad296,\quad824,\quad1272,\quad1626.
\]

For each threshold \(k\), a pair belongs to \(E(G_k)\) exactly when its computed distance is at most \(k\). This rule is exhaustive: no other final placements exist, and there is no extra legality condition between simultaneous endpoints. For \(k=4\), the program constructs all \(168\) edges and performs a complete component traversal. It returns component orders \(84,2,2,2,2\). For concreteness, the four small components (each a single edge) are the following pairs of row-column permutations:

```
(1,5,0,6,3,7,2,4) -- (3,5,0,4,1,7,2,6)
(2,0,6,4,7,1,3,5) -- (2,4,6,0,3,1,7,5)
(4,2,7,3,6,0,5,1) -- (6,2,7,1,4,0,5,3)
(5,3,1,7,4,6,0,2) -- (5,7,1,3,0,6,4,2)
```

For \(k=5\), all \(464\) edges are constructed by the same complete predicate. A breadth-first search from **every one** of the \(92\) states reaches the other \(91\). The \(4186\) distinct pairs have shortest-path multiplicities \(464,2002,1704,16\) at distances \(1,2,3,4\); the two eccentricities occur \(68\) and \(24\) times. Hence \(G_5\) is connected, its radius is \(3\), and its diameter is \(4\). Together with disconnectedness of \(G_4\), this proves that five changes are necessary and sufficient. The four small components contain eight placements, and direct application of the four rotations and four reflections shows these eight form one orbit.

Finally, filtering the exhaustive pair list to distance **exactly** five yields \(296\) edges. Another complete all-source shortest-path calculation verifies connectedness, radius \(4\), diameter \(5\), and the second stated pair-distance enumerator. The standalone integer certificate `certificate.json` records the complete solution list, all neighbors at thresholds four and five, all threshold-five shortest-path distances, the five threshold-four components, and both distance profiles. The checker recomputes these data from the definitions, rather than taking a logged result as a proof.

## Verification

Run with Python 3 using only the standard library:

```
python3 verify_permutations.py certificate.json
python3 verify_bitboards.py certificate.json
```

The first program enumerates all permutations and reconstructs all stated graphs, distances, and symmetry orbits, then writes an independently reproducible certificate. The second program **independently** enumerates placements with bitboard diagonal masks rather than by testing permutations, defines replacements by half the population count of the symmetric difference of occupied-square masks, and verifies the component, edge, and distance statistics. It also compares the shipped certificate's adjacency tables against a bitboard construction. Both procedures completed with `PERMUTATION_EXHAUSTIVE_PASS` and `BITBOARD_INDEPENDENT_PASS`, respectively.

## Relationship to prior work

The well-known total of \(92\) solutions and \(12\) classes modulo square-board symmetries predates this analysis. Zhang and Ma, *Counting Solutions for the N-queens and Latin Square Problems by Efficient Monte Carlo Simulations* (arXiv:0808.4003, public August 28, 2008), use transposition swaps on the space of **all rook-compatible permutations**, permitting diagonal-conflicting states at positive energy. Their swap chain does not assert a fully feasible eight-queen reconfiguration threshold or distances. Chaiken, Hanusa, and Zaslavsky, *A \(q\)-Queens Problem. I. General Theory* (arXiv:1303.1879, public March 8, 2013), and *II. The Square Board* (arXiv:1402.4880, public February 20, 2014), develop enumerative inside-out-polytope methods and an enumeration framework; their results concern counts and related generating functions, not shortest paths among fixed-board feasible solutions. Bell and Stevens, *A Survey of Known Results and Research Areas for n-Queens* (Discrete Mathematics 309 (2009), 1–31), provides historical and structural context. These established ideas are not claimed as new.

The present claim is the sharp *feasibility-preserving simultaneous-replacement* threshold and full exact small-board metric classification, not the count of solutions or ordinary permutation-swap mixing. Comparable statements were sought under exchange, swap, transposition, local-search and reconfiguration terminology; an exhaustive assertion about unindexed literature is not made.

## Limitations

This is a finite exhaustive proof for the classical \(8\times8\) board only. It neither proves nor conjectures a uniform threshold for all \(n\)-queen instances. The moves here are simultaneous relocation of up to five unlabelled queens; they may not be decomposable into five successively valid single-queen moves. Reproducibility depends on executing the supplied finite integer computations, not an external infinite theorem. Possible unindexed equivalent accounts of chess-placement transformation graphs remain an originality risk; independent scholarly audit has not been performed.

## References

1. C. Zhang and J. Ma, *Counting Solutions for the N-queens and Latin Square Problems by Efficient Monte Carlo Simulations*, arXiv:0808.4003 (first public August 28, 2008), subsequently Phys. Rev. E 79 (2009), 016703. https://arxiv.org/abs/0808.4003
2. J. Bell and B. Stevens, *A Survey of Known Results and Research Areas for n-Queens*, Discrete Mathematics 309 (2009), 1–31. https://doi.org/10.1016/j.disc.2007.12.043
3. S. Chaiken, C. R. H. Hanusa, and T. Zaslavsky, *A q-Queens Problem. I. General Theory*, arXiv:1303.1879 (first public March 8, 2013). https://arxiv.org/abs/1303.1879
4. S. Chaiken, C. R. H. Hanusa, and T. Zaslavsky, *A q-Queens Problem. II. The Square Board*, arXiv:1402.4880 (first public February 20, 2014). https://arxiv.org/abs/1402.4880
