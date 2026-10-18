# Complete five-prime-support classification of Jacobsthal gaps

## Finding

Let \(J(n)\) be the smallest integer \(m\ge1\) such that every block of \(m\) consecutive integers contains an integer coprime to \(n\), and let \(\omega(n)\) count distinct prime divisors. For every positive integer \(n\) satisfying \(\omega(n)=5\), the following table is exhaustive and its conditions are disjoint:

| Conditions on prime divisibility | \(J(n)\) |
|---|---:|
| \(2\mid n,\ 3\mid n,\ 5\mid n\) | \(14\) |
| \(2\mid n,\ 3\mid n,\ 5\nmid n\) | \(12\) |
| \(2\mid n,\ 3\nmid n\) | \(10\) |
| \(2\nmid n,\ 3\mid n,\ 5\mid n,\ 7\mid n\) | \(11\) |
| \(2\nmid n,\ 3\mid n,\ 5\mid n,\ 7\nmid n\) | \(9\) |
| \(2\nmid n,\ 3\mid n,\ 5\nmid n\) | \(8\) |
| \(2\nmid n,\ 3\nmid n,\ 5\mid n\) | \(7\) |
| \(2\nmid n,\ 3\nmid n,\ 5\nmid n\) | \(6\) |

In particular, the exact spectrum on integers with five distinct prime factors is \(\{6,7,8,9,10,11,12,14\}\); the value is determined entirely by membership of \(2,3,5,7\) in the prime support, independent of the other primes and all exponents.

## Assumptions and scope

All integers \(n>1\) with exactly five distinct prime factors are included; no squarefreeness hypothesis is imposed. The definition of \(J(n)\) concerns blocks anywhere in the integers. Because coprimality depends only on the radical, multiplicities of prime factors never affect \(J(n)\).

## Proof

**Residue-cover criterion.** For any finite set \(P\) of distinct primes and integer \(m\ge1\), a block of \(m\) integers all noncoprime to \(\prod_{p\in P}p\) exists if and only if \(\{0,\ldots,m-1\}\) is covered by one residue class modulo each \(p\in P\). Indeed, starting from a block gives those residues, and conversely the Chinese remainder theorem simultaneously realizes independently selected classes by choosing the starting integer. Thus \(J(n)-1\) is the largest coverable block length.

**Odd integers having five prime factors.** Set \(S=\{p\in\{3,5,7\}:p\mid n\}\) and \(q=5-|S|\). Every other prime divisor is at least \(11\), so in a block of at most \(11\) positions each such prime covers at most one position. It is therefore enough to determine the smallest number of uncovered positions when one residue class is chosen for each prime in \(S\). Define
\[
U_S(m)=\min_{0\le r_p<p\ (p\in S)}\left(m-\left|\bigcup_{p\in S}\{i:0\le i<m,\ i\equiv r_p\pmod p\}\right|\right).
\]
The \(q\) remaining primes can each be assigned, by CRT, to any one distinct uncovered position; hence a length \(m\le11\) is coverable exactly when \(U_S(m)\le q\). Exhausting the at most \(3\cdot5\cdot7=105\) residue tuples gives the following *complete finite certificate*. Entries in the last three columns are independently regenerable by `verify.py`:

| \(S\) | \(q\) | \(j\) | \(U_S(j-1)\) | \(U_S(j)\) | \(U_S(11)\) |
|---|---:|---:|---:|---:|---:|
| \(\varnothing\) | 5 | 6 | 5 | 6 | 11 |
| \(\{3\}\) | 4 | 8 | 4 | 5 | 7 |
| \(\{5\}\) | 4 | 7 | 4 | 5 | 8 |
| \(\{7\}\) | 4 | 6 | 4 | 5 | 9 |
| \(\{3,5\}\) | 3 | 9 | 3 | 4 | 5 |
| \(\{3,7\}\) | 3 | 8 | 3 | 4 | 5 |
| \(\{5,7\}\) | 3 | 7 | 3 | 4 | 6 |
| \(\{3,5,7\}\) | 2 | 11 | 2 | 3 | 3 |

