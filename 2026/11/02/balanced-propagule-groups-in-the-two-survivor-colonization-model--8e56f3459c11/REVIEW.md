# Independent mathematical audit

## correctness

PASS

By linearity of expectation the objective is additive in the site sizes. The binomial marginal is j p^2(1-p)^(j-1) for j>=1, strictly positive; merging a singleton into another group helps. For fixed pair sum s, the first exchange from t=0 hurts, and every later exchange has the sign of Q_s(t)-(1-p) where Q_s(t)=(t/u)^(1/(u-t)) and u=s-t-1>t. Strict increase of Q_s follows because log Q_s is -artanh(h/c)/h with c=(s-1)/2 and h=c-t, and artanh(z)/z is strictly increasing on (0,1) (e.g. its positive power series). With a strictly negative first difference and at most one intervening zero between decreases and increases, every interior pair is strictly dominated by at least one endpoint, even when the two endpoints tie. A globally optimal allocation cannot contain a pair differing by two or more, since a merge is admissible; this does not assert balance is optimal at each externally fixed k. Checking all allowed k proves the exact formula and the classification of ties. For N=6 an independent count of survivor patterns expands the adjacent score differences as p^2(p^2-3p+3)(5p^2-9p+3) and p^2(3-4p). The first factor changing sign does so only at p_0 in (0,3/4); the adjacent signs then suffice for all three ranges and the two ties. N<6 cannot support three groups of at least two. The incidental 'exponential family' description should mean exponential in order sqrt(N), not in N; the exact finite reduction is unaffected.

## originality

PASS

The supported distinction is the strict all-maximizers theorem for the indivisible Bernoulli two-success expected-count problem, with its first three-way budget example. Continuous equal-positive-support results and other stochastic founding objectives are genuine analogues, but do not provide this discrete strict pair lemma or its consequence for all integer optima. No absolute priority is asserted.

## value

PASS

This is a sharp structural reduction of a nonconcave integer allocation, not a table of optima for one probability. Strict domination excludes every unbalanced optimal partition for all probabilities in the open interval and reduces the search to at most floor(N/2) candidates. The N=6 example is a minimal boundary illustrating two distinct changes in the active-group count. Its value is as a stylized probability and optimization result, not a real release prescription.

The dated certificate retains the supplied scientific assessment, sources and limitations.
