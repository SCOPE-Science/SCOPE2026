# Review: exact factorization-delay law for Cohen's R-transform

## Correctness — PASS

The change of coordinates \(\psi(x)=(x+1)/(x-1)\) conjugates the root-preimage map to squaring, so each irreducible input polynomial has a well-defined two-adic order level. For degree at least two, the preimages either form an irreducible degree-doubling transform or two distinct irreducible factors of the original degree. Their valuation evolution is deterministic off the periodic level, where a fair branch choice creates an exact geometric number of retries. Möbius inversion yields the exact-degree counts, and the field-level expected-value sum yields the mean formula. The odd/even distinction follows from valuations of odd powers and a strictly positive exact-degree count. Independent small-field polynomial factorization and prime-power integer checks corroborate each step; enumeration is not substituted for the proof.

## Originality — PASS, with residual historical-priority risk

Ugolini (arXiv:1207.6959v1, Theorems 2.8 and 3.1) already provides the factorization dichotomy and a deterministic construction; Ugolini (arXiv:1304.3283v1, Theorem 2.6) gives the full-field reversed-tree depth counts. Bassa and Menares (arXiv:1909.02608v1) develop the power-map conjugacy more generally. None of the inspected material states the uniform exact-degree, independently randomized branching law, its probability generating function, or the exact odd/even expectation dichotomy. The claimed novelty is this ensemble-specific arithmetic distribution, **not** the graph structure or the basic transform. A prior implicit specialization or unlocated stochastic application remains a residual priority risk; semantic searches do not prove uniqueness.

## Mathematical value — PASS

The number of factorizations before the first doubled-degree irreducible polynomial is a direct measure of the overhead of a standard constructive finite-field procedure. Its complete distribution across the canonical uniform irreducible input ensemble and a declared fair branch policy is a natural arithmetic-probabilistic statistic. The finite divisor formula and exact parity-dependent expectation supply a quantitative average-case complement to the older worst-case depth bounds. This is more informative than a routine change of notation or a small computation.

## Checks and limits

Relevant full-text sections of the two Ugolini arXiv preprints were inspected, including the factorization theorem and the reversed-tree theorem. The Bassa–Menares preprint and accessible publisher text were compared for stronger transformations. No source located a direct distributional result; specialist literature could still contain equivalent formulas. The factorization verifier covers nine prime-field parameter pairs and exact arithmetic over additional proper prime-power fields; no infinite claim rests on the finite sample. The result does not concern software timing or infinite stability after first doubling.

Self-review: passed. Independent audit: not yet performed.
