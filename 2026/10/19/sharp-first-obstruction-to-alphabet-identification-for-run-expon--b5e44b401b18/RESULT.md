# Sharp first obstruction to alphabet identification for run-exponent sums

## Finding

Write \(E(w)\) for the sum of the exponents of the runs of a finite word \(w\). Call a word *identification-resistant* when it uses at least three distinct symbols and **every** identification of two distinct symbols occurring in the word strictly decreases \(E\).

**Theorem.** An identification-resistant word has length at least \(12\). At length \(12\), the unique such word up to bijective renaming of its symbols is `001101121122`. Moreover, for every integer \(k\ge2\),
\[
  w_k=\texttt{0011011211}\,\texttt{2}^{k}
\]
is identification-resistant. Precisely, if \(\pi_{a\leftarrow b}\) identifies symbol \(b\) with symbol \(a\) and fixes all other symbols, then
\[
\begin{aligned}
 E(w_k)&=k+12,\\
 E(\pi_{0\leftarrow1}(w_k))&=k+11,\\
 E(\pi_{0\leftarrow2}(w_k))&=k+\tfrac{34}{3},\\
 E(\pi_{1\leftarrow2}(w_k))&=k+11.
\end{aligned}
\]
Thus identification-resistance is attainable at every length at least \(12\), and at no smaller length. The uniqueness assertion concerns word patterns up to symbol renaming, not reversal, rotation, or complement of an externally prescribed alphabet.

## Assumptions and scope

Positions are numbered from \(1\). A period \(p\ge1\) of the factor \(w[i..j]\) satisfies \(w[t]=w[t+p]\) for all \(i\le t\le j-p\). A run is a triple \((i,j,p)\) in which \(p\) is the **least** period, \(j-i+1\ge2p\), and the period cannot extend one place to either side within the word. Its exponent is \((j-i+1)/p\); \(E(w)\) sums this over all runs, counting each maximal periodic interval exactly once. A symbol identification means a letter-to-letter map collapsing exactly one chosen pair of symbols, leaving the others pairwise distinct. The alphabet may be any finite alphabet; only the symbols actually appearing matter. No claim is made about preservation or non-preservation of the global extremal quantity \(\sigma(n)\).

## Proof

**1. Exhaustive minimal-length certification.** Every length-\(n\) word is equivalent under bijective renaming of used letters to exactly one *restricted-growth string*: \(a_1=0\) and \(0\le a_i\le1+\max(a_1,\ldots,a_{i-1})\) for every \(i>1\). Consequently the recursive enumeration in `verify_fast.cpp` and `verify_independent.cpp`, with no fixed alphabet cap smaller than \(n\), covers every equivalence class. Discarding strings with fewer than three distinct symbols leaves \(B_n-2^{n-1}\) cases, where \(B_n\) is the \(n\)-th Bell number.

For any candidate word, each program enumerates all period-maximal factors with length at least twice their putative period, determines the least periods, and adds the rational exponents without floating-point arithmetic. It then tests **every** pairwise identification of symbols appearing in that word. A candidate is resistant exactly when *every* merged score is strictly smaller. The two embedded, separately implemented checkers agree on the following exact counts:

| Length \(n\) | Tested canonical words with at least three symbols | Resistant |
| ---: | ---: | ---: |
| 3 | 1 | 0 |
| 4 | 7 | 0 |
| 5 | 36 | 0 |
| 6 | 171 | 0 |
| 7 | 813 | 0 |
| 8 | 4,012 | 0 |
| 9 | 20,891 | 0 |
| 10 | 115,463 | 0 |
| 11 | 677,546 | 0 |
| 12 | 4,211,549 | 1 |

The unique length-\(12\) representative is `001101121122`. This is a finite **exhaustive** proof, not an extrapolation: enumeration recurses through all canonical words, examines all letter pairs, and evaluates all possible runs. In the first checker, testing only proper divisors of the candidate period is valid by the Fine–Wilf periodicity theorem, because the candidate interval has length at least twice that period; the other checker instead tests every smaller positive period.

**2. Exact run lists for the infinite family.** Put \(N=10+k\). In the table below, each triple records the inclusive start, inclusive end, and least period. These are *all* the runs, for every \(k\ge2\):

| Word | Complete set of triples \((i,j,p)\) |
| --- | --- |
| \(w_k\) | \((1,2,1),(2,7,3),(3,4,1),(6,7,1),(6,11,3),(9,10,1),(11,N,1)\) |
| \(\pi_{0\leftarrow1}(w_k)\) | \((1,7,1),(6,11,3),(9,10,1),(11,N,1)\) |
| \(\pi_{0\leftarrow2}(w_k)\) | \((1,2,1),(2,11,3),(3,4,1),(6,7,1),(9,10,1),(11,N,1)\) |
| \(\pi_{1\leftarrow2}(w_k)\) | \((1,2,1),(2,7,3),(3,4,1),(6,N,1)\) |

