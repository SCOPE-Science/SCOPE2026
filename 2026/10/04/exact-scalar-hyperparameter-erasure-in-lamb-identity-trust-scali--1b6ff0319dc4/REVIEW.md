# Review

## Correctness

PASS. In one dimension with zero weight decay and \(\phi(z)=z\), the normalized update uses only the sign of the Adam-like direction. Under \(x f'(x)>0\) and \(0<\eta_t<1\), the iterate sign is invariant, so every gradient and first moment has the same sign. The exact recurrence \(x_{t+1}=(1-\eta_t)x_t\) follows for all iterations, independently of moment magnitudes.

## Originality

PASS. The defining paper states that layer normalization ignores update magnitude and discusses \(\phi(z)=z\), but its inspected algorithm and theorem do not state the complete scalar trajectory or the resulting erasure of all Adam magnitude hyperparameters. The trust-ratio-clipping follow-up studies extreme ratios rather than this exact sign-invariant law. Focused published-record searches over scalar LAMB, quadratics, trust ratios, curvature cancellation, and fixed-point dynamics found no covering statement.

Residual risk: the cancellation may have appeared informally in implementation notes or optimizer discussions.

## Value

PASS. The trust ratio is LAMB's defining mechanism. The theorem isolates an exact consequence of that mechanism: on scalar sign-coherent problems, the layer normalization removes all magnitude information produced by the Adam base method. The quadratic corollary is an exact curvature-erasure benchmark, while the scope conditions identify why clipping, crossings, weight decay, and multidimensional direction changes restore dependence.

Same-model review: passed. Independent audit: not yet performed.
