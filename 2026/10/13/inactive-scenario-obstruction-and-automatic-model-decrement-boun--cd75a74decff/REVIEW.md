# Independent mathematical audit

## correctness

PASS

The exact scalar model is bounded below by w+w²/2=−1/2+(w+1)²/2 everywhere, and at w=−1 the two affine terms are −1 and −2, so the lower bound is attained uniquely with θ=−1/2. Only the first scenario is active at zero, giving directional derivative −1; the inactive product is M>0 and hence exceeds every negative bound of the stated form. Both affine functions meet the smoothness and convexity conditions, and the robust max is bounded below since it grows at both infinities. The obstruction applies to any step prescription requiring the exact direction and the stated all-scenario test at this point; it does not refute convergence conditional on the test. For the general model, G=Ψ_x+∥·∥²/2 is strongly convex and G(0)=0, so G(0)≥G(v)+∥v∥²/2 at its minimizer. The norm bound follows, and each objective's baseline-adjusted model is bounded by Ψ_x(v)=θ−∥v∥²/2. Active scenarios have zero baseline offset and obey the claimed product bound. The frozen supporting script and saved output were inspected, not executed; the calculation here is analytic.

## originality

PASS

The supported distinct claim is a source-model obstruction: a family with strict actual robust descent and unbounded positive inactive-scenario product while the exact subproblem value stays fixed. The active-set descent criterion and exact proximal-model bounds are standard antecedents or elementary consequences of the available earlier model; they do not earn separate originality credit. The best inspected evidence does not cover the explicit counterexample or the specific incompatibility it diagnoses.

## value

PASS

An algorithm cannot require both the exact standard subproblem minimizer and a negative upper bound on all raw scenario-gradient products on the full finite-scenario class. The witness isolates the reason from curvature, line search and solver error: even affine scenarios give a fixed, genuinely descending exact step, while arbitrary inactive slopes defeat the proposed requirement. This diagnoses what to test in this model rather than merely rederiving a proximal inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
