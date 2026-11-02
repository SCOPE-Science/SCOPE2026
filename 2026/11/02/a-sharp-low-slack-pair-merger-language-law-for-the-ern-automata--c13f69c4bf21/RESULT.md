# A sharp low-slack pair-merger language law for the Černý automata

## Finding

Fix \(n\ge3\). In the classical \(n\)-state Černý automaton, every unordered pair of distinct states admits a **unique shortest merging word**. More substantially, the entire number of merging words at any extra length up to \(\lfloor(n-1)/2\rfloor\) follows the same explicit two-factor rational series. This linear-in-\(n\) low-slack interval is **sharp**, with exactly one additional non-idling word appearing at the first length beyond it for the hardest pair.

Write \(d_n(P)\) for the shortest length merging a pair \(P\), and \(N_n(P,L)\) for the number of words of length exactly \(L\) that merge it (possibly before the final letter). Define \(D_n\) and \(s_n\) below. Then for every integer \(n\ge3\), every distinct pair \(P\), and all integers \(0\le t\le \kappa_n=\lfloor(n-1)/2\rfloor\),

\[
\boxed{\displaystyle
N_n(P,d_n(P)+t)=[z^t]\frac{1}{(1-z)^{s_n(P)}(1-2z)},\qquad d_n(P)=D_n(P).
}
\]

For the hardest pair \(P_*=\{0,\lfloor n/2\rfloor\}\), write \(M_n=\binom n2\) and \(s_*=\binom{n-1}{2}\). Exactly at the first excluded slack,

\[
\boxed{\displaystyle N_n(P_*,M_n+\kappa_n+1)
=[z^{\kappa_n+1}]\frac1{(1-z)^{s_*}(1-2z)}+1.}
\]

The one-letter-over-optimum case is \(N_n(P,d_n(P)+1)=s_n(P)+2\), giving the sharp worst-pair count \(\binom{n-1}{2}+2\).

## Assumptions and scope

The state set is \(Q_n=\{0,1,\ldots,n-1\}\). The alphabet is precisely \(\{a,b\}\), with letters applied in written left-to-right order:

\[
a(q)=q+1\pmod n,\qquad b(q)=\begin{cases}0,&q=n-1,\\q,&0\le q<n-1.\end{cases}
\]

Each word acts on the *same initial unordered pair*. Counting includes words that have already merged the pair before the last symbol; after merging, both letters preserve singleton status. No statement concerns the full-state reset length except by way of motivation.

For \(P=\{i,j\}\), \(0\le i<j<n\), put \(h=j-i\) and

\[
D_n(i,j)=\begin{cases}
nh-i,&2h<n,\\
\binom n2-i,&2h=n,\\
(n-h)(n+1)-n-i,&2h>n.
\end{cases}
\]

Define

\[
s_n(P)=\#\{\{u,v\}:0\le u<v<n-1,\ D_n(u,v)\le D_n(P)\}.
\]

The coefficient formula is meaningful even when \(s_n(P)=0\), in which case the first factor is one. For the boundary case \(n=2\), the sole pair merges as soon as a letter \(b\) occurs, so \(N_2(P,1+t)=2^{t+1}-1\), \(t\ge0\); it is excluded from the uniform low-slack formula.

## Proof

**1. A complete distance ranking.** Set \(M_n=\binom n2\). The integers \(D_n(i,j)\) enumerate \(1,2,\ldots,M_n\) exactly once. Indeed, group the pairs by their shorter circular separation \(r=\min(j-i,n-j+i)\). For each \(r<n/2\), there are exactly \(n\) such pairs. The two orientations appearing in the piecewise formula fill precisely the consecutive ranks \((r-1)n+1,\ldots,rn\). When \(n\) is even, the remaining \(n/2\) antipodal pairs fill ranks \((n/2-1)n+1,\ldots,M_n\). Thus the pair \(P_*\) of the statement is the unique pair with distance rank \(M_n\).

**2. Transitions and the sharp upward-jump gap.** If a pair \(\{i,j\}\) has \(j<n-1\), then \(a\) reduces its rank exactly by one and \(b\) leaves the pair unchanged. For the pair \(\{0,n-1\}\), the letter \(b\) merges it and \(a\) raises its rank from one to \(n\). For other pairs \(\{i,n-1\}\) compare the two images \(\{0,i\}\) under \(b\) and \(\{0,i+1\}\) under \(a\). Direct substitution in the three branches of \(D_n\) gives the following exhaustive table. A 'jump' is the value of \(D_n\) after the nondescending letter minus its value before that letter; the other letter lowers rank by one.

| Ring length | Range of \(i\) | Descending letter | Other-letter jump |
|---|---|---|---|
| \(n=2k+1\) | \(1\le i\le k-1\) | \(b\) | \(n-1\) |
| \(n=2k+1\) | \(i=k\) | \(a\) | \(k\) |
| \(n=2k+1\) | \(k+1\le i\le n-2\) | \(a\) | \(n\) |
| \(n=2k\) | \(1\le i\le k-2\) | \(b\) | \(n-1\) |
| \(n=2k\) | \(i=k-1\) | \(b\) | \(k-1\) |
| \(n=2k\) | \(k\le i\le n-2\) | \(a\) | \(n\) |

