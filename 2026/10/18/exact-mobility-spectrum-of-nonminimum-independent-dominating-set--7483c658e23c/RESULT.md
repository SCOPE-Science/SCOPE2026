# Exact mobility spectrum of nonminimum independent dominating sets on cycles

## Finding
For every pair of integers \(n\ge8\) and \(\lceil n/3\rceil<k\le\lfloor n/2\rfloor\), define \(X_{n,k}\) to be the token-sliding graph of all \(k\)-element **maximal independent vertex sets** of \(C_n\). Write \(t=n-2k\), so \(0\le t<k\). Then:

1. If \(t=0\), \(X_{n,k}\cong2K_1\): the two alternating maximum independent sets are frozen.
2. If \(1\le t<k\), the graph is **connected and Eulerian**, with exact order and edge count
   \[
   |V(X_{n,k})|=\frac nk\binom kt,\qquad |E(X_{n,k})|=n\binom{k-2}{t-1}.
   \]
3. In the connected case its complete degree distribution is
   \[
   |\{S:\deg_{X_{n,k}}S=2r\}|=
   \frac nr\binom{t-1}{r-1}\binom{k-t-1}{r-1}
   \quad (1\le r\le\min\{t,k-t\}),
   \]
   and all other degree counts vanish. In particular every movable configuration has positive even degree, and when \(t=1\) the graph is exactly \(C_n\).
4. If \(t>0\), the graph is bipartite precisely for even \(n\). For odd \(n\) it has **odd girth exactly \(n\)**; a constructive simple cycle of length \(n\) exists even when the graph also contains shorter even cycles.

These assertions simultaneously characterize connectivity, frozen configurations, exact mobility frequencies, parity and shortest odd return walks at every **nonminimum feasible cardinality**.

## Assumptions and scope
The cycle \(C_n\) has vertices \(\mathbb Z/n\mathbb Z\), with edges between consecutive residues. A set is *independent* if no two elements are adjacent, and *maximal independent* if no other vertex can be added; this is equivalent to being independent and dominating. An edge in \(X_{n,k}\) slides one selected vertex by one cycle edge and retains cardinality, independence **and domination at every step**. This is not the larger graph of all independent sets under unrestricted intermediate domination. The integer range ensures there is at least one feasible configuration; the known minimum independent-domination size \(\lceil n/3\rceil\) is excluded because its token-slide graph has already been characterized in prior literature. The maximum layer \(k=n/2\) is included only when \(n\) is even.

## Proof
**1. Cyclic words and legal moves.** Let \(S\) be any maximal independent \(k\)-set, and list its selected vertices clockwise as \(x_0,\ldots,x_{k-1}\). Every successive clockwise distance \(d_i=x_{i+1}-x_i\pmod n\) is at least \(2\) by independence and at most \(3\) by domination. Conversely every circular placement with clockwise distances in \(\{2,3\}\) is a maximal independent set. Since \(\sum_i d_i=n\), exactly \(t=n-2k\) gaps have size \(3\) and exactly \(k-t\) have size \(2\).

Sliding token \(x_i\) one step clockwise changes the immediately preceding and succeeding gaps from \((2,3)\) to \((3,2)\); these are exactly the necessary and sufficient conditions for this slide to remain legal. The counterclockwise slide reverses this swap. Thus the degree of the configuration is exactly the number of transitions between \(2\) and \(3\) in its cyclic gap word. When both symbols occur, this number is twice their common number \(r\) of cyclic runs. When all gaps are \(2\), no slide exists and there are exactly two alternating configurations.

**2. Counting configurations and mobility classes.** Choose an anchor vertex \(x_0\) among \(n\) cycle positions and then choose the \(t\) positions occupied by gap \(3\) among the \(k\) ordered gaps. Each unmarked configuration is counted once for every choice of its \(k\) anchor tokens, giving \(\frac nk\binom kt\) configurations. For fixed \(r\), a cyclic binary word with exactly \(r\) runs of each symbol is counted by choosing the start of a distinguished \(3\)-run (\(k\) choices), a composition of \(t\) into \(r\) positive run lengths, and a composition of \(k-t\) into \(r\) positive run lengths; dividing by \(r\) choices of distinguished \(3\)-run gives \(\frac kr\binom{t-1}{r-1}\binom{k-t-1}{r-1}\) words anchored at a gap. Multiplying by \(n/k\) gives the stated degree-count formula. The handshaking identity and Vandermonde convolution yield
\[
|E|=\sum_{r\ge1}rN_{2r}
=n\sum_{r\ge1}\binom{t-1}{r-1}\binom{k-t-1}{r-1}
=n\binom{k-2}{t-1}.
\]

**3. Constructive connectivity.** Assume \(0<t<k\). Mark one distinguished token and keep it stationary. Sliding the other \(k-1\) tokens implements precisely the adjacent transpositions of the \(k\) **linear** gaps (swap gap indices \(i\) and \(i+1\) by moving the token between them, for \(0\le i<k-1\)). Since arbitrary binary words with the same number of \(3\)'s are connected by adjacent swaps, while the anchor token stays fixed we can transform its cyclic gap word into any ordered word with \(t\) threes.

