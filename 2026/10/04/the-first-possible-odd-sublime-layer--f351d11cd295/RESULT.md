# The first possible odd sublime layer
## Finding
Let \(\Omega(n)\) count prime factors with multiplicity. A sublime number is a
positive integer \(n\) for which both
\[
\tau(n)
\quad\text{and}\quad
\sigma(n)
\]
are perfect numbers.

Every odd sublime number satisfies
\[
\Omega(n)\ge 8.
\]

The first possible layer has an exact description. An odd integer \(n\) with
\(\Omega(n)=8\) is sublime if and only if
\[
n=p^6(2^a-1)(2^b-1),
\]
where the three displayed prime factors are distinct, \(s=a+b+1\), the
Mersenne numbers
\[
2^a-1,\qquad 2^b-1,\qquad 2^s-1
\]
are prime, and
\[
\Phi_7(p)=p^6+p^5+p^4+p^3+p^2+p+1=2^s-1.
\]
Necessarily \(a\) and \(b\) are distinct odd primes, \(s\) is prime, and
\[
p\equiv1\pmod8.
\]

## Assumptions and scope
The functions \(\tau(n)\) and \(\sigma(n)\) denote the number and sum of the
positive divisors of \(n\). A perfect number \(P\) satisfies
\[
\sigma(P)=2P.
\]
The result is unconditional: it does not assume that odd perfect numbers do
not exist.

The proof uses the Euclid--Euler characterization of even perfect numbers.
It also uses only the elementary fact that the perfect numbers below \(256\)
are \(6\) and \(28\).

## Proof
Write
\[
n=\prod_{i=1}^r p_i^{e_i},
\qquad
\Omega(n)=\sum_i e_i.
\]
Since \(e+1\le 2^e\) for every positive integer \(e\),
\[
\tau(n)=\prod_i(e_i+1)\le 2^{\Omega(n)}.
\]

Suppose first that \(\Omega(n)<8\). Then
\[
\tau(n)<256.
\]
Because \(\tau(n)\) is perfect, it must be \(6\) or \(28\).

If \(\tau(n)=28\), the multiplicative partitions
\[
28,\qquad 14\cdot2,\qquad 7\cdot4,\qquad 7\cdot2\cdot2
\]
correspond respectively to exponent sums
\[
27,\qquad14,\qquad9,\qquad8.
\]
Thus \(\Omega(n)<8\) is impossible when \(\tau(n)=28\).

Hence \(\tau(n)=6\). Its two multiplicative partitions give exactly the
exponent patterns
\[
(5)
\qquad\text{or}\qquad
(2,1).
\]
Therefore an odd sublime number with \(\Omega(n)<8\) would have one of the
forms
\[
n=p^5
\qquad\text{or}\qquad
n=p^2q
\]
with distinct odd primes in the second case.

For \(n=p^5\),
\[
\sigma(n)
=(p+1)(p^2+p+1)(p^2-p+1).
\]
The last two factors are odd, exceed \(1\), and are coprime, because their
greatest common divisor divides \(2p\) while each is congruent to \(1\)
modulo \(p\). Thus \(\sigma(n)\) has at least two distinct odd prime
divisors. But \(\sigma(n)\) is even and perfect, whereas an even perfect
number has exactly one odd prime divisor. This is impossible.

Now let
\[
n=p^2q
\]
with distinct odd primes \(p,q\). Put
\[
A=p^2+p+1.
\]
Then
\[
\sigma(n)=A(q+1).
\]
This number is even and perfect, so for some prime Mersenne number
\[
M_s=2^s-1
\]
one has
\[
A(q+1)=2^{s-1}M_s.
\]
Since \(A>1\) is odd, the unique odd prime factor of the right side forces
\[
A=M_s,\qquad q+1=2^{s-1}.
\]
Thus
\[
q=2^{s-1}-1.
\]
Primality of \(M_s\) forces \(s\) to be prime, while primality of \(q\)
forces \(s-1\) to be prime unless \(s-1=1\). The only possible prime
\(s\) is therefore \(3\). But then
\[
p^2+p+1=7,
\]
whose only nonnegative integral solution is \(p=2\), contradicting the
oddness of \(p\). Hence no odd sublime number has \(\Omega(n)<8\).

Now suppose \(\Omega(n)=8\). The same bound gives
\[
\tau(n)\le256.
\]
It cannot equal \(6\), whose exponent sums are \(3\) and \(5\), so
\[
\tau(n)=28.
\]
Among the four multiplicative partitions of \(28\) listed above, the only
one having exponent sum \(8\) is
\[
7\cdot2\cdot2.
\]
Hence
\[
n=p^6qr
\]
for distinct odd primes \(p,q,r\).

