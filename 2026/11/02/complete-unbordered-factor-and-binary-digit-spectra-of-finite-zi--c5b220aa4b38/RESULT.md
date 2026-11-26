# Complete unbordered-factor and binary-digit spectra of finite Zimin words

## Finding
For each integer \(n\ge1\), define the finite literal Zimin word \(Z_0=\varepsilon\) and \(Z_n=Z_{n-1}a_nZ_{n-1}\), where the letters \(a_1,a_2,\ldots\) are pairwise distinct. A nonempty word is **unbordered** if no nonempty proper prefix is also a suffix. Let \(U_n(\ell)\) count distinct unbordered contiguous factors of \(Z_n\) of length \(\ell\), and let \(s_2(q)\) count the one-bits of the nonnegative integer \(q\).

For each \(1\le r\le n\), the **unbordered factors** whose greatest-index letter is \(a_r\) are exactly
\[
\left\{\operatorname{suf}_i(Z_{r-1})\,a_r\,\operatorname{pre}_j(Z_{r-1}):\quad 0\le i,j<2^{r-1},\quad i\mathbin{\&}j=0\right\}.
\]
Here \(\operatorname{suf}_i\) and \(\operatorname{pre}_j\) are suffix and prefix of the stated lengths, including the empty word at length zero; \(\mathbin{\&}\) is bitwise AND. The descriptions are unique. The unrestricted family of all factors with greatest letter \(a_r\) allows every pair of lengths in range, including pairs that share one-bits.

The complete length spectrum is
\[
U_n(\ell)=\begin{cases}
(n-\lceil\log_2\ell\rceil)\,2^{s_2(\ell-1)},&1\le\ell\le2^{n-1},\\
0,&\ell>2^{n-1}.
\end{cases}
\]
The longest unbordered factors have length \(2^{n-1}\), and there are \(2^{n-1}\) of them. The total over all lengths is \((3^n-1)/2\). For fixed greatest letter \(a_r\), the length-generating polynomial is \(x\prod_{t=0}^{r-2}(1+2x^{2^t})\), with the empty product equal to one.

## Assumptions and scope
Factors are contiguous substrings with literal letter equality. A factor occurring at several positions is counted once. The result does not refer to occurrences under substitutions of a Zimin pattern, scattered subsequences, or words obtained by merging letters of the Zimin alphabet.

## Proof
**Marker lemma.** In a word \(XcY\) where \(c\) occurs only once, a common prefix and suffix containing \(c\) would align their two occurrences at \(c\), so the prefix and suffix would have to be the whole word. Thus a proper border exists exactly when a prefix of \(X\) equals a suffix of \(Y\) at some length between one and \(\min(|X|,|Y|)\).

**Binary criterion.** For \(m\ge0\), take a marker \(c\) not in \(Z_m\). Write \(W_m(i,j)=\operatorname{suf}_i(Z_m)c\operatorname{pre}_j(Z_m)\) for \(0\le i,j<2^m\). We show by induction that it is unbordered exactly when \(i\mathbin{\&}j=0\). At \(m=0\) the only word is \(c\), which is unbordered. For \(m\ge1\), put \(h=2^{m-1}\) and write \(i=\alpha h+i'\), \(j=\beta h+j'\) with \(i',j'<h\) and \(\alpha,\beta\in\{0,1\}\).

