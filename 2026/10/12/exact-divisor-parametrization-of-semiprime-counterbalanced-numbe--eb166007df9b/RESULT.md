# Exact divisor parametrization of semiprime counterbalanced numbers
## Finding
Let
\[
s(n)=\sigma(n)-n
\]
be the sum of the proper divisors of \(n\). Call a composite integer counterbalanced when
\[
s(n)\mid\varphi(n).
\]

Every counterbalanced integer with
\[
\Omega(n)=2
\]
is squarefree. More precisely, for distinct primes
\[
p<q,
\]
put
\[
d=p+q+1.
\]
Then
\[
s(pq)\mid\varphi(pq)
\]
if and only if
\[
d\mid(p-1)(p+2).
\]
Equivalently, for each prime \(p\), all squarefree semiprime counterbalanced numbers with smaller prime factor \(p\) are obtained by choosing a divisor
\[
d\mid(p-1)(p+2),\qquad d>2p+1,
\]
for which
\[
q=d-p-1
\]
is prime. The corresponding counterbalanced number is \(pq\).

Prime squares never satisfy the counterbalanced divisibility.

## Assumptions and scope
Here \(\sigma\) is the ordinary sum-of-divisors function, \(\varphi\) is Euler's totient, and \(\Omega\) counts prime factors with multiplicity.

The theorem classifies exactly the full multiplicity-two layer of the counterbalanced set. It does not classify integers with three or more prime factors counted with multiplicity.

## Proof
Suppose first that
\[
n=p^2
\]
for a prime \(p\). Then
\[
s(p^2)=1+p
\]
and
\[
\varphi(p^2)=p(p-1).
\]
Since \(\gcd(p,p+1)=1\), divisibility \(p+1\mid p(p-1)\) would force
\[
p+1\mid p-1,
\]
which is impossible. Thus no prime square is counterbalanced.

Now let
\[
n=pq
\]
with distinct primes \(p<q\). Then
\[
s(pq)=1+p+q
\]
and
\[
\varphi(pq)=(p-1)(q-1).
\]
Set
\[
d=1+p+q.
\]
Since
\[
q=d-p-1,
\]
we obtain the exact identity
\[
\varphi(pq)
=(p-1)(d-p-2)
=(p-1)d-(p-1)(p+2).
\]
Therefore
\[
d\mid\varphi(pq)
\]
if and only if
\[
d\mid(p-1)(p+2).
\]
This proves the first form of the criterion.

For the divisor parametrization, note that \(q>p\) is equivalent to
\[
d=p+q+1>2p+1.
\]
Thus every counterbalanced squarefree semiprime gives a divisor \(d\) of \((p-1)(p+2)\) above \(2p+1\), and \(q=d-p-1\) is prime. Conversely, if a prime \(p\) and such a divisor \(d\) are given and \(q=d-p-1\) is prime, then \(q>p\), the identity above shows
\[
p+q+1=d\mid\varphi(pq),
\]
and hence \(pq\) is counterbalanced.

This also gives the counterbalanced quotient explicitly:
\[
\frac{\varphi(pq)}{s(pq)}
=(p-1)-\frac{(p-1)(p+2)}{d}.
\]

## Verification
The attached `verify.py` checks every prime pair
\[
p<q<5000
\]
in two independent ways: directly from
\[
p+q+1\mid(p-1)(q-1)
\]
and through the divisor parametrization. The two sets agree exactly.

It separately checks prime squares in the same prime range and finds none satisfying the divisibility. It also verifies the first listed database examples
\[
133,403,583,713,817
\]
directly.

The finite computation is corroborative only. The unbounded theorem is the algebraic equivalence proved above.

## Relationship to prior work
Banks and Luca study the same set of composite integers satisfying
\[
s(n)\mid\varphi(n)
\]
and prove a strong upper bound for its counting function. They also give, conditional on Dickson's prime-tuples conjecture, an infinite semiprime family obtained when
\[
p=5m+1,
\qquad
q=20m+13
\]
are both prime.

The present parametrization contains that family but is strictly more structural: for those primes,
\[
p+q+1=25m+15
\]
is one divisor of
\[
(p-1)(p+2)=5m(5m+3).
\]
The general theorem characterizes every squarefree semiprime solution, not only one conditional subfamily.

OEIS A055940 is the exact database sequence of counterbalanced composite integers and records examples such as
\[
133=7\cdot19,
\]
for which \(\varphi(133)=108\) and \(s(133)=27\). The database gives membership data and the Banks--Luca asymptotic result, but not the divisor parametrization of the full semiprime layer.

Iannucci later studies the much narrower equation
\[
\sigma(n)=n+\varphi(n),
\]
which is the quotient-one subcase \(s(n)=\varphi(n)\). That problem does not imply the present divisibility classification.

## Limitations
The theorem does not imply that infinitely many semiprime counterbalanced numbers exist. The Banks--Luca conditional family remains conditional on a prime-tuples conjecture.

The result is confined to \(\Omega(n)=2\); higher multiplicity can introduce many more divisor shapes. Because the proof is elementary, an equivalent observation in an unindexed problem source remains a residual originality risk.

## References
1. W. D. Banks and F. Luca, “When the Sum of Aliquots Divides the Totient,” *Proceedings of the Edinburgh Mathematical Society* 50 (2007), 563–569, DOI 10.1017/S0013091505001161.
2. OEIS Foundation, A055940, “Counterbalanced numbers: Composite numbers \(k\) such that \(\varphi(k)/(\sigma(k)-k)\) is an integer,” entry originally authored 22 July 2000.
3. D. E. Iannucci, “On the Equation \(\sigma(n)=n+\varphi(n)\),” *Journal of Integer Sequences* 20 (2017), Article 17.6.2.
