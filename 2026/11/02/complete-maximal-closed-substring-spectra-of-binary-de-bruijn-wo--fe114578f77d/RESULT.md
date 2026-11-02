# Complete maximal-closed-substring spectra of binary de Bruijn words through order five

## Finding

Let \(\mathcal B_m\) be the set of binary cyclic de Bruijn words of order \(m\), with cycles identified up to rotation but not reversal or alphabet complement. Every member has a unique rotation beginning with the length-\(m\) block of all zeros. Its *canonical linearization* \(L(B)\) is this rotation followed by its first \(m-1\) symbols, hence has length \(2^m+m-1\). Write \(K(B)\) for the number of **occurrences** of maximal closed substrings of the finite word \(L(B)\), including maximal closed substrings of length one. Distinct equal-valued occurrences are counted separately.

The complete spectra through order five are:

| Order \(m\) | Total cycles | Multiplicities \(k:\#\{B\in\mathcal B_m:K(B)=k\}\) |
|:--:|--:|:--|
| 1 | 1 | 2:1 |
| 2 | 1 | 4:1 |
| 3 | 2 | 8:2 |
| 4 | 16 | 19:4, 20:10, 21:2 |
| 5 | 2048 | 40:8, 41:16, 42:112, 43:204, 44:252, 45:304, 46:308, 47:264, 48:176, 49:124, 50:108, 51:84, 52:52, 53:28, 54:8 |

In particular, for order five the attainable values are *every integer from 40 through 54*, with eight canonical cycles at each extreme. One extremal linearization with 40 occurrences is

`000001010111011010010001100111110000`

and one with 54 is

`000001000110101110010100111110110000`.

The complete order-five population has mean \(2957/64\) maximal closed substring occurrences. Thus the output size of maximal-closed-substring enumeration varies by a factor \(54/40\) within the order-five de Bruijn family, despite identical length and complete coverage of all five-bit windows.

## Assumptions and scope

An order-\(m\) binary cyclic de Bruijn word is a cyclic sequence of length \(2^m\) in which every binary word of length \(m\) occurs exactly once as a *cyclic* window. All string positions and substring intervals in \(L(B)\) are *linear* (without wraparound), indexed from zero in the checker. A nonempty finite word \(u\) is **closed** when it has length one or it has a nonempty proper border \(v\) occurring in \(u\) exactly at its prefix and suffix, with overlaps allowed. A substring occurrence \(L(B)[i..e]\) is **maximal closed** when it is closed and neither of its possible one-character extensions within \(L(B)\) is closed. This definition is occurrence-based; maximality is not maximality among distinct factor values.

The claim concerns the complete finite families \(1\leq m\leq5\), not a limiting distribution or all orders. The choice of the unique all-zero rotation removes the otherwise noncanonical cut position; its final \(m-1\) symbols are prescribed by linearization and cannot be changed arbitrarily.

## Proof

**1. Exhaustive, nonduplicating enumeration of the domain.** Model binary length-\(m\) words as edges of the directed binary de Bruijn graph, with an edge from its \(m-1\)-prefix to its \(m-1\)-suffix. An order-\(m\) cycle is exactly an Eulerian circuit traversing every edge once. Its all-zero edge is unique, so rooting the circuit at that edge yields exactly one canonical linearization per cyclic word. The embedded `verify.py` starts with the all-zero edge used and depth-first explores both possible next bits, never reusing an edge. At completion it checks all cyclic length-\(m\) windows and retains precisely the Eulerian circuits. Every Eulerian circuit rooted at the all-zero edge is visited because each transition is explored, and none is repeated because its bit string determines its traversal uniquely. This is a complete finite enumeration, not a sample. The numbers of completed words at orders one through five are respectively 1, 1, 2, 16, and 2048, agreeing with the classical binary de Bruijn cycle count \(2^{2^{m-1}-m}\).

**2. Exact independent characterization of closedness.** For each completed word, one checker inspects *every* nonempty interval. For each length-at-least-two factor \(u\), it inspects all possible proper border lengths. Such a border \(v\) witnesses closedness precisely when the next occurrence of \(v\) after its initial position is at \(|u|-|v|\). This tests intervening occurrences, including overlapping ones, and is equivalent to the definition of closedness. It then tests the two adjacent one-character extensions, when present, to identify maximal closed occurrences.

**3. Cross-check by longest common prefixes.** Independently, for every pair of suffix starting positions \(i<j\), form their longest common prefix length \(\ell(i,j)\). At fixed \(i\), the positive *strict record* values of \(\ell(i,j)\) as \(j\) increases correspond exactly to closed factors \(L(B)[i..j+\ell(i,j)-1]\) that cannot extend to the right while remaining closed. To prove this, any earlier occurrence with at least \(\ell(i,j)\) matching symbols would create an internal border occurrence; conversely a strict record has no such intervening occurrence. A right extension cannot be closed because \(\ell(i,j)\) is the full common-prefix length. Such a factor is also left-maximal precisely when \(i=0\) or its two border occurrences have unequal immediately preceding symbols. Length-one maximal closed occurrences are exactly the isolated symbols relative to their existing neighbors. This gives the separate record-LCP checker.

**4. Exhaustive accumulation.** For each enumerated canonical word, the interval-definition checker and the record-LCP checker produce *identical sets of endpoint pairs*. Accumulating the number of endpoint pairs yields precisely the table in the finding. The order-five frequencies sum to 2048, both extreme witnesses pass the cyclic-window check, and the stated mean follows by the exact weighted sum of the table. No probabilistic inference, solver optimization, or extrapolation beyond order five enters this proof.

## Verification

Run `python3 verify.py` using the included standalone Python 3 source. It uses only standard-library integer, string, and hashing operations and finishes with the exact line `DEBRUIJN_MCS_CENSUS_VERIFY_OK` if and only if every enumeration, histogram, witness and independent endpoint comparison passes. The checker confirms each cycle's length, unique all-zero start, all cyclic length-\(m\) factors, and uniqueness among generated cycles. It outputs a deterministic SHA-256 digest of the ordered canonical-word list for each order; for order five this is `b47b0bf70bc81346dc18f851456e7c19754b65a4a8294a61312f3b02a099ceb1`.

## Relationship to prior work

Shibata, Umezaki, Mieno, Nakashima and Inenaga study online enumeration of maximal closed substrings and characterize their one-step maximality in [1]. Umezaki, Shibata, Nakashima and Inenaga study compact enumeration from run-length encoding in [2]. Kosolobov [3] establishes general asymptotic bounds for closed repeats, an equivalent representation of maximal closed substrings. These results give definitions, algorithms, and general complexity bounds, but do not determine the present distribution for canonical binary de Bruijn words. The familiar Euler-tour/de Bruijn count fixes the number of objects being enumerated; it does not fix the maximal-closed-substring statistics on those objects. The current finite spectrum is a workload-sensitive statistic on a natural maximally factor-diverse family.

## Limitations

The distribution is for the specified canonical *linearization* of cyclic words, not a newly defined cyclic maximal-closed-substring statistic or the distribution over all cut positions. Only orders at most five are classified. The computations are exact and fully enumerative but do not establish a recurrence, asymptotics, or extremal bounds for higher orders. No independent external mathematical audit or definitive publication-priority determination has been performed.

## References

1. H. Shibata, H. Umezaki, T. Mieno, Y. Nakashima, S. Inenaga, *Online computation of maximal closed substrings*, arXiv:2607.00612, first submitted July 1, 2026. https://arxiv.org/abs/2607.00612
2. H. Umezaki, H. Shibata, Y. Nakashima, S. Inenaga, *Compact Enumeration of Maximal Closed Substrings in Run-Length Encoded Strings*, arXiv:2607.02838, first submitted July 3, 2026. https://arxiv.org/abs/2607.02838
3. D. Kosolobov, *Closed Repeats*, arXiv:2410.00209, first submitted September 30, 2024. https://arxiv.org/abs/2410.00209
