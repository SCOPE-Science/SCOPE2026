# Same-model review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

**PASS.** Each obstruction has a direct model-independent check.

1. In the one-vertex one-loop graph, the vertex idempotent is the identity and the Kumjian--Pask algebra is the Laurent algebra. Therefore the corner is the full Laurent algebra, not the coefficient ring.
2. For two disjoint one-loop components and the hereditary saturated subset containing one component, the subgraph algebra is the second direct summand. The first summand is annihilated by the identity of that corner algebra, so the ambient algebra cannot be a free right module over it. The tensor repair follows from the elementary balancing identity `a⊗v=a⊗pv=ap⊗v`.
3. In a Hausdorff ample groupoid, the point mass at the isotropy identity belongs to the Steinberg algebra only if the unit singleton is open. Conversely, an isolated unit makes every isotropy singleton compact open by restricting a compact-open bisection along the source local homeomorphism. This proves the iff criterion. The one-vertex two-loop path space has no isolated points, giving an explicit counterexample.

No computation or unreported software output is required.

## Adversarial checks

The main possible loophole is a convention allowing nonunital right modules over a unital corner algebra. It does not rescue the freeness claim: every free module over a unital ring is unital, while the displayed ambient right module has a nonzero element annihilated by the corner identity. Moreover the specific outside-vertex generator appearing in the proposed transversal has zero product with every coefficient from the corner algebra and hence cannot generate itself.

The singleton-isotropy obstruction does not depend on nontrivial isotropy. Even when the isotropy group is trivial, the proposed algebra map must send its identity to the characteristic function of the singleton unit; this function is absent whenever the boundary path is nonisolated.

The review deliberately does not infer that all later conclusions of the source paper are mathematically false. Some may be recoverable using established Steinberg-algebra isotropy induction or corrected corner bimodules. The finding concerns the stated constructions, missing hypotheses, counterexamples, and consequences for proofs depending on them.

## Originality

**PASS, to the best of our knowledge.** The general facts that Steinberg algebras are built from compact-open bisections, that open singleton units are special, and that isotropy induction exists are prior literature and are excluded from the novelty claim. The novelty claim is restricted to the correction of arXiv:2609.20230v1: the three explicit obstructions, the exact isolated-unit criterion for its point-mass embedding, and the idempotent-corner tensor repair of its hereditary induction object.

Internal archive searches for Kumjian--Pask, Steinberg isotropy, hereditary-subgraph freeness, and synonymous formulations found no overlapping accepted SCOPE record. External searches by the preprint identifier/title and by equivalent mathematical formulations found no prior public correction.

## Access and residual risk

The full arXiv HTML of arXiv:2609.20230v1 was inspected at the relevant definitions, propositions, theorems, proofs, examples, and reference list. The 2024 Nguyen--Nguyen article was inspected through its abstract and publisher-preview material; its complete text was not available in the sources inspected here. That creates a residual risk only for historical attribution of the standard isotropy machinery, not for the self-contained counterexamples or the correction to the new preprint. The source preprint is recent and may be revised after this record.

## Value

**PASS.** The affected claims are structural inputs to a proposed induction/restriction framework. The result gives exact boundaries rather than merely isolated counterexamples: actual vertex corners must be used; hereditary induction factors through `Ap`; and point-mass isotropy restriction is valid exactly for isolated boundary paths. These corrections distinguish what can be repaired locally from what requires the standard Steinberg isotropy machinery.
