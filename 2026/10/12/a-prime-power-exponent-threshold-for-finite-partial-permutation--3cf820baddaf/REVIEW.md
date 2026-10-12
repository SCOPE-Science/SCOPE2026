# Scientific review

## Correctness (PASS)

The exact problem is completion on the original finite carrier, with an explicit partial injection and a binary-encoded exponent. Each pre-existing cycle is forced; every path must occupy consecutive positions on one allowed cycle, yielding the exact packing equivalence. The 3-PARTITION reduction uses \(P=3Q\), \(L_i=3a_i+(Q-B)\); the inequalities \(P/4<L_i<P/2\) hold for every admissible source instance. Size-\(P\) cycles contain precisely three paths, size-\(P/3\) cycles precisely one path corresponding to \(a_i=B/3\); singleton exceptions appear in multiples of three and reassemble into valid original triples. The unary reduction is polynomial in the explicitly represented output size. Membership is verified via cycle decomposition. Fixed-exponent count-vector DP is polynomial for each fixed exponent. Verification replay passes 2317 six-integer reductions, 15 constructed cycle witnesses, and 5004 fixed-exponent packing comparisons. Exhaustive small cases are corroboration only.

## Originality (PASS; residual historical risk)

The motivating 2026 preprint allows enlargement of the carrier, studies existence of \(\Pi\)-group extensions and group-topological obstructions, and does not report the zero-added-vertex bounded-exponent NP-completeness or the fixed-exponent polynomial boundary in the inspected full-text sections. The 2003 Auinger–Steinberg article concerns existence of pseudovariety extensions, again with potentially larger carrier; only its abstract and bibliographic records were accessible, so complete exclusion of a hidden related result is impossible. Lohrey–Rosowski's 2025 cycle-type problem searches an already generated group, a different domain of choices. The classical partition-packing equivalence is an ingredient, not novel in isolation. Recorded searches of term variants, claim implications and accessible published records returned no exact covering theorem. Remaining risk: older equivalent results indexed as fixed-length cycle packing or partial injection completion.

## Value (PASS)

This distinguishes qualitative finite \(3\)-group extension existence from finite-model resource feasibility with **zero** new vertices. It gives a natural NP-completeness/tractability boundary in one-map partial-automorphism extension theory, with a restricted hardness construction and a fixed-parameter-slice decision algorithm. The power-of-three divisibility requirement and singleton \(P/3\) exceptions make a generic packing argument insufficient without the explicit reduction. The statement is not merely an isolated numerical fact.

Self-review: passed. Independent audit: not yet performed.
