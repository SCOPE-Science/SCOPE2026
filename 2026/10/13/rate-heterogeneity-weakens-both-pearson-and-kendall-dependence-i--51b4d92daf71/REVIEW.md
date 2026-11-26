# Independent mathematical audit

## correctness

PASS

Write L=λ1+λ2, a=cL, p=λ1/L and q=λ2/L. In the specified exponential model, the first-failure time S has rate a and is independent of the first-failure label; conditional on the label, the survivor has an independent residual at its full-load rate. The two residual add-ons are mutually exclusive, so their covariance is −(q/λ1)(p/λ2)=−1/L²; the first marginal variance is 1/a²+2q/λ1²−q²/λ1², and the other follows by exchange. This verifies the covariance and Pearson formula. Independently for Kendall, compare two copies: their first-failure time difference is symmetric Laplace of rate a. When both first failures have the same label and the survivor rate is λj, discordance has probability a/[2(a+λj)] by the Laplace difference of the two independent survivor residuals. For opposite labels, discordance occurs when the first-failure difference lies between the negative of one residual and the positive of the other, giving 1−λ1/[2(a+λ1)]−λ2/[2(a+λ2)]. Weight by p², q² and 2pq and use τ=1−2 P(discordance) (ties have probability zero). Simplification reproduces the published coefficient. The squared Pearson denominator is 1+c²(s²+2s−2)+c⁴(5+2s), s=r+1/r≥2; Kendall's denominator after normalization is c(c+1)s+2c²+2c+1. Both increase strictly, with positive numerators in the stated regime, and diverge under extreme rate imbalance. The equal-rate values and uniqueness follow at s=2. An exact SymPy replay verified the rational identities and obtained Kendall values 1/4 versus 8/35 at c=1/2 and respective rates (1,1), (1,2).

## originality

PASS

Pass for the heterogeneous Pearson expression and its strict rate-imbalance comparison. The Kendall formula is already published; the equal-rate maximum and the reversal of the source prose follow directly from that formula and receive no credit as a new Kendall theorem. The frozen result explicitly makes that attribution. No statement covering the distinct heterogeneous Pearson result was established in the inspected material.

## value

PASS

Pearson dependence for the same heterogeneous model used in the prior Kendall study is a natural missing exact quantity: it separates the effects of relative load rates from the common load factor and proves that equal-rate modelling overstates both correlations relative to rate-imbalanced alternatives at the same c. The exact covariance and variance ratios give usable calibration and boundary checks. The value judgment rests on the heterogeneous Pearson result, not on reprinting the published Kendall expression or the routine final derivative.

The dated certificate retains the supplied scientific assessment, sources and limitations.
