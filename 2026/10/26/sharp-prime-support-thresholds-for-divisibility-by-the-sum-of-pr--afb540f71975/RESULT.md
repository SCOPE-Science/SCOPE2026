# Sharp prime-support thresholds for divisibility by the sum of prime squares

## Finding
For every positive integer \(n\), set
\[
\beta_2(n)=\sum_{p\mid n}p^2,\qquad \omega(n)=\#\{p:p\text{ prime and }p\mid n\}.
\]
Among integers with at least two distinct prime factors, the least possible value of \(\omega(n)\) subject to \(\beta_2(n)\mid n\) is exactly \(4\). Among *odd* integers with at least two distinct prime factors, it is exactly \(5\).

The structural obstruction is stronger: whenever \(p,q,r\) are three distinct primes, some prime \(\ell\equiv3\pmod4\) divides \(p^2+q^2+r^2\) but divides none of \(p,q,r\). Thus multiplying any such three-prime support by arbitrary positive prime powers never makes the prime-square sum a divisor.

## Assumptions and scope
All primes are positive ordinary rational primes, and sums extend over **distinct** prime divisors rather than over prime-power factors with multiplicity. We consider integers \(n\ge2\) with \(\omega(n)\ge2\), expressly excluding prime powers: if \(n=p^a\) with \(a\ge2\), then \(\beta_2(n)=p^2\mid n\), so the support thresholds would be false without this restriction. All exponents of the permitted distinct primes are otherwise arbitrary positive integers. The result concerns the square-power sum only, not other powers.

## Proof
**A prime outside every triple.** Fix three distinct primes \(p,q,r\), and put \(S=p^2+q^2+r^2\). If all three are odd, then \(S\equiv3\pmod4\). By unique factorization, \(S\) has some prime factor \(\ell\equiv3\pmod4\): an integer congruent to \(3\pmod4\) cannot have all its prime factors congruent to \(1\pmod4\). For each of \(p,q,r\), say \(p\), if \(\ell=p\), then \(q^2+r^2\equiv0\pmod\ell\). Since \(q,r\) are nonzero modulo \(\ell\), dividing by \(r^2\) says that \(-1\) is a quadratic residue modulo \(\ell\), impossible for an odd prime \(\ell\equiv3\pmod4\). Thus \(\ell\) is external to the three primes.

If instead exactly one prime is even, relabel it \(p=2\). Every odd square is \(1\pmod8\), hence \(S=4+q^2+r^2\equiv6\pmod8\). Thus \(S/2\equiv3\pmod4\) and again has an odd prime factor \(\ell\equiv3\pmod4\). The same quadratic-residue argument shows \(\ell\ne q,r\); also \(\ell\ne2\). This establishes the assertion in all cases.

**Zero-, one-, two-, and three-support boundaries.** For \(n\) with exactly two distinct prime factors \(p,q\), both \(p^2+q^2\equiv q^2\not\equiv0\pmod p\) and \(p^2+q^2\equiv p^2\not\equiv0\pmod q\); hence \(\gcd(\beta_2(n),n)=1\). As \(\beta_2(n)>1\), it cannot divide \(n\). If \(\omega(n)=3\), the prime-square sum has, by the preceding step, a prime divisor not dividing \(n\), regardless of the positive exponents of its three supported primes. Therefore \(\beta_2(n)\nmid n\) for each \(n\) with \(\omega(n)=2\) or \(3\). Under the stated restriction \(\omega(n)\ge2\), this proves \(\omega(n)\ge4\).

**Odd boundary.** If \(n\) is odd, each supported prime is odd and \(\beta_2(n)\equiv\omega(n)\pmod2\). Divisibility by \(n\) forces \(\beta_2(n)\) odd, so \(\omega(n)\) is odd. Combined with the exclusion of \(\omega(n)=2,3\), it follows that \(\omega(n)\ge5\).

**Sharp witnesses.** The factorizations and exact divisions are
\[
46206=2\cdot3^2\cdot17\cdot151
=2\bigl(2^2+3^2+17^2+151^2\bigr)
=2\cdot23103,
\]
\[
72105=3\cdot5\cdot11\cdot19\cdot23
=69\bigl(3^2+5^2+11^2+19^2+23^2\bigr)
=69\cdot1045.
\]
Each listed factor is prime, and the first and second numbers have precisely four and five distinct prime factors, respectively. The second is odd. The lower bounds are therefore attained and are exact.

## Verification
The accompanying standalone Python 3 program `verify.py` has no external dependencies. Executing `python3 verify.py` returns `VERIFY_OK` after independently factoring all \(3654\) unordered triples among primes not exceeding \(110\), verifying an external \(3\pmod4\) prime divisor of their square sum, examining every integer from \(2\) through \(300000\) for the support thresholds, and checking both exact witness factorizations and divisions. This finite check is corroborative, not an infinite proof; the preceding modular and quadratic-residue argument proves the theorem for every possible prime and exponent.

## Relationship to prior work
De Koninck and Luca's paper *Integers divisible by sums of powers of their prime factors* (available online 23 March 2007) introduces \(\beta_j(n)\) and proves infinitely many non-prime-power simultaneous divisibility examples for every finite family of powers. It does not establish the sharp least prime support for the square-power case. OEIS A190882 lists examples including \(46206\) and \(72105\), and explicitly states only the weaker bound \(\omega(n)\ge3\). The MathPages article *Product Divisible By Sum of Squares* excludes products of at most four **distinct primes**, hence proves a squarefree-only nondivisibility assertion. Its argument does not exclude arbitrary exponents of three distinct primes: for example, \(46206\) shows that repeated factors can change the support threshold. The theorem here supplies an exponent-independent obstruction for exactly three supported primes and derives sharp unrestricted even and odd thresholds. The related De Koninck–Luca paper *Partial Sums of Powers of Prime Factors* studies exact equalities with selected prime-power summands, not the divisibility of the full prime-square sum into a prime-support integer.

## Limitations
The result does not classify all integers with four or more distinct prime factors satisfying divisibility, nor give a counting asymptotic or extend to other power exponents. The proof uses the elementary fact that \(-1\) is not a square modulo a prime congruent to \(3\pmod4\). The prior-art comparison covers the cited accessible full texts and targeted records, not every unindexed publication. The mathematical proof and finite verifier have not received independent external assessment.

## References
1. J.-M. De Koninck and F. Luca, *Integers divisible by sums of powers of their prime factors*, Journal of Number Theory **128** (2008), 557–563; first available online 23 March 2007. DOI: 10.1016/j.jnt.2007.01.010. Author-hosted full text: https://www.jeanmariedekoninck.mat.ulaval.ca/fileadmin/Documents/Publications/2008_integers_divisible_by_sums_of_powers_of_their_prime_factors.pdf
2. OEIS A190882, *Numbers other than prime powers divisible by the sum of the squares of their prime divisors*, originally dated 23 May 2011. https://oeis.org/A190882
3. MathPages, *Product Divisible By Sum of Squares*. https://www.mathpages.com/home/kmath126.htm
4. J.-M. De Koninck and F. Luca, *Partial Sums of Powers of Prime Factors*, Journal of Integer Sequences **10** (2007), Article 07.1.6, published 30 December 2006. https://www.jeanmariedekoninck.mat.ulaval.ca/fileadmin/Documents/Publications/2007_partial_sums_of_powers_of_prime_factors.pdf
