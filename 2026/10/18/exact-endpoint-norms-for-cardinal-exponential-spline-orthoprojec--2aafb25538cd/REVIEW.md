# Independent mathematical audit

## correctness

PASS

The Gram integrals and A−2B=∫(φ(u)−φ(1−u))²du>0 give an invertible Toeplitz Gram operator. The geometric inverse solves the off-diagonal recurrence and gives 1 at the origin by A−2Bq=Δ. The continuous symmetric kernel has uniformly integrable rows by geometric decay. K(x,x)>0 by positive definiteness of the inverse on the nonzero local basis vector; hence the Lebesgue function is positive. In each open cell, a nonzero kernel section satisfies K″=θ²K and any zero gives a nonnegative derivative jump for |K|, so integration gives strict convexity and knots-only maxima. Continuous outputs from bounded compactly supported truncations of the sign of a knot row show that the row maximum is the sharp essential-supremum norm; symmetry and L¹/L∞ duality give sharpness on L¹. The nodal integral is twice a geometric series times its single-crossing cell integral. For a check of the Taylor term, put C=cosh θ, α(q)=(1+q²)/(1+q), β(q)=q²/(1+q)^3. The cell-integral numerator is α(q)(C−1)+β(q)(C−1)²+O((C−1)³). With r=2−√3 and κ=−r/(5√3), this gives J=α(r)/2+θ²[−α(r)/24+β(r)/4+κα′(r)/2]+O(θ⁴). Dividing by Δ(1−q) and including the factor 2 gives 2+θ²/120+O(θ⁴). At large θ, Δ∼1/θ, q→0 and |J−tanh(θ/2)/θ|≤q tanh(θ/2)/θ. Continuity and the two endpoint limits yield attainment above 2 at finite positive θ, not uniqueness. Replay: RESULT.md proof §§1–4 (especially lines 37–97). The supplied check.py was inspected, not run; it uses floating-point checks and a cell antiderivative shared with the formula, plus a separate quadrature check of the row. Neither is the proof.

## originality

PASS

Best-of-knowledge pass for the fixed uniform full-line sharp formula and resulting tension profile. Known Gram/filter machinery, arbitrary-partition bounds, and the linear-spline baseline do not by themselves give those claims. No priority is assigned to those ingredients or to general endpoint norm duality.

## value

PASS

The norm measures exact worst-case endpoint amplification for a standard tension-parameterized least-squares approximation. Neither a universal spline bound nor the limiting polynomial case decides whether introducing tension improves or worsens the constant. The formula, knots-only extremizers of the Lebesgue function, and rigorously nonmonotone positive-tension behavior answer that question without inferring it from sampling. No location or uniqueness of the best tension is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
