# Scientific review

## Correctness

PASS. Gap encoding is bijective because the binary following-symbol condition is vacuous and the final-symbol condition forces a terminal one. The Burnside count handles periodic rotations. The leading error analysis separates double maximum ties from higher ties, uses a finite binomial inclusion-exclusion sum with its correct beta-integral coefficient, and shows all nonidentity rotations contribute below the main order. Direct source-definition enumeration and an independently implemented gap-orbit census agree on the finite test range. Asymptotic claims are proved symbolically, not inferred from tests.

## Originality

PASS under best available literature evidence. The 2026 primary paper introduces quasinecklaces and proves a general constant-factor candidate bound with a recurrence for unrestricted counts, but does not state the exact fixed-content formula or sharp first-order ratio. The 2017 pseudo-necklace generator addresses a different, smaller auxiliary language, and the older fixed-density necklace generator does not count quasinecklace false positives. Search coverage is not a proof of absolute publication priority; unindexed equivalent enumerations remain a residual risk.

## Value

PASS. Fixed-content generation is an explicit application of the new quasinecklace algorithm. The result replaces a constant-factor candidate guarantee by an asymptotically exact ratio, determines the leading correction, and identifies the precise first fixed-content obstruction at three ones. It quantifies avoidable candidate tests in a natural algorithmic enumeration problem; it does not assert a total-runtime improvement.

## Scope and evidence

The proof applies to all positive fixed ones counts in the exact formulas, and to each fixed count at least three in the asymptotic formula; binary alphabets only. The checker corroborates finite inputs. Relevant primary sources and their distinction are documented in `RESULT.md` and `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
