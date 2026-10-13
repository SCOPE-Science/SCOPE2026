# Review of The exact first-crossing threshold in Gubarev's binary-tree graph

## Correctness
PASS. The source's proof of Lemma 5.2 gives the universal upper bound \(2L_{2n-2}\) on a crossing-free path. The matching construction is explicit: inside a height-\(2n\) subtree, omit the two boundary grid gaps and replace each bottom cutoff vertex by its \(a\)-jump. This yields exactly \(2L_{2n-2}\) edges while visiting only the single interior grid height. The Section 6 decomposition then applies with the exact threshold because its exponent hypothesis is used to force a first crossing. The finite verifier agrees for all tested values.

## Originality
PASS. The source states the coarser threshold \(2^{2n+1}\) and contains the upper estimate \(2L_{2n-2}\) inside its proof, but it does not supply an attaining family or claim exactness. Targeted searches for the exact threshold, the crossing-free maximum, and the sharpened exponent found no matching prior statement. The strengthened nilpotency bound alone is a consequence of the source's hidden upper estimate; the original contribution assessed here is the matching lower construction and resulting exact threshold.

## Value
PASS. The crossing threshold is the central combinatorial cutoff that drives the paper's nilpotency mechanism. Determining it exactly is a natural structural boundary rather than an arbitrary parameter slice, and it uniformly reduces the exponent used in the construction by asymptotic factor \(3/4\). It also identifies the precise amount of slack in the first-crossing step, while clearly separating that improvement from the unchanged compression estimate.

## Closest literature and limitations
The closest source is arXiv:2610.05384v1 itself: its Lemma 5.2 proof contains the upper bound but not the matching lower path, and Theorem 6.2 uses a larger round-number exponent. Smoktunowicz's earlier simple-nil-ring construction is historical background and does not supply this binary-tree crossing invariant. Residual risk is that a later revision or independent very recent note may record the same sharpening. The nilpotency exponent \(E_n\) is not claimed to be optimal in every representation.

Self-review: passed. Independent audit: not yet performed.
