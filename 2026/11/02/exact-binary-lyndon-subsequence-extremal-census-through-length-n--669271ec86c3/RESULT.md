# Exact binary Lyndon-subsequence extremal census through length nineteen

## Finding

For each binary word \(w\), let \(\mathcal L(w)\) be the set of **distinct** nonempty Lyndon words occurring as scattered subsequences of \(w\), where \(0<1\). A Lyndon word is strictly lexicographically smaller than each of its nontrivial cyclic rotations. For every host length \(1\le n\le19\), we determine both the exact maximum \(M_n=\max_{w\in\{0,1\}^n}|\mathcal L(w)|\) and the number \(A_n\) of ordered binary hosts attaining it. The complete, finite exact answer is:

| \(n\) | \(M_n\) | \(A_n\) | Lexicographically first maximizer |
|---:|---:|---:|:---|
| 1 | 1 | 2 | `0` |
| 2 | 3 | 1 | `01` |
| 3 | 4 | 2 | `001` |
| 4 | 6 | 1 | `0011` |
| 5 | 8 | 4 | `00011` |
| 6 | 13 | 1 | `001011` |
| 7 | 18 | 2 | `0001011` |
| 8 | 28 | 1 | `00101011` |
| 9 | 41 | 1 | `000101011` |
| 10 | 63 | 1 | `0010101011` |
| 11 | 96 | 1 | `00010101011` |
| 12 | 141 | 2 | `000101011011` |
| 13 | 225 | 1 | `0001010101011` |
| 14 | 335 | 1 | `00010101011011` |
| 15 | 538 | 1 | `000101010101011` |
| 16 | 803 | 1 | `0001010101101011` |
| 17 | 1292 | 1 | `00010101010101011` |
| 18 | 1941 | 1 | `000101010101101011` |
| 19 | 3132 | 1 | `0001010101010101011` |

At length twelve the *two* maximizing hosts are exactly `000101011011` and `001010101011`. In particular, an alternating host is not generally extremal, while a simple-looking double-ended alternating candidate ceases to be the unique optimum by length twelve. The table concerns **subsequences**, not the previously studied distinct *contiguous* Lyndon factors, and counts strings without multiplicity of their embeddings. No infinite closed form for \(M_n\) is asserted.

## Assumptions and scope

The alphabet is the fixed ordered pair \(\{0,1\}\). A scattered subsequence preserves position order but may omit intervening positions. A nonempty one-letter string is Lyndon. The maximization ranges exhaustively over **all** \(2^n\) binary hosts for each \(n\le19\); different hosts are distinct even if reverses or complements happen to have equal scores. The indices and list of witnesses are an exact finite theorem, not extrapolation. The source literature explicitly distinguishes total occurrences, expected distinct counts, and maximum distinct counts.

## Proof

We supply an exhaustive finite proof with a short, transparent state invariant implemented in the standalone C11 source `verification/census.c`.

**1. Encoding.** Encode a binary string \(s=s_1\cdots s_k\) by the integer whose binary expansion is \(1s_1\cdots s_k\); encode the empty word by \(1\). This is an injection into integers \(1\) through \(2^{n+1}-1\) for words of length at most \(n\). Appending a letter \(b\in\{0,1\}\) transforms code \(x\) into \(2x+b\).

**2. Exhaustive subsequence recurrence.** If \(S(v)\) denotes the encoded set of all distinct scattered subsequences of host \(v\), including the empty word, then
\[
S(vb)=S(v)\cup\{2x+b:x\in S(v)\}.
\]
This is exact: every subsequence of \(vb\) either omits its last position or uses that position as its final selected letter. The two alternatives may represent the same string, so the union is a set. Starting from \(S(\epsilon)=\{1\}\), the `census.c` verifier implements the recurrence with an append-only list, a snapshot of the pre-letter list length, and a tagged membership array. Tags distinguish runs for different host words. Hence, after processing a particular host, every distinct scattered subsequence appears exactly once in the list, and no other encoded string appears.

