# Independent mathematical audit

## correctness

PASS

The variance decomposition of the latent occupancy score yields I_k=(1−R_k)/[ψ(1−ψ)], where R_k=E_P[(1−ψ+ψ L_k)^{-1}], and gives a complete-information bound independent of k. Since J_1>0 and J_k tends to zero at fixed ψ, a finite maximizing integer exists. With T=log(1/ψ), a design just above T/d has ψL_k diverging in P-probability by the law of large numbers and R_k tending to zero by boundedness. Below (1−ε)T/d, 1−R_k is bounded uniformly by (ψ/(1−ψ))^θ M_θ^k, exponentially small in T for small fixed θ because the derivative of log M_θ at zero is d. Above (1+ε)T/d, the bound from complete information gives a strictly worse leading constant than the design at (1+η)T/d with 0<η<ε. This confines every maximizer and squeezes the normalized optimum to d. At f=0, the event of any detection is sufficient, with probability ψa_k where a_k=1−(1−p)^k. For k≥2, a_k/k≤p(1−p/2), so the upper bound on J_k is strictly below J_1 for the claimed sufficient range ψ<p/(2−2p+p²).

## originality

PASS

The model and the general idea of repeating visits under false positives are not new. The inspected sources do not give the directed-KL scale for every full-history maximizer, the matched limiting information constant, or its contrast with the one-visit regime. The strongest indexed overlap already accounts for qualitative divergence by a symmetry, so qualitative divergence alone is not credited.

## value

PASS

The result resolves the number of repeats and the leading information payoff in a motivated sites-versus-visits problem, rather than merely detecting that repeats become desirable. The contrast with zero false positives shows which idealization changes the order of the optimal allocation even when a positive false-positive rate is small.

The dated certificate retains the supplied scientific assessment, sources and limitations.
