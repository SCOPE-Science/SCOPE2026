# Exact gap and run spectra for the power-of-two evil-number tails

## Finding
For every integer \(r\ge2\), write \(q=2^r\), \(m=2q+1\), and let \(s_2(n)\) be the number of ones in the binary expansion of \(n\). Define the additive submonoid
\[
S_r=\left\langle\{n\in\mathbb Z_{\ge m}:s_2(n)\equiv0\pmod2\}\right\rangle\subseteq\mathbb N_0.
\]
Its positive gap set has the exact description
\[
\mathbb N_{>0}\setminus S_r=\{1,\ldots,2q\}\;\sqcup\;
\{n:2q+1\le n\le4q,\ s_2(n)\equiv1\pmod2\}.
\]
Consequently the Frobenius number, conductor and genus are, respectively,
\[
F(S_r)=4q,\qquad c(S_r)=4q+1,\qquad g(S_r)=3q.
\]
A gap run is a maximal interval of consecutive positive integers outside the semigroup. There is one gap run of length \(2q\), namely \([1,2q]\), and every other gap run has length one or two. Their counts are
\[
R_1(r)=\frac{q+2(-1)^r}{3},\qquad
R_2(r)=\frac{q-(-1)^r}{3}.
\]
In particular, \(R_1(r)/g(S_r)\to1/9\), so the asymptotic fraction of gaps that are isolated is \(1/9\).

## Assumptions and scope
Here an evil integer has even binary digit sum and an odious integer has odd binary digit sum. The semigroup includes zero by definition. The generator threshold \(m=2^{r+1}+1\) is itself evil and is the evil number at zero-based index \(q\) in the usual increasing enumeration \(e_i=2i+(s_2(i)\bmod2)\). The stated theorem concerns the natural power-of-two thresholds only, with \(r\ge2\); it does not classify arbitrary thresholds. In particular, the formula for \(F(S_r)\) specializes the Frobenius problem already studied for general evil-number tails; the complete gap set and gap-run spectrum are the contribution here.

## Proof
**1. Membership up to twice the minimum generator.** The least positive generator is \(m=2q+1\), since it has two binary ones. Every positive sum using two generators is at least \(2m=4q+2\). Hence for \(1\le n\le4q+1\), membership in \(S_r\) is equivalent to \(n\ge m\) and \(s_2(n)\) even. In particular every integer in \([1,2q]\) is a gap, \(4q\) is a gap, and \(4q+1\) belongs to \(S_r\).

**2. A conductor interval.** Show that every integer \(n=4q+t\) with \(1\le t\le2q+1\) belongs to \(S_r\). If \(s_2(t)\) is odd, the leading binary one at place \(4q\) is disjoint from the digits of \(t\), so \(s_2(4q+t)=1+s_2(t)\) is even and \(n\) is itself a generator. Suppose instead \(s_2(t)\) is even. If \(1\le t\le2q-1\), split the set of its nonzero binary positions into two nonempty subsets of odd cardinality, and call their respective sums \(a,b\). Then \(a+b=t\), \(1\le a,b<2q\), and both \(s_2(a)\) and \(s_2(b)\) are odd. Thus \(2q+a\) and \(2q+b\) are evil generators and their sum is \(4q+t\). The case \(t=2q\) has odd digit sum and was handled already. For \(t=2q+1\), choose \(j=1\) when \(r\) is even and \(j=2\) when \(r\) is odd, and set \(a=2^j\), \(b=2q+1-2^j\). Since \(r\ge2\), both lie strictly between zero and \(2q\), while \(s_2(a)=1\) and \(s_2(b)=r-j+2\) are odd. Hence the same two-generator representation applies. We have established the complete length-\(m\) interval \([4q+1,6q+1]\subseteq S_r\). Because \(m\in S_r\), adding nonnegative multiples of \(m\) proves that every integer \(n\ge4q+1\) lies in \(S_r\). The claimed gap set and conductor follow.

**3. Genus.** There are \(2q\) gaps below \(m\). Among the integers \([2q+1,4q]\), exactly \(q\) are odious. Indeed, \([2q,4q-1]\) has \(q\) odious integers, since it is a complete power-of-two binary block with balanced binary parity; its initial integer \(2q\) and the replacement integer \(4q\) are both odious. Thus \(g(S_r)=2q+q=3q\).

