# Scientific review

## Correctness

**PASS.** The theorem uses one consistent time convention: the selected coordinate is changed at the end of each global step, and occupation sums count spins before that step. The exact identity \(A_i(n)=kT_i(N_i(n))+R_i(n)\) is verified pathwise; its correction is a conditional martingale with diagonal bracket \(k-1\) and off-diagonal bracket \(-X_iX_j\). The cited hypercube weak law implies that off-diagonal brackets vanish in rescaled time. Standard martingale convergence then gives an independent Gaussian correction, while independent embedded elephant invariance principles and uniform multinomial clocks give the other term. Critical \(\sqrt{n\log n}\) and supercritical \(n^{2p_i-1}\) cases are handled separately. The finite checker reproduces 38,687 exact algebraic/path assertions; it is not a substitute for these infinite-time arguments.

## Originality

**PASS, subject to historical-priority uncertainty.** The closest paper is Escobar Parra, arXiv:2607.07022v1, whose bounded-observable weak law is essential here, but whose central limit theorem concerns Doob innovations, not additive occupation. The known one-dimensional elephant functional CLT (Tokumitsu, arXiv:2603.13690v1; Baur–Bertoin, arXiv:1608.01305) covers only the embedded memory term. The dynamic elephant FCLT (Tokumitsu, arXiv:2507.01708v1) uses a different global increment-history model and does not yield the held-spin selector correction by changing parameters. Public mathematical-record and primary-literature comparisons found no same mathematical model joint occupation result with the independent second noise and explicit covariance. A broad older random-clock or additive-functional theorem could implicitly contain this as a specialization; definitive priority is not established.

## Mathematical value

**PASS.** Long-run empirical coordinate occupancy is an intrinsic statistic of the 2026 hypercube memory model. The extra variance \(k-1\) for randomly held spins, the non-Brownian Gaussian covariance away from \(p_i=1/2\), and the three memory regimes at \(p_i=3/4\) resolve a natural gap between occupation laws and Doob-martingale fluctuations. The limiting independence of coordinates despite shared update choices is an additional structural statement with motivation beyond a scalar variance calculation.

## Sources and limitations

Examined material: Escobar Parra (2026), Tokumitsu (2026 and 2025), Baur–Bertoin (2016), and Coletti–Gava–Schütz (2016). The claim is restricted to fixed-dimensional, independently and uniformly selected coordinates, interior memory probabilities, and complete occupation trajectories. No rates, varying-dimensional theorem, or general empirical-process result is claimed. Some general-priority risk remains.

Self-review: passed. Independent audit: not yet performed.
