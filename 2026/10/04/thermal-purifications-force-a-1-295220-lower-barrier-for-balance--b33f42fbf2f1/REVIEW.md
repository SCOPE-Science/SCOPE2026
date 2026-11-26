# Independent mathematical audit

## correctness

PASS

For each finite L the purified beam-splitter output gives a symmetric photon-count pair (k,l), with weight p_(k+l)^(L) binom(k+l,k) 2^(−k−l) when k+l≤L. The pure-state Schmidt identity replaces log ω_RB acting on the purification by log ω_E. The relative entropy is zero, and the variance is the expected square of log s_k^(L)−log s_l^(L). Binomial thinning gives limiting marginals (1−r)r^j with r=q/(2−q). Fatou applies to the nonnegative finite-state summands extended by zero; also s_j^(L)≥(1−q)(q/2)^j for j≤L and p_m^(L)≤q^m, so a geometrically summable quadratic bound in m proves actual convergence. The conditional variance of k−l given m=k+l is m, hence the limit is q/(1−q) (log r)^2. Reparametrizing by x=−log r gives 2x²/(exp(x)−1), tending to zero at both ends with derivative sign that of (2−x)exp(x)−2. The latter rises on (0,1) and falls after 1, giving the unique maximizing root in (1,2). Tensor-product variance adds, and support is at most nL. My separate Decimal computation (/workspace/independent_checks.py, thermal) gave C*=1.29522047578382971929… and V_20=1.29522047574529945072…. No optimizing infinite-support state is needed as a witness and no global optimality is proved.

## originality

PASS

The searched alternatives distinguish a Gaussian conditional variance from a thermal marginal entropy variance. Wilde's balanced-loss lemma supplies the starting identity and upper bound, not the optimized finite-support lower obstruction. The indexed exact hit is this same finding, not independent coverage.

## value

PASS

The coefficient concerns an explicitly identified open sharpening of a uniform fluctuation estimate. The finite-support witness shows that one cannot take the coefficient arbitrarily small, or replace the linear mode dependence by a uniform sublinear estimate. Optimizing this natural thermal family gives a quantitative obstruction without assuming a dimension-dependent continuity bound or claiming the optimal universal constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
