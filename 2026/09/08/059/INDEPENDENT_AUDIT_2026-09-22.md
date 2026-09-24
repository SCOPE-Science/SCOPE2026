# Independent three-axis audit — 2026-09-24

Reviewer type: separate AI audit. This document records reproducible scientific checks and literature comparison, not a transcript of private reasoning.

## Audited source

- Record: `SCOPE-20260908-059`
- Source path: `2026/09/08/059`
- Inventory source tree: `113d2f521d1b2ca61ef80de39e8ebeabbdd99a15`
- Audited `RESULT.md` blob: `4efe0671e685f5efdf1e724774236f38552a61ab`
- Claim audited: exact maximum ordered rainbow Schur-triple counts for all 3-colorings of `[n]`, `1<=n<=12`, including optimum counts/classes and comparison with the parity/interval template.

## Correctness — PASS

The finite census was recomputed independently from the definition. For each `n=1,...,12`, all colorings with the color of 1 fixed to 0 were exhaustively enumerated; this symmetry reduction is lossless for the maximum. Rainbow ordered triples `(x,y,z)` with `x+y=z` were counted directly. The recomputation gives

`R(1..12)=0,0,2,4,6,8,12,14,18,22,28,30`,

exactly as claimed. Recounting labelled optima gives

`3,9,6,6,12,12,6,24,30,6,6,66`,

and canonicalization under all six global color permutations gives respectively

`1,2,1,1,2,2,1,4,5,1,1,11`

color-permutation classes, again matching the record. Direct recount of the stated parity/interval template gives

`0,0,2,4,6,8,10,14,18,22,26,30`,

so the stated finite exceptions at `n=7` and `n=11` are correct.

## Originality — PASS, with corrected historical context

No checked source publishes this exact `n<=12` table, optimum multiplicities, or the complete color-permutation-class counts. Parczyk and Spiegel, **An Unsure Note on an Un-Schur Problem**, Electronic Journal of Combinatorics 33(1) (2026), #P1.45, DOI `10.37236/13554`, studies asymptotic bounds rather than an exact small-`n` census. The current follow-up by Hegde, Kumar and Pratibha, **A somewhat sure note on an un-Schur problem**, arXiv `2609.18474` (16 September 2026), improves the asymptotic bounds to `9/22` and `8/15` and states that a more detailed computation improves an asymptotic upper bound, but does not present the exact small-`n` table audited here.

There is, however, an earlier antecedent omitted by the record. A 4 January 2017 presentation by Thotsaporn Thanatipanonda, **On the Minimum Number of Monochromatic Generalized Schur Triples**, explicitly gives as its “Third Conjecture” the problem of maximizing rainbow solutions of `x+y=z` over 3-colorings of `[1,n]`, together with the same alternating parity/interval construction pattern and a conjectural count. Thus the record should not attribute the initial formulation or this construction solely to Parczyk–Spiegel. This does not cover the record's exact finite census, and the conjectural formula is not the exact table proved here.

Checked sources:
- https://doi.org/10.37236/13554
- https://arxiv.org/abs/2609.18474
- https://thotsaporn.com/GenSchur.pdf (2017 presentation, final slide)

Searches included exact value-prefix searches, `R(12)`/rainbow-Schur searches, construction terminology, and the September 2026 follow-up literature.

## Scientific value — FAIL

The surviving contribution is a correct and apparently unpublished brute-force census of only the first twelve values. Under the campaign's value standard, this finite computation is too narrow to stand as a validated scientific finding. It yields no structural formula, bound, proof technique, or reusable algorithm beyond exhaustive enumeration, and its principal conceptual comparison is with a construction already present in 2017 and subsequently superseded at the asymptotic level by the September 2026 `9/22` construction. The two small finite exceptions (`n=7,11`) are valid benchmark facts, but by themselves do not establish a meaningful new regime or substantial scientific advance.

## Repair attempt

A bounded repair was considered by narrowing the record to a benchmark dataset and explicitly crediting the 2017 antecedent. This improves historical accuracy but does not cure the value failure: the result remains an arbitrary small exhaustive table without a structural consequence or reusable improvement.

## Final disposition

**FAILED** on scientific value; correctness passes and the exact table is original relative to the literature checked. Scientific rejection evidence is published at the source record; archival relocation to the assigned failed-attempt path remains pending and does not affect the scientific verdict.
