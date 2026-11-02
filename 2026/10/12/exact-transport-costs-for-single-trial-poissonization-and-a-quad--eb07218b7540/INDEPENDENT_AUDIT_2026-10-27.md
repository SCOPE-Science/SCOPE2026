# Independent mathematical audit

## correctness

PASS

For all d≥1, the exchangeable Poisson vector admits a uniform marginal maximizer label by symmetric tie breaking. Pointwise squared cost 1+sum Y_j²−2Y_I is minimized by taking a maximum coordinate, hence W2²=2+1/d−2 E M_d. Similarly l1 cost=1+sum Y_j−2 1_{Y_I≥1}, giving 2/e because sum Y_j is Poisson(1). The tail-sum E M_d=sum_{k≥1}(1−F_{1/d}(k−1)^d) is absolutely convergent. Exact second factorial moments give excess 2 E[sum binom(Y_i,2)−(M_d−1)_+], nonnegative pointwise and strictly positive on Y_1≥3. With x=1/d, P(M≥2)=x/2−11x²/24+O(x³), P(M≥3)=x²/6+O(x³), and sum_{k≥4}P(M≥k)≤d E binom(Y_1,4)=x³/24, proving excess 7x²/12+O(x³). Independent symbolic Taylor expansions and d=1,2,3,5,10,20,50,100,400,1000 numerical tail evaluations corroborate rather than prove these universal identities. No extension to unequal weights, multi-trial multinomial, or arbitrary costs.

## originality

PASS

A fresh implication-level comparison found the same Bernoulli-vector/independent-Poisson domain in Pianoforte–Turin, but their Theorem 1.1 and Corollary 3.1 bound first-order l1 Wasserstein distance only. Deheuvels–Pfeifer (1988) give total-variation errors for multinomial Poissonization. Novak 2024 treats scalar 1-Wasserstein/other scalar probability metrics. These sources do not state or imply the exact vector squared-Euclidean optimal cost and cancellation coefficient 7/12 without the model-specific Poisson-maximum analysis. The scalar W1=2/e portion follows from standard one-dimensional Kantorovich formulas and is not treated as independently novel. Bounded Resultary, published-record and web alias searches found no independently published stronger exact statement. The originality judgment is best-of-knowledge and conditional on uninspected generic semidiscrete and Rüschendorf full texts.

## value

PASS

Independent Poissonization of a categorical trial is a natural minimal benchmark for converting exclusive occupancy into independent cell counts, explicitly treated in the Bernoulli-vector Poisson approximation literature. The exact squared l2 optimal transport cost for every d is a natural invariant of this pair of laws; the pointwise strictly positive collision discrepancy and surprising disappearance of its first-order 1/d term produce a sharp 7/(12d²) correction. A future researcher comparing stronger probability metrics or testing Poisson approximation constructions could use precisely this closed-form benchmark. The scalar W1 part is classical and the max-coordinate optimizer elementary, so the value is narrow and contingent on the exact quadratic cost/cancellation, not general methodological novelty or numerics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
