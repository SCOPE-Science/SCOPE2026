# Self-review

## Correctness — PASS

The source Algorithm 1 and equation (7) lead directly to the stated scalar recurrence with a fixed chi-square-r Hessian denominator. Conditional Gaussian normalization makes \(Z\) standard normal and independent of that denominator and of all additional Gaussian rows. Each strictly larger gradient sketch contributes a positive excess quadratic mass, making the leading coefficient of the degree-\(t\) inverse-denominator polynomial nonzero. The remaining response-noise polynomial is lower by a square-root power; a positive-probability compact conditioning event prevents cancellation. This establishes the strict, sharp \(r>p(2t+1)\) criterion. Exact inverse-chi-square identities yield the displayed one-step expectation. The standalone verifier checks the source recurrence, the polynomial identities and the rational one-step expectation from the actual file contents.

Scientific limitation: this is a finite-dimensional scalar instance and a moment criterion, not a convergence theorem for every least-squares problem.

## Originality — PASS

The defining IDS paper has the same Gaussian nested construction, but its theorem concerns asymptotic conditional risk or a separate efficiently structured sketch family. Classical iterative Hessian sketch analysis generally fixes the full gradient and establishes high-probability embeddings; work on refreshed IHS computes expected rates under different independence and initialization assumptions. The exact source-initialized nested-Gaussian all-moment clock, including its \(4t+2\) mean-square threshold, was not found in the inspected primary results or focused indexed searches. Closest alternative proof settings do not imply this correlated-source statement.

Residual risk: an unindexed source may already have quantified the same inverse-chi-square polynomial effect; absence from indexed searches alone does not certify novelty.

## Value — PASS

The theorem identifies a sharp and unexpectedly stringent finite-width robustness requirement for an algorithm intended to reduce gradient-sketch cost. It distinguishes almost-sure invertibility and high-probability correctness from existence of unconditional error moments, and quantifies the additional random-inverse power incurred by each step. Finite gradient oversampling cannot change the threshold unless the scheme leaves the finite-prefix Gaussian setting. The witness is strongly convex with unit condition number, isolating an intrinsic sketch-related mechanism.

Self-review: passed. Independent audit: not yet performed.
