# Independent mathematical audit

## correctness

PASS

For a fixed received word, the rightmost insertion representatives are the two appends and the insertion opposite to the symbol at each of the n−1 other positions, giving n+1 distinct parents. Deleting positions i and j from the same parent gives the same output only if entries i through j are constant; thus each parent's deletion set is an interval. The n edges each flip exactly the corresponding check coordinate and consecutive edges share a parent, so the edge syndromes recover the mask as the XOR of odd-parent intervals. Its 2r padded boundaries require at least r odd parents. For the proposed y the prescribed symbols do not conflict even with a single zero between support runs. The selected intervals reproduce those edge syndromes, and the actual syndrome of X_1 is r−1+Σ_j ℓ_j t_j=1 mod 2, ruling out global complement. For a single even run one odd parent alone would have to be constant on the whole support and would in fact be even. The block of ℓ−2 ones gives exactly two odd parents, including the ℓ=2 case. Unique tiling by 0 and 11 gives F_{n+1}, including the zero mask. Read the frozen proof, checker and recorded output; independently tested all masks and outputs through n=8 by canonical rightmost insertions with `python /workspace/branches/review-computations/check_finite.py`. The finite run corroborates the all-length argument, and does not classify the exceptional masks.

## originality

PASS

The checked predecessor supplies a list cap for the alternating singleton-run family, not the run-sensitive result for arbitrary fixed hyperplanes. Credit that family as overlap; the new content is the all-mask interval-XOR bound and its stated sharpness regimes and prevalence. No stronger covering result was verified.

## value

PASS

Worst-case distinct-parent ambiguity is a receiver-relevant invariant of the highest-rate proper binary linear codes. The result explains structurally why coordinate geometry, not just the number of parity checks or the Hamming distance, controls this ambiguity, and gives attainable values for exponentially nearly all masks without a length cutoff. The unresolved regime is expressly delimited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
