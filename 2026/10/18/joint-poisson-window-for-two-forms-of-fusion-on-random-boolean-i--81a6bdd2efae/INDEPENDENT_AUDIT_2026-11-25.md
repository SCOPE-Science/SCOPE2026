# Independent mathematical audit

## correctness

PASS

There are 3^k ordered joins and (3^k−1)/2 distinct unordered joins, because the only swap-fixed pair is (X,X). Write r(u)=2^{|u|}, d(u)=r(u)−1_{u=X}; the first two sums of r are 3^k and 5^k. Indicators involving disjoint bits are independent, and different indicators sharing one bit have covariance p^3(1−p). The ordered distinct overlap counts are 2Σ r(r−1) for mixed and Σ d(d−1) for self, and the cross count is Σ dr; these give the three stated second-moment coefficients. This handles k=0, where only the mixed Bernoulli(p²) indicator remains, and p=0,1. For an additional small check, at k=1 the conditional mixed count for a-patterns 00, 10, 01, 11 is respectively 0, b_X, b_∅+b_X, b_∅+2b_X; the self count is one only for 11. At p=1/2 this gives the two means 3/4,1/4, variances 13/16,3/16 and covariance 3/16. For the joint approximation distinct neighboring witnesses share exactly one bit. The squared-degree sum of the pooled bit graph is at most 5·5^k, so b1≤5·5^k p^4, b2≤5·5^k p^3 and b3=0 by joint independence outside the neighborhood. AGG Theorem 2 explicitly allows partition aggregation; the two Poisson sums are independent. Its variation norm is twice the sup-event distance, so the stated astronomical-scale bound 20·5^k(p³+p⁴) is conservative: even 10·5^k(p³+p⁴) follows with this normalization. Substituting p=t3^{−k/2} yields the stated exponentials and the adjustment for the self mean. The self truth event differs by at most p due to the lone diagonal; applying positivity to the limiting vector gives independent truth limits. Markov handles the sparse regime, and the dense relative variances vanish by the two bounds (3^kp²)^{−1} and (5/9)^k/p. All witnesses of x lie below x, where the same independent law holds. The original finite checker was read, not executed; the approximation and threshold follow from the proof rather than its bounded tests.

## originality

PASS

This is a specific joint induced-edge and cross-edge calculation on the Boolean disjointness graph, equivalently the Boolean-join fusion problem. The distinct support is the exact covariance and related second moments coupled with the two-intensity Poisson limit despite a common vertex sample. Neither fusion semantics nor the general Chen–Stein bound is new, and no exact finite joint distribution is claimed.

## value

PASS

The natural comparison is between reusing a truth set and drawing a second independent one in the same binary connective. The result distinguishes their threshold intensities, resolves what common randomness contributes at finite k, and gives a quantitative proof that it does not survive as dependence in the critical limit. The moment and error formulas are useful as a benchmark for alternative sampling models, without asserting persistence, independence at finite k, or simultaneous truth at all worlds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
