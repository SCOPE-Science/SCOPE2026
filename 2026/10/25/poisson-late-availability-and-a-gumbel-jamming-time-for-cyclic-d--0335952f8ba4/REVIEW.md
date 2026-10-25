# Self-review

## Correctness — PASS
The exactly coupled first-arrival-clock representation is valid because an edge rejected once remains blocked. The boundary-half-line differential equation gives the exact infinite-line available-pair probability \(\exp[-t-2(1-e^{-t})]\). Descending-clock ancestry gives a superpolynomially small probability of dependence beyond radius \(\lceil4\log n\rceil\); its truncated indicators have neighborhood size \(O(\log n)\) and joint bound \(e^{-2t}\). The Arratia–Goldstein–Gordon bound consequently proves the stated \(O(\log n/n)\) total-variation error. Mixed factorial moments of separated rare edges prove spatial Poisson convergence. Jamming is equivalent to zero available pairs. No simulation is used to infer the infinite theorem. A separate finite-generator and first-clock verification script passed 71 bounded checks.

## Originality — PASS relative to inspected literature
The inspected graph-RSA paper of Penrose and Sudbury develops stabilization and fixed-time results; Purvis–Reeve–Wattis–Mao derive near-jamming availability/coverage scaling; Turban evaluates extreme covering times on the fully connected rather than cyclic geometry. Their mathematical statements do not directly assert the finite-cycle late-time Poisson process, logarithmic jamming-time Gumbel centering, or uniform \(O(\log n/n)\) error. published-finding corpus searches for the exact cyclic claim, alias as greedy matching, vacancy method, and Gumbel/Poisson consequences returned no dominating statement. This is a best-knowledge comparison, not a proof of historical priority. Possible unlocated general Poisson/stabilization or rare-event theorem remains the principal risk.

## Mathematical value — PASS
Time until no further dimers can adsorb is a natural finite-system kinetic observable. The theorem determines the entire limiting law, spatial arrangement of last available positions, and an explicit error rate, extending the established one-dimensional mean coverage law into an extreme-time fluctuation regime. This is more than a routine parameter substitution or isolated finite computation.

## Closest literature and limitations
Penrose–Sudbury (2005), arXiv:math/0503519: general graph deposition and local-dependence ideas. Purvis et al. (2015), doi:10.1103/PhysRevE.91.022118: one-dimensional availability and coverage scaling near jamming. Turban (2019), arXiv:1908.00940: full-connectivity covering-time extreme values. Arratia–Goldstein–Gordon (1989), doi:10.1214/aop/1176991491: standard Poisson approximation method. Claim restricted to rate-one dimer adsorption on cycles; a joint multi-time point-process limit and other geometries are unproved. Older specialist work (Pippenger 1989; Burridge–Mao 2004) was not available in full and its implications remain uncertain.

Self-review: passed. Independent audit: not yet performed.
