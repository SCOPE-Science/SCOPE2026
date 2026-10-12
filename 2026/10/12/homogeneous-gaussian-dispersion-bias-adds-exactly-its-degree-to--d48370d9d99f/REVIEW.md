# Review

## Correctness

PASS. The centered normal sample is an isotropic Gaussian vector on an \((n-1)\)-dimensional subspace. Its residual norm and residual direction are independent, with normalized radius \(\chi_{n-1}\).

A degree-\(q\) homogeneous nonnegative statistic factors into \(R^q\) times a function of direction. Size-biasing therefore factors into an angular tilt and a radial tilt. Multiplication of the \(\chi_d\) radial density by \(r^q\) changes the power from \(r^{d-1}\) to \(r^{d+q-1}\), exactly a \(\chi_{d+q}\) density after normalization. The displayed Laplace, moment, and covariance identities follow.

No differentiability is used, so the proof applies to nonsmooth statistics such as range and Gini mean difference.

## Originality

PASS, with a residual risk from older spherical-distribution literature. The closest full inspected normal-sample sources focus on independence from the sample mean, studentized order statistics, or characterization of the normal law.

The Hu--Lin full manuscript explicitly covers positively homogeneous residual statistics, including sample range and Gini mean difference, but targeted searches found no size-bias, covariance, chi-square dimension-shift, or polar-law statement. Hwang--Hu's 1994 full paper identifies scale-free residual directional structure and exact studentized-order-statistic distributions, but does not state the homogeneous size-bias law.

Targeted database searches for the exact size-biased chi-square shift and for normal range/variance covariance did not locate a matching statement.

## Value

PASS. Range, Gini mean difference, mean absolute deviation, standard deviation, and many other dispersion measures are homogeneous functions of a centered sample. Their joint laws with sample variance are generally nontrivial.

The theorem gives an entire weighted distribution, not merely one covariance: under weighting by any degree-\(q\) statistic, sample variance acquires exactly \(q\) additional chi-square degrees of freedom. It consequently supplies all mixed powers with sample variance from one structural identity, independently of the angular details of the dispersion statistic.

Self-review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK exact_integer_moment_checks=700 gamma_moment_checks=560 covariance_checks=140 degree_one_checks=20`.
