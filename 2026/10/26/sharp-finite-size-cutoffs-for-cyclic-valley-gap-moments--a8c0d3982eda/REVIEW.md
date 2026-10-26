# Scientific review

## Correctness

PASS. For all positive gap indices, the one-site probability is computed separately at the one-guard-identification boundary and above it; the resulting integral evaluates to the stated rational closed form. At the covariance boundary, opposite offsets collapse into a single antipodal pair. Replacing two linear-window covariance terms with the cyclic term yields precisely \(w_i-2v_i+a_i^2\). Conditional integration of two long excursions and their short outward guards gives the Brownian-bridge factorization. Strict positivity follows from injectivity and dense range of the Brownian-bridge covariance operator. No finite enumeration is used as proof of a universal claim. The accompanying code independently exercises exact finite cases.

## Originality

PASS with residual risk. Matijasevick's Theorem A and Remark 3.2 supply the eventual thresholds but report that their optimality was checked only for finite ranges of indices. The present exact first-below-threshold formulas and an analytic all-index strictness argument are not stated there. The earlier Mansour–Rastegar–Roitershtein study treats selected gap lengths, while Ehrenborg's weighted cyclic pattern trace theorem treats general enumerations without identifying this variance correction. Literature might contain an implicit equivalent via general transfer operators; this remains a risk rather than a claim of exhaustive novelty.

## Mathematical value

PASS. The smallest sizes at which the previously known exact-linear moment laws begin are natural finite-sample invariants of the root-gap model. The result settles both sharpness questions uniformly in gap length, replacing bounded-index checks by an exact structural explanation. The positive Brownian-bridge quadratic form is a reusable analytic mechanism for cyclic covariance-boundary corrections, rather than a merely numerical extension.

## Scope and status

The findings depend on the iid homogeneous priority representation, the cited excursion-kernel calculation and the published eventual variance coefficient. Cases below the immediately preceding variance size, inhomogeneous clocks and joint gap moments are not resolved. Equivalent results may exist in broader weighted-pattern operator literature.

Self-review: passed. Independent audit: not yet performed.
