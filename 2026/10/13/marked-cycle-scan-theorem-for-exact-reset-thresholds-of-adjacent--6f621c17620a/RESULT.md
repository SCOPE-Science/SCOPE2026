# Marked-cycle scan theorem for exact reset thresholds of adjacent-merge automata

## Finding
For every integer \(n\ge2\) and every nonempty subset \(J\) of \(\mathbb Z/n\mathbb Z\), the reset threshold of the cyclic adjacent-merge automaton defined below equals the shortest backward cyclic scan that encounters \(n-1\) marked sites, counting multiple turns:
\[
R(n,J)=\min_{s\in\mathbb Z/n\mathbb Z}\min\left\{L\ge1:\sum_{r=0}^{L-1}\mathbf1_J(s-r\bmod n)\ge n-1\right\}.
\]
If \(J=\{u,v\}\) consists of exactly two distinct sites, write \(d=\min((u-v)\bmod n,(v-u)\bmod n)\). The formula becomes
\[
R(n,\{u,v\})=\begin{cases}
\frac{n(n-2)}2+1,&n\text{ even},\\
\frac{n(n-3)}2+1+d,&n\text{ odd}.
\end{cases}
\]
For one site it recovers the previously known \((n-1)^2\) threshold of the Černý automata. This is one exact reset-threshold classification, including its two-site specialization.

## Assumptions and scope
States are \(Q=\mathbb Z/n\mathbb Z\). The alphabet comprises a permutation \(a\) with \(a(i)=i+1\pmod n\), and, for each \(j\in J\), a distinct unitary idempotent \(b_j\) that maps \(j-1\mapsto j\) and fixes every other state. A reset word is a finite word mapping all \(n\) initial states to the same state. Its length counts one for every letter. No condition of primitivity or coprimality is imposed on \(n\) or on the gaps of \(J\). The set \(J\) must be nonempty; otherwise synchronization is impossible.

## Proof
**Inverse intervals.** For \(s\in Q\) and \(1\le k<n\), set \(I(s,k)=\{s,s+1,\ldots,s+k-1\}\pmod n\). These are nonempty proper cyclic intervals, with an unambiguous left endpoint \(s\). The inverse image under \(a\) is exactly \(I(s-1,k)\). For any \(j\in J\), inverse image under \(b_j\) has precisely three possible nonempty forms: (i) \(I(s-1,k+1)\) if \(j=s\) (and \(k<n\)); (ii) \(I(s,k-1)\) if \(j-1\) is the last element and \(j\) lies outside \(I(s,k)\), provided \(k>1\); or (iii) the same interval in all other cases. In case (ii) with \(k=1\), the preimage is empty. This follows directly because \(b_j\) only changes the image of state \(j-1\), and these are the two possible boundary placements of adjacent sites \(j-1,j\). Thus, until the full state set is reached, every nonempty iterated inverse image of a singleton is a cyclic interval; an inverse step enlarges its cardinality only in case (i), by exactly one. Its left endpoint moves one site backward precisely under an inverse \(a\)-step or under an enlarging inverse \(b_j\)-step. In the latter case the old left endpoint is a marked site in \(J\).

**Lower bound.** Take a reset word of length \(L\) with final state \(q\). Process its letters in reverse order, starting at \(\{q\}\) and taking full inverse images. All these inverse images are nonempty (because the final full inverse image equals \(Q\)). Stop on first reaching \(Q\). In order to increase size from one to \(n\), at least \(n-1\) enlargement steps are necessary; any shrink steps only increase that number. Let \(t\le L\) be the number of steps that move the left endpoint backward, ignoring any stationary steps. The successive old left endpoints of these \(t\) moving steps form a consecutive backward cyclic scan starting at \(q\). Each enlargement is one of these moving steps and uses a marked old endpoint, so that scan contains at least \(n-1\) marked positions. It follows that the minimum marked-scan length on the right-hand side is no larger than \(t\le L\), proving the lower bound.

