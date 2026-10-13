# Review

## Correctness
PASS. A one-digit transition \(x\mapsto y\) implies
\[
x^2\equiv y\pmod{\ell},
\qquad
\ell=b-1.
\]
For a nontrivial two-cycle with prime \(\ell\), composition gives
\[
x^3\equiv1\pmod\ell,
\]
so the two states must be exactly the two nontrivial cube roots of unity. Their integer sum is \(\ell-1\). The forward transition from the smaller root is automatic after checking the quotient range. The reverse transition is equivalent to a single quotient bound, which expands exactly to
\[
u^2-(3\ell-1)u+(\ell-1)^2\le0.
\]
All boundary states and the primes \(\ell=2,3\) are excluded correctly. A direct exhaustive replay for every prime below \(20000\) agrees with the theorem.

## Originality
PASS. Iannucci's 2000 paper completely classifies fixed points of the same square-split construction through unitary divisors of \(N-1\), and explicitly includes arbitrary bases. Iannucci--Foster 2005 develops cubic fixed-point analogues. Neither inspected primary source treats the one-digit period-\(2\) classification. Public cycle tables contain examples such as the base-\(8\) cycle but do not state the cubic-root rigidity or the exact digit-bound criterion.

Searches using Kaprekar-cycle, amicable/sociable, cube-root-of-unity, prime-\(b-1\), and base-\(8\) aliases found no equivalent theorem. The remaining risk is an unindexed recreational observation.

## Value
PASS. Periodic points are the natural dynamical extension of the classical Kaprekar fixed-point problem. The modulus \(b-1\) is already the organizing modulus in the fixed-point theory, so the prime-\(b-1\) stratum is structural rather than arbitrary. The theorem completely resolves its first nontrivial dynamical layer: there is at most one one-digit two-cycle, its candidate is cyclotomic, and existence is decided by one explicit inequality.

Self-review: passed. Independent audit: not yet performed.
