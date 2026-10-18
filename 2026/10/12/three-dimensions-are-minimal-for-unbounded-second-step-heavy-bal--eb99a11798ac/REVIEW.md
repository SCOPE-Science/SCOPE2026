# Independent mathematical audit

## correctness

PASS

Diagonalizing the SPD quadratic and setting rho=(sqrt(kappa)-1)/(sqrt(kappa)+1), p1(lambda)=1-alpha*lambda, p2(lambda)=p1(lambda)^2-beta*alpha*lambda. At endpoints, the absolute factors are g_mu=rho(3-2rho)/(2-rho) and g_L=rho(3+2rho)/(2+rho). Their exact difference is 2(r-1)^2/((r+3)(3r+1))>0 for r=sqrt(kappa)>1; the second/first objective ratio in dimension two is a convex weighted average of their squares, so the sharp maximum is g_L^2. The equation g_L=1 is r^2-4r-1=0 and gives kappa=9+4sqrt(5). In dimension three lambda*=1/alpha lies strictly between mu,L, so p1(lambda*)=0, p2(lambda*)=-beta; epsilon-perturbing lambda gives ratio ((epsilon^2-beta(1+epsilon))/epsilon)^2 -> infinity at unchanged exact endpoints. Exact kappa=4 reset f0=9/8,f1=0,f2=1/72 and lambda=20/9 finite ratio 516961/6561 independently checked. The infinite limit is analytic, not inferred from finite verification.

## originality

PASS

The 2018 Danilova-Kulakova-Polyak article gives Heavy-Ball nonmonotonicity and large transient peaks with optimal parameters and examines interior eigenmodes; this is important conceptual prior coverage. It does not give the exact first-to-second objective ratio across all two-eigenvalue quadratic starts, its kappa=9+4sqrt(5) frontier, or a minimal three-dimensional fixed-kappa divergence of this local ratio. A separate published Nesterov three-mode statement is for a different recurrence. Thus the precise joint boundary survives best-of-knowledge implication comparison.

## value

PASS

A sharp early-step objective-monotonicity frontier and a minimal-dimension failure of fixed-kappa adjacent-step bounds are algorithmically motivated boundary facts. The infinite-ratio construction is not global divergence or an arbitrary new invariant: it explains why classical stable momentum can land exactly at an optimizer then leave it, and supplies a quantitative limit for two-curvature safeguards.

The dated certificate retains the supplied scientific assessment, sources and limitations.
