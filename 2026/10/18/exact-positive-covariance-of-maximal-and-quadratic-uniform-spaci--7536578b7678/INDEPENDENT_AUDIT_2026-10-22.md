# Independent mathematical audit

## correctness

PASS

Uniform gaps have Dirichlet(1,...,1) law. For j selected gaps constrained >t, the translated simplex has factor (1-jt)^{m-1}; conditional G is j t^2+2j t(1-jt)/m+2(1-jt)^2/(m+1). Inclusion-exclusion for M>t and beta-polynomial integration yield I_(m,j)=2[(m+1)/j+1/j^2]/[m(m+1)(m+2)]. Binomial-harmonic sums sum (-1)^(j+1) C(m,j)/j=H_m and /j²=(H_m²+H_m^(2))/2. Thus E[M G]=(H_m²+H_m^(2)+2(m+1)H_m)/[m(m+1)(m+2)], subtract EM=H_m/m and EG=2/(m+1), proving covariance (H_m²+H_m^(2)-2H_m)/[m(m+1)(m+2)]. Its numerator strictly increases from 0 at m=1, with increment 2(H_m-1)/(m+1)+2/(m+1)²>0, so sign holds for all m>=2. The exact marginal variances [m H_m^(2)-H_m²]/[m²(m+1)] and 4(m-1)/[(m+1)²(m+2)(m+3)] produce corr~(sqrt6/(2pi))(log m)²/sqrt(m). An independent exponential-order-statistic third-moment calculation matched every m=2..23 using exact rationals; no finite test substitutes for inclusion-exclusion proof.

## originality

PASS

Best-of-knowledge originality: explicit cross-statistic theorem not established by the inspected primary statements; compare four mathematical implications below. No guarantee of absolute historical priority.

## value

PASS

The largest uniform gap and Greenwood's sum of squared gaps are classical, directly motivated but differently scaled uniformity/irregularity statistics. Their exact finite-sample dependence, unconditional positive sign and sharp diminishing correlation constant are useful for understanding redundant or complementary null diagnostics; marginal spacing laws alone do not provide this mixed moment. It is a natural complete covariance invariant of a standard Dirichlet-simplex model rather than an arbitrary slice or known marginal table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
