# Self-review

## Correctness

PASS. A dual repair check is exactly \((St,t)\); the commuting cube-flip operators give \(S^2=I\) at odd rank and \(S^2=0\) at even rank. Dot-product parity excludes two disjoint information-coordinate repairs in all ranks and any two repairs in the odd case. At even rank, two disjoint parity repairs are explicit. Equality of kernel and image, self-orthogonality, and distinct hypercube neighborhood columns yield the general packing bound without invoking any unverified asymptotic minimum-distance claim. The dimension-four exact packing is established by three explicit checked words and the sharp bound. An independent standard-library computation exhausts all 255 nonzero checks at rank four, verifies locality and the exact packing counts, and returns `VERIFY_OK`.

## Originality

PASS, with residual risk. The 2026 source arXiv:2610.03746 was examined in full, including construction and its main coding-theory section, and does not give disjoint repair availability. The much older paper by Fish–Key–Mwambene (2011) studies the same reflexive-cube matrix and self-dual graph-code phenomena; these ingredients are credited, not presented as new. Its full text remained inaccessible, so a previously published equivalent repair formulation cannot be completely excluded. Searches for parity-helper availability and closed-neighborhood code repair, together with published mathematical-record comparisons, returned no covering claim. No uniqueness inference is made from an unsuccessful search.

## Value

PASS. The parity of the recursion rank creates a persistent difference between information-symbol and parity-symbol multiple-recovery tolerance in an infinite, explicitly encoded code family. This is a structural storage-reliability invariant not supplied by length, dimension, minimum distance, or self-duality alone. The rank-four case supplies a nontrivial sharp three-set boundary, not simply two visible rows of the parity-check matrix. No unproved exact availability is asserted for larger even ranks.

## Limitations

The statement is about linear single-symbol recovery using helper sets of unrestricted cardinality. At even rank at least six the stated upper bound is not claimed sharp. An inaccessible plausible 2011 primary article and the possibility of an equivalent older repair formulation remain originality risks. Finite verification is a stress test, not an infinite proof.

Self-review: passed. Independent audit: not yet performed.
