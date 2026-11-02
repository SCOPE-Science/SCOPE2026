# The first lossless-spectrum obstruction occurs for binary four-grams

## Finding

For a finite binary word \(w\) of length at least \(k\), let \(\operatorname{Spec}_k(w)\) be the **set** (not multiset) of its distinct length-\(k\) contiguous factors. A nonempty subset \(S\subseteq\{0,1\}^k\) is *realizable* if it equals this spectrum for some finite word. It is *losslessly realizable* if some such word has each factor of \(S\) **exactly once**, hence length \(|S|+k-1\).

**Exact theorem.** At \(k=3\), exactly \(121\) of the \(255\) nonempty binary factor supports are realizable, and all \(121\) are losslessly realizable. At \(k=4\), exactly \(5921\) of the \(65535\) nonempty supports are realizable, but only \(2611\) are losslessly realizable. Thus \(3310\) realizable four-gram supports require repeated factors in every representing word. The complete distribution by support size is:

| \(|S|\) | Realizable 3-gram supports | Lossless 3-gram supports |
|---:|---:|---:|
| 1,2,3,4 | 8, 13, 20, 25 | 8, 13, 20, 25 |
| 5,6,7,8 | 26, 20, 8, 1 | 26, 20, 8, 1 |

| \(|S|\) | Realizable 4-gram supports | Lossless 4-gram supports |
|---:|---:|---:|
| 1,2,3,4 | 16, 29, 52, 93 | 16, 29, 52, 91 |
| 5,6,7,8 | 162, 279, 454, 682 | 144, 217, 306, 372 |
| 9,10,11,12 | 924, 1064, 1010, 705 | 398, 355, 276, 182 |
| 13,14,15,16 | 334, 100, 16, 1 | 104, 52, 16, 1 |

The **smallest obstructed support size is four**, with exactly two such supports:

\[
\{0010,0101,1010,1011\},\qquad \{0100,0101,1010,1101\}.
\]

These supports are complements of each other. They are realized by `00101011` and `11010100` respectively, each with one repeated four-gram. No support containing fewer than four distinct four-grams requires repetition.

## Assumptions and scope

The alphabet is the fixed labeled binary alphabet \(\{0,1\}\). Words and supports are linear, not cyclic. A word with \(|w|<k\) has empty spectrum and is excluded. Losslessness is relative to the exact spectrum: a witnessing word must contain every specified factor and no unlisted length-\(k\) factors, with no repeated factor. Two supports differing by bit complementation are counted separately. The assertions concern only \(k=3,4\), although the algorithms below work for other finite \(k\).

## Proof

**1. Exact correspondence with directed walks.** The order-\((k-1)\) binary de Bruijn graph has vertices the \(2^{k-1}\) binary words of length \(k-1\), and one directed edge labeled by each \(k\)-gram \(e=b_1\cdots b_k\) from prefix \(b_1\cdots b_{k-1}\) to suffix \(b_2\cdots b_k\). Given a binary word of length at least \(k\), its consecutive overlapping \(k\)-grams spell a directed walk; conversely any directed walk spells a unique word after its starting \((k-1)\)-gram is fixed. The set of edges encountered is exactly its spectrum. It follows that a support \(S\) is realizable exactly when the graph restricted to edges \(S\) has a directed walk covering all its edges; it is losslessly realizable exactly when it has an Euler trail.

**2. A finite-state exhaustion that does not truncate walk length.** Number the \(k\)-grams from \(0\) to \(2^k-1\) by their binary values. For each vertex \(v\) and a bit mask \(M\) of previously encountered edges, form the state \((v,M)\). Start at all \(2^{k-1}\) states \((v,0)\). Each legal de Bruijn edge \(e:v\to u\) takes \((v,M)\) to \((u,M\cup\{e\})\). A breadth-first reachability closure through this **finite** state graph computes every possible nonempty spectrum mask. Even if a representing walk has arbitrarily many repeated edges, its last state is reached in this closure; hence this procedure exhausts *all* finite words, not merely words below a chosen length. For the lossless calculation, reject any edge transition already contained in \(M\); the resulting reachable masks are precisely the edge-trail supports. At \(k=3\) there are at most \(4\cdot2^8=1024\) possible states per procedure; at \(k=4\), at most \(8\cdot2^{16}=524288\) states. The embedded standard-library verifier enumerates the actual reachable states and masks, rather than trusting a claimed count.

