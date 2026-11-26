# Independent mathematical audit

## correctness

PASS

Fixing the label set of descendants of vertex 2 restricts individual uniform parent choices independently to the corresponding earlier labels, giving two independent recursive trees. There are (s−1)!(n−s−1)! choices for every such set, and binomial(n−2,s−1) possible sets, yielding (n−2)! parent arrays for each s and proving uniformity. The only edge joining components is 1 to 2, which subtracts one leaf precisely for a singleton complement. The leaf process at size d has the Eulerian recursion because choosing a leaf leaves the total unchanged and choosing any nonleaf adds one; hence L_d=1+D_(d−1) in distribution for d≥2. With t=−u, its moment generating function is (1−exp(−u))^d/(d−1)! times the (d−1)st signed derivative of 1/(exp(u)−1). The leading Laurent pole gives ((exp(t)−1)/t)^d, and the first regular term contributes −β_d t^d/d! relative to that factor. This verifies the mean and cumulants of orders below d and zero order-d cumulant for even d. Additivity for the two independent sizes gives the interior identities and at s=2h gives the nonzero −β_(2h) defect with all lower moments matching, likewise at the mirrored boundary. Only the two singleton ends shift the mean, by +1/2 and −1/2 respectively for n≥3, giving the stated covariance; n=2 is deterministic. A separately written direct joint parent-transition recursion confirmed complete conditional laws, covariance, interior matching and even boundary defects 2, 4, 6 and 8 for tested sizes through 17.

## originality

PASS

The supported distinct contribution is the sharp conditional boundary at every even order, including the explicit nonzero Bernoulli defect for the whole tree. Uniform subtree size and individual Eulerian cumulants are not new, and a later indexed finding covers the split, interior hierarchy and covariance. That mathematical overlap is credited independently of priority; the rounded-sum cumulant formula provides strong methodological coverage but does not state the recursive-tree detection boundary.

## value

PASS

The size of a designated root branch and the total leaf count are natural global tree statistics. An exact all-even-order transition telling when one specific cumulant first becomes sensitive, with a sign and magnitude that can be used without recovering the whole distribution, is useful beyond a covariance or unquantified lower-order matching. The exact cutoff and coefficient are not a numerical example or an arbitrary choice of size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
