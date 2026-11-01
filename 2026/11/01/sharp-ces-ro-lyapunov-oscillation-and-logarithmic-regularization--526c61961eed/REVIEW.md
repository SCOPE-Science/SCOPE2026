# Scientific review

## Correctness — PASS

The source's exact coordinate derivative formula gives an alternating sequence of \(\log\lambda_1\) and \(\log\lambda_2\) in successive geometric blocks. The proof checks the geometric sum at every block endpoint, constructs the uniform signed-walk scaling profile, integrates the normalized walk and optimizes the last-block phase explicitly. The complete cluster set follows from exhaustion of the time intervals between consecutive block endpoints. A separate alternating-harmonic-block estimate proves the logarithmic mean converges. `verify.py` independently checks finite integer identities and several phase values; those finite tests are not substitutes for the analytic proof.

## Originality — PASS within inspected evidence

The closest primary paper is Nakano, Soma and Yamamoto, arXiv:2206.09508v1 (2022), which proves the earlier unaveraged Lyapunov cluster ranges and gives the exact geometric-block derivative sequence used here. This dependence is acknowledged. The new result concerns the different statistic formed by *averaging those finite-time exponents*; its sharp interval requires an additional self-similar integral and interior extremization, while convergence of its logarithmic weighting requires another summability argument. Relevant observable-irregularity literature and published mathematical-index comparisons did not yield an equivalent second-averaging statement. This bounded priority comparison leaves the risk of unindexed earlier formulas or stronger results.

## Mathematical value — PASS

This natural large-time statistic tests whether time averaging suppresses observable Lyapunov irregularity. The answer is quantitatively negative for arithmetic means but positive for logarithmic weighting, with all thresholds explicit. The strict interior extremum provides information not visible in the original block-end exponent limits.

## Limits and remaining risk

The dynamical realization and its first-order derivative sequence belong to the 2022 source and are not claimed as new. The present theorem is proved for the original coordinate tangent vectors on the full-measure derivative-defined subset of its wandering rectangles; it does not address mixed vectors, invariant-measure typical points, or arbitrary expanding maps. Exhaustive priority assessment would require further independent literature review.

Self-review: passed. Independent audit: not yet performed.
