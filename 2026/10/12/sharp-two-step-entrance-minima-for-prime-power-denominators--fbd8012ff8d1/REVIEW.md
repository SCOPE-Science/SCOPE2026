# Scientific review

## Correctness — PASS
For every reduced \(a/M=q+r/M\), the first reduced denominator is exactly \(d=M/\gcd(q,M)\), and the second iterate is integral exactly when \(d>1\) and \(d\mid q+\lfloor qr/M\rfloor\). The proof checks all possible smaller quotients using \(q\le Q\le2q-1\), identifies the first feasible quotient separately for even prime-power exponents and for odd powers of two and odd primes, and proves that the smallest necessary remainder is coprime to the odd prime. The exceptional denominator two is directly verified. An exact-rational standalone checker matches the formula over the stated finite ranges. There is no extrapolation of finite data to all parameters.

## Originality — PASS, with specific residual risk
The closest source, Carvalho, arXiv:2605.21802v1, develops exact-order residue classes and explicitly asks for \(\mu(M,n)\) in Question 3.5. Its general congruence-class count does not determine the first admissible reduced numerator; its stated exact minimum for denominator two is credited, not claimed. The 2012 Azevedo--Carvalho--Machiavelo paper studies \(x\mapsto x\lceil x\rceil\), a distinct recurrence, and the prime-representing-constant paper gives the iteration without minimum formulas. Published finding searches for the exact map, aliases, exponent parity and strong coverage found no covering statement. Equivalent work outside the searched or indexed literature remains possible.

## Value — PASS
The least starting numerator \(\mu(M,n)\) is explicitly posed as a natural invariant in a recent number-theory paper. The formula gives a complete infinite prime-power classification at the first nontrivial stopping order, including the different square-root quotient thresholds for even and odd valuation and an exceptional binary branch. The result specifies an actual extremizer, proves it is globally least over *all* reduced starting fractions, and is not merely a count of residue classes or a finite computation.

## Boundaries
The original paper already covers \(M=2\) and all stopping orders there. The new classification does not treat orders above two or arbitrary composite denominators. The broader termination conjecture remains open. The independent audit is unperformed, and failure to find unindexed formulations is not proof of absolute novelty.

Self-review: passed. Independent audit: not yet performed.
