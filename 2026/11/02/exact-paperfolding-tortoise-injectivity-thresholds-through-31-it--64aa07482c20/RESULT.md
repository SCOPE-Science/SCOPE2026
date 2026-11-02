# Exact paperfolding tortoise-injectivity thresholds through 31 iterations

## Finding
Let \(\mathbf f=f_1f_2\cdots\) be the regular paperfolding word with \(f_j=0\) when the odd part of \(j\) is congruent to \(1\) modulo \(4\), and \(f_j=1\) when it is congruent to \(3\) modulo \(4\). Let \(\mathcal F_n\) be its set of distinct factors of length \(n\). The binary tortoise operator \(T\) moves the leftmost \(1\), if any, to the right end of a finite word; let \(T^k\) be its \(k\)-fold iterate.

Define \(s(k)\) to be the least positive integer \(N\), if it exists, such that \(T^k\) is injective on \(\mathcal F_n\) for every integer \(n\ge N\). For each integer \(1\le k\le31\), the threshold exists and has the **exact** value in the following table:

| Iterations \(k\) | Threshold \(s(k)\) | Iterations \(k\) | Threshold \(s(k)\) |
|---:|---:|---:|---:|
| 1 | 8 | 17 | 98 |
| 2 | 13 | 18 | 100 |
| 3 | 14 | 19 | 101 |
| 4 | 25 | 20 | 104 |
| 5 | 26 | 21 | 105 |
| 6 | 28 | 22 | 106 |
| 7 | 29 | 23 | 109 |
| 8 | 49 | 24 | 112 |
| 9 | 50 | 25 | 113 |
| 10 | 52 | 26 | 114 |
| 11 | 53 | 27 | 116 |
| 12 | 56 | 28 | 117 |
| 13 | 57 | 29 | 121 |
| 14 | 58 | 30 | 122 |
| 15 | 61 | 31 | 125 |
| 16 | 97 | — | — |


In particular, at the four nontrivial dyadic iteration depths \(k=2,4,8,16\), the sharp thresholds are respectively \(13,25,49,97\). The observations \(s(1)=8\) and the proposed values \(s(2)=13\), \(s(3)=14\), \(s(4)=25\), \(s(5)=26\) were already reported by Campbell and Rampersad: only the \(k=1\) case was proved there. The new claims are rigorous certification of all \(k=2,\ldots,31\), including the first \(26\) previously unreported values \(k=6,\ldots,31\).

## Assumptions and scope
Words are over the ordered alphabet \(\{0,1\}\). Factors may begin at any positive index in the infinite one-sided paperfolding word. The map \(T\) is precisely the binary restriction of Defant--Kravitz tortoise, not the hare operator. Thresholds concern all integer lengths \(n\ge N\), rather than merely the checked finite prefix or a bounded range of lengths. The quantified iteration depths are the integers \(1\le k\le31\), and no infinite-in-\(k\) formula is asserted.

## Proof
**1. Binary tortoise and deletion.** If a finite binary word contains \(r\) ones, \(T^k\) deletes its first \(\min(k,r)\) occurrences of \(1\) and appends that many copies of \(1\) in their original order. This follows directly by writing the word as runs of zeros separated by ones in the Defant--Kravitz recursion; one application removes the first one and appends it.

**2. A finite exhaustive factor model.** For any positive \(n<2^h\), let \(P=2^{h+1}\). Every factor of length \(n\) is attained with starting index among \(1,2,\ldots,5P\). To prove it, fix the starting residue \(r\) modulo \(P\), represented by \(1\le r\le P\), and compare windows with starts \(r+tP\) for \(t=0,1,2,3,4\). Within a window of length smaller than \(2^h\), at most one position is a multiple of \(2^h\). At every other position, the binary digit is invariant under shifts by \(P\), since removing at most \(h-1\) powers of \(2\) leaves a residue modulo \(4\) determined by the original position modulo \(2^{h+1}\). If the exceptional position has valuation exactly \(h\), successive shifts by \(P\) toggle its digit. If it is divisible by \(P\), the five consecutive quotients of the five positions by \(P\) include odd residues congruent to both \(1\) and \(3\) modulo \(4\). Thus either possible value for the sole exceptional digit occurs among these five windows; this proves the factor-covering bound. Equivalently, enumerate residues \(1\le r\le P\), fix all nonexceptional digits, and insert both binary choices at the unique exceptional position. Both constructions enumerate exactly \(\mathcal F_n\).

