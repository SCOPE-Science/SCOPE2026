# Independent mathematical audit

## correctness

PASS

Specialize the ACTUAL SPAM gradient-estimator-plus-shifted-proximal recursion (not Polyak momentum) to two equiprobable scalar quadratics with curvature h±=a±δ, a>0, 0≤ρ=δ/a≤1, stepsize γ>0, and refresh p in (0,1]. Because the current sampled client is independent of history, the 3-state vector (x_k,x_{k-1},g_{k-1}) has a legitimate closed FIRST-MOMENT linear recursion E[u_{k+1}]=M E[u_k]. An independent derivation of the exact two realized prox transition matrices gave M=[[α,(1-p)(1-α),-(1-p)γα],[1,0,0],[a,-(1-p)a,1-p]], where t=γa, α=(1+t)/((1+t)^2-ρ²t²); the characteristic polynomial factors exactly as (λ-1+p)[λ²-αλ+(1-p)ρ²t²/((1+t)^2-ρ²t²)]. Under the stated nonnegative-curvature range, denominator is strictly positive, and the real quadratic Jury inequalities reduce to (2-p)ρ²t²<(1+t)^2, strict at the stable boundary. Independent symbolic matrix construction and determinant factorization were completed and checked; p=1, ρ=0, ρ=1 limit cases are consistent. In particular t=20,ρ=1 has p_c=359/400=0.8975, explaining why p=0.1 and p=0.9 straddle the FIRST-MOMENT threshold. This does NOT certify bounded second moments, almost-sure iterates or stochastic algorithm convergence in the stronger norms studied in the original paper.

## originality

PASS

Best-of-knowledge PASS for the exact sharp SPAM first-moment phase boundary for two scalar stochastic curvatures, not generic convex-proximal stability. The complete SPAM arXiv primary text was inspected at Algorithm 1, its nonconvex expected-squared-gradient theorem and p-dependent large-step experiment; it contains no such necessary-and-sufficient mean recursion. Full papers Kim–Toulis–Kyrillidis (PPAM) and Loizou–Richtarik (stochastic heavy ball) were inspected where their iteration maps are defined; both have different momentum state and update structure. The exact result is not a corollary of their convergence-region statements.

## value

PASS

The exact necessary-and-sufficient refresh/stepsize/curvature balance is a natural stability frontier for a fully specified, widely analyzed stochastic proximal algorithm, and it is motivated by the SOURCE's conspicuous p=0.1 versus p=0.9 large-stepsize contrast. The quantitative t=20 threshold separates those settings at 0.8975. Precisely distinguishing first-moment stabilization from genuinely stronger convergence exposes a mathematically meaningful gap and avoids overstating the model. The invariant is not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
