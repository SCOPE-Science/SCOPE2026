# Scientific assessment

## Correctness — PASS
Direct multiplication of \(T_bT_a\) and \(T_aT_b\) gives the same trace \(1+\beta^2-(1+\beta)(a+b)\eta+ab\eta^2\) and determinant \(\beta^2\). The quadratic Schur inequalities give the complete frozen-order stability set; the exact discriminant and root ordering distinguish connected, one-point-neutral, and disconnected regimes. For \(0<\beta<1\), the determinant bound \(\rho\ge\beta\) is attained precisely for \(|\tau|\le2\beta\), proving both sharp optimal-rate bands. For \(a=1,b=10,\beta=1/2,\eta=31/20\), the matrices in RESULT.md have eigenvalues \((-3\pm i\sqrt{91})/20\), both modulus \(1/2\), while their mean transpose-square matrix exceeds \(49I/2\) by a positive-definite matrix (principal minor \(58833/800\), determinant \(1643697/2560000\)). Conditional expectation proves exponential lower growth of expected squared error for all nonzero deterministic starts. The standalone exact-rational verification program checks the matrices, certificate and 1536 additional identities. No numerical check substitutes for the universal proof.

## Originality — PASS (best-knowledge)
The 2024 random-reshuffling-with-momentum paper by Qiu and Milzarek supplies the precise method and its analytical context. The relevant first-version date is 2024-04-29. Full manuscript material on Algorithm 1 and constant-step discussion was read. Wu–Yun–Sra (2023) address single-shuffle/reshuffling separation for batch-normalized, momentum-free SGD; their mathematically different update does not imply the present sharp cyclic heavy-ball criterion or mean-square counterexample. Chen–Bruna (2023) study deterministic nonconvex two-step gradient trajectories. Tran–Nguyen–Tran-Dinh (2021) introduce a distinct epoch-momentum shuffling scheme, but only its abstract was accessible in this comparison. published-finding corpus searches for the precise two-epoch companion product, disconnected learning-rate windows, and frozen-versus-fresh-reshuffling mean-square divergence produced semantically related but not covering claims: momentum-clipped single-loss dynamics, Loopless-SVRG on two quadratics, three-block alternating minimization, and two-coordinate Gauss-Seidel. This is not a claim to universal priority; periodic-coefficient and stochastic-switching linear-systems literature remains a material residual risk.

## Value — PASS
It addresses the natural practical choice between fixing a training permutation and independently redrawing it under the *same* two-gradient budget and the same ordinary momentum algorithm. Exact disconnected safe/fast stepsize regions already warn that homogeneous single-loss tuning may be misleading. More substantially, the rational witness disproves the natural assertion that independently mixing two stable epoch orders must preserve mean-square stability: each frozen order has spectral factor \(1/2\), yet expected squared optimizer-state norm grows by at least \(49/2\) per epoch for every nonzero starting state. The statement is not a claim about almost-sure behavior or more elaborate gradient estimators.

## Sources and residual risk
- Qiu and Milzarek, arXiv:2404.18452 (2024-04-29; revised with Ma later), full relevant algorithm and convergence sections inspected.
- Wu, Yun and Sra, arXiv:2302.12444 (2023), full relevant setup and contrast inspected.
- Chen and Bruna, PMLR 202 (2023), relevant deterministic gradient-dynamics sections inspected.
- Tran, Nguyen and Tran-Dinh, ICML 2021, abstract and bibliographic identification only; distinct algorithm.
- Exact result may have appeared as a period-two switching-matrix or stochastic-heavy-ball theorem under another name. Independent expert/priority validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
