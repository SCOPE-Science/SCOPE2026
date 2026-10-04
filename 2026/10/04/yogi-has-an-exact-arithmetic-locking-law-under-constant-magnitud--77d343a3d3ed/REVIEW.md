# Review

## Correctness

PASS. The normalized Yogi second moment is a deterministic fixed-step walk toward the target \(1\). Exact divisibility gives finite hitting and locking; nondivisibility gives immediate alternation between adjacent lattice points. The cycle width, first-moment limit, update-magnitude cycle, and Adam comparison all follow from exact scalar recurrences.

Risk: implementations with different initialization or debiasing conventions have different transients.

## Originality

PASS. The defining Yogi paper provides the sign-controlled additive recurrence and qualitative effective-learning-rate motivation, but the inspected full text does not state the arithmetic finite-lock versus period-two classification. Focused published-record and web searches found no implication-equivalent result.

Residual risk: the recurrence is simple enough that an equivalent calculation may exist in unindexed notes.

## Value

PASS. The finding concerns Yogi's defining mechanism rather than an arbitrary parameter slice. It shows that constant forcing does not generically produce a convergent second moment: exact convergence occurs only on an arithmetic locking set, while all other beta-two values produce a persistent two-cycle of exactly known width. The paper's reported beta-two grid lies precisely on the locking set.

Same-model review: passed. Independent audit: not yet performed.
