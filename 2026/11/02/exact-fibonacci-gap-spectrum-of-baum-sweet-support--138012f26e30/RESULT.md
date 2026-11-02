# Exact Fibonacci gap spectrum of Baum–Sweet support

## Finding

Let \(b_0=1\) and, for every positive integer \(j\), let \(b_j=1\) precisely when every maximal run of zeros in the standard binary expansion of \(j\) has even length; otherwise let \(b_j=0\). Let \(S_M=\{0\le j<2^M:b_j=1\}\), in increasing order, for each integer \(M\ge2\). Write \(H_M(d)\) for the number of consecutive pairs \((a,a+d)\) in that ordered set, for each positive integer \(d\). Adopt Fibonacci numbers \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\).

**Theorem (complete gap histogram).** For every integer \(M\ge2\),
\[
H_M(1)=1+\left\lfloor\frac{M-1}{2}\right\rfloor,\qquad
H_M(2)=\left\lfloor\frac{M}{2}\right\rfloor,\qquad
H_M(3)=F_{M+1}-2.
\]
For every integer \(r\) with \(3\le r\le M-2\), define
\[
d_r=2^{r-1}+\begin{cases}2,&r\text{ odd},\\1,&r\text{ even}.\end{cases}
\]
Then \(H_M(d_r)=F_{M-r+1}-1\), and \(H_M(d)=0\) at every other positive integer \(d\). In particular, the complete infinite set of gaps is
\[
\{1,2,3\}\cup\{6,9,18,33,66,129,\ldots\}.
\]

The theorem also gives the limiting empirical gap law. If one gap is chosen uniformly from those in \(S_M\) and \(M\to\infty\), then the mass at 3 approaches \(\varphi^{-1}\), the mass at each \(d_r\), \(r\ge3\), approaches \(\varphi^{-(r+1)}\), and the masses at 1 and 2 approach zero, where \(\varphi=(1+\sqrt5)/2\). The resulting probability law has infinite mean, with a tail of power-law order \(t^{-\log_2\varphi}\). The actual mean gap in \(S_M\) is exactly \((2^M-1)/(F_{M+2}-1)\), which diverges as \(M\to\infty\).

## Assumptions and scope

All integers are nonnegative unless otherwise specified. A consecutive pair in \(S_M\) means two entries with no third entry of \(S_M\) strictly between. The last entry of \(S_M\) is \(2^M-1\), so there is no artificial terminal gap to \(2^M\). The binary alphabet has its usual numerical and lexicographic order. The theorem is about occurrences of the symbol 1 in the infinite Baum–Sweet word, not about its subsequence universality, factor counts, or its formal-power-series inverse.

## Proof

**1. Accepted binary strings.** Every positive accepted integer has a unique canonical binary word beginning in 1 such that all runs of 0 have even length. Equivalently, the language is \(1(1\mid00)^*\). Let \(A_m\) be the number of accepted canonical words of length \(m\). We have \(A_1=A_2=1\), since the only such words are respectively \(1\) and \(11\). For \(m\ge3\), an accepted word ends either in 1 or in 00, giving a bijective last-block partition and \(A_m=A_{m-1}+A_{m-2}\). Thus \(A_m=F_m\). Including the accepted integer 0,
\[
|S_M|=1+\sum_{m=1}^{M}F_m=F_{M+2}.
\]

**2. Internal adjacent words of equal length.** Fix \(m\ge3\). Consider two lexicographically consecutive, distinct accepted \(m\)-bit words. Write their longest common prefix as \(p\), followed by the respective digits 0 and 1, and then \(r\) further digits, where \(r=m-|p|-1\). Since the automaton recognizing even-length zero runs has no permitted choice immediately after an unmatched first 0, the shared prefix \(p\) ends in an even-zero-run state; hence \(p\) itself is an accepted canonical binary word. It begins in 1, so \(|p|\ge1\), and the branch beginning with 0 forces a second zero, hence \(r\ge1\).

Within the accepted words beginning \(p0\), the largest available completion is \(p00\,1^{r-1}\). Within the words beginning \(p1\), the smallest completion is
\[
p1\,0^r\quad(r\text{ even}),\qquad
p1\,0^{r-1}1\quad(r\text{ odd}).
\]
Both are valid, and there can be no accepted word strictly between them because every string with prefix \(p0\) lies below every string with prefix \(p1\), while these are the respective extrema. This establishes both the necessity and sufficiency of all described pairs. Their difference in numerical value is
\[
d_r=2^{r-1}+\begin{cases}2,&r\text{ odd},\\1,&r\text{ even}.\end{cases}
\]
Indeed the low \(r+1\) bits of the left word have value \(2^{r-1}-1\), while the low \(r+1\) bits of the right word have value \(2^r\) for even \(r\), or \(2^r+1\) for odd \(r\). Therefore their difference equals \(2^{r-1}+1\) or \(2^{r-1}+2\), respectively.

For each fixed pair \((m,r)\) with \(1\le r\le m-2\), the prefix \(p\) has length \(m-r-1\), and there are exactly \(F_{m-r-1}\) valid choices of \(p\). These pairs are distinct because their maximal common prefix is unique; every consecutive within-length pair is accounted for once. Both \(r=1\) and \(r=2\) produce gap 3; \(r\ge3\) produces mutually distinct gaps \(d_r\).

