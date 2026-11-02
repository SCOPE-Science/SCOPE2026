# Complete unbordered-factor and binary-digit spectra of finite Zimin words

## Finding
For each integer \(n\ge1\), define the finite **literal** Zimin word \(Z_0=\varepsilon\) and \(Z_n=Z_{n-1}a_nZ_{n-1}\), where the letters \(a_1,a_2,\ldots\) are pairwise distinct. A nonempty word is **unbordered** if none of its nonempty proper prefixes is also a suffix. Write \(U_n(\ell)\) for the number of **distinct**, rather than occurrence-counted, unbordered contiguous factors of \(Z_n\) of length \(\ell\). Let \(s_2(q)\) be the number of ones in the ordinary base-two expansion of a nonnegative integer \(q\).

**Complete family.** For each \(1\le r\le n\), the factors whose greatest-index letter is \(a_r\) are exactly
\[
\left\{\operatorname{suf}_{i}(Z_{r-1})\,a_r\,\operatorname{pre}_{j}(Z_{r-1}):\quad 0\le i,j<2^{r-1},\quad i\mathbin{\&}j=0\right\},
\]
where \(\operatorname{suf}_0=\operatorname{pre}_0=\varepsilon\) and \(\mathbin{\&}\) denotes bitwise AND of nonnegative integers. There are no duplicates within or between these families.

**Complete length spectrum.** For every integer \(\ell\ge1\),
\[
U_n(\ell)=\begin{cases}
\bigl(n-\lceil\log_2\ell\rceil\bigr)\,2^{s_2(\ell-1)},&1\le\ell\le2^{n-1},\\
0,&\ell>2^{n-1}.
\end{cases}
\]
In particular the longest unbordered factors have length \(2^{n-1}\) and there are exactly \(2^{n-1}\) of them. The number over all lengths is
\[
\sum_{\ell\ge1}U_n(\ell)=\frac{3^n-1}{2}.
\]
For each fixed greatest-index letter \(a_r\), the length-generating polynomial is
\[
 x\prod_{t=0}^{r-2}\bigl(1+2x^{2^t}\bigr),
\]
with the empty product equal to \(1\).

## Assumptions and scope
The alphabet contains exactly the distinct symbols \(a_1,\ldots,a_n\), and a **factor** means a contiguous substring with literal symbol equality. Neither erasing/nonerasing substitutions of the variables of a Zimin pattern nor scattered subsequences are included. Count a distinct factor once, even if it appears in multiple positions. Prefixes/suffixes of length zero are permitted in the displayed construction, but the constructed factor is always nonempty. Standard base-two expansions of the integers \(i,j\) are used; no fixed leading-zero width is needed.

## Proof
**Step 1: a unique-marker lemma.** Let \(X\) and \(Y\) be finite words not containing a symbol \(c\). Any proper border of \(XcY\) must have length at most \(\min(|X|,|Y|)\): a common proper prefix and suffix containing \(c\) would place the unique marker \(c\) at the same position from both ends, forcing the prefix and suffix to be the whole word. Consequently \(XcY\) is unbordered precisely when no prefix of \(X\) of length \(k\) equals a suffix of \(Y\) of length \(k\), for \(1\le k\le\min(|X|,|Y|)\).

**Step 2: the exact bit-disjointness lemma.** Fix \(m\ge0\). For \(0\le i,j<2^m\) and fresh \(c\) absent from \(Z_m\), define
\[
 W_m(i,j)=\operatorname{suf}_i(Z_m)c\operatorname{pre}_j(Z_m).
\]
We prove simultaneously for all such pairs, by induction on \(m\), that \(W_m(i,j)\) is unbordered if and only if \(i\mathbin{\&}j=0\). At \(m=0\), only \(i=j=0\) is allowed, giving the unbordered word \(c\).

For \(m\ge1\), write \(h=2^{m-1}\) and \(Z_m=Z_{m-1}a_mZ_{m-1}\). Split each index into its high bit and lower residue: \(i=\alpha h+i'\), \(j=\beta h+j'\), with \(\alpha,\beta\in\{0,1\}\) and \(0\le i',j'<h\). If both high bits vanish, the relevant suffix and prefix lie entirely in \(Z_{m-1}\), so the assertion reduces exactly to \(W_{m-1}(i',j')\). If \(\alpha=1,\beta=0\), the left segment before \(c\) starts with \(\operatorname{suf}_{i'}(Z_{m-1})a_m\), whereas the right segment contains no \(a_m\). By Step 1, any border of length greater than \(i'\) is impossible; for lengths at most \(i'\), the border equality is exactly the one in \(W_{m-1}(i',j')\). The case \(\alpha=0,\beta=1\) is symmetric (candidate borders longer than \(j'\) contain \(a_m\) on the right but not the left). Finally if \(\alpha=\beta=1\), the word
\[
 \operatorname{suf}_{i'}(Z_{m-1})a_m\operatorname{pre}_{j'}(Z_{m-1})
\]
is simultaneously a nonempty proper prefix and proper suffix of \(W_m(i,j)\), so \(W_m(i,j)\) is bordered. Therefore the high bits cannot both equal \(1\), and otherwise only the induction hypothesis for the lower bits matters: exactly \(i\mathbin{\&}j=0\).

