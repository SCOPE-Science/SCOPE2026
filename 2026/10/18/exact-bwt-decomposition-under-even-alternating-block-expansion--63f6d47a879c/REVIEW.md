# Scientific review

## Correctness — PASS
The proof identifies the first double-letter defect of a rotation at its exact distance, orders odd- and even-defect phases lexicographically, derives every BWT block, and proves strict positivity of the monochromatic separator lengths. The endpoint case and the strict threshold at \(h=2\) were checked. The full-block formula and equal-run statements were checked with distinct BWT constructions, but the infinite result uses the symbolic proof rather than a finite computation.

## Originality — PASS against examined sources
The inspected 2019 treatment gives explicit BWTs of particular morphic iterates, not arbitrary binary parent words; the 2023 result concerns a distinct Thue–Morse-like morphism family with a fixed additive run increment; and the 2025 sensitivity results bound or classify morphism effects but do not imply an exact cross-exponent BWT identity. Related research-record searches and accessible claims were compared for stronger equivalent statements, without a match. Remaining risk: an earlier unindexed or differently stated all-input formula could imply this result.

## Mathematical value — PASS
This is a complete all-input, all-exponent structural BWT transformation rule, not a sample count. It demonstrates exact parameter rigidity in a natural uniform alternating morphism family while the input-dependent run increment relative to the parent varies. The ordered decomposition may allow transfer of BWT-run characteristics without sorting the full expanded string. BWT run count is a motivated invariant of text indexing and compression.

## Sources and scientific limitations
The main full-text comparisons are the 2019 BWT-morphisms treatment; Fici–Romana–Sciortino–Urbina (2023), DOI:10.4230/LIPIcs.CPM.2023.10; and Fici et al. (2025), DOI:10.4230/LIPIcs.MFCS.2025.49. The contextual historical public source is arXiv:1510.06257 (2015-10-21). No claim is made for single-symbol parents, \(h=1\), or endmarked BWTs. The finite checks do not establish literature uniqueness or replace the proof.

Self-review: passed. Independent audit: not yet performed.
