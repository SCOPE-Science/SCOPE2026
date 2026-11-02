# Review of exact stroboscopic reversibility in planar OU dynamics

## Correctness — PASS

The stationary covariance is strictly positive by its Lyapunov integral. The finite-lag joint Gaussian covariance is nondegenerate because positive-definite diffusion gives strictly positive innovation covariance. Direct inversion of the forward and swapped \(4\times4\) covariance matrices yields the invariant KL formula; the displayed two-by-two rotated form exposes all terms, not a numerical guess. The Cayley–Hamilton representation treats real distinct, repeated (including defective), and complex-conjugate spectra without unproved diagonalizability assumptions. Positive roots of the sine give exactly the reversible sampled lags; the local Taylor expansion produces a strictly positive quadratic coefficient. The motivating two-agent reduction uses explicitly documented Nash drift entries and small-planning-time expansions.

The verifier extracted from this scientific package calculates the Gaussian KL independently from its closed form and passed 2,120 randomized and boundary assertions. It does not substitute for the analytic proof. A minor interpretive limitation is that pairwise sampled detailed balance and continuous-path thermodynamic reversibility are different objects.

## Originality — PASS (qualified best-knowledge)

Closest published sources: Dey (arXiv:2610.30189v1, Sections 3 and 5) supplies the Nash-induced OU drift and steady-state entropy-production rate but not the observed two-time KL or its zero-lag classification. Nagayama, Kolchinsky and Ito (arXiv:2606.07263, 2026) describe oscillatory/nonnormal decomposition of continuous-time OU dissipation, not the exact sampled two-time Gaussian KL and its quadratic zeros. Bauer, Seifert and van der Meer (arXiv:2412.15642, 2024) already establish general stroboscopic generator non-identifiability for finite-state Markov networks, so aliasing itself is established prior art; they do not state the planar diffusion-wide if-and-only-if zero classification or its invariant KL coefficient. Cisneros, Fakhri and Horowitz (arXiv:2305.16197, 2023) study temporally coarse-grained irreversibility of finite-state chains. Lucente et al. (Phys. Rev. Research 4, 043103, 2022) prove hidden irreversibility for scalar Gaussian projections; the present reversible discrete full-state chain needs an exceptional sampling cadence instead. Related accessible mathematical research results concern OU autocorrelation trends rather than reversal of full two-time probability laws.

Residual risk: the exact Gaussian formula or the zero-set classification might be implicit in earlier stochastic-thermodynamics/linear-systems literature not indexed under these aliases. The novelty assessment is best-knowledge, not exhaustive independent priority certification. The supporting OU dissipation paper was material-inspected in its accessible scholarly text, but a full line-by-line comparison of every appendix was not possible here.

## Value — PASS

The classification answers an operationally motivated question: at exactly which observation cadences can full-state measurements of an irreversible, two-coordinate Gaussian nonequilibrium process produce a perfectly reversible sampled Markov sequence? It identifies a sharp spectral boundary, gives the complete countable zero set or proves its absence, quantifies recoverable arrow-of-time information near zero lags, and applies that phenomenon to a concrete new stochastic game. The finite-lag KL observable is different from steady-state entropy-production rate and has practical import for measurement design and thermodynamic inference. This exceeds an arbitrary parameter substitution or a cheap sign check.

## Scientific limitations

The theorem excludes higher-dimensional OU systems, nonstationary starts, degenerate/noisy partial observations, odd-under-time-reversal coordinates and nonlinear dynamics. The sampled KL is a lower-bound witness, not the true dissipation during unobserved intervals. No global uniqueness claim is made for Nash equilibria, and no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
