# Scientific assessment: complete nearest-neighbor covariance sign phase diagram

## Correctness — PASS

The theorem specifies an actual finite-state-space continuous-mass Markov process on the unit simplex, with rate-one adjacent-edge clocks and Beta redistribution \(\operatorname{Beta}(t,pt)\), \(\operatorname{Beta}(t,qt)\), for all real \(p,q,t>0\). Existence follows from compact Feller dynamics; uniqueness follows from two-step synchronous coupling with contraction constant \(1/2+1/[4(1+p)]+q/[4(1+q)]<1\). The generator gives exactly closed first- and second-moment equations. Substitution yields the full all-parameter \((0,1)\)-covariance identity with positive denominator; the affine numerator and a one-positive-root quadratic prove the complete sharp phase diagram. The selected \(p=4,q=2\) matrix is additionally reconstructed in full and shown consistent with mass conservation. A pure-standard-library multivariate polynomial certificate checked the global algebraic identity, and a separate rational-function checker passed 103 assertions for the complete special matrix. Neither finite simulations nor samples are treated as an infinite-parameter proof.

## Originality — PASS (qualified best-knowledge)

Giusfredi–Avena–Politi (arXiv:2610.21777v1) define precisely the general asymmetric bondwise Beta exchange generator and establish its stationary first moments. They explicitly identify the joint stationary mass law and second moments as more difficult and handle small systems numerically; neither their full text nor appendices give an explicit \((p,q,t)\) covariance sign phase diagram at fixed means. Their binary-swapped Sinai ensemble is a narrower specialization, distinct from the unrestricted two-bond biases here. Giardinà–Redig–van Tol (2025) study generalized KMP with symmetric bondwise Beta laws, homogeneous reversible product measures and reservoir-driven mixing. Carinci et al. (2024) independently establish positive association for boundary-driven harmonic systems, so positive covariance itself is known and credited. The current fixed-total-mass, incompatible-beta, fixed-mean sign-transition criterion does not follow directly from either article. Capanna–Gabrielli–Tsagkarogiannis (2023/2024) study reversible gradient dynamics and boundary-drive solvability. Indexed research-record and accessible prior-claim searches found no statement covering the precise all-positive-parameter classification.

Residual priority risks: generic higher-moment frameworks may yield the formula by an unlocated reduction; the complete text of Gilbert (arXiv:1703.01240) was inaccessible, so abstract-only comparisons cannot conclusively exclude it. The originality verdict is best-knowledge, not a proof of worldwide first publication.

## Value — PASS

The source literature identifies an important gap between the exactly solvable stationary mean profile and the joint stationary fluctuation law of heterogeneous exchange dynamics. The theorem gives a **complete two-dimensional bias phase boundary** for an otherwise uninformative fixed mean profile, demonstrates a sharp correlation sign reversal under changing noise concentration alone, and identifies the smallest nontrivial strictly conservative system in which the effect can occur. The explicit threshold \(p_c(q)\), all-parameter formula, and the integer-bias exact covariance matrix are natural quantitative benchmarks for more general invariant-state questions and stochastic numerical studies. The value does not depend on an unsupported large-volume theorem or on presenting mere algebraic computation as an intrinsically important fact.

## Closest literature and limitations

Giusfredi–Avena–Politi, arXiv:2610.21777v1 (15 October 2026), https://arxiv.org/html/2610.21777v1 ; Giardinà–Redig–van Tol, *J. Stat. Phys.* 192, 21 (2025), https://doi.org/10.1007/s10955-025-03393-1 ; Carinci et al., *J. Stat. Phys.* 191, 10 (2024), https://doi.org/10.1007/s10955-023-03226-z ; Capanna–Gabrielli–Tsagkarogiannis, arXiv:2309.14836; Gilbert, arXiv:1703.01240 (abstract only, full text unavailable).

The structural phase diagram concerns only a three-site closed chain with shared Beta concentration scaling and equal edge rates; the full covariance matrix and negativity of both remaining off-diagonal covariances are claimed only for \(p=4,q=2\). No arbitrary-graph, higher-moment, infinite-volume or complete invariant-density result is asserted. Independent mathematical and publication-priority audits have not been performed.

Self-review: passed. Independent audit: not yet performed.