- If \(\alpha=\beta=0\), the two sides of the marker lie in copies of \(Z_{m-1}\); apply the induction hypothesis to \(W_{m-1}(i',j')\).
- If \(\alpha=1,\beta=0\), the left side starts with \(\operatorname{suf}_{i'}(Z_{m-1})a_m\), while the right side has no \(a_m\). The marker lemma restricts any border to length at most \(i'\) and \(j'\), and all border tests in that range are exactly those for \(W_{m-1}(i',j')\). The case \(\alpha=0,\beta=1\) is symmetric.
- If \(\alpha=\beta=1\), the word \(\operatorname{suf}_{i'}(Z_{m-1})a_m\operatorname{pre}_{j'}(Z_{m-1})\) is both a prefix and a suffix. It is proper because neither copy includes the central \(c\), and nonempty because it contains \(a_m\).

Thus sharing the high bit forces a border, and otherwise the lower bits decide, proving the criterion.

**Factor classification and counting.** If a factor of \(Z_n\) has greatest-index letter \(a_r\), it avoids every \(a_s\) with \(s>r\). Repeatedly restricting to one copy of the lower-rank Zimin word shows that it occurs in \(Z_r\). In \(Z_r\) it crosses the unique \(a_r\), so it is a suffix and prefix around that marker, with \(i,j<2^{r-1}\). These positions determine the word and are determined by the unique position of \(a_r\) within the word and the word's length. Conversely every such pair gives a factor of \(Z_r\), hence of \(Z_n\). Ranks give disjoint families, and the criterion with \(m=r-1\) selects exactly the unbordered members.

When \(i\mathbin{\&}j=0\), the sum \(i+j\) has no carries. For fixed \(\ell=1+i+j\le2^{r-1}\), each one-bit of \(\ell-1\) can independently be assigned to either \(i\) or \(j\), giving \(2^{s_2(\ell-1)}\) words at rank \(r\). There are \(n-\lceil\log_2\ell\rceil\) possible ranks for \(1\le\ell\le2^{n-1}\) and none beyond that. At length \(2^{n-1}\), only rank \(n\) contributes, and \(2^{n-1}-1\) has \(n-1\) one-bits. For fixed \(r\), bit \(t\) contributes one choice if unused and two choices if used, in the latter case adding \(2^t\) to the length. This gives the generating product and total \(3^{r-1}\) at rank \(r\); summing over \(r\) gives \((3^n-1)/2\).

## Verification
The accompanying `checker.py` can be run with Python 3.10 or newer. It extracts literal substrings and tests proper borders, compares the resulting set and length counts with the templates for ranks 1–8, and checks the marker predicate on every length pair for marker ranks 0–7. These are finite checks; the induction proves the arbitrary-rank result.

## Relationship to prior work
Wojcik [1, slides 6–9] describes the infinite literal Zimin word by 2-adic valuations and parametrizes **all** its factors by two subsets around their unique greatest letter. The block lengths are powers of two, so this is equivalent to the unrestricted suffix–marker–prefix parametrization used here. Głowinski and Rytter [2, §2] give a compressed factor representation and membership criterion. Neither unrestricted parametrization is claimed as new. The assertion here is the border filter on that family and the resulting length spectrum.

The closed-factor spectrum [3] treats factors having a proper border with exactly two occurrences (and single letters). An example with a border but not closed is \(a_1a_3a_1a_2a_1a_4a_1\) in \(Z_4\): its only proper border is \(a_1\), which occurs four times. Thus counts for closed factors cannot simply be subtracted from all-factor counts to obtain the present spectrum. The related period-doubling sequence in Goc, Mousavi and Shallit [4, §5] uses a fixed binary coding of valuations and gives a different unbordered-factor count. Historical priority for the border filter and spectrum is not certified.

## References
1. C. Wojcik, *The Zimin word and words with a Lyndon orbit*, CIRM slides, March 2019, https://www.cirm-math.fr/RepOrga/1991/Slides/Wojcik-Lyndon-CIRM.pdf.
2. R. Głowinski and W. Rytter, *Compressed Pattern-Matching with Ranked Variables in Zimin Words*, https://arxiv.org/abs/1307.1560.
3. *Complete closed-factor and length spectra of finite Zimin words*, https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-complete-closed-factor-and-length-spectra-of-finite-zimin-words--37549fa1d106.
4. D. Goc, H. Mousavi and J. Shallit, *On the Number of Unbordered Factors*, https://arxiv.org/abs/1211.1301.
