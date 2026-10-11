# Semiprime bottlenecks in the four nonisosceles 120-degree triangle-tiling cases

## Finding

Let a triangle \(T\) with incommensurable angles be tiled by \(N\) congruent copies of a triangle \(R\) with angles
\[
(\alpha,\beta,2\pi/3).
\]
Assume \(T\) is one of the four nonisosceles cases treated in Theorems 18--21 of Beeson. Normalize the side lengths of \(R\), opposite \(\alpha,\beta,2\pi/3\), to coprime positive integers \((a,b,c)\). Then
\[
c^2=a^2+ab+b^2.
\]
For a positive integer \(n\), let \(\Omega(n)\) denote the number of prime factors of \(n\), counted with multiplicity.

Then the four cases have the following exact low-\(\Omega\) profile.

For
\[
T=(\alpha,2\alpha,3\beta),
\]
one has
\[
\Omega(N)\ge4.
\]
For
\[
T=(\alpha,2\beta,2\alpha+\beta),
\]
one has
\[
\Omega(N)\ge3.
\]
For
\[
T=(\alpha,\alpha+\beta,\alpha+2\beta),
\]
one has
\[
\Omega(N)\ge2,
\]
and equality holds if and only if
\[
\lambda^2=b
\quad\text{and}\quad
\Omega(a+b)=2.
\]
In that equality case,
\[
N=a+b.
\]
Finally, for
\[
T=(2\alpha,2\beta,\alpha+\beta),
\]
one has
\[
\Omega(N)\ge2,
\]
and equality holds if and only if
\[
\lambda=1
\]
and both
\[
a+2b
\quad\text{and}\quad
2a+b
\]
are prime. Those two primes are necessarily distinct and at least \(5\).

Thus semiprime tile counts among these four geometric families can occur only through the last two arithmetic gates. The necessary formulas themselves contain arithmetic examples at both gates:
\[
(a,b,c,\lambda,N)=(5,16,19,4,21)
\]
for the \((\alpha,\alpha+\beta,\alpha+2\beta)\) case, and
\[
(a,b,c,\lambda,N)=(3,5,7,1,143)
\]
for the \((2\alpha,2\beta,\alpha+\beta)\) case.

These two examples are not tiling constructions. They show only that the stated factor-count obstruction is sharp at the level of the necessary arithmetic formulas.

## Assumptions and scope

The hypotheses are exactly those under which Beeson obtains the four formulas in Theorems 18--21: the tile has an angle \(2\pi/3\), the relevant angles are incommensurable, and the target is not similar to the tile. Beeson proves that the tile sides are commensurable; they are then normalized to coprime positive integers \((a,b,c)\).

The integer \(\lambda\) is the positive scaling integer appearing in those theorems. No sufficiency statement is made: satisfying one of the displayed factor formulas does not by itself produce a tiling.

A semiprime means a positive integer \(N\) with
\[
\Omega(N)=2,
\]
so squares of primes and products of two distinct primes are both included.

## Proof

Beeson proves
\[
a+b\ \text{is composite}
\]
for every positive integral solution of
\[
c^2=a^2+ab+b^2.
\]
Hence
\[
\Omega(a+b)\ge2.
\]

In the first case, Theorem 18 gives
\[
N=3\lambda^2(a+2b)(a+b).
\]
Since \(a+2b>1\), additivity of \(\Omega\) on products gives
\[
\Omega(N)
=1+2\Omega(\lambda)+\Omega(a+2b)+\Omega(a+b)
\ge1+0+1+2=4.
\]

In the second case, Theorem 19 gives
\[
N=\lambda^2(2a+b)(a+b).
\]
Since \(2a+b>1\),
\[
\Omega(N)
=2\Omega(\lambda)+\Omega(2a+b)+\Omega(a+b)
\ge0+1+2=3.
\]