The listed triples are checked exactly for each \(2\le k\le9\) in `verify_family.py`. To justify the infinite extension rather than infer it from finite testing, use the following elementary bound. Suppose all positions after \(T\) in a word contain one symbol \(c\). In a run of least period \(p\ge2\), every full period block contains a symbol different from \(c\): otherwise periodicity would make the whole run constant, contradicting minimality. Because the first two full period blocks contain corresponding non-\(c\) positions separated by \(p\), one obtains \(p\le T-1\). Because the last full block also contains non-\(c\), its right endpoint \(j\) satisfies \(j\le T+p-1\le2T-2\). Thus **every** nonconstant run lies entirely in the prefix through position \(2T-2\).

Here \(T\le10\) in all four words, including each merged image. Hence all runs of least period at least \(2\) end by position \(18\), regardless of \(k\). Once \(k\ge8\), the first \(18\) symbols of **each** of the four word families no longer depend on \(k\); hence their nonconstant runs are the fixed ones listed in the table; their maximality is unchanged by further suffix extension, since any extension past position \(18\) would violate the bound. All remaining runs have period \(1\); the only varying one is the terminal constant run shown as ending at \(N\). The table is therefore valid for every \(k\ge2\).

**3. Exponent sums and strictness.** Summing \((j-i+1)/p\) across the respective complete rows yields \(k+12\), \(k+11\), \(k+34/3\), and \(k+11\). The three possible identifications exhaust the symbol pairs of the ternary word. All their sums are strictly below \(k+12\), because \(34/3<12\). Combined with the exhaustive minimal-length and uniqueness calculation, this proves the theorem. \(\square\)

## Verification

Extract `verify_fast.cpp`, `verify_independent.cpp`, `verify_family.py`, and `verify.py` from the same package into one directory. Run `python3 verify.py` with a C++17 compiler available. It compiles the two independent engines, enumerates all restricted-growth strings using exactly integral scaled exponents for \(3\le n\le12\), checks every merge for strictness, tests the unique witness, and checks the family run lists against direct factor enumeration. Expected outputs include `VERIFY_OK all canonical words with >=3 letters through length 12; unique witness at 12` and `FAMILY_VERIFY_OK`. The family checker additionally tests some longer words, but only the proven uniform-tail bound makes the infinite statement valid.

The exhaustive engines differ in how they enumerate candidate maximal intervals and how they test least periods. Neither engine relies on a precomputed catalog of words or previous verification output. The maximum length audited by exhaustive word enumeration is \(12\); no search completeness is asserted beyond that length, which is unnecessary given the infinite construction.

## Relationship to prior work

Czarkowski (2026) studies the same run-exponent objective and obtains distinct upper bounds for unrestricted and binary alphabets. Its definitions, alphabet-sensitive arguments, and general-alphabet section motivate testing whether identifying letters can supply a monotone reduction to the binary case. The present theorem proves a sharp obstruction to this **local reduction principle**; it does not invalidate the published bounds and does not imply any separation between optimal unrestricted and optimal binary totals. Crochemore et al. (2010) study bounds and morphic binary lower-bound constructions for the same sum, rather than all-pair identification resistance. No exact first-obstruction classification was identified in the checked primary sources and database searches; absence from these searches is not a proof of global novelty.

## Limitations

The uniqueness theorem is conditional on the stated **strict-decrease-under-every-pairwise-identification** predicate, not on being globally extremal for the total exponent sum. The four computed scores refer to the stated family and three one-pair mappings; they do not assert monotonicity for other words or for arbitrary noninjective morphisms. Exhaustive uniqueness is only through length \(12\). Earlier unindexed examples or stronger results, especially in less-accessible morphism literature, cannot be ruled out by database search. The scientific assessment has not received independent external audit.

## References

1. A. Czarkowski, *Improved Bounds on the Sum of Exponents of Runs in a String*, 37th Annual Symposium on Combinatorial Pattern Matching, LIPIcs 369, article 23 (2026). DOI: 10.4230/LIPIcs.CPM.2026.23. Full text: https://drops.dagstuhl.de/storage/00lipics/lipics-vol369-cpm2026/html/LIPIcs.CPM.2026.23/LIPIcs.CPM.2026.23.html.
2. M. Crochemore, M. Kubica, J. Radoszewski, W. Rytter, and T. Waleń, *On the Maximal Sum of Exponents of Runs in a String*, arXiv:1003.4866 (2010), subsequently Journal of Discrete Algorithms 14 (2012), 29–36. Preprint: https://arxiv.org/pdf/1003.4866.
3. N. J. Fine and H. S. Wilf, *Uniqueness Theorems for Periodic Functions*, Proc. Amer. Math. Soc. 16 (1965), 109–114. The period-gcd lemma is used only to accelerate one verifier; the independent verifier tests all shorter periods.