**Matching word.** Choose a site \(s\) and minimum length \(L\) attaining the displayed scan count. Start with the singleton interval \(I(s,1)\) and read the scan backwards. At each current left endpoint \(x\), take inverse \(b_x\) if \(x\in J\), and inverse \(a\) otherwise. Until the \((n-1)\)-st marked visit, the inverse set is a proper interval. Every marked step enlarges its size by one; every unmarked step translates it one site backward; in either case the left endpoint becomes \(x-1\). After exactly \(L\) steps the inverse image is all of \(Q\). Reversing this list of inverse letters gives a length-\(L\) reset word, establishing equality.

**Two marks.** When \(n=2m\) is even, the required \(n-1=2m-1\) marked visits consist of \(m-1\) complete turns (\(2m-2\) visits) and one more marked site. A scan of \((m-1)n\) steps has too few visits and an additional single step suffices when a scan begins at a mark. Hence \(R=(m-1)n+1=n(n-2)/2+1\). When \(n=2m+1\) is odd, \(n-1=2m\) visits require \(m-1\) complete turns and two additional marked sites. The minimum length containing both sites on the final partial turn is \(d+1\), where \(d\) is the shorter directed gap. Consequently \(R=(m-1)n+d+1=n(n-3)/2+1+d\). For a single mark, \(n-1\) visits have minimum scan length \((n-2)n+1=(n-1)^2\). These computations include \(n=2\) and \(n=3\).

## Verification
The standalone standard-library script `artifacts/verify.py` independently computes exact shortest reset lengths by forward breadth-first search on subsets and compares them with the scan formula. It exhausts every nonempty mark set for \(2\le n\le8\), additional two-mark and sampled families for \(9\le n\le11\), and the inverse-interval cases for \(2\le n\le12\). It also reconstructs the explicit inverse-scan reset words and checks the resulting forward images. Run `python3 artifacts/verify.py`. The recorded successful output is `VERIFY_OK automata=793 interval_cases=6083 complete_subfamilies=n2..8 random_and_two_pin=n9..11 one_pin=(n-1)^2 two_pin_parity_gap=checked forward_BFS=independent backward_witness=replayed`. These finite checks confirm the implementation; the preceding symbolic proof establishes the all-\(n\), all-\(J\) claim.

## Relationship to prior work
The \(|J|=1\) case is the standard Černý automaton and its known extremal reset threshold, and is not a novel result. Rystsov and Szykuła (arXiv:2307.01302, Section 4) study primitive automata with permutation and unitary letters and characterize synchronizability in terms of orbital graphs. Volkov (arXiv:2306.13317) proves conditions forcing synchronization from primitivity and defect-one transformations. Ferens and Szykuła (arXiv:2208.05956) address completely reachable automata and broad quadratic thresholds. None of these inspected statements determines the exact threshold for every chosen set of adjacent mergers on a fixed cycle; their general synchronization and bound results do not imply the mark-location-dependent formula. The new contribution is the exact shortest-window invariant and its explicit two-site parity-and-gap law.

## Limitations
The theorem applies only to letters that are the stated forward cycle and selected adjacent simple idempotents. Arbitrarily directed mergers, extra permutation letters, nonunitary letters and partial automata are outside its scope. It does not assert any improvement of the general Černý upper bound for all automata or any result for non-synchronizing systems. The originality comparison is limited to inspected accessible literature and available indexed records; independently confirming publication priority remains appropriate.

## References
1. M. V. Volkov, *Synchronization of primitive automata*, arXiv:2306.13317, first version 23 June 2023, https://arxiv.org/abs/2306.13317.
2. I. Rystsov and M. Szykuła, *Primitive Automata that are Synchronizing*, arXiv:2307.01302, first version 3 July 2023, https://arxiv.org/html/2307.01302v1.
3. R. Ferens and M. Szykuła, *Completely reachable automata: a quadratic decision algorithm and a quadratic upper bound on the reaching threshold*, arXiv:2208.05956, https://arxiv.org/html/2208.05956v5.
4. I. Rystsov, *Černý's conjecture for automata with simple idempotents*, Cybernetics and Systems Analysis (2022), DOI:10.1007/s10559-022-00428-3.
