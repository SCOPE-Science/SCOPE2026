# Independent Audit — 2026/09/15/020

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `b6a86079502017487f626586b44d95ca3eccd08f`
- Disposition: **PASSED**

## Correctness

**PASS** — The mod-n reduction is valid. On the full part, the F-classes inside each E-class are Z-indexed and the total predecessor shifts the index by -1. Grouping F-blocks by index modulo n defines a Borel subequivalence relation E_n of index exactly n; restricting the original lexicographic Z^2-order to E_n again has finite-interval relation F. Its immediate block-predecessor is exactly the n-step predecessor. Thus compatibility of < with the eta-corrected n-step derived order is self-compatibility for E_n (independent of the chosen predecessor section by the same Gao–Xiao Proposition 5.2 argument). Gao–Xiao Theorem 5.3 makes E_n hyperfinite, and the standard finite-index extension property for countable Borel equivalence relations makes E hyperfinite. The non-full part is already hyperfinite, completing the proof.

## Originality

**PASS** — Gao–Xiao prove the n=1 self-compatible theorem and exhibit in Remark 5.5 a particular non-self-compatible example whose second iterate is compatible. The located published/arXiv versions do not state the general finite-n theorem. The residue-class subrelation E_n turns that isolated phenomenon into a uniform result for every finite n.

## Scientific value

**PASS** — The result enlarges the class of hyperfinite-over-hyperfinite relations covered by the current self-compatibility method while preserving an elementary reduction to the established theorem. It does not solve the full Hyperfinite-over-Hyperfinite problem, but it gives a clean finite-iterate closure principle that can be reused when compatibility appears only after several predecessor steps.

## Sources

- An order analysis of hyperfinite Borel equivalence relations (Su Gao; Ming Xiao): https://arxiv.org/abs/2404.17516 — Theorem 5.3 proves self-compatible Z^2-orders hyperfinite; Proposition 5.2 controls predecessor-choice dependence; Remark 5.5 discusses a second-iterate compatible example.
- The structure of hyperfinite Borel equivalence relations (Randall Dougherty; Steve Jackson; Alexander S. Kechris): https://doi.org/10.1090/S0002-9947-1994-1149121-0 — Standard finite-index/finite-extension closure properties of hyperfinite countable Borel equivalence relations.

## Limitations

- The theorem uses the Section-5 eta-corrected interpretation of the n-step derived order; an arbitrary unrelated notion of gamma^n ordering would require separate formulation.
- This is only a finite-iterate sufficient criterion and does not settle the general Hyperfinite-over-Hyperfinite or Union problems.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence. Open-access/preprint sources were checked first; Oxford Download was not needed.
