# Scientific review: rare-event optimal sampling for affine least squares

## Correctness

**PASS.** The exact inverse-Gram expression reduces the chosen risk to a positive quadratic in the sample mean divided by the sample scatter, plus a constant. Orthogonal mean/scatter coordinates have Jacobian \(\sqrt m\); the rare event becomes a shrinking ball of dimension \(m-1\). Dominated convergence, a positive finite volume integral, and the layer-cake identity establish the exact coefficient and moment threshold. Hölder's equality case proves the unique minimizing continuous density for every sample size. The supplied exact-rational and deterministic-quadrature checker passed 1,528 tests; infinite claims follow from the proof rather than empirical checks.

## Originality

**PASS, subject to the stated residual risk.** The complete numerical-approximation and random-design sources inspected concern distinct sampling distributions, nonasymptotic error bounds, or generic lower-tail inequalities. The closest mathematical neighboring cases use unit-length angular observation rows and beta-distributed affine regression: the former does not give the variable-length affine inverse-Gram coefficient, and the latter's moment threshold does not give a globally optimal sampling density. Neither statement implies the universal fixed-loss \(m\)-independent optimizer claimed here. No exact same mathematical model theorem or stronger implication was identified in the searches. Specialized small-scatter and experimental-design literature remains a publication-priority risk; failed searches are not proof of absolute novelty.

## Value

**PASS.** Conditioning catastrophes occur in iid numerical least squares because sample sites can nearly coincide. This theorem gives their precise probability scale and identifies the unique way to suppress the leading tail among continuous independent-input designs. The optimal density remains unchanged as the sample budget varies, even when the moment-existence threshold changes. For \(m=4\) and a wide interval, the improvement in the leading catastrophic-risk coefficient over uniform sampling is nearly sevenfold. This exact and naturally motivated design objective is distinct from mean-risk or whole-distribution optimality.

## Closest literature and limitations

The closest external full texts checked were Chkifa--Dolbeault (arXiv:2306.07435), Mourtada (arXiv:1912.10754), and Dereziński--Clarkson--Mahoney--Warmuth (PMLR 99, 2019). They are not claimed to be exhaustive. This result applies only to continuous iid unweighted affine designs, a fixed positive-definite loss matrix and an asymptotic rare-event objective; no independent scientific audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
