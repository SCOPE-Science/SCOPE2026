# Review

## Correctness

PASS. Under the common constant-subgradient premise, the two published dual-averaging recurrences reduce to closed forms. D-Adaptation yields \(R_n\), Prodigy yields \(P_n\), and exact rational square-root enclosures certify the strict cutoff inequalities. The common condition \(D>d_0\sqrt8\) guarantees that the gradients used in both calculations genuinely come from one fixed convex Lipschitz objective.

Risk: only the pre-activation phase and the first strict growth index are classified.

## Originality

PASS. The D-Adaptation paper gives the learned-distance recurrence, while Prodigy explicitly modifies it for faster adaptation and proves improved rate dependence. The inspected full texts do not state the exact constant-subgradient first-growth indices \(8\) and \(5\). Focused published-record searches found no implication-equivalent cutoff theorem.

Residual risk: an equivalent short calculation may occur in unindexed implementation notes.

## Value

PASS. Distance-estimate growth is the mechanism by which these methods escape a conservative initialization. An exact startup latency directly measures that mechanism, and the three-update reduction supplies a concrete finite-time explanation for Prodigy's faster-adaptation motivation without overclaiming a universal convergence advantage.

Same-model review: passed. Independent audit: not yet performed.
