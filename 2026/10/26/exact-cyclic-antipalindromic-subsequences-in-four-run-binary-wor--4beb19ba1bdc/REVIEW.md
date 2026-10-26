# Review of the four-run circular antipalindrome result

## Correctness
The classification proof reduces all antipalindromic subsequences in a rotation of a four-run circle to exactly two- or four-run forms. Each case is bounded by a finite minimum of run lengths, with an explicit boundary cut attaining the bound. In balanced words, the two expressions reduce to \(s/2+U\) and \(s-U+V\); their average proves the sharp ceiling bound. Parametric witnesses exist for every \(s\ge2\). When \(4\mid s\), matching the lower bound forces \(U=s/4,V=0\), proving the equality classification. The standalone verification reproduces all the stated finite tests without relying on the formula in its interval DP or mask enumeration. No finite test replaces the infinite argument.

## Originality
The closest inspected primary source is Kynčl, Pach and Tóth's four-run geometric sharp example and more general separated-matching conjecture. The example is prior art and is explicitly credited; the original paper did not prove the universal bound for its two-runs-per-color restriction or derive the complete four-parameter formula. Müllner and Ryzhikov's 2019 antipalindromic subsequence study gives the primary middle-period motivation. Csóka and collaborators' 2020 counterexamples invalidate extrapolation to all run counts, not this particular four-run theorem. Meaning-based published-record searches for six aliases did not identify an implication covering the claim; equivalent unindexed work remains possible.

## Value
This gives a sharp exact answer to the natural first nontrivial fixed-run problem at the boundary of a broader false conjectural hierarchy. It supplies a complete formula in nonbalanced parameters, a finite-size optimum for every balanced size, and a rigidity characterization. These are structural results rather than routine computational increments.

## Limits and status
The result is not claimed for circles with more than four runs, the extremal example was known, and mathematical priority beyond inspected sources is not independently guaranteed. The finite checks are reproducibility tests, not exhaustive proofs of infinite statements.

Self-review: passed. Independent audit: not yet performed.
