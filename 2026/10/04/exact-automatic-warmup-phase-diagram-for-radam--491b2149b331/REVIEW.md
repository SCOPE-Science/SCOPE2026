# Review

## Correctness

PASS. The published RAdam statistic is treated symbolically: time monotonicity is strict, the source gate reduces to a polynomial inequality with a unique positive root, and those roots partition all \(\beta_2>0.6\) into exact first-activation indices. The asymptotic follows from an exact root-displacement equation.

Risk: software variants with a gate other than \(\rho_t>4\) are outside the theorem.

## Originality

PASS. The defining source gives the effective-length formula, strict gate, qualitative automatic warmup, and the \(\beta_2\le0.6\) degeneration. The inspected paper and project documentation do not state the activation-index partition, threshold polynomials, or their exponential accumulation. Focused published-record searches did not identify an implication-equivalent result.

Residual risk: an unindexed implementation discussion may contain partial activation tables.

## Value

PASS. Automatic warmup is central to RAdam's motivation. The exact phase diagram explains when the familiar short unadapted phase is guaranteed, when extra steps appear, and why the phase can become arbitrarily long near the method's degeneracy threshold.

Same-model review: passed. Independent audit: not yet performed.
