# Scientific review

## Correctness (C): PASS
The one-round kernel follows from the exact block enumeration of the cited 2023 full text. Conditioning produces the rational generating-function recurrence. For two and three cards, direct substitution gives respectively a simple and a double pole at the common location \(z=2\). The difference of the published block generating polynomials proves that every higher holding probability is strictly smaller than \(1/2\). A nonzero transition from every higher state to state three makes the recursively propagated double-pole coefficients strictly positive. Rational-function partial fractions convert the pole order to the survival asymptotic. The independent standard-library checker exhausts short permutations and verifies 221 rational assertions. The result is for fixed finite initial state, not uniform initial size.

## Originality (O): PASS under accessible evidence; priority risk remains
The 2023 arXiv preprint was read at its introduction, block enumeration, main theorems, and cited source relationship. Its theorems concern \(n\to\infty\) moments and a Gaussian limit, not a fixed-\(n\) far tail. The 2016 paper's accessible abstract mentions a distributional recurrence; that recurrence does imply our result after nontrivial singularity analysis, but neither the 2023 discussion nor the earlier abstract states the repeated leading pole and its resulting coefficient recursion. The 2016 primary full text could not be read; consequently any equivalent prior analysis in it remains a specific priority risk. Related database searches found no equivalent fixed-\(n\) asymptotic claim. A known exact distribution is not falsely presented as newly invented.

## Value (V): PASS
The derived law identifies the decay rate **and** the otherwise unexpected polynomial multiplier across every fixed initial number of cards. It explains why an elementary-looking absorbing finite chain is not asymptotically a single geometric waiting time and pinpoints the obstruction to an ordinary one-pole tail. This provides the long-duration counterpart to the established large-initial-size central limit theorem.

Self-review: passed. Independent audit: not yet performed.