In the third case, Theorem 20 gives
\[
N=\frac{\lambda^2(a+b)}{b}.
\]
The same theorem proves
\[
\gcd(a+b,b)=1
\]
and therefore
\[
m:=\frac{\lambda^2}{b}
\]
is a positive integer. Thus
\[
N=m(a+b)
\]
and
\[
\Omega(N)=\Omega(m)+\Omega(a+b)\ge2.
\]
Equality \(\Omega(N)=2\) occurs exactly when \(m=1\) and \(\Omega(a+b)=2\). The condition \(m=1\) is exactly
\[
\lambda^2=b,
\]
and then \(N=a+b\).

In the fourth case, Theorem 21 gives
\[
N=\lambda^2(a+2b)(2a+b).
\]
Both linear factors are greater than \(1\), so
\[
\Omega(N)
=2\Omega(\lambda)+\Omega(a+2b)+\Omega(2a+b)
\ge2.
\]
Equality holds exactly when \(\lambda=1\) and each linear factor has exactly one prime factor, hence each is prime.

They cannot be equal: equality would imply \(a=b\), and then
\[
c^2=3a^2,
\]
which has no positive integral solution. Neither prime can equal \(3\). Indeed, \(a+2b=3\) or \(2a+b=3\) with positive integers forces \(a=b=1\), again giving \(c^2=3\). Therefore both primes are distinct and at least \(5\).

For the arithmetic sharpness checks,
\[
19^2=5^2+5\cdot16+16^2,
\]
and with \(\lambda=4\), the third formula gives
\[
N=\frac{4^2(5+16)}{16}=21.
\]
Likewise,
\[
7^2=3^2+3\cdot5+5^2,
\]
and with \(\lambda=1\), the fourth formula gives
\[
N=(3+2\cdot5)(2\cdot3+5)=13\cdot11=143.
\]
Again, these are only arithmetic points on the necessary formulas.

## Verification

The proof is exact and uses only the four published tile-count formulas, the published compositeness lemma for \(a+b\), and elementary additivity of \(\Omega\).

The bundled checker independently enumerates primitive positive triples satisfying
\[
c^2=a^2+ab+b^2
\]
through a finite stress-test range, verifies the lower bounds and both equality characterizations for a range of positive \(\lambda\), and checks the two arithmetic gate examples exactly. The enumeration is not used as a proof of the infinite statement.

## Relationship to prior work

Beeson proves that prime \(N\) is impossible in these nonreptile incommensurable cases and derives the four exact formulas used above. His paper does not state a semiprime classification or a bound in terms of \(\Omega(N)\).

Zhang studies the same \(2\pi/3\)-angle families, gives constructions, and conjectures stronger classifications of the possible tile counts. In particular, the paper highlights the \((5,16,19)\) divisibility problem and gives construction formulas for the \((2\alpha,2\beta,\alpha+\beta)\) family. It does not state the low-prime-factor sieve above. The present result is a necessary arithmetic refinement of Beeson's universal formulas, not a solution of Zhang's sufficiency or divisibility conjectures.

The semiprime statement sharpens the source's prime exclusion in a way that separates the four geometric shapes: two are ruled out already at \(\Omega(N)=2\), while the other two have explicitly characterized arithmetic gates through which a semiprime count could pass.

## Limitations

The result is necessary, not sufficient. In particular, the arithmetic candidates \(N=21\) and \(N=143\) are not asserted to be realizable by tilings.

No classification is given for \(\Omega(N)\ge3\) in the last two cases, nor for the isosceles, equilateral, reptile, or commensurable-angle cases outside the four stated families.

The originality search covered the two primary preprints, their displayed formulas and conjectural classification sections, targeted searches for semiprime and prime-factor formulations, and the current and prior geometry ledgers. Very recent unindexed work remains a residual bibliographic risk.

## References

1. M. Beeson, *Tiling a triangle into a prime number of congruent triangles*, arXiv:2607.23453v1, first public 26 July 2026. Primary MSC 51M20.
2. Y. X. Zhang, *Tiling Triangles with \(2\pi/3\) Angles*, arXiv:2512.22696v1, first public 27 December 2025.
