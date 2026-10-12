# Scientific review of the shared sign-bilinear dimension theorem

## Correctness — PASS
The statement quantifies over every positive finite chain size, with one shared real entity vector for both relations and both argument positions, separate arbitrary bilinear matrices, and strictly signed scores. The explicit integer matrices prove each upper bound without approximation. The lower bound is a fully algebraic argument: equality's diagonal/off-diagonal pattern forces any dependence among three two-dimensional entity vectors to be strictly positive, but the strict order's all-negative first column excludes such a dependence. The one- and two-element minima are separately checked. `verify.py` confirmed the constructions over sizes one through one hundred and both separate-witness examples. No computation is relied upon for the universal lower bound.

## Originality — PASS, with residual risk
Quigley's arXiv:2609.18047v1 Corollaries 6.1–6.2 concern equality of real score matrices, not thresholded signs, and his Section 7 explicitly distinguishes support recovery from exact factorization. Sherstov's sign-rank examples show that each relation separately has a small-rank sign matrix, but do not enforce a shared set of vectors with equal head and tail representations. Wang–Gemulla–Li's 2018 universality and nonuniversality results, and Badreddine–van Krieken–Serafini's 2025 sign bottleneck bounds, do not specify the simultaneous equality/order minimum. Published-record searches for shared bilinear sign embeddings and the three-point obstruction found no direct counterpart. An equivalent result could remain implicit in oriented-matroid or common-factor sign-pattern literature; this limits novelty confidence, and absence from searched records is not treated as proof of uniqueness.

## Value — PASS
Equality and strict linear order are canonical binary logical relations, and the same-vector constraint is central to relational embedding semantics. The sharp dimension invariant is constant at three even where exact truth-matrix representation needs all domain coordinates. On three entities the comparison is genuinely joint: each relation individually permits dimension two, while the pair forbids it. This isolates a natural representational interaction rather than a special-purpose numerical slice. The result does not guarantee compositional truth-vector semantics or learned parameter recovery.

## Overall status
Self-review: passed. Independent audit: not yet performed.
