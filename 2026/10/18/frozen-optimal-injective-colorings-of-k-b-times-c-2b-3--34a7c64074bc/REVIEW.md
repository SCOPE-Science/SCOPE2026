# Scientific review

## Correctness — PASS

The same-model reconstruction checks the common-neighbor graph of the direct product, the exact one-unit deficiency in the independent color supports, the bijection with missing cycle edges, the consecutive-spare recoloring criterion, and the three ways to distribute three extra gap units. The proof is uniform for every integer \(b\ge3\). Finite independent-support enumeration through \(b=8\), two independent palette-transfer counts, and literal common-neighbor tests corroborate rather than replace the proof. Reproduce the checks with `python3 verify.py`.

## Originality — PASS (best available evidence)

The closest full-text sources concern injective-coloring product inequalities (Samadi–Soltankhah–Yero), chromatic-polynomial calculations for four-clique rings (Dong–Royle–Wagner), homomorphism reconfiguration decision problems (Brewster and coauthors), and the fraction of frozen colorings at the different \((\Delta+1)\)-color threshold (Bonamy–Bousquet–Perarnau). None of their inspected theorems gives the new three-class recoloring-degree distribution on the named infinite family. In particular, evaluating a chromatic polynomial counts all colorings, not their vertex-recoloring neighborhoods. Search results and close claims were compared by implication, not merely by title. Residual risk: obscure or unpublished results on multicoloring reconfiguration might give an equivalent formulation.

## Value — PASS

The one-defect boundary between feasible color-class supports yields an exact characterization of all optimal injective-coloring local moves, rather than only an optimal color count. It determines which states are absorbing for single-site recoloring dynamics and exhibits an asymptotic frozen fraction approaching one at the optimal palette. This behavior lies outside the \((\Delta+1)\)-color setting studied in general rare-frozen-coloring results and provides a concrete, exact, structurally motivated comparison.

## Limits

This is a self-review, not an independent audit. Connected components beyond single-step degrees, larger palettes and the two excluded small clique orders are unresolved by this finding. Comparison with unindexed work cannot be complete.

Self-review: passed. Independent audit: not yet performed.
