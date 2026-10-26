# Self-review

## Correctness — PASS
For algebraically closed characteristic \(p>0\), \(n\ge d\ge4\), the proof explicitly translates the derivative ideal into all complementary \(k\)-subset quadratics, rules out three values using a monic quadratic identity, rules out two nonsingleton blocks by a nonzero second finite difference, and solves both exceptional-coordinate equations. In every characteristic, the two conditions for an unconstrained exceptional coordinate are equivalent to \(Q>2\). The remaining diagonal condition is \(p\mid\binom{k}{2}\). The conclusion concerns reduced support only. The exact finite-field `VERIFY.py` checks the set formula in 24 parameter cases, but is not used to infer an infinite statement.

## Originality — PASS, with risks
Xie arXiv:2610.00259v1, Theorems 1.1 and 1.3, give dimensions and the already-known \(Q>2\) planes; Theorem 1.4 gives local coordinate multiplicities, and Section 7 expressly leaves smaller-dimensional components unclassified. The new scope is complete lower-dimensional reduced support, especially the conditional diagonal component, not a replacement for those published results. Orzel arXiv:2509.05009v3 concerns the different order-two zero locus. Targeted semantic searches of published mathematical records and title/parameter web searches found no exact coverage; an unindexed earlier elementary calculation remains possible. The finding is not independently audited.

## Value — PASS
This completes the smallest nontrivial higher-derivative component problem for all \(n\ge d\ge4\) and prime characteristics, including a sharp arithmetic change in the count of irreducible components that a dimension calculation cannot see. It identifies a natural projective configuration of \(n\) or \(n+1\) points, or \(n\) concurrent lines, and isolates exactly the newly arising diagonal component.

## Scope and outstanding risks
No claim about embedded components, global reducedness or higher-order derivative loci. General results on symmetric hypersurfaces and possible unindexed equivalent arguments remain originality risks.

Self-review: passed. Independent audit: not yet performed.
