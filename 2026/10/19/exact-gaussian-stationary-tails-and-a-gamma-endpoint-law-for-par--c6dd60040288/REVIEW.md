# Scientific review

**Correctness — PASS.** The stationary Gaussian scale mixture follows from a two-sided stochastic convolution and the contractive jump flow. Poisson backward recurrence time gives the exact deficit law \(\Pr(1-U<z)=Kz^\alpha\) on the stated nontrivial interval. The invariant variance-generator recurrence fixes \(K\) as an absolutely convergent series. Controlled Laplace asymptotics prove the Gaussian-density prefactor and the Gamma conditional limit. The supplied independent moment/quad checks support—but do not establish—the infinite limits.

**Originality — PASS, with residual risk.** The 2026 diffusion approximation of Galla and its stationary approximating density are prior work. The accepted theorem instead quantifies the exact finite-contraction Poisson process at extreme positions. Olsen–Gupta provide harmonic-potential second moments; Pierce gives a constant-advection proportional reset solution; Trajanovski et al. give full-reset OU theory. Inspected source statements do not include the displayed exact endpoint constant or Gamma localization. General Gaussian mixture asymptotics may implicitly encompass the final analytic step, and broader jump-process literature may contain an unstated special case.

**Value — PASS.** The sharp rare-event density prefactor and the conditional mechanism distinguish extreme displacements from typical fluctuations. The exact jump process has finite moments of every order, unlike the power-law far-tail diffusion approximation for finite small-reset parameter. This supplies a directly interpretable validity boundary for a physically motivated approximation.

**Scope and limitations.** The scalar centered model uses constant-rate Poisson contractions with \(\kappa,D,r>0\), \(0\le a<1\). No joint small-reset/far-position uniform expansion, random contraction strengths, or higher-dimensional result is asserted. The identified mathematical derivation has not been independently audited.

Self-review: passed. Independent audit: not yet performed.
