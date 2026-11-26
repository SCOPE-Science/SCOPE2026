# Independent mathematical audit

## correctness

PASS

The centered difference is exactly a⟨x,u⟩ for every positive radius. With v=(I−βP)x the normalized gradient estimate is x+(uuᵀ−I)v. The centered random term has covariance ||v||²I+vvᵀ by the Gaussian fourth moment, so the conditional P and Q variance traces are (k+1)δ²||Px||²+k||Qx||² and rδ²||Px||²+(r+1)||Qx||², respectively. Independence from the past and zero conditional mean give the exact matrix M_s. All nonnegative block-energy ratios can be achieved by initial states, so the uniform t-step factor is the largest column sum of M_s^t and its t-th root tends to the spectral radius. For nonzero δ both off-diagonal entries are positive; for δ=0 the Q mode reaches the larger eigenvalue and cannot be discarded. For positive s the condition ρ_s<1 is exactly s<2/(1+λ_+), including failure of universal decay at equality, and the quadratic minimizer is 1/(1+λ_+). The Perron root strictly increases with δ², including at zero since any positive δ² gives λ_+>r+1; at δ²=1 it is d+1. The exact one-step column sums give the stated max and show equality with unguided probing for each common s when δ²≤1. For β=1 the geometric sum of the upper-triangular powers gives the exact C_t attained in Q, and at r=1 the optimal-step first factor is (d+5)/9. At fixed r the diagonal lower and trace upper bounds on λ_+ give the iff bounded dδ² condition, and the trace and determinant limits give the critical-window formula. The source cubature and scaling checks are bounded corroboration, inspected but not executed. The conclusion concerns mean-square error, not sample-path convergence or total query cost.

## originality

PASS

The general control variate and Gaussian/LMS second-moment method are prior. Stronger exact overlap than just common technique occurs at perfect calibration: the October 25 Resultary affine recurrence for the full-space method has exactly the frozen β=1 homogeneous matrix, and deleting its finite-difference additive term gives the centered perfect-hint recurrence, stability boundary and transient factors by direct powering. The distinct contribution is the coupled imperfect-calibration law and its consequences: the strict phase 0<β<2 in the optimized asymptotic rate, the opposing worst-one-step conclusion across that phase, and the fixed-codimension calibration threshold and critical profile. The comparison does not claim novelty for the β=1 calculation in isolation or exclude less accessible classical coverage.

## value

PASS

A practically meaningful analytic question remains after crediting the perfect-hint recurrence: how much miscalibration can be tolerated before the dimension-free advantage vanishes, and does long-run speed imply uniform short-run improvement? The theorem gives a sharp answer to both in a canonical fixed-codimension model. The first step can grow linearly in d even at the asymptotically optimal perfect-hint step; the new mismatch analysis shows exactly when a dimension-uniform asymptotic factor survives. This is a useful diagnostic model, not evidence of query-cost savings or a nonquadratic guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
