# Self-review

## Correctness — PASS

The unconditional \(m\le2n\) EF1 protection follows analytically from the first-pick deviation bound and the two-pick limit: after deleting one good from any other player's bundle, at most one available-at-first-pick good remains. This argument does not assume additivity, strict preference, or particular off-path continuation behavior. For the seven-good upper witness, the displayed backwards-induction recurrence is both necessary and sufficient: after alternative moves, assign the minimum-payoff SPNE continuation while preserving the chosen equilibrium outcome. The exact verifier reproduces all 128 remaining-subset states, all two root SPNE outcomes, and independently checks an explicit strategy construction at 13,700 nodes. The counterexample's B-to-A EF1 deficit is exactly 69. Finite verification certifies only the finite witness; the uniform lower bound has its separate proof.

## Originality — PASS, with remaining priority risk

Goldberg–Hollender–Tyrovolas (arXiv:2609.18309v1, §4, Theorem 17 and proof) establish existence of three-agent online unfair SPNE outcomes through a **nine-good, uniquely unfair** example. Their two-agent theorem and general PROP1 theorem do not cover a universal two-round EF1 horizon, and the nine-good construction does not establish its sharp minimum for existence. Amanatidis et al. (arXiv:2610.23686v1, §§2–3, Proposition 1) give an eight-good unfair PNE for a simultaneous-report mechanism, not an SPNE of the sequential extensive-form mechanism. Targeted primary-literature and research-record searches for seven-good sequential SPNE examples, two-round safety, equivalences and tighter bounds did not locate the claimed result. The finite-instance combinatorial threshold may have been worked out elsewhere, including in unindexed work, so independent priority review remains appropriate.

## Value — PASS

The result settles the natural first-failure size after two complete sequential draft rounds for three players, and identifies a broad monotone-valuation safety region without additive restrictions. The explicit strictly positive, strict-bundle-preference example is smaller than the nine-good sequential example and is accompanied by a complete decision-tree equilibrium witness. It does not claim universal seven-good failure: the existential nature of the boundary is essential to its interpretation.

## Scientific limitations

A different nine-good theorem proves an all-equilibria failure at its example; no such claim is made here. This mathematical review is not independent validation, and no claim of publication or external certification is implied.

Self-review: passed. Independent audit: not yet performed.
