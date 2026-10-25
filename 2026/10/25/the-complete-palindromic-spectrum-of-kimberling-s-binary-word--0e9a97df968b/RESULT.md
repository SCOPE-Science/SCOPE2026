# The complete palindromic spectrum of Kimberling's binary word

## Finding

Let \(B=0100101100\cdots\) denote Kimberling's infinite binary word (OEIS A288462). For every integer \(n\ge1\), let \(P_B(n)\) be the number of **distinct** contiguous factors of length \(n\) that equal their reversals. Then

\[
P_B(n)=\begin{cases}
2,&n\in\{1,2,3,4,5,7\},\\
1,&n\in\{6,8,9\},\\
0,&n\ge10.
\end{cases}
\]

In particular, \(B\) has exactly \(15\) distinct nonempty palindromic factors, and its unique longest palindrome is `100101001`, of length \(9\). If \(B[0:N)\) is its prefix of length \(N\), and the palindromic defect of a finite word \(w\) is the difference between \(|w|\) and its number of distinct nonempty palindromic factors, then

\[
\operatorname{Def}(B[0:N))=N-15\qquad(N\ge25).
\]

The threshold \(25\) is optimal: the prefix of length \(24\) has only \(14\) distinct nonempty palindromes.

## Assumptions and scope

All factors and palindromes are **contiguous**; the empty word is excluded from \(P_B\). Let \(T=t_0t_1t_2\cdots\) be the Tribonacci fixed point of the morphism

\[
\varphi(0)=01,\qquad\varphi(1)=02,\qquad\varphi(2)=0.
\]

Define another morphism

\[
\pi(0)=100,\qquad\pi(1)=101,\qquad\pi(2)=10.
\]

Dvořáková, Pelantová, and Shallit prove the representation \(B=0\pi(T)\) (their Theorem 2, expressed using their return-word morphism). This representation, rather than a finite sampled prefix, is the starting point of the proof.

## Proof

**1. A complete alphabet of adjacent Tribonacci letters.** Every image under \(\varphi\) begins in \(0\), and every occurrence of \(1\) or \(2\) in \(T=\varphi(T)\) lies at the end of an image and is immediately followed by \(0\). Consequently the adjacent-letter pairs of \(T\) lie in

\[
S=\{00,01,02,10,20\}.
\]

Conversely, each pair in \(S\) occurs in the explicit prefix \(\varphi^4(0)=0102010010201\). Hence \(S\) is exactly the complete set of adjacent pairs of \(T\).

**2. A six-word finite cover for all short factors.** Since \(T=\varphi^3(T)\), put \(W_a=\pi(\varphi^3(a))\) for \(a\in\{0,1,2\}\). Direct application of the stated morphisms gives

| Letter | \(W_a\) | Length |
|---|---|---:|
| \(0\) | `10010110010100101100` | 20 |
| \(1\) | `10010110010100101` | 17 |
| \(2\) | `10010110010` | 11 |

Therefore

\[
B=0W_{t_0}W_{t_1}W_{t_2}\cdots.
\]

Every block has length at least \(11\). Thus a factor of length at most \(11\) either lies in one block, crosses exactly one boundary between two consecutive blocks, or touches the initial isolated \(0\). All such factors occur in one of the **six explicit words**

\[
0W_0\quad\text{and}\quad W_aW_b\quad(ab\in S).
\]

Indeed, any pair \(ab\in S\) occurs in \(T\), so its concatenated pair of blocks occurs in \(B\); \(0W_0\) is its initial prefix. This proves **equality**, not just inclusion, between the length-at-most-\(11\) factor language of \(B\) and the corresponding factor language of the six finite words.

**3. Exhaustive finite palindrome classification.** Enumerating all length-\(n\) factors in those six words, and retaining precisely those equal to their reversals, gives the following exhaustive table:

