# Review

## Correctness

PASS. The two-dimensional calculation reduces the initialization dependence to a single positive row-scaling ratio. The singular-value identity \(K+K^{-1}=\|A\|_F^2/|\det A|\) yields the unique row-equilibrating minimizer and the exact row-correlation floor. The Gaussian theorem uses a fixed null direction of one row to keep a test image bounded while another row grows as \(1/|g_1|\); the nonsingular Gaussian density then gives a logarithmically divergent expectation.

Risk: the infinite-mean theorem applies to the unregularized instantaneous diagnostic, not to a denominator-regularized optimizer update.

## Originality

PASS. The defining Adam-mini paper uses this random instantaneous preconditioner, reports degradation under dense eigenvector rotations, and explicitly identifies a lower-bound characterization as a difficult future direction. The strongest nearby Adam quadratic analysis studies different adaptive dynamics and condition quantities. Classical one-sided scaling theory is broader background and may subsume the deterministic row-equilibration subcalculation, but the inspected sources do not state the Gaussian infinite-mean law or its combination with the exact rotated-spectrum barrier.

Residual risk: an equivalent heavy-tail observation may exist in unindexed notes, and only abstract-level material was available for one general matrix-scaling source.

## Value

PASS. The condition number in question is itself the diagnostic used to motivate reducing Adam's coordinatewise learning rates. Its lack of a finite population mean under the prescribed Gaussian initialization changes how mean-based experiments should be interpreted. The exact two-dimensional orientation floor further gives a concrete mechanism for the reported deterioration as Hessian eigenvectors are rotated away from coordinate alignment.

Same-model review: passed. Independent audit: not yet performed.
