# Independent three-axis audit — 2026-09-22

Review date (UTC): 2026-09-23. Reviewer: separate AI audit. Source tree: `32cc9313659389236d68244ef7780b88cd823186`, verified unchanged before review.

## Correctness

I independently transcribed the two displayed order-8 arrays and checked every row and column is a permutation of `0..7`. Brute force over all `8! = 40320` column permutations gives exactly 64 transversals for `K1` and 192 for `K2`. I independently checked every listed 8-cell block in each proposed partition: each block contains all rows, all columns, and all symbols exactly once, and the eight blocks are disjoint and cover all 64 cells. Hence the packing number is exactly 8, the absolute upper bound. Constructing the mate symbol from partition membership reproduces a Latin square and all 64 ordered `(K_i,M_i)` pairs are distinct, so both orthogonal-mate claims follow directly.

The standard induced-`K3,3` pattern test on the displayed arrays gives zero forbidden configurations, consistent with the two representatives used in the Brouwer–Wanless / Krotov–Krotov classification.

## Originality

I checked the Krotov–Krotov order-8 classification and the earlier Brouwer–Wanless discussion of the two universally noncommutative order-8 loops. The earlier paper records striking symmetry data (including autotopism groups of orders 64 and 192), but I found no reported transversal counts, disjoint-transversal packings, or orthogonal mates for the two representatives. General transversal and orthogonal-mate surveys likewise do not provide these two values. The numerical coincidence between the transversal counts and old autotopism-group orders is therefore not being mistaken for a published transversal result.

## Scientific value

The calculation answers a natural structural question about the complete order-8 `K3,3`-free classification: universal noncommutativity does not prevent orthogonal mates, and the two main classes are separated by their transversal counts. The explicit partitions and mates make the result immediately reusable without relying on an opaque solver.

## Disposition

**PASSED unchanged.**
