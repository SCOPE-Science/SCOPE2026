# Review

## Correctness

PASS. Conditioning on the uniformly distributed first-key rank gives two independent random binary search subtrees. Total covariance separates the recursive covariance contribution from a between-split term. The expected leaf count is constant across all interior split sizes and changes by only \(\pm1/3\) at four boundary splits, reducing the between-split covariance to one difference of consecutive expected path lengths. The resulting harmonic term cancels exactly against the harmonic part of the accumulated induction sum.

The leaf-variance recurrence uses the same four boundary deviations and independently yields \(2(n+1)/45\) for \(n\ge4\). Exhaustive permutation enumeration and a separate exact recurrence replay reproduce every displayed finite identity.

## Originality

PASS, with a concrete residual risk from older analysis-of-algorithms literature. Flajolet--Gourdon--Martínez give detailed fringe-pattern theory and explicitly place leaves and path length among standard random-BST parameters, but the inspected paper does not state their mixed covariance. Kapur gives a broad additive-functional framework and treats internal path length, but the inspected dissertation does not state a leaf/path mixed moment.

Drmota--Hwang develop covariance theory for level profiles and total path length in the same random-BST model. Their full paper has no leaf statistic in the inspected text, so those results do not imply the accepted formula. Published-record searches under leaf, terminal-node, search-cost, internal-path-length, covariance, and the exact rational formula found no matching statement.

## Value

PASS. Leaf abundance and total internal path length are canonical global summaries of random search-tree shape: terminal branching versus aggregate search depth. Their exact interaction is therefore naturally motivated rather than an arbitrary mixed moment.

The formula gives more than a sign. It identifies a simple all-size rational covariance and a stable regression scale: after normalizing by the exact leaf variance, the best linear search-cost slope converges to \(-5/2\). This quantifies how fringe-rich fluctuations align with shallower search trees.

Self-review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK permutations_checked=409113 mean_checks=18 covariance_checks=9 variance_checks=9 slope_checks=6 recurrence_checks=598`.