**3. One-length injectivity propagates to every larger length.** Fix positive integers \(k,m\). Assume every member of \(\mathcal F_m\) has at least \(k\) ones and that \(T^k\) is injective on \(\mathcal F_m\). Suppose two equal-length factors \(u,v\) with length \(n>m\) have equal \(T^k\)-images. Deleting the first \(k\) ones of either entire word gives the same word. Because those ones occur before position \(m\) in each factor, the first \(m-k\) letters of their common deleted word are obtained by deleting the first \(k\) ones in the respective length-\(m\) prefixes. The prefixes therefore have equal \(T^k\)-images; by assumed injectivity they are equal. Their first \(k\) deleted positions now coincide, and equality of the remaining deleted words forces equality of their tails. Hence \(u=v\), proving injectivity for every \(n\ge m\).

**4. Exactly 62 decisive finite tests.** The row for iteration \(k\) and threshold \(m=s(k)\) in `threshold_table.csv` records a distinct collision pair at length \(m-1\), while exhaustive enumeration confirms injectivity at length \(m\) and at least \(k\) ones in every length-\(m\) factor. Every row satisfies \(m\ge8\). The counts of distinct factors at the two lengths are \(4(m-1)\) and \(4m\), consistent with the classical exact paperfolding factor-complexity theorem; the counts are independently checked by both enumerators. Step 3 gives injectivity at every length \(n\ge m\), and the exhibited collision at \(m-1\) rules out any lower threshold. This establishes the entire table with finite *exhaustive* tests plus an infinite-length propagation lemma, not from a finite search alone.

## Verification
Run `python3 verify_skeleton.py` followed by `python3 verify_prefix.py` in a directory containing both programs and the CSV file (the first verifier deterministically writes `threshold_table.csv`). The first program uses the periodic-skeleton-with-one-free-digit characterization, the exact deletion formula, and a directly enumerated factor set. The second program independently generates the paperfolding word with the recurrences \(f_{2j}=f_j\), \(f_{4j+1}=0\), and \(f_{4j+3}=1\), scans all starts in the proven covering prefix, and evaluates \(T^k\) through repeated one-step relocation. For each of the 31 depths both programs verify the 62 decisive finite lengths, and the second checks the predecessor collision witnesses from the CSV. Their actual outputs are included as `skeleton_output.txt` and `prefix_output.txt`.

## Relationship to prior work
Defant and Kravitz introduced the tortoise operator on finite words. Campbell and Rampersad introduced \(k\)-tortoise factor complexity and proved \(s(1)=8\) for regular paperfolding; their 2026 manuscript reports \(13,14,25,26\) as *computational predictions* for \(s(2),\ldots,s(5)\), without proving them, and explicitly asks for the sequence's evaluation. Their theorem for one iteration does not imply injectivity for higher iterates on factor sets. The present finite-skeleton proof certifies those predictions and obtains all 26 further exact thresholds to iteration 31. The reported infinite-length proof rests on the prefix-heredity lemma and a complete arithmetic description of factors, not on extrapolation from samples.

## Limitations
No formula for \(s(k)\) at arbitrary iteration depth is proved; the apparent dyadic pattern beyond the displayed finite range is only a research direction. No claim is made about higher-iteration tortoise complexity for other automatic words, or about independent review. A separate priority risk remains that another source could have obtained part of this 31-term table or the elementary inheritance lemma.

## References
- J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811v2, Section 5 (first publicly submitted 2026-04-28), https://arxiv.org/html/2604.25811v2.
- C. Defant and N. Kravitz, *Stack-sorting for words*, Australasian Journal of Combinatorics 77 (2020), 51--68, arXiv:1809.09158, https://arxiv.org/abs/1809.09158.
- J.-P. Allouche, *The number of factors in a paperfolding sequence*, Bulletin of the Australian Mathematical Society 46 (1992), 23--32; factor-complexity result also stated in Campbell--Rampersad, Section 5.
