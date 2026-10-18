# Rigidity of the \(3^3 r^2 q\) unitary–exponential divisor-sum equality

## Finding
For pairwise distinct primes \(3,r,q\), the equality
\[\sigma^*(3^3r^2q)=\sigma^{(e)}(3^3r^2q)\]
holds exactly when \(r=7\) and \(q=5\). The corresponding integer is \(6615\).

## Assumptions and scope
The unitary divisor sum \(\sigma^*(n)\) is multiplicative, with \(\sigma^*(p^a)=1+p^a\). The exponential divisor sum \(\sigma^{(e)}(n)\) is multiplicative, with \(\sigma^{(e)}(p^a)=\sum_{d\mid a}p^d\). Here \(r\) and \(q\) range over all prime numbers distinct from one another and from \(3\); only the exponents and the cubic prime are fixed. No assertion concerns other prime-exponent patterns or the open infinitude problem for equality of these functions.

## Proof
Since \(\sigma^*(27)=28\), \(\sigma^{(e)}(27)=30\), \(\sigma^*(r^2)=r^2+1\), \(\sigma^{(e)}(r^2)=r^2+r\), \(\sigma^*(q)=q+1\), and \(\sigma^{(e)}(q)=q\), the equation is precisely
\[28(r^2+1)(q+1)=30(r^2+r)q.\]
Equivalently,
\[q(r^2+15r-14)=14(r^2+1),\qquad
q=14-\frac{210(r-1)}{r^2+15r-14}.\]
The denominator is strictly positive for every prime \(r\ge2\). Therefore \(0<q<14\), and its primality restricts it to \(q\in\{2,3,5,7,11,13\}\). The value \(q=3\) is excluded by the pairwise-distinctness hypothesis. For any remaining \(q\), the integer \(r\) must be a root of
\[(q-14)r^2+15qr-14(q+1)=0,\]
whose discriminant is
\[\Delta(q)=281q^2-728q-784.\]
At \(q=2\) this is \(-1116<0\). At \(q=7\) it is \(7889\), strictly between \(88^2\) and \(89^2\). At \(q=11\) it is \(25209\), strictly between \(158^2\) and \(159^2\). At \(q=13\) it is \(37241\), strictly between \(192^2\) and \(193^2\). None gives an integer root. At \(q=5\), the equation becomes
\[9r^2-75r+84=3(3r-4)(r-7)=0,\]
so \(r=7\), the only integral root. Conversely, \(r=7,q=5\) yields \(28\cdot50\cdot6=30\cdot56\cdot5=8400\), proving the equality. The original integer is \(27\cdot49\cdot5=6615\).

## Verification
Every discriminant value and bounding square appears explicitly above. A standalone Python standard-library checker, `verify.py`, re-evaluates the exact formula and enumerates prime \(r\le100000\) as a non-probative cross-check. The infinite proof is the finite \(q<14\) argument and exhaustive exact discriminant check, not the enumeration.

## Relationship to prior work
Trudgian's archival paper introduced the equality question for \(\sigma^*\) and \(\sigma^{(e)}\) and reported \(6615\) among the first known examples. OEIS A236474 also records its presence. Neither the existence of this known example nor a bounded census implies uniqueness within the infinite family \(3^3r^2q\). A published finite-layer classification for \(p^a q\) concerns two prime supports and does not cover this three-prime-support assertion.

## Limitations
The assertion is confined to the fixed cubic prime \(3\), the square exponent on a second prime, and a third prime of exponent one. It is not a classification of all integers with three distinct prime factors, nor an infinitude statement. Novelty rests on the inspected literature and may be affected by an unindexed or differently formulated exact classification.

## References
- T. Trudgian, *The sum of the unitary divisor function*, first submitted 2013-12-17, arXiv:1312.4615, especially Section 4, https://arxiv.org/pdf/1312.4615.
- OEIS Foundation, A236474, *Numbers whose sum of unitary divisors is equal to the sum of exponential divisors*, https://oeis.org/A236474.
