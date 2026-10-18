# Every longest self-reversal common subsequence of a binary five-run word is palindromic

## Finding

Let \(w\) be a nonempty finite binary word, let \(w^{\mathrm R}\) be its reversal, and let \(\mathcal L(w)\) denote **all distinct words of maximum length that are scattered subsequences of both \(w\) and \(w^{\mathrm R}\)**. A *run* is a maximal nonempty block of equal symbols. Then:

**Theorem (sharp run threshold).** If \(w\) has at most five runs, every member of \(\mathcal L(w)\) is a palindrome. The run threshold is sharp: six-run binary words can have nonpalindromic members of \(\mathcal L(w)\). The smallest length where this occurs is seven. Precisely four labeled binary words of length seven exhibit it:
\[
0101001,\qquad 0110101,\qquad 1001010,\qquad 1010110.
\]
These four words form one orbit under reversal and bit complementation. In particular, for any binary input with at most five runs, **every** correct longest-common-subsequence backtracking choice applied to the input and its reversal produces a longest palindromic subsequence, without a special tie-breaking rule.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), with no restriction on the positive run lengths. The property concerns output *words* rather than position alignments: every distinct maximum-length common subsequence must be palindromic. A subsequence need not occupy consecutive positions. Runs are maximal blocks, so adjoining runs have different symbols. We may complement the alphabet to suppose the first run is a zero-run; reversing an input also preserves the property in question. The empty word is excluded from the theorem, though its unique longest common subsequence is trivially empty.

## Proof

Write \(\operatorname{LCS}(u,v)\) for the maximum common subsequence length. For a word with \(h\) runs, every subsequence has at most \(h\) runs. An optimal common subsequence may be classified by its alternating run pattern. It is enough to show that each nonpalindromic common subsequence has a *strictly longer* common subsequence (or, in a run-pattern class, that every length-maximizer has symmetric run lengths). This excludes all nonpalindromic global longest common subsequences.

**One and two input runs.** A constant word has only constant subsequences. If \(w=0^a1^b\) with \(a,b>0\), then \(w^{\mathrm R}=1^b0^a\). No common subsequence can use both symbols, and constant words are palindromes.

**Three input runs.** Put \(w=0^a1^b0^c\) and \(p=\min(a,c)\). A common subsequence with two runs is strictly extendible: append a zero when it has pattern \(0^i1^j\), or prepend a zero when it has pattern \(1^i0^j\). A common subsequence with three runs must have the form \(0^i1^j0^k\), where \(i,k\le p\) and \(j\le b\), with all exponents positive. The unique maximum within this pattern is \(0^p1^b0^p\), which is a palindrome. One-run subsequences are also palindromes.

**Four input runs.** Write \(w=0^a1^b0^c1^d\) and \(w^{\mathrm R}=1^d0^c1^b0^a\). No common subsequence can have four runs: one orientation is impossible in \(w\), and the other is impossible in \(w^{\mathrm R}\). The possible three-run patterns have the following coordinatewise bounds:
\[
0^i1^j0^k:\quad i,k\le \min(a,c),\quad j\le b,
\]
\[
1^i0^j1^k:\quad i,k\le \min(b,d),\quad j\le c.
\]
For each pattern the unique longest word is therefore palindromic. For completeness, a common two-run word \(0^i1^j\) cannot be globally optimal. Its occurrence in \(w^{\mathrm R}\) forces \(i\le c\) and \(j\le b\). If one occurrence in \(w\) takes its ones from the \(b\)-run, a zero may be appended in both inputs. Otherwise an occurrence takes its ones from the final \(d\)-run, giving \(j\le d\); the common palindrome \(1^j0^i1^j\) is strictly longer. For a common word \(1^i0^j\), its occurrence in \(w\) forces \(i\le b\) and \(j\le c\). If one occurrence in \(w^{\mathrm R}\) uses the first zero-run (length \(c\)), a one can be appended in both inputs. Otherwise an occurrence uses the final zero-run (length \(a\)), giving \(j\le a\); the common palindrome \(0^j1^i0^j\) is strictly longer. Thus an optimum cannot have two runs; one-run words are already palindromic.

**Five input runs.** Write
\[
w=0^a1^b0^c1^d0^e,\qquad
w^{\mathrm R}=0^e1^d0^c1^b0^a,
\]
where all five exponents are positive, and put \(p=\min(a,e)\), \(r=\min(b,d)\). A common palindrome always available in both words is
\[
P=0^p1^r0^c1^r0^p,\qquad |P|=2p+2r+c.
\]
Every common subsequence having an even number of runs (two or four) can be extended strictly: a pattern beginning with zero and ending with one admits a final zero in both input words, and a pattern beginning with one and ending with zero admits an initial zero in both. A five-run common subsequence must use all five input runs in both inputs. Consequently, its respective run lengths are independently bounded by \(p,r,c,r,p\); the only length-maximizer among such words is \(P\), a palindrome.

The three-run pattern \(1^i0^j1^k\) necessarily uses the two one-runs and the middle zero-run in each input. It satisfies \(i,k\le r\) and \(j\le c\), so its unique longest word is the palindrome \(1^r0^c1^r\).

It remains to analyze \(0^i1^j0^k\). In \(w\), its one-run is embedded either in the earlier one-run of length \(b\) (case E) or the later one-run of length \(d\) (case L). The same earlier/later choice applies independently in \(w^{\mathrm R}\). In an E embedding of \(w\), \(i\le a\), \(j\le b\), and \(k\le c+e\). In an L embedding of \(w\), \(i\le a+c\), \(j\le d\), and \(k\le e\). For \(w^{\mathrm R}\), exchange \(a\) with \(e\) and \(b\) with \(d\). Taking the intersections for the four possible pairs of embedding choices yields:

