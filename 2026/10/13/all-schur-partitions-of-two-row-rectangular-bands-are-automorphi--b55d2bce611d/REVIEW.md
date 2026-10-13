# Review: Schur partitions of two-row rectangular bands

**Correctness — PASS.** The product-coefficient identity \(r_X(i)c_Y(j)\) makes the closure test exact. Summing over block colors yields necessary row/column incidence-profile constancy, and the converse is immediate. In the unequal-row case this forces identical partitions in both rows. In the balanced case, the unordered pair of block colors in each column identifies a unique monochrome or equal-size paired component. A symmetric-group generator construction realizes all blocks as orbits. The exponential formula then counts labelled components without duplication. An exhaustive finite checker, not used as a substitute for proof, tests all partitions up to eight cells and reconstructs orbit witnesses.

**Originality — PASS, with residual risk.** Marrow–Misseldine (arXiv:2601.09940v1, January 14, 2026), Sections 2.2, 5.4, 5.6, provides \(2\mathscr B(m)\) direct-product examples for the two-row band and tabulates the counts \(5\) and \(13\) at the first two nontrivial sizes. It does not state or imply the all-\(m\) automorphic classification or the exact labelled enumerator. Exact-object, orbit-partition, equitable-profile, and stronger-coverage searches found no covering theorem, but older equivalence under different terminology remains possible.

**Value — PASS.** The classification resolves the natural simplest rectangular-band case beyond direct products, computes the full enumeration, and determines every Schur partition as an explicit automorphism orbit partition. In particular \(m=4\) has \(48\) Schur partitions, of which \(18\) are not direct products. This is a structural family theorem, not a routine small-tabulation extension.

**Scope.** Only the \(2\)-by-\(m\) rectangular band over rational coefficients; neither three-row bands nor positive-characteristic coefficient rings are classified. Independent verification of originality remains desirable.

Self-review: passed. Independent audit: not yet performed.
