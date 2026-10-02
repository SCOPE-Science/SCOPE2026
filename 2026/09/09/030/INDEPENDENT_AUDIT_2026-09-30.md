# Scientific audit — 2026-09-30

## Final claim

For all 109 primitive three-move subtraction sets with maximum move at most 10, the committed table gives a closing-window-certified eventual preperiod and least period; an independent recomputation reproduced all 109 rows' headline statistics, including 99 purely periodic sets, maximum preperiod 21 for {2,8,9}, maximum period 45 for {3,7,10}, and the windowed Grundy-value distribution.

## Correctness — PASS

An independent mex dynamic program regenerated every primitive triple in {1,...,10}, scanned candidate periods through 200, reconstructed the least closing preperiod, and reproduced the 109-set count, 99 pure cases, unique max-preperiod row {2,8,9} with (21,11), unique period-45 row {3,7,10}, period-22 row {2,5,7}, maximum-Grundy histogram 6/45/58 for values 1/2/3, and the six binary-valued sets. The closing-window induction is valid because each next Grundy value depends only on the preceding max(S) values; the checked terminal agreement block therefore propagates indefinitely.

## Originality — PASS

The exact full bounded census was not located in Resultary or the primary literature searched. Manabe's 2026 paper gives pure-periodicity criteria and least-period results for substantial three-move classes, so parts of the 99 purely periodic rows are prior-covered; that overlap is explicitly acknowledged. The surviving claim is the complete max-move-10 census, including the ten impure cases, exact preperiods, and windowed witness/cold-count data, rather than novelty of every individual pure row.

The originality comparison explicitly checked equivalent formulations, broader coverage, exact databases/tables, and implication from prior results. See `INDEPENDENT_AUDIT_2026-09-30.json` for the structured searches, source inspections, checked sources, and residual risks.

## Scientific value — PASS

The move bound 10 is a small but natural complete calibration range for a classical eventual-periodicity problem. The table isolates all impure exceptions in that range, exact transition cutoffs, and extremal witnesses, providing a replayable benchmark against general periodicity criteria rather than a one-off arbitrary instance.

## Disposition

PASSED. This assessment records the mathematical status of the claim. It is not an external attestation or formal-proof certificate.
