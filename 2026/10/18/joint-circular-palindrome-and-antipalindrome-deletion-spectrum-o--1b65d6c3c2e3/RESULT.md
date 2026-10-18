# Joint circular palindrome and antipalindrome deletion spectrum of binary order-five de Bruijn cycles

## Finding

For the \(2048\) binary order-five de Bruijn cycles \(B\), identified modulo cyclic rotation, denote by \(A(B)\) the maximum length of an antipalindromic scattered subsequence in any length-\(32\) linear cut of \(B\), and by \(P(B)\) the corresponding maximum palindromic scattered-subsequence length. Every such cycle has \(A(B)\in\{26,28,30,32\}\) and \(P(B)\in\{25,26,27,28,29\}\). The complete joint distribution is:

| \(A(B)\) | \(P(B)=25\) | \(P(B)=26\) | \(P(B)=27\) | \(P(B)=28\) | \(P(B)=29\) | Row total |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 26 | 4 | 16 | 284 | 52 | 32 | 388 |
| 28 | 52 | 80 | 860 | 180 | 136 | 1308 |
| 30 | 12 | 16 | 192 | 44 | 24 | 288 |
| 32 | 8 | 2 | 44 | 10 | 0 | 64 |
| Column total | 76 | 114 | 1380 | 286 | 192 | 2048 |

Exactly \(19\) of the \(20\) possible pairs occur. In particular, no cycle attains both the perfect antipalindromic value \(A(B)=32\) and the maximum palindromic value \(P(B)=29\). Every such cycle can be made antipalindromic by deleting at most six symbols after a suitable circular cut; exactly \(388\) cycles require six deletions, and \(64\) require none. Under reversal and bit complementation, the \(2048\) cycles form \(32\) orbits of size two (all with \(A(B)=32\)) and \(496\) orbits of size four.

## Assumptions and scope

A binary order-five de Bruijn cycle is a rotation class of a binary circular word of length \(32\) in which each of the \(32\) binary words of length five occurs exactly once as a contiguous circular factor. No reversal or bit-complement quotient is imposed when counting cycles. A *linear cut* is one of the \(32\) rotations of the circular word, retaining exactly one circumference. A scattered subsequence is obtained by deleting zero or more symbols without changing the order of the retained symbols. An ordinary palindrome reads identically backward; an antipalindrome satisfies \(u_i=1-u_{m+1-i}\) at every position, so its length \(m\) is even. Empty subsequences are permitted in intermediate dynamic programs, but the resulting maxima here are strictly positive. The maxima in \(A(B)\) and \(P(B)\) may be realized by different cuts.

## Proof

**Exhaustive parametrization.** Form the binary de Bruijn digraph with the \(16\) four-bit words as vertices and the \(32\) five-bit words as directed edges. The edge represented by the five-bit integer \(e\), with \(0\le e<32\), runs from vertex \(\lfloor e/2\rfloor\) to vertex \(e\bmod16\). Every vertex has exactly two incoming and two outgoing edges. A directed Eulerian circuit induces one bijection of incoming to outgoing edges at each vertex, of which there are exactly two; conversely, any choice of these bijections induces a permutation of the \(32\) edges. It corresponds to an Eulerian circuit precisely when that permutation is one cycle. Thus enumerating all \(2^{16}=65536\) choices and retaining the one-cycle permutations exhausts every binary order-five de Bruijn cycle, with a unique root at the edge \(00000\). A cycle is recovered from its successive edge-label last bits and normalized to its lexicographically smallest rotation. This computation finds exactly \(2048\) different normalized cycles. A separate depth-first enumeration of edge-distinct Eulerian circuits, also rooted at \(00000\), yields exactly the same set. Every reported word is independently checked to contain each five-bit circular window once.

**Exact optimal subsequences.** For a linear cut \(w=w_0\cdots w_{31}\), consider a closed interval \([i,j]\). Let \(F(i,j)\) denote its longest palindrome or antipalindrome scattered-subsequence length. For an ordinary palindrome, set \(F(i,i)=1\); for an antipalindrome, set \(F(i,i)=0\). Empty intervals have score zero. For \(i<j\), the recurrence is

\[
F(i,j)=\begin{cases}\max\bigl(F(i+1,j),F(i,j-1),2+F(i+1,j-1)\bigr),&\text{if endpoints eligible},\\\max\bigl(F(i+1,j),F(i,j-1)\bigr),&\text{otherwise}.\end{cases}
\]