The special pair \(\{0,n-1\}\) has its nondescending \(a\)-jump \(n-1\). Empty ranges in this table contribute nothing. Consequently every pair has **exactly one** outgoing letter lowering the rank by one. Its other letter either makes a literal self-loop or raises rank by at least \(\kappa_n=\lfloor(n-1)/2\rfloor\). Exactly **one** state-letter transition attains the minimum upward jump \(\kappa_n\): it is \(b\) from \(\{k,2k\}\) when \(n=2k+1\), and \(a\) from \(\{k-1,2k-1\}\) when \(n=2k\).

Because every transition lowers rank by at most one, reaching a singleton from rank \(d\) takes at least \(d\) letters. Repeating the uniquely rank-decreasing letter achieves \(d\), proving \(d_n(P)=D_n(P)\) and uniqueness of the shortest merging word. This descending path visits each lower rank exactly once.

**3. Counting all words in the low-slack window.** Consider a merging word of length \(d+t\), starting at rank \(d\), with \(0\le t\le\kappa_n\). An upward jump costs one letter yet increases the remaining necessary descent by at least \(\kappa_n\); consequently it would consume at least \(\kappa_n+1\) extra letters and cannot occur. Thus every such word follows the unique descending rank chain, possibly with repetitions of a self-loop, and may end with an arbitrary suffix after merging. Along that chain, the self-loop transitions occur exactly at the \(s_n(P)\) pairs omitting the state \(n-1\), and all such loops are labeled \(b\).

Allocating a total of \(e\) loop letters among \(s_n(P)\) ordered loop positions with repetition gives \(\binom{s_n(P)+e-1}{e}\) choices, with the standard convention of one choice for \(s=e=0\) and zero for \(s=0,e>0\). The remaining \(t-e\) letters after the merge have \(2^{t-e}\) choices. Summation over \(0\le e\le t\) proves the coefficient formula. The description is disjoint because the first deviation from the forced descending path locates each loop insertion, and the terminal suffix begins only after the unique first merge.

**4. Sharpness.** The pair \(P_*\) has rank \(M_n\), so its unique descending path visits the one pair with an upward jump of exactly \(\kappa_n\). Taking that wrong letter once and then following the uniquely decreasing letters produces a merging word of length \(M_n+\kappa_n+1\). All other upward jumps cost strictly more slack; at this exact length, no loops or terminal suffix can coexist with that one jump. Therefore this is exactly one additional word beyond the loop-and-suffix coefficient, proving the sharp formula. The two-state boundary follows immediately from its transition maps.

## Verification

A standalone Python 3 standard-library program, `verify_pairs.py`, independently builds the complete unordered-pair automaton; reverse-BFS computes shortest merging distances, while separate exact dynamic programming counts words at the claimed lengths. It checks the rank permutation, unique descending letter, sole minimal upward jump, low-slack counts for **every pair** and every permitted slack, and the first sharp correction for all \(3\le n\le22\). For \(3\le n\le5\) it additionally enumerates actual input strings as an independent check, and it verifies the \(n=2\) boundary. Running `python3 verify_pairs.py` prints `VERIFY_OK`. The proof, not the finite range, establishes the unlimited quantifiers.

## Relationship to prior work

Kisielewicz, Kowalski and Szykuła (first public online in 2013) develop shortest-reset algorithms and analyze Černý automata at the full-state level. Montoya and Nolasco (2017, §2.1, pp. 2155–2156) explain that the Černý pair automaton realizes a path through all unordered pairs, explicitly establishing the extremal pair-time bound for even ring lengths. Their action conventions differ by a cyclic relabeling of states. This existing Hamiltonian-path observation already entails the *distance-rank spectrum*, and **no novelty is claimed for the extremal bound or the mere existence of the pair path**. The claim here is instead the full near-geodesic language enumeration over a growing slack interval, its exact state-dependent coefficient, and a proven first extra word at a sharp boundary. The inspected source material does not supply those counts or the unique-minimum upward-jump analysis. Historical priority is not independently certified.

## Limitations

The result counts words synchronizing one specified **pair**, not all \(n\) states. The formula is established only for the stated low-slack window; beyond that window, upward excursions can contribute and the same coefficient need not apply. The finite checker is corroborative rather than an infinite-length proof. No claim is made about general synchronizing automata, triple merging, or cryptographic applications. Incomplete access to unindexed historical work leaves residual originality risk.

## References

- A. Kisielewicz, J. Kowalski and M. Szykuła, *Computing the shortest reset words of synchronizing automata*, Journal of Combinatorial Optimization 29 (2015), 88–124; first public online 17 November 2013. https://doi.org/10.1007/s10878-013-9682-0
- J. A. Montoya and C. Nolasco, *On the Synchronization of Small Sets of States*, Applied Mathematical Sciences 11 (2017), 2151–2173, especially §2.1, pp. 2155–2156. https://doi.org/10.12988/ams.2017.77232
