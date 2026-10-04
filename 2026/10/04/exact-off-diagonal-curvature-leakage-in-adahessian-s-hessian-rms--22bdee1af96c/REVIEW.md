# Review

## Correctness

PASS. The proof starts from the exact paper-form Hutchinson coordinate estimator. Rademacher orthogonality gives its first and second moments exactly, independent probe averaging divides only the variance by the probe count, and the bias-corrected Hessian RMS is a convex combination of those squared estimates. The two-dimensional condition-number formula is a complete one-variable extremization and is attained by an explicit eigenspace orientation.

Risk: the exact identity is for a fixed Hessian and the expected square of the RMS state, not for a changing stochastic Hessian or the expectation of the square root itself.

## Originality

PASS. Stochastic diagonal-estimator variance and off-diagonal error are established prior results. The inspected AdaHessian paper uses that estimator inside an RMS momentum but does not state the resulting exact mean-square target, the row-norm identity at one probe, the \(1/m\) leakage law, or the sharp two-dimensional conditioning factor. The claim is therefore restricted to that downstream optimizer-level consequence rather than asserting novelty for Hutchinson variance itself.

Residual risk: an unindexed implementation discussion may have noted the same RMS bias.

## Value

PASS. AdaHessian is specifically designed to use stochastic curvature information as an adaptive preconditioner. The result identifies a precise structural distinction between smoothing the stochastic estimate and removing its variance: temporal RMS momentum preserves off-diagonal variance in its mean-square target, while multiple probes reduce it. The condition-number extremum turns that distinction into a quantitative worst-case diagnostic.

Same-model review: passed. Independent audit: not yet performed.
