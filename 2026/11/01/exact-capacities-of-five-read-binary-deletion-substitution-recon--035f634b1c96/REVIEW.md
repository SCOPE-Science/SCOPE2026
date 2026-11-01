# Self-review

**Correctness: PASS.** The distinct-output channel definition agrees with the original one-deletion/at-most-one-substitution model. The proof reduces maximum reconstruction-code cardinality to a graph clique number and provides a complete, finite, rigorously pruned branch enumeration. The `verify.py` artifact, run from its actual path, checks every channel ball independently by a second method, confirms every listed lower-bound witness, and exhaustively certifies all seven upper bounds. The nine-bit case has 512 vertices and a reproducible complete search. The coloring-bound pruning is mathematically sound; no probabilistic or partial search is presented as proof.

**Originality: PASS with residual priority uncertainty.** Targeted comparisons against arXiv:2604.25294, arXiv:2505.04232, arXiv:2501.03833 and the accessible published exact-code-size index did not identify this seven-term five-read capacity profile. The latest source provides asymptotic constructions at five reads, not exact finite maxima. The closest indexed exact one-deletion/one-substitution result concerns one-read correction rather than a five-read reconstruction code, so its smaller feasible-code domain cannot determine the present maximum. The complete primary comparison is limited to relevant material in the published sources; unpublished or unindexed exact tables remain a genuine priority risk.

**Value: PASS.** The exact capacity of a fixed-read reconstruction channel is the natural optimization invariant underlying its coding problem. This first nontrivial finite profile provides an exact benchmark, includes a sharp length-nine optimum on all 512 candidate codewords, and exposes a nonmonotonic blocklength transition that is invisible in asymptotic redundancy bounds. It is a bounded exact classification, not merely a renamed theorem or an unsupported small numerical gain.

The finding is restricted to binary length \(3\) through \(9\) with exactly one deletion and at most one substitution. It does not settle general-length capacity or classify all maximizers.

Self-review: passed. Independent audit: not yet performed.
