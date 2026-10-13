# Squarefree structure of \(\tau(\sigma(n)+\varphi(n))=4\)
## Finding
Let \(\tau(n)\) be the number of positive divisors, let \(\sigma(n)\) be their sum, and let \(\varphi(n)\) be Euler's totient.

For a squarefree positive integer \(n\),
\[
\tau(\sigma(n)+\varphi(n))=4
\tag{1}
\]
if and only if either \(n\) is an odd prime, or
\[
n=2q
\]
where
\[
q\quad\text{and}\quad 2q+1
\]
are both prime.

Thus the squarefree composite members are exactly twice the odd Sophie Germain primes. For every real \(X\ge1\),
\[
\#\{n\le X:n\text{ is squarefree composite and satisfies (1)}\}
=
\#\{q\le X/2:q,\ 2q+1\text{ are prime}\}.
\tag{2}
\]
Consequently there are infinitely many squarefree composite members if and only if there are infinitely many Sophie Germain primes.

The first composite squarefree members are
\[
6,\ 10,\ 22,\ 46,\ 58,\ 82,\ 106,\ 166,\ 178,\ 226,\ldots
\]

## Assumptions and scope
The theorem concerns exactly the squarefree part of the sequence defined by
\[
\tau(\sigma(n)+\varphi(n))=4.
\]
A positive integer has exactly four divisors if and only if it is either the cube of a prime or the product of two distinct primes.

No claim is made about nonsquarefree members. In particular, the ambient sequence also contains nonsquarefree examples such as \(16\), \(25\), and \(27\).

## Proof
For \(n=1\),
\[
\sigma(1)+\varphi(1)=2,
\]
which has two divisors, so \(1\) is not a solution.

Let \(n=p\) be prime. Then
\[
\sigma(p)+\varphi(p)=(p+1)+(p-1)=2p.
\]
For \(p=2\), this is \(4\), which has three divisors. For odd prime \(p\), the number \(2p\) is the product of two distinct primes, so it has exactly four divisors. Hence the squarefree prime solutions are exactly the odd primes.

We shall use the elementary observation that
\[
4\mid N,\qquad \tau(N)=4
\tag{3}
\]
implies
\[
N=8.
\tag{4}
\]
Indeed, \(\tau(N)=4\) forces \(N\) to be either a prime cube or a product of two distinct primes. A product of two distinct primes cannot be divisible by \(4\), while a prime cube divisible by \(4\) must be \(2^3=8\).

Now let \(n\) be an odd squarefree composite,
\[
n=p_1p_2\cdots p_r,\qquad r\ge2,
\]
with distinct odd primes \(p_i\). Multiplicativity gives
\[
\sigma(n)=\prod_{i=1}^r(p_i+1),
\qquad
\varphi(n)=\prod_{i=1}^r(p_i-1).
\]
Each factor in both products is even, so
\[
4\mid\sigma(n)+\varphi(n).
\]
The sum is larger than \(8\), contradicting (3)–(4). Thus no odd squarefree composite occurs.

It remains to take
\[
n=2p_1p_2\cdots p_r
\]
with \(r\ge1\) and distinct odd primes \(p_i\). If \(r\ge2\), then
\[
\sigma(n)=3\prod_{i=1}^r(p_i+1),
\qquad
\varphi(n)=\prod_{i=1}^r(p_i-1).
\]
Again both terms are divisible by \(4\), while their sum exceeds \(8\), so (3)–(4) excludes the case.

Therefore every squarefree composite solution has
\[
n=2q
\]
for an odd prime \(q\). Then
\[
\sigma(2q)+\varphi(2q)
=
3(q+1)+(q-1)
=
4q+2
=
2(2q+1).
\tag{5}
\]
Since \(2q+1\) is odd,
\[
\tau\bigl(2(2q+1)\bigr)
=
2\,\tau(2q+1).
\]
This equals \(4\) exactly when
\[
\tau(2q+1)=2,
\]
that is, exactly when \(2q+1\) is prime.

Hence the map
\[
q\longmapsto2q
\]
is a bijection from odd Sophie Germain primes to squarefree composite solutions. Formula (2) and the infinitude equivalence follow immediately.

## Verification
The attached `verify.py` performs an independent exact-integer check through
\[
500{,}000.
\]
It factors every squarefree integer in that range, computes \(\sigma(n)\) and \(\varphi(n)\) from the prime factorization, computes the divisor count of their sum, and compares direct membership with the theorem's criterion.

It also checks that every composite hit is exactly twice a Sophie Germain prime.

The finite computation is corroborative only. The unbounded result follows from the proof above.

## Relationship to prior work
OEIS A067350 is the exact database sequence defined by
\[
\tau(\sigma(n)+\varphi(n))=4.
\]
Its entry notes that all odd primes occur, gives composite examples such as \(22\) and \(25\), and discusses the two possible factorization shapes of \(\sigma(n)+\varphi(n)\). It does not state a classification of the squarefree members.

OEIS A065387 tabulates the underlying function
\[
\sigma(n)+\varphi(n).
\]
Its comments record that for a squarefree semiprime \(n\),
\[
\sigma(n)+\varphi(n)=2(n+1).
\]
This specializes the arithmetic on the two-prime layer but does not exclude squarefree integers of larger support or identify the complete A067350 squarefree set.

OEIS A097646 studies the different equation
\[
n=\varphi(\varphi(n)+\sigma(n)).
\]
Its entry observes that \(n=2q\) belongs whenever \(q\) is an odd Sophie Germain prime. That is a different predicate and does not state that this family is exactly the squarefree composite part of A067350.

De Koninck and Luca study the interaction of \(\sigma\) and \(\varphi\) through the composition quotient
\[
\frac{\sigma(\varphi(n))}{\varphi(\sigma(n))}.
\]
Their paper has primary Mathematics Subject Classification \(11A25\) and concerns extremal order, average order, and density rather than the divisor-count condition in (1).

Targeted searches using the exact predicate, its squarefree restriction, the Sophie Germain formulation, and identity (5) did not locate an equivalent or stronger squarefree classification.

## Limitations
The theorem does not classify nonsquarefree members. In particular, it does not resolve the database question of whether the prime-cube alternative for
\[
\sigma(n)+\varphi(n)
\]
ever occurs.

The infinitude statement is an equivalence, not a proof that infinitely many Sophie Germain primes exist.

Because the argument is elementary and the sequence has been public since 2002, an equivalent observation could occur in an unindexed note or discussion not surfaced by the searches.

## References
1. OEIS Foundation, A067350, integers \(n\) for which \(\sigma(n)+\varphi(n)\) has exactly four divisors, entry authored 17 January 2002.
2. OEIS Foundation, A065387, the arithmetic function \(\sigma(n)+\varphi(n)\).
3. OEIS Foundation, A097646, integers satisfying \(n=\varphi(\varphi(n)+\sigma(n))\).
4. J.-M. De Koninck and F. Luca, “On the composition of the Euler function and the sum of divisors function,” *Colloquium Mathematicum* 108 (2007), 31–51, DOI 10.4064/cm108-1-4.
