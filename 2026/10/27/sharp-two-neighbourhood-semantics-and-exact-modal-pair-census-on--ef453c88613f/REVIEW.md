# Mathematical review

## Correctness

**PASS.** The local interval lemma is obtained by taking extremal minimum and maximum elements of each nonempty neighbourhood; the exceptional cases for the empty family and a family containing the empty subset are treated separately. Every local pair is realized with zero, one or two neighbourhoods. Taking suffix minima gives the precise operations on every upset, so formula-depth preservation follows by structural induction. The converse profile classification uses a unique possible jump out of the diamond threshold \(-1\) and the necessary-and-sufficient adjacent box equality at that jump. Disjoint cases are counted by stars-and-bars and a hockey-stick identity. An explicit top-world pair forces a strict two-member lower bound. A standalone checker enumerates all raw small frames and modal formulas, as described in `VERIFICATION.md`.

## Originality

**PASS within the inspected material, with residual risk.** Dalmonte and de Groot (arXiv:2606.31870v1) supply the constructive-neighbourhood semantics, continuality and the logic. Dalmonte (arXiv:2210.09937v1) treats related persistent semantics, and de Groot (arXiv:2507.13746v1) studies another intuitionistic neighbourhood presentation. The inspected semantic sections and theorem statements do not provide a two-neighbourhood universal representative *together with* the exact paired-operation chain census. Nearby finite-chain published results address KI relations, birelational conditions or instantial arity, which neither imply the semantic quotient count nor the sharp two-member representation. No claim of exhaustive literature coverage is made; older representation-theoretic formulations remain a priority risk.

## Value

**PASS.** This is a complete semantic-equivalence classification for a natural finite-model family in intuitionistic monotone modal logic. It compresses arbitrarily large local families into a sharp two-member presentation without changing any formula, and calculates the exact number of distinct simultaneous box/diamond behaviours. The exact quotient is useful for finite-model enumeration, comparing modalities and non-normal semantics, and benchmarking logical search procedures. The count is not a raw-table recomputation: a necessary-and-sufficient profile constraint and a general closed enumeration proof are supplied.

## Scientific limits and closest literature

The statement assumes only continuality, not the additional frame conditions corresponding to modal axioms. This is a full same-world semantic result for finite *chains*, not arbitrary posets; there is no claim of independent review or complete priority certification. The closest sources are Dalmonte–de Groot (2026), Dalmonte (2022), de Groot (2025), and the published finite-chain relational/instantial works described in `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
