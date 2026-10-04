# Review

## Correctness

PASS. The cut-bit representation is exact. Conditional on a fixed number of cuts, adding one uniformly chosen missing cut maps the uniform slice of \(s\)-subsets exactly to the uniform slice of \((s+1)\)-subsets, and a new cut cannot enlarge the longest zero run. This proves the stochastic regression without numerical inference.

The coordinate covariance identity follows from the two conditional values of one fair Bernoulli coordinate. For a unique longest run, the total decrement caused by flipping its zeros is bounded by the triangular profile \(\min(j,\ell-j+1)\); multiple longest runs contribute zero. The longest-run union bound then gives the stated explicit covariance estimate. Classical longest-run variance asymptotics supply the positive denominator needed for the correlation rate.

## Originality

PASS, with the exact conditional distribution treated as substantial prior art. Philippou--Makri already give \(\Pr(L_n\le k\mid S_n=r)\), so no novelty is claimed for having a joint or conditional law.

The accepted advance is the simple monotone coupling across fixed-weight slices, the exact coordinate-influence representation of the covariance, and the resulting \(O((\log N)^2/\sqrt N)\) correlation bound. Finch's full public paper studies the identical uniform-composition pair, gives recursive mixed-moment computations, reports negative numerical correlations, and explicitly says a rigorous proof of convergence to zero would be desirable. The present theorem supplies that missing qualitative proof with an explicit quantitative rate.

Schilling's full paper supplies the marginal longest-run variance asymptotics but not a mixed covariance with the number of successes.

## Value

PASS. Number of parts and maximum part are the two most immediate global summaries of a random composition. A rigorous dependence statement for them was explicitly left open in later numerical work.

The result is structurally stronger than a sign computation: every increasing transform of part count is negatively correlated with every increasing transform of the maximum, and the influence identity isolates exactly which cuts create the dependence. The explicit rate proves asymptotic decorrelation without requiring delicate bivariate generating-function asymptotics.

Same-model review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK bitstrings_checked=131070 covariance_checks=16 influence_checks=16 stochastic_order_checks=136 bound_checks=16`.
