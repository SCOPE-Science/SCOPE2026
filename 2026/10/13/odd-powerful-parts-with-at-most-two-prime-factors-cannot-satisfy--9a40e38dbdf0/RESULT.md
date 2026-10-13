# Odd powerful parts with at most two prime factors cannot satisfy the nonunitary Euler divisor equation
## Finding
For each positive integer \(m\), let \(\varphi^{\#}(m)\) count integers \(1\le j\le m\) divisible by none of the nonunitary divisors of \(m\), where a divisor \(d\mid m\) is nonunitary when \(\gcd(d,m/d)>1\).

Write \(n=s t\), where \(s\) is the product of prime divisors of \(n\) occurring to exponent exactly one and \(t\) is the product of the remaining prime-power blocks, all having exponents at least two. Then \(s\) is squarefree, \(t\) is powerful, and \(\gcd(s,t)=1\).

**Theorem.** No integer \(n>1\) satisfying
\[
\sum_{\substack{d\mid n\\\gcd(d,n/d)>1}}\varphi^{\#}(d)=n
\tag{1}
\]
has \(t\) odd with at most two distinct prime factors. Consequently, any counterexample to the Ligh--Wall conjecture that the powerful part of every solution is even must have at least three distinct odd primes dividing \(t\).

The sharp analytic ingredient is: if \(t>1\) is odd and powerful with at most two distinct prime factors, then
\[
0<\frac{B(t)}t\le\frac{113}{225},
\qquad
B(t)=\prod_{p^a\parallel t}(1+p^a)-\prod_{p^a\parallel t}(1+p^a-p^{a-1}).
\tag{2}
\]
Equality holds precisely for \(t=3^2 5^2=225\).

## Assumptions and scope
The definition of \(\varphi^{\#}\) and the identity reducing (1) to
\[
\sigma(s)B(t)=st
\tag{3}
\]
are those of Ligh and Wall (1987), Theorem 5. Here \(\sigma(s)=\sum_{d\mid s}d\) and \(\omega(t)\) denotes the number of distinct prime divisors of \(t\). An empty prime product equals \(1\), and \(B(1)=0\).

The theorem excludes the complete odd-powerful stratum \(\omega(t)\le2\). It does not prove the unrestricted Ligh--Wall conjecture for \(\omega(t)\ge3\), nor does it assert the existence of a counterexample.

## Proof
**Reduction.** For a prime power, the nonunitary Euler function satisfies
\[
\varphi^{\#}(p)=p,\qquad
\varphi^{\#}(p^a)=p^a-p^{a-1}\quad(a\ge2).
\]
It is multiplicative. The sum of \(\varphi^{\#}\) over all divisors equals the unitary divisor sum \(\sigma^*(n)=\prod_{p^a\parallel n}(1+p^a)\). The sum over unitary divisors equals \(\prod_{p^a\parallel n}(1+\varphi^{\#}(p^a))\). Subtracting the unitary contribution from the all-divisor sum and separating the exponent-one and higher-exponent blocks yields (3). This also directly reconstructs Ligh--Wall Theorem 5.

Suppose henceforth \(t>1\) is odd and powerful with \(\omega(t)\le2\). Both products in \(B(t)\) have opposite parity: \(1+p^a\) is even, while \(1+p^a-p^{a-1}\) is odd. Thus \(B(t)\) and \(t\) are odd.

**Sharp ratio bound.** If \(t=p^a\) with odd prime \(p\) and \(a\ge2\), then \(B(t)=p^{a-1}\) and \(B(t)/t=1/p\le1/3\).

If \(t=p^a q^b\), with \(3\le p<q\) prime and \(a,b\ge2\), write \(x=p^{a-1}\ge p\) and \(y=q^{b-1}\ge q\). Expanding the products gives
\[
B(t)=xy(p+q-1)+x+y,
\]
and therefore
\[
\frac{B(t)}t=
\frac1p+\frac1q-\frac1{pq}+\frac1{pqx}+\frac1{pqy}
\le f(p,q):=
\frac1p+\frac1q-\frac1{pq}+\frac1{p^2q}+\frac1{pq^2}.
\]
For fixed \(q\ge5\),
\[
f(p,q)=\frac1q+\frac{1-1/q+1/q^2}{p}+\frac1{p^2q}
\]
strictly decreases with \(p\). By symmetry, for fixed \(p\ge3\), it strictly decreases with \(q\). Therefore
\[
\frac{B(t)}t\le f(3,5)=\frac{113}{225}.
\]
Equality requires \(p=3,q=5,x=p,y=q\), equivalently \(t=3^2 5^2=225\). This also exceeds the one-prime bound, proving (2) sharply.

**Parity rigidity of the squarefree part.** If (1) holds, (3) gives
\[
\frac{B(t)}t=\frac{s}{\sigma(s)}.
\tag{4}
\]
Since \(B(t),t\) are odd, the exact equality \(\sigma(s)B(t)=st\) forces \(\nu_2(\sigma(s))=\nu_2(s)\). For squarefree \(s\), if \(s\) is odd, every prime \(r\mid s\) contributes an even factor \(r+1\) to \(\sigma(s)\), so \(s=1\). If \(s\) is even, write \(s=2v\) with odd squarefree \(v\). Then
\[
\sigma(s)=3\prod_{r\mid v}(r+1),
\]
and \(\nu_2(\sigma(s))=1\) requires \(v\) to consist of one odd prime \(q\) with \(\nu_2(q+1)=1\), i.e. \(q\equiv1\pmod4\). Thus
\[
s=1\quad\text{or}\quad s=2q\quad(q\ge5\text{ prime},\ q\equiv1\pmod4).
\tag{5}
\]

When \(s=1\), equation (4) would require \(B(t)/t=1\), contradicting (2). When \(s=2q\) as in (5), equation (4) would require
\[
\frac{B(t)}t=\frac{2q}{3(q+1)}\ge\frac{5}{9}=\frac{125}{225}>\frac{113}{225},
\]
again contradicting (2). The case \(t=1\) cannot satisfy (1) because \(B(1)=0\) and \(n>1\). The theorem follows.

## Verification
The standalone `verify.py` constructs prime factorizations and nonunitary divisors directly. It checks the identity (3) and absence of odd powerful parts with \(\omega(t)\le2\) for every \(2\le n\le10000\), and separately checks the ratio inequality on primes up to \(19\) with exponents \(2\) through \(6\), including equality at \(225\). These finite checks corroborate, but cannot replace, the unrestricted inequalities and parity proof above.

## Relationship to prior work
Ligh and Wall, *Functions of Non-Unitary Divisors* (1987), introduced the nonunitary Euler function, proved the factorization (3) in their Theorem 5, and explicitly conjectured in Conjecture 4 that the powerful part of every solution of (1) is even. Their Theorem 7 already proves that every solution's powerful part has at least two distinct prime divisors. This result advances the conjecture by ruling out the first possible odd-powerful case, exactly two distinct odd primes; it does not claim the original factorization or one-prime exclusion as new.

OEIS A055653 records the product \(\prod_{p^a\parallel t}(1+p^a-p^{a-1})\), the unitary analogue of Euler's totient, while A055654 records its complementary difference from \(t\). These are constituent functions of \(B(t)\), not a theorem covering the two-prime odd-powerful obstruction.

Searches of the exact nonunitary Euler identity, Ligh--Wall Conjecture 4, odd powerful part, two-prime-power support, and the ratio \(113/225\) found no published result with an implication equivalent to the theorem. An unindexed later treatment remains possible.

## Limitations
The full evenness conjecture is not proved. Odd powerful parts with at least three distinct prime factors are not excluded. The sharp ratio bound concerns only \(\omega(t)\le2\), and its argument does not claim the same bound at higher support. No statement is made about the existence of an odd-powerful counterexample.

## References
1. S. Ligh and C. R. Wall, "Functions of Non-Unitary Divisors," *The Fibonacci Quarterly* **25** (1987), 333–338, especially Theorems 5 and 7 and Conjecture 4. Authorized scanned article: `https://www.fq.math.ca/Scanned/25-4/ligh.pdf`.
2. OEIS Foundation, A055653, unitary Euler-type product (entry dated 7 June 2000).
3. OEIS Foundation, A055654, complement of the unitary Euler-type product (entry dated 7 June 2000).
