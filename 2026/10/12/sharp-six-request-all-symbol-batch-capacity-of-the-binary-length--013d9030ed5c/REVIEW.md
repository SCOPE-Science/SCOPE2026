# Scientific review

## Correctness — PASS
The seven-identical-demand upper bound follows from the all-ones leading generator row and distinct columns: six recovery sets avoiding the target need at least eighteen of fifteen available coordinates. The constructive lower bound rests on an exhaustive enumeration of all \(\binom{21}{6}=54{,}264\) six-demand multisets. For each, the checker finds and directly validates six pairwise disjoint legal recovery supports using the actual binary generator columns; this is a finite exhaustive witness proof, not a statistical sample. The packaged `verify.py` was replayed and returned `VERIFY_OK`.

## Originality — PASS
The closest sources are the original all-symbol framework (Boruchovsky et al., arXiv:2601.04041, Definition 2, Proposition 29 and final section) and the earlier four-request Reed–Muller batch construction (Baumbaugh et al., arXiv:1710.07386, Theorems 4.13–4.14). Neither establishes serving all six-request multisets using sixteen separate storage coordinates. The 2025 Ly–Soljanin decoding result concerns recovering message coefficients, not the sharp all-symbol six-request batch property. Prior nearby fixed-code recovery and same-family availability results do not imply mixed-demand batch feasibility. The search cannot exclude every unindexed equivalent result.

## Value — PASS
The sixteen-coordinate first-order Reed–Muller code is the first nontrivial even-dimensional instance in which single-symbol recovery reaches six disjoint copies. Showing that the same maximum survives *arbitrary mixed requests* resolves a natural exact batch-capacity question at this small classical code and improves on the older four-query guarantee. It distinguishes an all-symbol batch property from repeated-one-symbol availability without asserting a general-length theorem. The proof supplies a reusable exhaustive witness generator.

## Scientific limits and residual risk
The result is confined to \(\operatorname{RM}_2(1,4)\), and every lower-bound witness uses sets of cardinality one or three. Historical one-step majority-logic and batch-code formulations may contain an overlooked equivalent stronger theorem; a broad novelty search is not a proof of absence. The verifier is a self-review computational proof, not an independent audit.

Self-review: passed. Independent audit: not yet performed.
