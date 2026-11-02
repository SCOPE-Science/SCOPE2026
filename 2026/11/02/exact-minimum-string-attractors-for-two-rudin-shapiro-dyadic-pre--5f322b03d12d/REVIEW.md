# Scientific review

## Correctness (C): PASS

Every substring of the two fixed binary words is explicitly generated; each possible occurrence contributes its entire positional interval to a distinct-factor mask. The witnesses hit all 7,008 and 28,128 distinct-factor masks. The lower-bound checker retains equivalent minimal masks (48 and 64) and performs an exact branching search that tests all smaller hitting sets, with safe dominance and memoized-state pruning. The recursive search terminates with no size-9 or size-10 solution. This is a complete finite proof of the two claimed values, not an extrapolation to larger lengths.

## Originality (O): PASS, with residual priority risk

The closest published record of this specific sequence reports exact dyadic optima only through length 64, plus upper witnesses of sizes 12 and 13 for the two lengths here; its accessible title and abstract do not imply either equality. The inspected 2025 primary paper develops suffix-automaton and greedy attractor methods and tabulates other sequences, without reporting these Rudin–Shapiro values. The inspected 2020 foundational paper gives general automatic-sequence theorems, not the two numeric optima. Targeted record searches for both numbers, dyadic aliases, and exact attractors did not identify a stronger prior result. An unindexed prior finite computation remains possible. The detailed original 2026 public record was not fully available in this check; the comparison is grounded in its published indexed summary and its stated bounds, not an assertion about all uninspected bytes.

## Value (V): PASS

Smallest attractor cardinality is a natural precise measure in lossless text compression, while computing it is NP-hard in general. The result settles the first two dyadic Rudin–Shapiro prefix lengths beyond the previously exact range and replaces two only-upper-bound instances by exact, independently reproducible finite optima, with compact exhaustive proof trees rather than solely solver claims. The claim intentionally does not imply a formula for all lengths.

Self-review: passed. Independent audit: not yet performed.
