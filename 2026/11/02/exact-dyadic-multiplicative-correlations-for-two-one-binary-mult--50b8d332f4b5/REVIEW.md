# Review of exact dyadic multiplicative correlations

## Correctness
PASS. The binary multiplication carry recurrence and signed transitions are explicitly defined. The exact vector identity between rows at positions \(0,1,2,k+1,k+2\) is proved by cancellation. Multiplying it by arbitrary later powers produces a universal recurrence, while directly evaluated initial rows give the generating function. Tests independently enumerate direct sums for \(2\le k\le9\) and \(0\le r\le13\), and test the row identity and recurrence for the same parameters. No finite-to-infinite inference is made.

## Originality
PASS within checked sources. Related marginal rarefied sums in Shallit (arXiv:2302.09436) and Morgenbesser–Shallit–Stoll (arXiv:1009.5357), and the shift correlations in Baake–Coons (arXiv:2209.07102), do not state or algebraically imply this family-level formula from their inspected theorems. Winterhof (arXiv:2305.11486) surveys a distinct fixed-shift correlation framework. Existing result for multiplier three covers only \(k=1\); the present claim is explicitly \(k\ge2\). Standard transfer-matrix construction is not claimed as new. Residual risk: a general previously known mixed-dilation theorem not found in the searched corpus could subsume the formula.

## Mathematical value
PASS. Mixed digit parity under multiplication is a natural arithmetic correlation not fixed by either marginal, especially the first exactly nonzero length. A uniform closed generating function simultaneously determines infinitely many multipliers, arbitrarily high dyadic levels and a nontrivial cancellation threshold; it is more substantial than a fixed-parameter calculation.

## Scope and residual limitations
The theorem does not cover arbitrary odd multipliers or nondyadic endpoints; the automaton proof does not assert new machinery. Source comparisons are not exhaustive. No independent mathematical audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
