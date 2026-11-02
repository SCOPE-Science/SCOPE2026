# Scientific review: prime-power circular defect-one automata

## Correctness — PASS

The claim's exact domain is \(n=p^k\), \(p\) prime and \(k\ge2\), with one fixed cycle letter and every rank-\((n-1)\) second transition. The use of the established defect-one primitivity theorem is stated openly. Translation-invariance characterizes all possible congruences, while the rank condition forces each preserved quotient action to be a permutation. This proves the exact union-of-events characterization. Nested-block permutations and one defective fiber give each intersection size, and finite inclusion-exclusion yields the claimed nonnegative integer. Rank-defect-one map counts and free cyclic-conjugation orbits are proved separately. The independently implemented exhaustive pair-automaton census for four and eight states has no discrepancy with the structural criterion or factorial formula. The proof is conditional on the cited published primitive-automaton theorem, not on extrapolation from those finite checks.

## Originality — PASS, with historical-priority risk

The 2013 paper of Araújo and Cameron contains the primitive-permutation-group synchronization theorem, not the formula counting *all* rank-defect-one maps of a given prime-power circular automaton. Volkov's 2024 Corollary 2.4 is the stronger primitive-automaton criterion used in the argument and is explicitly credited; the formula is not claimed as a fresh proof of that criterion. Berlinkov–Nicaud (2018) give asymptotic nonsynchronization probabilities for almost-group automata, whose exceptional letter is a permutation except at one dangling state, a different and narrower family. The 2019 circular-random-automaton probability theorem uses an unrestricted random second letter and asymptotic bounds. An earlier exact finite census already contains the eight-state count of 1,856 rotational classes, so that special number is excluded from novelty. The new assessed claim is the complete all-prime-power factorial inclusion-exclusion distribution and exact rotation-class count. Searches for its equivalences, broader coverage, and tables did not identify the formula. The residual risk of an overlooked earlier exact enumeration is material and is not represented as independently resolved.

## Value — PASS

Nonsynchronization is the basic obstruction to reset coding in circular automata, and conditioning the second letter to have exactly one defect is the smallest nonpermutation perturbation. This theorem quantifies the entire exceptional set rather than a single extremal length or a small case. Overlapping congruence levels create genuine nontrivial correction terms: for eight states the two preservation-event sizes are 13,824 and 1,536 with a 512-map overlap. The all-prime-power formula separates this arithmetic obstruction from the generic synchronizing behavior and supplies exact conditional probabilities and unlabeled counts without enumerating exponentially many transitions.

## Closest literature and limitations

Araújo–Cameron (2013) and Volkov (2024) are the decisive structural sources. The 2018 almost-group model and 2019 circular random-model study are relevant but do not give the stated exact finite enumeration under the current parameter conditioning. The eight-state numeric special case was previously available. The theorem does not address arbitrary state numbers or unrestricted transition ranks. Formal peer or independent audit of the new all-order count has not occurred.

Self-review: passed. Independent audit: not yet performed.
