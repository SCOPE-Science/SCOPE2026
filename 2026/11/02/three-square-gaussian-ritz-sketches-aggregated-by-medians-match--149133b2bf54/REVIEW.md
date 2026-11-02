# Self-review

## Correctness

**PASS.** For every output entry, elimination against all but one square Gaussian column reduces the compression error to a deterministic residual-column norm times a ratio of two independent standard circular complex Gaussians. Direct change of variables gives the planar ratio density, then the real coordinate CDF and the transformed beta order-statistic density, with *exact* median second moment \(1/2\) in each coordinate. Summing over the matrix entries proves the square-median risk, while the two-complex-dimensional Schur-complement residual has Gamma shape two and reciprocal mean one, proving the one-row-oversampled risk. The same ratio has divergent squared moment for the unaggregated sketch. These checks cover nonnormal matrices, arbitrary residual column dependence, and the zero-residual boundary. The accompanying verifier independently checks finite cases, but its random samples are not the proof.

## Originality

**PASS on the inspected literature; historical priority is not certified.** Shao's randomized Rayleigh--Ritz study gives square Gaussian pencils and high-probability eigenpair analysis; its reported median is over performance data and not a median of compressed-matrix entries. Its rectangular oversampling comparison is a total-least-squares eigenproblem, not the estimator here. Nakatsukasa and Tropp introduce and analyze least-squares sketched Rayleigh--Ritz, but do not state this median-of-three versus one-row exact-risk equivalence. The established complex Student-ratio, order-statistic and inverse-Wishart identities are properly credited; none alone states the cross-algorithm matrix-risk identity. Available prior related claims concern different randomized Ritz perturbation laws, embedding thresholds and nonreal-spectrum probabilities. A specialized earlier robust-sketch aggregation result might still contain this equivalence.

## Mathematical value

**PASS.** At precisely the square sketch boundary, even a single nonzero residual produces infinite squared compression error in expectation. The three-independent-sketch median restores a finite dimension-explicit expected error and, without tuning or asymptotics, matches the benchmark from adding one Gaussian observation per solve. This supplies an exact robustness-versus-sketch-dimension comparison for a natural randomized Ritz computation. It does not purport to show lower computational cost, eigenpair accuracy or high-probability performance.

## Remaining scope and evidence risks

The numerical procedure uses complex Gaussian sketches in exact arithmetic; real-Gaussian behavior and floating-point effects are different. The studied publications were examined for compression estimators, probability bounds, oversampling and median usages, but inaccessible or older niche robust-sketch results may affect historical priority. No claim of eigenvalue-error improvement is made.

Self-review: passed. Independent audit: not yet performed.
