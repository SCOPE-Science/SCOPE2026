# Self-review

**Correctness — PASS.** For an upset \(U\), the defining algebraic equations give \(F(U)=\uparrow\downarrow U\), equal to one step in the common-lower-bound graph. On a shortest path of length \(k\) from \(U\), the initial \(k\) vertices are nonminimal and the \(k\) edges have pairwise distinct minimal common lower bounds. This proves \(2k\leq n\). The height-two fences attain equality and adjoining one isolated point handles odd sizes. The analytic argument covers every finite nonempty poset, beyond the explicitly checked cases.

**Originality — PASS within the inspected evidence.** Tasiou (2025, Definition 2.1) had already defined the least updownset/zigzag closure; it is credited, not claimed here. Badia–Kowalski–Olkhovikov (2026) treat broader expressivity and semantics; Stell–Worboys (1997) discuss the operations. Inspected relevant text and targeted searches did not uncover the sharp \(\lfloor n/2\rfloor\) convergence bound or the extremal height-two family. The remaining risk is an equivalent theorem phrased as a finite relation-powers or closure-iteration bound, which cannot be categorically ruled out.

**Mathematical value — PASS.** The sharp universal convergence index is a natural quantitative invariant of the canonical bi-Heyting saturation operation. It distinguishes poset height from formula-iteration depth: height-two frames realize unbounded indices. The minimum/nonminimum packing lemma yields a nontrivial factor-of-two improvement over generic monotone iteration bounds and has a concrete extremal classification witness; no stronger claim about all formulas is made.

**Verification and limits.** Separately implemented finite checks enumerate all naturally ordered transitively closed posets up to six elements and all their upsets, compare the algebraic and graph operations, and check 100 explicit fences. These are corroboration only. The historical-priority assessment is not independent and is limited to the inspected literature.

Self-review: passed. Independent audit: not yet performed.
