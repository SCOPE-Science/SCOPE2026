# Scientific assessment

## Correctness: PASS

The gap-triple parameterization is a bijection for rotation-identified weight-three binary circles. Deleting a marker produces a two-marker necklace whose unordered gaps are determined by the deleted gap length up to complementation. Deleting a zero decrements precisely one positive gap. Comparing the two rotated decremented triples exhausts collisions: three equal gaps or two equal gaps with a third gap one shorter. Adding the disjoint two-marker and three-marker outputs yields the complete pointwise classification. Stars-and-bars, ordered-positive-distinct inclusion–exclusion, and Burnside counting give the stated distribution and its exact average and asymptotics. The standard-library checker enumerated all 3,055 source necklaces with zero counts from 0 to 36 and 450 additional larger cases, independently constructing and rotating every one-deletion output. All assertions passed. The finite checks do not replace the unrestricted combinatorial proof.

## Originality: PASS (best-knowledge)

Narayanan and Ren's *Circular Trace Reconstruction* (arXiv:2009.01346, posted 2020-09-02), Section 5 and Theorem 1.6, examines distinguishing full deletion-trace distributions, including some weight-three circular constructions. It does not provide the spectrum or histogram of distinct one-deletion necklace outputs; using the same circular model does not imply the gap-collision enumeration. Bar-Lev, Etzion and Yaakobi's *On Levenshtein Balls with Radius One* (arXiv:2103.01681) treats linear words and fixed-length insertion/deletion distance rather than exact one deletion modulo rotations. Ota and Manada's circular reconstruction work (DOI:10.1587/transfun.2023TAP0015) concerns contiguous substring profiles and minimal absent factors, a different observation. Available published research records and historical claim descriptions yielded no statement that contains the present fixed-three-marker one-deletion class distribution. The standard necklace orbit-count formula and simple marker-gap merge are excluded from the novelty claim. Residual risk: an independently derived identical enumeration may appear in unindexed circular-code literature.

## Mathematical value: PASS

This is a complete distribution for a natural infinite family of circular deletion-channel inputs, not a single ad hoc finite example. The sharp six-output threshold, exact classification of all exceptional collisions, and average degree asymptotics explain how sparse cyclic geometry controls reconstruction ambiguity. The result is relevant to fixed-weight cyclic sequencing and code-design ball calculations, but does not claim efficient decoding or general trace reconstruction.

## Limits and review status

The source alphabet is binary, exactly three ones are required, and rotation but not reflection is factored out. General weights, multiple deletions, and reconstruction probabilities remain open beyond this result. No independent audit or third-party confirmation has been conducted.

Self-review: passed. Independent audit: not yet performed.
