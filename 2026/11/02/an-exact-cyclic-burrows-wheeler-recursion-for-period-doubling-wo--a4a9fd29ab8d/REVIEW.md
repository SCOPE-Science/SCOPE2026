# Scientific review: cyclic BWT under period doubling

## Correctness

**PASS.** The all-words transformation follows from a complete partition of rotations into the strict initial-prefix classes `000`, `001`, `01`, `1`. Predecessor bits and reversed order within the even-zero class establish the entire BWT formula. The fixed-point recurrence then has an explicit base case and a two-run increment. Cyclic boundaries, potentially tied rotations and the first exceptional iterate are treated explicitly. The independent direct and rank-doubling implementations agree over exhaustive small cyclic inputs; these tests support, but do not substitute for, the proof.

## Originality

**PASS, with residual literature risk.** The 2019 open manuscript focuses on Thue–Morse and Fibonacci-type substitutions rather than the period-doubling fixed-point BWT. The February 2022 arXiv manuscript establishes broad logarithmic-order bounds, including the uniform-morphism setting, but no exact four-block transform or period-doubling coefficient. The 2023 paper treats sensitivity of one morphism application to arbitrary inputs, even proving that its worst-case increase is unbounded; this does not entail the exact behavior of iterated images of a single symbol. The 2025 extension and 2026 survey maintain the distinct sensitivity focus. Related published research records on period-doubling string attractors and three-block lifts concern other invariants. Unindexed equivalent formulations remain possible.

## Mathematical value

**PASS.** The formula describes the full BWT rather than only its run count, over every circular \(11\)-avoiding binary word. The exact \(2m-2\) law pinpoints the leading logarithmic coefficient and lower-order constant for a canonical automatic word, relevant to the study of repetitiveness measures and BWT-based indexing. The derivation also supplies a compositional means to construct transforms without sorting exponentially many rotations.

## Limitations and closest results

The proof uses the unsentinelled cyclic BWT and the indicated ordered binary alphabet. It does not extend automatically to generic words or endmarker variants. The closest publications are arXiv:2202.02609 (general logarithmic morphic-word bounds), DOI:10.4230/LIPIcs.CPM.2023.10 (period-doubling one-step worst-case sensitivity), and DOI:10.4230/LIPIcs.MFCS.2025.49 (bounded-sensitivity characterization). The exact transformation was not found in the material inspected, which is not a guarantee of worldwide priority. The computational verifier checks only finite instances; the mathematical proof supplies the infinite quantifier.

Self-review: passed. Independent audit: not yet performed.
