# Review of the complete binary seven-column coverage-depth spectrum

## Correctness

**PASS.** The probabilistic definition yields the displayed subspace-Möbius tail formula: seven planes have coefficient one, seven lines coefficient minus two, and the zero subspace coefficient eight. Because each full-rank profile assigns mass less than one to every proper subspace, its exact expectation is the sum of convergent geometric series. Every binary \(3\times7\) matrix is represented by exactly one of the \(3432\) eight-vector column-multiplicity profiles. A deterministic complete search checks ranks, expectation equality against the independent information-set formula, all \(42\) exact spectrum levels and their weights. A separate enumeration of all \(2097152\) ordered matrices verifies the multinomial weighting. Dividing by the free row-basis action of order \(168\) establishes the count per labeled code and its exact ensemble variance. All \(42\) second-level profiles have the stated missing-and-repeated-point structure.

## Originality

**PASS, with a stated residual risk.** Bertuzzo–Ravagnani–Yaakobi (arXiv:2507.20639, 2025) explicitly reported the same best value \(47/12\) and lower bound \(17/4\) in Example 1, so **neither is claimed as new**. The general simplex optimality proved by Kong–Elishco–Wang–Duman and Gross et al. in October 2026 is likewise prior. Gross et al. compute random-code mean performance, not the present exact histogram of all labeled binary \([7,3]\) code expectations, its variance, or the exhaustive second-level equivalence classification. Searches and full-text comparisons found no statement covering those contributions. Original authors might possess unreported enumeration data, and unindexed equivalent calculations remain a risk.

## Value

**PASS.** This is the full code-design performance distribution for the natural seven-point binary projective plane and the foundational finite instance of the coverage-depth problem. A mean or optimum cannot show the frequency of unusually good or poor designs; the exact \(42\)-atom law and dispersion resolve this gap. The \(630\) second-level codes form a single geometric orbit, giving a complete robustness/equality classification instead of one sample witness. The result is finite and self-contained, not a claim of a general coding-rate improvement.

## Independent validation and limitations

The exhaustive finite computation is reproducible from the attached source, but no independent external audit has been conducted. All tests are exact; the result is specific to binary dimension three, length seven, full-message recovery and uniform replacement sampling.

Self-review: passed. Independent audit: not yet performed.
