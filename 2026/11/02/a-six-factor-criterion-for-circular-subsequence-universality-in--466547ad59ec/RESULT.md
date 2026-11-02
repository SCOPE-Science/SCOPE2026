# A six-factor criterion for circular subsequence universality in binary de Bruijn cycles of order five

## Finding
Let \(W\) be a binary de Bruijn cycle of order five: a circular binary word of length \(32\) in which each length-five circular factor occurs exactly once. For a linear word \(u\), let \(\iota(u)\) be the largest integer \(k\geq 0\) for which *every* binary word of length \(k\) is a scattered subsequence of \(u\). Write \(W^{(t)}\) for the length-\(32\) linear word obtained by starting at circular position \(t\), and define the rotation-invariant maximum \(U(W)=\max_{0\leq t<32}\iota(W^{(t)})\).

**Theorem (complete order-five spectrum and local criterion).** Among the \(2048\) distinct order-five binary de Bruijn cycles up to rotation, exactly \(512\) satisfy \(U(W)=10\) and exactly \(1536\) satisfy \(U(W)=11\). Moreover,
\[
 U(W)=11\quad\Longleftrightarrow\quad
 \text{\(W\) contains the six-letter circular factor \(\mathtt{010101}\) or \(\mathtt{101010}\)}.
\]
The two alternating six-letter factors cannot coexist in an order-five binary de Bruijn cycle. The complete rotation-index distribution is as follows:

| Number of cycles | Six-letter alternating factor | Rotation indices (multiplicities) |
| ---: | :---: | :--- |
| \(512\) | Neither | \(\iota=9\) at \(4\) starts; \(\iota=10\) at \(28\) starts |
| \(768\) | \(\mathtt{010101}\) only | \(\iota=10\) at \(9\) starts; \(\iota=11\) at \(23\) starts |
| \(768\) | \(\mathtt{101010}\) only | \(\iota=10\) at \(9\) starts; \(\iota=11\) at \(23\) starts |

In particular every start has index at least nine, and the table gives every possible index at every rotation of every cycle. The actual circular words, rather than their arbitrary rootings, are the objects being counted.

## Assumptions and scope
All words are literal binary words; scattering permits gaps but preserves order. Circular factors may cross the end of a fixed linear representation; each \(W^{(t)}\) traverses the circle exactly once, never twice. For a representation \(w=w_0\cdots w_{31}\), its circular length-\(m\) factors for \(m\leq 32\) are \((ww)_{t}\cdots(ww)_{t+m-1}\), with \(0\leq t<32\). Cycles are equivalent under rotations, not under reversal or complement.

The classification is an **exact exhaustive finite theorem**, supported by a transparent finite exhaustive proof with a standalone checker. No assertion is made for de Bruijn orders other than five.

## Proof
**1. Feedback tables exhaust the cyclic objects without duplication.** Regard a five-bit word as a state \((b_0,b_1,b_2,b_3,b_4)\). Every order-five de Bruijn cycle defines a successor permutation of its \(32\) five-bit factors. For each fixed four-bit suffix \(s=(b_1,b_2,b_3,b_4)\), the two states \((0,s)\) and \((1,s)\) must have different outgoing final bits, since their successors must also be different states. Consequently the successor map has the form
\[
F_h(b_0,s)=(s,\,b_0\mathbin\oplus h(s)),
\]
where \(h:\{0,1\}^4\to\{0,1\}\) is one of exactly \(2^{16}\) Boolean functions. Conversely, for each such \(h\), the formula defines a permutation of the \(32\) states: from an output \((s,c)\), the unique predecessor is \((c\oplus h(s),s)\). It gives a binary order-five de Bruijn cycle precisely when its orbit starting at state \(\mathtt{00000}\) visits all \(32\) states before returning. Every de Bruijn cycle has exactly one rooting starting with the unique five-bit factor \(\mathtt{00000}\), and so corresponds to exactly one successful feedback table. Thus enumerating all integers \(0\leq H<2^{16}\) as the sixteen Boolean outputs is exhaustive and duplicate-free.

