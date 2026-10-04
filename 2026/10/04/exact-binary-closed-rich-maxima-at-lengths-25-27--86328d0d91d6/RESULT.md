# Exact binary closed-rich maxima at lengths 25–27
## Finding
For a finite binary word \(w\), let \(\operatorname{Cl}(w)\) be the number of distinct closed factors of \(w\), including the empty word. A factor is closed when its length is at most \(1\), or equivalently when its longest nonempty border occurs exactly twice, as prefix and suffix and not internally. Define
\[
C_2(n)=\max\{\operatorname{Cl}(w):w\in\{0,1\}^n\}.
\]
Then
\[
C_2(25)=109,\qquad C_2(26)=117,\qquad C_2(27)=126.
\]
The complete maximizer counts and shortest-period distributions are:

| length \(n\) | \(C_2(n)\) | number of maximizers | shortest periods of maximizers |
| ---: | ---: | ---: | --- |
| \(25\) | \(109\) | \(56\) | \(56\) of period \(8\) |
| \(26\) | \(117\) | \(128\) | \(56\) of period \(8\), \(72\) of period \(9\) |
| \(27\) | \(126\) | \(72\) | \(72\) of period \(9\) |

In particular, every length-\(27\) maximizer is the cube of a primitive binary word of length \(9\). Example maximizers are `0001001100010011000100110`, `00010011000100110001001100`, and `000100111000100111000100111` at lengths \(25\), \(26\), and \(27\), respectively.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\). The empty factor is counted, matching the normalization of the published closed-rich table, where the maximum at length \(1\) is \(2\). A positive integer \(p\le n\) is a period of \(w=w_1\cdots w_n\) when \(w_i=w_{i-p}\) for every \(p<i\le n\); the shortest period is the least such \(p\).

The result determines only the three first lengths beyond the published exact table. It does not assert a closed formula for arbitrary \(n\).

## Proof
The computation is exhaustive over all binary words, and its recurrence gives an exact count rather than an estimate.

Let \(u\) be a binary word and let \(w=ua\) be obtained by appending one letter. Every factor of \(w\) that was not already a factor of \(u\) must end at the last position of \(w\). Therefore every new distinct closed factor is a suffix of \(w\). Conversely, a closed suffix of \(w\) contributes one new distinct closed factor exactly when it has no occurrence ending before the final position. Hence
\[
\operatorname{Cl}(ua)=\operatorname{Cl}(u)+N(ua),
\]
where \(N(ua)\) is the number of suffixes of \(ua\) that are closed and have no earlier occurrence in \(ua\).

The verifier encodes each length-\(n\) binary word by an \(n\)-bit integer. For every possible suffix length it first computes the closed predicate exactly: for lengths at least \(2\), it finds the longest nonempty border and counts all of its occurrences, accepting precisely when that count is \(2\). For each word it then evaluates the recurrence above by checking every suffix and every possible earlier occurrence. Starting from \(\operatorname{Cl}(\varepsilon)=1\), induction on the word length proves that the stored value for every encoded word is exactly its number of distinct closed factors.

At each of lengths \(25\), \(26\), and \(27\), the program scans all \(2^n\) words, so the largest stored value is exactly \(C_2(n)\), and the number of words attaining it is exact. For every maximizer it then tests periods \(p=1,2,\ldots,n\) directly against the defining equalities and records the least valid \(p\). Thus the maximizer counts and period distributions are also exhaustive.

As a regression check on both the normalization and implementation, the same run recomputes the complete published sequence through length \(24\):
\[
2,3,4,6,8,10,12,15,18,21,25,29,33,37,42,48,54,60,66,72,79,86,93,101.
\]
Every value agrees with the table of Parshina and Puzynina before the computation continues to the three new lengths.

## Verification
Compile and run `verify.c` with a standard C11 compiler, for example `cc -O3 -std=c11 verify.c -o verify && ./verify`.

The verifier constructs the closed predicate for every binary word of every length through \(27\), computes \(\operatorname{Cl}(w)\) for every binary word through length \(27\), matches the published maxima through length \(24\), and then checks the three new maxima, exact numbers of maximizers, and complete shortest-period histograms. It terminates with:

`VERIFY_OK source_table_1_24=matched n25=109 count25=56 p25=8:56 n26=117 count26=128 p26=8:56,9:72 n27=126 count27=72 p27=9:72`

A separate direct factor-set calculation on each displayed witness gives \(109\), \(117\), and \(126\) distinct closed factors, respectively. The exhaustive recurrence is what supplies the upper bounds and the complete maximizer classifications.

## Relationship to prior work
Parshina and Puzynina introduced the closed-rich extremal problem in their 2021 conference paper and later proved
\[
C_2(n)\sim \frac{n^2}{6}.
\]
Their expanded paper explicitly asks for the exact formula for the maximum number of closed factors and publishes the binary values only through \(n=24\), ending at \(C_2(24)=101\). The same discussion conjectures that closed-rich words are cubes or have exponent close to \(3\). The present computation begins exactly at the first unlisted length and determines three consecutive new values. Its period census also tests that structural conjecture at those lengths: all length-\(25\) maximizers have period \(8\), the length-\(26\) maximizers have period \(8\) or \(9\), and all length-\(27\) maximizers have period \(9\), hence are exact cubes.

Mieno, Takahashi, Seto, and Horiyama subsequently gave linear or near-linear algorithms for counting distinct closed factors in one given string. Their work describes the extremal result of Parshina and Puzynina as asymptotic and does not provide the missing exact extremal values. A 2026 follow-up by Maity and Puzynina studies closed-rich constants of infinite words rather than extending the finite exact table.

Searches for the exact triples \((25,109)\), \((26,117)\), and \((27,126)\), for notation of the form \(C_2(25)\) or \(\operatorname{Cl}(25)\), and for equivalent “maximum distinct closed factors” formulations did not locate a prior statement of these values or the maximizer-period classification.

## Limitations
This is a finite exhaustive determination at exactly three lengths, not a proof of the still-open general exact formula. The period data classify only maximizers at these lengths and do not establish that every closed-rich word at arbitrary length is a cube or near-cube. Although the most relevant primary and subsequent literature was inspected and targeted searches found no coverage, an unindexed computation, thesis, or unpublished table remains a residual originality risk.

## References
1. O. Parshina and S. Puzynina, “On Closed-Rich Words,” Computer Science – Theory and Applications, CSR 2021, LNCS 12730, 381–394, DOI 10.1007/978-3-030-79416-3_23.
2. O. Parshina and S. Puzynina, “Finite and infinite closed-rich words,” arXiv:2111.00863; Theoretical Computer Science 984 (2024), 114315, DOI 10.1016/j.tcs.2023.114315.
3. T. Mieno, S. Takahashi, K. Seto, and T. Horiyama, “Online and Offline Algorithms for Counting Distinct Closed Factors via Sliding Suffix Trees,” arXiv:2409.19576; SOFSEM 2025, 172–183.
4. A. Maity and S. Puzynina, “Bounds on the closed-rich constant of infinite words,” arXiv:2605.19535, 2026.
