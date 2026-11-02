# Scientific review: two-scale cherry/depth dependence

## Correctness — PASS

For every possible tree, the leaf-split updates of cherry count, total tip depth, and cherry-tip depth sum are verified by direct deletion/insertion bookkeeping. The exact conditional recurrences for the three first moments and the mixed cherry-count/depth moment imply the two-scale formulas by induction. The boundary cases are explicit: size two has no non-cherry tip, and size three has deterministic cherry count. A standalone exact-arithmetic verifier enumerated 46,233 size-indexed growth histories and checked 873 single-step transitions; the proof does not extrapolate from finite cases. The remaining mathematical risk is only undetected transcription of an algebraic step, mitigated by the separate transition checks and recurrence substitution.

## Originality — PASS, qualified

Searches compared exact statements, not paper names. McKenzie and Steel give the Yule cherry marginal law. Mir–Rosselló–Rotger give the Sackin expectation and balance-index analysis, not a mixed cherry/depth moment. Wu–Choi treat cherries jointly with pitchforks, not Sackin depth. Coronado–Mir–Rosselló–Rotger derive different Sackin/cophenetic covariance formulas; Plazzotta and colleagues report correlations in other branching-process simulations. Relevant complete primary texts and sections were inspected where available. Public mathematical-record searches for cherry/Sackin mixed moments, local cherry membership/depth, and the exact constants returned no matching stronger published statement among the nearest records. Failed searches are not a proof of priority, and older multivariate enumeration and tree-index literature remains a historical-overlap risk.

## Mathematical value — PASS

Cherry count is an established local tree-shape statistic and Sackin depth an established global imbalance statistic. A sign reversal occurs when moving between individual sampled leaves and whole-tree covariance: a cherry leaf is one edge deeper in conditional expectation, yet trees with more cherries have shorter aggregate path length in covariance. The fixed local excess and exact all-size global formula supply a baseline dependence structure for interpreting combined phylogenetic shape statistics; they are not merely a renaming of a marginal result. The value claimed is that precise structural comparison, not an unsupported downstream test improvement.

## Closest literature and limits

The closest comparable full texts are McKenzie–Steel (cherry distribution), Mir–Rosselló–Rotger (Sackin/phylogenetic balance), and Wu–Choi (cherry/pitchfork joint law). The finding uses the leaf-splitting Yule law with unit topological edge depths, with no extension to evolutionary time or non-Yule models. Equivalence hidden in older tree-generating-function literature remains possible, and independent expert assessment is still needed for publication priority.

Self-review: passed. Independent audit: not yet performed.
