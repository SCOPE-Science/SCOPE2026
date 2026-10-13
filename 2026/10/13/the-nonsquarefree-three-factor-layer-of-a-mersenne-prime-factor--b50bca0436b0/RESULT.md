# The nonsquarefree three-factor layer of a Mersenne prime-factor-sum divisibility
## Finding
Define
\[
\beta(n)=\sum_{p\mid n}p,
\]
the sum of the distinct prime divisors of \(n\), and let \(\Omega(n)\) count prime factors with multiplicity.

Among the positive integers satisfying
\[
\beta(n)\mid 2^n-1
\]
and
\[
\Omega(n)=3,
\]
the nonsquarefree solutions are exactly
\[
12=2^2\cdot3
\qquad\text{and}\qquad
52=2^2\cdot13.
\]

Equivalently, the even solutions in the \(\Omega=3\) layer are exactly \(12\) and \(52\). Every other solution in that layer is an odd squarefree product of three distinct primes.

## Assumptions and scope
The function \(\beta\) is the prime-divisor sum used by Banks and Luca in their study of integers for which \(\beta(n)\) divides the \(n\)-th Mersenne number.

The theorem concerns exactly the first multiplicity layer beyond semiprimes:
\[
\Omega(n)=3.
\]
It classifies the entire nonsquarefree sublayer and, equivalently, the entire even sublayer. It does not classify the odd squarefree solutions \(pqr\).

The proof uses only elementary multiplicative-order facts. If an odd prime \(\ell\) divides \(2^N-1\), then
\[
\operatorname{ord}_{\ell}(2)\mid N
\qquad\text{and}\qquad
\operatorname{ord}_{\ell}(2)\mid \ell-1.
\]

## Proof
Let \(n\) satisfy
\[
\Omega(n)=3
\qquad\text{and}\qquad
\beta(n)\mid2^n-1.
\tag{1}
\]

There are three factorization shapes:
\[
p^3,\qquad p^2q,\qquad pqr,
\]
where the displayed primes are distinct when more than one occurs.

A prime cube cannot occur. If \(p=2\), then \(\beta(8)=2\) cannot divide the odd number \(2^8-1\). If \(p\) is odd, then
\[
p^3\equiv1\pmod{p-1},
\]
so Fermat's theorem gives
\[
2^{p^3}\equiv2\pmod p.
\]
Hence
\[
p\nmid2^{p^3}-1.
\]

Now consider \(p^2q\). If \(p\) and \(q\) are both odd, then
\[
\beta(p^2q)=p+q
\]
is even, while \(2^{p^2q}-1\) is odd. Thus every nonsquarefree candidate must have support \(\{2,q\}\) with \(q\) odd. There are two exponent patterns:
\[
n=4q
\qquad\text{or}\qquad
n=2q^2.
\]

First take
\[
n=4q.
\]
Put
\[
m=q+2=\beta(4q).
\]
Assume
\[
m\mid2^{4q}-1.
\tag{2}
\]
Let \(\ell\) be a prime divisor of \(m\), and set
\[
t=\operatorname{ord}_{\ell}(2).
\]
Then
\[
t\mid4q
\qquad\text{and}\qquad
t\mid\ell-1.
\tag{3}
\]

If \(\ell<m\), then because \(\ell\) is a proper divisor of \(m\),
\[
\ell\le\frac m2=\frac{q+2}{2}<q.
\]
Thus \(t<q\). Since \(q\) is prime and \(t\mid4q\), equation (3) forces
\[
t\mid4.
\]

If instead \(\ell=m=q+2\), then \(m\) is prime and
\[
t\mid\gcd(4q,q+1)\mid4.
\]
Hence in all cases
\[
t\mid4.
\]
Therefore
\[
\ell\mid2^4-1=15,
\]
so every prime divisor of \(m\) is \(3\) or \(5\). Write
\[
m=3^a5^b.
\tag{4}
\]

If \(a>0\), then \(q=m-2\equiv1\pmod3\). Since
\[
2^{4q}-1=16^q-1=(16-1)(1+16+\cdots+16^{q-1}),
\]
the second factor is congruent to \(q\equiv1\pmod3\). Consequently
\[
\nu_3(2^{4q}-1)=1,
\]
so \(a\le1\).

Similarly, if \(b>0\), then \(q=m-2\equiv3\pmod5\), and the same factorization gives
\[
1+16+\cdots+16^{q-1}\equiv q\not\equiv0\pmod5.
\]
Thus
\[
\nu_5(2^{4q}-1)=1,
\]
so \(b\le1\).

