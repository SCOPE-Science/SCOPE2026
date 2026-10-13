# Review: No triple global mode in the first eight Poisson orders

## Correctness

**PASS.** For \(2\le k\le8\), the coefficient recurrence bounds every modal index by \(\lambda k(k+1)/2\); at \(\lambda\le2\), this gives indices no larger than \(k(k+1)\). The exact integer-to-prime reduction and Gauss-lemma argument in RESULT.md establish that every triple of candidate masses is distinct for positive intensity except for possible pair ties, via \(109943\) exhaustive gcd comparisons. Only the triple \((1,3,4)\) has a nonconstant gcd in characteristic \(1000003\), and its exact common nonzero root is negative. At larger intensities an existing strict compound-Poisson log-concavity theorem applies. No infinite claim is inferred solely from finite experiments.

## Originality

**PASS, with residual priority risk.** Mane’s 2023 preprint expressly calls triple joint modes an open question and offers numerical evidence. Kwon–Philippou rigorously locate some modes for orders \(3,4\) at low intensity, tabulating other cases approximately; Georghiou–Philippou–Saghafi provide bounds and integer-rate uniqueness for orders \(2\) to \(5\); Johnson–Kontoyiannis–Madiman cover the high-rate region. None of these inspected statements proves the complete low-rate algebraic exclusion through order \(8\). Search records were also compared using the stuttering-Poisson and uniform-jump-compound-Poisson aliases. An unlocated equivalent earlier result remains possible.

## Value

**PASS.** A precise universal statement for each of the first eight orders rigorously advances an explicit mode-multiplicity problem. Exact, reproducible algebraic certification rules out isolated real-parameter triple ties that plots and grids cannot, while respecting the pre-existing high-rate theorem. The result does not extend to all orders or classify double-mode locations.

Self-review: passed. Independent audit: not yet performed.
