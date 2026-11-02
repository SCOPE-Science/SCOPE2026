# Review of nine-read binary reconstruction capacities

## Correctness
**PASS.** The claim is fully finite and the graph reduction is an equivalence, not a heuristic. The channel uses one exact deletion and zero or one substitution with duplicate outputs removed. All \(480\) nontrivial output balls are crosschecked between independent representations. The four explicit codebooks attain the reported values; exhaustive maximum-clique enumeration with a proper greedy-color bound rules out all larger ones. The tiny lengths follow from an unconditional output-alphabet bound. `CHECKER.cpp` is the exact proof procedure and `OUTPUT.txt` is its replay result. The validity of color-based pruning and completeness of the branches were inspected separately from the outputs.

## Originality
**PASS within the checked literature, with residual priority risk.** The most relevant 2026 source proves an asymptotic nine-read construction for lengths at least ten, and the 2025 mixed-error papers supply pairwise bounds and other read-count constructions, not the unrestricted length-five-to-eight maxima. Published indexed results closest to the search concern conventional error correction, other read counts, or other deletion channels. The prior five-read finite-capacity sequence uses a strictly stronger code constraint and cannot imply the nine-read optimum. Actual searches, source sections and implication comparisons are recorded in `AUDIT.json`. Unindexed finite tables and independently performed computations cannot be excluded.

## Value
**PASS.** The fixed nine-read regime is singled out by current code-construction research. The complete initial capacity profile supplies optimal short-block benchmarks and reveals a first strict blocklength decline from \(26\) to \(24\), showing that the formal finite-length reconstruction capacity need not increase with length. This is a natural boundary and not a routine extension to one more blocklength of an already-known nine-read table.

## Limits
The result neither provides an infinite-length formula nor classifies all optimum codes; the coding condition itself is formal and may be satisfied by words with fewer than nine available distinct outputs.

Self-review: passed. Independent audit: not yet performed.
