# Same-model review

## Correctness
PASS. The source's scalar constant-momentum quadratic recurrence specializes exactly at \(\lambda/L=5/8\) and \(\beta=1/3\) to \(x^{k+1}=\tfrac12x^k-\tfrac18x^{k-1}\), with \(x^1=3x^0/8\). Its roots are \((1\pm i)/4\), so the four-step scaling \(x^{k+4}=-x^k/64\) is exact. The first block gives magnitude ratios \(3/8,1/6,1/4,1\); hence the quadratic objective never strictly rises. The scalar gradient-restart sign is exactly the sign of \(x^{k+1}(x^{k+1}-x^k)\), which first becomes positive for the update producing \(x^3\). Exact-arithmetic replay agrees.

## Originality
PASS with stated residual risk. O'Donoghue--Candes analyze the same constant-momentum model but explicitly make phase/frequency approximations and say that either adaptive rule is expected to trigger after approximately one quarter period; they do not state this exact resonant blind spot. Fercoq--Qu later report that an adaptive restart condition can fail to occur for more than 10,000 iterations and therefore use bounded/forced restart intervals, but the inspected material does not derive the one-dimensional closed-form mechanism here. Targeted published-finding corpus searches found no implication-equivalent item; the closest indexed Nesterov result concerns three-dimensional objective spikes rather than a scalar monotone under-damped orbit.

Residual risk: an implementation note, thesis, lecture note, or unindexed discussion may contain this exact \(\lambda/L=5/8\), \(\beta=1/3\) resonance or an equivalent rational-phase construction.

## Value
PASS. Function-based and gradient-based restart are widely presented as comparable oscillation detectors. This exact one-dimensional strongly convex quadratic shows a structural distinction at the simplest possible level: strict objective increase can be completely blind to a genuinely oscillatory under-damped mode, while the gradient detector fires immediately after the sign crossing. It also supplies a concrete mechanism consistent with later empirical observations that adaptive conditions can fail to activate, and it identifies strict-versus-nonstrict comparison as a mathematically relevant implementation boundary.

Same-model review: passed. Independent audit: not yet performed.
