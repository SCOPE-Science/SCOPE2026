# The complete circular-palindrome spectrum of finite Zimin words

## Finding

Let \(Z_0=\varepsilon\) and \(Z_n=Z_{n-1}a_nZ_{n-1}\), with pairwise distinct symbols \(a_1,\ldots,a_n\). For each \(n\ge 1\), write \(N=2^n-1\). A circular factor of length \(1\le\ell\le N\) is a contiguous length-\(\ell\) factor of the periodic repetition of \(Z_n\). A palindrome is a word equal to its reversal. Count distinct words, not occurrences.

**Theorem.** All nonempty circular palindromes of \(Z_n\) are precisely the following disjoint families:

1. The odd palindromes \(u_ta_ru_t^R\), for \(1\le r\le n\), \(0\le t<2^{r-1}\), where \(u_0=\varepsilon\), and for positive \(t\), \[u_t=a_{1+\nu_2(t)}a_{1+\nu_2(t-1)}\cdots a_{1+\nu_2(1)}.\]
2. The even palindromes \(\operatorname{suf}_t(Z_n)\operatorname{pre}_t(Z_n)\), for \(1\le t\le 2^{n-1}-1\), where \(\operatorname{suf}_t\) and \(\operatorname{pre}_t\) take the last and first \(t\) symbols.

Here \(\nu_2(d)\) is the exponent of two dividing the positive integer \(d\), and \(u^R\) denotes the reversal of \(u\). At each even length \(2t\le N\) there is **exactly one** circular palindrome. At each odd length \(2t+1\le N\), there are **exactly**
\[n-\lceil\log_2(t+1)\rceil.\]
Every odd circular palindrome is already an ordinary (nonwrapping) factor of \(Z_n\). All additional circular palindromes have even length. The total number of distinct nonempty circular palindromes is exactly
\[\boxed{3\cdot2^{n-1}-2=\frac{3N-1}{2}}.\]

## Assumptions and scope

All ranks \(n\) are positive integers, and the alphabet symbols are pairwise distinct and distinguished by rank. Circular factors have length at most \(N\); longer palindromes in the infinite periodic continuation are **not counted**. Words are distinguished by actual letter sequence, not by reversal class or conjugacy. The proof uses no alphabet ordering. The empty word is omitted from the count.

## Proof

**Ruler identity.** For the one-based position \(j\) in \(Z_n\), where \(1\le j\le 2^n-1\), the letter is
\[Z_n[j]=a_{1+\nu_2(j)}.\]
This follows by induction, since the unique middle position \(j=2^{n-1}\) has rank \(n\), while the left and right copies of \(Z_{n-1}\) have the same valuations at corresponding positions: for \(0<d<2^{n-1}\), \(\nu_2(2^{n-1}+d)=\nu_2(d)\).

**Odd centers.** Take a center at position \(j=2^{r-1}(2q+1)\). Its symbol is \(a_r\). For every offset \(1\le d<2^{r-1}\), the positions \(j-d\) and \(j+d\) lie inside the linear word, and both have two-adic valuation \(\nu_2(d)\). Thus the radius-\(t\) palindrome around this center is exactly \(u_ta_ru_t^R\) for every \(0\le t<2^{r-1}\). These palindromes occur linearly, for example at the first rank-\(r\) center \(j=2^{r-1}\).

For \(r<n\), the first possible additional offset is \(d=2^{r-1}\). If both positions lie inside the word, they are \(2^rq\) and \(2^r(q+1)\), respectively; since consecutive integers have different two-adic valuations, these letters differ. If one side meets the circular seam, it becomes an endpoint with symbol \(a_1\), whereas the other side is an interior multiple of \(2^r\) and has symbol of rank at least \(r+1\); these also differ. Hence no odd-centered circular palindrome can extend to radius \(2^{r-1}\) when \(r<n\). For \(r=n\), the maximum allowed radius at word length \(N\) is \((N-1)/2=2^{n-1}-1\), exactly the asserted bound. This proves the complete odd family. A palindrome of odd length has a unique middle letter, so different ranks cannot coincide; at each fixed rank, different radii have different lengths. There are \(\sum_{r=1}^{n}2^{r-1}=N\) distinct odd palindromes.

