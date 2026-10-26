# Self-review

## Correctness — PASS
The bit-linear ADRT offset from Rim (2026), Lemma 2.1, yields independent column-bit errors \(e_i=(b_i-x_i)/2\). Maximizing over column bits gives a slope-specific exact formula and a bit-reversed witness. The negative extremum has no greater magnitude because the sum of column coefficients equals \(s/N\ge0\). A two-action Bellman recursion, solved by an explicitly checked two-branch induction and scalar recurrences, gives the global sharp constant for every \(n\ge1\). The lower bound is attained by a finite control word and its reversed-bit column; exhaustive rational tests are supplementary, not the infinite proof.

## Originality — PASS with disclosed residual risk
The nearest established results are the 2017 Ershov–Karpenko and 2023 Smirnov–Karpenko sharp deviations relative to the **endpoint-joining** line \(st/(N-1)\). They do not supply the exact **normalized-slope** \(st/N\) maximum or a slope-specific bit-reversal certificate. Rim (2026) explicitly uses the latter geometry but states only \(n/2\). Kazimirov et al. (2026) discusses line-approximation error in a broader algorithm-comparison setting, not the stated normalized dyadic exact formula in material inspected. The older results' coefficient \(1/6\) is prior art; this work's potentially original content is the changed normalization's exact finite correction and local calibration. Additional uninspected supplementary material and alternate terminology remain risks; database search alone is not treated as evidence of novelty.

## Value — PASS
A row-index enclosure for the line at slope \(s/N\) is a natural accuracy certificate for numerical Radon-line sampling. The verified optimal global tolerance has leading coefficient \(1/6\) instead of the published \(1/2\), while the fixed-slope formula computes exact local tolerances in \(O(n)\) arithmetic per slope. The parity-dependent correction gives the exact clearance even on small grids; the geometric statement has definite use independent of downstream inverse-reconstruction guarantees.

## Closest sources and limitations
Primary numerical-analysis motivation: Kazimirov et al., *Mathematics* 14 (2026), 1136, DOI 10.3390/math14071136 (first MSC 65R10). Explicit normalized-offset definition: Rim, arXiv:2610.23363v1, Lemma 2.1. The strongest nearby older geometry is Ershov–Karpenko, arXiv:1712.05615, and Smirnov–Karpenko, arXiv:2311.10064, both using the \(N-1\) endpoint normalization. The theorem excludes general inverse accuracy, non-dyadic widths, and the endpoint-normalized metric. Full text of some connected algorithm-comparison supplemental material was not accessible; equivalence in older digital-geometry terminology cannot be excluded.

Self-review: passed. Independent audit: not yet performed.
