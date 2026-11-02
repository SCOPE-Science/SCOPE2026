# The two-prime-support case of the alternating-divisor Lehmer problem

## Finding
Let \(\beta\) be the multiplicative alternating sum-of-divisors function, defined on prime powers by
\[\beta(p^a)=p^a-p^{a-1}+\cdots+(-1)^a=\frac{p^{a+1}+(-1)^a}{p+1}.\]
Write \(\omega(n)\) for the number of distinct prime divisors of \(n\).

**Theorem.** For every integer \(n>1\) such that \(\omega(n)\le2\),
\[\beta(n)\mid n-1\quad\Longleftrightarrow\quad n\text{ is prime or }n=4.\]
Hence every composite solution other than \(4\) to the alternating-divisor Lehmer divisibility problem must have at least three distinct prime divisors.

## Assumptions and scope
All integers and exponents in the theorem are positive; primes are rational primes. The divisibility is in \(\mathbb Z\). No claim is made for integers with at least three distinct prime factors.

## Proof
For every prime \(p\) and exponent \(a\ge1\), the geometric alternating sum satisfies
\[p^{a-1}(p-1)\le\beta(p^a)\le p^a-1.\]
The first inequality follows by subtracting \(p^{a-1}(p-1)\) from the displayed closed form, yielding \((p^{a-1}+(-1)^a)/(p+1)\ge0\); the second follows from the decreasing alternating expansion. Multiplicativity gives \(\beta(n)\ge\varphi(n)\). If \(n\) has at least two distinct prime factors, write \(n=uv\) with coprime \(u,v>1\); then \(\beta(n)\le(u-1)(v-1)<n-1\). For a prime power \(p^a\) with \(a\ge2\), the same strict inequality holds except for \(p^a=4\). In particular, every composite candidate other than \(4\) would have integer quotient \((n-1)/\beta(n)\ge2\).

**One prime factor.** If \(n=p^a\) with odd \(p\) and \(a\ge2\), then
\[1<\frac{p^a-1}{\beta(p^a)}<\frac{p}{p-1}\le\frac32<2,\]
contradicting integrality. If \(p=2\), then \(a=2\) gives \(\beta(4)=3\), while for \(a\ge3\) the alternating geometric formula gives \((2^a-1)/2<\beta(2^a)<2^a-1\), again excluding an integer quotient. The primes themselves satisfy \(\beta(p)=p-1\).

**Two odd prime factors.** Write \(n=p^a q^b\) with distinct odd primes \(p<q\). Since \(p\ge3\) and \(q\ge5\),
\[\frac{n-1}{\beta(n)}<\frac{n}{\varphi(n)}=\frac{p}{p-1}\frac{q}{q-1}\le\frac{15}{8}<2.\]
Together with \(\beta(n)<n-1\), this rules out divisibility.

**One even and one odd prime factor.** Put \(n=2^a p^b\) with \(p\ge3\) odd and \(a,b\ge1\). Since \(n-1\) is odd and \(\beta(2^a)\) is odd, \(\beta(p^b)\) must be odd. Its alternating formula modulo two shows that \(b\) must be even, hence \(b\ge2\). Set \(A=\beta(2^a)\), \(B=\beta(p^b)=(p^{b+1}+1)/(p+1)\), and \(k=(n-1)/(AB)\).

If \(a=1\), then \(A=1\), \(B<p^b\) and \(B>p^{b+1}/(p+1)\). Consequently \(1<k<2(p+1)/p\le8/3\), forcing \(k=2\). The equation \(2B=2p^b-1\) becomes \(2p^b=p+3\), impossible for \(p\ge3\), \(b\ge2\).

Suppose \(a\ge2\). The explicit geometric expression yields
\[\frac{2^a}{A}<\frac32\quad(a\text{ even}),\qquad \frac{2^a}{A}\le\frac85\quad(a\text{ odd},\ a\ge3),\]
and \(p^b/B<p/(p-1)\). If \(p\ge5\), then \(n/(AB)<(8/5)(5/4)=2\). If \(p=3\) and \(a\) is even, then \(n/(AB)<(3/2)(3/2)\) would be too weak; instead the sharper even-exponent bound \(2^a/A<3/2\) combines with \(3^b/B<4/3\) to yield \(n/(AB)<2\). In both cases, \(1<k<2\), a contradiction.

The sole remaining case is \(p=3\) with odd \(a\ge3\). The bounds give \(1<k< (8/5)(4/3)=32/15<3\), so \(k=2\). Now
\[A=\frac{2^{a+1}-1}{3},\qquad B=\frac{3^{b+1}+1}{4}.\]
The equation \(2AB=2^a3^b-1\) simplifies to
\[3^{b+1}-2^{a+1}=5.\]
Because \(b\) is even and \(a\ge3\), the left side is congruent to \(3\pmod8\), whereas the right side is congruent to \(5\pmod8\). This final contradiction completes the proof. \(\square\)

## Verification
The companion standalone script `verify.py` independently computes \(\beta(n)\) by the divisor convolution \(\sum_{d\mid n}d\lambda(n/d)\), where \(\lambda\) is the Liouville function, and compares it to the prime-power product formula for all \(2\le n\le50000\). It checks all divisibility outcomes with at most two distinct prime factors and a grid of \(420\) even two-prime exponent combinations. Execution produced `CHECK_OK all_n=2..50000; two_support_count=23052; exceptional_composite=4; parameter_pairs=420`. This finite verification does not establish the theorem; the argument above treats all permitted exponents.

## Relationship to prior work
L. Tóth, *A survey of the alternating sum-of-divisors function*, arXiv:1111.4842v1 (first posted 2011-11-21), gives the definition, the comparison with Euler's totient, and explicitly poses the problem of whether any composite \(n\ne4\) satisfies \(\beta(n)\mid n-1\). The present result resolves the entire subclass with at most two prime supports but does not resolve the remaining open question. Classical Lehmer-type divisibility for Euler's totient applies to a different function and does not imply this classification.

## Limitations
The result neither establishes nor rules out composite counterexamples with at least three distinct prime factors. Searches and examination of the primary survey did not locate an earlier proof of this precise support-two classification, but absence from search results does not prove uniqueness; equivalent specialist literature could exist. No independent audit has been performed.

## References
1. L. Tóth, *A survey of the alternating sum-of-divisors function*, arXiv:1111.4842v1, 2011-11-21, https://arxiv.org/abs/1111.4842.
2. OEIS A206369, alternating sum-of-divisors function, https://oeis.org/A206369.
3. Classical Euler totient and Liouville convolution identities, as used and derived above.
