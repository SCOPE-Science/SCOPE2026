# Self-review

## Correctness
PASS. The fixed-step criterion follows from an exact entrywise square of \(I-sA\). The adaptive statement follows from a two-mode asymptotic expansion around the positive Perron eigenvector, with the non-Perron mode surviving at first order while the Perron mode is suppressed. The exact witness and radical signs are replayed by `verify.py`.

## Originality
PASS. The primary SqS3 paper already documents that unsafeguarded runs can violate parameter constraints; that general observation is not the claim here. The inspected literature did not state the exact \(s\le2/\operatorname{tr}(I-J)\) cone boundary or prove generic completed-cycle sign loss near the Perron ray for positive symmetric affine contractions. The closest semantic-database record concerns scalar Aitken--Steffensen robustness, not matrix cone invariance. Residual risk remains from older vector-extrapolation terminology.

## Value
PASS. The result converts a qualitative safeguard concern into a sharp structural criterion on the smallest coupled positive model. It explains why positivity of the base fixed-point map does not transfer automatically to squared acceleration and pinpoints a mechanism that feasibility-aware implementations can test or guard against.

## Closest literature and limitations
Varadhan--Roland (2008) supplies SqS3 and globalization; Roland--Varadhan--Frangakis (2007) supplies the preceding squared-polynomial framework. The finding is limited to exact arithmetic, two-dimensional symmetric strictly positive affine contractions, and unsafeguarded SqS3; it does not classify nonsymmetric or higher-dimensional maps.

Self-review: passed. Independent audit: not yet performed.
