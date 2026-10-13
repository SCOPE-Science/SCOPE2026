# Sharp onset of superlinear ambiguity for binary three-subsequence decks

## Finding

For a binary word \(w=w_1\cdots w_n\), let \(D_3(w)\) be the eight-entry vector indexed by \(abc\in\{0,1\}^3\), whose \(abc\) entry is the number of strictly increasing triples \(1\le i<j<k\le n\) with \((w_i,w_j,w_k)=(a,b,c)\). For every \(n\ge3\), define the worst-case inverse-list size
\[
L_3(n)=\max_{w\in\{0,1\}^n}\left|\{v\in\{0,1\}^n:D_3(v)=D_3(w)\}\right|.
\]

**Theorem (finite, sharp).** The complete sequence for \(3\le n\le16\) is
\[
(L_3(3),\ldots,L_3(16))=(1,1,1,1,2,2,3,3,4,4,6,10,14,20).
\]
In particular, \(n=16\) is the smallest valid blocklength \(n\ge3\) for which \(L_3(n)>n\). At length \(16\), there are exactly two maximum fibers, each containing \(20\) words. In lexicographic pattern order \((000,001,010,011,100,101,110,111)\), their spectra are exactly
\[
(56,85,82,85,57,82,57,56),\qquad
(56,57,82,57,85,82,85,56).
\]
They are exchanged by complementing all symbols, or by reversing the word: these operations respectively send a triple pattern \(abc\) to \((1-a)(1-b)(1-c)\), or to \(cba\).

The complete length-\(16\) fiber-size histogram, given as \((\text{fiber size}:\text{number of different decks})\), is
\[
1:22448,\;2:7331,\;3:2952,\;4:2081,\;5:746,\;6:624,\;7:246,\;8:83,\;9:66,\;10:44,\;11:14,\;12:4,\;13:2,\;14:6,\;20:2.
\]
Thus there are exactly \(36649\) attainable decks and \(65536\) binary words at length \(16\).

## Assumptions and scope

The alphabet is literally \(\{0,1\}\), words are position-labeled, and each *scattered* subsequence occurrence is counted with its multiplicity. The triple index positions need not be adjacent. Decks are not normalized, cyclic, or quotiented by reversal/complement. The range \(n\ge3\) is essential: below length three every triple deck is empty, so the statistic is degenerate. This is an exact finite claim for \(3\le n\le16\), not a formula or asymptotic bound for all lengths.

For fixed \(n\ge3\), the length-three deck also determines counts of all scattered subsequences of length one and two. Indeed, for any pattern \(a\) of length \(s=1\) or \(2\), count pairs consisting of an occurrence of \(a\) and an extension by \(3-s\) additional positions. Each occurrence extends in exactly \(\binom{n-s}{3-s}\) ways; alternatively sum over all length-three patterns weighted by how many scattered occurrences of \(a\) each contains. As that binomial factor is nonzero, equal three-decks imply equal counts at all smaller positive lengths. The fibers are therefore precisely the length-\(n\) binary \(3\)-binomial equivalence classes.

## Proof

We give an exact exhaustive *finite* certificate with two independently structured implementations. Both enumerate every word, rather than sampling. Their loops and output conditions can be audited using the packaged programs `verify_dp.py` and `verify_direct.py`.

**Counting recurrence.** Scan a word from left to right. Maintain \(A_b\), the number of occurrences of the one-bit pattern \(b\); \(B_{ab}\), the number of occurrences of the two-bit scattered pattern \(ab\); and \(C_{abc}\), the three-bit counts already formed. Appending symbol \(t\) changes these in descending length order by
\[
C_{abt}\leftarrow C_{abt}+B_{ab},\quad
B_{at}\leftarrow B_{at}+A_a,\quad
A_t\leftarrow A_t+1.
\]
All other entries remain unchanged. Every scattered triple either precedes the appended symbol or ends at it, where the first two indices form a unique old pair, proving the recurrence by induction. All arrays start at zero. Therefore the final \(C\) equals \(D_3(w)\) exactly.

