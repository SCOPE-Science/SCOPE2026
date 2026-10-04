# Review

## Correctness

PASS. The random first key has a uniform rank, so conditioning on its rank gives two independent random BST subproblems and the exact conditional mean in (1). The harmonic first-difference formula proves that this conditional mean increases strictly with distance of the first pivot from the median and therefore with squared root imbalance.

The mixed covariance is evaluated from explicit finite sums; all harmonic terms cancel to the displayed cubic polynomial. The imbalance variance follows from exact uniform power sums. The path-length variance and its asymptotic coefficient agree with the classical full-text derivation in the primary literature. Exhaustive permutation replay through order nine independently reproduces the finite formulas.

## Originality

PASS, with a concrete textbook-corollary risk. Prodinger's full paper was inspected across all nine pages. It develops the same path-length statistic and gives its exact expectation and variance, but does not retain root split size as a joint statistic.

Drmota--Hwang's full public text was inspected in its random-BST definition and its BST covariance section. It gives sophisticated correlation formulas among profile level sizes and relates profile limits to total path length, but no root-imbalance statistic or first-split/path-length covariance was found.

Targeted searches for root imbalance, root split, first-pivot rank, exact covariance, the cubic constant, and the regression slope did not locate the statement. Because the underlying root recurrence is standard, an equivalent calculation could still appear as an exercise or unindexed remark; that risk is stated rather than hidden.

## Value

PASS. The first split is the most local structural choice in a random BST or Quicksort execution, whereas total path length is a global recursive cost. The exact nonzero correlation limit shows that one local split retains a macroscopic amount of information about the final cost.

The result is more than a sign check: it gives strict monotone regression, an exact cubic covariance, an exact least-squares coefficient, and an asymptotic explained-variance fraction of about \(0.33048\). This quantifies, in a simple closed form, how much of total Quicksort variability is already visible from the first pivot.

Same-model review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK permutations_checked=409112 covariance_checks=8 conditional_mean_checks=44 monotone_regression_checks=8 marginal_moment_checks=16 imbalance_moment_checks=16 slope_checks=7 harmonic_reduction_checks=796 asymptotic_checks=7`.
