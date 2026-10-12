# Review
## Correctness
PASS. Conditioning on the represented support gives a uniform occupied subset and a uniform surjection of the labeled bootstrap positions onto that subset. A one-pair merge gives the exact Stirling ratio controlling the second moments of the bootstrap weights. Centering the observed data then yields the conditional variance. A separate exact multinomial calculation gives the global covariance. Exhaustive rational enumeration of small bootstrap samples independently reproduces the formulas.

## Originality
PASS. The closest completely inspected paper identifies random bootstrap support size as an information-content problem and develops fixed-support sequential resampling, but does not state the exact finite conditional variance or covariance here. Follow-up work treats asymptotic correctness of modified schemes. Published-formula searches across bootstrap, unique-observation, occupancy, and Stirling-number aliases did not locate a covering statement. An unindexed historical identity remains a residual risk.

## Value
PASS. Support size is the classical quantity behind the approximately 0.632 fraction of represented observations in the ordinary bootstrap. The result gives an exact finite calibration of how that support diversity controls uncertainty in the bootstrap mean, including a strictly negative support-size/squared-error covariance and transparent no-repeat and one-support endpoints.

## Closest literature and limitations
The result concerns the conditional nonparametric bootstrap mean for uniform resampling of labeled observations. It does not cover studentized or nonlinear statistics, weighted bootstraps, or support counts that merge tied numerical values. The strongest comparison is the fixed-support sequential-bootstrap literature, which is asymptotic rather than an exact conditional analysis of the ordinary bootstrap.

Self-review: passed. Independent audit: not yet performed.
