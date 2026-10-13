# Divisibility by the small-divisor sum through \(\Omega(n)\le3\)

## Finding
Let
\[
a(n)=\sum_{\substack{d\mid n\\ d\le\sqrt n}}d,
\]
the sum of the positive divisors of \(n\) not exceeding \(\sqrt n\), and let \(\Omega(n)\) count prime factors with multiplicity. For every integer \(n\ge2\) with \(\Omega(n)\le3\),
\[
a(n)\mid n
\]
if and only if one of the following mutually compatible descriptions applies:

1. \(n\) is prime;
2. \(n=6\);
3. \(n\in\{12,18\}\);
4. \(n=p^2q\), where \(p,q\) are distinct primes and
\[
q=p^2+p+1;
\]
5. \(n=p^2q\), where \(p,q\) are distinct primes and
\[
q=p^2-p-1.
\]

In items 4 and 5 the displayed value of \(q\) is required to be prime. In particular, no squarefree integer with three distinct prime factors has its small-divisor sum dividing the integer.

The first composite examples are
\[
6,\ 12,\ 18,\ 28,\ 45,\ 117,\ 475,\ 775,\ldots
\]
where \(28=2^2\cdot7\) and \(117=3^2\cdot13\) lie on the \(p^2+p+1\) branch, while \(45=3^2\cdot5\) and \(475=5^2\cdot19\) lie on the \(p^2-p-1\) branch.

## Assumptions and scope
All variables are positive integers unless stated otherwise, and every letter denoting a prime is a rational prime. The result is an exact classification only on the stratum \(\Omega(n)\le3\). It does not assert that either polynomial \(p^2+p+1\) or \(p^2-p-1\) is prime infinitely often, and it makes no claim about integers with four or more prime factors counted with multiplicity.

## Proof
We exhaust the multiplicative partitions of \(\Omega(n)\le3\).

If \(n=p\) is prime, then the only small divisor is \(1\), so \(a(p)=1\) and \(a(p)\mid p\).

For \(\Omega(n)=2\), first let \(n=p^2\). Its small divisors are \(1,p\), hence \(a(n)=p+1\). Since \(\gcd(p,p+1)=1\), the integer \(p+1>1\) cannot divide \(p^2\). Now let \(n=pq\) with primes \(p<q\). The small divisors are \(1,p\), so \(a(n)=p+1\). If \(p+1\mid pq\), coprimality with \(p\) gives \(p+1\mid q\). Since \(q\) is prime, \(q=p+1\), and the only consecutive primes are \(2,3\). Thus \(n=6\), which indeed works.

For \(\Omega(n)=3\), a prime cube \(p^3\) again has small divisors \(1,p\), hence \(a(p^3)=p+1\nmid p^3\).

Consider next \(n=p^2q\) with distinct primes \(p,q\). The divisors \(p^2\) and \(q\) are complementary with respect to \(\sqrt n\): exactly one is at most \(\sqrt n\). Thus the small divisors are
\[
1,\ p,\ \min\{p^2,q\},
\]
and therefore
\[
a(n)=1+p+\min\{p^2,q\}.
\]
If \(q>p^2\), then \(a(n)=p^2+p+1\). This is coprime to \(p\). Hence \(a(n)\mid p^2q\) forces \(a(n)\mid q\), and because \(q\) is prime,
\[
q=p^2+p+1.
\]
Conversely, this equality makes \(a(n)=q\), so the divisibility holds.

Suppose instead that \(q<p^2\). Then \(a(n)=p+q+1\), which is larger than both \(p\) and \(q\), yet smaller than \(p^2q\). If it divides \(p^2q\), it must therefore be one of the two proper divisors of \(p^2q\) larger than both primes, namely \(p^2\) or \(pq\). The first possibility gives
\[
q=p^2-p-1,
\]
and conversely this equality yields \(a(n)=p^2\). The second possibility gives
\[
pq=p+q+1,
\]
equivalently
\[
(p-1)(q-1)=2.
\]
Thus \((p,q)=(2,3)\) or \((3,2)\), producing \(12\) and \(18\), and direct substitution gives \(a(12)=6\) and \(a(18)=6\).

It remains to rule out squarefree \(n=pqr\) with primes \(p<q<r\). The divisor pairs around \(\sqrt n\) are
\[
(1,pqr),\ (p,qr),\ (q,pr),\ (r,pq).
\]
Because \(q<pr\), the small divisors are exactly
\[
1,\ p,\ q,\ \min\{r,pq\}.
\]

If \(r>pq\), then
\[
a(n)=1+p+q+pq=(p+1)(q+1)>pq.
\]
Any proper divisor of \(pqr\) exceeding \(pq\) is one of \(r,pr,qr\). Equality with \(r\) is impossible because \((p+1)(q+1)\) is composite. If \((p+1)(q+1)=pr\), then \(p\mid q+1\); writing \(q+1=pt\), the inequality \(q>p\) gives \(t>1\), so \(r=(p+1)t\) is composite. If \((p+1)(q+1)=qr\), then \(q\mid p+1\), forcing \((p,q)=(2,3)\), after which \(r=4\), again impossible.

If \(r<pq\), then
\[
a(n)=1+p+q+r>r.
\]
Hence divisibility would force \(a(n)\in\{pq,pr,qr\}\). If \(a(n)=pq\), then
\[
r=pq-p-q-1.
\]
For \(p=2\) this gives \(r=q-3<q\); for odd \(p\) and \(q\) the right side is even and greater than \(2\), so it is not the prime \(r\). If \(a(n)=pr\), then
\[
q=(p-1)r-p-1.
\]
For \(p\ge3\) the right side exceeds \(r\), contradicting \(q<r\); for \(p=2\) it gives \(r-q=3\), impossible for two odd primes. Finally, \(a(n)=qr\) gives
\[
p=(q-1)r-q-1>q,
\]
contradicting \(p<q\). Thus no squarefree three-prime case occurs, completing the classification.

## Verification
The accompanying `verify.py` independently computes prime factorizations and the small-divisor sum by integer arithmetic, then checks every \(2\le n\le300000\) with \(\Omega(n)\le3\) against the theorem. It reports no mismatch. This finite computation is regression evidence only; the proof above is unbounded and does not depend on the cutoff.

## Relationship to prior work
Iannucci's arXiv:1910.11835v1 defines the same small-divisor sum \(a(n)\), proves supermultiplicativity for coprime inputs, determines its average order, studies its Dirichlet generating series, and records the prime-power formula \(a(p^m)=1+p+\cdots+p^{\lfloor m/2\rfloor}\). The full text does not state a divisibility classification for \(a(n)\mid n\). OEIS A066839 records the function, formulas, examples, and links to the small-divisor literature, but the checked entry likewise does not give the low-\(\Omega\) divisibility theorem. Searches for the defining formula, the divisibility relation, and the two polynomial branches did not locate a statement implying the classification.

## Limitations
The theorem stops at \(\Omega(n)=3\). New small-divisor order types arise at higher multiplicity, so the proof does not automatically extend. The primality frequency of \(p^2+p+1\) and \(p^2-p-1\) is not addressed. Literature searches cannot exclude an obscure or unindexed equivalent statement, especially under terminology different from “small divisors.”

## References
1. D. E. Iannucci, *On sums of the small divisors of a natural number*, arXiv:1910.11835v1, 2019.
2. OEIS Foundation Inc., *A066839: sum of positive divisors \(d\) of \(n\) with \(d\le\sqrt n\)*.
3. D. E. Iannucci, *When the Small Divisors of a Natural Number Are in Arithmetic Progression*, Integers 18 (2018), Paper A77.
