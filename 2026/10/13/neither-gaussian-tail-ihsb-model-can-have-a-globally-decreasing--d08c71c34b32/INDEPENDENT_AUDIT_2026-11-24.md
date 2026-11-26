# Independent mathematical audit

## correctness

PASS

The primary article's Proposition 4 gives the frozen normalization: the hazard is x^(alpha−1) R_0(x)/m_alpha(x), and the common density/survival normalizer cancels. The exact model formulas use the frozen scales. For the two baselines, put nu=−1 (half-normal) or nu=1 (Maxwell). Their survival is asymptotic to a positive constant times x^nu exp(−x²/(2 beta²)); comparison with each exact density gives baseline hazard h_0(x)~x/beta² without differentiating a big-O error. Both q=beta² x^(alpha−2) R_0(x) and m_alpha tend to zero, m_alpha' is everywhere negative, and q'/m_alpha'=beta² h_0(x)/x−beta²(alpha−2)/x²→1. Hence q/m_alpha→1 and the transformed hazard tends to infinity on the right with the stated equivalent. Tonelli applied to X_0^alpha=∫_0^{X_0} alpha t^(alpha−1) dt gives the finite strictly positive m_alpha(0); lower-endpoint continuity gives the second equivalent. Right divergence excludes even nonincreasing behavior. For 0<alpha<1 both ends diverge, so minimizing on a compact subinterval cut off above a fixed interior value gives an interior global minimum. The hazard is nonconstant real analytic on (0,infinity), so such a minimum is also an actual local turn. The independent tail-moment calculation at alpha=0.1, beta=1 finds local minima near 0.7925118344 and 0.6556500382 and reproduces the hazard values at those points and at 0.1 and 10.

## originality

PASS

The published model definitions and Gaussian tail expansions are antecedents. The best supported distinct result is an all-parameter exclusion of a hazard class explicitly named in the primary article's figure discussions, with a common asymptotic slope and the interior-minimum consequence. The actual primary passages were retrieved and checked; the closest indexed analog concerns a different endpoint mechanism.

## value

PASS

This answers a concrete error in how two published lifetime models can be used: neither can represent globally decreasing failure rates. One analytic tail mechanism settles all shape and scale parameters and explains why a descending segment on a finite window cannot establish global decrease. For shapes below one it additionally proves the existence of a turn without relying on optimization of a plotted curve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
