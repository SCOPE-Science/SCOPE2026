# Independent mathematical audit

## correctness

PASS

For selected labels a<b, there are n-a-1 and n-b unselected labels above them, respectively. Their combined expected label sum is n+1, fixed by the 2/n marginals, so the variance is the expectation of (a+b-n-1)^2. For even n the zero-cost edges form a disjoint perfect matching and each row forces mass 2/n. For odd n, subtract a dual weight of 1 on edges incident to the center (n+1)/2; all resulting costs are nonnegative, and the tight edges are the outer mirror edges and the central triangle. Their marginal equations force 2/n on isolated edges and 1/n on each triangle edge, attaining 2/n and giving the stated envy masses. The triangle-only n=3 case is feasible and unique. Permutation invariance forces the uniform law; order its two labels at random so they are draws without replacement. Their covariance is minus the population variance divided by n-1, giving (n+1)(n-2)/6. This equals the unrestricted value only at n=3; the stated ratio for odd n follows. Replay: `cd /workspace && python audit_checks.py 1` confirms tight supports, exact marginals, direct inversion counts and uniform variances for n=3 through 40; the proof handles all n.

## originality

PASS

The exact parity optimum, forced support and risk law are supported as a distinct evaluation of a previously defined and algorithmically solved optimization problem. The statistic, rule-independent mean, generic linear program and ordinary sampling-variance identity are not new.

## value

PASS

The concrete obstruction to exact balancing for odd n and the unique optimal law are useful benchmarks for dependent rounding with prescribed marginals. The solution distinguishes representational fairness (the same inclusion probability) from permutation invariance, and quantifies a natural variance tradeoff that a per-instance LP output would not explain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
