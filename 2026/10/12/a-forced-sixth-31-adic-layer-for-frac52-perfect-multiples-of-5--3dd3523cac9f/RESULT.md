# A forced sixth \(31\)-adic layer for \(\frac52\)-perfect multiples of \(5\)

## Finding
Let \(\sigma\) denote the sum-of-divisors function and let \(I(N)=\sigma(N)/N\) be the abundancy index. Suppose \(N\) is a positive integer satisfying
\[
I(N)=\frac52
\]
and \(5\mid N\). Then
\[
2^4\parallel N,\qquad 5^2\parallel N,\qquad 31^6\mid N.
\]
In addition, if \(q\notin\{2,5,31\}\) is a prime divisor of \(N\), then
\[
q\ge149.
\]

## Assumptions and scope
The starting point is Theorem 7 of Almeida and Cardoso, which proves for exactly this hypothesis that \(2^4\parallel N\), \(5^2\parallel N\), and \(31^2\mid N\). Write
\[
c=\nu_{31}(N)\ge2,\qquad N=2^4 5^2 31^c u,
\]
where \(\gcd(u,2\cdot5\cdot31)=1\). The result is a necessary-condition theorem; it does not assert that any such \(N\) exists.

## Proof
First suppose a prime \(q\mid u\). Since the abundancy index is multiplicative on coprime factors and \(I(q^e)\ge(q+1)/q\) for every \(e\ge1\),
\[
\frac52=I(N)\ge I(2^4)I(5^2)I(31^2)\frac{q+1}q.
\]
The fixed product is
\[
I(2^4)I(5^2)I(31^2)
=\frac{31}{16}\frac{31}{25}\frac{993}{961}
=\frac{993}{400}.
\]
Therefore
\[
\frac{1000}{400}\ge\frac{993}{400}\frac{q+1}q,
\]
so \(7q\ge993\), hence \(q\ge142\). The least prime at least \(142\) is \(149\), proving the prime-divisor cutoff.

It remains to strengthen the forced exponent of \(31\). From
\[
I(2^4)I(5^2)=\frac{961}{400}
\]
and \(I(N)=5/2\), multiplicativity gives
\[
I(u)=\frac{1000\,31^c}{961\,\sigma(31^c)}.
\]
For the four possible exponents \(c=2,3,4,5\), reduction to lowest terms gives respectively
\[
I(u)\in\left\{
\frac{1000}{993},
\frac{3875}{3848},
\frac{192200}{190861},
\frac{3723875}{3697932}
\right\}.
\]
If \(I(u)=A/B\) in lowest terms, then \(B\sigma(u)=Au\), and \(\gcd(A,B)=1\) forces \(B\mid u\). For \(c=2\), the denominator is divisible by \(3\); for \(c=3\) and \(c=5\), the denominator is even; and for \(c=4\), the denominator \(190861\) is divisible by \(11\). Each alternative forces a prime divisor of \(u\) below \(149\), contradicting the cutoff (and the even cases also contradict \(\gcd(u,2)=1\)). Thus \(c\notin\{2,3,4,5\}\), so \(c\ge6\), as claimed.

## Verification
The accompanying `verify.py` recomputes the fixed abundancy product, the prime cutoff, all four reduced quotients for \(I(u)\), and the small denominator obstructions. Its recorded output is

`VERIFY_OK core=993/400 cutoff_prime=149 rejected_31_exponents=2,3,4,5`

The script is a regression check for the exact arithmetic. The universal proof is the symbolic argument above; no finite search is used to infer the theorem.

## Relationship to prior work
Almeida and Cardoso prove that a \(5/2\)-perfect integer divisible by \(5\), if one exists, must satisfy \(2^4\parallel N\), \(5^2\parallel N\), and \(31^2\mid N\). Their proof ends with the \(31^2\)-divisibility conclusion and does not give the stronger \(31^6\)-divisibility or the cutoff \(q\ge149\) for all additional prime divisors.

OEIS A141643 tabulates the known integers with abundancy index \(5/2\): \(24\), \(91963648\), and \(10200236032\), and reports that no additional terms are known below \(10^{12}\). None of these listed values is divisible by \(5\). That table is consistent with, but is not used to prove, the present necessary conditions.

## Limitations
The argument does not prove existence or nonexistence of a \(5/2\)-perfect integer divisible by \(5\). It does not show that the exponent \(6\) of \(31\) is attainable, nor does it classify possible primes at or above \(149\). The result depends on the published Almeida--Cardoso theorem for the initial exact \(2\)- and \(5\)-adic valuations and the initial \(31^2\)-divisibility.

## References
1. P. J. Almeida and G. Cardoso, “An Extension of the Euclid-Euler Theorem to Certain \(\alpha\)-Perfect Numbers,” *Journal of Integer Sequences* 25 (2022), Article 22.8.4, published October 14, 2022. Full text: https://cs.uwaterloo.ca/journals/JIS/VOL25/Almeida/almeida9.pdf
2. OEIS Foundation Inc., OEIS A141643, “Numbers \(k\) such that \(\sigma(k)/k=5/2\),” https://oeis.org/A141643
