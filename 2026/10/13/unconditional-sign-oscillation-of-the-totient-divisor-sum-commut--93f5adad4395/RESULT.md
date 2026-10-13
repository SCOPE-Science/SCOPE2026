# Unconditional sign oscillation of the totient–divisor-sum commutator on powers of two

## Finding
Write \(\varphi(n)\) for Euler's totient and \(\sigma(n)\) for the sum of the positive divisors of \(n\), and define
\[
C(n)=\sigma(\varphi(n))-\varphi(\sigma(n)).
\]
For every integer \(k\ge 2\), the following assertions hold:

1. If \(k\) is prime, then \(C(2^{k-1})<0\).
2. If \(12\mid k\), then \(C(2^{k-1})>0\).
3. The first positive value among the powers of two is \(C(2048)=319\); explicitly, \(C(2^{k-1})<0\) for \(2\le k\le 11\).

In particular, both signs occur infinitely often even when \(n\) is restricted to powers of two. Among exponent indices \(2\le k\le X\), there are at least \(\pi(X)\) negative instances and at least \(\lfloor X/12\rfloor\) positive instances, where \(\pi\) counts primes. The negative assertion does not assume that infinitely many Mersenne numbers are prime.

## Assumptions and scope
All integers are positive unless otherwise specified. A prime index means an ordinary prime \(k\ge2\); it does **not** mean that \(2^k-1\) is prime. No hypothesis about unproved prime families is imposed. The theorem makes no assertion classifying the sign at every composite index, and does not concern the density of signs over all positive integers.

## Proof
**Reduction.** Put \(M_k=2^k-1\). If \(k\ge2\), then \(\varphi(2^{k-1})=2^{k-2}\) and \(\sigma(2^{k-2})=2^{k-1}-1\), while \(\sigma(2^{k-1})=M_k\). Consequently
\[
C(2^{k-1})=\frac{M_k-1}{2}-\varphi(M_k). \tag{1}
\]

**All prime indices give a negative sign.** For \(k=2\), \(M_k=3\) and \(C(2)=1-2=-1\). Let \(k\ge3\) be an odd prime. Every prime \(q\) dividing \(M_k\) has multiplicative order \(k\) for \(2\) modulo \(q\), since the order divides the prime \(k\) but cannot be \(1\). Hence \(k\mid q-1\). Since \(q\) is odd and \(k\) is odd, \(2k\mid q-1\), giving \(q\ge2k+1\).

Let \(t\) be the number of distinct prime factors of \(M_k\). If \(t\ge k\), then
\[
M_k\ge(2k+1)^k>2^k>M_k,
\]
a contradiction; therefore \(t\le k-1\). Using the elementary inequality \(\prod_{i=1}^t(1-u_i)\ge1-\sum_{i=1}^t u_i\) for \(0\le u_i\le1\),
\[
\frac{\varphi(M_k)}{M_k}
 =\prod_{q\mid M_k}\left(1-\frac1q\right)
 \ge1-\sum_{q\mid M_k}\frac1q
 \ge1-\frac{k-1}{2k+1}
 =\frac{k+2}{2k+1}>\frac12.
\]
Thus \(\varphi(M_k)>M_k/2>(M_k-1)/2\), proving the negative sign by (1).

**Every twelfth index gives a positive sign.** Since
\[
M_{12}=4095=3^2\cdot5\cdot7\cdot13,
\qquad\frac{\varphi(4095)}{4095}=\frac{1728}{4095}=\frac{192}{455}<\frac12,
\]
and \(M_{12}\mid M_k\) whenever \(12\mid k\), the prime-divisor product formula for \(\varphi\) yields
\[
\frac{\varphi(M_k)}{M_k}\le\frac{192}{455}.
\]
For such \(k\), \(M_k\ge4095\). Substitution into (1) gives
\[
C(2^{k-1})\ge\frac{M_k-1}{2}-\frac{192M_k}{455}
=\frac{71M_k-455}{910}>0.
\]
This argument also gives \(C(2048)=(4095-1)/2-1728=319\).

**The first positive power.** It remains to exclude the composite indices \(k\in\{4,6,8,9,10\}\) below \(12\), since the other indices between \(2\) and \(11\) are prime. The following exact values follow from the displayed prime factors of each \(M_k\):

| \(k\) | \(M_k\) | \(\varphi(M_k)\) | \((M_k-1)/2\) |
| ---: | ---: | ---: | ---: |
| 4 | 15 | 8 | 7 |
| 6 | 63 | 36 | 31 |
| 8 | 255 | 128 | 127 |
| 9 | 511 | 432 | 255 |
| 10 | 1023 | 600 | 511 |

In each row the totient exceeds the half-difference, so (1) is negative. Finally, Euclid's theorem supplies infinitely many prime \(k\), and the multiples of \(12\) are infinite. This proves every assertion.

## Verification
The bundled `verify.py` recomputes \(\varphi\) and \(\sigma\) directly from prime-power factorizations for \(2\le k\le36\), checks the formula (1) and both indicated sign conditions, checks that \(k=12\) is the first positive index, and checks \(C(2048)=319\). Execute `python3 verify.py` in the directory containing this document and the script. Expected output:

```
VERIFY_OK k=2..36 positive_indices= [12, 20, 24, 28, 30, 36] first_positive_n=2048 C_2048=319 prime_indices_negative= 11
```

The unrestricted assertions are proved by the inequalities above; the finite script is a corroboration, not a substitute for the proof.

## Relationship to prior work
Golomb's 1993 work posed and studied the sign question for \(\sigma\circ\varphi-\varphi\circ\sigma\), including a negative-sign construction on powers of two **assuming** infinitely many Mersenne primes. De Koninck and Luca (2007) proved quantitative order and density statements for the quotient \(\sigma(\varphi(n))/\varphi(\sigma(n))\) across unrestricted integers. Those results do not assert sign oscillation inside the sparse geometric subsequence of powers of two, nor the prime-index and divisible-by-twelve rules. OEIS A065395 records the unrestricted commutator, while A116083 records the separate exact difference-one condition. The present theorem gives explicit unconditional infinite subfamilies of both signs within the same sparse subsequence; it does not claim novelty of the global sign-oscillation fact itself.

## Limitations
No complete sign classification of all \(C(2^{k-1})\) is claimed; in particular, some composite indices not divisible by \(12\) are positive. The proof makes no claim about infinitely many Mersenne primes or any density among all integers. Although exact primary statements and published records were compared, earlier unindexed elementary observations may exist. The accompanying finite verification is not an independent mathematical audit of the unrestricted argument.

## References
1. S. W. Golomb, “Equality among number-theoretic functions,” *Abstracts of the American Mathematical Society* **14** (1993), 415–416, abstract 882-11-16. AMS presentation listed for 23 May 1993: https://www.ams.org/meetings/sectional/1882_progfull.html . Scanned manuscript, §4: https://oeis.org/A006872/a006872_1.pdf .
2. J.-M. De Koninck and F. Luca, “On the composition of the Euler function and the sum of divisors function,” *Colloquium Mathematicum* **108** (2007), 31–51, https://doi.org/10.4064/cm108-1-4 ; open full text: https://www.impan.pl/shop/en/publication/transaction/download/product/87236 .
3. OEIS A065395, “Commutator of sigma and phi functions,” originally entered 5 November 2001, https://oeis.org/A065395 .
4. OEIS A116083, “Numbers \(n\) such that \(\varphi(\sigma(n))-\sigma(\varphi(n))=1\),” https://oeis.org/A116083 .
