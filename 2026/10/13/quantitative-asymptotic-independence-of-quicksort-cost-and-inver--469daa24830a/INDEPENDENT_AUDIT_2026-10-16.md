# Independent mathematical audit

## correctness

PASS

Centered C_n/(n+1) is an L²-bounded martingale: external gap depth identity sum=C_n+2n gives its exact conditional mean; insertion depth is dominated in second moment by lower record maxima and upper record minima, giving L² tail E|M_n-M_k|=O((1+log k)/sqrt(k)). Inversions on the last n-k inputs are independent of M_k; omitted centered inversion pairs are bounded by kn, hence O(k/sqrt(n)) after n^(3/2) normalization. Lipschitz covariance substitutions yield inequality (1), optimizing k yields n^(-1/6)(log n)^(2/3), and CLT follows from independent insertion-rank inversion decomposition with variance asymptotic 1/36. Reflection of every key leaves Quicksort cost unchanged but complements inversion count, yielding exact conditional symmetry/covariance 0. Independent enumeration 5,913 permutations n<=7 validates conditional reflection and covariance; independence in the limit rests on analytic martingale+tightness proof.

## originality

PASS

Classical Quicksort comparison limit and marginal inversion CLT are background. Neininger 2001 joint analysis compares comparisons to key-exchanges, not input inversion count. Baxter-Zeilberger inversion+major-index limit is different. No checked source established quantitative bounded-Lipschitz independence of the specific pair. Potential implicit generic recursive-statistics theorem remains a residual risk.

## value

PASS

Distinguishes exact finite zero covariance from true nonlinear asymptotic independence of a non-Gaussian Quicksort cost and Gaussian inversion noise. Explicit rate provides useful quantitative decoupling for two natural fundamental permutation statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