Because \(m=q+2\ge5\), equations (4) and the exponent bounds leave
\[
m=5\quad\text{or}\quad m=15.
\]
These give
\[
q=3\quad\text{or}\quad q=13,
\]
hence
\[
n=12\quad\text{or}\quad n=52.
\]
Both work:
\[
5\mid2^{12}-1
\qquad\text{and}\qquad
15\mid2^{52}-1.
\]

It remains to exclude
\[
n=2q^2.
\]
Again put
\[
m=q+2.
\]
If
\[
m\mid2^{2q^2}-1,
\tag{5}
\]
then for every prime \(\ell\mid m\), its order \(t=\operatorname{ord}_{\ell}(2)\) divides \(2q^2\).

If \(\ell<m\), then
\[
\ell\le\frac m2<q,
\]
so \(t<q\). The only divisors of \(2q^2\) below \(q\) are \(1\) and \(2\); hence \(t\mid2\).

If \(\ell=m=q+2\), then
\[
t\mid\gcd(2q^2,q+1)=2.
\]
Thus every prime divisor of \(m\) divides
\[
2^2-1=3,
\]
so
\[
m=3^a.
\]
Since \(m=q+2\ge5\), one has \(a\ge2\).

But \(q=3^a-2\equiv1\pmod3\), and
\[
2^{2q^2}-1=4^{q^2}-1
=(4-1)(1+4+\cdots+4^{q^2-1}).
\]
The second factor is congruent to
\[
q^2\equiv1\pmod3.
\]
Therefore
\[
\nu_3(2^{2q^2}-1)=1,
\]
contradicting \(9\mid m\). Hence no number \(2q^2\) satisfies (1).

Finally consider the squarefree shape \(pqr\). If one prime is \(2\), then
\[
\beta(2qr)=2+q+r
\]
is even, so it cannot divide the odd number \(2^{2qr}-1\). Thus every squarefree solution in the layer is odd.

We have proved that the only nonsquarefree solutions, and also the only even solutions, are
\[
12,\ 52.
\]

## Verification
The attached `verify.py` performs an exact finite corroboration through
\[
2{,}000{,}000.
\]
It enumerates all integers with
\[
\Omega(n)=3,
\]
computes \(\beta(n)\), and tests
\[
2^n\equiv1\pmod{\beta(n)}
\]
by modular exponentiation. It verifies that every nonsquarefree or even hit is one of
\[
12,\ 52,
\]
and that both numbers are hits.

The same program separately tests the two nonsquarefree parameter branches \(4q\) and \(2q^2\) for primes \(q<100{,}000\), agreeing with the symbolic classification.

The finite checks are corroborative only. The unbounded result follows from the multiplicative-order and valuation arguments above.

## Relationship to prior work
Banks and Luca introduced the exact divisibility problem
\[
\beta(n)\mid2^n-1
\]
and obtained global counting estimates for its solution set. Their article is the primary source for the object studied here.

OEIS A336657 is the exact database sequence. It records that all terms are composite and that there are no semiprimes, so \(\Omega=3\) is the first possible multiplicity layer. It also records the closure property that if \(n\) is a term and \(d\mid n\), then \(dn\) is a term; in particular this explains the family containing \(12\).

The database does not state that \(12\) and \(52\) are the only nonsquarefree or even solutions with \(\Omega=3\). The first terms alone cannot prove that exclusion for unbounded primes.

A later paper of Luca and Tipu defines the same \(\beta\), cites the Banks--Luca problem explicitly, and studies the neighboring condition
\[
\beta(n)\mid2^{n-1}-1.
\]
That neighboring result does not imply the present classification because changing the exponent changes the multiplicative-order constraints.

Targeted searches for the exact equation, the \(\Omega=3\) layer, nonsquarefree/even aliases, and the pair \(12,52\) found no statement equivalent to or stronger than this result.

## Limitations
The theorem does not classify odd squarefree solutions
\[
n=pqr.
\]
Such solutions exist, for example
\[
345=3\cdot5\cdot23
\qquad\text{and}\qquad
385=5\cdot7\cdot11.
\]

Direct access to the complete Banks--Luca article body was unavailable from the publisher and linked archive during this review; the electronic issue abstract, indexed first page, exact database entry, and later full-text citation were inspected. Therefore an equivalent observation in the inaccessible body or an unindexed elementary source remains a residual originality risk.

## References
1. W. D. Banks and F. Luca, “Sums of prime divisors and Mersenne numbers,” *Houston Journal of Mathematics* 33 (2007), 403–413.
2. OEIS Foundation, A336657, numbers \(k\) for which \(2^k-1\) is divisible by the sum of the distinct prime divisors of \(k\).
3. F. Luca and V. Tipu, “On Positive Integers \(n\) with a Certain Divisibility Property,” *Journal of Integer Sequences* 12 (2009), Article 09.3.1.
