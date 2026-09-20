# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The core argument uses exact identities from the source ODEs. The surviving fraction satisfies \(S'= -\mu h-\delta i\le-\min(\mu,\delta)S\), so healthy-plus-ill mass decays exponentially. An integrating factor then gives the provisioning variable exactly as the sum of an exponentially deteriorating initial stock and a convolution with the consumption rate. At the first positive-threshold crossing this yields an exact clock identity, and the consumption convolution vanishes in the large-buffer limit because the crossing time diverges. This proves the additive-sharp logarithmic asymptotic for \(\rho>0\).

For \(\rho=0\), the same survival estimate bounds total lifetime consumption by \(c_+/m\), giving the stated no-crossing region. When \(p_0\to\infty\), provisioning stays uniformly large, so the illness rate converges uniformly to its baseline value \(\alpha\); dominated convergence is justified by the same exponential survival bound. Integrating the limiting two-compartment linear system gives the explicit constant \(J_\alpha\). The matrix-inverse formula was checked symbolically, and direct numerical integration with the source-paper parameters confirms both limiting regimes.

Potential failure modes were checked. The clipping rule at \(p=0\) is irrelevant because all arguments stop at a fixed positive threshold, and in the large-buffer \(\rho=0\) regime the stock stays positive. Threshold uniqueness follows from strict monotonicity of \(p\) while \(p>0\). The asymptotic statement is not inferred from a timeout or finite numerical window.

## Originality

**PASS, to the best of current knowledge.** The novelty claim is deliberately source-specific. Standard integrating-factor formulas, comparison estimates, and compartmental matrix inverses are not claimed as new mathematics. The new claim is that, for the exact model introduced in arXiv:2609.20430v1, the paper's critical provisioning time has a logarithmic large-buffer law whenever \(\rho>0\), while its auxiliary \(\rho=0\) limit has finite total consumptive depletion and eventually no threshold crossing; the explicit high-buffer consumption constant is also given.

The source paper was inspected in full around the model definition and the critical-time discussion. It explicitly motivates \(t_c\propto p_0-p_c\) by neglecting \(\rho\) and freezing the health fractions, and reports approximate linearity only over \(t_c\le120\) days. Searches by arXiv identifier, exact title, critical-provisioning terminology, resource-coupled terminology, and logarithmic-threshold variants found only the source paper and secondary summaries, not these asymptotic statements. The related 2025 historical-resource model by the same author was checked at the abstract level and does not concern this provisioning ODE.

No inaccessible paper was identified as specifically likely to overturn this narrow source-specific claim. Residual risk remains that an unindexed comment, author revision, or mathematically equivalent observation elsewhere could contain the same elementary asymptotic mechanism.

## Value

**PASS.** The result changes the interpretation of one of the source paper's main scaling observations. It separates a finite-window approximately linear regime from the actual large-buffer asymptotic of the full model, and shows that the very simplification used to motivate linearity produces a qualitatively different global behavior once mortality is allowed to act for arbitrarily long times. The dichotomy between direct stock deterioration and population-mediated consumption is simple, exact, and reusable in related resource-population models.

## Limitations

The result applies only to the deterministic ODE model and fixed positive stress thresholds. It does not assess historical fidelity, parameter calibration, heterogeneous crews, stochastic shocks, or resupply. It does not provide a closed form for the intermediate-buffer crossover and does not claim the source paper's finite-window numerical observations are incorrect; rather, it identifies their non-asymptotic character.
