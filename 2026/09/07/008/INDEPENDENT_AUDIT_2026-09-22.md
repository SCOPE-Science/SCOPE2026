# Independent audit — 2026-09-22

## Scope and source identity

Separate AI audit of `2026/09/07/008`, reviewed 2026-09-22 UTC. The audit began from repository commit `b491a8d1d4b639eb085a4c66fe4951ac3f344663` (after the separately published audit of record 001).

Source blobs: `RESULT.md` c6ca4132f1bda0831baaef1c3e2699e94c2277b0; `METADATA.json` 754b82c436341501abd78853dd51f143df7c70b5; prior `AUDIT.json` a6266bd2d77d183f1438ad83c9c04addac2c2573; prior `VERIFICATION.md` 83b03a7f246da30fad50fa39962dbb6d7f0519f0.

Reviewed claim: Up to independent row/column permutations and transpose there are 719 binary 5x5 ordinary-rank-3 classes: 713 have nonnegative rank 3 and six have nonnegative rank 4; none has nonnegative rank 5.

## Correctness — PASS

PASS. I independently enumerated all C(36,5)=376,992 column multisets. The exact rank histogram matches the record, with 63,015 rank-3 multisets. A separately written canonicalization under all 120 row permutations, column sorting and transpose produced exactly 719 classes; one representative of each was rechecked at exact SymPy rank 3. I then independently parsed and verified all 719 rational W·H factorizations entry-by-entry: 713 use rank 3 and six use rank 4. The six stored fooling-set witnesses were separately checked and give the matching rank-plus≥4 lower bounds. Therefore every class is certified 3 or 4 and none can have nonnegative rank 5.

## Originality — PASS relative to checked evidence

PASS relative to checked evidence. Rank-3/nonnegative-rank-4 binary examples based on the 4-cycle are classical, so the gap motif itself is not new. The checked literature did not contain the complete 5×5 binary rank-3 orbit census or the 713/6 classification.

## Scientific value — PASS

PASS. The complete small-entry classification with exact rational factors and lower-bound witnesses is a reusable finite benchmark; this remains useful after subtracting the classical 4-cycle example.

## Prior-art checks

1. Real and complex ranks with respect to nonnegative matrices — https://doi.org/10.1016/j.laa.2009.03.050 — Contains classical small rank/nonnegative-rank gap phenomena, not this census.
2. On the geometric interpretation of the nonnegative rank — https://doi.org/10.1016/j.laa.2012.06.038 — Rank-3 geometric theory, not the finite binary classification.
3. A Study of the Binary and Boolean Rank of Matrices with Small Constant Real Rank — https://arxiv.org/abs/2507.05824 — Related small-real-rank binary/Boolean classifications; reinforces that the cycle motif is prior art.

The originality verdict means no substantive covering result was found in the checked evidence; it does **not** establish or award scholarly priority.

## Residual risks / limitations

- The classification is computational, though all upper/lower certificates are exact and independently checked.
- No claim is made about ternary matrices or about a novel primitive gap construction.

## Final disposition

- Correctness: **PASS**
- Originality: **PASS relative to checked evidence**
- Scientific value: **PASS**
- Disposition: **passed**.
