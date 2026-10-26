# Research review

## Correctness — PASS
The host-tree coding and inversion graph characterization follow Janson's Lemma 11. The automata record inversion conditions for all selected pairs, count only four-marked increasing position sets, and exhaust both choices of each free code symbol. The explicit denominator bound \(71+45=116\), plus mandatory endpoints, makes the coefficient check through degree 122 an **all-length** rational identity proof. Re-execution of `verify.py` establishes the two reachable state sizes, all 123 exact identities, full binary-code enumerations through size 9, and an independent brute permutation comparison through size 7. The strict positivity argument uses positive power-series factors. Risk: transfer construction is a nonstandard combinatorial lemma requiring careful inspection; the certificate and transition definitions are included.

## Originality — PASS, with bounded priority risk
Janson's 2022 first public preprint (Problem 7) explicitly states the finite-size equal-expectations extension to equal-length, equal-block-count forest patterns was unknown. Its established equality is for tree-pattern inputs, while the new inputs 1243 and 1324 are forest patterns. The full paper's coding and later pattern-count discussion were inspected; no formula for this pair appears in that material. Acan–Hitczenko (2014), Section 2, supplies the tree-permutation count and coding, not this pairwise expectation law in the inspected sections. Current mathematical record and external searches yielded no stronger covering result, but no search proves unique priority. Specific risk: equivalent results may be derived in broader enumeration literature.

## Value — PASS
The theorem answers an explicit published equality question with the smallest natural four-letter examples, and strengthens a one-size counterexample to an exact all-size rational generating function and positive gap for every size at least five. The essential contrast is structural: equal block count controls the leading asymptotic but not exact finite-size expectations.

## Scope of validation
Proof and checker are internally reproducible with exact arithmetic. The result has not undergone independent assessment. Historical-priority uncertainty remains.

Self-review: passed. Independent audit: not yet performed.
