# Review

## Correctness
PASS. The claim is reduced exactly to a binary mismatch profile. The legal-start condition is a weight-one length-\(k\) window. Equality of parents from starts \(i<j\) is equivalent to a zero mismatch interval \([i+k,j+k-1]\). This yields a local packing lemma: at most two representatives of distinct parents can occur among \(k+1\) consecutive starts. The periodic mismatch construction meets that bound, and its realizability over any alphabet with at least two symbols is explicit. The bundled verifier checks the raw channel independently on thousands of received words and checks the witness family on a broad parameter grid.

## Originality
PASS with residual risk. The closest primary source is Tang–Farnoud’s noisy-duplication paper, which defines the same Hamming-distance-one copied-block operation and develops root-based error characterization and coding. Relevant full-text portions and the conclusion were inspected, together with targeted searches for inverse-ball aliases; no theorem counting distinct one-step parents was located. Exact tandem-duplication sphere work by Lenz–Wachter-Zeh–Yaakobi was compared at the statement level: its adjacent blocks must agree, whereas the present inverse event is a weight-one mismatch window, so its sphere formulas do not imply this law. Published-result searches under parent, preimage, inverse-ball, list-size, ambiguity, and mismatch-profile aliases returned no matching claim. A negative search is not a novelty proof, so an unindexed or differently phrased derivation remains a stated risk.

## Value
PASS. The maximum received-word inverse degree is the sharp worst-case list ambiguity of the one-noisy-duplication channel. It is a natural channel invariant directly tied to unique/list decoding and sphere-packing viewpoints, and the formula resolves all alphabet sizes, duplication lengths, and parent lengths rather than an isolated finite instance.

Same-model review: passed. Independent audit: not yet performed.
