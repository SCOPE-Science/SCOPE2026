# Independent mathematical audit

## correctness

PASS

Putting y=|z|² in the normalized area integral gives β times the beta integral B(m+1,β), exactly 1/h_m. The complete orthonormal monomial basis converts each orbit vector to one scalar entry √(h_s/h_m), and summation of squared coefficients over indexed pairs by Tonelli gives the diagonal and the sharp global bounds by testing each basis vector. Initial coverage s₀=0 makes every finite diagonal entry positive. At s_j the new coefficient is one and the prior sum is rescaled by h_(s_j−1)/h_(s_j)→1. Boundedness therefore forces B∞−A∞≥1. On [s_j,s_(j+1)−1] the numerator does not change, so max/min on the gap is exactly the corresponding ratio of h's. Using h_m∼m^β/Γ(β+1) at both endpoints bounds limsup s_(j+1)/s_j by κ∞^(1/β), including adjoining insertions. For any larger q, iterating s_(j+1)≤q s_j eventually gives s_j≤Cq^j, proving the lower count for all sufficiently large real R and then the sharp inequality as q decreases to the bound. For geometric seeds, h_(s_j)/r^(βj) tends to a positive constant. Dividing the partial sum by r^(βj), split off finitely many initial terms (vanishing) and squeeze the remaining terms between geometric sums with constants arbitrarily close to the limit; the post-insertion limit is (1−r^−β)^−1. The gap endpoint ratio tends to r^β, giving the other limit. All gaps are monotone, hence these are the true asymptotic extrema and finite initial entries preserve the frame. Counting geometric degrees gives log R/log r+O(1). For β=1, the dyadic prefix is 2^(J+1)−1 on 2^J≤m+1≤2^(J+1)−1, giving the exact infimum 1 and supremum 2 plus the floor count. These are analytic checks (RESULT.md lines 37–101); the inspected numeric script uses floating-point diagnostics, even for the exact dyadic identity, and was not executed. No claim for general seeds or renormalized iterates, α=−1, or a general global-condition optimum.

## originality

PASS

What survives comparison is the sharp logarithmic degree-count versus high-degree condition ratio for indexed norm-one monomial seeds under the weighted Bergman forward shift, with all-ratio attainment. Existing cardinality results, finite polynomial point-sampling complexity, and thinning of times along given orbits measure different quantities. No inspected result supplies this condition–density relation. This is not a priority certification.

## value

PASS

The count of normalized monomial sensors below a resolution degree is a natural cost beyond minimum generator cardinality. The result determines the precise tradeoff with high-degree conditioning and supplies a construction at every feasible ratio; it does not rely on a small computed improvement or claim generality over arbitrary seeds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
