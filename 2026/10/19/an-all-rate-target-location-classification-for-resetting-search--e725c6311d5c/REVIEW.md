# Scientific review

## Correctness
**PASS.** A four-lump transient continuous-time generator with absorbing exits exactly represents each nonbridge target. Inverting the generator yields the Laplace transforms \(D(s)/H_m(s)\) and \((n+s)/H_n(s)\); Poisson renewal gives the two claimed mean-time rational functions. The two bridge endpoint cases reduce to a two-state generator and to a constant rate-one hazard. Differentiation produces strict, globally signed derivatives on the whole admissible domain; no numerical extrapolation is needed. The standalone checker passed symbolic identities and 600 full-state generator checks. Rates at every vertex are sums of edge rates (not degree-normalized), and resets are independent Poisson events.

## Originality
**PASS, with bibliographic risk.** The published 2012 arXiv trapping paper studies **unreset, discrete-time** global MFPT and barbell extrema, not this theorem. The 2019/2020 resetting paper presents **general formulas** but a different degree-normalized walk and numerical global barbell search, not the target-by-target edge-clock monotonicity theorem. The 2021 barbell paper uses **hitting-triggered** resets, not independent Poisson resets. A 2023 barbell source addresses centrality-selected reset nodes and global discrete-time means. Relevant mathematical research record searches, alternative descriptors, and recoverable earlier research claims did not exhibit equivalent all-size four-class formulas. Generic renewal/resolvent identities are acknowledged as prior results and not claimed as original. The 2023 full text could not be retrieved through available access despite indexed barbell material; an unidentified earlier exact specialization remains possible.

## Value
**PASS.** For a natural two-community transport network, the target's location—not just the existence of a bottleneck—completely determines the global response to resetting, with no positive interior optimum. The sharp maximal fractional gain \(n/(m+n)\) can approach one as the remote trap-clique grows, while the opposite-clique delay diverges at large reset rate. This explicit robust partition provides finite-network benchmark predictions that are not apparent from numerical averages or generic spectral resolvent formulas.

## Source comparisons and limitations
Primary mathematical content examined: Lin–Julaiti–Zhang arXiv:1209.6165v1, Riascos–Boyer–Herringer–Mateos arXiv:1910.13568v2, and Huang–Chen arXiv:2104.09731v3. Indexed 2023 Entropy barbell material was additionally compared; full-text retrieval encountered access problems. The result does not cover degree-normalized walks, a longer bridge path, other source positions, or non-Poisson resetting.

Self-review: passed. Independent audit: not yet performed.
