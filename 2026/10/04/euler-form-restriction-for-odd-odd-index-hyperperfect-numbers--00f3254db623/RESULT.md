# Euler-form restriction for odd odd-index hyperperfect numbers
## Finding
Let \(k>1\) be odd and let \(n>1\) be an odd \(k\)-hyperperfect number:
\[
n=1+k(\sigma(n)-n-1).
\]
Then
\[
\nu_2(\sigma(n))=1.
\]
Therefore, if
\[
n=\prod_{i=1}^r p_i^{a_i},
\]
exactly one exponent \(a_i\) is odd. Writing the corresponding prime as \(q\) and
its exponent as \(\alpha\), one has
\[
n=q^\alpha m^2,\qquad \gcd(q,m)=1,\qquad
q\equiv\alpha\equiv1\pmod4.
\]
Hence no odd squarefree composite can be \(k\)-hyperperfect for odd \(k>1\).

## Assumptions and scope
Here \(\sigma\) is the ordinary sum-of-divisors function. The theorem assumes both
that \(k\) is odd and that the hyperperfect number \(n\) itself is odd. The latter
assumption is essential to this proof: the cited literature notes that all known
odd-index examples are odd, but does not prove that every odd-index hyperperfect
number must be odd.

The result is a necessary structural condition. It does not prove the stronger
conjecture that every odd-index \(k\)-hyperperfect number has the form
\(p^2q\) from the known two-prime construction.

## Proof
From the defining equation,
\[
n=1+k(\sigma(n)-n-1),
\]
one obtains
\[
k\sigma(n)=(k+1)n+(k-1)=(k+1)(n+1)-2.
\]
Because both \(k\) and \(n\) are odd, both \(k+1\) and \(n+1\) are even. Thus
\[
(k+1)(n+1)\equiv0\pmod4,
\]
and consequently
\[
k\sigma(n)\equiv2\pmod4.
\]
Since \(k\) is odd, it is a unit modulo \(4\), so
\[
\sigma(n)\equiv2\pmod4.
\]
Equivalently,
\[
\nu_2(\sigma(n))=1.
\]

Now factor the odd integer \(n\) as
\[
n=\prod_i p_i^{a_i}.
\]
By multiplicativity,
\[
\sigma(n)=\prod_i \sigma(p_i^{a_i}).
\]
For an odd prime \(p\), the sum
\[
\sigma(p^a)=1+p+\cdots+p^a
\]
is odd exactly when \(a\) is even. Since the total \(2\)-adic valuation of
\(\sigma(n)\) is exactly \(1\), precisely one exponent is odd; call it
\(\alpha\), attached to the odd prime \(q\). All remaining prime exponents are
even, hence
\[
n=q^\alpha m^2,\qquad \gcd(q,m)=1.
\]

It remains to determine the residue classes of \(q\) and \(\alpha\). Since
\(\alpha\) is odd, \(\alpha+1\) is even. The lifting-the-exponent identity gives
\[
\nu_2(q^{\alpha+1}-1)
=
\nu_2(q-1)+\nu_2(q+1)+\nu_2(\alpha+1)-1.
\]
Therefore
\[
\nu_2(\sigma(q^\alpha))
=
\nu_2(q+1)+\nu_2(\alpha+1)-1.
\]
This valuation equals \(1\), while both terms on the right before subtraction are
at least \(1\). Hence
\[
\nu_2(q+1)=\nu_2(\alpha+1)=1,
\]
which is equivalent to
\[
q\equiv\alpha\equiv1\pmod4.
\]

## Verification
The proof is symbolic. The accompanying checker independently enumerates odd
integers in a finite range, detects those for which the defining hyperperfect
index is an odd integer greater than \(1\), and verifies the asserted
\(2\)-adic and factorization conditions. It also checks the standard known
odd-index examples \(325\), \(10693\), \(51301\), \(214273\), and \(306181\).
The computation is corroborative only and is not used to infer the infinite
theorem.

## Relationship to prior work
McCranie proved that when \(k>1\) is odd and
\[
p=\frac{3k+1}{2},\qquad q=3k+4
\]
are prime, \(p^2q\) is \(k\)-hyperperfect, and conjectured that every
odd-index \(k\)-hyperperfect number belongs to this family. The same paper says
that all known odd-index examples are odd. The theorem here does not assume the
two-prime shape; it proves an Euler-style necessary factorization for every odd
odd-index hyperperfect number.

The later survey by Bege and Fogarasi restates McCranie's construction and says
the converse remained unproved. OEIS A034897 records the hyperperfect numbers by
the defining equation, but does not supply this prime-exponent restriction.

## Limitations
The theorem does not show that odd-index hyperperfect numbers are always odd.
It also does not reduce the number of distinct prime factors to two. Thus it does
not settle McCranie's converse conjecture. Literature and database searches found
no statement implying this Euler-form restriction, but a short observation of
this kind could exist in a poorly indexed source.

## References
1. J. S. McCranie, "A Study of Hyperperfect Numbers", Journal of Integer
   Sequences 3 (2000), Article 00.1.3, published 21 January 2000.
2. A. Bege and K. Fogarasi, "Generalized perfect numbers", Acta Universitatis
   Sapientiae, Mathematica 1 (2009), 73--82.
3. H. J. J. te Riele, "Rules for constructing hyperperfect numbers",
   Fibonacci Quarterly 22 (1984), 50--60; MSC 11A25.
4. OEIS Foundation, A034897, "Hyperperfect numbers".
