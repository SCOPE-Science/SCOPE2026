# Exact arch-refined census of shortest binary palindrome-universal supersequences through order fifteen

## Finding

For a finite binary host word \(w\), call it *palindrome-\(k\)-universal* if every binary palindrome of length \(k\) appears as a **scattered subsequence** of \(w\). Let \(U_k\) be the number of shortest such indexed host words, and let \(A_{k,j}\) count the hosts whose ordinary (unrestricted) scattered-subsequence universality index is \(j\). The complete exact census for \(1\le k\le15\) is:

| \(k\) | Total \(U_k\) | Nonzero \((j:A_{k,j})\) |
|---:|---:|---|
| 1 | 2 | 1:2 |
| 2 | 6 | 1:2, 2:4 |
| 3 | 14 | 2:6, 3:8 |
| 4 | 40 | 3:24, 4:16 |
| 5 | 94 | 3:2, 4:60, 5:32 |
| 6 | 266 | 4:22, 5:180, 6:64 |
| 7 | 600 | 5:52, 6:420, 7:128 |
| 8 | 1690 | 5:2, 6:316, 7:1116, 8:256 |
| 9 | 3732 | 7:712, 8:2508, 9:512 |
| 10 | 10374 | 7:46, 8:3076, 9:6228, 10:1024 |
| 11 | 22556 | 8:116, 9:6724, 10:13668, 11:2048 |
| 12 | 61826 | 9:1078, 10:24144, 11:32508, 12:4096 |
| 13 | 132640 | 9:2, 10:2338, 11:51920, 12:70188, 13:8192 |
| 14 | 359020 | 10:16, 11:14680, 12:165904, 13:162036, 14:16384 |
| 15 | 760884 | 11:72, 12:29640, 13:352672, 14:345732, 15:32768 |

Thus \(U_{15}=760884\). Of these shortest hosts, exactly \(32768\) are also universal for every binary length-15 pattern, whereas \(728116\) cover all 256 length-15 palindromes without covering all binary length-15 patterns. The minimum unrestricted universality index among the palindrome-universal length-30 hosts is exactly \(11\), attained by exactly 72 hosts.

## Assumptions and scope

The alphabet is labeled \(\{0,1\}\). A scattered subsequence retains increasing host positions, permitting gaps. Palindromes are strings invariant under reversal, counted once as targets regardless of embedding multiplicity. The host word has \(2k\) indexed positions; rotations are NOT identified. The universality index \(\iota(w)\) is the largest integer \(j\) such that every binary word of length \(j\) occurs in \(w\) as a scattered subsequence. This is a complete classification only for integer \(1\le k\le15\).

## Proof

**Minimum length.** Both constant palindromes \(0^k\) and \(1^k\) must embed. Thus a universal host has at least \(k\) zeros and \(k\) ones, and has length at least \(2k\). Conversely, any concatenation of \(k\) two-symbol permutation blocks, each either `01` or `10`, contains every binary target of length \(k\): select each target symbol from the corresponding block. Hence minimum length is precisely \(2k\). All shortest hosts have exactly \(k\) copies of each letter.

**Exact finite decision recurrence.** For each of the \(2^{\lceil k/2\rceil}\) distinct palindromic targets \(p\), maintain \(m_p(u)\), the length of the longest prefix of \(p\) that embeds greedily in a partially generated host \(u\). Initially all coordinates vanish. On appending a letter \(b\), the coordinate increases by one exactly when \(m_p(u)<k\) and the next needed symbol of \(p\) equals \(b\); otherwise it stays. Induction on the host prefix proves the recurrence and the equivalence \(p\) embeds in \(w\) iff \(m_p(w)=k\).

**Exhaustive-search certificate.** Enumerate all balanced hosts through recursive append choices, while tracking the exact greedy coordinates for every target. At a prefix \(u\) with \(R=2k-|u|\) positions remaining, the branch can safely be pruned whenever \(m_p(u)+R<k\) for some \(p\): each remaining letter advances its matcher by at most one. At completed hosts the algorithm accepts iff all coordinates equal \(k\). Every rejected branch has no accepting extension; every accepted balanced host is visited once. The provided C11 program implements precisely this recurrence and checks \(1\le k\le15\). It visits only hosts whose first symbol is zero and doubles each frequency: complementation bijects these hosts with those beginning in one, preserves palindromes as a family, and preserves the universality index.

**Universality-index classification.** Scan a host left to right and close a binary *arch* whenever both letters have appeared since the previous closure. The number of closed arches equals its ordinary scattered-subsequence universality index. For the lower bound, each full arch permits greedy selection of any target symbol; for the upper bound, when an arch closes, its last letter is the first opportunity to select the absent symbol after the preceding closure, so a greedy absent target of length one greater than the arch count exists. The index computed for each accepted host gives the exact displayed classes. At length \(2k\), having index \(k\) forces all \(k\) arches to be of length two, giving exactly \(2^k\) fully universal hosts (one of the two permutation blocks at each arch).

The exhaustive enumeration plus the matcher and pruning invariants establish every entry of the finite table. No extrapolation or unbounded search is used.

## Verification

Compile the standalone file `verify_paluniversal.c` using `cc -std=c11 -O3 -Wall -Wextra -pedantic verify_paluniversal.c -o verify_paluniversal`, then run `./verify_paluniversal K` for every integer `K` from `1` through `15`. Each result prints the full accepting count and index-refined frequencies, including `k=15 ... total=760884 ... iota_11=72 ... iota_15=32768`. An independent Python script `verify_paluniversal_independent.py` performs an **unpruned** census over *all* balanced hosts and explicitly checks every palindrome target for each \(1\le k\le10\); its results agree with the same C11 entries. These are exact finite calculations; no computational sample is treated as evidence beyond its tested domain.

## Relationship to prior work

Mahalingam and Pandoh (2021) study counting scattered palindromes within a given finite word and related extremal counts; that differs from counting shortest host words containing **every** palindrome of a fixed target length. Kosche, Koß, Manea and Siemer (2021) develop absent-subsequence algorithms and the general arch/universality framework for unrestricted binary patterns; their general tools do not directly specify this restricted-language, index-refined length-\(2k\) finite census. The classical fully universal baseline \(2^k\) accounts only for the final column of the table, not for the numerous palindrome-universal hosts that fail full universality. The algorithm is a specialized finite application of standard greedy embedding, not a claim of a new general algorithm.

## Limitations

The novelty and completeness claims are restricted to this exact finite table for \(1\le k\le15\). In particular, no formula for \(U_k\) at arbitrary \(k\), no asymptotic expansion, and no global optimization theorem for larger hosts is proved. Generic enumeration algorithms could reproduce the data in principle; an unindexed equivalent finite table or a general published theorem implying its entries remains an originality risk. The independently implemented unpruned verifier reaches only \(k=10\); the exact \(k=11\) through \(k=15\) values rely on the stated sound exhaustive C11 recurrence, not on an independent second complete enumeration.

## References

1. V. Mahalingam and D. Pandoh, *Counting Scattered Palindromes in a Finite Word*, first public version August 5, 2021, arXiv:2108.02729.
2. M. Kosche, T. Koß, F. Manea and S. Siemer, *Absent Subsequences in Words*, first public version August 31, 2021, arXiv:2108.13968.
