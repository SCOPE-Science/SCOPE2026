# All four minimal unique substrings of every finite period-doubling word

## Finding

For every integer \(m\ge 3\), the finite period-doubling word \(D_m\) of length \(N=2^m\) has **exactly four minimal unique substrings (MUSs)**, and all four have length \(N/4+1\). In zero-based, half-open interval notation their unique occurrences are exactly

\[
[N/4-1,N/2),\quad [3N/8-1,5N/8),\quad
[N/2-1,3N/4),\quad [3N/4-1,N).
\]

In particular the MUS count stays constant at four at every generation \(m\ge3\), while each of their lengths grows linearly.

## Assumptions and scope

Work over \(\{0,1\}\). Define the binary morphism \(\phi(0)=01\), \(\phi(1)=00\), and \(D_0=0\), \(D_{m+1}=\phi(D_m)\). An occurrence is a zero-based half-open interval \([i,j)\). A substring of a finite word is *unique* if it occurs exactly once, and a *minimal unique substring* if it is unique but every proper (nonempty) substring occurs at least twice. Equivalently, for length at least two, its length-one-shorter prefix and suffix both repeat. Counts refer to the finite word, not the infinite fixed point. The alphabet, indexing and minimum generation are part of the statement.

## Proof

**1. Parity recognition.** No \(D_m\) contains \(11\), since every image under \(\phi\) begins with \(0\). In \(\phi(D_m)\), every length-three factor starting at an even index is either \(000\) or \(010\). A length-three factor starting at an odd index must be one of \(001,100,101\): the forbidden alternative \(000\) would require consecutive \(11\) in the source. Hence any factor of length at least three has occurrences starting in **one parity only**. At an even starting index, \(\phi(u)\) has as many occurrences as the corresponding source factor \(u\); at an odd starting index, the sequence of odd-coordinate bits \(1-u_i\), interleaved with zeros, identifies the source factor. The possible trailing zero imposes only that its source occurrence is not terminal.

