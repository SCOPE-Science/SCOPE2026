# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/09/007`  
**Audited source tree:** `37851046aba406532042766328d3ef011792361b`  
**Date:** 2026-09-26 UTC  
**Disposition:** PASSED

## correctness — PASSED

An independent odd-byte sieve through 5,000,008 and direct four-offset scan found 546 quadruplets, first 5 and last 4,997,381. Consecutive gaps have unique maximum 56,910 at 3,741,161→3,798,071 and runner-up 56,580. Integer-square binning of the 546 least primes gives 478 occupied intervals among n=1..2235 and one longest empty run of length 22 at n=187..208. Direct evaluation with the stated H4 gives a=12690.5171, T0=72353.6324, R0=−1.21694, and sums 538.45224/461.39736. These are finite computations, not statements about all quadruplets.

## originality — PASSED

The maximal gap 56,910 is already in OEIS A113404 and the initial witness 3,741,161 in the record-gap tables; Kourbatov's preprints provide the estimator and long-range gap tables. Novelty is confined to the complete square-interval occupancy and empty-run statistics at this cutoff and their specified heuristic comparisons, not the isolated gap or the Hardy–Littlewood model.

## scientific value — PASSED

The exact 2,235-interval occupancy census and unique 22-interval empty run can serve as a finite benchmark for constellation Legendre-style questions. The bound is modest and the model residual is negative; the record makes no asymptotic or significance claim.

## Prior work

- https://arxiv.org/abs/1301.2242
- https://arxiv.org/abs/1309.4053
- https://oeis.org/A113404
- https://oeis.org/A192870

## Limits

The source artifact was checked against an independent sieve and separate binning. The constant H4 is adopted from the cited model, not independently derived here; its approximations are conditional on that value.
