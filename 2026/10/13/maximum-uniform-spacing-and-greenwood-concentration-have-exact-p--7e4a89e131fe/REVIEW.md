# Self-review

## Correctness
PASS. The proof starts from the exact uniform-simplex law. On a \(k\)-fold threshold event, translation by \(x\) leaves residual simplex mass \(1-kx\), and normalized residual coordinates remain uniform Dirichlet. This yields the conditional quadratic moment exactly. Inclusion-exclusion and two standard alternating binomial identities produce the mixed moment. Subtracting the exact marginal means gives the covariance. The strict sign follows from the exact increment identity \(F_m-F_{m-1}=2(H_m-1)/m>0\). The displayed correlation uses independently reconstructed exact variances of the maximum and Greenwood statistic. The attached checker replays all algebraic components with exact rational arithmetic.

## Originality
PASS, with a classical-spacing residual risk. Pyke's spacing review explicitly surveys Greenwood's square-sum statistic and maximum/ordered-spacing statistics as separate tests, while Mirakhmedov studies Greenwood efficiency and Royen studies the marginal Greenwood distribution. The inspected statements do not give the joint mixed moment, the covariance formula, or the correlation asymptotic proved here. Scientific searches using maximum-spacing, Greenwood, Dirichlet maximum, square-sum, covariance, joint moment, and harmonic-number formulations did not locate an equivalent or stronger statement. The remaining risk is an older random-division or ordered-spacing source using different notation.

## Value
PASS. Maximum spacing and Greenwood concentration are canonical, complementary summaries of the same random partition: one records the most extreme local gap and the other records global quadratic unevenness. Their finite-sample dependence matters when the two diagnostics are interpreted jointly. The exact positive covariance and explicit vanishing-correlation rate quantify a relationship not supplied by their separate marginal theories.

Self-review: passed. Independent audit: not yet performed.
