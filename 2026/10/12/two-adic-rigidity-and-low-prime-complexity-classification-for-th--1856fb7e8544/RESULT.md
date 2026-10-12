# Two-adic rigidity and low-prime-complexity classification for the derivative of an aliquot sum

## Finding
Let \(\sigma(n)\) denote the ordinary sum of positive divisors and \(S(n)=\sigma(n)-n\) the sum of proper positive divisors. Let \(D\) be the arithmetic derivative, defined by \(D(p)=1\) for each prime and \(D(uv)=uD(v)+vD(u)\). Write \(\Omega(m)\) for the number of prime factors of \(m\), counted with multiplicity, and \(\nu_2(m)\) for its exponent of \(2\).

**Theorem.** For every integer \(a\ge2\) and odd prime \(p\), put \(n=2^a p\). Whenever
\[
D(S(n))=n,
\]
necessarily \(\nu_2(S(n))=2\). Writing \(m=S(n)/4\), the number \(\Omega(m)\) is even if \(a=2\) and odd if \(a\ge3\). Moreover, all the solutions for which \(\Omega(m)\le2\) are exactly
\[
 n=284,
\]
and, for integers \(a\ge3\),
\[
n=2^a(2^{a+1}+3)
\]
provided **both** the integers
\[
p_a=2^{a+1}+3,\qquad q_a=2^{2a-1}+3\cdot2^{a-2}-1
\]
are prime. This condition on the two numbers is necessary and sufficient, not a claim that infinitely many such exponents exist. For instance, \(a=3,11,15\) give \(n=152,8394752,2147581952\), respectively.

## Assumptions and scope
All numbers are ordinary positive integers; \(a\ge2\), and \(p\ge3\) is an odd prime. The classification concerns the solutions of the fixed-point equation \(D(\sigma(n)-n)=n\) *with* \(\Omega((\sigma(n)-n)/4)\le2\); the quotient is defined only after the theorem forces the \(2\)-adic valuation. The \(2\)-adic and parity conclusions apply to every fixed-point solution in this entire two-prime-support domain, without an upper bound on \(\Omega\). The result makes no assertion about other prime supports, the case \(a=1\), or infinitude of the paired-prime family.

## Proof
Put \(t=2^a\ge4\). Multiplicativity of \(\sigma\) and \(\sigma(t)=2t-1\) yield
\[
S(n)=(t-1)p+2t-1,\qquad n=tp.
\]
The first expression is even because \(t-1\) and \(p\) are odd. If \(\nu_2(S)=1\), writing \(S=2v\) with \(v\) odd gives \(D(S)=v+2D(v)\) odd, contradicting the even value \(n\). If \(\nu_2(S)=e\ge3\), the arithmetic-derivative identity
\[
\frac{D(S)}S=\sum_{r^j\parallel S}\frac{j}{r}
\]
gives \(D(S)/S\ge e/2\ge3/2\). Yet \(S/n>(t-1)/t\ge3/4\), so \(D(S)>9n/8>n\), another contradiction. Therefore \(\nu_2(S)=2\).

Write \(S=4m\) with \(m\) odd. Since \(D(4)=4\), the fixed-point identity implies
\[
4m+4D(m)=tp.
\]
Eliminating \(p\) using the formula for \(S\) yields the *exact pair of identities*
\[
p=4D(m)+2t-1,\qquad m-(t-1)D(m)=\frac{t(2t-1)}4=:K.
\]
For odd \(m=\prod r^j\), \(D(m)=\sum j(m/r)\), so \(D(m)\equiv\sum j=\Omega(m)\pmod2\). Since \(t-1\) and \(m\) are odd, the second identity shows \(\Omega(m)\equiv1-K\pmod2\). When \(a=2\), \(K=7\) is odd; when \(a\ge3\), \(K=2^{a-2}(2^{a+1}-1)\) is even. This proves the asserted parity separation.

