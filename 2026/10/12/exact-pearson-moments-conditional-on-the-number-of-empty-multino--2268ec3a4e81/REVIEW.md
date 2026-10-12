# Review
## Correctness
PASS. Conditioning on \(K=k\) occupied cells gives a uniform surjection. Pearson's statistic is affine in the number of colliding observation pairs. One collision constraint reduces the number of free labeled units by one and two distinct collision constraints reduce it by two, yielding the Stirling ratios used in the first two moments. Exact rational enumeration independently reproduces every conditional mean and variance in the stated finite verification range.

## Originality
PASS. Finkler's complete sparse-table preprint explicitly relates the number of zero cells to corrections of Pearson's statistic but does not give \(\mathbb E[X^2\mid K]\) or \(\operatorname{Var}(X^2\mid K)\). Filina and Zubkov's complete exact-distribution article is unconditional. A prior occupancy-covariance identity is also unconditional and does not determine these conditional moments. The 1970 Good-Gover-Mitchell article remains an explicit residual risk because its full text could not be inspected.

## Value
PASS. Empty-cell count is a classical measure of table sparsity and a direct input to prior Pearson corrections. Exact conditional mean and variance formulas give a finite-sample calibration of Pearson's statistic at each observed sparsity level and isolate the mechanism through pair collisions.

## Closest literature and limitations
The closest fully inspected source is Finkler's sparse-table work, which introduces the zero-cell count and adjusts Pearson's statistic according to it. The result here is limited to the equiprobable multinomial null with sampling zeros. Unequal probabilities and structural zeros are outside scope.

Self-review: passed. Independent audit: not yet performed.
