# Independent mathematical audit

## correctness

PASS

For each scalar quadratic, the Polyak ratio is exactly \(1/(2ca_i)\), so the capped update is \(x^+=(1-r_i)x+r_ib_i\) with \(r_i=\min\{q,a_i\gamma_b\}\) and \(0<r_i\le1\). Synchronous coupling is uniformly contractive, giving a unique stationary law. Its first- and centered second-moment fixed-point equations give the displayed mean and variance exactly. Factoring \(\gamma_b\) from \(r_i\) yields the clipped-curvature surrogate and all phase boundaries. Independent simulation of a mixed-cap example matched the exact stationary moments, and the piecewise formulas were checked algebraically.

## originality

PASS

The defining SPS work gives the capped rule and neighborhood bounds, while Orvieto--Lacoste-Julien--Loizou explicitly derive curvature cancellation only after assuming the cap is large enough to be inactive. No checked source gives the fixed-cap clipped-curvature target, exact invariant variance, or phase thresholds. Those finite-cap statements remain a distinct method-specific classification.

## value

PASS

The cap is a practically meaningful algorithmic parameter, and outside interpolation it changes the stationary target rather than merely limiting step magnitude. The exact clipped-curvature target, bias-variance decomposition, and phase thresholds give a motivated diagnostic benchmark for SPSmax and are more than a routine restatement of its known loose-cap failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
