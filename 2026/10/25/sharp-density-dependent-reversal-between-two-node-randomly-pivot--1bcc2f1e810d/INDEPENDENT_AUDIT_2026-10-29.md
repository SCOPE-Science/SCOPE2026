# Independent mathematical audit

## correctness

PASS

The RKHS feature map Φ=(1,√b cosθ,√b sinθ) makes optimal unrestricted-weight error the squared orthogonal distance from mean feature to the span of two sampled features. A normal vector (−√b cos(Δ/2),cosψ,sinψ) yields the exact conditional orientation-averaged error b[a² cos²(Δ/2)+(u²+v²)/8]/[1+b cos²(Δ/2)]. Under constant diagonal, RP residual gives difference density q_b=4(1−cosΔ)(1+b cos²(Δ/2))/(b+4); iid difference is uniform. Integrating yields RP b/(b+4)(a²+(u²+v²)/2), iid (1−1/√(1+b))a²+b(u²+v²)/(8√(1+b)). Algebraic subtraction factors into ((√(1+b)−1)(√(1+b)−3)/(√(1+b)(b+4)))(a²−b(u²+v²)/8), establishing b=8 and t=√(8/b) exact sign classifications for nonnegative g=1+t cos. An independent numerical integration check covered 28 parameter-target combinations, not an infinite proof.

## originality

PASS

Epperly–Moreno developed continuous RPCholesky and optimal-weight kernel quadrature, while Belhadji–Bardenet–Chainais derived general volume-sampling expected projection errors. For this stationary kernel, RP-only risk is derivable from prior volume-sampling theory and is not novel by itself. The new narrowly specified content is the joint exact iid comparison and density-dependent sign reversal at b=8; that implication is not stated in the inspected passages.

## value

PASS

Exact comparison between two major data-adaptive quadrature sampling schemes matters because general error bounds do not specify which is better on a given kernel/target; the unusual b=8 and modulation-dependent reversal gives a sharp, interpretable counterexample to uniform sampler dominance. Its restricted finite-rank setting is expressly stated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
