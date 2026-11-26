# Independent mathematical audit

## correctness

PASS

PASS applies to repairs/5/RESULT.md, not to the frozen iid equivalent. The frozen second-moment diagonal numerator and its residue are false: the bivariate numerator specializes to (1−z)(4−2z−2z²+2z³), and its denominator to (1−z)P₂. The frozen reduction implies a z coefficient of 6, but both length-one sources have S=1, so the sum of S² is 2. The corrected numerator is 2(2−z−z²+z³), giving C₂≈2.217430020 and CV prefactor ≈1.073150221, with the same base ≈1.021673846. The repaired proof rederives the bivariate laws: a shortest absent target has exactly one greedy consumption per complete binary arch and a missing terminal letter in the remainder. For the second moment, both ordered targets must satisfy this constraint using the same arch; writing u=xy and L₀=xy/(1−y), L₁=xy/(1−x), the three pair-state equations sum to F₂=[(1−y)^−1+(1−x)^−1+2(1−u)]/[(1−u)(1−2u)−L₀−L₁]. The one-target equations likewise give F₁. They cover the empty and unary cases with a fixed ambient alphabet. After diagonalization, the two-state transfer has determinant P₂/(1−z) and positive Perron crossing of one at r₂. At other points of the same modulus, strict triangle inequality in an entry with consecutive powers plus Perron comparison gives spectral radius below one. The same scalar argument gives the first-moment pole. Both residues are positive, and 0.406866<2(0.460811)² ensures the squared mean is exponentially negligible. Independent direct enumeration of subsequence sets for all 1024 length-ten sources and rational-coefficient comparison across all 11 weights gave A_{5,5}=1110 and B_{5,5}=10174; rational endpoint-sign checks verified the pole brackets and the numerical residue recalculation was checked against the corrected numerator. The exact bivariate and diagonal transfer calculations in the repair give a replay without depending on finite testing. The frozen checker's bracket checks do not test the false numerator or residues.

## originality

PASS

For the repaired finding, originality rests on composition-marked moment aggregation, especially the exact second-moment law and its iid relative-variance consequence, not on the single-word SAS characterization, the length-only first moment, or correcting a sign in isolation. The strongest matched exact second-moment result has a restricted source ensemble that does not cover this law.

## value

PASS

The corrected result gives exact compositional variance for a natural, established word statistic where extremal counts and the known summed mean do not quantify typical fluctuations. The second moment uses a common-source ordered-pair count and reveals exponential growth of the relative mean-square deviation in the unrestricted random-source model, something the first moment does not determine. The correction preserves this substantive invariant and gives the right quantitative constants rather than only restating an asymptotic base.

The dated certificate retains the supplied scientific assessment, sources and limitations.
