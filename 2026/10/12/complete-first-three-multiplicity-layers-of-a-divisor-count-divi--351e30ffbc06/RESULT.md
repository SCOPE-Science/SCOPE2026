# Complete first three multiplicity layers of a divisor-count divisibility
## Finding
Let \(\tau(n)\) denote the number of positive divisors of \(n\), let \(\sigma(n)\) denote their sum, let \(\varphi(n)\) be Euler's totient, and let \(\Omega(n)\) count prime factors with multiplicity.

For
\[
\Omega(n)\le3,
\]
the condition
\[
\tau(n)\mid \sigma(n)+\varphi(n)
\tag{1}
\]
has the following complete classification.

For \(\Omega(n)=1\), every prime is a solution.

For \(\Omega(n)=2\):
\[
p^2\text{ is a solution}\iff p\ne3,
\]
and for distinct primes \(p<q\),
\[
pq\text{ is a solution}\iff p,q\text{ are both odd}.
\]

For \(\Omega(n)=3\):
\[
p^3\text{ is a solution}\iff p\equiv1\pmod4.
\]
For distinct primes \(p,q\), with \(p\) the repeated prime,
\[
p^2q\text{ is a solution}
\]
if and only if \(q\) is odd and either
\[
p\equiv1\pmod3,
\]
or
\[
p=3,\qquad q\equiv2\pmod3.
\]
Finally, for distinct primes \(p<q<r\), every odd product \(pqr\) is a solution; an even squarefree product
\[
2qr
\]
is a solution exactly when
\[
q\not\equiv r\pmod4.
\]

## Assumptions and scope
The statement classifies exactly the first three multiplicity layers of the sequence defined by (1), corresponding to the six factorization shapes
\[
p,\quad p^2,\quad pq,\quad p^3,\quad p^2q,\quad pqr.
\]

The classification is unbounded in the prime parameters. No claim is made for
\[
\Omega(n)\ge4.
\]

## Proof
For a prime \(p\),
\[
\tau(p)=2,
\qquad
\sigma(p)+\varphi(p)=(p+1)+(p-1)=2p,
\]
so every prime is a solution.

For a prime square,
\[
\tau(p^2)=3,
\]
and
\[
\sigma(p^2)+\varphi(p^2)
=(p^2+p+1)+(p^2-p)
=2p^2+1.
\]
If \(p=3\), this is \(19\), not divisible by \(3\). If \(p\ne3\), then
\[
p^2\equiv1\pmod3,
\]
hence
\[
2p^2+1\equiv0\pmod3.
\]
Thus \(p^2\) is a solution exactly when \(p\ne3\).

For distinct primes \(p<q\),
\[
\tau(pq)=4
\]
and
\[
\sigma(pq)+\varphi(pq)
=(p+1)(q+1)+(p-1)(q-1)
=2(pq+1).
\]
This is divisible by \(4\) exactly when \(pq\) is odd, proving the \(\Omega(n)=2\) squarefree criterion.

For a prime cube,
\[
\tau(p^3)=4
\]
and
\[
\sigma(p^3)+\varphi(p^3)
=(p^3+p^2+p+1)+(p^3-p^2)
=2p^3+p+1.
\]
For \(p=2\) this equals \(19\), so \(8\) is not a solution. For odd \(p\),
\[
p^3\equiv p\pmod4,
\]
and hence
\[
2p^3+p+1\equiv3p+1\pmod4.
\]
This vanishes exactly when
\[
p\equiv1\pmod4.
\]

Now consider
\[
n=p^2q
\]
with distinct primes, where \(p\) is the repeated prime. Since
\[
\tau(n)=6,
\]
a direct expansion gives
\[
\sigma(n)+\varphi(n)
=(p^2+p+1)(q+1)+p(p-1)(q-1)
=q(2p^2+1)+2p+1.
\tag{2}
\]
The right side of (2) is even exactly when \(q\) is odd.

Modulo \(3\), if \(p=3\), expression (2) is congruent to
\[
q+1,
\]
so divisibility by \(3\) is equivalent to
\[
q\equiv2\pmod3.
\]
If \(p\ne3\), then \(p^2\equiv1\pmod3\), so (2) is congruent to
\[
2p+1.
\]
For a prime \(p\ne3\), this is divisible by \(3\) exactly when
\[
p\equiv1\pmod3.
\]
Combining the parity and modulo-\(3\) conditions proves the \(p^2q\) criterion.

Finally take three distinct primes. If all three are odd, then
\[
\tau(pqr)=8,
\]
and both products
\[
(p+1)(q+1)(r+1)
\quad\text{and}\quad
(p-1)(q-1)(r-1)
\]
are divisible by \(8\). Hence every odd squarefree product of three primes satisfies (1).

For the even squarefree shape \(2qr\), write
\[
q=2a+1,\qquad r=2b+1.
\]
Then
\[
\sigma(2qr)+\varphi(2qr)
=
3(q+1)(r+1)+(q-1)(r-1)
\]
equals
\[
4\bigl(3(a+1)(b+1)+ab\bigr).
\]
The factor in parentheses is even exactly when
\[
a+b+1\equiv0\pmod2,
\]
that is, exactly when \(a\) and \(b\) have opposite parity. This is equivalent to \(q\) and \(r\) having opposite residues modulo \(4\). The classification is complete.

## Verification
The attached `verify.py` computes \(\tau(n)\), \(\sigma(n)\), \(\varphi(n)\), and \(\Omega(n)\) exactly for every
\[
2\le n\le1{,}000{,}000
\]
with \(\Omega(n)\le3\), and compares direct divisibility with the displayed classification.

The computation is corroborative only. The universal conclusion follows from the exhaustive six-shape proof above.

## Relationship to prior work
OEIS A055464 is exactly the sequence of integers satisfying
\[
\tau(n)\mid\sigma(n)+\varphi(n).
\]
Its entry supplies terms, a computational predicate, and the related theorem that equality
\[
\sigma(n)+\varphi(n)=n\tau(n)
\]
characterizes primes, but it does not give a classification by \(\Omega(n)\).

De Koninck and Luca study the interaction of \(\sigma\) and \(\varphi\) through the composition quotient
\[
\frac{\sigma(\varphi(n))}{\varphi(\sigma(n))}.
\]
Their paper has first-listed Mathematics Subject Classification \(11A25\) and develops orders and densities for those arithmetic functions. Its inspected statements do not concern the divisor-count divisibility in (1).

Targeted searches for the exact A055464 condition, prime-square and semiprime restrictions, the \(p^2q\) residue formula, prime cubes modulo \(4\), and squarefree three-prime residues modulo \(8\) did not locate an equivalent or stronger low-multiplicity classification.

## Limitations
The theorem does not classify any layer with
\[
\Omega(n)\ge4.
\]
It also does not give a counting asymptotic for the classified layers.

Because the proof is elementary and the exact sequence has been public since 2000, an equivalent observation could occur in an unindexed problem note or discussion not surfaced by the searches.

## References
1. OEIS Foundation, A055464, integers for which \(\sigma(n)+\varphi(n)\) is an integer multiple of \(\tau(n)\), entry authored 27 June 2000.
2. J.-M. De Koninck and F. Luca, “On the composition of the Euler function and the sum of divisors function,” *Colloquium Mathematicum* 108 (2007), 31–51, DOI 10.4064/cm108-1-4.
3. R. Sivaramakrishnan, *Classical Theory of Arithmetical Functions*, Marcel Dekker, 1989.