Now assume \(\Omega(m)\le2\). Since \(m\) is odd and \(S\ge16\), necessarily \(m>1\). For \(a\ge3\), the parity condition gives \(\Omega(m)=1\), hence \(m=q\) prime and \(D(m)=1\). Substitution into the exact identities gives
\[
p=2t+3,\qquad q=\frac{t(2t-1)}4+t-1
=2^{2a-1}+3\cdot2^{a-2}-1.
\]
Thus both \(p\) and \(q\) must be prime. Conversely, for any \(a\ge3\) with both expressions prime, the two displayed identities imply \(S(2^ap)=4q\), and therefore \(D(S)=D(4q)=4(q+1)=2^ap\).

For \(a=2\), parity and \(\Omega(m)\le2\) force \(\Omega(m)=2\). Write \(m=rs\) for odd primes \(3\le r\le s\), possibly equal, so \(D(m)=r+s\). Now \(t=4\), \(K=7\), and the identity \(m-3D(m)=7\) is equivalent to
\[
(r-3)(s-3)=16.
\]
Both positive factors must be even, so with \(r\le s\) the only possibilities are \((r,s)=(5,11)\) and \((7,7)\). The formula \(p=4(r+s)+7\) gives \(p=71\) in the first case and \(p=63\) in the second; the latter is not prime. The first gives \(n=4\cdot71=284\), \(S(n)=220=4\cdot55\), and \(D(220)=284\). This proves necessity and sufficiency in every case. \(\square\)

## Verification
The accompanying standalone standard-library program `verify.py` independently computes the prime factorizations and arithmetic derivatives for all \(n=2^ap\) with \(2\le a\le10\) and odd prime \(3\le p\le3000\), checking the parity obstruction and the stated equivalence at low prime complexity. It tests the paired-prime family for \(3\le a\le18\), within a deterministic \(64\)-bit primality-test range, and checks \(n=284\). It reports `CHECK_OK tested_prime_pairs=3861 fixed_points=2 low_odd_support=2 family=[(3, 152, 19, 37), (11, 8394752, 4099, 2098687), (15, 2147581952, 65539, 536895487)] exceptional=284`. This finite check supports reproducibility but is not used to prove the unbounded assertion, which follows entirely from the preceding algebra.

## Relationship to prior work
OEIS A248816 (first entry dated October 15, 2014) asks for and lists integers satisfying \(D(\sigma(n)-n)=n\), including the early values just identified, without stating this two-adic obstruction or unbounded small-\(\Omega\) classification. OEIS A125246 separately records the well-known deficient-by-four integers \(2^a(2^{a+1}+3)\) and their prime condition; the algebraic *shape* of this family is prior art. The new restriction is the necessity of the additional prime \(q_a\) for the derivative equation, together with an exhaustive converse when the odd aliquot quotient has at most two prime factors. OEIS A003415 gives standard arithmetic-derivative identities. Nearby database entries A248815 and A230164 consider other compositions with Euler's totient or the full divisor sum and do not imply this classification.

## Limitations
This is a precise conditional classification, not a solution of the full OEIS A248816 sequence. Higher values of \(\Omega(m)\), the case \(a=1\), more than two distinct prime factors of \(n\), and whether there are infinitely many simultaneous primes \((p_a,q_a)\) are unresolved here. An earlier unindexed argument could establish some or all of the statements; the known deficient-by-four family is not asserted to be new. Self-review is not independent mathematical validation.

## References
- OEIS Foundation, **A248816**, "Numbers that are equal to arithmetic derivative of sum of aliquot parts," https://oeis.org/A248816 (record originating October 15, 2014).
- OEIS Foundation, **A125246**, "Numbers that are deficient by 4," https://oeis.org/A125246 (records the prime-shaped family).
- OEIS Foundation, **A003415**, "Arithmetic derivative of n," https://oeis.org/A003415.
- OEIS Foundation, **A248815**, https://oeis.org/A248815 (comparison with derivative of Euler totient).
- OEIS Foundation, **A230164**, https://oeis.org/A230164 (comparison involving the ordinary divisor sum).