| \(n\) | Distinct palindromic factors | \(P_B(n)\) |
|---|---|---:|
| 1 | `0`, `1` | 2 |
| 2 | `00`, `11` | 2 |
| 3 | `010`, `101` | 2 |
| 4 | `0110`, `1001` | 2 |
| 5 | `00100`, `01010` | 2 |
| 6 | `010010` | 1 |
| 7 | `0010100`, `1001001` | 2 |
| 8 | `10100101` | 1 |
| 9 | `100101001` | 1 |
| 10 | none | 0 |
| 11 | none | 0 |

The calculation is finite and exactly reproducible with `verify_cover.py`; its entire input consists of the explicit morphisms and the six explicit words, not any unbounded sampling. The table contains \(15\) entries in all. Every even palindrome of length at least \(12\) has a central palindromic factor of length \(10\), and every odd palindrome of length at least \(13\) has a central palindromic factor of length \(11\). The two empty rows therefore exclude **every** longer palindrome. This proves the asserted complexity function, total, and longest palindrome.

**4. Sharp defect stabilization.** The 25-letter prefix is

`0100101100101001011001001`.

Direct factor enumeration finds all \(15\) palindromes in this prefix; its first 24 letters contain only \(14\). Because the infinite word has no other palindromes, every longer prefix has exactly \(15\) distinct nonempty palindromes. Subtraction from prefix length gives the stated defect formula and the optimal threshold.

## Verification

The standalone Python 3 program `verify_cover.py` regenerates the Tribonacci adjacent-pair set, all three block images, the six finite cover words, the complete table at lengths \(1\) through \(11\), and the sharp prefix threshold. It also checks that the finite cover has exactly \(2n\) distinct length-\(n\) factors for these first eleven lengths. Its exact recorded output is `verify_cover_output.json`.

An independently implemented palindromic tree (`verify_eertree.py`) checks a 100,000-symbol prefix, constructed by two equivalent morphic codings, obtaining \(15\) distinct palindromes, maximal length \(9\), and last new palindrome at prefix length \(25\). Its recorded output is `verify_eertree_output.json`. This second bounded calculation is corroboration; the **infinite** nonexistence statement follows from the exhaustive short-factor cover and the central-palindrome argument, not from searching a long finite prefix.

Run both checkers in Python 3 with `python3 verify_cover.py` and `python3 verify_eertree.py`.

## Relationship to prior work

Dvořáková, Pelantová, and Shallit (arXiv:2510.11318, Theorem 2 and Section 5) provide the exact Tribonacci morphic representation and establish the ordinary factor complexity \(p_B(n)=2n\), together with the critical exponent. They do not state the palindromic spectrum or the sharp defect stabilization found here. Ordinary factor counts do not determine these palindromic counts.

General results about palindromic complexity of **complement-symmetric** Rote sequences do not cover this particular word. The factor `0010` occurs in \(B\), whereas its bitwise complement `1101` does not. Likewise, `1011` occurs but its reversal `1101` does not, so the language of \(B\) is not reversal-closed. Accordingly, the reversal-closed hypotheses in Kim and Kwon's 2026 low-complexity theorem are not met; furthermore, the known ordinary factor complexity \(2n\) exceeds their \(3n/2+1\) bound for sufficiently large \(n\).

## Limitations

The theorem concerns this one fixed binary word, its contiguous palindromes, and the standard palindromic defect of prefixes. It does not classify palindrome spectra for arbitrary morphic images of the Tribonacci word or establish a general principle for all Rote words. The literature comparisons do not exclude unindexed or unpublished equivalent work. An independent scientific review has not been performed.

## References

1. L. Dvořáková, E. Pelantová, and J. Shallit, *On a sequence of Kimberling and its relationship to the Tribonacci word*, arXiv:2510.11318 (first public posting October 13, 2025); *Discrete Mathematics & Theoretical Computer Science* 28:2 (2026), DOI:10.46298/dmtcs.16926.
2. OEIS A288462, *Kimberling's word*: https://oeis.org/A288462.
3. J.-P. Allouche, M. Baake, J. Cassaigne, and D. Damanik, *Palindrome complexity*, arXiv:math/0106121.
4. D. H. Kim and S. Kwon, *On the number of palindromic factors of low complexity words*, arXiv:2609.16596 (September 15, 2026).
