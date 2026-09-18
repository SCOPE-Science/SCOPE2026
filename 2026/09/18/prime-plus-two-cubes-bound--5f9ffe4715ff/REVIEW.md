# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

PASS.

The finite search is exhaustive after the identity
\[
12(b^3-a^3)-3=(6t-3)^2
\]
and the explicit global bounds \(a\le6933\), \(b\le8735\). The verifier uses exact integer square and cube tests, reports 579 floor-admissible first-pair solutions and zero triple-cube obstructions, and independently cross-checks the pair reduction against a direct \((t,a)\) enumeration through \(t=10000\).

The deduction of the final bound was checked separately. For \(n<333334^3\), Applegate--Pratt Theorem 3.2 with \(N_3=10^{12}\) applies. In its only unresolved branch the first two residuals are cubes. For \(10^{16}\le n<333334^3\), the third residual lies strictly between the largest element of \(\mathcal E_3\) and \(10^{12}\); the new finite exclusion makes it a noncube, so their Theorem 3.1 supplies the required odd-prime-plus-cube representation. Their Corollary 3.5 supplies the interval below \(10^{16}\).

The local divisibility statement \(27\mid n\) was checked both directly from cube residues and by exact residue enumeration.

## Originality

PASS, to the best of our knowledge.

The motivating paper explicitly states Conjecture 5.1 as open and reports a simple brute-force search related to the stronger Conjecture 5.2 only through \(t<10^4\). Its published prime-plus-two-positive-cubes range ends at \(10^{16}\). Searches for the three-consecutive-cube equations, the exact new endpoint \(333334^3\), the decimal endpoint 37037259259703704, and equivalent prime-plus-two-cubes formulations did not locate a stronger published bound or this finite reduction. The accompanying source repository was also checked; its most recent visible commits precede the arXiv submission and no matching endpoint or computation was found.

The source preprint is extremely recent, so unindexed simultaneous work remains the main originality risk. No inaccessible paper was identified whose metadata specifically indicates the same improved bound or the same triple-cube computation.

## Value

PASS.

The result improves a concrete verified boundary from \(10^{16}\) to \(3.7037259259703704\times10^{16}\), while also replacing a direct search in \((t,a)\) by an exact discriminant-based finite reduction. The same computation verifies the specific triple-cube obstruction relevant to the paper's bootstrapping argument through \(t=333333\), versus the source paper's reported search scale \(t<10^4\). The method is compact, reproducible, and directly reusable if the one-prime-plus-one-cube base range is extended.

## Scientific limitations

The large computations underlying the cited paper's Theorem 3.1 and Corollary 3.5 are accepted as literature inputs rather than independently reproduced. The present result is a finite verification, not a proof of Applegate--Pratt Conjecture 5.1 for all integers.
