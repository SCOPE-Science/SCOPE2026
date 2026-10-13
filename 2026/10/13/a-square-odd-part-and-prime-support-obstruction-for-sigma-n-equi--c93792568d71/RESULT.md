# A square-odd-part and prime-support obstruction for \(\sigma(n)\equiv5\pmod n\)

## Finding

Let \(\sigma(n)=\sum_{d\mid n}d\), and let \(\omega(n)\) denote the number of distinct prime divisors of \(n\). For every integer \(n>5\) satisfying
\[
\sigma(n)\equiv5\pmod n,
\]
we have \(\omega(n)\ge3\). Moreover, if \(n\) is odd then \(\omega(n)\ge4\), while if \(n\) is even its odd part is a perfect square. Thus, in the smallest permitted support case, any solution must have the form
\[
n=2^a p^{2b}q^{2c},\qquad a,b,c\ge1,\quad 2<p<q\text{ prime}.
\]
No assertion is made that such a solution exists.

## Assumptions and scope

The lower bound \(n>5\) is essential: it makes residue \(5\) the actual least nonnegative remainder. In particular, small integers such as \(n=2\) can satisfy the congruence without having remainder \(5\). Throughout, exponents of prime factors are positive integers. The term *odd part* means \(n/2^{v_2(n)}\), and the result applies to arbitrarily large exponents and prime factors.

## Proof

Write \(\sigma(n)=kn+5\) with integer \(k\ge1\), since \(n>5\) and \(\sigma(n)>n\). If \(n\) is composite with at least two distinct prime divisors \(p<q\), the proper divisors \(1,p,q\) show \(\sigma(n)-n\ge1+p+q\ge6>5\); hence \(k\ne1\), and thus \(k\ge2\). For three distinct odd prime divisors \(p<q<r\), the stronger lower bound is \(\sigma(n)-n\ge1+p+q+r\ge16\).

**One prime divisor.** If \(n=p^e\), the congruence modulo \(p\) gives \(1\equiv5\pmod p\), so \(p\mid4\) and \(p=2\). But for \(n=2^e>5\), one has \(\sigma(n)=2n-1\) and \(\sigma(n)\bmod n=n-1\ne5\). This rules out all prime powers.

**Two odd prime divisors.** Suppose \(n=p^a q^b\) with odd primes \(3\le p<q\). The geometric-series bound gives
\[
\frac{\sigma(n)}n<\frac{p}{p-1}\frac{q}{q-1}\le\frac32\frac54=\frac{15}{8}<2.
\]
But \(k\ge2\), whereas \(\sigma(n)/n=k+5/n>2\). This is impossible.

**One odd prime divisor and \(2\).** Let \(n=2^a p^b\), with \(a,b\ge1\) and \(p\) odd. Since \(kn+5\) is odd, \(\sigma(n)\) is odd. Multiplicativity of \(\sigma\), together with oddness of \(\sigma(2^a)\), forces \(b\) to be even, so \(b\ge2\). Also
\[
\frac{\sigma(n)}n<2\frac p{p-1}\le3,
\]
so \(k\ge2\) implies \(k=2\). Put \(t=2^{a+1}\) and \(S=1+p+\cdots+p^{b-1}\). Rewriting
\[
(t-1)(1+p+\cdots+p^b)=tp^b+5
\]
yields the exact integer equation
\[
(t-p)S=6.
\]
Because \(S\ge p+1\), only \(p=3\) or \(p=5\) are possible. At \(p=3\), even \(b\ge2\) gives \(S=4\) when \(b=2\), and \(S>6\) when \(b\ge4\); neither divides \(6\). At \(p=5\), \(S=6\) only for \(b=2\), forcing \(t=p+1=6\), not a power of \(2\). Hence the two-prime even case is impossible.

**Three odd prime divisors.** Let \(n=p^a q^b r^c\), with odd primes \(3\le p<q<r\). Since
\[
\frac{\sigma(n)}n<\frac p{p-1}\frac q{q-1}\frac r{r-1}\le\frac32\frac54\frac76=\frac{35}{16}<3,
\]
we have \(k=2\). Hence \(\sigma(n)=2n+5\) is odd. Every exponent of an odd-prime power in \(n\) must therefore be even. The same ratio bound then forces \(p=3\): otherwise the ratio is at most \((5/4)(7/6)(11/10)<2\). Next it forces \(q=5\): otherwise the ratio is at most \((3/2)(7/6)(11/10)<2\). Finally \((3/2)(5/4)r/(r-1)>2\) implies \(r<16\), so \(r\in\{7,11,13\}\).

If \(r=7\) or \(r=13\), both \(3\) and \(r\) have multiplicative order \(4\) modulo \(5\). Their geometric sums with even exponents (hence odd numbers of terms) are nonzero modulo \(5\). The factor \(\sigma(5^b)\) is \(1\) modulo \(5\), whence \(\sigma(n)\not\equiv0\pmod5\), contradicting \(\sigma(n)=2n+5\) and \(5\mid n\). If \(r=11\), then \(5\equiv11\equiv-1\pmod3\); their even-exponent geometric sums and \(\sigma(3^a)\) are all \(1\) modulo \(3\). Thus \(\sigma(n)\equiv1\pmod3\), contradicting \(2n+5\equiv2\pmod3\). Therefore no odd solution has three distinct prime divisors.

Finally, whenever \(n\) is even, \(kn+5\) is odd, so \(\sigma(n)\) is odd. Since for every odd prime \(p\), \(\sigma(p^e)\) is odd exactly when \(e\) is even, the odd part of \(n\) must be a perfect square. Combining the proved exclusions gives all conclusions.

## Verification

The proof is unrestricted and uses no finite enumeration of candidate integers. Running `python3 verify.py` with Python 3 and only its standard library computes exact divisor sums for \(6\le n\le10^6\), checks the absence of a remainder-\(5\) witness in this finite range, verifies strict rational ratio thresholds, and cross-checks \(1064\) local even-power identities. Its finite checks corroborate but cannot replace the congruence proof above.

## Relationship to prior work

Pomerance's 1975 investigation introduces the general congruences \(\sigma(n)\equiv a\pmod n\) and notes that \(1\) and \(2\) are the only then-known members for \(a=5\), with no asserted complete classification. Anavi–Pollack–Pomerance give an asymptotic sparsity theorem for sporadic solutions, not the prime-support and square-odd-part exclusions here. OEIS A076495 asks for the least number with a prescribed *actual remainder* and records the five-remainder entry as conjecturally absent. Neither the conjectural absence nor computational non-detection proves this theorem; the present conclusions follow from the exact inequalities and congruences above.

## Limitations

This result does not prove that the remainder \(5\) is never attained. It does not classify solutions with at least four odd prime supports or even solutions with at least two odd-prime supports. It does not establish existence for the necessary even forms.

## References

1. C. Pomerance, *On the congruences \(\sigma(n)\equiv a\pmod n\) and \(n\equiv a\pmod{\varphi(n)}\)*, Acta Arithmetica 26 (1975), 265–272, DOI: 10.4064/aa-26-3-265-272. Author-hosted full text: https://math.dartmouth.edu/~carlp/PDF/paper7.pdf .
2. A. Anavi, P. Pollack, C. Pomerance, *On congruences of the form \(\sigma(n)\equiv a\pmod n\)*, International Journal of Number Theory 9 (2013), 115–124, DOI: 10.1142/S1793042112501266. Author-hosted full text: https://math.dartmouth.edu/~carlp/sigmacongruence.pdf .
3. OEIS A076495, *Smallest x such that sigma(x) mod x = n*, original entry dated 2002-10-21, https://oeis.org/A076495 .
