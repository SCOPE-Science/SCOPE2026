# Scientific review

## Correctness

**PASS.** The singleton-generator lemma is an exact consequence of the inhabited-neighborhood semantics and downward persistence of support, not a finite-depth approximation. Structural induction handles atoms, empty state, conjunction, inquisitive disjunction, implication, and arbitrarily nested existential modalities. Both witnessing models use the same upward-monotone neighborhood structure. The formula \(\top\Rrightarrow?p\) distinguishes them exactly because the two-world neighborhood fails to settle \(p\) in one valuation. The one-world bound follows from exhaustion of the only two possible inhabited neighborhood families on a singleton and a uniform recursive elimination translation. A direct semantic checker passed 22,584 assertions; no infinite conclusion is inferred from enumeration.

## Originality

**PASS with residual literature risk.** Ciardelli's 2025 full-text article explicitly leaves existential definability over upward-monotone models open in Open Problem 4.6. Its earlier nondefinability statement (Corollary 4.4) is over unrestricted neighborhood models; it does not logically establish nondefinability on the upward-monotone subclass. The new two-world construction lives wholly inside that subclass and so closes this quantifier gap. Searches in mathematical research records, public literature, and accessible prior work found no stronger equivalent claim. This is best-knowledge originality rather than an assertion that no unindexed version exists.

## Value

**PASS.** The result resolves the first half of an explicit recent open problem in the semantics of inquisitive modal logic with a sharp minimal countermodel. It identifies why the existential operator cannot express global question settlement on a singleton-generated upward filter, clarifying the expressive boundary between unary and binary neighborhood operators. The convex-model/two-unary question remains open under this argument.

Self-review: passed. Independent audit: not yet performed.
