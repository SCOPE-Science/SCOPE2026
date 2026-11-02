# Scientific review: binary additive-colouring spectra on cycles

## Correctness — PASS
The claim is precisely formulated for labelled simple cycles with the two-number palette. Translating the inequality from numeric labels to bits yields the exact four-window condition. Its eight-state closed-walk representation is a bijection, and listing all simple directed cycles yields the rational determinant through the disjoint-cycle expansion. The trace–determinant identity establishes every coefficient for every cycle length. The forbidden-window and cyclic-gap arguments establish minimum support and multiplicity. Complementation proves symmetry. The standalone checker independently reconstructs the local rules and enumerates all short assignments. This verifies the critical finite computation without using it as an infinite proof.

## Originality — PASS (qualified)
Koutsoutis–Koutsoutis (2026, arXiv:2610.30174) prove a sharp general upper bound on the additive chromatic number, rather than this specific generating function. Severín (2016, arXiv:1602.07675) computes the exact additive chromatic number on cycles, but the checked relevant sections do not enumerate two-label assignments by weight. Comparisons under the terms lucky labeling, additive coloring, neighbourhood sum distinguishing labeling, transfer-matrix enumeration, and constrained cyclic binary word count found no covering formula. A more general existing enumeration or exact-sequence record may imply the result; this residual priority risk is explicitly acknowledged. A negative search alone was not used as a novelty proof.

## Mathematical value — PASS
The new object is the complete count of optimal-palette additive labelings, refining a previously known minimum palette number. The all-weight generating function, exact extremal multiplicities, period-four contrast, coefficient symmetry, and growth law provide naturally motivated structural and enumerative information for an infinite graph family. The period-four multiplicity phenomenon is not implied by the two/three minimum palette-size dichotomy. The result is restricted to a natural small-palette question, not an arbitrary parameter slice.

## Limitations and risks
Only labelled simple cycles with two numeric labels are enumerated; odd cycles have no such assignments. Three-label functions, larger palettes and symmetry-quotient counts remain untreated. A generic pre-existing cyclic-local-constraint enumeration might subsume the rational function. Verification is exact but not an independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
