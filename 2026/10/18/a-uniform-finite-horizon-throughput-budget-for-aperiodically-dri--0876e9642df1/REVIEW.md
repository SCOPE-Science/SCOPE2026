# Independent mathematical audit

## correctness

PASS

PASS: For n>=1, x0=1,x_(n+1)=0 and measurable rates u_i in [m,M], positive-rate equilibrium e(λ) with common current R=λ_i e_i(1-e_(i+1)²) exists uniquely and varies continuously on compact λ-cube. Holding each horizon λ,e fixed, define z=x-e, η_i=(1-e_(i+1)²)z_i−2e_i e_(i+1)z_(i+1), c_i=e_i(1-e_(i+1)²), p_(i+1)/p_i=2e_(i+1)²/(1-e_(i+1)²), normalized Σp_i=1. Summation of the flux conservation laws yields exact pointwise identity q_n+Σ p_i u_i d_i+d/dt[V_λ+Σ_j(Σ_(i<j)p_i)x_j]=Σp_i u_i c_i, with V_λ=1/2 Σ p_j z_j²/e_j and d_i=η_i²/c_i−(1−η_i/c_i)ρ_i. Strict convexity of (1−y²)^(-1/2) implies uniform nonnegative quadratic lower bound for each d_i in successor deviation, including boundary cases; compactness of the equilibrium cube gives Σp_i d_i>=κΣ z_j². Integrate over [0,T], use actual horizon means λ_i and compact storage to get average terminal output +mκ average squared deviation <=R(λ)+C/T, independent of control regularity. If Cesàro means converge, continuity yields limsup and turnpike consequence. For n=1 unit rates starting from occupancy 1, equilibrium e=(√5−1)/2 and transient integral ∫(x-e)dt=log[(e+2)/(2e+1)]>0, so 1/T is uniformly optimal order. Source rational checks (3170 sampled identities) corroborate but cannot prove arbitrary measurable inputs.

## originality

PASS

Best-of-knowledge PASS, with substantial residual priority risk from the closest same mathematical model periodic source that was not accessible in full this execution; decisive global/nonperiodic quantitative implication was not identified from available primary summaries.

## value

PASS

PASS: This is a structurally motivated finite-horizon nonperiodic throughput budget for a coupled nonlinear exclusion chain, strengthening a periodic no-gain result to arbitrary measurable rate schedules and initial transients, while controlling average quadratic state deviation and identifying the optimal inverse-horizon term. The new storage/inventory identity makes the quantified extension substantive rather than a parameter relabeling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