To make the enumeration unambiguous, encode \(s\) by the ordinary four-bit integer \(0\leq s\leq15\), take \(h_H(s)=(H\gg s)\,\&\,1\), and encode a five-bit state by its usual integer \(0\leq x\leq31\). Its successor is precisely the implementation's
\[
 x\longmapsto 2(x\bmod16)+\big(\lfloor x/16\rfloor\oplus h_H(x\bmod16)\big).
\]
A successful table is detected by exactly \(32\) distinct states and a return to the initial zero state. That is a finite algorithm using only bounded bit operations and comparisons, not a heuristic search.

**2. Scattered-subsequence universality is measured independently in two exact ways.** A *complete binary arch* of a word is its shortest nonempty prefix containing both \(0\) and \(1\); remove it and repeat until the suffix has fewer than two symbols. If there are \(k\) complete arches, any prescribed length-\(k\) binary word embeds by taking its successive symbols from successive arches. To see why no length-\(k+1\) universality is possible, let \(a_j\) be the symbol first completed at the last position of arch \(j\), for \(1\leq j\leq k\). Let \(b\) be a symbol absent from the incomplete final remainder. In every embedding of \(a_1\cdots a_k\), the earliest possible choice of \(a_j\), after earlier greedy choices, is the final position of the \(j\)th arch. Therefore \(a_1\cdots a_kb\) is not a subsequence. Thus \(\iota(u)\) equals the number of greedy complete binary arches of \(u\).

An independent exact test counts *distinct* subsequences, rather than greedy arches. For a suffix beginning at position \(i\), define \(n(i,a)\) as the position immediately after its first occurrence of letter \(a\), or an invalid sentinel if absent. Set \(D(i,0)=1\), and recursively set
\[
 D(i,m)=\sum_{a\in\{0,1\}:\,n(i,a)\text{ exists}}D(n(i,a),m-1).
\]
Each distinct subsequence has exactly one greedy earliest embedding, so \(D(0,m)\) counts distinct length-\(m\) subsequences. Consequently \(u\) is \(m\)-universal precisely when \(D(0,m)=2^m\). Both the greedy arch measure and this recurrence are independently implemented and compared for every one of \(32\) rootings of each successful table.

**3. The alternating-factor mechanism.** The state \(\mathtt{01010}\) has four-bit suffix \(\mathtt{1010}\), encoded by \(10\), and produces a sixth bit \(1\) exactly when \(h(10)=1\). Thus \(\mathtt{010101}\) occurs as a six-letter circular factor exactly when \(h(10)=1\). Similarly, the state \(\mathtt{10101}\), with suffix \(\mathtt{0101}\), produces sixth bit \(0\) exactly when \(h(5)=1\), giving \(\mathtt{101010}\). If both bits are \(1\), then the two states \(\mathtt{01010}\) and \(\mathtt{10101}\) form a closed two-cycle of \(F_h\). Hence no de Bruijn \(32\)-cycle can have both patterns.

**4. The exact exhaustive certificate.** The embedded `checker.py` iterates all \(65536\) sixteen-bit feedback tables, retains only single-orbit tables, and, for each one, compares the arch count with the independently computed distinct-subsequence count at all \(32\) starts. In addition it reconstructs all cyclic words independently by running an Eulerian-tour construction on the order-four binary de Bruijn graph for all \(65536\) assignments of local two-edge priorities. The two resulting sets of canonical rootings are compared for exact equality; the set has cardinality \(2048\). The tally produced *before asserting the stated target table* is

| \(h(5)\) | \(h(10)\) | Number of valid tables | Minimum \(\iota\) | Maximum \(\iota\) | Number of maximizing starts |
| ---: | ---: | ---: | ---: | ---: | ---: |
| \(0\) | \(0\) | \(512\) | \(9\) | \(10\) | \(28\) |
| \(1\) | \(0\) | \(768\) | \(10\) | \(11\) | \(23\) |
| \(0\) | \(1\) | \(768\) | \(10\) | \(11\) | \(23\) |
| \(1\) | \(1\) | \(0\) | — | — | — |

