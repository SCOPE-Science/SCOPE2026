# Complete low-factor neighbor classification for alternating divisor sums at the exact 2-adic layer

## Finding
Define the multiplicative alternating divisor-sum function by \(\beta(1)=1\) and
\[
\beta(p^a)=p^a-p^{a-1}+p^{a-2}-\cdots+(-1)^a
\]
for primes \(p\) and positive integers \(a\). Let \(\Omega(m)\) be the number of prime factors, counted with multiplicity. The complete classification is
\[
\boxed{\text{For }n\ge2,\ n\equiv2\pmod4,\ \Omega(n+1)\le3:\quad\beta(n)=\beta(n+1)\iff n=194.}
\]
The common value is \(\beta(194)=\beta(195)=96\). In particular, the odd factor \(n/2\) is not assumed to be prime, a prime power, squarefree, or of bounded prime support.

## Assumptions and scope
This is the multiplicative alternating divisor sum of Tóth, not the alternating sum obtained by ordering the divisors. All integers are positive. Exactly one factor of \(2\) divides \(n\); the bound \(\Omega(n+1)\le3\) counts multiplicity, not merely distinct prime factors. The theorem makes no assertion for \(n\) divisible by \(4\), or for an odd successor with at least four prime factors.

## Proof
For every prime power \(p^a\) with \(a\ge1\), the exact formula gives
\[
0<\beta(p^a)<p^a,\qquad \beta(p^a)\ge p^{a-1}(p-1)=\varphi(p^a).
\]
Multiplicativity therefore yields \(0<\beta(t)\le t\) and \(\beta(t)\ge\varphi(t)\) for all positive integers \(t\), with \(\beta(t)<t\) when \(t>1\). For example, these inequalities also follow directly by separating even and odd exponents in \(\beta(p^a)=(p^{a+1}+(-1)^a)/(p+1)\).

Write \(n=2u\), where \(u\) is odd. Since \(\beta(2)=1\) and \(2\) is coprime to \(u\), multiplicativity gives \(\beta(n)=\beta(u)\). If \(u=1\), then \(n=2\), and \(\beta(2)=1\ne2=\beta(3)\). We may henceforth suppose \(u>1\).

Put \(m=2u+1=n+1\). If consecutive equality holds, then
\[
\varphi(m)\le\beta(m)=\beta(u)<u=\frac{m-1}{2}<\frac m2,
\]
so necessarily
\[
\frac{\varphi(m)}m<\frac12.\tag{1}
\]
But \(m\) is odd and \(\Omega(m)\le3\). If \(m\) has at most two distinct prime factors, then the minimum possible ratio occurs at the two smallest odd primes and
\[
\frac{\varphi(m)}m\ge\left(1-\frac13\right)\left(1-\frac15\right)=\frac8{15}>\frac12,
\]
contradicting (1). Hence \(m\) has exactly three distinct odd prime factors; since \(\Omega(m)\le3\), it is a product \(pqr\) of three distinct odd primes, \(p<q<r\).

If \(p\ge5\), then \(\varphi(m)/m\ge(4/5)(6/7)(10/11)>1/2\). If \(p=3\) but \(q\ge7\), then \(\varphi(m)/m\ge(2/3)(6/7)(10/11)>1/2\). Thus necessarily \(p=3,q=5\). If \(r\ge17\), then
\[
\frac{\varphi(m)}m=\frac23\cdot\frac45\cdot\left(1-\frac1r\right)
\ge\frac23\cdot\frac45\cdot\frac{16}{17}=\frac{128}{255}>\frac12,
\]
a final contradiction. Accordingly \(r\) is one of \(7,11,13\), giving the **exhaustive finite list**
\[
m\in\{3\cdot5\cdot7,3\cdot5\cdot11,3\cdot5\cdot13\}=\{105,165,195\}.
\]
Consequently \(u=(m-1)/2\) belongs to \(\{52,82,97\}\). The hypothesis that \(u\) is odd excludes \(52\) and \(82\), leaving \(u=97\), hence \(n=194\). Finally,
\[
\beta(194)=\beta(2)\beta(97)=1\cdot96=96,
\qquad \beta(195)=\beta(3)\beta(5)\beta(13)=2\cdot4\cdot12=96.
\]
This proves necessity and sufficiency for all integers satisfying the hypotheses. No computational cutoff is needed.

## Verification
The supplied standalone \(\texttt{verify.py}\) checks the prime-power formula and exact rational inequalities, then performs a finite independent regression over every \(2\le n\le10^6\) with \(n\equiv2\pmod4\) and \(\Omega(n+1)\le3\). Run `python verify.py` with Python 3 standard library. This finite check supplements but does not replace the complete unbounded proof.

## Relationship to prior work
Tóth's 2011 survey formulates the problem of equal consecutive values \(\beta(n)=\beta(n+1)\) (Problem 3) and records finite examples, including \(194,195\). OEIS A206368 lists known indices of equality, and OEIS A206369 tabulates the underlying alternating divisor-sum function. Neither a list of examples nor a finite search implies the exact classification here. A closely related classification for \(n=2p\) with \(p\) prime and a low-complexity odd neighbor restricts the even input to two prime factors counted with multiplicity. The present theorem removes that primality restriction **entirely** on the natural \(n\equiv2\pmod4\) layer: the odd integer \(u=n/2\) may have arbitrarily many distinct prime factors and arbitrarily large exponents. This is a strict extension of its successor case, not a corollary of the prime-only hypothesis.

## Limitations
The classification is limited to \(\Omega(n+1)\le3\) and \(\nu_2(n)=1\). It does not solve the unrestricted consecutive-equality problem, nor classify any other residue class. An obscure or unindexed prior derivation is not excluded. No independent mathematical or literature audit has been performed.

## References
1. L. Tóth, *A survey of the alternating sum-of-divisors function*, arXiv:1111.4842, first posted 2011-11-21, especially the definition and Problem 3 in Section 7. https://arxiv.org/abs/1111.4842
2. OEIS A206368, indices of consecutive equal alternating divisor sums. https://oeis.org/A206368
3. OEIS A206369, multiplicative alternating sum-of-divisors function. https://oeis.org/A206369
