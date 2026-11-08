# Independent mathematical audit

## correctness

PASS

With B=1-1_{no *} and P(no *)=s^n, Cov(B,K)=s^n[E K-E(K|no *)] holds. Conditional residual observations are iid t and give F(s)=1-s^n+sum((1-t_i)^n-(1-st_i)^n). Its second derivative equals -n(n-1)[s^{n-2}+sum t_i^2(1-st_i)^{n-2}]<0. F(0)=1-E_t K_n<0 for n>=2 and r>=2 positive t; F(1)=0; F′(1)<0. Strict concavity produces exactly one interior zero, with signs negative then positive. The limit H(x)=1-sum exp(-xt_i) has a unique positive root and positive derivative, so the O(1/n) Taylor correction in F(x/n) gives the stated negative second coefficient and O_t(n^-3) in sigma. For n>=r+1 and s<sigma, the conditional mean of K given B=1 is smaller than when B=0; yet K=r+1 has positive probability given B=1 and is impossible given B=0. Thus neither conditional law FOSD-dominates. Independently enumerated 76 exact rational cases (4 profiles, n=2..6 or 5, 4 s choices), also checked sigma_2=1/3, and ran 4 high-precision root profiles at n=100,500,2000 confirming the second-order coefficient. No finite test substituted for the analytic all-parameter argument.

## originality

PASS

Best-knowledge PASS for the global unique concentration-path sign transition, its fixed-profile Poisson-scale second coefficient and the conditional first-order stochastic-incomparability regime. Prior occupied-box indicator covariance identities already imply the raw finite Cov(B,K) expression, which is not a new identity. Their pairwise anti-correlation and positive inverse do not mathematically force the row-sum sign or its unique parameter switch. The published equal-box richness--frequency-count switch changes a frequency index instead of distinguished-cell mass. Bogachev--Gnedin--Yakubovich 2006 supplies the cross terms in the variance of the occupied-box count and pursues infinite-box asymptotics, not the present finite-species one-parameter threshold. Complete arXiv 2022 missing-mass paper studies estimator risk, Fisher scoring and bounds, not this conditional covariance. A highly relevant 2009 ecological occurrence/richness study remains full-text inaccessible: its spatial site-incidence design is distinguishable in abstract but the whole-document priority implication is not ruled out. Searches did not expose exact prior dominating theorem; remaining risk is explicitly preserved.

## value

PASS

Covariance between a particular species being observed and total observed species richness is an interpretable natural indicator in occupancy/ecology: the direct positive contribution of that species competes with negative cross-occupancy correlations. The sharp finite-n one-switch theorem resolves which mechanism wins along any fixed heterogeneous conditional community profile; the Poisson-scale root and explicit second coefficient describe when a rare distinguished species crosses the boundary as sample size grows. Conditional richness distributions can lack even first-order stochastic ordering despite a definite mean sign, giving a meaningful methodological boundary. These precise mathematical facts are not known table recomputation nor a renaming of pairwise covariances, although the raw identity is earlier work. No general ecological causality or empirical dataset claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
