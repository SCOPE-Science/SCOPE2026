# Review

## Correctness

PASS. On each sampled scalar quadratic, the Polyak ratio is exactly \(1/(2ca_i)\), so the bounded SPS update is the affine contraction
\[
x^+=(1-r_i)x+r_i b_i,
\qquad
r_i=\min\{1/(2c),a_i\gamma_b\}.
\]
For \(c\ge1/2\), every map is nonexpansive and the finite family is uniformly contractive because every \(r_i>0\). The invariant mean and variance follow from the exact affine fixed-point equations. The all-capped, mixed, and all-uncapped regimes are direct substitutions, and the two-component phase boundaries match continuously.

Risk: the multidimensional case does not reduce to scalar clipped curvature weights unless additional commutativity structure is imposed.

## Originality

PASS. The original SPS paper defines the cap and proves convergence to a neighborhood but does not identify its exact target on heterogeneous quadratics. Later SPS-dynamics work already establishes curvature cancellation and convergence toward the unweighted average of component minimizers in a loose-cap, decreasing-step quadratic regime; that fact is explicitly treated as prior coverage here. Crucially, its counterexample assumes the cap is large enough to be inactive. The inspected literature does not state the fixed-cap stationary target
\[
m=\frac{\sum_i\min(q,a_i\gamma_b)b_i}{\sum_i\min(q,a_i\gamma_b)}
\]
or the corresponding stationary variance and cap thresholds.

Residual risk: an equivalent affine-iteration calculation may appear in stochastic-approximation literature without SPS terminology.

## Value

PASS. The cap is a defining parameter of \(\mathrm{SPS}_{\max}\) and is described in the literature as both a safeguard and a quantity that needs tuning outside interpolation. The result gives that tuning parameter a precise structural meaning: it clips component curvature in the long-run target. This separates a bias mechanism from ordinary sampling variance and shows exactly when the cap preserves the intended objective, when it solves a clipped surrogate, and when it loses curvature information completely.

Same-model review: passed. Independent audit: not yet performed.
