# Review of the exact prime-three border collision

## Correctness — PASS

The positive scaling of the source map and endpoint conventions are specified. Period-three orbits cannot contain a fixed point because none exists. Away from zero and the boundaries, sign parity forces exactly two inner visits and one outer visit. Positive-outer and negative-outer cases are mirror images; solving one three-equation affine system gives the unique candidate and strict inequalities that are equivalent to the threshold \(\(r(s-1)>1\)\). The boundary case is handled separately from \(0\mapsto-s\mapsto-r(s-1)\), with zero's only negative preimage \(-1\). The multiplier identity and its sharp lower bound follow from the same inequalities. The actual standalone checker passed five symbolic identities and 768 exact-rational itinerary trials. These trials corroborate the argument but do not prove its universal quantifier.

## Originality — PASS within inspected evidence

Direct semantic comparison was made with the 2021 source paper's available first-page preview and abstract; that material establishes the family and fixed-point-free/Devaney results, not the present all-parameter period-three theorem. The fully accessible 2023 follow-up's map and dynamical sections were read; they analyze one Devaney-chaotic example and numerically detected period-four/period-six dynamics, without the sharp prime-three census or multiplier gap. The 2022 comparative study was readable only at the abstract level and concerns numerical comparisons. Searches of relevant primary-literature phrases and the published-finding corpus mathematical index found no equivalent or stronger result. **Residual risk:** an uninspected theorem in the inaccessible 2021 body or 2022 chapter, or an unindexed subsequent paper, might cover part of the result. The available evidence supports but does not prove publication priority.

## Value — PASS

Period three is the shortest odd period possible after excluding all fixed points. The exact two-parameter phase diagram identifies its global existence boundary, explains the asymmetric border orbit caused by the prescribed discontinuity convention, and proves a sharp uniform multiplier gap exceeding four. This resolves a natural periodic-orbit question for the established map over an entire parameter region, rather than an arbitrary finite list of numerical instances. It makes no claims about invariant measures, crypto security, or higher periods.

## Scope of review

One mathematically unified claim is reported in RESULT.md and METADATA.json. The original 2021 paper's complete text and a related 2022 chapter remain materially unreadable; these affect priority confidence, not the analytic derivation. Independent mathematical audit is still outstanding.

Self-review: passed. Independent audit: not yet performed.
