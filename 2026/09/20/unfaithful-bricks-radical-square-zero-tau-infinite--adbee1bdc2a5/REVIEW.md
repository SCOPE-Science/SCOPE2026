# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** Mousavand--Paquette reduce every minimal τ-tilting-infinite radical-square-zero algebra to a sink-source orientation of an affine Dynkin graph. The subsequent classification uses only the resulting path algebra.

For a sincere module, the annihilator has no semisimple idempotent part. When there are no parallel arrows, primitive idempotents isolate the one-dimensional arrow blocks, so the annihilator is exactly the span of arrows acting by zero. In a tree, a zero arrow disconnects a sincere representation, ruling it out for a brick. Thus affine D/E sincere bricks are faithful, while nonsincere bricks are unfaithful and have support on a proper finite-Dynkin subgraph, yielding only finitely many.

For an alternating affine cycle, nonsincere indecomposables are exactly interval modules on proper connected cyclic intervals; there are n(n-1). A sincere brick can have at most one zero arrow, because two zero edges disconnect the representation. With one specified zero arrow the representation factors through Dynkin A_n, which has a unique sincere indecomposable, of dimension vector (1,...,1). This gives exactly n further unfaithful bricks, hence n^2 total.

For Kronecker, a sincere unfaithful brick has a nonzero proper annihilator line in the two-dimensional parallel-arrow space. Factoring by that line gives A_2, whose unique sincere indecomposable has dimension (1,1). Conversely every nonzero pair of arrow scalars defines such a brick, with annihilator the orthogonal linear relation, giving a P^1(k)-family. Nonsincere bricks are the two vertex simples.

Finally, Kronecker has infinitely many two-sided ideals because every line in its two-dimensional arrow space is an ideal. In every other sink-source affine case there are no parallel arrows, and every ideal is determined by a finite set of vertex idempotents together with a finite set of one-dimensional arrow blocks. Jans's criterion therefore gives nondistributivity exactly in the Kronecker case.

No computational evidence is required for these arguments.

## Originality

**PASS, to the best of our knowledge.** The 2023 Mousavand--Paquette paper was inspected around its radical-square-zero classification, its discussion of faithful and unfaithful bricks, the Kronecker example, and its stated question relating nondistributivity to infinitely many unfaithful bricks. It establishes the sink-source affine-Dynkin reduction and notes that regular Kronecker bricks are unfaithful, but it does not state the three-way classification above, the exact n^2 count for alternating affine cycles, or the affirmative solution of its question for the complete radical-square-zero subclass.

Targeted literature searches covered faithful/unfaithful bricks for Kronecker and extended-Dynkin quivers, annihilators of regular-simple modules, minimal τ-tilting-infinite algebras together with nondistributivity, and synonymous formulations using sincere bricks and annihilators. No prior theorem matching the classification or the n^2 cycle count was located.

Recent work on radical-square-zero representation theory was also checked for a current-status collision. Drozd's 2026 paper on representations of radical-square-zero algebras does not present a matching brick/annihilator classification in the accessible text inspected.

The residual originality risk is meaningful: after the known affine-Dynkin reduction, the proof is elementary and could exist as folklore, an exercise, or an observation phrased without τ-tilting terminology. The literature search is not exhaustive over all historical affine-quiver sources. No highly relevant inaccessible paper was identified that provided concrete evidence of prior coverage.

## Value

**PASS.** The result answers a published structural question on a complete nontrivial subclass rather than merely adding an example. It also gives a sharp trichotomy: the Kronecker algebra has a projective family of unfaithful sincere bricks, alternating affine cycles have exactly n^2 unfaithful bricks, and affine D/E tree types have only finitely many, with every sincere brick faithful. The proof identifies parallel-arrow linear dependence as the mechanism responsible for the infinite unfaithful family.

## Scope and status

The theorem applies only to minimal τ-tilting-infinite algebras with radical square zero; the general Mousavand--Paquette question remains outside its scope. Originality is to the best of our knowledge.

The review is not independent validation, formal verification, or peer review.
