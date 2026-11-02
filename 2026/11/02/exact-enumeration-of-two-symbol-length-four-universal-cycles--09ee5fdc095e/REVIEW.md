# Review of the exact two-symbol four-window cycle count

## Correctness — PASS

The claim is quantified for every integer \(q\ge2\), for a labeled alphabet, with rotation alone as the equivalence. The four-letter allowed language has exactly \(7q(q-1)\) distinct words. Its overlap graph has \(q\) degree-\(q-1\) vertices and \(3q(q-1)\) degree-two vertices. The proof explicitly lists all outgoing transitions and shows strong connectivity. Each unordered pair contributes one six-state internal Laplacian block of determinant \(28\) and exact Schur transfer \(\frac17\bigl(\begin{smallmatrix}3&4\\4&3\end{smallmatrix}\bigr)\). Thus the reduced constant-vertex Laplacian is \(\frac47(qI_q-J_q)\), and the directed matrix-tree theorem gives \(2^{(q-1)(q+2)}7^{\binom{q-1}{2}}q^{q-2}\) rooted in-arborescences. The BEST theorem, using a unique specified first four-word, yields the additional factor \(((q-2)!)^q\). Boundary \(q=2\) is legitimate; the counted cycles each have full length, so fixed-first-edge normalization counts rotation classes exactly once. The standalone checker recomputes exact integer cofactors for \(q=2\) through \(6\), the six-state transfer, sixteen binary tours and explicit longer witnesses.

## Originality — PASS, with stated residual risk

Gardner–Godbole (arXiv:1711.07029) and Leitner–Godbole (arXiv:0808.1309) treat existence for various larger or differently restricted languages, including onto and almost-onto words, without an exact enumeration of tours for the fixed range-size-two length-four language. Chen–Kitaev–Sun (arXiv:1908.01116) count which sets of removed words permit cycles; that existential probability is not the number of cycles of this specific restricted language. A related exact length-three two-symbol count has a different overlap graph; separate length-four counts for three- or four-symbol languages have disjoint allowed edges; and a count for tandem-square avoidance uses a strictly larger word language. None of these implications determines the present determinant. Actual searches included `universal cycles exact two distinct symbols length four words all q count rooted spanning trees`, `number of Euler circuits restricted de Bruijn graph two-symbol factors length 4 seven q q-1 matrix tree`, and `four letter words exactly two alphabet symbols cyclic universal cycle enumeration de Bruijn`. No direct or stronger enumerative coverage was located. Residual risk: an unindexed older count or a general Euler-tour theorem specialized to this exact graph may exist.

## Value — PASS

The question is a natural, support-constrained de Bruijn enumeration: two-symbol length-four words are precisely the first nonconstant support stratum on an arbitrary alphabet. Unlike a finite census or an existence-only deduction, the theorem gives a parameter-uniform exact count with a nontrivial six-state gadget and an explicit \(7^{\binom{q-1}{2}}\) factor. It also makes available minimal-length explicit universal cycles for every alphabet size. Its relevance is to enumerative combinatorics on words and constrained universal-cycle constructions, not to an asserted downstream theorem.

## Limits

No claim is made about inequivalent cycles under alphabet permutations or reversal, other support strata, or longer windows. Exact matrix-tree/BEST reductions establish the result for all alphabet sizes; the finite checker is corroboration. Novelty remains subject to external literature review. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
