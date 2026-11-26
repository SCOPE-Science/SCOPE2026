# Independent mathematical audit

## correctness

PASS

The migration weights and death factor 1/2 agree with the source model's Appendix B in the specified symmetric equal-rate case. Clearing the two stationary denominators gives P+Q=(x−y)[1−(1−m)(x+y)]. At the isolated equilibrium the Jacobian is diag(−1/6,−1/4); the implicit branch has X=1−2m+4m²+O(m³), Y=3m−3m²+O(m³), so it stays in the physical rectangle and has X≠Y. Thus F(m)=1/[2(1−m)] there. At m=0 the artificial faces of a sufficiently small rectangle are strictly inward, and this persists uniformly for small m. The physical faces remain weakly inward; the symmetric part of the Jacobian is uniformly negative in that same convex rectangle by continuity. The time-T map is then a contraction, giving one attracting T-periodic orbit there for each T>0. On the x=1 and y=0 faces the inward drift is bounded below by a positive constant times m in the rectangle. Each distance to its physical face therefore satisfies w′≥−Lw+c m(t); integration over any preceding period rules out boundary contact even at isolated times when m=0. The moving branch has bounded derivative and |m′|≤πq/T, so contraction gives a uniform O(q/T) tracking error on the periodic orbit. Averaging F(q cos²θ) and substituting tan θ on the half interval gives 1/(2√(1−q)). It is strictly between F(q/2) and F(q); Taylor expansion of the equal-mean excess yields q²/16. This is local and adiabatic, not an all-amplitude, all-finite-period or stochastic-fixation statement. The frozen checker was inspected, not executed; the algebra and limit were independently reconstructed.

## originality

PASS

The two-deme model, forcing schedule and average-frequency observable are established prior work. The supported distinct claim is the exact stationary balance on the small-migration separated-deme branch and its consequent slow-period value strictly between the equal-mean and peak baselines. In particular the source's full-amplitude interpretation does not state this answer; tracking the frozen equilibrium throughout the cycle gives a different limit in the proved regime.

## value

PASS

The exact adiabatic invariant answers a specific comparison left ambiguous in the motivating model: matching the time-mean migration gives a strict increase, whereas matching its peak gives a strict decrease. The branch formula and uniform tracking establish this baseline dependence for a nonempty interval with a quantified leading excess, rather than drawing a conclusion from a few finite-period simulations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
