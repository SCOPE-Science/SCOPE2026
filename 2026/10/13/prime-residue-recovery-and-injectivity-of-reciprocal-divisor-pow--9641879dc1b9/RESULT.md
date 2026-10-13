# Prime-residue recovery and injectivity of reciprocal divisor-power sums

## Finding
For a positive integer \(k\) define \(\sigma_k(n)=\sum_{d\mid n}d^k\), \(\tau(n)=\#\{d:d\mid n\}\), and \(R_k(n)=\sigma_k(n)/n^k=\sum_{d\mid n}d^{-k}\). Fix **any even** \(k\ge2\), and write \(t=\nu_2(k)\).

**Theorem.** If \(n\ge1\) has \(\tau(n)\) a power of two, then every odd prime dividing \(\sigma_k(n)\) is congruent to \(1\pmod{2^{t+1}}\). Let \(B_k(n)\) denote the positive denominator of \(R_k(n)\) in lowest terms. For every odd prime \(q\) satisfying \(\nu_2(q-1)\le t\), one has
\[
\nu_q(B_k(n))=k\nu_q(n).
\]
In particular, \(R_k\), and also its fractional part, is injective on the infinite class
\[
\mathcal F_k=\{n\ge1:\tau(n)\text{ is a power of }2,\ \nu_2(q-1)\le\nu_2(k)\text{ for every odd prime }q\mid n\}.
\]
This includes even integers. There is no fixed limit on prime support or on permitted powers \(2^s-1\) of prime factors.

## Assumptions and scope
Here \(\nu_q(z)\) is the exponent of a prime \(q\) in an integer \(z>0\). The phrase '\(\tau(n)\) is a power of two' permits \(\tau(1)=1\) and means that each nonzero prime-power exponent in \(n\) is \(2^s-1\), for some integer \(s\ge1\). The parameter \(k\) is a fixed **even positive integer**, not a varying prime and not a real exponent. The auxiliary prime-residue condition restricts odd prime factors but does not restrict the factor \(2\), which is recovered separately.

## Proof
Write \(k=2^t u\) with \(u\) odd and \(t\ge1\). If \(p^{2^s-1}\parallel n\), the geometric-series factorization gives the exact integer identity
\[
\sigma_k(p^{2^s-1})=\sum_{h=0}^{2^s-1}p^{kh}=\prod_{j=0}^{s-1}\bigl(p^{k2^j}+1\bigr).
\]
It is valid also for \(p=2\). Suppose an odd prime \(\ell\) divides one factor \(p^{k2^j}+1\). Then \(\ell\nmid p\) and \(p^{2^{t+j}u}\equiv-1\pmod\ell\). Let \(h\) be the multiplicative order of \(p\) modulo \(\ell\). Since \(h\mid2^{t+j+1}u\) while \(h\nmid2^{t+j}u\), it follows that \(\nu_2(h)=t+j+1\). The group order \(\ell-1\) is divisible by \(h\); thus \(2^{t+1}\mid\ell-1\). Multiplicativity of \(\sigma_k\) proves the first assertion, including the case \(n=1\) where its numerator is one.

If \(q\) is odd and \(\nu_2(q-1)\le t\), the preceding assertion yields \(q\nmid\sigma_k(n)\). Hence cancelling the fraction \(\sigma_k(n)/n^k\) removes no factor of \(q\) from its denominator, and \(\nu_q(B_k(n))=k\nu_q(n)\). This statement includes \(q\nmid n\), when both valuations are zero.

Now take \(n,m\in\mathcal F_k\) with \(R_k(n)=R_k(m)\). The reduced denominators agree. By the valuation formula, \(\nu_q(n)=\nu_q(m)\) for all allowed odd primes \(q\); because **every odd prime factor** of either integer is allowed, the odd parts of \(n\) and \(m\) coincide, say \(n=2^a v\) and \(m=2^b v\), where \(v\) is odd and \(a,b\ge0\). By multiplicativity,
\[
R_k(2^a v)=R_k(v)\sum_{j=0}^{a}2^{-kj}.
\]
The finite sum strictly increases with \(a\), and \(R_k(v)>0\), so equality implies \(a=b\) and therefore \(n=m\).

Finally \(1\le R_k(n)<2\) for all \(n\ge1\) and \(k\ge2\): every summand beyond the first is at most \(j^{-2}\) for some integer \(j\ge2\), while \(\sum_{j=2}^{\infty}j^{-2}<\sum_{j=2}^{\infty}[j(j-1)]^{-1}=1\). Hence equality of fractional parts of \(R_k(n)\) is equivalent to equality of the numbers themselves, proving the last assertion.

## Verification
The included file `VERIFY.py` uses only Python's standard library. Run `python VERIFY.py`. For each \(k\in\{2,4,6,8,12\}\) and every \(1\le n\le30000\) with power-of-two divisor count, it evaluates \(\sigma_k(n)\) exactly, tests numerator exclusions against all forbidden odd primes through \(1000\), checks the reduced-denominator valuation formula for each odd prime factor, and confirms distinct reduced fractions on \(\mathcal F_k\). These **finite** checks corroborate, but do not replace, the proof for every integer.

Observed counts by \(k=2,4,6,8,12\), respectively: all eligible numbers \(20647\) each; members of \(\mathcal F_k\) \(6830,14670,6830,17318,14670\), with the same respective numbers of distinct reduced fractions. Direct boundary tests check \(\sigma_2(63)\equiv0\pmod 7\) when the divisor-count condition is dropped and \(\sigma_2(15)\equiv0\pmod5\) when the protected-residue condition is dropped.

## Relationship to prior work
The arithmetic functions \(\sigma_k\) and \(\sigma_{-k}=R_k\) are classical. Defant (2015, arXiv:1506.05432) studies the density and gaps of the **range** of generalized divisor sums; its theorems do not establish injectivity on prime-restricted domains. Zhi-Wei Sun's conjecture, recorded in OEIS A001157 on 2015-10-15, asks for distinct fractional parts of \(\sigma_k(n)/n^k\) for all positive integers when \(k\ge2\). The theorem establishes this for the specific infinite class \(\mathcal F_k\) for every even \(k\), and strengthens it to an exact prime-valuation recovery formula. OEIS A017667 and A017668 tabulate the reduced numerators and denominators for \(k=2\), but the inspected statements do not provide the asserted general valuation/injectivity theorem.

The order-based observation is elementary; no claim is made that related observations have never appeared in unindexed literature. The unrestricted conjecture, even for \(k=2\), is **not** resolved.

## Limitations
The proof requires even \(k\), a power-of-two divisor count, and the stated residue condition on **odd** prime factors for the injectivity conclusion. Outside these restrictions numerator and denominator prime factors may cancel; no conclusion of noninjectivity follows. It is unknown whether the exact family here is maximal. The finite verifier and primary-literature comparisons do not constitute exhaustive novelty certification or independent review.

## References
1. C. Defant, *On the Density of Ranges of Generalized Divisor Functions*, arXiv:1506.05432, first posted 2015-06-17, https://arxiv.org/html/1506.05432v1.
2. OEIS A001157, *Sum of squares of divisors of n*, comment by Zhi-Wei Sun, 2015-10-15, https://oeis.org/A001157.
3. OEIS A017667 and A017668, *Numerator/denominator of sum of reciprocal squares of divisors*, https://oeis.org/A017667 and https://oeis.org/A017668.
