# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** For every fixed finite tanh network used by the motivating method, the raw output is smooth and finite at a finite boundary point. Softplus is smooth and strictly positive, and the one-dimensional hard factor \(x(1-x)\) has a simple zero. Therefore the constrained trial is \(a x+O(x^2)\) with \(a>0\), while its second derivative is bounded. The residual is consequently \(-a^{-\alpha}x^{-\alpha}(1+o(1))\); multiplying its square by \(1+\beta\widehat u^{-p}\) gives the exponent \(2\alpha+p\). The codimension-one collar integral is finite exactly when that exponent is below one. The source choice \(p=\alpha\) therefore has the sharp threshold \(\alpha<1/3\), versus \(\alpha<1/2\) for the standard squared residual.

The quasi-uniform-grid laws follow from ordinary harmonic-sum asymptotics. The i.i.d. statement is simply the divergence of the corresponding population integral: finite samples remain finite almost surely, but the one-sample expectation is infinite at and above the threshold. The supplied script evaluates an exactly source-compatible smooth trial and reproduces the predicted logarithmic and power scalings.

Adversarial checks included the possible cancellation in \(-\Delta\widehat u-\widehat u^{-\alpha}\): it cannot occur for a fixed smooth hard trial because \(\Delta\widehat u\) stays bounded whereas \(\widehat u^{-\alpha}\) diverges. The exact solution avoids the obstruction through an unbounded second derivative and the fractional \(d^{2-\alpha}\) boundary correction. The multidimensional extension uses a smooth boundary collar, so the normal distance has a one-dimensional integration measure to leading order; the threshold is independent of ambient dimension for a codimension-one boundary.

## Originality

**PASS, to the best of our knowledge.** The full HTML of arXiv:2609.19335v1 was inspected for the hard Softplus architecture, residual, weighting rule, formal energy, and numerical setup. The paper motivates the weight by giving more importance to points where the predicted solution is small, but no continuum-integrability threshold, fixed-trial resolution law, or boundary-regularity mismatch of this form was located. Repository searches by source identifier, singular-PINN terminology, weighted-residual terminology, and integrability terminology found no prior SCOPE record covering the claim; recent repository changes were also checked for overlap.

The broad principle is not claimed as new. Führer, Heuer, and Karkulik explicitly note that conventional least-squares/minimum-residual methods usually exclude non-square-integrable singular data and study regularized alternatives. Sukumar and Srivastava establish hard boundary factors in PINNs, and Kharazmi, Zhang, and Karniadakis establish variational PINNs. These works delimit the novelty: the present claim is the source-specific interaction of the smooth hard trial, the singular nonlinearity, and the additional inverse-solution weight, yielding the exact \(1/2\) and \(1/3\) thresholds and associated collocation scaling.

The most plausible residual originality risks are the classical singular-elliptic literature and the broader least-squares literature. Crandall–Rabinowitz–Tartar (1977) is cited by the motivating preprint and was not checked line by line here; it may contain sharper boundary regularity results, although it predates PINNs and cannot directly discuss this particular weighting rule. The full 2022 MINRES article and the full 2022 distance-function PINN article were not inspected line by line; their abstracts and relevant public descriptions were checked. They can cover the general norm-selection or hard-boundary principles, but no evidence was found that they imply the specific \(p=\alpha\) weighted-PINN threshold without the calculation given in RESULT.md. The motivating preprint is very recent, so contemporaneous revisions or follow-up comments remain possible.

## Value

**PASS.** The paper's singularity-aware weight is designed to emphasize the boundary-singular region; the theorem shows that, for the stated smooth hard architecture, the same choice changes a logarithmic borderline strong-residual divergence at \(\alpha=1/2\) into an \(N^{1/2}\) fixed-trial growth law and makes the population objective non-integrable already at \(\alpha=1/3\). This is directly relevant to loss scaling, sampling, and interpretation of residual-based validation. The result also points to two mathematically motivated repairs: use a norm/weak formulation compatible with the singular data, or enrich the trial with the fractional boundary term needed to cancel the leading singularity.

## Limitations

The theorem is not a claim that every finite training run fails. It applies to each fixed finite smooth trial and to its continuum or refinement limit; trained parameters can depend on collocation resolution and can develop increasingly sharp derivatives. The multidimensional statement assumes a smooth boundary patch and a simple-zero hard factor. The proposed fractional enrichment cancels only the leading singular term. No end-to-end convergence rate for the trained optimizer is claimed, and no numerical comparison against a weak or enriched method is included.
