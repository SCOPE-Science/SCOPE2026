# Review
## Correctness
PASS. Conditioning on a specified cell with occupancy \(r\) leaves a uniform occupancy problem on the remaining \(m-1\) cells, so the conditional collision expectation is exact. Pearson's statistic is affine in total pair collisions, yielding the covariance formula directly. The exact Pearson variance follows from pairwise independence of distinct pair-collision indicators, and the \(K_r\) variance follows from one-cell and two-cell multinomial probabilities. The fixed-load limit is obtained by fixed-\(r\) factorial expansions.

Exact enumeration independently reproduces the finite covariance formulas on a grid of small allocation problems and checks the conservation identities forced by total cell count and total sample size.

## Originality
PASS, with a classical-occupancy residual risk. The closest complete source develops the same \(r\)-count coordinates and their covariance structure, but does not introduce Pearson chi-square or the mixed covariance profile. A complete collision source develops exact occupancy-collision theory but studies a different collision object. Targeted exact and alias searches did not locate the covariance polynomial, the singleton \(n=2m\) orthogonality, or the fixed-load sign law.

The main residual risk is an equivalent expression in older finite-urn or goodness-of-fit literature under alternate notation.

## Value
PASS. Occupancy frequency counts describe which cells are rare or common, while Pearson chi-square is the standard quadratic departure statistic for equal cell probabilities. The result gives a complete coordinate-wise explanation of which occupancy levels push Pearson fluctuation in the same or opposite direction. The singleton threshold and the limiting polynomial sign profile are structural features not visible from aggregate richness alone.

## Closest literature and limitations
The closest literature studies frequency-count covariance structures and collision laws separately. The theorem is restricted to equal cell probabilities, and the fixed-load limit keeps \(r\) fixed.

Self-review: passed. Independent audit: not yet performed.
