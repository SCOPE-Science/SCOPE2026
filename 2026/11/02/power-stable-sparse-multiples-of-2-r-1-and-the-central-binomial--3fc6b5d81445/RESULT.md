# Power-stable sparse multiples of \(2^r-1\) and the central-binomial fixed divisor

## Finding
For integers \(r\ge2\) and \(k\ge1\), let \(M=2^r-1\), and let \(s_2(n)\) be the number of nonzero bits of \(n>0\). Then
\[
\min_{t\ge1}s_2(M^k t)=r,\qquad
\gcd_{t\ge1}\binom{2M^k t}{M^k t}=2^r.
\]
Both equalities hold for every power \(k\), with no prime assumption on \(M\). The gcd ranges over all positive indices; it is not a computed finite gcd.

## Assumptions and scope
All quantities are ordinary positive integers. For a prime \(p\), \(\nu_p(n)\) denotes its \(p\)-adic exponent. Exponents in sums of powers of two are distinct unless explicitly described as tokens before carrying. The classical lifting-the-exponent lemma for odd primes is used in the standard case \(p\mid a-1\): \(\nu_p(a^d-1)=\nu_p(a-1)+\nu_p(d)\), when \(p\) is odd, \(a\equiv1\pmod p\), and \(d>0\).

## Proof
**1. A universal lower bound.** If \(N=\sum_{i=1}^{s}2^{e_i}>0\) is divisible by \(M\), reduce each \(e_i\) modulo \(r\), since \(2^r\equiv1\pmod M\). View the resulting multiset as \(s\) tokens of weights \(1,2,\ldots,2^{r-1}\). Whenever two tokens have the same weight \(2^j\), replace them by one token of weight \(2^{j+1}\), interpreting \(2^r\) as \(1\). This preserves the residue modulo \(M\), decreases the number of tokens, and preserves positivity. At termination every weight occurs at most once. The terminal positive integer lies between \(1\) and \(M\), and is divisible by \(M\), so it must equal \(M\), using exactly \(r\) tokens. Therefore \(s\ge r\). In particular every multiple of \(M^k\) has at least \(r\) binary ones.

**2. Lifting a sparse multiple through arbitrary powers.** Set \(A=2^r=1+M\) and, for \(t\ge0\), set \(H(t)=(A^t-1)/M\in\mathbb Z\). For every prime \(p\mid M\) and integers \(a>b\ge0\), the odd-prime lifting-the-exponent lemma gives
\[
\nu_p(H(a)-H(b))=\nu_p(a-b).
\]
Consequently for every \(s\ge1\), the map \(t\mapsto H(t)\) induces an injective, hence bijective, function on \(\mathbb Z/M^s\mathbb Z\) (periodicity and injectivity follow prime by prime). For \(k=1\), take \(t=0\). For \(k\ge2\), choose the unique residue \(t\pmod {M^{k-1}}\) satisfying \(H(t)\equiv-2^{-1}\pmod {M^{k-1}}\), and choose its nonnegative representative. Define
\[
N=1+2^{1+rt}+\sum_{j=2}^{r-1}2^j
 =M+2(A^t-1)=M(1+2H(t)).
\]
The finite sum is empty when \(r=2\). By construction \(M^k\mid N\). The exponents \(0,1+rt,2,\ldots,r-1\) are pairwise distinct; hence \(s_2(N)=r\). Together with Step 1 this proves the minimum, uniformly in \(r,k\).

**3. Exact power of two in the fixed divisor.** Legendre's formula implies for every positive \(n\),
\[
\nu_2\binom{2n}{n}
=2s_2(n)-s_2(2n)=s_2(n).
\]
Since all \(n\) divisible by \(M^k\) have at least \(r\) ones, every central binomial coefficient in the claimed gcd is divisible by \(2^r\). Step 2 constructs an index \(n=N\) divisible by \(M^k\) at which the valuation is exactly \(r\).

**4. Exclusion of every odd prime.** Fix any odd prime \(p\), and write \(m=M^k=p^e u\) with \(e\ge0\) and \(p\nmid u\). If \(u=1\), take \(n=p^e\). Otherwise let \(h\) be the multiplicative order of \(p\) modulo \(u\) and put
\[
n=p^e\sum_{j=0}^{u-1}p^{jh}.
\]
Every term in the sum is \(1\pmod u\), so \(u\mid n/p^e\), whence \(m\mid n\). All digits of \(n\) in base \(p\) are either zero or one, at distinct positions. Adding \(n\) to itself in base \(p\) causes no carry because \(p\ge3\). By Kummer's theorem (or Legendre's digit formula), \(p\nmid\binom{2n}{n}\). As \(p\) was arbitrary, no odd prime divides the infinite gcd. Step 3 now proves that the gcd is exactly \(2^r\).

## Verification
The standalone `verify_mersenne_power.py` checks the lifting algorithm by modular exponentiation for \(23\) combinations of \((r,k)\), including nonprime Mersenne bases, and directly materializes moderate-size sparse witnesses. It tests independent odd-prime zero-carry witnesses, finite initial portions of every claimed lower bound, and the Legendre carry identity on manageable integers. Invoke `python verify_mersenne_power.py` with Python 3.8 or later. Its successful summary begins `VERIFY_OK`. The test set is finite and does not certify any unrestricted quantifier; these follow from the four proof steps.

## Relationship to prior work
The sequence of minimum binary weights of positive multiples is OEIS A086342; its 2013 comment states the \(k=1\) identity for \(2^r-1\), so that base case is not claimed to be new. Elsholtz (2016, §§2–3 and the proof of Theorem 5) studies sparse multiples of primes and Mersenne divisors, rather than uniform exact weight for **every power** of a Mersenne number. The Lucas–Kummer literature supplies the classical binomial valuations. Clokie–Lidbetter–Molina Lovett–Shallit–Witzman (2020, §§2–4) give general algorithms and sturdy-number criteria; their inspected statements do not provide the power-stability formula. The novelty claim is limited to the simultaneous exact power-stability and resulting fixed-divisor identity, not to these background ingredients. Broader unpublished or unlocated coverage is possible.

## Limitations
This does not determine the least *size* of a sparse multiple, enumerate all minimal-weight multiples, or give the analogous formula for arbitrary odd moduli. The gcd statement is a consequence of the sparse-multiple theorem plus classical valuation formulas. Computational samples are illustrative, not proofs. Priority remains subject to comprehensive historical review; independent validation has not been performed.

## References
1. OEIS Foundation, *A086342: Smallest number of 1's in binary expansion of any positive multiple of n*; first created September 2, 2003, Mersenne base case comment May 1, 2013. https://oeis.org/A086342
2. C. Elsholtz, *Almost all primes have a multiple of small Hamming weight*, arXiv:1602.05974v1 (February 18, 2016), §§2–3. https://arxiv.org/abs/1602.05974
3. R. Meštrović, *Lucas' theorem: its generalizations, extensions and applications (1878–2014)*, arXiv:1409.3820v1 (September 6, 2014). https://arxiv.org/abs/1409.3820
4. T. Clokie, T. F. Lidbetter, A. Molina Lovett, J. Shallit, and L. Witzman, *Computational Aspects of Sturdy and Flimsy Numbers*, arXiv:2002.02731v1 (February 7, 2020), §§2–4. https://arxiv.org/abs/2002.02731
