# Scientific review

## Correctness — PASS

The disk has 13 lattice points. The sharp planar Steinitz constant \(\sqrt5/2\), explicitly established in the cited Girard–Plagne source, gives an absolute cutoff of 21 for every primitive zero sum. The six antipodal pairs yield exactly 64 one-sign orientation cases for lengths at least three. For each, two integer-independent pivots and all 809,600 bounded free quadruples are exhaustively enumerated; Cramer's rule is exact. The primitive-antichain pruning is sound because any proper zero-sum submultiset has strictly smaller free-degree. The certificate, replayed successfully, reports counts 12/16/12 at lengths three/four/five; 12 extrema split into two orbits of sizes 4 and 8. Direct subset-sum checking independently establishes minimality of all reported atoms. All counts and quantifiers are restricted to the radius-two lattice disk. Residual correctness risk: implementation errors in the enumerator or reliance on the cited non-elementary Steinitz theorem; the separate direct short enumeration helps mitigate, but does not eliminate, program risk.

## Originality — PASS (best-knowledge, residual risk)

The full-text primary paper of Girard and Plagne defines this invariant, proves general-radius bounds and a radius-one special case, and states a support-size conjecture; it does not supply the radius-two exact census or the two extremal symmetry types. The previous box literature deals with a superseding square lattice set, without an implication that determines the exact disk value or its primitive atoms. Actual semantic-index queries for the first nontrivial radius, aliases, 13 lattice points, primitive zero sums and dihedral symmetry, together with primary literature and accessible prior claims, disclosed no covering theorem. The observed value does not follow from the parent's asymptotic upper/lower bounds or a generic larger-set inequality. Residual risk: an obscure unindexed elementary calculation or earlier classification may exist; a database nonhit does not prove novelty.

## Value — PASS

This is the first nontrivial integer-radius planar disk immediately after the known radius-one case, in a family introduced and investigated by recent literature. The result determines the complete natural primitive-relation semigroup basis (47 atoms), its exact maximal length, and the full symmetry-orbit classification. The coexistence of two distinct support sizes at the exact maximum is useful finite structural information for understanding support-restricted Davenport invariants; it is not merely a selected random numerical instance. Larger-radius behavior remains open.

Self-review: passed. Independent audit: not yet performed.
