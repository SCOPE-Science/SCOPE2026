# Nine consecutive odd-exponent obstructions for pristine numbers

## Finding

Let \(a(1)=1\) and \(a(n)=1+\sum_{m\mid n,\,m<n}a(m)\) for every \(n>1\). An integer \(n\) is *pristine* if \(a(n)=n\). For every
\[
d\in\{9,11,13,15,17,19,21,23,25\},\qquad c\ge1,\qquad q\text{ an odd prime},
\]
there is **no** pristine integer of the form \(2^c q^d\).

In fact, the following factorial-divisor sieve underlies the complete nine-exponent classification. For each listed \(d\), define
\[
P_d(X)=\sum_{i=0}^{d}\binom{d}{i}\binom{X+i}{i},\qquad F_d=d!,
\]
\[
Q_d(X)=\frac{d!P_d(X)}{X+d+1}\in\mathbb Z[X],\qquad K_d=Q_d(-d-1)\ne0.
\]
If \(P_d(c)=q^d\) with \(c\ge1\) and \(q\) an odd prime, then necessarily
\[
\boxed{\ c+d+1\mid d!\quad\text{or}\quad q\mid K_d.\ }
\]
Both sets of possibilities are finite and exhaustively eliminated below. This establishes nonexistence for unbounded \(c\) and \(q\), not merely below a numerical cutoff.

## Assumptions and scope

All factorials, binomial coefficients, and products use exact integers. For a polynomial variable \(X\), the generalized binomial coefficient \(\binom{X+i}{i}\) means \(\prod_{j=1}^{i}(X+j)/i!\). The nine specified odd exponents are the entire proved range; no conclusion is asserted for higher odd exponents or even exponents. The restriction \(c\ge1\) and primality of \(q\) are essential to the pristine-number interpretation. The sieve itself is established for all nine specified odd exponents; its construction works for any odd exponent when the corresponding nonzero critical value is available.

## Proof

**1. Reduction to the binomial polynomial.** The recursive-divisor formula for two prime-power blocks gives
\[
a(2^c q^d)=2^c\sum_{i=0}^{d}\binom{d}{i}\binom{c+i}{i}=2^cP_d(c).
\]
Thus \(2^c q^d\) is pristine precisely when \(P_d(c)=q^d\). The identity is also directly derivable from the ordinary ordered-factorization recursion; no assumptions about the size of \(q\) are used.

**2. An integral polynomial factor for odd \(d\).** Because \(d!/i!\) is an integer, \(d!P_d(X)\) belongs to \(\mathbb Z[X]\). At \(X=-d-1\), for \(0\le i\le d\),
\[
\binom{-d-1+i}{i}=(-1)^i\binom di.
\]
For odd \(d\), the sum \(\sum_{i=0}^{d}(-1)^i\binom di^2=0\), since the terms indexed by \(i\) and \(d-i\) cancel. Therefore the monic polynomial \(X+d+1\) divides \(d!P_d(X)\) in \(\mathbb Z[X]\), defining \(Q_d\). The critical value \(K_d=Q_d(-d-1)\) is an integer. Direct differentiation, or exact polynomial division, gives the explicitly evaluable identity
\[
K_d=d!\sum_{j=0}^{(d-1)/2}\frac{(-1)^j\binom dj}{d-2j}.
\]
For completeness, the identity follows by taking the linear coefficient in \(u\) of
\[
P_d(-d-1-u)=(-1)^d[z^d](1-z^2)^d(1+z)^u,
\]
then using the odd powers in the series for \(\log(1+z)\). The exact verifier also computes \(K_d\) by independent integer polynomial division and checks that the two expressions agree.

**3. The factorial-divisor/exceptional-prime dichotomy.** Fix \(c\ge1\), put \(m=c+d+1\), and suppose \(P_d(c)=q^d\) for an odd prime \(q\). Then
\[
mQ_d(c)=d!q^d.
\]
The first two terms in the positive binomial sum give
\[
P_d(c)\ge 1+d(c+1)>c+d+1=m,
\]
because \(d\ge9\) and \(c\ge1\). Hence \(Q_d(c)=d!P_d(c)/m>d!\). If \(q\nmid K_d\) and \(q\mid m\), polynomial congruence gives \(Q_d(c)\equiv Q_d(-d-1)=K_d\not\equiv0\pmod q\). Since \(Q_d(c)\mid d!q^d\) and \(q\nmid Q_d(c)\), we would have \(Q_d(c)\mid d!\), contradicting \(Q_d(c)>d!\). Therefore \(q\nmid m\). Returning to \(mQ_d(c)=d!q^d\), coprimality now forces \(m\mid d!\).

Thus a solution always belongs to one of two exhaustive branches: (A) \(c=m-d-1\) for a positive divisor \(m\) of \(d!\) with \(m\ge d+2\), or (B) \(q\) is an odd prime dividing \(K_d\). These branches may overlap; no disjointness is needed.

