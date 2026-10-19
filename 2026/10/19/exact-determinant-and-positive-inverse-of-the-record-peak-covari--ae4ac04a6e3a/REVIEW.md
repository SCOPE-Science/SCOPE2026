# Scientific review: record–peak cross-covariance

## Correctness — PASS

The conditional peak probabilities are computed in all five relative-position cases by independence, the record maximum distribution, and a one-dimensional beta integral. Substitution yields the exact matrix. The explicit lower–upper bidiagonal product matches every entry, establishes its positive determinant at every integer size, and gives strictly positive inverse entries by triangular inversion. The included `verify.py` supplies 1,167 exact-rational checks including finite exhaustive permutation enumeration; it is corroboration rather than an infinite proof.

## Originality — PASS, with a stated historical risk

The inspected primary material on records (Gnedin, arXiv:math/0611538), permutation peak sets (Kasraoui, arXiv:1210.5869), peak-algebra methods (Diaconis–Fulman–Holmes, arXiv:1107.2961), and a later joint generating function for aggregate peak and record counts (Ji, arXiv:2310.01053) concerns marginal families, peak-set enumeration, or joint **totals** and does not give the position-indexed cross-covariance matrix, its determinant, or the positive inverse. Published comparisons involving inversion indicators or fixed-point/descent pairs use different observables. The distinguishing content is the combined exact kernel, factorization, and inverse positivity, not the classical one-point probabilities. A general pre-existing record–peak generating function might still imply the theorem without explicitly stating it; comprehensive independent historical priority validation is absent.

## Mathematical value — PASS

The exact cross-covariance of two common local/global permutation observables is a natural joint-dependence problem. The all-size full-rank result shows that no nonzero linear combination of interior record indicators is orthogonal to all interior peaks, and the stronger entrywise positive inverse yields a nontrivial structural property not derivable from the marginal distributions alone. The complete characterization and factorization are meaningful beyond a single small numerical invariant.

## Scope of review

The result is for iid continuous observations and finite \(n\ge3\); its inverse is not a Gaussian precision matrix. The finite script does not establish an arbitrary-size identity on its own. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
