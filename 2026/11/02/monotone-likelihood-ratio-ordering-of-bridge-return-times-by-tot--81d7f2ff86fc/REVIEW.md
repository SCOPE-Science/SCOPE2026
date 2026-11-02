# Scientific review: conditional return-time ordering

## Correctness — PASS
First-return excursion counts are \(2C_{j-1}\), and Lagrange inversion applied to \(F=z+F^2\) yields the exact forest/bridge count \(a_{n,k}\). Cutting at a marked return gives the conditional mass function. A direct factorial cancellation produces an adjacent conditional likelihood ratio monotone in the return time; its derivative has the stated sign, with the excluded last point ensuring strict stochastic order. The last-return truncation probability follows from the same coefficient ratio. Integer-arithmetic enumeration and a separate coefficient-check program verify small cases. The all-size conclusion follows from algebra, not finite tests.

## Originality — PASS, qualified
A full-text inspection of Lindell and Holst (2007), including the finite-walk excursion generating functions, ranked-length distributions and appendix, found no comparison of the chronological \(r\)-th return time under adjacent exact return counts. Voss's October 17, 2007 marginal-return-count derivation likewise does not give the conditional rank-resolved likelihood-ratio hierarchy. Related records concerning return-count/peak regressions or return-count/height-energy covariances do not imply this statement. Search comparisons for local time, first passage, bridge excursions, stochastic ordering and monotone likelihood ratios found no directly covering result. The classical coefficient formula makes a latent equivalent in older literature possible; searches do not establish priority uniquely.

## Value — PASS
Return-time conditioning is natural in renewal/excursion decompositions of tied-down random walks. The theorem settles *all* return ranks, bridge lengths and conditioning levels in the stronger likelihood-ratio order, giving valid comparisons for every increasing timing loss, rather than isolated moments. The exceptional last-return identity exactly quantifies how conditioning by one more excursion changes the distribution and provides a nontrivial sharp total-variation value. This is a structural finite-sample dependence theorem, not an arbitrary numerical slice.

## Limitations and closest literature
The result applies only to the discrete nearest-neighbor bridge. Lindell–Holst covers ranked excursion sizes and their continuum limits, not this chronological order. Voss covers the count of returns but not rank-resolved timing. Classical coefficient identities are prior inputs and are not claimed as novel. Unlocated older equivalences remain possible. No general statement is made for walks with non-nearest-neighbor increments or for the Brownian bridge.

Self-review: passed. Independent audit: not yet performed.
