# Review

## Correctness

PASS. Both published revision maps take values only among facets satisfying the announced factual formula. Definition 5.1 explicitly fixes each already-satisfying facet pointwise. For Definition 5.2, if all current belief facets satisfy the announcement, its internal Grove branch is nonempty for every input facet, selects only current same-perspective facets, and contains the input facet itself. Thus both operators fix exactly the models whose belief facets all satisfy the announcement. Their outputs always have that property, proving idempotence.

If \(F_\psi\subseteq F_\varphi\), a \(\psi\)-revised model is already a fixed point for \(\varphi\), yielding the absorption identity. The argument is independent of finiteness and does not infer a general theorem from the bundled finite enumeration.

## Originality

PASS. The primary source defines the two revision operators and discusses nontrivial behavior under iterated, changing announcements, but it does not state their exact fixed-point class, idempotence, or entailment absorption. The author explicitly lists comparison with AGM revision as future work.

Targeted searches for repeated simplicial revision, idempotence, retractions, fixed points, and same-announcement stability did not locate the model-level result. Standard AGM repeated-input stability is relevant background, but it concerns belief sets under abstract postulates and does not imply equality of these agent-indexed simplicial subcomplex transformations.

## Value

PASS. The source motivates memory mechanisms because iterated revision can oscillate. The theorem isolates a sharp structural boundary: neither basic operator can oscillate under repetition of one factual input, because each is a retraction after one step. The fixed-point theorem and entailment-absorption law identify exactly which iterated behaviors remain possible and give reusable algebraic laws for later action-model or protocol analyses.

## Closest literature and limitations

The closest source is Sink's 2026 simplicial revision paper, especially Definitions 5.1 and 5.2 and the later iterated-revision discussion. A follow-up preprint develops simplicial actions for distributed protocols and incorporates belief revision into action models; only its abstract and accessible summaries were available in the comparison performed here, so complete overlap with every later action-model specialization remains a residual risk.

The result is restricted to factual formulas and the two basic revision definitions. It does not claim commutativity of different announcements or cover the memory-enriched variants.

Same-model review: passed. Independent audit: not yet performed.
