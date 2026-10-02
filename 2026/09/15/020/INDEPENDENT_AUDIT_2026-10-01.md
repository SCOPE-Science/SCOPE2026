# Independent mathematical audit — 2026-10-01

Audited at: 2026-10-01T04:47:00Z

## Final claim

Finite-iterate self-compatibility implies hyperfiniteness for hyperfinite-over-hyperfinite equivalence relations

## Correctness — PASS

PASS. The mod-n decimation argument was reconstructed directly. On the full part of a class-wise Z^2 ordering, the finite-interval F-classes are indexed by Z and the total predecessor map shifts this index by -1. The relation E_n retaining block indices modulo n is Borel and splits each E-class into exactly n E_n-classes. The inherited order on each E_n-class is again Z^2 and has the same finite-interval relation F; its immediate predecessor among F-blocks is exactly the n-step predecessor. Therefore compatibility with the n-step derived F-order is precisely the self-compatibility hypothesis needed for Gao-Xiao's theorem applied to E_n. Hyperfiniteness of E_n then lifts across the finite index-n extension, and the non-full part is already hyperfinite. No finite experiment is used.

## Originality — PASS

PASS. Resultary and web searches found only the audited record for the finite-iterate statement. Gao-Xiao's published theorem covers self-compatible Z^2-orderings (the one-step setting) but does not state the mod-n decimation extension in the accessible primary abstract. The audited theorem requires the additional construction of E_n and the proof that the inherited ordering has the same finite-interval relation and n-step immediate predecessor. This is a genuine reduction rather than a parameter substitution; no prior exact implication was located.

### Equivalent formulations
PASS. Resultary and web searches found only the audited record for the finite-iterate statement. Gao-Xiao's published theorem covers self-compatible Z^2-orderings (the one-step setting) but does not state the mod-n decimation extension in the accessible primary abstract. The audited theorem requires the additional construction of E_n and the proof that the inherited ordering has the same finite-interval relation and n-step immediate predecessor. This is a genuine reduction rather than a parameter substitution; no prior exact implication was located.

### Broader coverage
PASS. Resultary and web searches found only the audited record for the finite-iterate statement. Gao-Xiao's published theorem covers self-compatible Z^2-orderings (the one-step setting) but does not state the mod-n decimation extension in the accessible primary abstract. The audited theorem requires the additional construction of E_n and the proof that the inherited ordering has the same finite-interval relation and n-step immediate predecessor. This is a genuine reduction rather than a parameter substitution; no prior exact implication was located.

### Exact database or table
No exact database/table coverage was identified; this is supporting best-knowledge evidence only, not proof by failed search.

### Claim versus prior implication
PASS. Resultary and web searches found only the audited record for the finite-iterate statement. Gao-Xiao's published theorem covers self-compatible Z^2-orderings (the one-step setting) but does not state the mod-n decimation extension in the accessible primary abstract. The audited theorem requires the additional construction of E_n and the proof that the inherited ordering has the same finite-interval relation and n-step immediate predecessor. This is a genuine reduction rather than a parameter substitution; no prior exact implication was located.

## Scientific value — PASS

PASS. The result advances a natural finite-iterate variant of a theorem aimed at the Hyperfinite-over-Hyperfinite problem. It gives a clean closure principle for every finite iterate without claiming the general open problem.

## Sources inspected

- **Su Gao and Ming Xiao, An order analysis of hyperfinite Borel equivalence relations** (https://arxiv.org/abs/2404.17516): GENERAL_ONE_STEP_THEOREM_NOT_EXACT_FINITE_ITERATE_STATEMENT. The accessible primary text states the self-compatible theorem but not the finite-iterate mod-n conclusion.
- **R. Dougherty, S. Jackson and A. S. Kechris, The structure of hyperfinite Borel equivalence relations** (https://doi.org/10.1090/S0002-9947-1994-1149121-0): STANDARD_CLOSURE_INPUT. Finite extensions of hyperfinite countable Borel equivalence relations are hyperfinite; this supplies only the last step, not the E_n construction.

## Residual risks

- Full text of Gao-Xiao was not successfully obtained in this run; this leaves a residual risk that a later section already records the finite-iterate reduction even though no exact search hit was found.
- The theorem depends on the RESULT's Section-5-style meaning of the n-step derived order; other meanings of a gamma^n-derived order are outside the audited claim.

## Disposition

**passed**
