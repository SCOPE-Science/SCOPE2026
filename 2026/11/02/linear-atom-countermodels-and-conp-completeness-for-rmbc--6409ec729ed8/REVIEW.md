# Self-review

## Correctness — PASS

The separation lemma is proved by refining the equivalence classes of at most \(t+1\) subformula values with at most \(t\) selected finite-Boolean-algebra atoms. Inserting the projected, partially specified negation and consistency tables is justified by injectivity on the full set of those values; defaults satisfy both BALFI identities, including where just one unary operation has been prescribed. The polynomial certificate checks the same local identities and functional collisions; the non-top output survives. The hardness bound is attributed to Coniglio–Mallea, arXiv:2608.28443. The checker performs 41,568 exhaustive small-case trials, 2,000 seeded randomized trials, and a separate witness; it is not a substitute for the proof.

## Originality — PASS with explicit priority risk

Coniglio–Mallea establish decidability and a 2-EXPTIME validity upper, not the constructive linear-atom BALFI countermodel lemma or coNP upper bound. Carnielli–Coniglio–Fuenmayor prove BALFI semantics and translation to two non-normal modalities, and Dalmonte–Mazzullo prove coNP for relevant modal fusions. Those earlier results create a serious, acknowledged alternative-derivation risk for the coNP corollary; the directly established fine-grained Boolean-atom bound is not stated in the material inspected. A complete older-literature priority guarantee cannot be given.

## Value — PASS

The motivating finite-filtration argument gives an exponentially structured family of Boolean subformula values without a tight complexity classification. A linear number of distinguishable atoms and a polynomial-size native-language verifier sharpens the decision upper bound to match the known lower bound. The distinction between whole-vector functionality and single-coordinate projection is structurally necessary and is demonstrated by a small counterexample.

## Closest literature and limitations

Coniglio–Mallea (2026; arXiv:2608.28443), Carnielli–Coniglio–Fuenmayor (2020/2022; arXiv:2003.09522), and Dalmonte–Mazzullo (2023; DOI:10.1007/978-3-031-43513-3_17). The atom upper bound is not claimed sharp; no inference about added algebraic axioms or theories with arbitrary premises is made; the existing modal embedding may admit a more compact encoding than inspected here.

Self-review: passed. Independent audit: not yet performed.