In particular reorder the gaps so that the gap immediately *before* the marked token is \(2\) and the gap immediately *after* it is \(3\). Sliding the marked token clockwise is then legal. Repeating reordering and sliding lets the marked token visit any prescribed vertex of \(\mathbb Z/n\mathbb Z\), while preserving the mark. For any two configurations choose an anchor token in each: position the first marked token at the desired second anchor, then reorder the gaps to the second configuration. Thus the graph is connected. Its vertex degrees are positive and even by step 1, so it has an Eulerian circuit. For \(t=1\), the count formulas show it is a connected \(2\)-regular graph on \(n\) vertices, hence \(C_n\).

**4. Exact odd girth.** Define the position-sum invariant \(\Phi(S)=\sum_{x\in S}x\pmod n\). Any slide changes \(\Phi\) by \(\pm1\pmod n\). When \(n\) is even, reduction modulo \(2\) yields a proper bipartition. When \(n\) is odd, any closed odd walk of length less than \(n\) would make an odd, nonzero integer sum of \(\pm1\)'s of absolute value less than \(n\), yet congruent to zero modulo \(n\); impossible. Hence any odd cycle has length at least \(n\).

For an explicit matching upper bound, since \(0<t<k\), we have \(2<n/k<3\). For integers \(s=0,\ldots,n\), place \(k\) labelled tokens at lifted locations
\[
a_i(s)=\left\lfloor\frac{in+s}{k}\right\rfloor\pmod n
\qquad(0\le i<k).
\]
Each gap, including the wrapping one, is \(2\) or \(3\), hence every resulting set is valid. As \(s\) increases by one, precisely those tokens satisfying \((in+s)\bmod k=k-1\) advance one place; all others stay. If \(d=\gcd(n,k)\), the moving indices are spaced by \(k/d\) in the circular list. Since \(t>0\), we have \(k/d\ge2\), so no two moving tokens are consecutive. Each moving token has a preceding gap \(2\) and a following gap \(3\), as seen directly from the floor differences (the preceding remainder is \(k-1-t\)). Therefore these noninteracting moves may be performed singly in any order, with every intermediate set still maximal independent.

The final lifted sequence is shifted in index by one: \(a_i(n)=a_{i+1}(0)\), where \(a_k(0)=n\), so the *unlabelled* terminal state equals the initial state. The total number of unit moves is \(\sum_i(a_i(n)-a_i(0))=n\). No nonempty subwalk of this exclusively clockwise closed walk of length strictly below \(n\) can return to its own starting configuration: the invariant \(\Phi\) increases by its positive length, which is not a multiple of \(n\). Hence the closed walk is a simple cycle of length \(n\). For odd \(n\), the lower and upper bounds match, proving odd girth exactly \(n\) and showing non-bipartiteness.

## Verification
Two complementary standalone Python programs accompany this result. `brute_cycle.py` starts from all vertex subsets, tests independence and domination directly, constructs every legal move, computes graph components and degree frequencies, and checks the claims over all feasible nonminimum pairs through \(n=20\). `gap_cycle.py` independently generates configurations from cyclic gap words, reconstructs the slide graph, verifies the enumerators and explicit floor-schedule cycles through \(n=29\) for tractable configuration counts. Their recorded outputs are included as `brute_cycle.out` and `gap_cycle.out`. Both programs terminate with explicit `REPLAY_OK` flags. These finite checks support, but do not replace, the all-order proof above.

## Relationship to prior work
Bonsma, Kamiński and Wrochna (2014), arXiv:1403.0359v1, establish reachability of **unrestricted independent** sets under token slides on claw-free graphs (including cycles). Their general reachability result permits an intermediate independent set that ceases to dominate, so it cannot establish connectivity of the induced maximal-independent reconfiguration graph; it also does not give its degree spectrum or odd girth. Brewster, Mynhardt and Teshima (2023), arXiv:2303.08190v1, determine the graph of **minimum** independent dominating sets on cycles, the expressly excluded \(k=\lceil n/3\rceil\) layer. Their gap-word approach is an important methodological antecedent. Avis and Hoang (2022), arXiv:2203.16861v1, study the full token-sliding graph of independent sets, without the maximality requirement, including cycle examples and its Eulerian behavior; ambient-graph results alone do not determine these induced layer graphs. Exhaustive title, equivalence, key-parameter and statement comparisons identified no source with the all-nonminimum connectivity, full exact degree spectrum and odd-girth conclusions jointly; the possibility of equivalent earlier unindexed treatments remains.

## Limitations
The theorem covers simple cycles and nonminimum cardinality layers only; it does not classify paths, general claw-free graphs, or the separately published minimum independent-domination reconfiguration graphs. It does not calculate the ordinary girth, graph diameter or automorphism group of the active layers. Global bibliographic novelty is not mathematically provable from a finite search; older work outside indexed sources may be relevant. Source review and computational checks are not independent external scientific certification.

## References
- P. Bonsma, M. Kamiński, M. Wrochna, *Reconfiguring Independent Sets in Claw-Free Graphs*, arXiv:1403.0359v1 (2014-03-03), https://arxiv.org/abs/1403.0359.
- R. C. Brewster, C. M. Mynhardt, L. E. Teshima, *The i-Graphs of Paths and Cycles*, arXiv:2303.08190v1 (2023-03-14), https://arxiv.org/abs/2303.08190.
- D. Avis, D. A. Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, arXiv:2203.16861v1 (2022-03-31), https://arxiv.org/abs/2203.16861.
