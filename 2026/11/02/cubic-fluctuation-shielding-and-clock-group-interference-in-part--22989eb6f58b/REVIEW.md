# Review: cubic fluctuation shielding under grouped subsystem resetting

## Correctness — PASS

The claim is confined to finite connected weighted undirected graphs, exact real-valued harmonic drift, at least one reset and at least one unreset node, independent rate-\(r\) Poisson clocks assigned to a partition of reset nodes, and fixed frequencies. The synchronous-coupling quadratic generator has strictly positive damping \(2A+rP\), giving a unique invariant law with finite second moments. The first moment satisfies \((A+rP)\mu=\omega\) independently of group partition. The exact covariance generator gives the stated jump-dependent Lyapunov system without neglecting shared-clock effects. In the high-rate expansion, its reset-set, cross, and unreset blocks successively yield \(D\), \(-BD\), and the uniquely solvable grounded-Laplacian Sylvester equation; invertibility at zero perturbation justifies \(O(r^{-4})\). An exact opposite-frequency star construction exhibits invariant zero center position under a shared clock; an independent-clock rational covariance calculation gives the strictly positive formula. A self-contained rational solver reconstructs these facts in finite test cases. Residual limitation: finite checks are not a proof of the matrix limit, which is supported instead by the written analytic argument.

## Originality — PASS (best-knowledge, qualified)

Paramero-Arias–Riascos, arXiv:2610.21842v1, develops subsystem reset-induced synchronization and the high-rate grounded-Laplacian mean-field limit, but does not provide a grouped-clock stationary fluctuation Gramian or an exact cancellation/reversal example in the studied main text. General piecewise-deterministic moment closures already exist (Soltani–Singh, arXiv:1711.04884, and their 2019 renewal-transitions article); this work does **not** claim the moment closure, the grounded Laplacian, or reset-created correlations as new. It claims the graph-specific leading cubic covariance, exact grouping-dependent nonzero criterion, and strict finite-rate cancellation on a physical three-node network. Targeted record and primary-literature searches found no explicit equivalent. The most material residual risk is that the general moment-framework full text, not fully retrievable for inspection, could imply some graph-specific formulas via an unstated specialization. Originality is not an independently certified priority claim.

## Value — PASS

Finite resetting in a partly pinned oscillator network may give the same deterministic mean for differently correlated reset protocols but sharply different stationary fluctuations. The cubic law and exact Gramian quantify how strongly stochastic reset perturbations penetrate never-reset nodes; groupwise cancellation is a strong design contrast, not a cosmetic parameter shift. The exact star shows zero variance for one clock versus strictly positive for independent clocks, and reversal for aligned frequencies. This addresses stochastic robustness beyond the fast-rate synchronization mean limit. The model remains a linearized rather than fully nonlinear phase-network result.

## Closest literature and risks

* Paramero-Arias and Riascos, *Synchronization induced by stochastic subsystem resetting in complex networks*, arXiv:2610.21842v1; the publicly accessible main-text rendering was inspected for reset mechanism, fast-rate grounded limit, and finite-rate discussion.
* Soltani and Singh, *Linear piecewise-deterministic Markov processes with families of random discrete events*, arXiv:1711.04884; abstract and indexed metadata inspected; full text could not be reliably retrieved through attempted open-access and institutional routes. General exact moments are already prior art; partial coverage of our specialization remains possible.
* Soltani and Singh, *Moment Analysis of Linear Time-Varying Dynamical Systems with Renewal Transitions*, SIAM J. Control Optim. 57 (2019), DOI:10.1137/17M118351X; abstract inspected, general moment theory acknowledged.
* Bressloff, *Kuramoto model with stochastic resetting and coupling through an external medium*, arXiv:2411.15534; distinct globally reset coupling geometry.

Self-review: passed. Independent audit: not yet performed.
