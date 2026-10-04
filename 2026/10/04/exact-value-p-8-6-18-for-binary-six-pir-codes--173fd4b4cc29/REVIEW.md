# Same-model review

## Correctness
PASS. The proof reduces a hypothetical length-\(17\) six-PIR code to the unique binary \([17,8,6]\) equivalence class. For an explicit cyclic representative, `verify.py` checks rank, primal and dual distances, the complete dual weight-\(5\) support list, and the pair-incidence maximum. The combinatorial implication from six disjoint equal-syndrome recovery sets to five weight-\(5\) dual supports through one pair is explicit and basis-invariant. The published length-\(18\) construction supplies the matching upper bound.

The main correctness dependency not reconstructed from scratch is the published uniqueness classification of binary \([17,8,6]\) codes. The verifier checks the representative and the obstruction, not the classification algorithm.

## Originality
PASS. The direct PIR source leaves the parameter at \(17\le P(8,6)\le18\). Searches using the native notation, minimum-block-length language, six-disjoint-recovery language, the \([17,8,6]\) code, the quadratic-residue representative, and unique-code obstruction language found no prior exact statement. The closest code-classification source provides uniqueness but not the PIR implication.

Residual risk remains that an unindexed note, thesis, or unpublished computation contains the same one-unit closure.

## Value
PASS. This is the exact closure of a published small-parameter gap in the main invariant \(P(s,k)\), not a routine continuation of a table. The proof also isolates a reusable obstruction: under the forced size pattern, the relevant dual weight-\(5\) supports would need excessive common pair incidence.

Same-model review: passed. Independent audit: not yet performed.