**4. Certified finite exhaustion.** For branch (A), generate all divisors of \(d!\) from its exact prime factorization, retain precisely \(m\ge d+2\), and test whether the corresponding exact integer \(P_d(m-d-1)\) is an odd perfect \(d\)-th power. For branch (B), factor the known integer \(K_d\) using all primes at most \(d\), check that the residual cofactor is exactly \(1\), and for each odd prime factor \(q\) solve the monotone equation \(P_d(c)=q^d\) by a doubling bracket and integer binary search. Strict increase of \(P_d(c)\) for \(c\ge1\) follows termwise from its defining binomial sum, so at most one \(c\) could solve each fixed exceptional equation. The integer-root routine uses downward integer Newton iteration from a certified upper bound, finishing with two exact power comparisons; no floating-point arithmetic occurs.

The complete exact counts are:

| \(d\) | Divisors of \(d!\) | Admissible \(c\) in branch (A) | Odd prime factors of \(K_d\) | Solutions |
|---:|---:|---:|:---|:---|
| 9 | 160 | 150 | 3 | none |
| 11 | 540 | 528 | 3, 5 | none |
| 13 | 1,584 | 1,570 | 3, 5 | none |
| 15 | 4,032 | 4,016 | 3, 5, 7 | none |
| 17 | 10,752 | 10,734 | 3, 5, 7 | none |
| 19 | 29,376 | 29,356 | 3, 5, 7 | none |
| 21 | 60,800 | 60,778 | 3, 5, 7 | none |
| 23 | 192,000 | 191,976 | 3, 5, 7, 11 | none |
| 25 | 340,032 | 340,006 | 3, 5, 7, 11 | none |

There are \(639114\) branch-(A) candidates altogether and no odd perfect powers among them. Every possible branch-(B) prime is explicitly checked, with no equality. Since the two branches cover every hypothetical solution, the claimed nonexistence follows for every positive \(c\) and every odd prime \(q\).

## Verification

Run `python3 verify.py` using Python 3 with standard-library arbitrary-precision integer arithmetic. The saved output in `verification_output.txt` ends with `VERIFY_OK` and documents all nine cases and \(639114\) integer-root checks. The program builds \(d!P_d(X)\) over integer coefficients, divides by \(X+d+1\), and independently checks its critical value against a finite rational sum; it enumerates **all** divisors of \(d!\) by prime-power products, proves each factorization is complete, checks every candidate via exact integer root, and completes the exceptional-prime search by monotone binary search. The finite computation is exhaustive only because Step 3 proves a bound-free reduction to the two finite branches; direct testing to a large value of \(c\) alone would not be a proof.

## Relationship to prior work

The original recursive-divisor function was introduced in Fink's *Recursively divisible numbers* (public preprint 17 December 2019, journal version 2024, first-listed MSC 11A25). Fink's *Recursively abundant and recursively perfect numbers* (public preprint 24 August 2020) defines pristine integers and gives the exact binomial equation, eliminates odd exponents \(3\) and \(5\), and proves a general upper bound on the number of solutions for a fixed odd exponent. The integer factor \(X+d+1\) is already present in that paper, and is **not** claimed as new here. A later published result excludes exponent \(7\). None of those statements implies nonexistence in the nine odd exponent layers \(9\) through \(25\). The new contribution is the prime-incidence sieve using \(K_d\), together with an unrestricted exact classification in those nine layers. Formulae expressing the recursive-divisor function by other special functions likewise do not by themselves decide these prime-power Diophantine equations.

## Limitations

The argument does not settle Fink's question for all odd exponents: it leaves \(d\ge27\) untreated. The computer program is part of the **finite** completeness proof and requires separate reproduction and mathematical scrutiny for external assurance. A potentially unindexed derivation of the same polynomial sieve or a later full classification remains a bibliographic originality risk. The source associated with the earlier 2019 paper was compared using its available abstract and classification metadata, whereas the later 2020 pristine-number paper was inspected in substantive full text; this is a limitation of source coverage, not an assertion of uniqueness.

## References

1. T. Fink, *Recursively divisible numbers*, arXiv:1912.07979 (first public 2019-12-17); Journal of Number Theory 256 (2024), 37 ff., DOI 10.1016/j.jnt.2023.08.008. Bibliographic MSC data: https://portal.mardi4nfdi.de/wiki/Publication:6184602.
2. T. Fink, *Recursively abundant and recursively perfect numbers*, arXiv:2008.10398 (first public 2020-08-24), especially Section 4.2, Theorems 5–6; full public text: https://lims.ac.uk/wp-content/uploads/paper4-1-1.pdf.
3. *No pristine number has the form \(2^c q^7\)*, publicly indexed 2026 result, identifier `d65d52b1-5000-49a9-b05c-d7949b665f5b` (only the exponent-\(7\) case is used for comparison).
