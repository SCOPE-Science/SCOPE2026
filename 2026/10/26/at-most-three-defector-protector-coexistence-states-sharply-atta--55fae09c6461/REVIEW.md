# Self-review

**Correctness — PASS.** Direct group-level payoffs reproduce the exact jump-form Bernstein coefficients. Positive-real-root Descartes counting limits the nonendpoint defector–protector equilibria to three, and the one-downturn derivative pattern limits attracting edge equilibria to one. An explicit four-player polynomial has three simple real roots in disjoint rational intervals and its middle root has negative transverse invasion growth. The included `verify.py` performs 2169 exact-arithmetic checks against raw payoff enumeration. Exhaustive checks are corroboration, not infinite proof.

**Originality — PASS, qualified.** Li et al. (arXiv:2609.28132, 2026) define the same collective-risk public-goods game and analyze a boundary saddle-node. Archetti (Games 9(2):17, 2018) establishes the Bernstein variation theorem used as a tool here. The inspected works did not yield the explicit model coefficient pattern, universal sharp three-root bound, at-most-one-attractor property, or a four-player sharp witness. An earlier exact pivotal-risk gain analysis gives \(P_S-P_C\), not the number and type of zeros of \(P_S-P_D\). Unindexed equivalence or a differently formulated prior implication remains an originality risk.

**Value — PASS.** The original equilibrium polynomial degree grows with group size, whereas the proven count stays at three. The attaining four-player example and uniqueness of locally stable protective coexistence provide useful global structure for interpreting the model's bifurcation diagrams, independently of particular numerical parameter scans.

Scientific limits: only the defector–protector invariant edge is globally classified; no full-simplex basin characterization, interior three-strategy count, or finite-population conclusion follows. The general Bernstein technique is prior art and is explicitly credited. Independent technical and publication-priority audits have not been performed.

Self-review: passed. Independent audit: not yet performed.
