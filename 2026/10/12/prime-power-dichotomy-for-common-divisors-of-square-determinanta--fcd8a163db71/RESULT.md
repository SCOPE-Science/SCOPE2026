# Prime-power dichotomy for common divisors of square determinantal degrees
## Finding
For integers
\[
n\ge2,
\qquad
1\le r\le n-1,
\]
let
\[
X_{n,r}\subset\mathbb P^{n^2-1}_{\mathbb C}
\]
be the projective determinantal variety of complex \(n\times n\) matrices of rank at most \(r\), and write
\[
D_{n,r}=\deg X_{n,r}.
\]
Define the common divisor of the singular-rank tower by
\[
G_n=\gcd_{1\le r\le n-1}D_{n,r}.
\]

Then the tower has a nontrivial common prime divisor if and only if \(n\) is a prime power.

More precisely:

* if
  \[
  n=p^e
  \]
  for a prime \(p\), then
  \[
  p\mid D_{n,r}
  \]
  for every \(1\le r\le n-1\), and \(p\) is the only prime that can divide \(G_n\);
* if \(n\) has at least two distinct prime divisors, then
  \[
  G_n=1.
  \]

The second assertion has an explicit witness for every prime divisor. If
\[
p\mid n,
\qquad
c=p^{\nu_p(n)},
\]
and \(n\) is not a power of \(p\), then the rank
\[
r=n-c
\]
satisfies
\[
p\nmid D_{n,r}.
\]

Thus the set of common prime divisors of all proper square determinantal degrees is empty unless the matrix size is a prime power; in the prime-power case it consists of the underlying prime alone.

## Assumptions and scope
The base field is \(\mathbb C\), and all degrees are projective degrees in the standard projective space of matrix entries.

The full-space stratum \(r=n\), whose degree is \(1\), is excluded. The hypersurface stratum \(r=n-1\) is included and has degree
\[
D_{n,n-1}=n.
\]
Consequently every common prime divisor must already divide \(n\).

The theorem classifies the prime support of \(G_n\). It does not determine the exact exponent of the common prime when \(n\) is a nontrivial prime power.

## Proof
Put
\[
c=n-r,
\qquad
1\le c\le n-1.
\]
The classical determinantal degree formula is
\[
D_{n,n-c}
=
\prod_{j=0}^{c-1}
\frac{(n+j)!\,j!}{(n-c+j)!\,(c+j)!}
=
\prod_{j=0}^{c-1}
\frac{\binom{n+j}{c}}{\binom{c+j}{c}}.
\]
Equivalently, by the dual Jacobi--Trudi determinant for the rectangular Schur class,
\[
D_{n,n-c}
=
\det\!\left[\binom{n}{c-i+j}\right]_{1\le i,j\le c},
\]
with binomial coefficients outside the range \(0,\ldots,n\) interpreted as zero.

First suppose
\[
n=p^e
\]
for a prime \(p\). Lucas's theorem gives
\[
\binom{p^e}{k}\equiv0\pmod p
\]
for every
\[
0<k<p^e.
\]
In the determinant above, every diagonal or lower-triangular entry has index
\[
1\le c-i+j\le c<n,
\]
so it vanishes modulo \(p\). An entry can be nonzero modulo \(p\) above the diagonal only when its binomial index is exactly \(n\); indices larger than \(n\) give zero. Hence the whole matrix is strictly upper triangular modulo \(p\). Therefore
\[
p\mid D_{n,n-c}
\]
for every \(1\le c\le n-1\).

Since
\[
D_{n,n-1}=n=p^e,
\]
no prime other than \(p\) can divide the common gcd. Thus \(p\) is exactly the common prime support.

Now suppose \(n\) is not a power of a prime \(p\) dividing \(n\). Write
\[
n=p^e m,
\qquad
p\nmid m,
\qquad
m>1,
\]
and set
\[
c=p^e.
\]
Then \(c<n\). In the localized ring at \(p\), use the product formula
\[
D_{n,n-c}
=
\prod_{j=0}^{c-1}
\frac{\binom{n+j}{c}}{\binom{c+j}{c}}.
\]
For \(0\le j<c\), Lucas's theorem gives
\[
\binom{n+j}{c}\equiv m\pmod p,
\qquad
\binom{c+j}{c}\equiv1\pmod p.
\]
Indeed, \(c=p^e\) has a single nonzero base-\(p\) digit, while adding \(j<c\) changes only the lower \(e\) digits. Hence every factor is a \(p\)-adic unit, and therefore
\[
p\nmid D_{n,n-c}.
\]

Finally, every prime divisor of \(G_n\) must divide
\[
D_{n,n-1}=n.
\]
If \(n\) has at least two distinct prime divisors, the preceding construction removes each prime divisor of \(n\) from at least one determinantal degree. Hence no prime divides every degree and
\[
G_n=1.
\]
This proves the dichotomy.

## Verification
The bundled exact checker evaluates the Harris--Tu product and the Jacobi--Trudi determinant independently for all
\[
2\le n\le32
\]
and every proper rank stratum, confirming exact agreement.

It then computes the full gcd tower for all
\[
2\le n\le120
\]
and verifies the prime-support dichotomy. For every non-prime-power \(n\) in that range and every prime \(p\mid n\), it also checks the explicit witness
\[
c=p^{\nu_p(n)}.
\]

Finite computation is regression evidence only. The infinite theorem follows from the two Lucas-theorem arguments in the proof.

## Relationship to prior work
The degree formula for generic determinantal varieties is classical. Friedland and Krattenthaler reproduce the Harris--Tu product and study parity of individual determinantal degrees, with a plane-partition interpretation. Their analysis emphasizes the prime \(2\) and gives recursive and binary criteria for individual ranks.

Algebraic-geometric work on bounded-rank matrix varieties treats the same nested rank loci as central projective varieties, including their singular stratification and related enumerative invariants.

The statement proved here is different in quantifier and arithmetic content: it asks which primes divide every proper rank-stratum degree for a fixed square matrix size. Targeted searches for common gcds across the entire rank tower, prime-power criteria, and explicit prime-avoiding strata did not locate an equivalent theorem. The proof combines the Schur-determinant form of the degree with Lucas's theorem in two complementary directions.

## Limitations
When \(n=p^e\) with \(e>1\), the theorem identifies the unique common prime but does not determine the exact exponent of \(p\) in \(G_n\).

The result is for generic square matrices. Rectangular, symmetric, and skew-symmetric determinantal varieties have different degree formulas and are not covered.

The closest arithmetic source studies parity of individual degree formulas in substantial detail, so an equivalent all-ranks prime-support statement could exist in unindexed combinatorial literature on plane partitions or rectangular Schur values.

## References
Jonathan Hauenstein, Jose Rodriguez, and Bernd Sturmfels, *Maximum Likelihood for Matrices with Rank Constraints*, arXiv:1210.0198, first submitted 30 September 2012.

Shmuel Friedland and Christian Krattenthaler, *2-adic valuations of certain ratios of products of factorials and applications*, arXiv:math/0508498, first submitted 25 August 2005.

Joe Harris and Loring W. Tu, *On symmetric and skew-symmetric determinantal varieties*, *Topology* 23 (1984), 71--84.
