# Scientific review

## Correctness — PASS

The domain consists of two independently Bernoulli-sampled relations over a common finite key and value alphabet. Given a key and the cardinality of its first relation's fiber, an overlapping value contributes one fewer mismatch than a nonoverlapping value; this proves the full finite PGF directly, including empty fibers. The zero-event is exhausted by the two empty-fiber cases and the common singleton case. In the balanced regime, simultaneous nonempty fibers occur with probability \(ab/q+o(1/q)\) and multiple violations are negligible per key. In the imbalanced regime, the rare fiber is singleton with probability \(b/q+o(1/q)\), creating a nearly Poisson number of repeated mismatches. The respective limiting generating functions establish both laws, and exact linearity gives the same limiting expectation. Exhaustive finite tests were replayed; they support but do not substitute for proof. No inference about unstudied regimes is made.

## Originality — PASS, with residual risk

Hannula–Kontinen–Virtema (arXiv:1704.02158), §§2.2–3 and 5, define poly-dependence and explore logical axiomatization and expressive power; these do not give its Bernoulli reliability law. Demetrovics et al. (*TCS* 190 (1998), §2 and Theorem 1) give classical one-relation random-tuple functional-dependency probabilities with an \(e^{-\lambda}\) limit; their sampling hypotheses do not cover independent two-table asymmetric regimes or force the present compound-Poisson law. Amarilli–Kimelfeld (arXiv:1908.07093, abstract and introductory results) establish model-counting and reliability complexity classifications, not this parameterized two-table PGF and cross-scaling distribution comparison. Searches for polyteam random sampling, aliases such as cross-table functional dependencies, reliability, and compound-Poisson violations found no stronger coverage among inspected results. Generic rare-event cluster laws, or uninspected relational probabilistic-query literature, might encode an equivalent special case; this remains a genuine residual risk, not a uniqueness claim.

## Mathematical value — PASS

The truth value of poly-dependence is an integrity test across distinct database teams. An explicit exact probability and the full violation-generating function supply natural reliability and defect-severity invariants. The substantive boundary is that two distributions with **the same limiting mean** exhibit strictly different rates of logical validity: \(e^{-ab}\) versus \(e^{-b(1-e^{-a})}\). The latter overdispersion reveals a coherent violation-clustering mechanism, so the distinction cannot be recovered by a naive Poisson approximation based only on expected mismatches. This is a motivated classification of two naturally different sparsity designs, rather than an arbitrary small-parameter table.

## Scope and risk

Only two Bernoulli-independent relations with uniform per-relation probabilities, and the balanced and asymmetric critical limits, are proved. Exact formulas cover all finite alphabet sizes; no arbitrary-parameter phase diagram, general dependent sampling, or unique novelty guarantee is claimed. Independent mathematical and literature audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