* E/E: \(i\le p\), \(j\le r\), \(k\le c+p\). Hence \(i+j+k\le2p+c+r<|P|\).
* L/L: \(i\le c+p\), \(j\le r\), \(k\le p\). Again \(i+j+k<|P|\).
* E/L: \(i,k\le U=\min(a,c+e)\), \(j\le b\). Within this class, all three run lengths can be increased independently up to their bounds. Its unique maximum-length word is the palindrome \(0^U1^b0^U\).
* L/E: \(i,k\le V=\min(e,a+c)\), \(j\le d\). Its unique maximum-length word is the palindrome \(0^V1^d0^V\).

Thus no nonpalindromic three-run word can be globally longest. Together with the one-, even-, and five-run cases, this proves the assertion for all five-run words. Complementing symbols handles words beginning in one. This finishes the infinite run-threshold assertion.

**Sharpness and all shortest witnesses.** For \(w=0101001\), its reversal is \(1001010\). Their maximum common subsequence length is five, and their common subsequences of that length include the nonpalindromes \(00101\) and \(10100\). The preceding theorem proves that any binary counterexample requires at least six runs, hence at least six positions. The only six-run words of length six are the two alternating words; their maximum common subsequences have length five and alternate, hence are palindromes. At length seven, all words with at most five runs are covered by the theorem, and the alternating seven-run words are themselves palindromes. Each remaining six-run word has exactly one doubled run, so up to bit complementation it is obtained by doubling one of the six runs of \(010101\). The exhaustive six-case table below is obtained by the standard common-subsequence recurrence (the accompanying checker independently verifies it by direct enumeration):

| Doubled run index | Binary word starting with zero | Maximum common-subsequence length | Nonpalindromic maximum words? |
| --- | --- | ---: | --- |
| 1 | `0010101` | 5 | No |
| 2 | `0110101` | 5 | Yes |
| 3 | `0100101` | 6 | No |
| 4 | `0101101` | 6 | No |
| 5 | `0101001` | 5 | Yes |
| 6 | `0101011` | 5 | No |

Complementation supplies exactly the four displayed exceptional words, establishing both minimal length and the full length-seven classification. Reversal exchanges the run-index-two and run-index-five representatives and exchanges the other two by complementation, so these four form one symmetry orbit. \(\square\)

## Verification

`CHECKER.py` reconstructs all distinct maximum common subsequence outputs using a three-branch dynamic program, **including the equal-symbol case in which an optimal alignment may skip either equal symbol**. A second implementation computes the entire subsequence sets by bit-mask enumeration and intersects them; the implementations agree for all binary source words of lengths one through nine (1,022 words). The checker also enumerates every binary source word of length one through twelve (8,190 words), confirming the five-run assertion and the exact length-seven exceptions. Finally, it checks all \(4^5=1024\) positive five-run-length tuples with each run length between one and four. The infinite theorem rests on the preceding run-embedding proof; these finite checks are independent tests, not an extrapolated proof.

Run with `python3 CHECKER.py` using standard Python 3; no external dependencies are required. Successful output is `ALL_FIVE_RUN_LCS_CHECKS_PASSED` followed by the checked counts.

## Relationship to prior work

Brodal, Fagerberg, and Rysgaard (ESA 2024) prove that longest-common-subsequence length against reversal equals longest-palindromic-subsequence length; they analyze which backtracking rules return palindromes, and give examples where another valid LCS is nonpalindromic. Their result guarantees at least one palindromic optimum, not that **every** optimum is palindromic. The present result gives a sharp input-structure criterion (at most five binary runs) under which tie-breaking becomes irrelevant, and identifies every shortest binary failure. The same 2024 paper's example on more than two symbols does not contradict the alphabet-restricted run threshold. Chowdhury, Hasan, Iqbal, and Rahman study longest common palindromic subsequences of two arbitrary strings and algorithms that impose the palindrome constraint; they do not establish this unconditional binary run-bound guarantee.

## Limitations

The theorem is restricted to the binary alphabet and a maximum of five runs; six or more runs may or may not have nonpalindromic longest common subsequences. It does not classify every longer counterexample, every optimal alignment, or the number of optimal words in general. The originality assessment rests on examined primary sources and searched research records; it cannot exclude an equivalent unindexed statement. The verification programs check finite instances and are not substitutes for the infinite combinatorial proof. Independent assessment has not been performed.

## References

1. Gerth Stølting Brodal, Rolf Fagerberg, and Casper Moldrup Rysgaard. *On Finding Longest Palindromic Subsequences Using Longest Common Subsequences*. ESA 2024, LIPIcs 308, Article 35. DOI: 10.4230/LIPIcs.ESA.2024.35. Public source date: 2024-09-23. Full open-access paper: https://drops.dagstuhl.de/storage/00lipics/lipics-vol308-esa2024/LIPIcs.ESA.2024.35/LIPIcs.ESA.2024.35.pdf .
2. Shihabur Rahman Chowdhury, Md. Mahbubul Hasan, Sumaiya Iqbal, and M. Sohel Rahman. *Computing a Longest Common Palindromic Subsequence*. arXiv:1110.5296 (2011), https://arxiv.org/html/1110.5296v1 .
