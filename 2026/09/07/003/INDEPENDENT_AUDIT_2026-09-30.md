# Independent audit — 2026-09-30

## Final claim assessed

For diagonal-one J2-free binary square matrices, the exact minimum ranks for sizes two through five are respectively 2, 3, 3, and 4 with the stated minimizer counts and orbits; the four-cycle block construction gives the ceiling of three quarters of the dimension as a general upper bound, is optimal when every row has weight at most two, and the general lower bound of the ceiling of half the dimension holds through dimension eight.

## Correctness — PASS

Independent exhaustive enumeration of every off-diagonal completion for n=2,3,4,5 reproduced exactly the survivor/rank counts 3; 21; 311 with six rank-three; and 8995 with 390 rank-four, and reproduced one minimizer orbit for n=4 and five for n=5 with orbit sizes 120,120,60,60,30. The peeling lemmas are valid. The row-weight-at-most-two theorem reduces to functional digraph cycles, where odd cycles have full rank and even cycles lose one rank. The Frobenius-rank calculation for the n<=8 lower bound is algebraically consistent after transposed light-column peeling.

Evidence inspected:
- RESULT.md
- artifacts/enumerate.py
- artifacts/classify.py
- independent exact enumeration of all completions through n=5

Residual risks:
- The full ceil(3n/4) lower bound is explicitly only a conjecture; n=5 counts/classification are computational; the corrected minors file rather than the older mismatched pairing is the relevant artifact.

## Originality — PASS

The closest inspected literature studies Boolean rank/isolation, graph minrank with forbidden subgraphs, or Boolean/binary rank conditional on small real rank. Parnas-Shraibman already features the same 4-cycle circulant matrix at real rank three, so that particular construction is not new by itself, but their theorem does not state or imply the diagonal-one J2-free minimum-rank census, the n=5 classification, the all-n row-weight-two lower bound, or the n<=8 Frobenius bound. Published-record search found no duplicate package.

Sources inspected:
- Kovacs, arXiv:2206.04089
- Haviv, arXiv:1806.00638
- Parnas-Shraibman, arXiv:2507.05824 / Discrete Applied Mathematics 2026

Residual risks:
- The 4-cycle extremal block is a known matrix in adjacent rank literature; novelty attaches to the stated constrained-minimum results and classifications, not to the block itself.

## Scientific value — PASS

The problem is a natural real-rank extremum under a standard forbidden 2-by-2 configuration and diagonal normalization. It supplies exact first cases, a reusable tiling upper bound, a complete structural theorem for row weight two, and a nontrivial lower bound through n=8, while clearly separating the open conjecture.

Context checked:
- RESULT.md
- rank/forbidden-matrix literature above

Residual risks:
- The all-n conjecture remains open and the exact census is small-dimensional.

## Outcome

All three acceptance axes pass for the final claim as stated. Conjectures, heuristic search observations, and explicitly excluded broader regimes remain outside the accepted claim.
