# Independent mathematical audit

## correctness

PASS

The costate boundary-value system solves the strictly convex scalar LQ problem, and variation of constants yields m_b=e^(2a)-H(a,q_b)/D_b for the true-plant endpoint. The inspected rational-interval script encloses the multipliers with strict signs, r1<1<r2, AB<1 and the nominal-model multiplier. Independence gives E|X_n|^p=|X_0|^p r_p^n. Strict convexity of r_p and the derivative at zero establish the unique p*; the strong law for bounded log multipliers gives almost-sure exponential decay. The realized interval cost is c_b X_n^2 with 0<c_b<infinity, so Tonelli gives infinite expectation and negative log growth gives a.s. finite sum. RK4 is corroborative only.

## originality

PASS

The directly related randomized MPC and time-splitting sources establish first-moment stability/convergence under stated conditions, but the inspected full texts do not imply this exact pair of coarse-horizon true-plant multipliers or the sharp fractional-moment and cost reversal. A broader random-switching MPC theorem remains a priority risk.

## value

PASS

The example isolates a consequential gap between typical stabilization/first-moment decay and quadratic performance: even with stabilizable/detectable scalar dynamics and an unbiased random-batch decomposition, mean-square state and expected accumulated true-plant cost diverge while almost every realized cost is finite. The exact positive moment cutoff gives more than a single failed second-moment test and is robust under small parameter perturbations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
