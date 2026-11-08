# Independent mathematical audit

## correctness

PASS

The deterministic hydrodynamic expansion solves lambda_ddot=omega^2/lambda^2 and lambda_dot=sqrt(2) omega sqrt(1-1/lambda); the stationary Poisson reset age has density h_alpha(lambda)=alpha exp[-alpha F(lambda)] F_prime(lambda), F(lambda)=sqrt(lambda(lambda-1))+asinh sqrt(lambda-1), alpha=r/(sqrt2 omega). Setting U=1/lambda(T), the center macroscopic density is proportional to U and density at x0 z to B_z(U)=U(1-z^2 U^2)_+. The mean q(z)=E[U B_z]/E B_z strictly decreases in z by decreasing likelihood ratios (and removal of high-U mass); q(0)=E[U^2]/E[U]>E U, q(z)<=1/z->0. The covariance is positive multiple of E B_z(q(z)-E U), so a unique threshold exists. For large alpha, moment expansions U=1-(omega^2/2)T^2+O(T^4) and exact covariance Var U/z²Cov(U,U^3) imply z_*^2=1/3+O(alpha^-2). For small alpha, m=E U=alpha(L+O(1)), and for z=k/(alpha L log L) with L=ln(1/alpha), I1(z)~alpha log L, I2(z)~2alpha/(3z); q(z)/m->2/(3k), giving z_*~2/[3alpha L log L]. Independently evaluated positive reset-age integrals with scipy quadrature at alpha=0.2,1,10, finding roots ~1.029090172, 0.795436896, 0.596232179 with strict opposite signs at 0.9 and 1.1 times each root. This corroborates, not proves, the monotone-likelihood-ratio and double-logarithmic asymptotic.

## originality

PASS

Mesquita–Kulkarni–Majumdar–Sabhapandit arXiv:2609.37110 derives the SAME self-similar Thomas–Fermi reset profile, expansion-clock density h(lambda), averaged density and counting/edge observables (Eq. 48–55 on inspected PDF page 17). It already implies every reset-age-induced local density random variable in principle; no novelty is asserted for the profile or mixture construction. The assessed extra result is a unique all-distance covariance sign front for center versus point, plus its fast-reset 1/sqrt3 and slow-reset doubly logarithmic asymptotics. The source sections inspected describe the mean density, particle counting and edge statistics rather than the exact two-point sign boundary; however a full prior conditional distribution logically enables its derivation. Brownian common-reset gases are different profiles. Qualified O pass for structural covariance threshold, not for the reset-age law itself.

## value

PASS

Averaging stationary macroscopic density conceals anticorrelation between central and distant local density across repeated reset ages. The exact unique spatial sign front and sharp slow-reset scale [alpha log(1/alpha) loglog(1/alpha)]^-1 give a meaningful two-point diagnostic and its rate-dependent crossing of initial cloud support, with clear hydrodynamic limitations. This is not a trivial consequence of total mass conservation or a sampled finite grid.

The dated certificate retains the supplied scientific assessment, sources and limitations.
