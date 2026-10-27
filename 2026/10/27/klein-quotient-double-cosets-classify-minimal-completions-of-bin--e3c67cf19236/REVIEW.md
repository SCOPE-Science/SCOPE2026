# Scientific review

## Correctness (PASS)

The claim is an iff **for arbitrary supplementary generating sets**, not merely a formula for the minimum size. The proof independently reconstructs the first-nonunit kernel argument: an elementary collapse between two size-four orbits is kernel-minimal among nonunits, so one generator must itself lie in its left-right unit double-coset. Equivariant units preserve exact stabilizer subgroups; different quotient kernels cannot share a generator. The converse is proved using the full finite-group orbit-collapse generation theorem and Lemma 3.14(1) of arXiv:2610.18480v1. The four-point quotient configuration census and the sixfold quotient-map normalization establish the formula. `verify.py` independently checks all quotient kernels for binary ranks two through five and all relevant orbit types in ranks two and three. The finite tests supplement, rather than replace, the all-group proof.

## Originality (PASS, with priority risk)

The closest paper, arXiv:2610.18480v1, gives a qualitative generation criterion and critical lemmas. arXiv:2610.20329v1 explicitly computes relative rank one for the single Klein-four group. arXiv:2203.12158v3 studies rank modulo all units, not modulo the lazy-generated submonoid. None states the arbitrary-supplement **double-coset hitting criterion** for all finite groups or its exact Gaussian-quotient count; for \((C_2)^3\) the newly classified minimum is seven rather than the earlier isolated example's one. The present synthesis genuinely relies on known nonstandard lemmas, which are clearly cited and not claimed as original. A historical treatment under different semigroup language might cover the synthesis, so priority remains subject to specialist review.

## Mathematical value (PASS)

The earlier qualitative obstruction did not quantify how many inequivalent new rules are unavoidably required, nor characterize every suitable collection. The theorem answers that natural generator-design question for every finite group, showing that no single exotic rule can remove two distinct quotient obstructions. The exact minimum grows from \(1\) to \(7\), \(35\), and \(155\) for elementary-abelian groups of ranks two to five. Both the iff criterion and the sharp count are structural, not arbitrary finite slices.

## Closest literature and limits

The proof depends on published finite \(G\)-set decomposition and lazy-rule arguments; it does not extend to infinite groups, nonbinary alphabets, limited lazy neighborhoods, or word-length optimization. Strongest residual risk is an equivalent rank statement in broader algebraic-semigroup literature not located by the searches. No independent review or audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