**4. Gap-run classification.** Define the Thue–Morse parity \(t(a)=s_2(a)\bmod2\). For \(1\le a<2q\), the number \(2q+a\) is a gap exactly when \(t(a)=0\); the endpoint \(4q\) is another gap. The elementary relations \(t(2k)=t(k)\) and \(t(2k+1)=1-t(k)\) show there are no three consecutive equal Thue–Morse bits. Since \(t(1)=1\), the initial long run ends at \(2q\); all later gap runs have length at most two. At the upper endpoint, \(t(2q-1)=r+1\bmod2\) and \(t(2q-2)=r\bmod2\), so appending the gap at \(4q\) cannot create a length-three run.

An interior singleton gap at \(2q+a\) (\(2\le a\le2q-2\)) has \(t(a)=0\) and \(t(a-1)=t(a+1)=1\). For \(a=2k\) this is equivalent to \(t(k-1)=t(k)=0\); for \(a=2k+1\), it is equivalent to \(t(k)=t(k+1)=1\). Thus interior singleton gaps correspond bijectively to the equal adjacent pairs in the prefix \(t(0),\ldots,t(q-1)\). Let \(E_r\) be the number of these pairs. Each even-to-odd neighboring pair is unequal, whereas an odd-to-even neighboring pair is equal precisely when the corresponding previous-level pair is unequal. Hence
\[
E_1=0,\qquad E_r=(2^{r-1}-1)-E_{r-1},
\]
which gives \(E_r=(q-1)/3\) for even \(r\), and \(E_r=(q-2)/3\) for odd \(r\). The final gap \(4q\) is an additional singleton if and only if \(4q-1\) belongs to \(S_r\), equivalently \(r\) is even, since \(s_2(4q-1)=r+2\). This yields \(R_1=(q+2(-1)^r)/3\). Since the remaining \(q\) gaps are partitioned into singleton and doubleton runs, \(R_1+2R_2=q\), yielding \(R_2=(q-(-1)^r)/3\). Finally, \(R_1/(3q)\to1/9\). This completes the proof.

## Verification
The independent finite enumeration program `verify_evil_tail.py` forms the generator set up to \(6q+3\), performs unbounded coin-change reachability, reconstructs the complete finite gap list, and independently checks exact gap-set equality, genus, conductor interval and maximal-run counts for every \(r\) from \(2\) through \(10\). It examines nine families and checks \(6,132\) gaps and \(4,106\) candidate positive generators, with no discrepancies. Its finite tests are consistency checks; the preceding proof handles infinitely many parameters and all integers.

## Relationship to prior work
Shallit, *Frobenius Numbers and Automatic Sequences* (arXiv:2103.10904; first public 2021-03-19), studies Frobenius numbers of tails of the evil sequence. The present \(F(S_r)=4q\) is a specialization of that established subject, not claimed to be a new general Frobenius theorem. Allouche and Shallit, *Additive Properties of the Evil and Odious Numbers and Similar Sequences* (arXiv:2112.13627; first public 2021-12-27), study additive representations from untruncated sequences. The inspected main results address representation counts rather than the exact positive gap set of a thresholded semigroup or its maximal-run counts. The complete gap and run formulas are not implied simply by the Frobenius value, which alone provides no interior-gap classification.

## Limitations
This theorem applies only to the thresholds \(m=2^{r+1}+1\) with \(r\ge2\); no assertion is made for all evil-tail starting indices. Full formal or independent human verification was not performed. Although the primary sources and relevant mathematical search results were compared for exact statements, implicit recovery from general automatic-sequence algorithms or other older literature remains a bibliographic possibility. Finite testing is not substituted for proof.

## References
1. Jeffrey Shallit, *Frobenius Numbers and Automatic Sequences*, arXiv:2103.10904 (first public 2021-03-19), https://arxiv.org/abs/2103.10904.
2. Jean-Paul Allouche and Jeffrey Shallit, *Additive Properties of the Evil and Odious Numbers and Similar Sequences*, arXiv:2112.13627 (first public 2021-12-27), https://arxiv.org/abs/2112.13627.
