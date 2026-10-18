# Independent mathematical audit

## correctness

PASS

Poisson u_a(k) is log-concave with interval support; the kernel u_a(x−z) is TP2. Product of all latent factors is MTP2, and marginalization over common Z preserves it (Fallat et al., Prop3.4(ii)). The joint pair-sum coefficient kernel g(x,s)=[t^(s−x)]e^(at)(a+bt)^x/x! has adjacent minors equal to nonnegative log-concavity expressions, establishing LR monotonicity for every pair. Since S_n=T_n+nZ, T_n~Pois(na), condition on S_n=n−1 gives Bin(n−1,1/n), and on S_n=n gives w Bin(n,1/n)+(1−w)δ1 with w=(na)^n/n! divided by that plus b. Therefore the tail-2 gap changes sign exactly at b_ST=(na)^n/n! * δ_n/r_n with r_n=Pr(Bin(n−1,1/n)≥2) and δ_n=(n−1)/n²(1−1/n)^(n−2). At n=3, exact conditional mass ratios yield LR iff b≤2a³, ST iff b≤6a³. Independently checked exact rational thresholds at n=3..12 for b/bcrit=1/2,1,2; finite samples corroborate but universal proof is analytic.

## originality

PASS

The exact MTP2 common-shock counterexample and distinct LR/ST adjacent-level frontiers refine dependent-sum monotonicity results. The primary sufficient condition on (Xi, sum(other Xj)) is stronger/different, and its examples do not give these precise common-shock thresholds.

## value

PASS

A sharp structural boundary of dependent conditional ordering in a canonical MTP2 positively correlated multivariate Poisson model. Exact distinct LR/ST cutoffs provide reusable risk/association counterexamples with explicit dimension dependence, beyond mere numerical nonmonotonicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
