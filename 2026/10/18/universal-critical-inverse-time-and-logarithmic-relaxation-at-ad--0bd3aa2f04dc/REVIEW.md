# Independent mathematical audit

## correctness

PASS

At both faces the reward derivative of the displayed Lyapunov function cancels (x−x*)(a−a*) from its x derivative, leaving −(x−x*)(q(x)−q(x*)). The x term diverges at 0 and 1; the reward term diverges at the opposite face and is smooth on the included critical face. Thus the compact sublevel argument and largest-invariant-set test give convergence for every strict interior start. In the oriented system y>0 at finite times; z eventually becomes positive because it crosses z=0 only toward z>0, and remaining nonpositive prevents y→0. The exact ratio h=z/y solves a scalar linear tracking equation along the orbit with positive limiting damping F*q₁ and limiting forcing F*, so h→1/q₁ and 1/y∼Dt/q₁. Writing k=1/q₁, the quadratic graph coefficient m for z=ky+my² is fixed by −Dk²=F*(−q₁m−σq₂k²/2). The derivative of F cancels at this order. This coefficient is not merely formal: the ratio error h−k−my obeys a damped scalar equation with O(y²) forcing, hence is O(t⁻²) by exponential convolution. The reciprocal derivative is Dk+(Dm−Dk/L)y+O(y²); integrating once and reinserting y=(Dkt)⁻¹+O(log t/t²) gives the stated log coefficient and integrable remainder, hence finite C. No feedback-speed restriction is used. The log coefficient is allowed to vanish. Independently reproduced the two exact examples with python3 /workspace/audit_checks.py, check 2 (A=21/4 and 21/16; B=160/3 and 643/48). The frozen verifier was inspected, not executed; finite integration is not a premise of this result.

## originality

PASS

Pass is for the simultaneous, model-specific quantitative asymptotics on both equality faces for all interior starts. The motivating model, its bifurcating equilibria and qualitative selection are not asserted as original. The record's reference to previous qualitative selection at both faces is uncited and not pinned down by the accessible evidence; the independent proof establishes it without using that attribution. The inspected same-model records are for strict interior coexistence. The earlier logarithmic law in a different planar model is a substantive precedent for the form of the result, not for these amplitudes, the speed-dependent correction, or the two-face basin assertion.

## value

PASS

Both endpoint equalities are intrinsic boundaries of the published equilibrium cases. Exact physical-time amplitudes for every interior start are useful near reward saturation, and the logarithmic correction detects feedback speed even though the leading laws cannot. The finite residual constant confirms genuine logarithmic asymptotics rather than a rate fit, without implying validity for edge-initialized trajectories, stochastic populations, or joint ε→0 limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
