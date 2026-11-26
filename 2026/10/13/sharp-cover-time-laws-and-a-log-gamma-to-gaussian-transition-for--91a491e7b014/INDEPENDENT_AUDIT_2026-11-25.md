# Independent mathematical audit

## correctness

PASS

Re-audited the replacement critical-window theorem. At equal positive unseen counts, ordered success thresholds give a monotone coupling; at unequal counts a one-step decrement cannot reverse the order. Conditional reconstruction of the individual walk steps preserves full history-dependent marginals. Under greedy, each side's count transition depends only on its own count, so disjoint step subsequences give independent clocks; the initial side subtracts the deterministic geometric with k=m, and the other side first arrives at odd time. Independently checked 117 small finite CDFs against an exact visited-set Bellman recursion. In the replacement transform, a_m=mε_m/(1−ε_m) stays bounded, p_{m,k}=(k+a_m)/(m+a_m), and b_m(s)=(m+a_m)(exp(s/m)−1)=s+O(1/m) locally uniformly, so both positive and negative small s are admissible. The exact gamma product then gives the moment transform Γ(c+1+s)/Γ(c+1); the centering factor m^(s−b_m(s)) tends to one. Joint independent convergence and the parity offsets give the asserted maximum and the square of the upper incomplete gamma ratio, including the shifted Gumbel at c=0. The removed supercritical statement in the frozen record was mathematically sound: integral comparison gives variance asymptotic m/ε_m and a normalized third absolute moment sum O((mε_m)^(-1/2)+(mε_m)^(-3/2)), hence a one-side CLT and a maximum for the full walk. Its removal is a scope/originality decision, not a counterexample.

## originality

PASS

Originality FAIL for the frozen combined finding as framed: the advertised exact finite law and optimality are fully covered by a broader distinct indexed finding (c51f7839a720), without any inference of priority from the later path date. The replacement no longer claims them as contributions and credits them as ingredients. It retains the real-valued critical-window law alone, with the c=0 and positive integer cases explicitly related to partial coupon collection. The ordinary partial-collection reduction does not provide fractional critical intensities; the term-by-term comparison and source inspections did not yield an already stated all-real critical theorem. This is a bounded best-of-knowledge PASS for the repaired claim only. The supercritical CLT is not retained as a distinct result: at diverging affine shift it is closely tied to a growing integer number of missed coupons (rounding the shift by at most one changes the mean clock by O(m/a_m), below the m/√a_m fluctuation scale). The comparison does not assert that the uninspected classical paper proves the full frozen steering result.

## value

PASS

The narrowed result resolves a natural scale for control: when steering has probability of order 1/m, the parameter can change the limiting shape rather than just improve an expected time bound. It gives the optimal full distribution at all real intensities in that window; neither the exact finite recursion nor an integer-only partial-coupon stopping rule gives an expression for physically allowable fractional intensities by substitution of a coupon count. It also keeps separate the one-side log-Gamma law and the two-side maximum needed for cover time. The value does not depend on credit for the known finite law or on retaining a separate CLT.

The dated certificate retains the supplied scientific assessment, sources and limitations.
