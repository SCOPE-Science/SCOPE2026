# Assessment of the two-probe XTrace diagnostic

## Correctness

PASS. The samplewise equality comes from the equality of the two sketch norms for any diagonal matrix under Rademacher signs. Both leave-one-out estimates reduce to the same expression in the coordinatewise products of the probes. Walsh-pair orthogonality gives the exact error second moment, and a short case analysis gives the necessary and sufficient zero-risk classification. Exact rational enumeration of 7,168 pairs independently checks the formulas in selected dimensions.

## Originality

PASS, qualified. The primary XTrace source states the estimator and its correlated-error diagnostic and supplies an abstract identity (Proposition 3.1) explaining underreporting at positive correlation. It does not identify the perfect samplewise correlation for every diagonal input at two Rademacher probes, nor the complete diagonal Walsh risk formula or zero-risk classification. A later software paper discusses XTrace probes without deriving these special-case identities. The abstract correlation identity is compatible with, but does not produce without further input, the pathological diagonal family. An unidentified earlier specialization remains possible.

## Value

PASS. The exact model is a natural matrix-free trace-estimation baseline, not an arbitrary numerical slice: XTrace with its smallest nontrivial even budget and standard Rademacher probes. Its empirical squared-error indicator is identically zero on an entire positive-definite class where actual error is random, and a one-probe Hutchinson estimator is exact. This directly informs the limitations of empirical leave-one-out error estimates used in adaptive stopping. For dimension at least five the specified budget is smaller than the ambient dimension.

## Closest literature and limits

Epperly–Tropp–Webber, arXiv:2301.07825 (equations (1.4)–(1.6), (3.1), Proposition 3.1 and sections 2.3, 5.6), is closest. Epperly's 2024 discussion of probe distributions and the 2025 traceax paper are supporting comparisons. Scope is strictly the unnormalized two-probe estimator with independent Rademacher probes and real diagonal matrices. The residual-renormalized variant is excluded. Priority needs independent confirmation.

Self-review: passed. Independent audit: not yet performed.
