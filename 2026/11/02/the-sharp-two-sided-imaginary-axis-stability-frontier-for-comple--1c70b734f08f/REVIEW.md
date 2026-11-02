# Scientific assessment

## Correctness — PASS

The statement is fully quantified for \(R,S>0\) and the polynomial \(P_c(z)=1+z+cz^2\). Formula (1) expresses modulus loss as a quadratic factor, whose convexity makes the two endpoint inequalities sufficient as well as necessary. Each endpoint inequality is an exact closed disk in the coefficient plane. The computed squared center-distance-minus-summed-radii identity proves the two-sided threshold without numerical approximations. External tangency gives unique equality coefficient; an algebraically checked factorization proves the strict interior inequality. The real-coefficient optimum follows by completing the square. The normal-matrix corollary follows from the spectral theorem. The embedded checker independently confirms the nonstandard algebra symbolically and runs exact-rational supplementary cases; it is not used to extrapolate finite observations to all parameters.

## Originality — PASS, with residual priority risk

The closest direct comparison is George, Koellermeier, Jung and Mangan, *Explicit complex time integrators for stiff problems* (arXiv:2601.07730v1/v2). Their Theorem 1 solves the positive-**or**-negative one-sided quadratic problem; their Theorem 2 and Tables 1--2 likewise concern one chosen half-axis. They do not classify all pairs of simultaneously positive endpoint lengths and negative endpoint lengths or give the unique mixed-sign optimizer. Ketcheson--Ahmadia's 2012/2013 optimization and Doehring--Gassner--Torrilhon's 2024 method use real polynomial coefficients for the compared imaginary-axis regimes; their general optimization viewpoints do not supply the present complex-coefficient disk-frontier identity. Targeted literature and public mathematical-record searches for mixed-sign quadratic Runge--Kutta stability, coefficient-disk intersection, complex Euler two-sided spectral intervals, and equivalent formulations located no covering result. Novelty is assessed on mathematical implications, not title differences or a null search alone. Residual risk: an earlier specialized complex-polynomial interpolation or stability-disk result could encode the same theorem without this terminology.

## Mathematical value — PASS

The model is the minimal nontrivial first-order complex integrator that stabilizes imaginary-axis modes. Positive and negative frequencies are simultaneously present in general complex-valued oscillatory discretizations, so the sharp front \(R+S=2\) answers an intrinsic method-design question missed by one-sided optimality. The result gives the exact step bound, proves uniqueness for every imbalance, and quantifies how much complex coefficients help relative to real coefficients; the benefit varies continuously from one to nearly two. The explicit amplification identity and a practical two-stage realization make this a reusable analytical benchmark, rather than a parameter substitution or numerical table. It does not claim improved overall accuracy or nonnormal stability.

## Scope and historical limitations

The objective is continuous-interval contractivity of a linear two-stage, first-order polynomial, not higher order or arbitrary nonnormal spectra. Published sources and accessible own-history comparisons do not establish complete mathematical priority; remaining equivalent specialized work is an acknowledged risk. No independent audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
