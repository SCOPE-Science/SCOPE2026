# Scientific review: succession–fixed-point cross-covariance

## Correctness — PASS

The claimed indexed covariance is obtained directly from the joint-event count: incident fixed points require two specified images, while nonincident fixed points remove one value and either one or two admissible consecutive-value pairs. Explicit subtraction of the marginal product proves all entries for every integer \(n\ge3\); a separate direct enumeration covers \(n=2\). The rank proof reconstructs the full left kernel from the boundary and interior columns and verifies the parity condition without assuming any unproved spectral statement. The aggregate covariance is an exact row/column sum. The accompanying self-contained verifier exhausts sizes \(2\)–\(8\) and checks integer-matrix rank up to size \(40\), corroborating the all-size proof. There is no infinite-proof claim based solely on finite enumeration.

## Originality — PASS (self-review)

The closest work is Diaconis–Evans–Graham, *Unseparated pairs and fixed points in random permutations* (Berkeley Technical Report 822, 2013; arXiv:1308.5459). Their Theorem 1.1 proves equality in distribution of the succession-position set and the restricted fixed-point set, but this does not determine their joint dependence inside the same permutation. Chen–Fu (arXiv:2402.02743) refine related equidistributions and aggregate joint enumerators; these do not give the indexed mixed covariance with fixed points in the same permutation. A prior calculation concerning fixed points and **descent** indicators has distinct conditioning and cannot imply the exact-consecutive-value cross-covariance. Neither the inspected source statements nor the accessible prior claim ledgers provide a dominating result. Risks: an unlocated older mixed enumeration might implicitly yield the formula, and not every historically relevant permutation-statistics article was fully accessible. Thus novelty is assessed against checked sources rather than independently certified priority.

## Mathematical value — PASS

This result investigates how two natural shuffle diagnostics—unseparated adjacent cards and fixed cards—interact when measured simultaneously on one shuffle. Their equality in marginal distribution makes the joint dependence a motivated question rather than an arbitrary statistic. The proof gives a complete finite-size sign matrix, an exact even/odd rank dichotomy with a parity-alternating null contrast, and a boundary-dominated positive aggregate covariance despite negative interior entries. The rank dichotomy is not determined by either marginal law and exposes a structural constraint on linear prediction from fixed-point events.

## Scope and residual risks

The result is limited to uniform permutations, exact plus-one successions, and second-order dependence. Uncorrelated contrasts are not asserted to be independent. The historical priority risk noted above requires independent literature verification before a formal novelty claim beyond the inspected evidence.

Self-review: passed. Independent audit: not yet performed.
