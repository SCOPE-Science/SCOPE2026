# Same-model scientific review

## Correctness
**PASS.** The rank-one spectral reduction is exact, the Sherman--Morrison denominator is positive for every admissible parameter, and post-transfer regularity is not assumed implicitly: it is characterized by the displayed entrywise inverse condition. Under that condition the next-generation matrix is nonnegative rank one, so its sole nonzero eigenvalue is its spectral radius. The source-specific identity follows by reducing both threshold offsets to the numerator \(AD-B(C+D)\).

## Originality
**PASS.** The closest recent source on regular splittings proves threshold equivalence and explicitly notes nonuniqueness; the recent ALT-graph paper gives common-target rank reduction and two distinct same-threshold reproduction numbers; the earlier next-generation-matrix paper gives several alternative decompositions; and classical matrix-splitting comparison theorems give qualitative inequalities. The inspected statements do not imply the exact aligned-transfer law \(R_t-1=(R_0-1)/(1+ts)\), its inverse-positivity criterion, or the strict factor relating the two Johnston--Cupons formulas.

Residual risk remains that older numerical-linear-algebra literature contains the same rank-one identity under different splitting terminology. The Sherman--Morrison identity itself is standard; the claimed contribution is the exact regular-splitting deformation statement and its threshold interpretation.

## Value
**PASS.** Nonuniqueness of \((F,V)\) is explicitly identified in the motivating literature as a substantive issue, and the newer ALT-graph construction deliberately seeks common-target low-rank splittings. The theorem quantifies that natural regime exactly: it gives a computable admissibility condition, preserves the threshold side, orders the values, and measures the contraction toward \(1\). The concrete corollary resolves the relative placement of two published reproduction numbers without a parameter sample.

## Closest literature and limitations
The closest scientific sources are arXiv:2603.06778v4, arXiv:2610.01636v1, arXiv:2311.16686v2, and DOI:10.1155/2014/573024. The result does not apply to unaligned rank-one changes, arbitrary higher-rank splittings, or transfers that destroy inverse positivity. It does not assign a unique biological meaning to competing reproduction numbers.

Same-model review: passed. Independent audit: not yet performed.
