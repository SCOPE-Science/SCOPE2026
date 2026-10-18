# Scientific review: random colored equal-block equivalence relations

## Correctness — PASS

The exact assumptions are that both block number and common block size diverge, with independent fair unary colors and ordinary first-order sentences over equivalence and color. The proof supplies a rank-\(q\) Ehrenfeucht–Fraïssé invariant: per-block color counts and multiplicities are truncated at \(q\). It directly constructs Duplicator's strategy for any \(q\), including equality and reused elements. With growing block sizes, all non-generic block types are precisely the finitely many low-color-count defects. Their multinomial counts have vanishing, diverging, or independent Poisson limits whenever each fixed expected count has an extended limit. Thus every fixed-rank profile and sentence probability converges. Conversely, explicit first-order sentences detecting an exactly \(r\)-colored class force convergence of each expected count; the binomial expression and its logarithmic asymptotics cover also divergent expectations. The ratio of binomial coefficients establishes uniqueness of a finite nonzero critical intensity, and the limiting bivariate generating function proves independence of the two symmetric defect counts. No numerical experiment is used as a proof of the asymptotic theorem. The executable finite checker returned `COLORED_EQUIVALENCE_VERIFY_OK EF=246 probability=36`.

## Originality — PASS, with a defined priority risk

The 2026 comparison article by Koponen [1] studies partial closure, finite model properties, and conditions on deterministic base structures; Example 2.12 and Remark 2.15 motivate random expansions but do not give the exact necessary-and-sufficient criterion for independent coloring of equal blocks. The 2025 motivating literature is Koponen–Karlsson [2], which gives a sufficient zero-one law for expansions of **ordered** equivalence classes with sizes growing faster than every logarithm and slower than a polynomial. The present criterion also handles the logarithmic rare-defect windows, proves necessity, determines Poisson probabilities there, and drops order. Its abstract does not establish those extensions, but the complete paper was inaccessible and could contain an unstated reduction: this is a specific residual originality risk. Dawar–Grädel–Hoelzel [3] addresses powers of a fixed finite structure rather than this family with two independently diverging size parameters. Direct semantic searches for the claim, equivalent Poisson formulations, and stronger general convergence theorems did not identify a covering record. Search absence is not proof of priority, and an unindexed general theorem may imply this specialization. Subject to these bounded source limitations, the statement and comparisons support originality.

## Value — PASS

The result classifies **all** growth sequences of a natural random monadic expansion by one explicit family of numerical invariants, simultaneously giving the exact zero-one boundary and every nontrivial Poisson critical regime. The positive-limit windows are precisely the places where rare almost-monochromatic equivalence classes cause measurable first-order events. These include regimes outside the superlogarithmic sufficient hypotheses of [2]. The classification provides concrete probability calculations for any fixed first-order sentence via finitely many truncated Poisson variables. This exact boundary has value beyond merely observing a standard probability limit; it does not claim a general randomized-structure limit theorem.

## Closest literature and limitations

[1] Vera Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories*, arXiv:2610.16163v1 (2026-10-12), especially Example 2.12 and Remark 2.15, https://arxiv.org/html/2610.16163v1.

[2] Vera Koponen and Edward Karlsson, *Convergence Laws for Expansions of Linear Preorders*, WoLLIC 2025, DOI:10.1007/978-3-031-99536-1_7 (first online 2025-08-01). Publisher/academic repository abstract inspected; complete text unavailable despite open-access search. Its possibly stronger unstated results are a priority risk.

[3] Anuj Dawar, Erich Grädel and Matthias Hoelzel, *Convergence and Nonconvergence Laws for Random Expansions of Product Structures* (2020), full-text PDF, https://api.repository.cam.ac.uk/server/api/core/bitstreams/07815c3c-7f3e-4cdc-8e5e-afb88dd574e6/content.

The theorem excludes varying bias, unequal blocks, extra relations and counting quantifiers. The finite checker is corroborative, not exhaustive, and independent verification has not occurred.

Self-review: passed. Independent audit: not yet performed.
