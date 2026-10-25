# Scientific review

## Correctness — PASS
The update matches the original 2023 algorithm's growth and curvature-cap branches, not its 2024 parameterized revision. For a scalar quadratic, the local secant quotients are identically the positive curvature, provided the point iterates never coincide. The exact roots and branch inequalities give strict prime periods two and three; their steps avoid one, so the reduction never degenerates. Jacobian chain products have one zero eigenvalue and one certified eigenvalue below minus one, while direct multiplication yields a positive period contraction below one for the primal iterates. The embedded exact-rational interval verifier replays the critical root bounds, inequalities and multipliers; the proof supplies the global-in-time induction.

## Originality — PASS, with remaining priority risk
The 2023 source reports seemingly cyclic step magnitudes and expressly leaves their rigorous characterization open (Algorithm 2.1 and Section 4.3), but provides no exact prime-three orbit or Jacobian certificate. The 2024 generalized AdaPG analysis has a different curvature-cap constant and establishes convergence of optimization iterates, not this periodic map classification. The closest identified mathematical record, a plastic-constant period-two orbit of the 2025 B-adaPGα update, has a different recurrence and different exact initial steps; its results do not imply the growth/growth/cap prime-three orbit here. Targeted record, full-text and phrase searches did not identify covering formulas. Other unindexed specialized analyses may nevertheless contain them; absolute publication priority is not established.

## Value — PASS
Exact limit behavior of the automatically selected step sequence is a natural question expressly highlighted as open by the source, independently of the source's proven primal convergence. The simple strongly convex benchmark exhibits both two- and three-phase nonlinear feedback cycles and proves their repulsion, clarifying that observed quasi-cyclic transients need not come from attracting periodic states. This is a structural algorithmic counterexample/benchmark, not a tiny accuracy increment or an arbitrary data-table slice. It makes no unsupported claims about typical initializations.

Self-review: passed. Independent audit: not yet performed.
