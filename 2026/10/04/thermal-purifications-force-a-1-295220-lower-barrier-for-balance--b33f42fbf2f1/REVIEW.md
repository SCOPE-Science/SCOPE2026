# Review

## Correctness
PASS. Wilde's source states the exact finite-support domain, the balanced-output equality, and the variance identity used here. For the truncated geometric purification, the receiver marginal is diagonal with the displayed binomial thinning formula, so the finite-cutoff variance reduces to an explicit nonnegative double sum. The geometric limit is evaluated exactly, and Fatou's lemma gives the required lower bound without assuming continuity of the infinite-dimensional logarithmic moment. The optimization is one-dimensional and has a unique interior maximizer. Tensor powers preserve finite total-photon support and make the variance additive because each factor has zero relative entropy. The packaged checker reproduces the scalar constant and finite-cutoff sums.

Risk: the argument proves a lower barrier, not equality with the globally best coefficient. The claim and proof maintain that distinction.

## Originality
PASS. The closest primary source, Wilde's 2026 paper, proves only the upper coefficient \(4\) and explicitly leaves improvement of that constant open. Claim-specific searches for thermal purifications, balanced beam splitters, relative-entropy variance, truncated geometric inputs, and the best universal coefficient found no published statement of the \(1.295220475783829\ldots\) barrier. The 2014 pure-loss second-order paper computes a thermal entropy variance for classical communication, a different object and implication. The cumulative prior finding ledger contains no balanced pure-loss thermal variance barrier.

Residual risk: an older Gaussian-state calculation under different terminology may contain an algebraically equivalent special-case variance formula. Even if so, the inspected sources and searches did not identify the optimized finite-support universal-constant obstruction proved here. This residual terminology risk is recorded rather than treated as proof of uniqueness.

## Value
PASS. The 2026 source itself identifies improvement of the uniform variance constant as a concrete finite-blocklength research question. The result supplies a natural, exact and extensive obstruction: any future universal improvement from \(4\) must stop above an explicit coefficient \(1.295220475783829\ldots\). The witnesses are physically standard geometric photon-number purifications, and the truncation argument keeps them inside the theorem's exact finite-support domain. This is a structural constraint on the sharp constant, not a recomputation of a known table or an arbitrary numerical slice.

## Closest literature and limitations
The closest literature is Wilde's 2026 balanced-loss variance lemma and its stated open question about the coefficient, together with the 2014 pure-loss second-order analysis of thermal entropy variance. The present result does not determine the global sharp coefficient, does not improve the upper bound, and does not establish a coding dispersion theorem.

Same-model review: passed. Independent audit: not yet performed.
