# Six nondegenerate Schenker branches at 2339

## Finding

For positive integers \(n\), let \(A_n=\sum_{j=0}^n(n!/j!)n^j\) and take \(p=2339\). The six nonzero zeros modulo \(p\) are \(156,470,520,589,1092,2170\). Each satisfies the nondegeneracy criterion of Miska's Theorem 1. Consequently for every integer \(k\ge1\), \(p^k\mid A_n\) has exactly six classes modulo \(p^k\) among positive indices with \(p\nmid n\), one above each of those residues. The classes modulo \(p^2\), in the same order, are
\[
3595199,\quad 1015596,\quad 3195594,\quad 2479929,\quad 2054734,\quad 2820665.
\]

## Assumptions and scope

All indices are positive. A class modulo \(p^k\) is called nonzero here only if its reduction modulo \(p\) is nonzero. The prime \(p\) is fixed throughout the lifting assertion. The minimality of \(2339\) for having six level-one roots, and the level-one root list, are already established in [1]; the contribution here is the nondegenerate lifting classification and the explicit next level at this prime.

## Proof

For a unit index \(n\), the normalized sum \(n^{-n}A_n\) modulo \(p\) equals \(\sum_{k=0}^{n}\prod_{i=0}^{k-1}(1-i/n)\), by reversing the summation index. Every term with \(k\ge p\) vanishes modulo \(p\), since the first \(p\) factors include an \(i\equiv n\pmod p\). Extending the sum to \(p-1\) if \(n<p-1\) adds only zero terms, since each added product contains the factor with \(i=n\). The resulting normalized sum depends only on \(n\bmod p\). Normalization is by a unit, so the level-one root test depends only on that residue as well.

Use the six level-one roots from [1]. They can also be reproduced by evaluating \(A_r\bmod p\) at each integer \(1\le r<p\). A modular Horner rule valid for any positive modulus starts with \(c=u=1\) and, for \(j=n,n-1,\ldots,1\), updates \(c\leftarrow jc\) and then \(u\leftarrow nu+c\), reducing both modulo the modulus. In this rule \(c\) successively equals the coefficients \(n!/(j-1)!\) modulo the modulus, and the output \(u\) is \(A_n\) modulo that modulus.

For a level-one root \(r\), compute
\[
Q_{r,p}=A_{r+p}-A_r (r+p)^{r+2}r^{p-r-2}.
\]
The exponents here are nonnegative for all six roots. Horner evaluation modulo \(p^2\) and modular exponentiation give a representative of \(Q_{r,p}\bmod p^2\) divisible by \(p\) in each case. The divided residue and the verified level-two root \(r+tp\) are as follows.

| \(r\) | \(Q_{r,p}/p\bmod p\) | \(t\) | \(r+tp\) |
| ---: | ---: | ---: | ---: |
| 156 | 843 | 1537 | 3595199 |
| 470 | 1662 | 434 | 1015596 |
| 520 | 1732 | 1366 | 3195594 |
| 589 | 24 | 1060 | 2479929 |
| 1092 | 685 | 878 | 2054734 |
| 2170 | 1079 | 1205 | 2820665 |

Each divided residue is nonzero modulo \(p\), and applying the Horner rule at each displayed \(r+tp\) yields zero modulo \(p^2\). By the final assertion in Miska's Theorem 1 [2], for a prime \(p\) and a unit index \(r\) with \(p\mid A_r\) and \(Q_{r,p}\not\equiv0\pmod{p^2}\), there is precisely one root class modulo \(p^k\) above \(r\) for every \(k\ge1\). The six calculated divided residues verify that hypothesis. The classes above distinct \(r\) are disjoint. Every unit-index root at level \(k\) must first be a root modulo \(p\); the level-one list is complete, so the six branches exhaust all possibilities. In particular the six directly verified level-two roots must be the unique lifts there.

## Verification

The supplied `verify_schenker.cpp` checks the level-one roots in its finite census, the six divided residues, and the six explicit lifts. Build with `c++ -O2 -std=c++17 verify_schenker.cpp -o verify_schenker` and run `./verify_schenker`. The census retained in `schenker_census.csv` corroborates [1] and is not a new minimality result. The arithmetic does not itself enumerate the higher levels; the theorem applies at every depth after the six nondegeneracy checks.

## Relationship to prior work and limitations

The first six-root prime and its level-one root set are from [1], which confines its classification to level one. Miska [2] supplies the general conditional lifting theorem, not the six nonvanishing premises and next-level digits at this prime. A table of Schenker primes such as OEIS A219546 records only whether a prime has any nonzero root; it does not determine nondegeneracy or higher-level residues. The exact prime-power decomposition at the first six-root prime distinguishes persistence of all six roots from singular lifting behavior under the same theorem. No claim is made about non-unit indices, larger multiplicity thresholds, or the branch structure at other primes.

## References

1. *The first Schenker prime with six nonzero zero classes*, Resultary, [published record](https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-the-first-schenker-prime-with-six-nonzero-zero-classes--007dd404ce57), Finding and scope.
2. P. Miska, *A note on p-adic valuations of the Schenker sums*, [arXiv:1401.1717v1](https://arxiv.org/html/1401.1717v1), Theorem 1 and Section 4.
3. [OEIS A219546](https://oeis.org/A219546), *Schenker primes*.