**Step 3: no factors omitted or repeated.** Any factor of \(Z_n\) with maximal letter \(a_r\) avoids every \(a_s\) with \(s>r\). Since \(a_n\) occurs once in \(Z_n\), such a factor is contained in one of the two copies of \(Z_{n-1}\) when \(r<n\); iterating the argument shows that it is a factor of \(Z_r\). In \(Z_r=Z_{r-1}a_rZ_{r-1}\), the letter \(a_r\) occurs uniquely, hence the factor must be \(\operatorname{suf}_i(Z_{r-1})a_r\operatorname{pre}_j(Z_{r-1})\) for unique indices \(0\le i,j\le |Z_{r-1}|=2^{r-1}-1\). Step 2 selects precisely the unbordered factors. Different values of \(r\) have different maximal letters, and within one rank the unique position of \(a_r\) determines \(i,j\); thus all displayed factors are distinct.

**Step 4: length distribution and total.** For rank \(r\), a constructed factor has length \(\ell=1+i+j\). Under \(i\mathbin{\&}j=0\), the sum \(i+j\) is the bitwise OR \(i\mathbin{|}j\), with no carries. Consequently \(0\le\ell-1<2^{r-1}\); for each one-bit of \(\ell-1\), the bit can be assigned independently to \(i\) or to \(j\), giving \(2^{s_2(\ell-1)}\) factors. The number of allowable ranks is exactly \(n-\lceil\log_2\ell\rceil\) when \(\ell\le2^{n-1}\), otherwise zero. This proves the length spectrum and the longest-length assertion. For fixed \(r\), every bit position contributes either nothing, membership in \(i\), or membership in \(j\), so its generating polynomial is \(x\prod_{t=0}^{r-2}(1+2x^{2^t})\) and its cardinality is \(3^{r-1}\). Summing the geometric series over \(1\le r\le n\) gives \((3^n-1)/2\). All claims follow. \(\square\)

## Verification
The supplied standalone `checker.py` uses brute-force literal-factor extraction and naive border testing, independently builds the binary-disjointness templates, and checks equality of the two sets, the length spectra, and totals for ranks \(1\) through \(8\). It also independently tests the marker lemma's predicted unbordered status on every index pair \((i,j)\) for marker ranks \(0\) through \(7\). All tested cases passed. Run with `python3 checker.py` using Python 3.8+ (3.10+ preferred for integer `.bit_count()`). These finite tests are corroboration, not a proof of the all-rank statements; the induction above is the proof.

## Relationship to prior work
Goc, Mousavi and Shallit [1] study unbordered-factor enumeration of several automatic sequences, notably the infinite Thue–Morse word; they motivate the invariant but do not provide this rank-parametrized literal Zimin-factor classification. Rytter and Shur [2] analyze Zimin-pattern occurrences and searching under substitutions; the objects and claims there are different. Cooper and Rorabaugh [3] study Zimin-pattern instances and recurrences for bifix-free words over fixed alphabets; the fact that a word is bifix-free does not say whether it is a factor of a particular literal Zimin word. Existing general bifix-free-word enumeration therefore does not automatically give the displayed factor family and popcount spectrum. The overlap comparison also distinguished existing enumerations of *minimal absent* Zimin factors and of *Lyndon* Zimin factors: the first concerns absent strings, while the second counts a strict subclass of present unbordered strings. No examined source established the stated formulas; this does not establish unconditional historical uniqueness.

## Limitations
The results apply to finite literal Zimin words with an alphabet increasing with rank, not arbitrary homomorphic images, infinite-alphabet limits, or general automatic sequences on a fixed alphabet. The family is an exact mathematical characterization, not an enumeration algorithm optimized for memory. Bibliographic priority is qualified because mathematically equivalent statements may appear in unindexed or unavailable literature. Mathematical checking and historical comparisons have not received independent audit.

## References
[1] D. Goc, H. Mousavi, J. Shallit, "On the Number of Unbordered Factors," arXiv:1211.1301, first posted 2012-11-06, https://arxiv.org/abs/1211.1301.

[2] W. Rytter, A. M. Shur, "On Searching Zimin Patterns," arXiv:1409.8235, first posted 2014-09-29, https://arxiv.org/abs/1409.8235.

[3] J. Cooper, C. Rorabaugh, "Asymptotic Density of Zimin Words," arXiv:1510.03917, first posted 2015-10-13, https://arxiv.org/abs/1510.03917.