where the third candidate is *included only when* the endpoints are eligible, meaning \(w_i=w_j\) for a palindrome and \(w_i\ne w_j\) for an antipalindrome. The recurrence follows by partitioning an optimal subsequence into the cases where at least one endpoint is omitted, or both endpoints are retained. In the latter case the retained interior must have the same symmetry type. Induction on interval length proves that every recurrence value is exact. Maximizing the full-interval score over the \(32\) cuts gives precisely \(P(B)\) and \(A(B)\).

**Finite certificate.** Apply this recurrence to every cut of every cycle in the exhaustive graph enumeration. The computed per-cycle values are fully recorded in `cycles.csv`. Direct tally gives the displayed \(19\)-cell distribution. To guard against a shared search implementation error, the separately implemented Eulerian-depth-first generator is compared with the local-pairing generator, and each interval score is additionally compared with an independently programmed longest-common-subsequence calculation against the reversed word or its bitwise complement. All \(65536\) cuts agree. This comparison is a finite numerical cross-check: the mathematical proof of optimality is the interval recurrence itself, not an assumption that an arbitrary longest common subsequence has the required symmetry.

Finally, reversal and complementation preserve both invariants. Enumerating the induced groups of up to four rotation classes gives \(32\) two-element orbits and \(496\) four-element orbits. All two-element orbits have \(A(B)=32\), as confirmed by the complete orbit enumeration. The orbit totals \(2\cdot32+4\cdot496=2048\) are a separate consistency check.

## Verification

The accompanying `verify.cpp` and `cycles.csv` are standalone, source-level verification artifacts. With a C++17 compiler, run `g++ -O2 -std=c++17 verify.cpp -o verify` followed by `./verify cycles.csv`. The checker enumerates all \(65536\) local pairings, independently enumerates Eulerian circuits by depth-first search, verifies every five-bit circular factor, compares interval dynamic programs with independent longest-common-subsequence calculations for all \(65536\) rooted cuts, checks the nineteen joint frequencies and both marginals, and verifies the complete CSV and reversal/complement orbit counts. The recorded successful execution reported `VERIFY_OK` with \(2048\) cycles, \(19\) joint cells, and \(528\) symmetry orbits. All arithmetic in the enumeration is exact integer arithmetic.

## Relationship to prior work

Guo, Shallit and Shur develop the finite-word theory of antipalindromes and their conjugates; their results concern contiguous factors, antipalindrome factorizations, and related word properties, not the two longest scattered-subsequence statistics of de Bruijn cycles. Müllner and Ryzhikov formulate both the ordinary palindromic and antipalindromic circular-subsequence problems and their general conjectural lower bounds for balanced circles. Their all-word statements neither classify the order-five de Bruijn population nor give its joint deletion tradeoff. Chang and Wang study reverse-complement-symmetric (CR) de Bruijn sequences at odd orders. Their existence and divisibility results bear on the boundary event \(A(B)=32\), but do not determine the conditional palindromic distribution or the other \(15\) nonzero cells. The present finding is the exact *joint* distribution on a specific natural subclass; it does not resolve any all-length, all-order, or universal lower-bound conjecture.

## Limitations

This is an exact finite classification at de Bruijn order five, not an asymptotic theorem. The statements concern scattered subsequences across any single full-length cut, not contiguous palindromic factors or independently chosen wraparound subsequences with repeated circular positions. The two maximizers need not use the same cut. The individual ordinary-palindrome marginal and the reverse-complement boundary are not claimed as separately new discoveries. The theorem proves no formula for other de Bruijn orders. An unindexed earlier enumeration of the joint statistic remains a historical-priority risk; no claim of externally independent review is made.

## References

- C. Guo, J. Shallit, A. M. Shur, *On the Combinatorics of Palindromes and Antipalindromes*, arXiv:1503.09112, first posted 2015-03-31, https://arxiv.org/abs/1503.09112.
- C. Müllner, A. Ryzhikov, *Palindromic Subsequences in Finite Words*, arXiv:1901.07502, first posted 2019-01-22, https://arxiv.org/abs/1901.07502.
- Z. Chang, Q. Wang, *Efficient generation of odd order de Bruijn sequence with the same complement and reverse sequences*, arXiv:2408.01794, first posted 2024-08-03, https://arxiv.org/abs/2408.01794.
