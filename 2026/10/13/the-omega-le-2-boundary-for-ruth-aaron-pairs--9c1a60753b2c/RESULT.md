# The \(\Omega\le 2\) boundary for Ruth--Aaron pairs
## Finding
Let \(S(n)=\sum_p p\nu_p(n)\) be the sum of prime factors of \(n\), counted with multiplicity, and let \(\Omega(n)=\sum_p\nu_p(n)\). For every integer \(n\ge2\),
\[
S(n)=S(n+1),\qquad \Omega(n)\le2,\qquad \Omega(n+1)\le2
\]
holds if and only if \(n=5\). Thus \((5,6)\) is the unique ordinary multiplicity Ruth--Aaron pair whose two entries are each prime or semiprime when multiplicity is counted. In particular, two consecutive semiprimes can never form such a pair.

## Assumptions and scope
A prime is counted with its exponent in \(S\) and in \(\Omega\). Thus a semiprime means a positive integer with \(\Omega=2\), allowing a square of a prime. The assertion concerns consecutive positive integers \(n,n+1\) with \(n\ge2\), and uses the ordinary multiplicity convention for Ruth--Aaron pairs.

## Proof
There are four factor-complexity cases.

If both entries are prime, the only consecutive prime pair is \((2,3)\), and its two values of \(S\) are unequal.

Suppose \(n=p\) is prime and \(n+1=ab\), where \(a,b\) are primes, not necessarily distinct. The Ruth--Aaron equality gives \(p=a+b\), while consecutiveness gives \(p=ab-1\). Hence
\[
(a-1)(b-1)=ab-a-b+1=2.
\]
The only positive factorization compatible with prime \(a,b\) is \(\{a,b\}=\{2,3\}\), so \((n,n+1)=(5,6)\). Conversely, \(S(5)=5=S(6)\).

Suppose \(n=ab\) is semiprime and \(n+1=q\) is prime. Then \(a+b=q=ab+1\), so
\[
(a-1)(b-1)=0,
\]
impossible for primes \(a,b\).

Finally suppose both entries are semiprime: \(n=ab\) and \(n+1=cd\), with \(a,b,c,d\) prime and repetitions allowed. Equality of the prime-factor sums gives \(a+b=c+d\), hence \(d=a+b-c\). Substituting into \(cd-ab=1\) yields
\[
1=(c-a)(b-c).
\]
Both integer factors are therefore \(1\), or both are \(-1\). In the first case \(c=a+1\) and \(b=c+1\); consecutive primes \(a,c\) must then be \(2,3\), forcing \(b=4\), not prime. In the second case \(c=a-1\) and \(b=c-1\); consecutive primes \(b,c\) must be \(2,3\), forcing \(a=4\), again impossible. Hence no semiprime--semiprime case exists, completing the classification.

## Verification
The proof is symbolic and bound-free. The accompanying checker independently evaluates \(S\) and \(\Omega\) through \(200000\) and finds only \(n=5\) under the stated low-multiplicity hypotheses. It also checks a finite prime grid for the semiprime--semiprime algebraic obstruction. These finite computations are regression checks only and are not used to establish the universal statement.

## Relationship to prior work
Jiang and Miller define and study generalized Ruth--Aaron numbers and the ordinary multiplicity function \(S\), provide initial tables, and prove asymptotic results. Their inspected paper does not give a classification at the boundary \(\Omega\le2\). The canonical OEIS table for the multiplicity convention lists examples but likewise does not prove this low-factor-complexity theorem. A closely related indexed result proves only that \((5,6)\) is the unique Ruth--Aaron pair containing a prime; that statement does not rule out a pair in which both entries are semiprime. The last case above supplies exactly that missing implication.

## Limitations
This result does not classify Ruth--Aaron pairs once either entry has at least three prime factors counted with multiplicity, and it makes no assertion for alternative conventions that count distinct prime factors only. The originality comparison is limited by the possibility of an unindexed historical or recreational note stating the same semiprime observation.

## References
1. Y. Jiang and S. J. Miller, "Generalizing Ruth-Aaron Numbers," arXiv:2010.14990v1, first public 2020-10-28; later published in *PUMP Journal of Undergraduate Research* 4 (2021), DOI 10.46787/pump.v4i0.2458.
2. OEIS A039752, Ruth--Aaron numbers for the prime-factor-sum convention with multiplicity.
