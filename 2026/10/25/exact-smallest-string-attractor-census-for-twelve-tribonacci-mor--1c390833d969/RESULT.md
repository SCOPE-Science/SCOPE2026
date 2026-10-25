# Exact smallest-string-attractor census for twelve Tribonacci morphic words

## Finding
Let \(\mu(0)=01\), \(\mu(1)=02\), and \(\mu(2)=0\), and put \(T_k=\mu^k(0)\). An attractor of a nonempty word is a set of positions such that each distinct nonempty contiguous factor has some occurrence crossing one of those positions. Positions are indexed from zero. Write \(a_k\) for the number of **minimum-cardinality** attractors of \(T_k\).

The following table is exact, with no assertion outside the displayed index range.

| \(k\) | \(|T_k|\) | minimum size | \(a_k\) |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 |
| 1 | 2 | 2 | 1 |
| 2 | 4 | 3 | 2 |
| 3 | 7 | 3 | 8 |
| 4 | 13 | 3 | 12 |
| 5 | 24 | 3 | 16 |
| 6 | 44 | 3 | 32 |
| 7 | 81 | 3 | 56 |
| 8 | 149 | 3 | 112 |
| 9 | 274 | 3 | 224 |
| 10 | 504 | 3 | 416 |
| 11 | 927 | 3 | 832 |

Every optimal position set in the table is specified **completely**, not sampled, by `certificates/attractors.json`. In particular, the multiplicity for order ten is \(416\), not \(448\); the initial observed doubling pattern does not persist unchanged.

## Assumptions and scope
The alphabet is exactly \(\{0,1,2\}\), and the substitution is iterated as written, without a terminal-symbol deletion. An occurrence of a factor \(f\) in \(w\) starting at \(i\) spans positions \(i,\ldots,i+|f|-1\). Each attractor is an unordered set, represented by an increasing list of distinct zero-based positions. The statement is a **complete finite computation** for the twelve canonical morphic iterates \(0\le k\le11\). It is not a recurrence for all orders.

## Proof
For a word \(w\) of length \(n\), associate to each distinct nonempty factor \(f\) the finite set \(C_w(f)\) of positions covered by **at least one** occurrence of \(f\). It follows immediately from the definition that \(S\subseteq\{0,\ldots,n-1\}\) is an attractor exactly when \(S\cap C_w(f)\ne\varnothing\) for every factor \(f\).

Each set \(C_w(f)\) is computed exactly: enumerate every starting position and every positive length, use the literal factor bytes to group equal substrings, and OR the bit masks of the occurrence intervals. The list of constraints may be reduced without changing its feasible sets: whenever \(C_w(f)\subseteq C_w(g)\), the constraint for \(g\) is redundant. Ordering distinct bit masks by cardinality and discarding those containing a previously retained mask computes exactly the inclusion-minimal antichain of coverage constraints.

Every attractor must contain a position carrying each different alphabet symbol, since it must meet each length-one factor. For \(k\ge2\) the word \(T_k\) contains all three symbols, so any size-three attractor necessarily contains **exactly one position of each symbol**. Fix positions \(x\) and \(y\) occupied by two different symbols, and let \(P\) denote the set of positions of the third symbol. The possible third positions are exactly
\[
P\cap\bigcap_{C:\,x\notin C,\;y\notin C} C,
\]
where \(C\) ranges over all inclusion-minimal coverage sets. Computing this intersection as an exact integer bit mask and listing its set bits enumerates **all** valid triples, without omissions or duplicates. This procedure checks each possible pair of positions for the first two symbols and exhaustively enumerates its third choices. For \(k=0,1\), direct inspection gives the single complete attractor \(\{0\}\) and \(\{0,1\}\), respectively.

The supplied `verify.py` performs this exact exhaustive operation for each word \(T_k\), \(0\le k\le11\), and compares the entire sorted list of optimal position sets with `certificates/attractors.json`. Its output establishes the twelve counts in the table. Non-emptiness of these lists supplies matching upper bounds for minimum attractor cardinality, while the distinct-letter lower bounds above prove minimality. This is a finite exhaustive proof whose correctness is directly inspectable in the self-contained source; no conjectured infinite recurrence is used.

## Verification
Run `python3 verify.py` in the directory containing `certificates/attractors.json`. It checks the exact generated word by SHA-256 at each of twelve orders, reconstructs every factor coverage mask, reduces logically redundant constraints, and enumerates and checks each optimal position tuple. Every table entry and every list in the certificate must match.

Run `python3 verify_independent.py` for a separate factor-by-position incidence computation through order nine (length \(274\)). This second program constructs, for each position, the set of distinct factors with an occurrence crossing it; it tests every candidate triple using unions of those sets. It does not reuse the factor-coverage-mask enumeration. The two exact methods agree on each of their shared instances. Integer bit masks are unbounded and substring keys are exact bytes: there is no floating-point error, probabilistic hashing, or cutoff inside any asserted source length.

## Relationship to prior work
Schaeffer and Shallit, *String Attractors for Automatic Sequences* (arXiv:2012.06840, Section 5, Theorem 6), prove that prefixes of the Tribonacci word of length at least four have minimum-attractor size three and give one attracting triple. Dvořáková, *String attractors of episturmian sequences* (arXiv:2211.01660, Theorem 7 and Example 8), gives a construction of a minimum attractor for each episturmian factor, including Tribonacci examples. These size/existence statements are consistent with, but do not supply, the **numbers of all optimum triples** or their complete lists.

Banbara et al., *The Smallest String Attractors of Fibonacci, Period-Doubling, and Thue–Morse Words* (arXiv:2602.16152; initially public February 18, 2026), motivate the multiplicity invariant by classifying every optimum for those three other canonical families. The present finite exact Tribonacci census complements that program without extending their proved infinite families. Faro, Marino, and Pavone (arXiv:2610.10950) analyze Thue–Morse minimal-coverage certificates and likewise do not enumerate Tribonacci optima.

## Limitations
The data give exact multiplicities **only for the first twelve specified iterates**, not a general closed formula or growth law. The fact that some consecutive counts double does not imply future doubling. Exhaustiveness is finite and relies on the supplied algorithm rather than a short symbolic classification of the solution triples. Historical priority beyond the inspected sources and indexed searches cannot be guaranteed. The minimum size three itself is previously known; the contribution is the multiplicity table and complete finite solution lists.

## References
1. L. Schaeffer and J. Shallit, *String Attractors for Automatic Sequences*, arXiv:2012.06840, especially Theorem 6 and its constructive witness.
2. L. Dvořáková, *String attractors of episturmian sequences*, arXiv:2211.01660, Theorem 7 and Example 8.
3. M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno, and Y. Okamoto, *The Smallest String Attractors of Fibonacci, Period-Doubling, and Thue–Morse Words*, arXiv:2602.16152 (first version 2026-02-18).
4. S. Faro, F. P. Marino, and A. Pavone, *Smallest String Attractors and Minimal Coverage Certificates of Thue–Morse Words*, arXiv:2610.10950 (2026-10-07).
