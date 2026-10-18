# Scientific review

## Correctness — PASS
The proof determines both the feasible even-inversion code and a matching that saturates the opposite parity class in every fixed content component. The crucial involution swaps the first unequal pair in a predefined disjoint pairing, so it is genuinely involutive and content preserving. The only unmatched words consist of doubled adjacent symbols, optionally followed by a single unpaired symbol, and have even inversion parity. The exact fixed-point enumeration and total sum settle all integer parameters, including length one. An independently implemented maximum bipartite matching verifies all stated finite cases but is not used to claim an infinite proof.

## Originality — PASS, with priority risk
The 2023 asymmetric-deletion papers and 2023 q-ary mixed-edit construction treat correcting broader channels rather than optimal detection for only one adjacent swap. The 1998 Abdel-Ghaffar predecessor studies detecting substitutions together with transpositions, a distinct stronger condition; its accessible abstract does not imply the detection-only optimum. Complete text of the older paper was unavailable, so possible special-case overlap is a serious residual risk rather than a conclusively excluded source. The multiset inversion-parity enumerator is classical (DLMF §26.16), but matching-based channel optimality is an additional assertion. Several actual semantic research-record queries failed to locate an equivalent statement, which is evidence of a search, not a uniqueness proof.

## Mathematical value — PASS
The result solves a natural exact alphabet-size/blocklength coding-capacity problem and its constant-composition refinement, with a short proof providing a saturating matching certificate. Its use is strongest for channels that detect a changed valid word but do not promise unique recovery, including composition-constrained applications. It does not claim correction, multiple swaps, or novel inversion enumeration.

## Closest sources and limitations
Wang–Vu–Tan (arXiv:2301.11680, first released 2023-01-27); Khuat–Kim (doi:10.1109/OJCOMS.2023.3327435); Abdel-Ghaffar (doi:10.1093/comjnl/41.4.270, abstract inspected only); NIST DLMF §26.16. Novelty risk from uninspected older full text and unindexed equivalents remains. No independent review of this theorem has occurred.

Self-review: passed. Independent audit: not yet performed.
