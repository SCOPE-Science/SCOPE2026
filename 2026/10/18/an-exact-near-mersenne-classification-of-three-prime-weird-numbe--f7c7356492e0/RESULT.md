# An exact near-Mersenne classification of three-prime weird numbers

## Finding
Fix an integer \(k\ge 1\), and put \(M=2^{k+1}-1\). Let \(p<q\) be odd primes, set \(h=p-M\), and assume \(h>0\) and \(p>h^2\). Then \(h\) is even, \(p<2M\), and the integer \(n=2^k p q\) is weird if and only if **both** conditions hold:
\[
\frac{M(p+1)}{h+1}<q<\frac{M(p+1)}h,
\qquad
q\equiv-1+u h^{-1}\pmod p
\quad\text{for some }1\le u\le h-1.
\tag{1}
\]
Here \(h^{-1}\) denotes the inverse of \(h\) modulo \(p\). Every weird integer thus obtained is primitive weird. Its abundance \(a=\sigma(n)-2n\) obeys
\[
0<a<q,\qquad
 a<\frac{M(p+1)}{h+1}\le\frac{M(M+3)}3
<\frac{(M+1)(M+2)}3.
\tag{2}
\]
In particular, the one-third-scale abundance upper bound conjectured in Iannucci's 2015 study is valid throughout the full strip \(0<p-M<\sqrt p\). Condition (1) is an exact classification, not merely a sufficient construction.

## Assumptions and scope
An integer \(n\) is *abundant* if the sum \(\sigma(n)\) of all its positive divisors exceeds \(2n\); it is *semiperfect* if some distinct proper divisors sum to \(n\). It is *weird* when abundant but not semiperfect, and *primitive weird* when no proper divisor is weird. The claim concerns all \(k\ge1\) and all ordered odd primes \(p<q\) subject only to \(h=p-M>0\) and \(p>h^2\). It does not assume or assert the existence of such prime pairs for every \(k\).

Since \(M\) and \(p\) are odd, \(h\ge2\) is even. The hypothesis \(p=M+h>h^2\) implies \(M>h(h-1)\ge h\), hence \(M<p<2M\). The prime \(p>h\) makes the modular inverse in (1) unambiguous.

## Proof
**Step 1: Exact small-divisor representation.** Multiplicativity of the divisor sum gives
\[
 a=(2^{k+1}-1)(p+1)(q+1)-2^{k+1}pq
 =M(p+1)-hq=M(1+p+q)-pq.
\tag{3}
\]
Whenever \(a>0\), we have \(a<Mp<pq\), since \(M-hq<0\). The sum of all proper divisors is \(n+a\). Complementing a subset therefore shows that \(n\) is semiperfect exactly when \(a\) is representable as a sum of distinct proper divisors. No divisor divisible by \(pq\) can contribute to such a sum, because each is at least \(pq>a\). All remaining divisors are \(2^j\), \(2^jp\), and \(2^jq\) for \(0\le j\le k\). As their powers-of-two subset sums fill \(\{0,1,\ldots,M\}\), representability is equivalent to
\[
 a=r+sp+tq,\qquad 0\le r,s,t\le M \quad(r,s,t\text{ integers}).
\tag{4}
\]
The coefficients use disjoint divisor blocks, so (4) is both necessary and sufficient.

**Step 2: An abundance \(a\ge q\) forces semiperfectness.** Assume \(a\ge q\). For \(t=0,1\), the numbers \(b_t=a-tq\) lie in \([0,Mp)\). If \(b_t\bmod p\le M\) for either \(t\), writing \(b_t=sp+r\) gives \(0\le s<M\), \(0\le r\le M\), and (4). Thus a counterexample would require both residues to belong to the short terminal interval \(\{M+1,\ldots,p-1\}\). Write
\[
 a\equiv-u,\quad a-q\equiv-v\pmod p,
 \qquad 1\le u,v\le h-1.
\]
Then \(q\equiv d=v-u\pmod p\), with \(2-h\le d\le h-2\). Reducing (3) modulo \(p\), using \(M\equiv-h\pmod p\), yields
\[
 u\equiv h(1+q)\equiv h(1+d)\pmod p.
\tag{5}
\]
But \(z=h(1+d)\) lies in \([h(3-h),h(h-1)]\). Because \(p>h^2\), a positive \(z\) is between \(h\) and \(p-1\); a negative \(z\) has \(p+z>3h>h-1\), while \(z=0\) has zero residue. Consequently the least nonnegative residue of \(z\) modulo \(p\) cannot belong to \(\{1,\ldots,h-1\}\), contradicting (5). Hence at least one of \(b_0,b_1\) gives a representation (4). Every abundant integer in this strip with \(a\ge q\) is therefore semiperfect.