**3. Cross-length boundaries.** The maximum accepted \(m\)-bit word is \(1^m\), of value \(2^m-1\). The minimum accepted \((m+1)\)-bit word is \(10^m\) when \(m\) is even and \(10^{m-1}1\) when \(m\) is odd. Accordingly the cross-length gap is 1 for even \(m\), and 2 for odd \(m\). For \(1\le m\le M-1\), these contribute \(\lfloor(M-1)/2\rfloor\) gaps of 1 and \(\lfloor M/2\rfloor\) gaps of 2. The additional initial adjacent pair \((0,1)\) contributes exactly one gap of 1.

**4. Exact histogram.** Summing the internal contributions over all bit lengths at most \(M\), the gap 3 occurs
\[
\sum_{m=3}^{M}F_{m-2}+\sum_{m=4}^{M}F_{m-3}=(F_M-1)+(F_{M-1}-1)=F_{M+1}-2
\]
times. For fixed \(r\ge3\), the gap \(d_r\) occurs only when \(m\ge r+2\), and its number of occurrences is
\[
\sum_{m=r+2}^{M}F_{m-r-1}=F_{M-r+1}-1.
\]
All possibilities have been partitioned into within-length and cross-length pairs, proving completeness. As checks, the histogram sums to \(F_{M+2}-1\) pairs and its distance-weighted sum equals \(2^M-1\).

**5. Limiting distribution.** Binet's formula gives \(F_{M-c}/F_{M+2}\to\varphi^{-(c+2)}\) for each fixed integer \(c\). Hence the limits displayed in the finding follow. The masses add to one since \(\varphi^{-1}+\sum_{r\ge3}\varphi^{-(r+1)}=\varphi^{-1}+\varphi^{-2}=1\). Because \(d_r\) lies between positive constant multiples of \(2^r\), the limiting tail has order \(t^{-\log_2\varphi}\); since \(2/\varphi>1\), its mean diverges. The exact finite mean follows by telescoping the distances between the first and last accepted integers, 0 and \(2^M-1\), and using \(|S_M|=F_{M+2}\). This completes the proof.

## Verification

The included `checker.py` tests the given Baum–Sweet predicate directly, constructs the increasing finite support, computes its actual successive-difference histogram, and compares it with the closed form for every integer \(2\le M\le16\). It checks the total number of accepted integers, total number of pairs, and the telescoping weighted sum independently. Execution with Python 3 produced `ALL TESTS PASSED`. These finite tests support, but do not replace, the unrestricted proof above.

## Relationship to prior work

OEIS A060142 explicitly enumerates the same increasing support and supplies its self-generating relations \(x\mapsto2x+1\) and \(x\mapsto4x\), but does not state the displayed all-scale consecutive-gap histogram or limiting probability law. Baum and Sweet's foundational 1976 work introduces the underlying automatic sequence. Merta's 2018 article studies the index sequence \((\ell_n)\) of 1 positions, proves its Fibonacci-word parity coding and non-regularity, and gives a recursion for the sets of fixed-bit-length accepted integers; those results are not the stated exact gap histogram. Merta also gives an exact difference spectrum for a **different** sequence, the position sequence of 1s in a formal-power-series inverse (Theorem 4.6); these are not the Baum–Sweet support differences here. Dreyfus, Hardouin, and Roques establish a hypertranscendence property of Baum–Sweet generating functions, a separate invariant. The all-scale histogram is a further derived classification, not an assertion that the underlying support or its regular-language description was previously unknown.

## Limitations

This theorem concerns the standard binary Baum–Sweet sequence and windows with upper endpoint exactly a power of two. It does not identify the frequency of gaps for arbitrary truncation lengths, or derive mixing properties of the induced infinite gap sequence. The limiting distribution is along dyadic cutoff windows, not a claim about every possible averaging scheme. No independent external mathematical audit is asserted. Historical-priority assessment is limited by searchable material and by the inaccessible full text of the original 1976 Baum–Sweet paper; the available source descriptions do not give evidence that this gap histogram appeared there.

## References

1. OEIS A060142, *Ordered set \(S\) defined by the rules \(0\in S\), \(x\in S\Rightarrow2x+1,4x\in S\)*, Clark Kimberling, first dated 2001-03-05. https://oeis.org/A060142
2. L. E. Baum and M. M. Sweet, *Continued Fractions of Algebraic Power Series in Characteristic 2*, *Annals of Mathematics* 103 (1976), 593–610. https://doi.org/10.2307/1970953
3. Ł. Merta, *Composition inverses of the variations of the Baum–Sweet sequence*, arXiv:1803.00292v1 (2018), §2 and Theorem 4.6. https://arxiv.org/html/1803.00292v1
4. T. Dreyfus, C. Hardouin, and J. Roques, *Hypertranscendence of solutions of Mahler equations*, arXiv:1507.03361v1 (first public 2015-07-13), §4.2. https://arxiv.org/abs/1507.03361
5. C. Kimberling, *A Self-Generating Set and the Golden Mean*, *Journal of Integer Sequences* 3 (2000), Article 00.2.8. The underlying generator in that article differs from the current Baum–Sweet support recurrence. https://cs.uwaterloo.ca/journals/JIS/VOL3/goldentext.html
