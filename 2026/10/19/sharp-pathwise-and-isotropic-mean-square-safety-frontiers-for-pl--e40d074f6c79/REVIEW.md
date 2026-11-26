# Independent mathematical audit

## correctness

PASS

The first sketch imposes r₀ᵀr₁=0 and gives r₁=(I−αA²)r₀ with α=||r₀||²/(r₀ᵀA²r₀). Put P=a², Q=b² and s=P cos²θ+Q sin²θ. In the eigenbasis the relative norm is (κ²−1)t/(κ²+t²) with t=|tan θ|; differentiation gives the maximum at t=κ for κ>1, with zero residual for κ=1. As an independent check on the angular mean, the squared relative norm is (P+Q)/s−PQ/s²−1. Integrating over uniform θ gives E[1/s]=1/√(PQ) by the tangent substitution, and differentiating with a common shift in P,Q gives E[1/s²]=(P+Q)/(2(PQ)^(3/2)). Thus the mean is (κ−1)²/(2κ). The strict increase set is between the two positive roots of t²−(κ²−1)t+κ² when κ>1+√2. Integrating the half-Cauchy direction law and using the root product κ² gives the stated arctangent and limit; the event is empty at equality and below. If r₁≠0, the orthogonal r₀,r₁ span the plane and force r₂=0 in the next exact sketch projection. Eigenvalue signs disappear through A².

## originality

PASS

The update is an exact steepest-descent residual map and its deterministic extremum is prior coverage; the two-step termination is also prior. The strongest earlier indexed match already gives the same deterministic frontier for an equivalent first-step LSQR normal-residual map in the planar symmetric case. The supported distinct result is the exact isotropic squared mean, its different sharp frontier, and the angular probability of strict growth. The earlier deterministic extremum does not determine an angular mean or the measure of the expanding set.

## value

PASS

The planar isotropic law shows a real distinction between pathwise safety and mean-square safety for the same residual step: an interval of condition numbers permits a nonzero fraction of expanding directions even while the mean contracts, and the probability formula quantifies that fraction. These exact benchmarks address distinct notions of residual safety in the minimal dimension where they can differ, without confusing finite termination with monotonicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
