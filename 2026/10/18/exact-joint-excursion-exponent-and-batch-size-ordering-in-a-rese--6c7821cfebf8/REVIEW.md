# Scientific review: exact joint-excursion law for uniform batch resetting

## Correctness — PASS

The Poisson marks give a joint backward-age survival law with intensity \(r\phi_J\). Convexity and symmetry yield the sharp equal-age lower bound \(\phi_J\ge(q_j/j)\sum t_i\), and decreasing increments of \(q_j\) imply the common constant \(r q_k/k\). Product-exponential integral identities establish the precise age-sum moment domain, with divergence at the boundary. Conditional independent Gaussian tail bounds and a matched equal-age event give the same rate \(\sqrt{r k q_k/D}\). The exact falling-factorial sum proves strict ordering of the marginal-normalized rate across batches. The independent symbolic/counting checks and numerical two-particle quadratures in `verify.py` support, but do not replace, this proof.

## Originality — PASS, subject to residual risk

The nearest primary work (de Mauro, Majumdar and Schehr, arXiv:2601.20077) gives exact marginals and nonmonotonic covariance versus batch size; its main and supplemental materials were inspected. It does not state the sharp all-\(k\) absolute co-excursion logarithmic rate, its age-sum moment threshold or their strict normalized batch-size ordering. The full-synchronization mixture of arXiv:2509.06658 and the independent/extremal resetting model of arXiv:2205.10273 do not cover uniform intermediate batch sizes. Searches examined equivalent joint extremes, shock-age moment thresholds, generic density recurrences, stronger stationary laws and possible exact tables. The source's general Fourier closure is broader distributional machinery and could conceal an unstated implication; general shock-model asymptotics also remain an explicit originality risk. Search absence is not novelty proof.

## Value — PASS

The theorem identifies a nontrivial quantitative measure of simultaneous many-particle spatial extremes that varies monotonically with reset synchrony even though covariance amplitude need not. The complete integer-batch comparison and exact structural moment boundary address a physically motivated asymptotic beyond a routine rescaling of the source's two-point covariance. The result is confined to finite fixed particle number and the logarithmic rare-tail rate; no claim is made for pre-exponential factors or growing-\(N\) limits.

Self-review: passed. Independent audit: not yet performed.
