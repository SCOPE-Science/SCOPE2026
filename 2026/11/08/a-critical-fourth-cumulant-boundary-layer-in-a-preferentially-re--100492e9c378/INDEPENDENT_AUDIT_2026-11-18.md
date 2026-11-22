# Independent mathematical audit

## correctness

PASS

Re-audited the final narrowed RESULT.md: the Boyer--Majumdar exact Fourier/Kummer formula gives a holomorphic slow branch a(z,rho) and a fast branch whose exponent has a uniform strictly positive gap for rho in a thin complex neighborhood of [3/2,5/2]. Kummer transformation and sectorial asymptotics then yield E=O(t^-eta) uniformly in z and rho, and Cauchy differentiation gives two z derivatives and one rho derivative with the same power bound (shrinking eta for logarithms). Independent SymPy expansions confirm a=z/(2rho)+(rho-2)z^2/(8rho^2)+..., log C coefficients (rho-2gamma_E)/(4rho) and (15rho^2-12gamma_E rho-24-2pi^2+24gamma_E)/(96rho^2). Thus known fixed-rate kappa2, kappa4 expansions hold with uniform rate derivative. For g=(2-rho)/rho^2, g′=(rho-4)/rho^3<0 on I; H′=g′ log(gamma t)+O(1)<0; endpoint signs are opposite, proving one unique zero on I. Expanding about rho=2 yields rho_c=2+(3-pi^2/6)/log(gamma t)+O(log^-2), and h^2 excess kurtosis at rho=2+xi/h tends to 9-pi^2/2-3xi. An independently derived mpmath Kummer differentiation found roots at t=200,2000,20000 approximately 2.424873,2.290769,2.208169 and negative finite-time rho derivatives on a five-point grid at t=3000. Finite tests corroborate but do not prove asymptotic uniformity. v,gamma>0 fixed, r varies only in compact interval; no early-time/all-rate assertion.

## originality

PASS

PASS best-of-knowledge for the substantive final narrowed finite-time rate-uniform threshold, NOT for the original positive fourth-cumulant constant. Material comparison found that the 2026-11-02 published SAME-model theorem already gives the exact fixed-rho O(1) cumulant, critical positive constant v^4(18-pi^2)/(8 gamma^4), and log^-2 kurtosis, so these are removed from the novelty claim and explicitly credited. Boyer--Majumdar 2023 provides the exact transform and leading exponent. Neither consulted published result states the uniform first rho-derivative, unique late finite-time zero throughout [3/2,5/2], its asymptotic displacement, or uniform moving-layer limit. The short Kummer-uniformity upgrade could be seen as an implicit consequence of the prior proof and remains a material residual novelty/value risk; this is not claimed to be a wholly new cumulant formula.

## value

PASS

The natural finite-observation fourth-cumulant sign boundary is not settled by a fixed-parameter eventual sign: a physically meaningful reset rate moves by order 1/log time and can reverse the sign of the leading non-Gaussian statistic. A single exact zero for every sufficiently late finite horizon in an entire compact parameter interval, plus its sharp shifted location and moving-layer profile, is a complete motivated analytic boundary theorem. It remains a narrow consequence of uniform Kummer asymptotics, not a claim to a new fixed-rho cumulant, global phase diagram or landmark result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