**2. Terminal-suffix parity lemma.** Every nonempty suffix of \(D_m\) occurs an **odd** number of times in \(D_m\). For \(m=0\) this is immediate. For \(m\ge1\), both letters have odd counts: at \(m=1\) each occurs once; and the number of ones obeys \(\#_1(D_{m+1})=|D_m|-\#_1(D_m)\), which is odd for \(m\ge1\), as is the number of zeros. This proves the suffix-length-one case. A length-two terminal suffix of \(D_{m+1}\) is \(01\) when \(D_m\) ends in \(0\), and has exactly \(\#_0(D_m)\) occurrences; otherwise it is \(00\) and occurs exactly \(2\#_1(D_m)-1\) times, because every source \(1\) supplies an aligned \(00\) and every nonterminal source \(1\) supplies another crossing \(00\). These numbers are odd. For suffix length \(L\ge3\), parity recognition in step 1 maps its occurrences bijectively to occurrences of the suffix of \(D_m\) of length \(\lceil L/2\rceil\): if \(L\) is even, the terminal factor starts even and consists of complete images; if \(L\) is odd, it starts odd and consists of the final bits of those images with intervening zeros. Induct on the generation. In particular, a *terminal* source factor cannot occur exactly twice: if repeated at all, it occurs at least three times.

**3. No short MUSs at the lift level.** The finite word \(D_4=0100010101000100\) has precisely the six distinct length-four factors \(0001,0010,0100,0101,1000,1010\), occurring respectively \(2,2,3,2,2,2\) times. Because \(D_4\) is a prefix of every \(D_m\) for \(m\ge4\), every factor of length at most four of any such word occurs at least twice: each shorter factor can be extended to some length-four occurrence in \(D_4\), and the two occurrences of that length-four factor give two occurrences of the shorter factor. Therefore all MUSs in \(D_m\), \(m\ge4\), have length at least five.

**4. Exact lifting lemma.** For every \(m\ge3\), the entire MUS family satisfies

\[
\operatorname{MUS}(D_{m+1})
=\bigl\{[2i+1,2j):[i,j)\in\operatorname{MUS}(D_m)\bigr\}.
\]

Write \(w=D_m\), \(W=\phi(w)\), and let \(F=W[a:b)\) be any MUS of \(W\), of length at least five by step 3. If \(a\) is even, the length-one-shorter suffix \(F[1:]\) has exactly the same occurrence count as \(F\): both encode the same source factor, including the same possible nonterminal restriction when \(b\) is odd. So \(F\) is not minimal. Suppose \(a\) is odd and \(b\) is odd (thus \(F\) has even length). The full factor encodes a source factor \(u\) followed by a source symbol (a nonterminal occurrence), whereas the prefix \(F[:-1]\) encodes any occurrence of \(u\). If \(F\) is unique and its prefix repeats, \(u\) must occur twice, once nonterminal and once terminal. This contradicts the odd-occurrence terminal-suffix lemma in step 2. Thus \(a\) is odd and \(b\) is even.

Such an \(F=W[2i+1:2j)\) corresponds bijectively, occurrence for occurrence, to \(u=w[i:j)\): \(F\) consists of the last image-bit for \(w_i\), followed by full images of \(w_{i+1},\ldots,w_{j-1}\). Its proper suffix \(F[1:]\) corresponds to all occurrences of the source suffix \(u[1:]\). Its proper prefix \(F[:-1]\) corresponds to nonterminal occurrences of the source prefix \(u[:-1]\). If this source prefix occurs at least twice, there are at least two nonterminal occurrences: otherwise one is terminal and there are exactly two total, contradicting step 2. Consequently the source prefix repeats if and only if the lifted prefix repeats; the same is true for the suffix, without qualification. It follows that \(F\) is MUS in \(W\) **if and only if** \(u\) is MUS in \(w\). This proves the lifting identity, in both directions. Its quantifiers include the terminal occurrences; there is no unjustified assumption of cyclic indexing.

**5. Base case and iteration.** \(D_3=01000101\). Every length-one or length-two factor repeats. The four unique length-three factors are \(100\), \(000\), \(001\), \(101\), at intervals \([1,4)\), \([2,5)\), \([3,6)\), \([5,8)\); the remaining length-three factor \(010\) repeats. Each length-four factor contains one of those four unique length-three factors; hence no longer factor is a MUS. Therefore these are precisely the four MUSs of \(D_3\). Iterate step 4: each interval changes by \([i,j)\mapsto[2i+1,2j)\), whose length changes by \(L\mapsto2L-1\). After \(m-3\) iterations, the four displayed intervals and common length \(2^{m-2}+1=N/4+1\) follow. \(\square\)

## Verification

The accompanying standalone program `check_period_doubling_mus.py` computes the MUSs independently using a suffix-array/LCP calculation in each direction, with no assumed four-interval restriction. It compares with the theorem for every \(3\le m\le12\) (lengths through \(4096\)); for \(3\le m\le7\), it also uses a separate exhaustive substring-frequency enumeration. The checker verifies odd occurrence counts of all terminal suffix lengths for \(3\le m\le8\) and repetitions of all length-four factors for \(m\ge4\). Its exact captured output is `check_period_doubling_mus.out`. These are bounded corroborations, not substitutes for the infinite symbolic proof above.

Run with `python3 check_period_doubling_mus.py` using Python 3 standard library only. The recurrence generates each word afresh from \(D_0\). No external data or compiled dependencies are required.

## Relationship to prior work

Banbara et al. (first posted February 18, 2026, arXiv:2602.16152) characterize all minimum-cardinality *string attractor position sets* of period-doubling words (two choices for each \(m\ge3\)); their Section 4 also establishes the starting-parity recognition used here, but does not state the four-MUS interval classification. The two quantities differ: attractors hit occurrences of *all* factors, whereas a MUS is a distinct irreducibly unique factor with one occurrence. Their Section 3 treats MUSs of Fibonacci words instead. Kishi et al. (May 18, 2026, arXiv:2605.18034) treat occurrence-preserving morphisms and MUSs in Fibonacci and Thue–Morse words; the period-doubling finite-word four-interval theorem is not among their stated applications. Faro et al. (October 7, 2026, arXiv:2610.10950) classify the Thue–Morse family. The lifting in step 4 is a direct specialized argument and does not claim novelty of parity recognition, the definition of MUS, or the general occurrence-preserving paradigm.

## Limitations

The theorem concerns finite prefixes of exactly power-of-two length, not arbitrary finite prefixes or the infinite word's MUSs. An earlier unindexed or differently named characterization remains a priority risk; absence from checked material does not establish global uniqueness. The computational checks are finite. The source-lifting lemma is used only in the period-doubling family with the specified occurrence-parity and terminal-count properties.

## References

1. M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno, Y. Okamoto, *The Smallest String Attractors of Fibonacci and Period-Doubling Words* (original preprint 2026-02-18; later expanded edition), arXiv:2602.16152, https://arxiv.org/abs/2602.16152; CPM 2026, DOI:10.4230/LIPIcs.CPM.2026.33.
2. K. Kishi, P. Guo, C. Urbina, H. Bannai, *On Occurrence-Preserving Morphisms* (2026-05-18), arXiv:2605.18034, https://arxiv.org/abs/2605.18034; CPM 2026, DOI:10.4230/LIPIcs.CPM.2026.24.
3. S. Faro, F. P. Marino, A. Pavone, *Smallest String Attractors and Minimal Coverage Certificates of Thue–Morse Words* (2026-10-07), arXiv:2610.10950, https://arxiv.org/abs/2610.10950.