For each row a length \(j-1\) block is coverable and a length \(j\) block is not. No length \(11\) block is coverable in any row because \(U_S(11)>q\), which also excludes all longer blocks. Monotonicity under taking subblocks proves the five odd cases.

**Even integers having five prime factors.** For odd \(a\), \(J(2a)=2J(a)\): even numbers are excluded, and, as two is invertible modulo \(a\), consecutive odd numbers, divided by two modulo \(a\), correspond bijectively to consecutive integers modulo \(a\). The largest run of even-or-noncoprime odd numbers therefore has length exactly \(2(J(a)-1)+1\). It remains to determine \(J(a)\) for odd \(a\) having four prime factors.

If \(3\nmid a\), the four primes are at least five: they cover any prescribed four positions separately, but none can cover more than one of five positions, so \(J(a)=5\). If \(3\mid a\) and \(5\nmid a\), the class modulo three can cover two of five consecutive positions and the other three primes can each cover one; in six positions the total capacity is at most five, so \(J(a)=6\). If \(15\mid a\), the primes three and five can cover disjoint pairs in six positions, and the other two primes cover the remaining two, so a six-position cover exists. In seven positions, to cover all seven with two additional singletons the class modulo three must hit \(\{0,3,6\}\) and the class modulo five must hit either \(\{0,5\}\) or \(\{1,6\}\), necessarily overlapping. Hence \(J(a)=7\). Doubling yields precisely the three even cases \(10,12,14\). These exhaust all \(\omega(n)=5\) cases.

## Verification

The standalone Python 3 program `verify.py` exhausts each of the eight small-prime residue systems and confirms the certificate values at lengths \(j-1\), \(j\), and \(11\). It also independently scans the complete period of eight representative five-prime radicals using the gcd definition, one example for each claimed value; all eight periodic scans agree. This is a finite exhaustive verification of the only finite lemma, not extrapolation from sampled integers to arbitrary prime factors. The infinite quantifier is supplied by the CRT and the prime-\(\ge11\) singleton argument.

## Relationship to prior work

Hagedorn (2008) computes the Jacobsthal values for primorial supports. Hajdu and Saradha (2012) prove that the maximum over all integers with \(r\) distinct primes agrees with the primorial value for \(r\le23\), and characterize mandatory divisors at the maximizing supports; in particular the known value \(H(5)=14\) is recovered here, *not claimed as novel*. Their published covering lemma and doubling identity are antecedents of the proof. The contribution isolated here is the eight-way exact classification for **all** five-prime supports, including nonmaximal strata and rigidity under arbitrary large-prime replacements. Costello and Watts (2013) give general upper bounds, not this support-resolved classification. The OEIS Jacobsthal records list values and maxima, not an equivalent five-prime-support rule.

## Limitations

This is only the case of exactly five distinct prime factors; no claim about the complete spectra at larger support sizes is made. The proof contains a finite 105-tuple residue-class enumeration reproduced by the standalone checker; it is exact only because the preceding reduction proves exhaustiveness. A similar derivation may be implicit in uncatalogued earlier work, and Hagedorn's full paper was not materially available during comparison. Independent mathematical audit and independent novelty certification have not been performed.

## References

1. T. R. Hagedorn, *Computation of Jacobsthal's function \(h(n)\) for \(n<50\)*, Mathematics of Computation 78 (2009), 1073–1087; electronically public 2008-11-20. DOI: 10.1090/S0025-5718-08-02166-2.
2. L. Hajdu and N. Saradha, *Disproof of a conjecture of Jacobsthal*, Mathematics of Computation 81 (2012), 2461–2471, especially Theorems 1.2–1.3, Lemmas 2.1–2.2, and the covering algorithm. DOI: 10.1090/S0025-5718-2012-02581-6. Public full text: https://math.unideb.hu/sites/default/files/inline-files/jacobsrevsaradha.pdf.
3. F. Costello and P. Watts, *A short note on Jacobsthal's function*, 2013, arXiv:1306.1064v1.
4. OEIS A048669, Jacobsthal function; OEIS A395279, maximum with specified prime-factor count.
