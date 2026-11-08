# Independent mathematical audit

## correctness

PASS

The strictly concave dual has unique constant optimum c=−ερ/(ε+2ρ) log(κ/n), with block derivatives DT_g=−τWᵀ and DT_f=−τW. The two-block F Jacobian on (f,g) is triangular with upper-left τ²WWᵀ and overwrites g; positive doubly stochastic W has simple constant singular value one and s<1 on 1⊥ by strict Jensen/Perron. Exact scalar translation maximizer δ=(ρ/2)log(mean e^(-f/ρ)/mean e^(-g/ρ)) gives Dδ=0.5(mean dg−mean df); after two raw updates the recovered constant-mode multiplier is −τ(1−τ)/2, while nonuniform eigenvalues remain τ²σ_j(W)². Thus q_G=max of this magnitude and τ²s², proving both thresholds and equality. Independently built nonlinear finite-difference Jacobians for n=2,3,5 and five ε/ρ ratios (15 parameter cases × F/G), including nonsymmetric W, agree; finite differences are corroboration, not all-n proof.

## originality

PASS

Best-of-knowledge priority: compared actual claims and implications of identical/nearby primary sources, searched semantic published record corpus and theorem aliases, and explicitly separated existing methodology/qualitative findings from the exact new result. No located prior implication dominates this final scoped theorem; genuine inaccessible and general-coverage risks remain recorded.

## value

PASS

The exactly defined extra gauge maximization can worsen local contraction: an explicit, dimension-independent ε=2ρ crossover and oscillating constant mode sharpen the original empirical rule of thumb and distinguish strict kernel-dependent dominant-mode transition. This is a practical local solver comparison on naturally balanced kernels, without claiming global or runtime advantage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
