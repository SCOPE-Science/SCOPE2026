# Scientific review: Weibull-workload/Gamma-duration maximizers

## Correctness — PASS

The stated object is a set of independent jobs with Weibull-distributed workload \(W\) and duration \(L\mid W=w\sim\operatorname{Gamma}(\lceil w\rceil,1)\); it is not a random walk. The proof gives the Weibull top-order scaling \(h_n=(\log n)^{1/\beta}\) and \(b_n=h_n^{1-\beta}/\beta\), then proves a Chernoff-based cutoff excluding all lower-workload intruders for \(\beta\leq1/2\). Its critical marked-Poisson limit and void-probability calculation yield \(p_\star\). For \(\beta>1/2\), exponentially many near-extreme workloads independently have a nonvanishing chance to exceed the workload-maximizing job's duration. Each limiting case is handled without extrapolating finite computation. The independent checker completes 3009 finite checks, including quadrature and an independent truncated Poisson-process simulation. The results are analytical; the checker is auxiliary.

## Originality — PASS (subject to historical-priority risk)

The October 30, 2026 source by Wu (arXiv:2610.41990v1) concerns independent **random-walk excursion** depth/duration marks, with a light-tail versus regularly-varying dichotomy, not independent Weibull workloads and Gamma-service duration. Perfilev–Wachtel (arXiv:1907.02578v1) give a Cramér-regime random-walk excursion local limit, not the claimed extremal agreement classification. David–Galambos examine concomitant asymptotics in a different classical setting, and Basrak–Molchanov–Planinić provide broad marked-Poisson machinery, which may be relevant for a general theorem but does not supply this stated formula in the examined material. A closely related prior finding, an adaptive rank limit for biased-walk excursion depths and durations, has a distinct walk model and a divergent rank, not a Weibull/Gamma half-shape crossover. The new proof uses classical Gaussian, Chernoff and Poisson-limit tools without claiming them new. Full-text and abstract access varied; the possibility of an earlier general concomitant theorem implying the result remains a material historical-priority risk.

## Mathematical value — PASS

The model measures whether the longest stochastic completion time belongs to the largest latent workload when service is made of a random number of phases. This ranking question is motivated by the distinction between longest and deepest excursions, but its precise mechanism is independently natural in queues and stochastic workload scheduling. The exact boundary \(\beta=1/2\) is where extreme-value spacing matches square-root Gamma fluctuation, and its critical probability \(p_\star\approx0.744414083\) is a genuinely nontrivial intermediate value. It also explains *why* similar-looking heavy-tail ranking models can have different winner behavior. No extension to actual walk excursions or arbitrary work/service laws is asserted.

## Closest sources and residual limitations

- Y. Wu, *When is the deepest drawdown also the longest?*, arXiv:2610.41990v1, https://arxiv.org/html/2610.41990v1 (full-text discussion of models, results and concluding limitations).
- E. Perfilev and V. Wachtel, *Local tail asymptotics for the joint distribution of length and of maximum of a random walk excursion*, arXiv:1907.02578v1, https://arxiv.org/html/1907.02578v1 (related conditional excursion fluctuations).
- H. A. David and J. Galambos, *The asymptotic theory of concomitants of order statistics*, https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/asymptotic-theory-of-concomitants-of-order-statistics/0BEA2135DEFD89D7A3AB6B13AED67123 (abstract/bibliographic information only).
- B. Basrak, I. Molchanov and H. Planinić, *Extremal behavior of stationary marked point processes*, https://arxiv.org/abs/2210.01474 (abstract/method comparison; general priority risk).

The principal unproved extension would replace the exact Weibull tail or the independent Gamma service clocks; such extensions are **not** part of the present result. Numerical simulation does not by itself certify convergence.

Self-review: passed. Independent audit: not yet performed.