All loops are bounded by explicit small integers, all operations are exact integer/bit operations, and every assertion checks a finite universally quantified condition over the enumerated domain. Step 1 proves exhaustiveness; Step 2 proves that the computed statistic is the claimed invariant; Step 3 explains the two six-factor alternatives; Step 4 establishes the remaining exact frequencies and the characterization of the index values. This proves the theorem.

## Verification
With Python 3.9 or later, from the directory containing the embedded code, run `python checker.py`. It prints `FEEDBACK_TABLE`, `CIRCULAR_PROFILE`, `UNIQUE_CYCLES 2048`, and `CHECKS_PASSED` after verifying every asserted condition. The checker is self-contained and uses no third-party packages, random generators, floating-point arithmetic, parallel processes, downloaded data, or approximate comparisons.

The certificate has two independent *enumerators* (feedback-cycle permutations and de Bruijn-graph Euler circuits), and two independent *subsequence tests* (greedy arches and earliest-embedding dynamic programming). The proof does not extrapolate from a proper subset or from a timeout: it examines all \(65536\) feedback maps and verifies the complete domain. Its logical guarantees still depend on the transparently specified Python algorithm and the correctness of the implementation; it is not an externally audited formal proof.

## Relationship to prior work
De Bruijn's 1946 paper introduced the cycle construction and classical count, Zhi Xu’s 2010 multi-shift construction classifies contiguous windows at specified positions, while OEIS A169672 (first posted April 11, 2010) documents an explicit order-five binary cycle. General scattered-factor universality and circular variations are treated by Barker, Fleischmann, Harwardt, Manea and Nowotka (2020), while Fleischmann, Germann and Nowotka (2021) develop arch and remainder machinery. These general results supply a framework, but none of the specifically inspected statements supplies the complete order-five conjugacy-class counts and the six-letter alternating-factor criterion together with the per-rotation frequency distribution. Prior BWT-run and palindrome classifications of the same order-five cycles concern different invariants and do not imply scattered-subsequence universality counts. This is a comparison of actual implications, not a claim that absence of a database hit proves priority.

## Limitations
This is a complete finite theorem only for order-five binary de Bruijn circles. The rotation index is for a linear traversal of length exactly \(32\), not an indefinitely repeated periodic word, a length-\(31\) factor, or a two-traversal window. The enumerator is a transparent computational certificate rather than an independent, human-verified enumeration of every feedback case. Existing literature may contain an unindexed equivalent finite table; exhaustive historical priority is not guaranteed. No formula for larger de Bruijn orders follows automatically.

## References
1. N. G. de Bruijn, *A Combinatorial Problem*, Proceedings of the Koninklijke Nederlandse Akademie van Wetenschappen, 49 (1946), 758–764. https://research.tue.nl/en/publications/a-combinatorial-problem/
2. Zhi Xu, *Multi-Shift de Bruijn Sequence*, arXiv:1004.1216v1, first posted 2010-04-08. https://arxiv.org/html/1004.1216v1
3. N. J. A. Sloane, OEIS A169672, *Lexicographically earliest de Bruijn sequence for n = 5 and k = 2*, first posted 2010-04-11. https://oeis.org/A169672
4. M. Barker, P. Fleischmann, F. Harwardt, F. Manea, and D. Nowotka, *Scattered Factor-Universality of Words* (2020), https://arxiv.org/abs/2003.04629
5. P. Fleischmann, F. Germann, and D. Nowotka, *Scattered Factor Universality – The Power of the Remainder* (2021), https://arxiv.org/abs/2104.09063
6. D. Gabric and J. Sawada, *Investigating the Discrepancy Property of de Bruijn Sequences* (2020), https://arxiv.org/abs/2005.01638
