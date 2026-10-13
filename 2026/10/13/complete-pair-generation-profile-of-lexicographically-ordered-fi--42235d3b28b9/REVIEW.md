# Scientific review

## Correctness — PASS
The binary-carry formula counts each cyclic transition exactly, including the closing pair. Prefix parity is an invertible change of variables. The positive place-value coefficients determine both the complete symbol-pair weight enumerator and the rank of the generated subspace at every integer threshold; Cayley graph components are precisely its cosets. The independent finite replay in `verify_rm_pair.py` checks all words and all thresholds for \(2\le m\le8\). All-length correctness comes from the written algebraic proof, not finite extrapolation.

## Originality — PASS, residual access risk
The 2026 Singh–Singh paper introduces generic pair generation and protection thresholds, not an accessible exact formula for the naturally ordered Reed–Muller family. Pan–Ling–Liu–Chen's Reed–Muller result gives minimum \(b\)-symbol distances, which cannot imply the entire spectrum and the intermediate dimensions. Liang–Liu study equiweight codes and simplex constructions, not this non-equiweight truth-table family in the accessible description. Targeted index, equivalent-formulation, and table searches did not identify the theorem. Two important full articles remain uninspected; an unnoticed exact example or table would compromise originality.

## Value — PASS
Exact pair-generation phases on a canonical infinite family determine which low-pair-weight differences can connect codewords, giving complete component sizes and an exact \(n/4\) separation from the Hamming connectivity threshold. This is a protection-relevant graph invariant beyond minimum distance, not an arbitrary short-code census.

## Limits
Only binary first-order Reed–Muller codes in cyclic lexicographic coordinate order are covered. The result does not solve minimum redundancy for arbitrary functions, and it is not invariant under coordinate permutation. External independent audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
