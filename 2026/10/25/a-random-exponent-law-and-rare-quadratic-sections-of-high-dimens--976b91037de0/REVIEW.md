# Scientific review: affine regular-simplex sections

## Correctness — PASS

The object is an \(m\)-vertex regular Euclidean simplex for each integer \(m\ge3\). The probability measure is normalized translation-and-rotation invariant hyperplane measure restricted to intersecting hyperplanes, **not** uniform normal followed by uniform conditional offset. A separating hyperplane cuts precisely \(k(m-k)\) edges. In an isonormal Gaussian parametrization, the Crofton expectation is the Gaussian offset integral divided by the expected width; the Gaussian radius factors out in homogeneous functionals. This proves the exact mean \(\binom m2/(\sqrt\pi\,\mathbb E\max_i Z_i)\). Gaussian endpoint limits, concentration of the radial width tilt, and binomial small-tail concentration prove the \(2-U^2\) random exponent. For each fixed \(a\in(0,1/4)\), empirical Gaussian quantiles give an admissible offset interval of length \(2q_a+o_{L^2}(1)\); dividing by the total width yields the rare-event constant and the stated conditional distribution. The proof does not mistake finite experiments for infinite asymptotic proof. The companion verified standard-library script passed 2,310 edge identities, four finite expectation comparisons, the Gaussian integral identity and three quantile tests.

## Originality — PASS, with residual historical-priority uncertainty

Kabluchko, Litvak and Zaporozhets, arXiv:1511.08479 (first public 2015-11-26), establish Gaussian mean-width and projection laws for regular simplices, not counts of vertices of randomly translated affine sections. Swan, arXiv:1808.09482, studies expected vertices of hypercube slices, with a different body and different exact mean. De Loera, Lopez-Campos and Torres, arXiv:2412.12419, study attainable section vertex counts, without the present affine random law. Closest published regular-simplex section results place the hyperplane **through the centroid** and obtain \(m^2\)-order typical complexity; that fixed-offset law neither states nor implies the rare quadratic probability for invariant affine sections. The published comparison records and the relevant portions of the primary full texts were consulted. Exhaustive priority across old stochastic geometry is not asserted.

## Mathematical value — PASS

The random-exponent limit shows that a typical motion-invariant affine section has a random polynomial order between one and two, while its expectation is dominated by an explicitly quantified vanishing event of quadratically complex sections. The Gaussian-quantile tail constant and conditional law expose the mechanism behind the gap between typical complexity and mean complexity. This is a natural high-dimensional random section invariant, not an arbitrary finite computation or routine relabeling.

## Limits and risks

Published comparison records are not substitutes for a full-text inspection of every possible older paper. In particular, Crofton-section combinatorics may be indexed under alternative integral-geometric terminology. No claim is made for nonregular simplices, other hyperplane measures, fixed or moving endpoints \(a\), or higher-codimension sections. Numerical checks validate finite identities and sample behavior but cannot certify asymptotic limits.

Self-review: passed. Independent audit: not yet performed.
