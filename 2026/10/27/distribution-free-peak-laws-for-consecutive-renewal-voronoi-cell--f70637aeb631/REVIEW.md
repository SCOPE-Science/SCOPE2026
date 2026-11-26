# Independent mathematical audit

## correctness

PASS

Canceling the shared gap in each neighbor comparison gives M_i=1{G_i>G_(i−2)}1{G_(i−1)>G_(i+1)}. The factors concern disjoint gap pairs, giving mean 1/4. Adjacent peaks are impossible, lag two requires independent three-rank chains with probabilities 1/6 each, and lag three requires the single shared gap to rank first from the bottom in a triple independently of two comparisons, giving 1/12. For lag at least four the relevant gap sets are disjoint; in fact whole separated index families are independent. Subtracting (1/4)^2 and substituting in the stationary variance sum gives the stated exact windows and positive long-run variance 5/144. Blocks of length floor(n^(1/3)) separated by three discarded indices are independent. By boundedness and 3-dependence the discarded terms (including a final partial block) have variance O(n^(2/3)+n^(1/3)); the centered block third moments sum to at most the block length times the total block variance, o(n^(3/2)). This verifies the CLT. An independent exact rank replay matched all four joint moments and the first six window variances, 3/16, 1/4, 35/144, 5/18, 5/16, and 25/72: enumerate all permutations of the h+4 gaps at lag h or n+3 gaps in an n-peak window, apply the two comparisons per indicator, and divide first and second moment sums by the factorial. This is corroboration, not the proof of the general n result.

## originality

PASS

The distinct supported finding is the distribution-free indexed renewal peak law with its exact lag and finite-window constants. The Gaussian MA(1) process with coefficient +1 is exactly equivalent at the peak-indicator level; positivity of renewal gaps does not distinguish these peak laws. The accessible earlier study addresses Gaussian MA(1) peak variances and CLTs, but does not specify in the inspected text the coefficient range or whether its formulas give the stated endpoint moments. No inspected theorem establishes the exact profile or supplies a verified stronger implication. The blocking CLT itself is standard once the profile and dependence range are known.

## value

PASS

Local longest cells are a natural rank summary in one-dimensional renewal geometry. The exact lag profile identifies positive dependence at distance three despite negative shorter lags. The resulting variance is only 5/27 of the independent-indicator approximation per indexed cell, a substantive quantitative difference for peak-count inference. This value is in the exact evaluated constants and their distribution-free scope, not in invoking a standard finite-dependence CLT.

The dated certificate retains the supplied scientific assessment, sources and limitations.
