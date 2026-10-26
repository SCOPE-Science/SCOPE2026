# Self-review

## Correctness
PASS. The proof independently derives the wall-interchange action, shows every complete-sweep wall permutation has two cycles, and tracks the single reference bit. The two equations for wall periodicity and fiber return yield the exact binary rank count, and Möbius inversion counts primitive cycles. The global order is minimal because the wall action is faithful on even-parity vectors for at least three sites. Reconstructed boundary cases include a one-element wall cycle, even and odd ring sizes, and possible rank-zero matrices. Exact finite calculations provide corroboration but are not substitutes for these unrestricted arguments.

## Originality
PASS with the bounded literature evidence listed below. Defant's Theorem 4.1 already gives the **identity-sweep** periodic-point census and must not be considered new. Macauley–McCammond–Mortveit derive a Rule-150 dynamics group and gap-permutation action; Macauley–Mortveit give update-order cycle-equivalence bounds. Those are essential antecedents, not exact arbitrary-schedule cycle census formulas. The new statement determines fixed points of every power for every permutation update order from a two-by-two rank, covering distinct non-identity schedules. Relevant searches also compared other parity cellular automata and reversible Rule-150 Floquet systems. Historical priority remains subject to independent assessment, particularly against general affine Coxeter-element classification.

## Value
PASS. The problem is naturally posed by update-order dependence in sequential dynamical systems. The result supplies a complete, explicitly computable phase-space invariant for all schedules rather than a routine case extension; orders on a six-site ring realize global periods \(3\), \(5\), and \(8\). It is motivated both by the earlier identity-order formula and the theoretical bound on inequivalent update schedules.

## Closest literature and limitations
See Defant, arXiv:1511.06966, Theorem 4.1 (identity schedule); Macauley–McCammond–Mortveit, doi:10.1007/s10801-010-0231-y, Theorem 5.4 (group action); Macauley–Mortveit, arXiv:0802.4412, Section 5 (equivalence classes); and Macauley–McCammond–Mortveit, arXiv:0707.2360 (periodic-set independence). The result concerns one visit per site on finite rings only; it does not prove historical priority beyond the inspected sources or cover arbitrary update words. The verifier executes exactly reproducible finite tests. Independent review is outstanding.

Self-review: passed. Independent audit: not yet performed.
