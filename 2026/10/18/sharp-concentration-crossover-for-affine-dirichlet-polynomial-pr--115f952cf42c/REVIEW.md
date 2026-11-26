# Independent mathematical audit

## correctness

PASS

Re-audited /workspace/repairs/4/RESULT.md. The symmetric Dirichlet covariance is 1/[n(na+1)] on the sum-zero hyperplane. The resulting kernel is symmetric and affine in its evaluation point, so the absolute row integral is convex and all vertices give its common maximum. Testing the sign of a vertex row gives the endpoint lower bound even though the vertex itself has zero mass: the output is continuous and the interior has full support. The vertex row has mean one and sign threshold a/(na+1), giving the credited beta expression by truncated first moment. With λ=na, beta–gamma algebra makes YS Gamma(a,1) for S independent Gamma(λ,1), and the difference of the two deviations is bounded by E[Y] times the root mean square of S−(λ+1), exactly √(λ+1)/n. The absolute Gamma deviation follows by integrating the derivative of x^a e^(−x) from 0 to a. At λ→0 the elementary bounds squeeze; at λ→c>0 the beta fractional moment is O(1/n), so n(λ+1)Y→0 in probability and the bounded negative part has limit c in mean. At λ→∞ the relative error is O(λ^(−1/2)+λ^(−1)) for a≤1 and O(n^(−1/2)) for a≥1, by the positive lower bound on g(a) from its asymptotics at zero and infinity. This also gives divergence and the subsequence argument for merely unbounded λ. These checks replay directly from the repaired proof. The frozen formula and analysis are mathematically correct; the repair concerns originality, not a numerical flaw. CHECK.py was inspected, not executed, and its finite regression grid is not the proof of either the bound or arbitrary-path limits. No unequal-parameter or higher-degree claim is validated.

## originality

PASS

For the frozen record the exact endpoint formula fails originality: the distinct 5c9fbf13aa23 Finding covers it for arbitrary positive parameters, hence for the full symmetric family, not only a=1. The repaired RESULT.md credits this result as input and states the finite-parameter Gamma comparison and the joint arbitrary-sequence crossover as the contribution. Fixed-path asymptotics also receive credit. The inspected comparisons do not supply the uniform error or the path-uniform divergent law and boundedness criterion. The equal date on the two records establishes no historical priority.

## value

PASS

The surviving result distinguishes bounded amplification from divergence for every dimension-dependent symmetric concentration path, not just two fixed examples. The uniform Gamma comparison produces leading values for sparse parameters with growing total mass, large parameters and mixed sequences; the exact pointwise norm alone does not expose that quantitative stability threshold. This supports the narrower finding without presenting already covered formula recomputation as the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