**Step 3: The exact two-parameter test.** If \(0<a<q\), equation (4) forces \(t=0\). Since \(a<Mp\), representability reduces exactly to \(a\bmod p\le M\). Thus the integer is weird exactly when \(a\bmod p=p-u\) for some \(1\le u<h\). From \(a\equiv-h(1+q)\pmod p\), this is precisely \(h(1+q)\equiv u\pmod p\), or the congruence in (1). Finally, by (3), the two strict inequalities \(a>0\) and \(a<q\) are equivalent to the open interval for \(q\) in (1). Step 2 excludes all remaining abundant integers, proving the equivalence.

**Step 4: The upper bound and primitivity.** From \(a<q\) and (3), \(q>M(p+1)/(h+1)\), so
\[
 a=M(p+1)-hq<\frac{M(p+1)}{h+1}
 =M\left(1+\frac{M}{h+1}\right)
 \le \frac{M(M+3)}3.
\]
The final inequality in (2) follows by expanding \((M+1)(M+2)=M(M+3)+2\). To see primitivity without another hypothesis, every proper divisor lacking \(p\) or \(q\) is deficient: for example, \(\sigma(2^j p)-2(2^jp)=(2^{j+1}-1)-p<0\) for \(0\le j\le k\), since \(p>M\), and similarly for \(q\). For a proper divisor \(2^j pq\) with \(j<k\), put \(U=2^{j+1}-1\le(M-1)/2\). Its abundance is \(U(1+p+q)-pq\), which decreases with \(p,q\) for \(p,q>U\). It is therefore strictly below
\[
 \frac{M-1}{2}(1+2M)-M^2=-\frac{M+1}{2}<0.
\]
Every proper divisor is deficient and hence not weird. This completes the proof.

## Verification
A standalone Python 3 exact-integer checker, `VERIFY.py`, tests the classification against an independently expressed subset-sum criterion for every candidate prime pair with \(1\le k\le10\). It examines 186282 prime pairs in the near-Mersenne strip and, additionally, checks the unrestricted published weird-number counts \(1,1,5,3,10,23,29,53,115,210\) for the same ten exponents. For \(k\le3\), it also constructs subset sums directly from actual proper divisors. The strip counts, in order, are \(1,0,3,1,5,5,10,9,32,51\). The checker prints `VERIFY_OK` on success.

For instance, \(k=5\), \(M=63\), \(p=67\), \(h=4\) give eligible primes \(q=887,971,1021\), with abundances \(736,400,200\), respectively. Those integers occur among established examples; the novelty is the uniform exact classification and proof of the conjectured upper bound in the stated strip. These finite checks corroborate the algebraic theorem; finite enumeration alone would not prove the result for all exponents.

## Relationship to prior work
Iannucci's 2015 paper proves general necessary conditions \(M<p<2M\) and \(M<a<M(M+1)\), gives a finite search criterion, and conjectures the upper bound \(a<(M+1)(M+2)/3\). It does not establish an all-exponent modular classification for \(p> (p-M)^2\) or prove this conjecture on that strip. Melfi's 2014 theorem gives a different sufficient prime construction with \(p\) near \(2^{k+2}\), rather than \(M=2^{k+1}-1\). Amato–Hasler–Melfi–Parton treat constructive families with additional prime factors. A later published result, “A uniform three-quarter abundance bound for weird numbers of form \(2^k p q\),” proves \(a<3M^2/4+M\) for **all** weird integers of this form via residue packing. Its universal bound is weaker on the near-Mersenne strip and neither gives (1) nor implies the conjectured one-third-scale bound proved here. The common divisor-sum identity and complement criterion are acknowledged prior ingredients; the short-residue contradiction in Step 2 and its all-exponent consequences are the additional claims.

## Limitations
This is not a proof of Iannucci's one-third conjecture outside \(0<p-M<\sqrt p\), nor of infinitude of prime pairs in any particular interval or residue class. The congruence is an exact conditional characterization for prime \(q\), not a primality test. A differently indexed prior classification or an implicit consequence of older structural work (including Pajunen's 1980 study) cannot be conclusively ruled out by database and literature searches; this is the principal residual originality risk. The proof is independent of the finite checks and does not rely on any external certification.

## References
1. D. E. Iannucci, “On primitive weird numbers of the form \(2^k p q\),” arXiv:1504.02761v1, first publicly posted 7 April 2015, https://arxiv.org/html/1504.02761v1.
2. G. Melfi, “On the conditional infiniteness of primitive weird numbers,” *Journal of Number Theory* **147** (2015), 508–514, DOI:10.1016/j.jnt.2014.07.024; available online 16 September 2014; lawful open text https://libra.unine.ch/bitstreams/9084975d-4950-470b-aa6e-4f3e564c2f4b/download.
3. G. Amato, M. F. Hasler, G. Melfi, and M. Parton, “Primitive weird numbers having more than three distinct prime factors,” *Rivista di Matematica della Università di Parma* **7** (2016), 153–163; https://arxiv.org/abs/1803.00324 (later preprint).
4. “A uniform three-quarter abundance bound for weird numbers of form \(2^k p q\),” public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-uniform-three-quarter-abundance-bound-for-weird-numbers-of-for--b810d8b66c9f.
