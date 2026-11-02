# Review of the optimal prism proper conflict-free colouring census

## Correctness — PASS

A two-column transition state records every proper rung/row edge and tests both open-neighbourhood uniqueness conditions. Closed length-\(n\) walks are in bijection with named valid colourings of the labelled prism. The finite, explicitly defined transfer matrices have dimensions 18 and 84. An independent standard-library checker constructs them and certifies every characteristic-polynomial coefficient using integer traces and Newton identities. Formal log-differentiation therefore proves the all-length generating functions. Direct labelled assignment tests over 6,498,957 assignments, constructive closed walks, and exact characteristic checks corroborate the proof. Finite tests are not substituted for the universal transfer identity.

## Originality — PASS, qualified

Madaras and Šurimová (2023), Theorem 3, prove prism homogeneous-colouring existence ranges, including the \(3\mid n\) threshold; that threshold is credited. They do not give the all-length counts. Allagan and collaborators (2026) derive the ordinary prism chromatic polynomial, whose transfer counts colourings without the conflict-free neighbourhood constraint. Qi, Song and Cao (2026) study proper conflict-free list-colouring of high-girth sparse graphs, not these labelled counts. Comparison by dynamic-colouring terminology and ordinary-versus-constrained transfer implications did not identify the same determinant or exact sequence. A general, unlocated enumeration may still subsume the formula. Some indirect sources were available only as abstracts.

## Value — PASS

The result completely enumerates the minimum-palette admissible colourings of an infinite, standard cubic family, not just the minimum number of colours. The unexpected full four-colour determinant and explicit spectral rate give a quantitative measure of how strongly the local uniqueness condition restricts ordinary proper colourings. A complete count, sharp three-colour multiplicity, and conditional exponential decay are mathematically motivated invariants of the same model.

## Scientific limits

The theorem covers labelled cycle prisms of length at least three with three or four available named colours. It does not describe arbitrary palettes, list-colouring, or orbit counts. Independent historical-priority and mathematical assessments are not claimed.

Self-review: passed. Independent audit: not yet performed.
