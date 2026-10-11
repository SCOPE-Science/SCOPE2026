# Independent mathematical audit

## correctness

PASS

Direct minimization expresses the loss as \(\sum_ja_jd_j\) with \(a_j=\min\{(1-\tau)P_j,\tau(1-P_j)\}\). The same gaps expand the centered support in cut indicators, yielding the strict lower bound. The cell average of the mean-zero quantile score has covariance \(a_j\) with each cut indicator, hence the whole loss equals \(\operatorname{Cov}(X,S)\); Cauchy--Schwarz gives the upper edge. Conditional variance gives the displayed closed form for \(C_\tau^2\), and the projected score has at most three levels, producing exactly the stated attainment cases. Fresh exact-rational replay verified 2500 independent profiles/levels, including the covariance identity and both bounds.

## originality

PASS

The closest primary papers define the same quantile-locating asymmetric absolute functional and develop p-quantile absolute-deviation representations, but do not optimize its minimized value relative to standard deviation with a prescribed atom-probability partition. No Resultary or repository theorem was found that states the cumulative-cut lower constant, the cell-projection upper constant and exact attainment classification.

## value

PASS

Minimum pinball/check loss is the canonical unconditional quantile scale, and standard deviation is the canonical quadratic scale. The theorem completely quantifies their interaction for categorical or empirical distributions with fixed frequencies, including a transparent information-loss term when the target quantile cuts through a probability cell. This is a motivated exact profile rather than an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