**3. Independent graph-theoretic characterization.** For any nonempty edge set \(S\), form its directed graph and delete isolated vertices. Contract each strongly connected component. A single directed walk can cover every edge **if and only if** either there is one strongly connected component, or the component condensation consists of a directed chain with **exactly one** intercomponent edge between each successive pair and no other intercomponent edges. Necessity: once a walk leaves an SCC in the acyclic condensation, it can never return; therefore each intercomponent edge must occur exactly once and the succession of components must be one chain. Sufficiency: within any SCC one can traverse all its internal edges while moving from a chosen entry to a chosen exit (strong connectivity supplies connecting paths); traverse the chain's single intercomponent edges in order. This criterion yields a second exhaustive implementation over all \(2^{2^k}-1\) nonempty supports, using transitive reachability and condensation degrees. For \(k=3,4\), its realizable-mask sets agree **exactly** with the independent state-closure algorithm, not only in cardinality.

**4. Certified enumerations and the sharp obstruction.** The state-closure calculation returns at \(k=3\) exactly \(121\) realizable masks and \(121\) edge-trail masks; its cardinality distribution is the first table. At \(k=4\), it returns \(5921\) realizable masks and \(2611\) edge-trail masks with the second table. Subtracting yields \(3310\) masks requiring repetition. Exactly two realizable supports of cardinality four are absent from the trail set, and every realizable support of smaller cardinality is in that set. The two exceptions have the explicit binary-four-gram lists in the statement. For the first, the overlap graph includes the directed path `001→010→101→011` and the extra edge `101→010`; a walk covering all four edges must use `010→101` twice, because it is needed both before and after the `101→010` return. The string `00101011` makes exactly that repetition. The second obstruction follows by complementing every bit. This simultaneously proves the sharp minimum size four and provides witnesses.

## Verification

Execute `python3 verify_kgram.py`; the included `verify_kgram_output.txt` records the exact per-cardinality tables and the final line `ALL_CHECKS_PASSED`. In addition to the two distinct algorithms (state closure and strongly connected component criterion), the code independently enumerates all binary words of lengths three through ten, recovering exactly the \(121\) three-gram masks. This independent word enumeration is exhaustive for three-gram **lossless** profiles because a trail with at most eight distinct edges spells a word of length at most ten. The finite-state closure, not the bounded word enumeration, certifies the complete four-gram census.

## Relationship to prior work

Alanko and Pérez-López, *Computing k-mers in Graphs*, arXiv:2509.22885 (first submitted 2025-09-26), study counting distinct \(k\)-mers along graph walks and constructing de Bruijn graph representations. They do not state this exact spectrum-mask census for binary linear words or the lossless-transition threshold. Chukhin, Kulikov, Mihajlin and Smal, *The Greedy Superstring Algorithm Achieves Ratio 2 for Strings of Length 6 Already*, arXiv:2608.20018 (2026-08-20), define the linear \(k\)-spectrum and de Bruijn overlap graph and study **greedy shortest-superstring approximation**, not the exact set of realizable masks or which admit an edge-simple representing word. Their graph/trail framework motivates precisely separating occurrence-set feasibility from unique-edge traversal. The known basic Euler criterion is used and credited; the new contribution is the exact binary support census and the first-obstruction classification.

## Limitations

The numerical census is exhaustive **only** for the two specified window lengths, three and four, over a labeled binary alphabet. It does not assert a closed form for arbitrary window length or larger alphabets. The independent algorithms establish exhaustive finite correctness because every possible state or mask is covered, not because a bounded random experiment succeeded. A bounded primary-literature and indexed search does not exclude unpublished or unindexed equivalent tables. No independent mathematical audit is claimed.

## References

1. J. N. Alanko and M. Pérez-López, *Computing k-mers in Graphs*, arXiv:2509.22885, initial public submission 2025-09-26. https://arxiv.org/abs/2509.22885 ; full text https://drops.dagstuhl.de/storage/00lipics/lipics-vol369-cpm2026/html/LIPIcs.CPM.2026.3/LIPIcs.CPM.2026.3.html
2. N. Chukhin, A. S. Kulikov, I. Mihajlin, A. Smal, *The Greedy Superstring Algorithm Achieves Ratio 2 for Strings of Length 6 Already*, arXiv:2608.20018, initial submission 2026-08-20. https://arxiv.org/abs/2608.20018
