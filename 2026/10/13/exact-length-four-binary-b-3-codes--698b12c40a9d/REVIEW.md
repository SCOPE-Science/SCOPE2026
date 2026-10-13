# Review: Exact length-four binary \(B_3\)-codes

## Correctness
PASS. The claim is a finite exhaustive statement. The verifier checks the defining multiset-sum injectivity in two independent encodings, accepts exactly 656 of the 8008 six-subsets, rejects every one of the 11440 seven-subsets, and uses heredity to exclude larger codes. It then partitions the 656 maxima under all 384 Hamming isometries into six exact orbits of sizes \(16,64,96,96,192,192\), whose sizes sum to 656. The orbit sizes give stabilizer orders \(24,6,4,4,2,2\).

## Originality
PASS. Direct comparisons were made with the original binary-column \(B_s\)-code formulation of D’yachkov–Rykov, Derksen's \(B_h\)-sequence construction paper, and Gu's modern shared-codebook adder formulation. Those sources define or bound the general objects but do not imply the finite upper bound, labeled count, or equality-orbit classification. Literature-index searches covered the source title, \(B_3\)/\(B_h\) aliases, shared-codebook adder terminology, the equivalent parameter notation \(N(3,6)\), and the numerical count 656. The closest returned records were on other coding problems rather than this finite parameter. A residual risk remains that an obscure historical finite table contains the maximum value, but no decisive unresolved source was found and no checked source covers the combined equality classification.

## Value
PASS. Binary \(B_h\)-codes are a standard additive-coding object and model zero-error decoding when three users share one codebook in a noiseless integer adder channel. An exact smallest-scale higher-order benchmark that includes all symmetry types is useful for testing constructions and computational searches. The equality layer is nontrivial: 656 labeled maxima split into six inequivalent Hamming-isometry classes rather than one routine construction.

## Closest literature and limitations
Derksen's arXiv:math/0311385v1 supplies the archive literature lead and the standard \(B_h\) additive-uniqueness definition, but its tables concern Hamming-code bounds. D’yachkov–Rykov (1981) treats the equivalent binary-column multiple-access model and asymptotic length bounds. Gu, arXiv:1809.07364v1, gives the modern exact \(B_h\)-code definition and surveys rate results. The new statement is only finite at block length four, and literature search cannot exclude an obscure poorly indexed historical enumeration.

Self-review: passed. Independent audit: not yet performed.
