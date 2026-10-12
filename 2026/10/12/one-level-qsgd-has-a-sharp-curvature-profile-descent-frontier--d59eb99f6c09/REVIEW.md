# Review

## Correctness

PASS. The source \(s=1\) quantizer reduces coordinatewise to Bernoulli stochastic rounding with exact second moment \(\|g\|_2|g_i|\). Substitution into the diagonal quadratic gives the conditional expected-objective identity without approximation. Cauchy--Schwarz is sharp and gives both the exact universal frontier and its attaining state. The isotropic minimax factor follows from the sharp \(\ell_1/\ell_2\) inequality.

Scientific risk: the result is an expected-objective statement, not an almost-sure descent theorem.

## Originality

PASS. The defining source gives unbiasedness and a dimension-only variance bound. General scalar compressed-gradient theory can recover the isotropic square-root-dimension scale, so that component is explicitly treated as prior-compatible. The surviving claim is the exact anisotropic curvature-profile threshold, its equality direction, and the exact objective identity. Matrix-smooth fixed-sketch theory uses a different compressor model and does not directly imply the state-dependent QSGD result.

Residual risk: an unindexed specialization of QSGD may contain the same diagonal calculation.

## Value

PASS. The curvature-profile frontier distinguishes the actual stability tax of aggressive QSGD from a generic worst-curvature dimension bound and can be substantially less conservative on anisotropic problems. It also identifies a concrete dense direction on which an otherwise exact gradient-descent step becomes unstable in expectation.

Self-review: passed. Independent audit: not yet performed.
