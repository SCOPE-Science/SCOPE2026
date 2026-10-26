# Scientific review

## Correctness

**PASS.** A direct subset-sum proof establishes that \(2^tp\) is Zumkeller for the indicated \(t\), and coprime multiplication preserves the property. The modulus \(2p(2^tp)\) has no prime factors other than \(2\) and \(p\), so every eligible odd \(n\) gives a coprime progression. The uniform Linnik bound with exponent \(5\) gives a prime \(q=O(p^{15})\); for \(p\le2n^\delta\), \(\delta<1/15\), this and the seed are \(o(n)\). An interval contains asymptotically \(n^\delta/(\delta\log n)\) prime parameters; at most \(\lfloor1/\delta\rfloor\) divide \(n\), and at most that number divide any fixed second summand. The lower bound and all quantifiers follow. There is no numerical extrapolation.

## Originality

**PASS, subject to literature risk.** Li's 2026 Lemma 3.1 is a uniform one-parameter existence result; the present statement obtains a pointwise polynomial *number of distinct additive representations* by packing simultaneously many parameter primes and controlling collisions through prime support. Li's Theorem 1.2 and an earlier accessible result give exceptional-set density upper bounds, neither of which implies pointwise multiplicity or finiteness of odd exceptions. Somu–Kukla–Tran explicitly leave the exact odd problem as Conjecture 4.20; Proposition 4.12 leaves the residue class \(3\pmod{18}\) open. Searches for equivalent formulation, stronger uniform coverage, and exact tables identified no directly covering theorem. A short implicit argument in older unindexed work remains possible.

## Value

**PASS.** Establishing polynomially many decompositions for **each** sufficiently large odd integer, rather than a density-one statement, is a meaningful strengthening in an active additive-representation problem. It resolves the asymptotic parity-exception question and establishes the large-number part of a natural explicit published conjecture. The quantitative prime-support packing is not a mere repackaging of a finite table or a routine parameter substitution.

## Limits and attribution

The proof uses standard Linnik and prime-number theorems and builds on the published single-parameter construction; those ingredients are credited. It does not prove the exact \(8,21\) cutoff conjecture, locate an effective threshold, or remove known even exceptions. Independent external mathematical validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
