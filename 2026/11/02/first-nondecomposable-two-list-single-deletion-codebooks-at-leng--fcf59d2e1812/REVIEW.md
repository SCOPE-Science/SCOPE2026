# Scientific review of the finite two-list one-deletion capacity result

## Correctness

**PASS.** For each length \(1\leq n\leq7\), a complete explicit witness has been checked against all distinct one-deletion outputs. Exact rational dual bounds certify all seven optima: a one-leaf upper certificate for each of the first six lengths and a 101-node exhaustive binary-decision tree for length seven. A second 25-node rational tree establishes the unique-decoding capacity \(16\) at length seven. The central inequality follows directly from nonnegative weighted residual capacities and unit upper bounds on each unfixed codeword indicator. `verify.py` checks the inequalities using exact `Fraction` arithmetic, not floating-point solver results. No infinite proof is inferred from finite experiments.

## Originality

**PASS, with publication-priority uncertainty.** The closest relevant full text is Lin's *Lower Bounds for all List-Decodable Deletion Codes* (arXiv:2609.26650v1), whose single-deletion analysis uses a union of VT syndrome classes to obtain asymptotic guarantees, not an exact seven-bit optimum or nondecomposability result. No (2019) treats one-list unique decoding, while Song, Cai and Nguyen (2022) treat two-list decoding under the strictly more demanding deletion-plus-substitution channel. Actual indexed mathematical-claim searches for the exact number, seven-bit capacity and two-class decomposability returned different error models or deletion counts, with no exact covering claim identified. The conclusion is best-knowledge originality, not a proof that no unindexed result exists.

## Value

**PASS.** The theorem exposes a sharp structural failure of decomposable optimum two-list deletion decoding. At every smaller positive length, the best code can be formed as the union of two uniquely decodable VT classes. At length seven, the exact capacity exceeds **twice** the unique-decoding capacity. This distinguishes genuine list-decoding packing gains from merely combining standard syndrome classes, provides a reproducible exact benchmark for deletion hypergraphs, and gives a natural boundary phenomenon in a currently active coding-theoretic model.

## Sources and residual limitations

Relevant directly inspected sources: Lin (2026), arXiv:2609.26650v1; No (2019), DOI 10.3390/e21121202; Song, Cai and Nguyen (2022), arXiv:2201.02013v2. The public mathematical-results index was searched for alternative terminology and stronger exact claims. Residual risks are older or unindexed enumerations and the possibility of an equivalent short-block assertion embedded in uninspected sources. The claim is strictly finite and makes no extrapolation to larger blocklengths.

Self-review: passed. Independent audit: not yet performed.