The divisor sum is
\[
\sigma(n)=\Phi_7(p)(q+1)(r+1),
\]
where \(\Phi_7(p)\) is odd. Since \(\sigma(n)\) is an even perfect number,
there is a prime Mersenne number \(M_s=2^s-1\) such that
\[
\Phi_7(p)(q+1)(r+1)=2^{s-1}M_s.
\]
The unique odd prime factor on the right forces
\[
\Phi_7(p)=M_s
\]
and
\[
(q+1)(r+1)=2^{s-1}.
\]
Therefore
\[
q=2^a-1,\qquad r=2^b-1,\qquad a+b=s-1
\]
for positive integers \(a,b\). Since \(q,r,M_s\) are prime, their
Mersenne exponents \(a,b,s\) are prime. If one of \(a,b\) were \(2\),
then \(s=a+b+1\) would be an even integer greater than \(2\), impossible.
Thus \(a,b\) are distinct odd primes and
\[
s=a+b+1.
\]

Conversely, if these Mersenne-prime and cyclotomic conditions hold, then
\[
\tau(n)=7\cdot2\cdot2=28
\]
and
\[
\sigma(n)
=(2^s-1)2^{a+b}
=(2^s-1)2^{s-1},
\]
so both divisor functions are perfect and \(n\) is sublime.

Finally, because \(s\ge3\),
\[
\Phi_7(p)=2^s-1\equiv7\pmod8.
\]
For odd \(p\), direct reduction of
\[
1+p+p^2+\cdots+p^6
\]
modulo \(8\) gives \(7,5,3,1\) as \(p\equiv1,3,5,7\pmod8\),
respectively. Hence
\[
p\equiv1\pmod8.
\]

## Verification
The proof is unrestricted. The accompanying checker independently enumerates
all exponent partitions with \(\Omega<8\) and confirms that the only ones
whose divisor count is perfect are \((2,1)\) and \((5)\). It also checks the
\(\Omega=8\) partition boundary and finite prime ranges for the two eliminated
\(\tau=6\) shapes and for the stated congruence of the equality layer.

These computations corroborate the symbolic proof; they are not used to infer
the infinite result.

## Relationship to prior work
Kevin Brown's 1995 public discussion introduced the term "sublime" and
explicitly raised the possibility of odd sublime numbers. His later exposition
derives, under the assumption that odd perfect numbers do not exist, a
Mersenne-based necessary form for an odd sublime number. In the first case of
that framework he exhibits \(375\) as a near miss and concludes by asking
whether the required prime conditions might be impossible.

The result here closes that first multiplicity layer unconditionally. It does
not assume the nonexistence of odd perfect numbers: for the only possible
low-\(\Omega\) shapes, the divisor sum is automatically even. It also identifies
the exact next layer \(\Omega=8\) and reduces it to the single cyclotomic--
Mersenne equation
\[
\Phi_7(p)=2^{a+b+1}-1
\]
together with primality of the three Mersenne numbers.

OEIS A081357 records the two known sublime numbers and the 1995 sources.
A recent database comment uses broader wording about a Mersenne form, but it
supplies no proof and the same entry continues to link the literature in which
odd sublime numbers remain an open possibility. MathWorld likewise states that
the existence of odd sublime numbers is unknown.

## Limitations
The theorem does not decide whether the \(\Omega=8\) cyclotomic--Mersenne
conditions have a solution, and therefore does not settle the existence of odd
sublime numbers. No claim is made for higher multiplicity layers.

The exact database contains a recent broad structural comment whose wording
could be read more strongly than the primary sources support. This is retained
as an originality risk rather than treated as a proof, because no derivation or
covering reference is attached to that comment and contemporary reference
sources still describe odd sublime existence as open.

## References
1. Kevin S. Brown, "Twelve is special", public sci.math discussion,
   20 March 1995.
2. Kevin S. Brown, "Odd Sublime Numbers?", public sci.math discussion,
   26 March 1995.
3. Kevin S. Brown, "Sublime Numbers", MathPages.
4. OEIS Foundation, A081357, "Sublime numbers".
5. Jean-Marie De Koninck, *Those Fascinating Numbers*, American Mathematical
   Society, 2009; primary 2000 Mathematics Subject Classification includes
   11A25.