**Exhaustive coverage.** For each integer \(n=3,4,\ldots,16\), `verify_dp.py` iterates integers \(0\le z<2^n\), interprets each in exactly \(n\) binary digits with leading zeroes, applies the above recurrence and increments a dictionary count for its eight-entry deck. Binary representation is a bijection from those integers to all binary words of length \(n\), so every word is included once and only once. The dictionary value at a deck is exactly the fiber cardinality; taking its maximum proves the reported \(L_3(n)\), and tabulating the dictionary values proves the histogram and the two maximizing spectra. All computations use exact integers, with no tolerance or solver.

**Independent count.** `verify_direct.py` does not use the recurrence. For every \(n\) and every word, it visits every triple from `combinations(range(n),3)` and directly increments the entry \(4w_i+2w_j+w_k\). A fixed word has exactly \(\binom n3\) such triples, so this is exactly the defining vector. The second, independently computed dictionary yields the same maxima for \(3\le n\le16\), the complete histogram for \(n=16\), and the same two extremal vectors. This cross-check eliminates reliance on the recurrence as an unchecked implementation shortcut.

The numerical entries of the claimed vector and histogram are finite integers certified by the exhaustive source loops and asserted against explicit constants in **both** independent programs. Their correctness is independently inspectable by checking that the loops cover their stated finite ranges and implement the definitions. The maximum for \(n=16\) is \(20>16\); for \(3\le n\le15\), the listed maxima are at most \(n\). This proves the sharp onset statement.

## Verification

Execute, using Python 3 with only its standard library, `python3 verify_dp.py` and `python3 verify_direct.py`. Both must terminate with respectively `VERIFY_DP_OK` and `VERIFY_DIRECT_OK`. The full classes and histograms are additionally available from `class_statistics.csv` and `maximal_fibers.txt`. As arithmetic checks, the length-\(16\) histograms satisfy
\[
\sum_s H_{16}(s)=36649,\qquad \sum_s sH_{16}(s)=65536.
\]
All comparisons use exact integer equality. The independently enumerated totals agree with the published number \(D_3(16)=36649\), but that published distinct-deck count alone is insufficient to determine fiber cardinalities.

## Relationship to prior work

Rigo and Salimov introduced the binomial-equivalence framework and studied class-count growth for arbitrary words and special infinite words. Freydenberger and collaborators analyzed algorithms for testing \(k\)-binomial equivalence. Chrisnata, Kiah, Rao, Vardy, Yaakobi and Yao determined numbers \(D_k(n)\) of distinct \(k\)-decks for a range of parameters; their table includes \(D_3(16)=36649\). These results count *different decks*, not the distribution of preimage cardinalities; their reported results do not provide the maximum twenty or the two maximizing decks. Lejeune, Rigo and Rosenfeld studied individual binomial-equivalence classes, chiefly giving an algorithm for **two**-binomial classes and results about larger alphabets, rather than this binary three-binomial fiber histogram. The exact comparison has been made against the cited available full texts, not merely titles.

## Limitations

The result proves a finite threshold in the nondegenerate domain \(3\le n\le16\); it does not give \(L_3(n)\) for \(n\ge17\) or say that the maximum increases monotonically thereafter. Independent formal verification was not performed. Completeness depends on the mathematical correctness of the two short exact enumeration programs and the execution environment, rather than a closed-form symbolic classification of all words. Historical or unindexed prior enumerations could contain the same finite histogram.

## References

1. M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words* (2013). Author's preprint: https://orbi.uliege.be/bitstream/2268/149313/1/binomial_final_short.pdf ; institutional record (available since 2013-05-27): https://orbi.uliege.be/handle/2268/149313 .
2. D. D. Freydenberger et al., *Testing k-binomial equivalence*, arXiv:1509.00622 (2015-09-02 first submission), https://arxiv.org/abs/1509.00622 .
3. J. Chrisnata, H. M. Kiah, S. R. Karingula, A. Vardy, E. Yaakobi and H. Yao, *On the Number of Distinct k-Decks: Enumeration and Bounds*, ISCIT 2019, author's PDF: https://yaakobi.net.technion.ac.il/files/2020/07/105_K_Deck_ISCIT19.pdf ; extended journal version, DOI 10.3934/amc.2021032.
4. M. Lejeune, M. Rigo and M. Rosenfeld, *On the Binomial Equivalence Classes of Finite Words*, author preprint: https://www.lirmm.fr/~mrosenfeld/LejeuneRigoRosenfeld.pdf (2020).