**3. Independent Lyndon predicate.** Before enumerating hosts, the program computes `isly[code]` for every nonempty string with length at most the chosen cutoff. For length one it is true. For longer length \(k\), the code checks every nonidentity cyclic rotation, requiring the original \(k\)-bit string to be lexicographically smaller; fixed-length lexicographic order equals the numerical order on these \(k\)-bit integers. An early necessary filter requiring first letter \(0\) and last letter \(1\) is valid for all nonconstant binary Lyndon words. Thus `isly` agrees with the definition without relying on an unverified string-pattern database.

**4. Complete maximization.** For each \(n=1,\ldots,19\) an outer loop enumerates the integers \(0,1,\ldots,2^n-1\), representing every possible \(n\)-letter host in fixed-width binary, with no omissions or symmetry quotient. Applying Step 2 to each host and summing `isly[code]` over its newly inserted distinct nonempty subsequences yields exactly \(|\mathcal L(w)|\). The loop records the largest value, the number of ties, and the first maximizing host. This proves all entries of the displayed table, conditional only on exact integer execution of the supplied straight-line loops. Maximum arithmetic stays below the available integer widths: there are at most \(2^{20}-1\) coded nonempty binary patterns at cutoff nineteen, and fewer than \(2^{20}\) host visits summed over all lengths. All allocation sizes and bit shifts are explicitly bounded. In fact the program uses 32-bit unsigned indices and 64-bit sums.

**5. Independent reconstruction.** A separate Python 3 verifier `verification/crosscheck.py` uses Python integer sets, Python string rotations, and a completely different per-host enumeration of subsequence codes. It independently recomputes all maxima, maximizing-word counts, first maximizers and total scores through \(n=16\), and it asserts agreement with the C census for these overlapping lengths. This crosscheck does not by itself prove the last three lengths, whose exhaustive verification is accomplished by the C enumeration of Step 4.

## Verification

To reproduce the complete census, compile and run from the package root using `cc -O3 -std=c11 -Wall -Wextra verification/census.c -o census` followed by `./census 19`. All tables in the result are emitted as checkable lines. To independently compare the overlapping finite range, run `python3 verification/crosscheck.py`. Both complete without network access and have no external software dependencies beyond a C11 compiler and Python 3. The loops cover \(\sum_{n=1}^{19}2^n=1,048,574\) host evaluations; the final length alone contains \(524,288\) hosts. Finite exhaustive computation proves precisely the finite statement, and does not imply a formula or an optimum for \(n\ge20\).

## Relationship to prior work

Hirakawa, Nakashima, Inenaga and Takeda (2021) distinguish the maximum number of all (position-counted) Lyndon subsequences, the expected total, and the expected number of *distinct* Lyndon subsequences; their distinct-maximum problem is not resolved by the total-maximum formula. Bannai, I, Kociumaka, Köppl and Puglisi (2022/2023) study algorithms for longest Lyndon subsequences, not the full count of distinct patterns in a host. Glen, Simpson and Smyth (2017) determine maxima for distinct **contiguous** Lyndon factors, a different statistic: their binary OEIS A290743 values differ from those here. These distinctions, source comparisons, and the absence of matching published or research-database tables for this exact finite statistic motivate the finite computation; the absence of a search hit alone cannot certify novelty.

## Limitations

This is a complete *finite* enumeration only through length nineteen. The proof is algorithmic and relies on exact, replayable finite execution, not an infinite combinatorial classification. The unproved general maximization problem remains open here. An unindexed or inaccessible published finite table could subsume these values. The numerical census and available source comparisons have not undergone an independent scientific audit.

## References

1. R. Hirakawa, Y. Nakashima, S. Inenaga, M. Takeda, *Counting Lyndon Subsequences*, arXiv:2106.01190, first public June 2, 2021; https://arxiv.org/abs/2106.01190 .
2. H. Bannai, T. I, T. Kociumaka, D. Köppl, S. J. Puglisi, *Computing Longest Lyndon Subsequences and Longest Common Lyndon Subsequences*, first arXiv January 18, 2022; open-access *Algorithmica*, May 6, 2023; https://link.springer.com/article/10.1007/s00453-023-01125-z .
3. A. Glen, J. Simpson, W. F. Smyth, *Counting Lyndon Factors*, *Electronic Journal of Combinatorics* 24(3), 2017, P3.28; https://oeis.org/A290743 (binary factor maximum; different invariant).
