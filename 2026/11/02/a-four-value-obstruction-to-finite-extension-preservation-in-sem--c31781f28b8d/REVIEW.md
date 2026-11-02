# Self-review

## Correctness — PASS

The quantified theorem is proved for naturally ordered, zero-sum-free semirings with nondecreasing squares, a unit with no additive absorption, and one nonidempotent square. Extension preservation follows termwise from monotonic powers. Nondefinability uses two model-defining domains and a sum-of-monomials expansion for an arbitrary existential NNF formula; the hypotheses force all additional monomials to vanish at unit weight and remain zero at the distinguishing weight. Saturated counting operations meet the hypotheses for every integer cap at least three, and the exact boundary for the designated sentence at the two smaller caps is checked. `checker.py` produced `ALL_CHECKS_OK axioms=1295 extension_pairs=10269 witness_cases=13`. Exhaustive finite checks are subsidiary to the universal proof.

## Originality — PASS within inspected evidence

The strongest directly relevant prior result is Brinke–Dawar–Grädel–Pago (arXiv:2605.10829; ICALP 2026, Theorem 5.1 and Lemma 3.1), proving a failure for the unbounded natural semiring using the same sentence. Their Theorem 5.11 proves a positive theorem for non-Boolean lattice semirings and does not cover capped counting. The present result distinguishes every finite capped semiring with four or more elements, whereas polynomial degree unboundedness used for the natural semiring is unavailable after saturation; a new two-domain monomial obstruction is supplied. The separate CSL 2026 compactness paper concerns semiring compactness, not this finite existential equivalence. Targeted published-work searches and semantic database comparisons did not exhibit an equivalent finite capped theorem. The longer arXiv version and unindexed literature remain material priority risks, not evidence of uniqueness.

## Value — PASS

The motivating article explicitly asks which other semirings retain finite extension preservation. This structural obstruction criterion supplies an infinite family of finite non-lattice failures and a smallest member within the capped-counting family, separating saturation from idempotent lattice semantics. It classifies the behavior of a natural preservation-test sentence across all finite caps, rather than merely exhibiting a numerically accidental small counterexample.

Self-review: passed. Independent audit: not yet performed.
