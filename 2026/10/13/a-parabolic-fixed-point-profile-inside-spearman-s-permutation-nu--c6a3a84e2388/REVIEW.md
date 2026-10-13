# Review
## Correctness
PASS. Conditioning on \(\Pi(i)=i\) leaves the other positions uniformly matched to the remaining values. Spearman's squared rank displacement is affine in \(\sum_j j\Pi(j)\), so one conditional finite-population mean gives the exact location profile. Summation gives the aggregate covariance. Independent centered-rank covariance algebra gives \(\operatorname{Var}(\rho)=1/(n-1)\), while the two fixed-point inclusion probabilities give \(\operatorname{Var}(F)=1\). Exhaustive exact enumeration through \(n=9\) reproduces every formula.

## Originality
PASS, with a specific historical-enumeration risk. The exact Spearman null literature located determines the marginal distribution of \(\rho\) or its squared rank-difference numerator. The fully inspected Diaconis–Evans–Graham paper determines the fixed-point random set and does not study Spearman's statistic. A prior fixed-point/descent theorem concerns adjacent comparisons, not the global quadratic displacement. Searches across fixed-point, derangement, Spearman-distance, squared-rank-difference, and covariance formulations did not locate the parabolic conditional profile.

## Value
PASS. Fixed points and Spearman's rho are two canonical notions of agreement between rankings: one exact and local, the other graded and global. The location-resolved formula shows that exact matches near the center and extremes have sharply different null effects, and the aggregate identity yields the exact linear calibration \(1+\rho\) for the fixed-point count.

## Closest literature and limitations
The 1938–1939 exact-null literature for Spearman's statistic and the 2013 fixed-point random-set paper are the closest source families. Their marginal results do not determine the joint mixed moment. Full text of the 1939 Biometrika article was inaccessible because the publisher required human verification, so older joint enumeration remains a stated residual risk. The result assumes a uniform permutation and no ties.

Self-review: passed. Independent audit: not yet performed.