**Even centers.** For \(n\ge2\), every odd position of \(Z_n\) contains \(a_1\), and every even position contains a different symbol. Therefore no two internally adjacent letters are equal. The two letters adjacent across the circular seam, however, are both \(a_1\), because the word begins and ends in \(a_1\). An even palindrome necessarily has equal middle adjacent letters. Thus every nonempty even palindrome must be centered on this one seam. By the recursion, \(Z_n\) is a palindrome, so \(\operatorname{suf}_t(Z_n)=\bigl(\operatorname{pre}_t(Z_n)\bigr)^R\); its seam-centered word \(\operatorname{suf}_t(Z_n)\operatorname{pre}_t(Z_n)\) is consequently a palindrome. The allowed radii are precisely \(1\le t\le\lfloor N/2\rfloor=2^{n-1}-1\). For \(n=1\), no even length lies in the permitted range. Different radii give different lengths. There are exactly \(2^{n-1}-1\) distinct even palindromes.

**Length spectrum and total.** At odd length \(2t+1\), a rank \(r\) is admissible if and only if \(t<2^{r-1}\), which occurs for exactly \(n-\lceil\log_2(t+1)\rceil\) values of \(r\). Every permitted even length contains the unique seam-centered palindrome. Summing odd and even contributions yields \(N+(N-1)/2=(3N-1)/2\). This completes the proof.

## Verification

The standalone `checker.py` generates \(Z_n\), exhaustively enumerates every length-at-most-\(N\) circular factor, tests palindromicity, constructs the claimed explicit language, and compares sets and lengthwise multiplicities. Ranks \(1\) through \(8\) passed with respective circular-palindrome counts \(1,4,10,22,46,94,190,382\). It also checked that all odd circular palindromes occur linearly. This is finite consistency testing, **not** a replacement for the all-rank proof.

Run with `python3 checker.py`; no third-party packages are needed.

## Relationship to prior work

The ruler description and algorithms for Zimin-word factors occur in Głowinski–Rytter (2013). Glen–Justin–Widmer–Zamboni (2008) develop structural theory of rich words and the palindromic properties relevant to powers and conjugates. Simpson (2014) proves a general strict upper bound of \(5N/3\) for distinct nonempty palindromes of length at most \(N\) in a circular word of length \(N\), along with nearly sharp constructions. The present theorem is an explicit, letter-by-letter and length-by-length classification for the particular Zimin family; it does not assert a new general upper bound or a new maximality principle. The numerical count alone is not offered as a novel integer sequence. A complete-material comparison with Simpson (2014) was unavailable, so priority remains subject to that source's full-text inspection and other specialist literature.

## Limitations

The result does not address arbitrary partial Zimin prefixes, identifying different alphabet symbols under morphisms, circular factors longer than one revolution, or unconstrained circular words. The original claim and its consequences are proved only for literal finite \(Z_n\). Full-text comparison with Simpson (2014) and independent mathematical assessment remain outstanding.

## References

1. A. Glen, J. Justin, S. Widmer, and L. Q. Zamboni, *Palindromic Richness*, 2008, arXiv:0801.1656, https://arxiv.org/abs/0801.1656 (first public 2008-01-10).
2. R. Głowinski and W. Rytter, *Compressed Pattern-Matching with Ranked Variables in Zimin Words*, 2013, arXiv:1307.1560, https://arxiv.org/abs/1307.1560 (first public 2013-07-05).
3. J. Simpson, *Palindromes in circular words*, Theoretical Computer Science 550 (2014), 66–78, https://doi.org/10.1016/j.tcs.2014.07.012 (abstract and public bibliographic material examined; full text not obtained).
