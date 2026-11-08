# Independent mathematical audit

## correctness

PASS

After row 2 sweep, error is t v + ζ_{2}a2 with v perpendicular a2; first/second row projection yields t_k=c² t_{k-1}+c s ζ2,k-1-s ζ1,k, preserving the critical one-sweep lag. Independently cached errors have covariance σ_i²(1-r_i)^h, even at refresh endpoints. Filtering yields stationary variance via exactly summed geometric double kernel (1+uα)/[(1-u²)(1-uα)]. Orthogonality gives R=σ2²+(1/(1+u))[σ1²(1+uα1)/(1-uα1)+uσ2²(1+uα2)/(1-uα2)]; the contraction u<1 yields convergence regardless of Gaussianity. On r1+r2=B, minimization of σ1²/(1-u+ur1)+uσ2²/(1-u+ur2) is strictly convex, first-order ratio gives unique clipped minimizer. Independent rational stationary covariance equations were solved and checked at 96 parameter choices. Does not establish finite-horizon optimality.

## originality

PASS

Best-of-knowledge comparison of mathematical claims, implications, aliases and relevant primary texts; general tools are credited and historical priority is qualified. Fixed-order exact two-row cyclic projections with temporally reused right-hand-side measurements differ from randomized Kaczmarz with fresh time-varying noisy equations, and from optimized relaxation/learning-rate schedules. Their update law and objective are not equivalent under a parameter rename.

## value

PASS

The model asks how to allocate a fixed costly measurement-refresh budget between nonorthogonal equations under persistent measurement noise. Its exact stationary risk and clipped global optimum reveal a robust near-parallel tradeoff: refreshing only one row may diverge while a balanced refresh stays bounded. This is a motivated algorithmic noise-design result rather than a generic convergence inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
